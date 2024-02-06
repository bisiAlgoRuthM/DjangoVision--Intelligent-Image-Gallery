from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from django.http import JsonResponse
from django.contrib import messages
import pyrebase
import uuid


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
                    'image_url': image_url,
                    'tags': list(),
                    'description': ''
                })
                return JsonResponse({'success': True, 'message': 'Image upload successful!'})
            else:
                return JsonResponse({'success': False, 'message': 'No image file provided, Try again!'})
    return render(request, 'upload.html')

def gallery(request):
    if request.method == "GET":
        images = database.child('uploaded_images').get().val() 
        return render(request, 'gallery.html', {'images': images})       
       
    
def gallery_detail(request, image_id):
    image_details = database.child('uploaded_images').child(image_id).get().val()
    return render(request, 'gallery_detail.html', {'image_details' : image_details})

def category(request):
    return render(request, 'category.html')

def login(request):

    return render(request, "login.html")

@csrf_protect
def postsign(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('pass')

        try:
            user = authe.sign_in_with_email_and_password(email, password)
            messages.success(request, 'Login successful')
        except:
            message='Invalid credentials'
            return redirect('login', {'message':message} )
        return render(request, "welcome.html",{'e': email})


def welcome(request):
    return render(request, 'welcome.html')


def test(request):
    name = database.child('Data').child('Name').get().val()
    description = database.child('Data').child('Project Description').get().val()
    githubLink = database.child('Data').child('GithubLink').get().val()

    return render(request, 'test.html', {
        "name": name,
        "description": description,
        "githubLink": githubLink
    })


