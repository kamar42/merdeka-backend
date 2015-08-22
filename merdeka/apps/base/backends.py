from .models import *

class CustomMyUserBackend(object):
    """
    Authenticating using username or email
    """

    def authenticate(self, username=None, password=None):
        # check if it's an email or not
        if '@' in username:
            kwargs = {'email': username}
        else:
            kwargs = {'username': username}

        # try to authenticate
        try:
            user = MyUser.objects.get(**kwargs)
            if user.check_password(password):
                return user
        except MyUser.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return MyUser.objects.get(pk=user_id)
        except MyUser.DoesNotExist:
            return None
