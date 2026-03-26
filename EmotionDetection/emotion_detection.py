import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers =  {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = {"raw_document": { "text": text_to_analyse }}
    response = requests.post(url, json=input_json, headers=headers)
    text = json.loads(response.text)
    if response.status_code == 200:
        anger = text["emotionPredictions"][0]["emotion"]["anger"]
        disgust = text["emotionPredictions"][0]["emotion"]["disgust"]
        fear = text["emotionPredictions"][0]["emotion"]["fear"]
        joy = text["emotionPredictions"][0]["emotion"]["joy"]
        sadness = text["emotionPredictions"][0]["emotion"]["sadness"]
        dominant_emotion_max = max(anger, disgust, fear, joy, sadness)
        dominant_emotion = ""
        if dominant_emotion_max == anger:
            dominant_emotion = "anger"
        elif dominant_emotion_max == disgust:
            dominant_emotion = "disgust"
        elif dominant_emotion_max == fear:
            dominant_emotion = "fear"
        elif dominant_emotion_max == joy:
            dominant_emotion = "joy"
        elif dominant_emotion_max == sadness:
            dominant_emotion = "sadness"

        return {
            "anger": anger,
            "disgust": disgust,
            "fear": fear,
            "joy": joy,
            "sadness": sadness,
            "dominant_emotion": dominant_emotion,
        }
    elif response.status_code == 400:
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None,
        }
    else:
        #This is for the blank entries
        return {"message:":"You have to enter text!"}