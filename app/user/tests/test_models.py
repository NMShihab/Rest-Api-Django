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

