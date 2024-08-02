import requests
import json
from collections import Counter

def emotion_detector(text_to_analyze):
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    HEADERS = { "grpc-metadata-mm-model-id" : "emotion_aggregated-workflow_lang_en_stock" }
    json = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(URL, headers=HEADERS, json=json)
    result = parse_emotions(response.text)
    return result

def parse_emotions(text: str) -> dict[str, any]:
    data = json.loads(text)
    emotions = data["emotionPredictions"][0]["emotion"]
    dominant, _ = Counter(emotions).most_common(1)[0]
    emotions.update({'dominant_emotion' : dominant})
    return emotions