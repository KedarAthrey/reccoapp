This project aimed to create an application that takes the user's movie of choice as input and recommends 5 movies most similar to it. 
I've used the tmbd 5000 database to get the data for the movies, and the cosine similarity model from sklearn to find similar movies :)

Libraries used: pandas, numpy, streamlit(for the web app UI), pickle and cosine similarity(the main ML model) from sklearn. You will have to install these libraries in order to host it locally. Once installed, run    streamlit run (location of file)\app.py
