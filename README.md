# Twitter Sentiment Analysis

A machine learning web application that classifies tweets as positive or negative using natural language processing and logistic regression.

## 🌟 Features

- Real-time sentiment classification of tweets
- Web-based interface with responsive design
- Machine learning model trained on Sentiment140 dataset
- Text preprocessing with stemming and stopword removal
- RESTful API for programmatic access

## 🛠️ Technologies Used

- **Python 3.9**
- **Flask** - Web framework
- **scikit-learn** - Machine learning library
- **NLTK** - Natural language processing
- **TF-IDF Vectorizer** - Text feature extraction
- **Logistic Regression** - Classification algorithm

## 📊 Dataset

The model is trained on the **Sentiment140 dataset** containing 1.6 million tweets:
- **0** - Negative sentiment
- **1** - Positive sentiment

## 🚀 Quick Start

### Prerequisites

- Python 3.9+
- pip package manager

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/dsharma08k/Twitter-Sentiment-Analyser.git
cd Twitter-Sentiment-Analyser
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Run the application**
```bash
python app.py
```

## 📁 Project Structure

```
twitter-sentiment-analysis/
├── app.py                          # Flask web application
├── twitter_sentiment_analysis.py   # Model training notebook
├── classify_new_tweets.py          # Standalone classification script
├── requirements.txt                # Python dependencies
├── templates/index.html            # Main web interface
├── static/
│   ├── style.css                   # Styling and animations
│   └── script.js                   # Frontend JavaScript
└── trained_model.sav               # Serialized ML model
└── vectorizer.sav                  # Serialized vectorizer
```

## 🔍 API Endpoints

### Health Check
```http
GET /health
```

### Classify Tweet
```http
POST /classify
Content-Type: application/json

{
  "tweet": "I love this beautiful sunny day!"
}
```

**Response:**
```json
{
  "sentiment": "Positive",
  "emoji": "😊",
  "processed": "love beauti sunni dai"
}
```

## 🧠 Model Details

### Training Process
1. **Data Loading**: Sentiment140 dataset (1.6M tweets)
2. **Text Preprocessing**: Remove URLs, mentions, special characters; apply stemming
3. **Feature Extraction**: TF-IDF vectorization with bigrams
4. **Model Training**: Logistic Regression with hyperparameter tuning
5. **Model Persistence**: Pickle serialization

### Performance
- **Training Accuracy**: ~82%
- **Test Accuracy**: ~78%

## 🔧 Text Preprocessing Example

```
Input:  "I'm loving this sunny day! 😊 #beautiful"
Output: "love sunni dai beauti"
```

## 📱 Usage Examples

### Command Line
```python
python classify_new_tweets.py
# Enter a tweet to classify: Great weather today!
# Sentiment: Positive
```

### Programmatic Usage
```python
import requests

response = requests.post('/classify', json={'tweet': 'Great weather today!'})
result = response.json()
print(f"Sentiment: {result['sentiment']}")
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

## 📝 License

This project is open source and available under the MIT License.
