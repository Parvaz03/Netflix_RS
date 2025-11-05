import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

def get_recommendations(movie_name, data):
    cv = CountVectorizer(max_features=5000, stop_words='english')
    vectors = cv.fit_transform(data['genre']).toarray()
    similarity = cosine_similarity(vectors)
    
    if movie_name not in data['title'].values:
        return ["Movie not found in database."]
    
    movie_index = data[data['title'] == movie_name].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(
        list(enumerate(distances)), reverse=True, key=lambda x: x[1]
    )[1:6]
    
    return data.iloc[[i[0] for i in movie_list]]['title'].values.tolist()
