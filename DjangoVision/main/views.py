from django.shortcuts import render
import pyrebase

config = {
    'apiKey': "AIzaSyD34Sk-s0N7B2cPnb2xHotL1NbyAEYWm04",
    'authDomain': "djangovision-115e0.firebaseapp.com",
    'databaseURL': "https://djangovision-115e0-default-rtdb.firebaseio.com",
    'projectId': "djangovision-115e0",
    'storageBucket': "djangovision-115e0.appspot.com",
    'messagingSenderId': "326790656348",
    'appId': "1:326790656348:web:bf5ff16b913bb2e7e81199",
}

firebase = pyrebase.initialize_app(config)
authe = firebase.auth()
database = firebase.database()

# Create your views here.
def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

def test(request):
    name = database.child('Data').child('Name').get().val()
    description = database.child('Data').child('Project Description').get().val()
    githubLink = database.child('Data').child('GithubLink').get().val()

    return render(request, 'test.html', {
        "name": name,
        "description": description,
        "githubLink": githubLink
    })


