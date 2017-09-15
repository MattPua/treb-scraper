import httplib2
import os
import io
from apiclient import discovery, http, errors

from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage
from config import GOOGLE_CLIENT_SECRET_FILE, GOOGLE_SCOPES, GOOGLE_APPLICATION_NAME, GOOGLE_CREDENTIALS_FILE, FILE_NAME, SHEET_NAME, FILE_MIME_TYPE, IS_CLOUD_SOURCE_OF_TRUE
from apiclient import errors
from apiclient.http import MediaFileUpload, MediaIoBaseDownload

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None


def download_file(service, file_id):
    request = service.files().get_media(fileId=file_id)
    fh = io.BytesIO()
    downloader = MediaIoBaseDownload(fh, request)
    done = False
    while done is False:
        status, done = downloader.next_chunk()
        print "Download %d%%." % int(status.progress() * 100)
    open(FILE_NAME, 'wb').write(fh.getvalue())


def update_file(service, file_id, mime_type, file_name):
    """Update an existing file's metadata and content.

    Args:
        service: Drive API service instance.
        file_id: ID of the file to update.
        mime_type: MIME type for the file.
    Returns:
        Updated file metadata if successful, None otherwise.
    """
    try:
        print 'Saving new data into file...'
        # File's new content.
        media_body = MediaFileUpload(file_name, mimetype=mime_type, resumable=True)
        # Send the request to the API.
        updated_file = service.files().update(
            fileId=file_id,
            body={},
            media_body=media_body).execute()
        return updated_file
    except errors.HttpError, error:
        print 'An error occurred: %s' % error
        return None


def insert_file(service, filename, mime_type):
    """Insert new file.
    Args:
        service: Drive API service instance.
        filename: Title of the file to insert, including the extension.
        parent_id: Parent folder's ID.
        mime_type: MIME type of the file to insert.
    Returns:
        Inserted file metadata if successful, None otherwise.
    """
    media_body = MediaFileUpload(filename, mimetype=mime_type, resumable=True)
    body = {
        'name': filename,
        'mimeType': mime_type
    }
    try:
        file = service.files().create(
            body=body,
            media_body=media_body).execute()

        # Uncomment the following line to print the File ID
        print 'New file: ' + filename + ' created. File ID: %s' % file['id']

        return file
    except errors.HttpError, error:
        print 'An error occurred: %s' % error
        return None


def get_credentials():
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir, GOOGLE_CREDENTIALS_FILE)

    store = Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(GOOGLE_CLIENT_SECRET_FILE, GOOGLE_SCOPES)
        flow.user_agent = GOOGLE_APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else: # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials


"""
    downloads the latest file for the file from Google Drive if exists.
    If found, returns the file object, else None
"""
def get_latest_file_from_drive():
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('drive', 'v3', http=http)

    results = service.files().list().execute()
    items = results.get('files', [])
    if not items:
        print('No existing files found.')
        return None
    else:
        print('Found some files. Checking if ' + FILE_NAME + ' exists...')
        match = next((l for l in items if l['name'] == FILE_NAME), None)
        if match:
            if IS_CLOUD_SOURCE_OF_TRUE:
                print('Found existing file. Downloading file')
                download_file(service, match['id'])
            return match
        else:
            print 'Could not find ' + FILE_NAME + '.'
            return None
    
def saveIntoGoogleDrive(file_object):
    """Shows basic usage of the Google Drive API.

    Creates a Google Drive API service object and outputs the names and IDs
    """
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('drive', 'v3', http=http)

    results = service.files().list().execute()
    items = results.get('files', [])
    if not file_object:
        print('No files found. Creating new excel sheet called ' + FILE_NAME)
        insert_file(service, FILE_NAME,FILE_MIME_TYPE)
    else:
        print('Updating existing file on Drive.')
        update_file(service, file_object['id'], file_object['mimeType'], file_object['name'])

if __name__ == '__main__':
    get_latest_file_from_drive()
