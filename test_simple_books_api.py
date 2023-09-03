import requests
import logging

BASE_URL = "https://simple-books-api.glitch.me"


def test_get_status():
    # Send a GET request to the /status endpoint
    response = requests.get(f"{BASE_URL}/status")

    # Log the request and response
    logging.info(f"Request: {response.request.method} {response.request.url}")
    logging.info(f"Response: {response.status_code} - {response.text}")

    # Perform assertions to check the response status code and content
    assert response.status_code == 200
    assert "OK" in response.text
