from django.test import TestCase
from django.contrib.auth import  get_user_model


class ModelTes(TestCase):
    def test_user_created(self):
        """Test using a new user with email"""
        
        email = "test@gmail.com"
        password = "test123"

        # Creating user
        user = get_user_model().objects.create_user(
            
            email = email,
            password = password
        )

        # Test email and password
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test the new user email is normalized"""
        email = "test@GMAIL.COM"
        user = get_user_model().objects.create_user(email,"test@123")

        self.assertEqual(user.email,email.lower())
    
    def test_new_user_invalid_email(self):
        
        """Test creating user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')