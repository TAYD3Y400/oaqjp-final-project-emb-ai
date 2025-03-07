'''
This server.py is the main supervisor of connecting the front and backend.
'''
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotions Detector")

@app.route("/", methods=["GET"])
def index():
    '''
    render the index.html template for the frontend
    '''
    return render_template("index.html")

@app.route("/emotionDetector")
def get_emotions():
    '''
    call the previous created function emotion_detector and format the output 
    '''
    input_text = request.args.get("textToAnalyze")

    response = emotion_detector(input_text)

    if response["dominant_emotion"] is None:
        return "Invalid text! Please try again!"

    dominant_emotion = response["dominant_emotion"]
    anger = response["anger"]
    joy = response["joy"]
    disgust = response["disgust"]
    fear = response["fear"]
    sadness = response["sadness"]

    return (f"For the given statement, the system response is: "
                f"anger: {anger}, "
                f"disgust {disgust}, "
                f"fear {fear}, "
                f"joy {joy}, "
                f"sadness {sadness}. "
                f"The dominant emotion is {dominant_emotion}.")

if __name__ == '__main__':
    app.run(debug=True, port=5001)
