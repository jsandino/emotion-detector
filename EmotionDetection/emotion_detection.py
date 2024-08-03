import requests
import json
from collections import Counter

EMPTY_RESULT = {k:None for k in ('anger', 'disgust', 'fear', 'joy', 'sadness', 'dominant_emotion') }

def emotion_detector(text_to_analyze):
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    HEADERS = { "grpc-metadata-mm-model-id" : "emotion_aggregated-workflow_lang_en_stock" }
    json = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(URL, headers=HEADERS, json=json)
    if response.status_code == 400:
        return EMPTY_RESULT

    result = parse_emotions(response.text)
    return result

def parse_emotions(text: str) -> dict[str, any]:
    data = json.loads(text)
    emotions = data["emotionPredictions"][0]["emotion"]
    dominant, _ = Counter(emotions).most_common(1)[0]
    emotions.update({'dominant_emotion' : dominant})
    return emotions