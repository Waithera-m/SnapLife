from django.db import models
from  django.contrib.auth.models import User
import datetime as dt

# Create your models here.
class Profile(models.Model):
    """
    class facilitates the creation of profile objects
    """
    bio = models.CharField(max_length=70)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='profiles/')
    followers = models.ManyToManyField(User, related_name='followers', symmetrical=False)

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
    
    @classmethod
    def get_profile_by_id(cls, id):
        """
        methods gets and returns a profile with a given id
        """
        profile = Profile.objects.get(pk=id)
        return profile
    
    @classmethod
    def get_by_name(cls, name):
        """
        class method facilitates the retrieveal and return of profile objects with the ginven search term
        """
        profile = Profile.objects.filter(user__username__icontains=name)
        return profile

    

class Image(models.Model):
    """
    class facilitates the creation of image objects
    """
    image = models.ImageField(upload_to='images/')
    image_name = models.CharField(max_length=30)
    image_caption = models.CharField(max_length=70)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True, null=True)

    def save_image(self):
        """
        method saves added image object
        """
        self.save()

    def update_image(self, using=None, fields=None, **kwargs):
        """
        method updates saved profile
        """
        if fields is not None:
            fields = set(fields)
            deferred_fields = self.get_deferred_fields()
            if fields.intersection(deferred_fields):
                fields = fields.union(deferred_fields)
        super().refresh_from_db(using, fields, **kwargs)

    def delete_image(self):
        """
        method deletes saved image object
        """
        self.delete()
    
class Comments(models.Model):
    """
    class facilitates the creation of comment objects
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    comment = models.CharField(max_length=100)
    pub_date = models.DateTimeField(auto_now_add=True)

    def save_comment(self):
        """
        method saves added comment
        """
        self.save()
    
    def delete_comment(self):
        """
        method deletes saved comment
        """
        self.delete()
    
    @classmethod
    def get_comments(cls,id):
        """
        method gets comments associated with a given image
        """
        comments =  Comments.objects.filter(image__pk=id)
        return comments

class Like(models.Model):
    """
    class facilitates the creation of like objects
    """
    image = models.ForeignKey(Image, related_name='liked_image', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='liker', on_delete=models.CASCADE)
    date_liked = models.DateTimeField(auto_now_add=True)

