import pytest
from server import summarize

@pytest.fixture
def data() -> dict[str, any]:
    return {
        'anger' : 0.0132405795,
        'disgust' : 0.0020517302,
        'fear' : 0.009090992,
        'joy' : 0.9699522,
        'sadness' : 0.054984167,
        'dominant_emotion': 'joy'
    }

@pytest.fixture
def emotions() -> str:
    return "'anger': 0.0132405795, 'disgust': 0.0020517302, 'fear': 0.009090992, 'joy': 0.9699522, 'sadness': 0.054984167"

def test_summarize(emotions, data):
    expected_text = f"For the given statement, the system response is {emotions}. The dominant emotion is <b>joy</b>."
    assert expected_text == summarize(data)