from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from pymongo import MongoClient
from loginpage.views import loginpage

# Establish connection to database
client = MongoClient("mongodb://localhost:27017")
nsubh = client["NSUBH"]

# Load the review page for a chosen room using login information


@csrf_exempt
def reviewpage(request):
    context = {}
    if request.method == 'POST':
        roomnumber = request.POST.get('R', False)
        bed = request.POST.get('B', False)
        reviewpage.roomnumber = roomnumber
        reviewpage.bed = bed
        # Get login info and pass into HTML file
        context = {
            'username': loginpage.firstname + " " + loginpage.lastname,
            'nnumber': loginpage.nnumber,
            'email': loginpage.email,
            'building': loginpage.building,
            'roomnumber': roomnumber,
            'bed': bed,
        }
    return render(request, 'reviewpage.html', context)
