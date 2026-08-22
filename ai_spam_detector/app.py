from flask import Flask, render_template, request
from model import predict_message

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():

    result = None
    confidence = None
    message = ""

    if request.method == "POST":

        message = request.form["message"]

        if message.strip():

            result, confidence = predict_message(message)

    return render_template(
        "index.html",
        result=result,
        confidence=confidence,
        message=message
    )


if __name__ == "__main__":
    app.run(debug=True)