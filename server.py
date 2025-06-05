"""Flask server app for Emotion Detection Application."""

from flask import Flask, render_template,request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector")
def get_emotion():
    """ 
    This is endpoint for the form submission and 
    analysizing the text send from the client
    using the emotion_detection module
    """
    text_to_analyze = request.args.get("textToAnalyze")
    response = emotion_detector(text_to_analyze)
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']
    return  (
        f"For the given statement, the system response is "
        f"'anger': {anger}, 'disgust': {disgust}, "
        f"'fear': {fear}, 'joy': {joy} and 'sadness': {sadness}. "
        f"The dominant emotion is {dominant_emotion}."
    )

@app.route("/")
def render_index_page():
    """
    This is the endpoint for the base index.html rendering
    """
    return render_template('index.html')

if __name__ == "__main__":
    # Run the Flask app on localhost at port 5000.
    app.run(host="0.0.0.0", port=5000)
