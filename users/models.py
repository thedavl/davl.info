from django.contrib.auth.models import AbstractUser
# Although we don't need any fields to the model itself, 
# we are looking to the future, incase we need to expand 
# the user model

# The abstract user model has all the fields we need, 
# such as name, email, is staff, etc.

class CustomUser(AbstractUser):
    pass


