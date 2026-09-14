# AI Spam Detector

A small Flask web application that classifies a message as `spam` or `normal` using a TF-IDF text vectorizer and a Multinomial Naive Bayes classifier.

## End-to-End Architecture

```text
Browser
	|
	| GET / - display the form
	| POST / - submit a message
	v
Flask application (ai_spam_detector/app.py)
	|
	| Reads the form field named "message"
	v
Prediction module (ai_spam_detector/model.py)
	|
	| 1. Convert the message to TF-IDF features
	| 2. Run the trained MultinomialNB model
	| 3. Calculate the highest class probability
	v
Flask template (ai_spam_detector/templates/index.html)
	|
	| Render the classification and confidence percentage
	v
Browser result page
```

### Request and prediction flow

1. The user opens `/` and Flask renders the message form.
2. The user submits a message with a `POST` request.
3. The route reads `request.form["message"]` and ignores blank input.
4. `predict_message()` transforms the text with the fitted `TfidfVectorizer`.
5. `MultinomialNB` predicts the class and returns its highest probability.
6. Flask passes `result`, `confidence`, and the submitted `message` to the template.
7. The template displays either a spam or normal result with the confidence percentage.

## Requirements

- Python 3.9 or newer
- `pip`
- A virtual environment is recommended

## Setup and Run

From the project root:

### Windows PowerShell

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
python ai_spam_detector\app.py
```

Open <http://127.0.0.1:5000> in a browser.

If PowerShell blocks virtual-environment activation, run this once in the current PowerShell session and activate again:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

### macOS or Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
python ai_spam_detector/app.py
```

## Project Structure

```text
.
├── requirements.txt             # Python dependencies
├── readme.MD                    # Project documentation
└── ai_spam_detector/
		├── app.py                   # Flask application and / route
		├── model.py                 # Training data, vectorizer, and prediction
		├── templates/
		│   └── index.html           # Message form and prediction result
		└── static/
				└── style.css            # Page styling
```

## Model Details

- Features: `TfidfVectorizer`
- Classifier: `MultinomialNB`
- Classes: `spam` and `normal`
- Training: the sample messages in `model.py` are fitted when the module is imported
- Persistence: no model file or database is currently used

The training set is intentionally small and embedded in the source code. The confidence value is the model's predicted class probability, not a guarantee that the message is safe. For production use, replace the sample data with a larger representative dataset, evaluate the model on held-out data, and save/load a versioned trained model.

## Development Notes.

The application currently runs with Flask debug mode enabled when started with `python ai_spam_detector\app.py`. Use a production WSGI server and disable debug mode before deploying publicly.
