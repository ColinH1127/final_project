import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json ={ "raw_document": { "text": text_to_analyze } }, headers=header)
    formatted_response = json.loads(response.text)
    anger_score = formatted_response['anger']
    disgust_score = formatted_response['disgust']
    fear_score = formatted_response['fear']
    joy_score = formatted_response['joy']
    sadness_score = formatted_response['sadness']
    scores = [anger_score, disgust_score, fear_score, joy_score, sadness_score]
    dominant_emotion = max(scores)
    return {'anger': anger_score, 'disgust': disgust_score, 'fear': fear_score, 'joy': joy_score, 'sadness': sadness_score, 'dominant_emotion': dominant_emotion}
