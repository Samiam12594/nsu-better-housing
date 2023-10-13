#!/bin/sh


# Installs pymongo if not installed already
python -m pip install pymongo

# Create and import NSUBH database and all associated documents
mongoimport --db NSUBH --collection MAK < ../NSUBH/datasets/MAK.json --jsonArray
mongoimport --db NSUBH --collection CLC < ../NSUBH/datasets/CLC.json --jsonArray
mongoimport --db NSUBH --collection FAR < ../NSUBH/datasets/FAR.json --jsonArray
mongoimport --db NSUBH --collection FOU < ../NSUBH/datasets/FOU.json --jsonArray
mongoimport --db NSUBH --collection LGW < ../NSUBH/datasets/LGW.json --jsonArray
mongoimport --db NSUBH --collection ROLL < ../NSUBH/datasets/ROLL.json --jsonArray
mongoimport --db NSUBH --collection VET < ../NSUBH/datasets/VET.json --jsonArray

# Files properly added and welcome message
echo "Files added."
echo "Welcome to NSUBH!"

# Run the NSUBH server
python manage.py runserver
chmod +x Run.sh
