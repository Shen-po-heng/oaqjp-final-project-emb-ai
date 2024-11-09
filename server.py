"""
Flask web server for emotion detection using the EmotionDetection package.

Author: Po 
Date: 2024-11-09
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("emotion_detector")

@app.route("/emotionDetector", methods=['GET', 'POST'])
def sent_analyzer():
    """
    Analyze the sentiment of the given text.

    Returns:
        str: Emotion analysis result or error message.
    """
    text_to_analyze = request.args.get('textToAnalyze')

    if not text_to_analyze:
        return "Invalid input! Please provide text to analyze."

    response = emotion_detector(text_to_analyze)

    if response is None:
        return "Invalid text! Please try again!"

    return f"For the given statement, the system response is {response}"

@app.route("/")
def render_index_page():
    """
    Render the index page.

    Returns:
        HTML: The rendered index page.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
