# test_app.py
import pytest
from app import app

@pytest.fixture
def client():
    """Create a test client for the Flask app"""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_homepage(client):
    """Test homepage returns 200 and correct message"""
    response = client.get('/')
    assert response.status_code == 200
    assert b"Halo dari Flask + Docker + Jenkins!" in response.data

def test_homepage_content_type(client):
    """Test homepage returns HTML content"""
    response = client.get('/')
    assert response.content_type == 'text/html; charset=utf-8'

def test_app_is_not_none():
    """Test that Flask app is created successfully"""
    assert app is not None