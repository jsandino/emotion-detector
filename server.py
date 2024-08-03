from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/emotionDetector")
def detect_emotion():
    text = request.args["textToAnalyze"]
    result = emotion_detector(text)
    if not result["dominant_emotion"]:
        return "<b>Invalid text! Please try again!"

    return summarize(result)


def summarize(data: dict[str, any]):
    emotions = [f"'{k}': {v}" for k, v in data.items() if k != 'dominant_emotion']
    emotions_text = ", ".join(emotions) 
    dominant = data["dominant_emotion"]
    return f'For the given statement, the system response is {emotions_text}. The dominant emotion is <b>{dominant}</b>.'


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)