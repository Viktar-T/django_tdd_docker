import json
from unittest.mock import MagicMock

from django.urls import reverse


def test_hello_world():
    assert "hello_world" == "hello_world"
    assert "foo" != "bar"


def test_ping(
    client, monkeypatch
):  # client is a pytest-django helper fixture: instance of django.test.Client.
    # mock_ping = MagicMock()
    # mock_ping.return_value.status_code = 200

    # monkeypatch.setattr("client.get.status_code", mock_ping)

    url = reverse("ping")  # /ping/
    response = client.get(url)
    content = json.loads(response.content)
    assert response.status_code == 200
    assert content["ping"] == "pong!"
