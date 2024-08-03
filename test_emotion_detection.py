import pytest
from EmotionDetection.emotion_detection import parse_emotions, emotion_detector

@pytest.fixture
def sample_data() -> str:
 return '{"emotionPredictions":[{"emotion":{"anger":0.0132405795, "disgust":0.0020517302, "fear":0.009090992, "joy":0.9699522, "sadness":0.054984167}, "target":"", "emotionMentions":[{"span":{"begin":0, "end":26, "text":"I love this new technology"}, "emotion":{"anger":0.0132405795, "disgust":0.0020517302, "fear":0.009090992, "joy":0.9699522, "sadness":0.054984167}}]}], "producerId":{"name":"Ensemble Aggregated Emotion Workflow", "version":"0.0.1"}}'

@pytest.fixture
def expected_parsed_data() -> dict[str, any]:
    return {
        'anger' : 0.0132405795,
        'disgust' : 0.0020517302,
        'fear' : 0.009090992,
        'joy' : 0.9699522,
        'sadness' : 0.054984167,
        'dominant_emotion': 'joy'
    }

@pytest.fixture
def expected_emotion_keys() -> tuple[str]:
    return ('anger', 'disgust', 'fear', 'joy', 'sadness', 'dominant_emotion')

def test_parse_emotions(sample_data, expected_parsed_data):
    assert expected_parsed_data == parse_emotions(sample_data)

def test_emotion_detector_result_keys(expected_emotion_keys):
    result = emotion_detector("I love this technology")
    for emotion_key in expected_emotion_keys:
        assert emotion_key in result

def test_emotion_detector_yields_joy():
    result = emotion_detector("I am glad this happened")
    assert "joy" == result["dominant_emotion"]
    
def test_emotion_detector_yields_anger():
    result = emotion_detector("I am really mad about this")
    assert "anger" == result["dominant_emotion"]

def test_emotion_detector_yields_disgust():
    result = emotion_detector("I feel disgusted just hearing about this")
    assert "disgust" == result["dominant_emotion"]

def test_emotion_detector_yields_sadness():
    result = emotion_detector("I am so sad about this")
    assert "sadness" == result["dominant_emotion"]

def test_emotion_detector_yields_fear():
    result = emotion_detector("I am really afraid that this will")

def test_emotion_detector_with_blank_text(expected_emotion_keys):
    expected_data = {k:None for k in expected_emotion_keys}
    assert expected_data == emotion_detector("")