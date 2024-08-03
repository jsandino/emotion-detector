from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/emotionDetector")
def detect_emotion():
    text = request.args["textToAnalyze"]
    if not text:
        return "Required argument missing: 'textToAnalyze'", 400
    
    result = emotion_detector(text)
    if result:
        return summarize(result)
    else:
        return "Invalid text supplied, try something else'", 400


def summarize(data: dict[str, any]):
    emotions = [f"'{k}': {v}" for k, v in data.items() if k != 'dominant_emotion']
    emotions_text = ", ".join(emotions) 
    dominant = data["dominant_emotion"]
    return f'For the given statement, the system response is {emotions_text}. The dominant emotion is <b>{dominant}</b>.'


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)