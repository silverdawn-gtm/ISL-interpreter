from flask import Flask, request, jsonify
import tensorflow as tf
import numpy as np

app = Flask(__name__)

# Load the trained model
model = tf.keras.models.load_model("mobilevit_landmarks_model.h5")

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        if 'landmarks' not in data:
            return jsonify({'error': 'No landmarks provided'}), 400

        # Convert to NumPy array and reshape
        landmarks = np.array(data['landmarks']).reshape(1, -1)

        # Make prediction
        prediction = model.predict(landmarks)
        class_idx = np.argmax(prediction)
        confidence = float(prediction[0][class_idx])

        return jsonify({'class': int(class_idx), 'confidence': confidence})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)  # Render requires an open port
