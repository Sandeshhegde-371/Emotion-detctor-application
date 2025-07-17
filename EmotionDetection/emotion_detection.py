import requests  
import json

def emotion_detector(text_to_analyse):  
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'  
    myobj = { "raw_document": { "text": text_to_analyse } }  
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"} 
    response = requests.post(url, json = myobj, headers=header) 
    formatted_response = json.loads(response.text)

    prediction = formatted_response['emotionPredictions'][0]  # Access the first element

    anger_score = prediction['emotion']['anger']
    disgust_score = prediction['emotion']['disgust']
    fear_score = prediction['emotion']['fear']
    joy_score = prediction['emotion']['joy']
    sadness_score = prediction['emotion']['sadness']
    
    # Identify the dominant emotion based on max score
    emotion_scores = { 'anger': anger_score, 'disgust': disgust_score,               
           'fear': fear_score, 'joy': joy_score, 'sadness': sadness_score}
    label = max(emotion_scores, key=emotion_scores.get)

    return {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': label
    }


