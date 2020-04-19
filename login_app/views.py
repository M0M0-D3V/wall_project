from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from login_app.models import Users
import bcrypt


def index(request):
    # [x] root render where users can register or login
    # [] context to hold session stuff
    # if request.session:
    #     return redirect("/success")
    # request.session['first_name'] = ''
    return render(request, "index.html")


def register(request):
    # [x] set basic validator
    errors = Users.objects.register_validator(request.POST)
    #
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
    # [x] if errors go back to register with messages
        return redirect("/")
    else:
        # [x] success only when errors = 0
        # [x] receive post information
        first_name = request.POST['first_name']
        request.session['first_name'] = first_name
        last_name = request.POST['last_name']
        birthday = request.POST['birthday']
        email = request.POST['email']

        password = request.POST['password']
        # [x] create hash for pw
        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        print(f"pw hash: {pw_hash}")
        confirm_password = request.POST['confirm_password']
        # [x] create user
        Users.objects.create(first_name=first_name, last_name=last_name,
                             birthday=birthday, email=email, password=pw_hash)

        messages.success(request, "Successfully registered!")
        return redirect("/success")


def login(request):
    errors = Users.objects.login_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect("/")

    user = Users.objects.filter(email=request.POST['email'])
    if user:
        logged_user = user[0]
        if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
            request.session['first_name'] = logged_user.first_name
            messages.success(request, "Successfully logged in!")
            return redirect("/success")
    else:
        messages.error(request, "Password did not match")
    return redirect("/")


def success(request):
    if request.session['first_name'] == '':
        return redirect("/")
    else:
        context = {
            "first_name": request.session['first_name']
        }
        return redirect("/wall")
        # return render(request, "success.html", context)


def logout(request):
    request.session.clear()
    return redirect("/")
