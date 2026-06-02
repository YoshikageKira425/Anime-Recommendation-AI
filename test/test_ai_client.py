import pytest
from src.ai_client import send_to_ai

def test_get_one_recommendation():
    assert send_to_ai("Give one anime title recommendation.") != "Sorry, I couldn't get a recommendation right now."