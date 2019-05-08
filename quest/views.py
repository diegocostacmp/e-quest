from django.shortcuts import render
import pyrebase

config = {
    'apiKey':               "AIzaSyDbScV081zr7iWPEmiCN9kPi3jeZlgWmTk",
    'authDomain':           "e-quest-aaecf.firebaseapp.com",
    'databaseURL':          "https://e-quest-aaecf.firebaseio.com",
    'projectId':            "e-quest-aaecf",
    'storageBucket':        "e-quest-aaecf.appspot.com",
    'messagingSenderId':    "662995373472"
}
firebase = pyrebase.initialize_app(config)

auth = firebase.auth()

def signIn(request):
    return render(request, 'signIn.html')

def postsign(request):
    email = request.POST.get('email')
    passw = request.POST.get('pass')

    user = auth.sign_in_with_email_and_password(email, passw)

    return render(request, 'welcome.html', {'e':email})