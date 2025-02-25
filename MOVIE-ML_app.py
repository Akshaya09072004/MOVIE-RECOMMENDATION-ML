from flask import Flask, request, jsonify, render_template
from model import get_recommendations

app = Flask(__name__)

# Route for the homepage
@app.route('/')
def home():
    return render_template('index.html')

# Route for generating recommendations
@app.route('/recommend', methods=['POST'])
def recommend():
    data = request.get_json()
    movie = data['movie']
    recommendations = get_recommendations(movie)
    
    return jsonify({'recommendations': recommendations})

if __name__ == '__main__':
    app.run(debug=True)



