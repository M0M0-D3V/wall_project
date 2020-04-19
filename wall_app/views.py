from django.shortcuts import render

# Create your views here.


def wall(request):
    # [] Display all messages on the main page
    # [] most recent message at the top
    # [] Allow users to post messages
    return render(request, "wall.html")

# [] Display all comments per message
# [] oldest comment first
# [] Allow users to comment on each message
# [] NINJA BONUS: Allow users to delete only their own messages
# [] SENSEI BONUS: Allow the user to delete their own messages only if the message was written within the last 30 minutes
