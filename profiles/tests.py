import pytest
from django.test import Client, TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from profiles.models import Profile


@pytest.mark.django_db
class TestProfiles(TestCase):
    client = Client()

    def test_profile_index_view(self):
        url = reverse('profiles:index')
        self.checkAssertion(url, b"Profiles")

    def test_profile_view(self):
        user = User.objects.create(username='OpenClassrooms',
                                   first_name='Open', last_name="Classrooms",
                                   email='openclassrooms@yopmail.com')
        Profile.objects.create(favorite_city='Tanger', user_id=user.id)
        url = reverse('profiles:profile', args=(user.username, ))
        self.checkAssertion(url, b'OpenClassrooms')

    def checkAssertion(self, url, arg1):
        response = self.client.get(url)
        assert arg1 in response.content
        assert response.status_code == 200
