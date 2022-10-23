from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    def create_superuser(
        self, firebase_uid: str, email: str, password=None, **extra_fields
    ):
        if not email:
            raise ValueError("User must have an email")
        if not password:
            raise ValueError("User must have a password")

        user = self.model(email=self.normalize_email(email))
        user.firebase_uid = firebase_uid
        user.set_password(password)
        user.is_superuser = True
        user.is_staff = True
        user.active = True
        user.save(using=self._db)
        return user
