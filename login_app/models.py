from django.db import models
import re
from datetime import date

# Create your models here.


class UsersManager(models.Manager):
    def register_validator(self, postData):
        errors = {}
        # [x] first_name and last_name at least 2 char
        if len(postData['first_name']) < 2:
            errors["first_name"] = "First name should be at least 2 characters"
        if len(postData['last_name']) < 2:
            errors["last_name"] = "Last name should be at least 2 characters"
        # [x] birthday is in past validate
        today = date.today().strftime("%Y-%m-%d")
        dob = postData['birthday']
        if dob > today:
            print(
                f"printing validations for email: postData is: {postData['birthday']} and date comparing to {today}")
            errors["birthday"] = "You're not even born yet."

        # [] check if birthyear is at least 13 years
        # current = date.today()
        # if (dob.year + 13, dob.month, dob.day) < (current.year, current.month, current.day):
        #     errors["birthday"] = "Must be at least 13 years old to register."
        # [x] email address should be valid
        EMAIL_REGEX = re.compile(
            r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        # [x] email address needs to be unique
        check_email = Users.objects.filter(email=postData['email'])
        if check_email:
            errors["email"] = "Email is already registered."
        # test whether a field matches the pattern
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Email address is not in valid format"
        # [x] passwords should match
        # [x] password should be at least 8 char
        if postData['password'] != postData['confirm_password']:
            errors["confirm_password"] = "Password does not match"
        if len(postData['password']) < 8:
            errors["password"] = "Password needs to be at least 8 characters"
        return errors

    def login_validator(self, postData):
        errors = {}
        # [x] email address should be valid
        EMAIL_REGEX = re.compile(
            r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        # test whether a field matches the pattern
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Email address is not in valid format"
        # [x] email address needs to be unique
        check_email = Users.objects.filter(email=postData['email'])
        if not check_email:
            errors["email"] = "Email needs to be registered first."
        # [x] password should be at least 8 char
        if len(postData['password']) < 8:
            errors["password"] = "Password needs to be at least 8 characters"
        return errors


class Users(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=45, blank=False, unique=True)
    password = models.CharField(max_length=255)
    confirm_password = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    birthday = models.DateField()
    objects = UsersManager()

    def __repr__(self):
        return f"User ID:({self.id}): {self.first_name} {self.last_name}"
