
# General 

# Server
SERVER_PORT = 8080
SERVER_HOST = '0.0.0.0'

# Should allow saving to Google Drive or not
ENABLE_CLOUD_SAVING = True

# Whether or not we should let the file on the Cloud be the Source of Truth for the file
IS_CLOUD_SOURCE_OF_TRUE = False

# Application
FILE_NAME = 'listings.xlsx'
FILE_MIME_TYPE='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
SHEET_NAME = 'Listings'
CATEGORIES = [
    '#',
    'address',
    'unit',
    'city',
    'prov',
    'postal',
    'salesStatus',
    'listPr',
    'downPayment',
    'mortgageAmt',
    'estMonthlyMortgage',
    'maintenance',
    'taxes',
    'taxesPerMonth',
    'taxYear',
    'lastStatus',
    'unitType',
    'unitType2',
    'lockerNum',
    'lockerLevel',
    'lockerUnit',
    'floorNum',
    'unitNum',
    'roomCount',
    'bedroomCount',
    'washroomCount',
    'washroomTypes',
    'crossSt',
    'mlsNum',
    'possessionDate',
    'numKitchens',
    'hasBasement',
    'hasFireplace',
    'heatType',
    'approxAge',
    'approxSqFeet',
    'sqftSource',
    'unitDirection',
    'pets',
    'locker',
    'airCon',
    'taxesIncl',
    'waterIncl',
    'heatIncl',
    'hydroIncl',
    'cablTvIncl',
    'centralAirCon',
    'buildingInsurIncl',
    'parkingIncl',
    'balconyType',
    'ensuiteLaundry',
    'exterior',
    'garage',
    'parking',
    'parkType',
    'parkSpaces',
    'totalParkSpots',
    'parkSpotNum',
    'parkPerMonth',
    'parkLevel',
    'commonElemIncl',
    'textDescriptions',
    'dateAdded'
]
SHEET_MLS_INDEX_NUM = CATEGORIES.index('mlsNum') + 1


# Google API Specific
GOOGLE_SCOPES = 'https://www.googleapis.com/auth/drive.file'
GOOGLE_CLIENT_SECRET_FILE = 'client_secret.json'
GOOGLE_APPLICATION_NAME = 'Treb-Web-Scraper-Drive'
GOOGLE_CREDENTIALS_FILE = GOOGLE_APPLICATION_NAME+'.json'


# Mortgage Calculator Specific
MORTGAGE_INTEREST_RATE=2.99
MORTGAGE_LOAN_YEARS=25
MORTGAGE_LOAN_MONTHS=None
MORTGAGE_DOWNPAYMENT_PERCENTAGE=20