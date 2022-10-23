from blog.exceptions.user_create_exception import UserCreationException
from blog.models import User
from django.contrib.auth.models import Group


class SignupRepository:
    def signup(self, user_data):
        try:
            if User.objects.filter(email=user_data["email"]):
                raise UserCreationException("The email is already taken")

            user_instance, created = User.objects.get_or_create(
                email=user_data["email"]
            )
            user_instance.email = user_data["email"]
            user_instance.first_name = user_data["first_name"]
            user_instance.last_name = user_data["last_name"]
            # This should be changed so the password is not store in database
            user_instance.password = user_data["password"]
            user_instance.groups = Group.objects.get(name='client')
            user_instance.save()
        except:
            UserCreationException("Sign up failed")



