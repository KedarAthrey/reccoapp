import streamlit as st
import pickle
import pandas as pd
import requests

api_key = '0eb31fcd72411786d3083c42f1a9fa78'
base_url = 'https://api.themoviedb.org/3'
def get_movie_poster(movie_id):
    endpoint = f'{base_url}/movie/{movie_id}'
    params = {'api_key': api_key}

    response = requests.get(endpoint, params=params)
    data = response.json()
    if response.status_code == 200:
        # Extract the poster path from the response
        poster_path = data.get('poster_path')
        if poster_path:
            # Construct the full URL for the poster image
            poster_url = f'https://image.tmdb.org/t/p/w500/{poster_path}'
            return poster_url
        else:
            print("Poster path not found for the movie.")
    else:
        print(f"Error {response.status_code}: {data.get('status_message')}")

def reccomend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    reccomended_movies = []
    reccommended_posters=[]
    for i in movies_list:
        reccomended_movies.append(movies.iloc[i[0]].title)
        reccommended_posters.append(get_movie_poster(movies.iloc[i[0]].id))
    return reccomended_movies,reccommended_posters


movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies= pd.DataFrame(movies_dict)
similarity= pickle.load(open('similarity.pkl', 'rb'))

st.title('Movie Reccomendation System')
selected_movie_name  = st.selectbox(
'What movie do you want the recommendations to be similar to?',
movies['title'].values)

if st.button('Recommend'):
    names,posters = reccomend(selected_movie_name)
    import streamlit as st
    col1, col2, col3 ,col4 ,col5 = st.columns(5)

    with col1:
        st.text(names[0])
        st.image(posters[0])

    with col2:
        st.text(names[1])
        st.image(posters[1])

    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])
