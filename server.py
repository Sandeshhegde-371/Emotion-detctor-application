"""
Flask server for Watson NLP Emotion Detection App.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector")
def sent_analyzer():
    """
    Endpoint to analyze user input text and return emotion scores.
    Returns an error message if the input is invalid.
    """
    text_to_analyze = request.args.get('textToAnalyze')

    response = emotion_detector(text_to_analyze)

    if response["dominant_emotion"] is None:
        return "Invalid text! Please try again!"

    anger_score = response['anger']
    disgust_score = response['disgust']
    fear_score = response["fear"]
    joy_score = response["joy"]
    sadness_score = response["sadness"]
    label = response["dominant_emotion"]

    return (
        "The given text has emotion scores: "
        "anger = {}, disgust = {}, fear = {}, joy = {}, sadness = {}. "
        "The dominant emotion is '{}'.".format(
            anger_score, disgust_score, fear_score,
            joy_score, sadness_score, label
        )
    )

@app.route("/")
def render_index_page():
    """
    Renders the index HTML page.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
