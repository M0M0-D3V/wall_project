from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from login_app.models import Users
from wall_app.models import Messages, Comments
import bcrypt

# Create your views here.


def wall(request):
    if 'first_name' in request.session:
        # [] Display all messages from all users on the main page
        # [] most recent message at the top
        # [] each message is clickable to redirect to just that message with relating comments...
        return render(request, "wall.html")
    else:
        return redirect("/register")


def message(request):
    # [x] Allow users to post messages
    # [] process POST and add to message list with user info
    pass


def comment(request):
    # [] Display all comments per message
    # [] oldest comment first
    # [] Allow users to comment on each message
    pass
# [] NINJA BONUS: Allow users to delete only their own messages
# [] SENSEI BONUS: Allow the user to delete their own messages only if the message was written within the last 30 minutes
