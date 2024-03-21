from django.test import TestCase
from django.contrib.auth.models import User



# Create your tests here.
def add(a,b):
    return a+b

class Usertest(TestCase):

    def test_add(self):  # we want to create test function should compulsory to add before function test keyword  
        self.assertEqual(add(5,5),10)

    def setUp(self):
       self.user=User.objects.create(username="TestUser",first_name="TestfName",last_name="TestlName",email="TestUser@gmail.com",password="User123")
    
    def test_create_user(self):
        user=User.objects.get(username="TestUser")
        self.assertEqual(user.username,self.user.username)

    def test_update_user(self):
        user=User.objects.get(username="TestUser")
        oldEmail=user.email
        user.email="updatedemail@email.com"
        user.save()

        user=User.objects.get(username="TestUser")
        self.assertNotEqual(oldEmail,user.email)


