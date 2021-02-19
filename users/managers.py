from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email, password, **kwargs):
        user = self.model(email=email, is_active=True, **kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **kwargs):
        from users.models import User
        return self.create_user(email, password, user_type=User.SUPERUSER, **kwargs)
