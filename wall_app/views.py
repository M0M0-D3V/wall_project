from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from login_app.models import Users
from wall_app.models import Messages, Comments
import bcrypt

# Create your views here.


def index(request):
    if 'first_name' in request.session:
        return render(request, "wall.html")
    else:
        return redirect("/register")

    # [] Display all messages on the main page
    # [] most recent message at the top
    # [] Allow users to post messages
# [] Display all comments per message
# [] oldest comment first
# [] Allow users to comment on each message
# [] NINJA BONUS: Allow users to delete only their own messages
# [] SENSEI BONUS: Allow the user to delete their own messages only if the message was written within the last 30 minutes
