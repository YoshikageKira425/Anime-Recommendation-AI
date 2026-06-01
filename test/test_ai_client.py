import pytest
from src.ai_client import get_recommendation

def test_get_one_recommendation():
    assert get_recommendation("Give one anime title recommendation.") != "Sorry, I couldn't get a recommendation right now."