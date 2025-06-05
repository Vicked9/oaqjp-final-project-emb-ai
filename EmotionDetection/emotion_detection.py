import requests
import json

def emotion_detector(text_to_analyze):
    URL= 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    inputs= { "raw_document": { "text": text_to_analyze } }
    response = requests.post(URL,headers=header,json=inputs)
    if response.status_code == 200 :
        formatted_respone = json.loads(response.text)
        emotion = formatted_respone["emotionPredictions"][0]["emotion"]
        anger = emotion['anger']
        disgust = emotion['disgust']
        fear = emotion['fear']
        joy = emotion['joy']
        sadness = emotion['sadness']
        dominant_emotion = max(emotion, key=emotion.get)
        return { 'anger': anger,'disgust': disgust,'fear': fear,'joy': joy,'sadness': sadness,'dominant_emotion': dominant_emotion}
    elif response.status_code == 400:
        return { 'anger': None,
        'disgust': None,
        'fear': None,
        'joy': None,
        'sadness': None,
        'dominant_emotion': None
        }
