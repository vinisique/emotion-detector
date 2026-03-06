from flask import Flask, request
from EmotionDetection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def detect_emotion():

    text = request.args.get('textToAnalyze')

    if text is None or text == "":
        return "Invalid text! Please try again."

    response = emotion_detector(text)

    return str(response)

@app.route("/")
def render_index_page():
    return "Emotion Detection App"

app.run(host="0.0.0.0", port=5000)
