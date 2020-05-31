from django.test import TestCase
from .models import Profile, Image
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

class ImageModelTests(TestCase):
    """
    class facilitates the creation of tests to test model's behavior
    """
    def setUp(self):
        """
        method dictates the instructions to be executed before each test
        """
        self.new_user = User(username="peaches", email="njihiamary11@gmail.com", password="somepassword")
        self.new_user.save()
        self.new_profile = Profile(bio="something something scifi", user=self.new_user, profile_pic="tablet.jpg")
        self.new_profile.save()
        self.image = Image(image='tablet.jpg', image_name='tablet', image_caption='random tablet', profile=self.new_profile, likes=0, comments='random comment')
    
    def test_instance(self):
        """
        method checks if objects are initialized properly
        """
        self.assertTrue(isinstance(self.image, Image))
    
    def test_save_image(self):
        """
        method tests if an added image objects is saved to the database
        """
        self.image.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)
    
    def test_update_image(self):
        """
        method test if a saved image object can be updated
        """
        self.image.save_image()
        Image.objects.filter(pk=self.image.pk).update(image_name="random")
        self.image.update_image()
        self.assertEqual(self.image.image_name, 'random')

    def test_delete_image(self):
        """
        method check if a saved image objects can be deleted
        """
        self.image.save_image()
        Image.objects.filter(pk=self.image.pk).delete()
        self.image.delete_image()
        images = Image.objects.all()
        self.assertTrue(len(images) == 0)