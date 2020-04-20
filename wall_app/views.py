from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from login_app.models import Users
from wall_app.models import Messages, Comments
import bcrypt

# Create your views here.

# USERFUL SESSION INFO:
# request.session['first_name']
# request.session['user_id']


def wall(request):
    print(f"in the wall function....")
    if 'user_id' in request.session:
        # [] Display all messages from all users on the main page
        user_id = request.session['user_id']
        print(f"what's in user_id: {user_id}")
        user = Users.objects.get(id=user_id)
        all_messages = Messages.objects.all()
        all_users = Users.objects.all()
        print(f"printing what's in all_messages: {all_messages}")
        # [] most recent message at the top
        # [] each message is clickable to redirect to just that message with relating comments in /wall...
        context = {
            "all_messages": all_messages, "user": user, "all_users": all_users
        }
        return render(request, "index.html", context)
    else:
        return redirect("/register")


def new_message(request):
    # [x] Allow users to post messages
    # [x] process POST and add to message list with user info
    print(f"in the new message function! let's try to print from here")
    user_id = request.session['user_id']
    print(f"user_id is: {user_id}")
    this_user = Users.objects.get(id=user_id)
    message = request.POST['message']
    new_message = Messages.objects.create(message=message, user=this_user)
    print(f"printing new message: {new_message}")
    return redirect("/")


def this_message(request, user_id, message_id):
    context = {}
    return render(request, "wall.html", context)


def comment(request):
    # [] Display all comments per message
    # [] oldest comment first
    # [] Allow users to comment on each message
    pass
# [] NINJA BONUS: Allow users to delete only their own messages
# [] SENSEI BONUS: Allow the user to delete their own messages only if the message was written within the last 30 minutes
