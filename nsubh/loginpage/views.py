from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from pymongo import MongoClient
from homepage import views

# Establish connnection to database
client = MongoClient("mongodb://localhost:27017")
nsubh = client["NSUBH"]

userNameStored = ''
nNumberStored = ''

loginInfo = {}

# Load the loginpage for NSUBH


@csrf_exempt
def loginpage(request):
    # Check the request method
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        error = None
        docUser = None

        logincollection = nsubh['Login']
        userquery = {"Username": username}
        dbUserDocument = logincollection.find_one(userquery)
        # Find if a user exists in the database
        if dbUserDocument:
            docUser = dbUserDocument["Username"]
            docPass = dbUserDocument["Password"]
            docNNumber = dbUserDocument["N Number"]
            docEmail = dbUserDocument["EMail"]
            docFN = dbUserDocument["First Name"]
            docLN = dbUserDocument["Last Name"]

        user = docUser
        passwordChecker = False
        # Checks for incomplete username or password
        if user != username:
            error = 'Incorrect username.'

        elif docPass == password:
            passwordChecker = True

        elif not passwordChecker:
            error = 'Incorrect password.'
        else:
            error = None

        # Store login info if there is a successful login
        if error is None:
            loginInformation = {
                'username': username,
                'nnumber': docNNumber,
            }
            loginpage.user = username
            loginpage.password = password
            loginpage.nnumber = docNNumber
            loginpage.email = docEmail
            loginpage.firstname = docFN
            loginpage.lastname = docLN
            loginpage.building = ''
            return render(request, 'homepage.html', loginInformation)
        else:
            errorInfo = {
                'error': error,
            }
            print(error)
            return render(request, 'loginpage.html', errorInfo)

    return render(request, 'loginpage.html')
