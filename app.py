from flask import Flask, render_template, request, jsonify
import pickle
import re
import os
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

# Initialize Flask app
app = Flask(__name__)

# Global variables to store model and vectorizer
model = None
vectorizer = None

def initialize_nltk():
    """Download NLTK data if not available"""
    try:
        stopwords.words('english')
    except LookupError:
        print("Downloading NLTK stopwords...")
        nltk.download('stopwords', quiet=True)

def load_models():
    """Load the trained model and vectorizer"""
    global model, vectorizer
    try:
        print("Loading model and vectorizer...")
        model = pickle.load(open('trained_model.sav', 'rb'))
        vectorizer = pickle.load(open('vectorizer.sav', 'rb'))
        print("Model and vectorizer loaded successfully!")
        return True
    except FileNotFoundError as e:
        print(f"Error: Model files not found - {e}")
        return False
    except Exception as e:
        print(f"Error loading models: {e}")
        return False

def preprocess_tweet(content):
    """Preprocess tweet text"""
    try:
        port_stem = PorterStemmer()
        content = re.sub('[^a-zA-Z]', ' ', content)
        content = content.lower()
        content = content.split()
        content = [port_stem.stem(word) for word in content if word not in stopwords.words('english')]
        return ' '.join(content)
    except Exception as e:
        print(f"Error in preprocessing: {e}")
        return content.lower()

# Initialize on module import
initialize_nltk()
models_loaded = load_models()

@app.route('/')
def index():
    """Main page"""
    try:
        return render_template('index.html')
    except Exception as e:
        return f"Error loading page: {str(e)}", 500

@app.route('/health')
def health():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'model_loaded': model is not None,
        'vectorizer_loaded': vectorizer is not None,
        'models_loaded': models_loaded
    })

@app.route('/classify', methods=['POST'])
def classify():
    """Classify tweet sentiment"""
    try:
        # Check if models are loaded
        if not models_loaded or model is None or vectorizer is None:
            return jsonify({'error': 'Models not loaded properly'}), 500
            
        # Get JSON data
        data = request.get_json()
        if not data or 'tweet' not in data:
            return jsonify({'error': 'Invalid request format'}), 400
            
        tweet = data.get('tweet', '').strip()
        if not tweet:
            return jsonify({'error': 'No tweet provided'}), 400
            
        # Limit tweet length
        if len(tweet) > 500:
            return jsonify({'error': 'Tweet too long. Max 500 characters.'}), 400
        
        print(f"Processing tweet: {tweet}")
        
        # Preprocess and predict
        processed_tweet = preprocess_tweet(tweet)
        transformed_tweet = vectorizer.transform([processed_tweet])
        prediction = model.predict(transformed_tweet)
        
        sentiment = "Positive" if prediction[0] == 1 else "Negative"
        emoji = "😊" if prediction[0] == 1 else "😢"
        
        return jsonify({
            'sentiment': sentiment, 
            'emoji': emoji,
            'processed': processed_tweet
        })
        
    except Exception as e:
        print(f"Error in classification: {str(e)}")
        return jsonify({'error': f'Classification failed: {str(e)}'}), 500

# For Vercel, we need this
def handler(request):
    """Vercel handler function"""
    return app(request.environ, lambda *args: None)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)