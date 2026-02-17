from flask import Flask, request, jsonify
from flask_cors import CORS
from PIL import Image
import numpy as np

app = Flask(__name__)
CORS(app)  # allow requests from frontend

# -----------------------------
# Dummy AI Detection Functions
# -----------------------------
def detect_text_ai(text):
    words = len(text.split())
    if words > 50:
        return "AI", 85, [
            "High repetition detected",
            "Predictable sentence structure",
            "Overly consistent word usage"
        ]
    else:
        return "Real", 90, [
            "Varied sentence structure",
            "Natural punctuation",
            "Human-like word choice"
        ]

def detect_image_ai(image_file):
    # dummy image processing
    img = Image.open(image_file).convert("RGB")
    arr = np.array(img)
    # always return AI for dummy
    return "AI", 75, [
        "Smooth textures",
        "Asymmetric features",
        "Unnatural lighting patterns"
    ]

# -----------------------------
# API Route
# -----------------------------
@app.route("/detect", methods=["POST"])
def detect():
    input_type = request.form.get("type", "").lower()

    if input_type == "text":
        text = request.form.get("text", "")
        if not text:
            return jsonify({"error": "No text provided"}), 400

        result, confidence, explanation = detect_text_ai(text)

        return jsonify({
            "result": result,
            "confidence": confidence,
            "explanation": explanation
        })

    elif input_type == "image":
        if "image" not in request.files:
            return jsonify({"error": "No image uploaded"}), 400

        image_file = request.files["image"]
        result, confidence, explanation = detect_image_ai(image_file)

        return jsonify({
            "result": result,
            "confidence": confidence,
            "explanation": explanation
        })

    else:
        return jsonify({"error": "Invalid type"}), 400

# -----------------------------
# Run the server
# -----------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)