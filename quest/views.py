from django.shortcuts import render
import pyrebase

from django.contrib import auth

config = {
    'apiKey':               "AIzaSyDbScV081zr7iWPEmiCN9kPi3jeZlgWmTk",
    'authDomain':           "e-quest-aaecf.firebaseapp.com",
    'databaseURL':          "https://e-quest-aaecf.firebaseio.com",
    'projectId':            "e-quest-aaecf",
    'storageBucket':        "e-quest-aaecf.appspot.com",
    'messagingSenderId':    "662995373472"
}
firebase = pyrebase.initialize_app(config)

authe = firebase.auth()
database = firebase.database()

def signIn(request):
    return render(request, 'signIn.html')

# autenticacao via firebase
def postsign(request):
    email = request.POST.get('email')
    passw = request.POST.get('pass')

    try:
        user = authe.sign_in_with_email_and_password(email, passw)
    except:
        message = 'Credenciais Invalidas!'
        return render(request, 'signIn.html', {'msg': message})
    print('Token de acesso: \n', user['idToken'])
    session_id=user['idToken']  
    request.session['uid']=str(session_id)  

    return render(request, 'welcome.html', {'e':email})

def logout(request):
    auth.logout(request)
    return render(request, 'signIn.html')

def signup(request):
    return render(request, 'signup.html')

def postsignup(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    passw = request.POST.get('pass')

    print(email)
    print(passw)
    try:
        user=authe.create_user_with_email_and_password(email,passw)
        uid = user['localId']
        data={"name":name, "status":"1"}
        database.child("users").child(uid).child("details").set(data)
    except:
        message='Nao foi possivel criar a conta!'
        return render(request, 'signup.html', {'msg':message})
    
    return render(request, 'signIn.html')

def create(request):
    
    return render(request, 'create.html')

def post_create(request):
    import time 
    from datetime import datetime, timezone
    import pytz

    tz = pytz.timezone('Asia/Kolkata')
    time_now = datetime.now(timezone.utc).astimezone(tz)
    millis = int(time.mktime(time_now.timetuple()))

    work = request.POST.get('work')
    progress = request.POST.get('progress')

    data = {
        'work': work,
        'progress': progress
    }
    return render(request, 'welcome.html')