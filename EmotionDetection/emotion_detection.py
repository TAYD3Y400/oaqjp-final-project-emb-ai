import requests
import json

def emotion_detector(text_to_analyse):

    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyse } }

    response = requests.post(url, json=myobj, headers=header)

    if response.status_code == 400:
        return {"anger":None, "disgust":None, "fear":None, "joy":None, "sadness":None, "dominant_emotion":None}

    formatted_response = json.loads(response.text)

    emotions = formatted_response['emotionPredictions'][0]['emotion']

    higher = -1
    higher_label = ""

    for emotion in emotions.keys():
        if emotions[emotion] > higher:
            higher = emotions[emotion]
            higher_label = emotion
            
    emotions["dominant_emotion"] = higher_label

    return emotions

# from emotion_detection import emotion_detector
# emotion_detector("I love this new technology.")