"""
Emotion Detection Web Application

This module implements a Flask web server that provides an API
for detecting emotions in text using the EmotionDetection package.
"""

from flask import Flask, render_template, request, jsonify
from EmotionDetection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/")
def render_index_page():
    """
    Renders the main page of the application.

    Returns:
        HTML content of the index page.
    """
    return render_template('index.html')

@app.route("/emotionDetector", methods=['POST'])
def emotion_detector_route():
    """
    API endpoint that performs emotion detection on submitted text.

    This function receives text via a POST request, processes it using
    the emotion_detector function, and returns a formatted response.

    Returns:
        JSON response containing the formatted emotion analysis.
    """
    # Get the text from the request
    text_to_analyze = request.json.get('text')

    # Call the emotion_detector function
    result = emotion_detector(text_to_analyze)

    # Format the response as specified
    formatted_response = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, 'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, 'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. The dominant emotion is "
        f"{result['dominant_emotion']}."
    )

    return jsonify({"response": formatted_response})

if __name__ == "__main__":
    app.run(host="localhost", port=5001)