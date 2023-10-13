from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from pymongo import MongoClient
from reviewpage.views import reviewpage
from loginpage.views import loginpage

client = MongoClient("mongodb://localhost:27017")
nsubh = client["NSUBH"]

# Load the completion page


@csrf_exempt
def completionpage(request):
    # Check request method, should be POST
    if request.method == 'POST':
        logincollection = nsubh[loginpage.building]
        userquery = {"Bed": reviewpage.bed, "Room": reviewpage.roomnumber}
        dbUserDocument = logincollection.find_one(userquery)
        updatedName = {
            '$set': {"Name": loginpage.firstname + " " + loginpage.lastname}}
        updatedStatus = {'$set': {"Occupied": "T"}}
        # Find the bed in a building to be occupied,
        # update its occupancy status and add the students name
        if dbUserDocument:
            logincollection.update_one(userquery, updatedName)
            logincollection.update_one(userquery, updatedStatus)
    return render(request, 'completionpage.html')
