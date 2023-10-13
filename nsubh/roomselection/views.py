from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from pymongo import MongoClient
from loginpage.views import loginpage

# Establish connection to database
client = MongoClient("mongodb://localhost:27017")
nsubh = client["NSUBH"]

# Load Mako. Check if any beds are occupied from database collection


def makoRS(request):
    context = {}
    loginpage.building = 'MAK'
    mkh = nsubh[loginpage.building]
    cursor = mkh.find({})
    occupiedBeds = []
    for document in cursor:
        roomNumber = document['Room']
        bedType = document['Bed']
        if document['Occupied'] == 'T':
            print(roomNumber + '' + bedType)
            occupiedBeds.append(roomNumber + "" + bedType)
    context = {
        "occupiedrooms": occupiedBeds,
        "firstname": loginpage.firstname,
        "lastname": loginpage.lastname,
        "nnumber": loginpage.nnumber,
    }
    return render(request, 'makors.html', context)

# Load Commons. Check if any beds are occupied from database collection


def commonsRS(request):
    context = {}
    loginpage.building = 'COM'
    mkh = nsubh[loginpage.building]
    cursor = mkh.find({})
    occupiedBeds = []
    for document in cursor:
        roomNumber = document['Room']
        bedType = document['Bed']
        if document['Occupied'] == 'T':
            occupiedBeds.append(roomNumber + "" + bedType)
    context = {
        "occupiedrooms": occupiedBeds,
        "firstname": loginpage.firstname,
        "lastname": loginpage.lastname,
        "nnumber": loginpage.nnumber,
    }
    return render(request, 'commonsrs.html', context)

# Load Leogoodwin. Check if any beds are occupied from database collection


def leogoodwinRS(request):
    context = {}
    loginpage.building = 'LGW'
    mkh = nsubh[loginpage.building]
    cursor = mkh.find({})
    occupiedBeds = []
    for document in cursor:
        roomNumber = document['Room']
        bedType = document['Bed']
        if document['Occupied'] == 'T':
            occupiedBeds.append(roomNumber + "" + bedType)
    context = {
        "occupiedrooms": occupiedBeds,
        "firstname": loginpage.firstname,
        "lastname": loginpage.lastname,
        "nnumber": loginpage.nnumber,
    }
    return render(request, 'leogoodwinrs.html', context)

# Load Farquhar. Check if any beds are occupied from database collection


def farquharRS(request):
    context = {}
    loginpage.building = 'FAR'
    mkh = nsubh[loginpage.building]
    cursor = mkh.find({})
    occupiedBeds = []
    for document in cursor:
        roomNumber = document['Room']
        bedType = document['Bed']
        if document['Occupied'] == 'T':
            occupiedBeds.append(roomNumber + "" + bedType)
    context = {
        "occupiedrooms": occupiedBeds,
        "firstname": loginpage.firstname,
        "lastname": loginpage.lastname,
        "nnumber": loginpage.nnumber,
    }
    return render(request, 'farquharrs.html', context)

# Load Founders. Check if any beds are occupied from database collection


def foundersRS(request):
    context = {}
    loginpage.building = 'FOU'
    mkh = nsubh[loginpage.building]
    cursor = mkh.find({})
    occupiedBeds = []
    for document in cursor:
        roomNumber = document['Room']
        bedType = document['Bed']
        if document['Occupied'] == 'T':
            occupiedBeds.append(roomNumber + "" + bedType)
    context = {
        "occupiedrooms": occupiedBeds,
        "firstname": loginpage.firstname,
        "lastname": loginpage.lastname,
        "nnumber": loginpage.nnumber,
    }
    return render(request, 'foundersrs.html', context)

# Load Vettel. Check if any beds are occupied from database collection


def vettelRS(request):
    context = {}
    loginpage.building = 'VET'
    mkh = nsubh[loginpage.building]
    cursor = mkh.find({})
    occupiedBeds = []
    for document in cursor:
        roomNumber = document['Room']
        bedType = document['Bed']
        if document['Occupied'] == 'T':
            occupiedBeds.append(roomNumber + "" + bedType)
    context = {
        "occupiedrooms": occupiedBeds,
        "firstname": loginpage.firstname,
        "lastname": loginpage.lastname,
        "nnumber": loginpage.nnumber,
    }
    return render(request, 'vettelrs.html', context)

# Load CLC. Check if any beds are occupied from database collection


def clcRS(request):
    context = {}
    loginpage.building = 'CLC'
    mkh = nsubh[loginpage.building]
    cursor = mkh.find({})
    occupiedBeds = []
    for document in cursor:
        roomNumber = document['Room']
        bedType = document['Bed']
        if document['Occupied'] == 'T':
            occupiedBeds.append(roomNumber + "" + bedType)
    context = {
        "occupiedrooms": occupiedBeds,
        "firstname": loginpage.firstname,
        "lastname": loginpage.lastname,
        "nnumber": loginpage.nnumber,
    }
    return render(request, 'clcrs.html', context)

# Load Rolling. Check if any beds are occupied from database collection


def rollingRS(request):
    context = {}
    loginpage.building = 'ROLL'
    mkh = nsubh[loginpage.building]
    cursor = mkh.find({})
    occupiedBeds = []
    for document in cursor:
        roomNumber = document['Room']
        bedType = document['Bed']
        if document['Occupied'] == 'T':
            occupiedBeds.append(roomNumber + "" + bedType)
    context = {
        "occupiedrooms": occupiedBeds,
        "firstname": loginpage.firstname,
        "lastname": loginpage.lastname,
        "nnumber": loginpage.nnumber,
    }
    return render(request, 'rollingrs.html', context)
