import pytest
from django.test import Client, TestCase
from django.urls import reverse
from lettings.models import Letting, Address


@pytest.mark.django_db
class TestLettings(TestCase):
    client = Client()

    def test_letting_index_view(self):
        url = reverse('lettings:index')
        self.checkAssertion(url, b"Lettings")

    def test_letting_view(self):
        address = Address.objects.create(
            number=9, street='Street Name',
            city='Test City',
            state='TS',
            zip_code=12345,
            country_iso_code='XXXXX'
        )
        letting = Letting.objects.create(
            title='Test Title',
            address_id=address.id
        )
        url = reverse('lettings:letting', args=(letting.id,))
        self.checkAssertion(url, b'Test Title')

    def checkAssertion(self, url, arg1):
        response = self.client.get(url)
        assert arg1 in response.content
        assert response.status_code == 200
