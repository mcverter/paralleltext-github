"""
models.py defines the data and behavior that is being stored in the database.
The register models contains how the user account information should be stored.
"""
from django.db import models
from django.contrib.auth.models import User
from languages.models import Languages

class UserAccount(models.Model):
    """
    UserAccount stores the account settings for the user.
    This is an extension of the user_auth table in the database.
    """
    user = models.ForeignKey(User, unique=True)
    is_contentmgr = models.BooleanField(default=False)
    native_lang = models.ForeignKey(Languages)
    #learn_lang = models.ForeignKey(Languages)

