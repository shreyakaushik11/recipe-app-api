from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email is successful"""
        email = 'test@github.com'
        password = 'Testpass123'

        #calling the user function on the user manager for our user model 
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        #checking if the email in our created user equals the email we passed in
        self.assertEqual(user.email, email)
        """the check_password function is a helper function that comes with the Django
        user model and it returns true if the password is correct or false if it's
        not correct"""
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test the email for a new user is normalized"""
        email = 'test@GITHUB.COM'

        """added a random string for password since we've already
        tested the password"""
        user = get_user_model().objects.create_user(email, 'test123')
        
        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')