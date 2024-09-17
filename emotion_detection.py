import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json=myobj, headers=headers)
    response_data = json.loads(response.text)
    
    # Extract emotions from the correct structure
    emotions = response_data['emotionPredictions'][0]['emotion']
    
    result = {
        'anger': emotions.get('anger', 0),
        'disgust': emotions.get('disgust', 0),
        'fear': emotions.get('fear', 0),
        'joy': emotions.get('joy', 0),
        'sadness': emotions.get('sadness', 0),
    }
    
    # Find the dominant emotion
    dominant_emotion = max(result, key=result.get)
    result['dominant_emotion'] = dominant_emotion
    
    return result

# Test the function
if __name__ == "__main__":
    print(emotion_detector("I am so happy I am doing this."))
