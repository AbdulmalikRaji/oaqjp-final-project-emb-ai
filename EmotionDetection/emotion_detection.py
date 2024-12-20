import requests

def emotion_detector(text_to_analyze):
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    Headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyze } }

    resp = requests.post(URL, headers=Headers, json=input_json)

    if resp.status_code == 200:
        output = resp.json()
        emotions = output["emotionPredictions"][0]["emotion"]
        emotions["dominant_emotion"] = max(emotions, key=emotions.get)
        
    elif resp.status_code == 400:
        emotions = {"anger":None,"disgust":None,"dominant_emotion":None,"fear":None,"joy":None,"sadness":None}

    return emotions