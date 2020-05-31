from django.test import TestCase
from .models import Profile
from django.contrib.auth.models import User

# Create your tests here.
class  ProfileModelTests(TestCase):
    """
    class facilitates the creation of test units to test profile model's behavior
    """
    def setUp(self):
        """
        method defines the instructions to be executed before each test
        """
        self.new_user = User(username="peaches", email="njihiamary11@gmail.com", password="somepassword")
        self.new_user.save()
        self.new_profile = Profile(bio="something something scifi", user=self.new_user, profile_pic="tablet.jpg")
    
    def test_instance(self):
        """
        method checks if model's objesct are initialized properly
        """
        self.assertTrue(isinstance(self.new_profile, Profile))

    def test_save_profile(self):
        """
        test unit tests if the model's object are saved to the database
        """
        self.new_profile.save_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) > 0)
    
    def test_update_profile(self):
        """
        method tests model's update profile functionality
        """
        self.new_profile.save_profile()
        Profile.objects.filter(pk=self.new_profile.pk).update(bio="randomness")
        self.new_profile.update_profile()
        self.assertEqual(self.new_profile.bio, 'randomness')
    
    def test_delete_profile(self):
        """
        method tests model's delete functionality
        """
        self.new_profile.save_profile()
        Profile.objects.filter(pk=self.new_profile.pk).delete()
        self.new_profile.delete_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) == 0)