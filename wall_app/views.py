from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from login_app.models import Users
from wall_app.models import Messages, Comments
import bcrypt

# Create your views here.

# USERFUL SESSION INFO:
# request.session['first_name']
# request.session['user_id']


def index(request):
    if 'user_id' in request.session:
        # [x] Display all messages from all users on the main page
        user_id = request.session['user_id']
        # print(f"what's in user_id: {user_id}")
        user = Users.objects.get(id=user_id)
        all_messages = Messages.objects.all()
        all_users = Users.objects.all()
        # print(f"printing what's in all_messages: {all_messages}")
        # [x] most recent message at the top
        # [] each message is clickable to redirect to just that message with relating comments in /wall...
        context = {
            "all_messages": all_messages, "user": user, "all_users": all_users
        }
        return render(request, "wallindex.html", context)
    else:
        return redirect("/register")


def new_message(request):
    # [x] Allow users to post messages
    # [x] process POST and add to message list with user info
    # print(f"in the new message function! let's try to print from here")
    user_id = request.session['user_id']
    this_user = Users.objects.get(id=user_id)
    message = request.POST['message']
    Messages.objects.create(message=message, user=this_user)
    return redirect("/")


def this_message_on_wall(request):
    user_id = request.session['user_id']
    # print(f"what's in user_id: {user_id}")
    this_user = Users.objects.get(id=user_id)
    all_messages = Messages.objects.all()
    all_users = Users.objects.all()
    all_comments = Comments.objects.all()
    # print(f"printing what's in all_messages: {all_messages}")
    # [x] most recent message at the top
    # [x] each message is clickable to redirect to just that message with relating comments in /wall...
    context = {
        "all_messages": all_messages, "this_user": this_user, "all_users": all_users, "all_comments": all_comments
    }
    return render(request, "wall.html", context)


def new_comment(request):
    # [X] Display all comments per message
    # [x] oldest comment first
    # [x] Allow users to comment on each message
    print(f"in the new comment function! let's try to print from here")
    user_id = request.session['user_id']
    print(f"user_id is: {user_id}")
    this_user = Users.objects.get(id=user_id)
    comment = request.POST['comment']
    message_id = request.POST['message_id']
    this_message = Messages.objects.get(id=message_id)
    new_comment = Comments.objects.create(
        comment=comment, user=this_user, message=this_message)
    # print(f"printing new comment: {new_comment}")
    return redirect("/wall")
# [] NINJA BONUS: Allow users to delete only their own messages
# [] SENSEI BONUS: Allow the user to delete their own messages only if the message was written within the last 30 minutes
