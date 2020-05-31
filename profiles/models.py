from django.db import models
from  django.contrib.auth.models import User
import datetime as dt

# Create your models here.
class Profile(models.Model):
    """
    class facilitates the creation of profile objects
    """
    bio = models.CharField(max_length=70)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='profiles/')
    def __str__(self):
        """
        function returns informal representations of the models' objects
        """
        return self.user

    def save_profile(self):
        """
        method saves entered profiles to the database
        """
        self.save()

    def update_profile(self, using=None, fields=None, **kwargs):
        """
        method updates saved profile
        """
        if fields is not None:
            fields = set(fields)
            deferred_fields = self.get_deferred_fields()
            if fields.intersection(deferred_fields):
                fields = fields.union(deferred_fields)
        super().refresh_from_db(using, fields, **kwargs)

    def delete_profile(self):
        """
        method deletes saved profile
        """
        self.delete()
        