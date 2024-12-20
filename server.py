''' Server file for final project'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Final project")

@app.route("/emotionDetector")
def emot_detector():
    '''
    function to run emotion detection on some text
    '''
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the emotion detector function and store the response
    response = emotion_detector(text_to_analyze)

    # Return a formatted response
    if response["dominant_emotion"]:
        return response
    return "Invalid text! Please try again!."

@app.route("/")
def render_index_page():
    '''
    function to run render index page
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
