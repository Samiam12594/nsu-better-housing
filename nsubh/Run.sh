#!/bin/sh


# Installs pymongo if not installed already
python -m pip install pymongo

# Create and import NSUBH database and all associated documents
mongoimport --db NSUBH --collection MAK < ./datasets/MAK.json --jsonArray
mongoimport --db NSUBH --collection CLC < ./datasets/CLC.json --jsonArray
mongoimport --db NSUBH --collection FAR < ./datasets/FAR.json --jsonArray
mongoimport --db NSUBH --collection FOU < ./datasets/FOU.json --jsonArray
mongoimport --db NSUBH --collection LGW < ./datasets/LGW.json --jsonArray
mongoimport --db NSUBH --collection ROLL < ./datasets/ROLL.json --jsonArray
mongoimport --db NSUBH --collection VET < ./datasets/VET.json --jsonArray

# Files properly added and welcome message
echo "Files added."
echo "Welcome to NSUBH!"

# Run the NSUBH server
python3 manage.py runserver
chmod +x Run.sh
