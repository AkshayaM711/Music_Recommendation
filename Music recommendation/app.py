import streamlit as st
import pandas as pd

# Load dataset
@st.cache_data
def load_data():
    return pd.read_csv("music_sentiment_dataset.csv")  # Ensure the dataset is in the same folder

df = load_data()

# Extract unique values for dropdowns
genres = df["Genre"].dropna().unique().tolist()
energy_levels = df["Energy"].dropna().unique().tolist()
danceability_levels = df["Danceability"].dropna().unique().tolist()


# Streamlit UI
st.title("🎵 Music Recommendation System")
st.write("Select your preferences to get song recommendations.")

# Dropdowns for filtering
selected_genre = st.selectbox("Select Genre:", ["--Select--"] + genres)
selected_energy = st.selectbox("Select Energy Level:", ["--Select--"] + energy_levels)
selected_danceability = st.selectbox("Select Danceability:", ["--Select--"] + danceability_levels)


# Get Recommendations
if st.button("Get Recommendations"):
    # Filter data based on selections
    filtered_df = df[
        (df["Genre"] == selected_genre) & 
        (df["Energy"] == selected_energy) & 
        (df["Danceability"] == selected_danceability) 
        
    ]
    
    # Get unique User_Text values
    recommendations = filtered_df["User_Text"].dropna().unique().tolist()

    # Display results
    if recommendations:
        st.subheader("Recommended User Text:")
        for text in recommendations:
            st.write(f"- {text}")
    else:
        st.warning("No matching recommendations found. Try different selections.")
