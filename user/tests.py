from django.test import TestCase
from user.models import User

class UserTestCase(TestCase):
  def setUp(self):
    User.objects.create(
      password="TheWorldIsMine1423233",
      username="AliBabaisHere",
      is_superuser=False,
      email="DentistAli@gmail.com",
    )
    User.objects.create(
      password="aVeryPleasentDayInnit",
      username="BenedigtSurgeon",
      is_superuser=False,
      email="BeneDonuts77@gmail.com",
    )
    
  def test_check_creation(self):
    Ali = User.objects.get(username="AliBabaisHere")
    Benedigt = User.objects.get(username="BenedigtSurgeon")
    self.assertEqual(Ali.username, "AliBabaisHere")
