import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

# Load the expanded movie dataset
movies_df = pd.read_csv('movies.csv')

# Combine relevant features (genres, director, cast) for the recommendation
movies_df['combined_features'] = movies_df['genres'] + " " + movies_df['director'] + " " + movies_df['cast']

# Create a TF-IDF Vectorizer for the combined features
tfidf_vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf_vectorizer.fit_transform(movies_df['combined_features'])

# Calculate cosine similarity between all movies
cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

# Function to get movie recommendations based on a movie title
def get_recommendations(title, cosine_sim=cosine_sim):
    # Get the index of the movie
    idx = movies_df[movies_df['title'].str.lower() == title.lower()].index[0]
    
    # Get similarity scores of all movies with the given movie
    sim_scores = list(enumerate(cosine_sim[idx]))
    
    # Sort movies by similarity scores, excluding the movie itself
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:6]  # Get top 5 most similar
    
    # Get the indices of recommended movies
    movie_indices = [i[0] for i in sim_scores]
    
    # Return the titles of recommended movies
    return movies_df['title'].iloc[movie_indices].tolist()
