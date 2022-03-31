from django.urls import reverse


def test_index_view(client):
    url = reverse('index')
    response = client.get(url)
    assert b'Holiday Homes' in response.content
    assert response.status_code == 200
