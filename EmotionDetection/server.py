from flask import Flask, request, jsonify
from emotion_detection import emotion_detector  

app = Flask(__name__)

@app.route('/emotion-detector', methods=['POST'])
def detect_emotion():
    data = request.get_json()
    text_to_analyze = data.get('text')
    
    if not text_to_analyze:
        return jsonify({"error": "No text provided"}), 400
    
    result = emotion_detector(text_to_analyze)
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)