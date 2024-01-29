from django.shortcuts import render
from django.http import JsonResponse
import pyrebase
import uuid
import os


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
storage = firebase.storage()

# Create your views here.
def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

def upload(request):
    if request.method == 'POST':
        if 'image' in request.FILES:
            image = request.FILES['image']

            if image:
                filename = f"uploads/{str(uuid.uuid1())}_{image.name}"
                storage.child(filename).put(image)
                image_url = storage.child(filename).get_url(None)

                database.child('uploaded_images').push({
                    'filename' : filename,
                    'image_url': image_url
                })
                return JsonResponse({'success': True, 'message': 'Image upload successful!'})
            else:
                return JsonResponse({'success': False, 'message': 'No image file provided, Try again!'})
    return render(request, 'upload.html')
        



def signIn(request):

    return render(request, "login.html")

def postsign(request):
    return render(request, "welcome.html")

def test(request):
    name = database.child('Data').child('Name').get().val()
    description = database.child('Data').child('Project Description').get().val()
    githubLink = database.child('Data').child('GithubLink').get().val()

    return render(request, 'test.html', {
        "name": name,
        "description": description,
        "githubLink": githubLink
    })


