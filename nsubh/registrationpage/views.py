import datetime
import dbm
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from pymongo import MongoClient
from loginpage import views
from django.views.decorators.csrf import csrf_exempt

# Initializing Database
USERNAME = ''
client = MongoClient("mongodb://localhost:27017")
nsubh = client["NSUBH"]


@csrf_exempt
def register(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        nnumber = request.POST['n#']
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        year = request.POST.get('year', False)
        error = None

        # Checks if username or password are missing
        if not username:
            error = "Username is required."
        elif not password:
            error = "Password is required."

        # If no error, upload the info to mongoDB
        if error is None:
            logincollection = nsubh["Login"]
            USERNAME = username
            information = {
                "First Name": firstname,
                "Last Name": lastname,
                "N Number": nnumber,
                "Username": username,
                "Password": password,
                "EMail": email,
                "Year": year,
                "Date Created": datetime.datetime.utcnow()
            }
            logininfo = logincollection.insert_one(information)
            print("Inserted")
            return render(request, 'loginpage.html')

    return render(request, 'registrationpage.html')
