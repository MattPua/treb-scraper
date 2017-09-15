#!/bin/bash
sudo apt install virtualenv
sudo apt install python-minimal
virtualenv env
source env/bin/activate
pip install --upgrade -r requirements.txt