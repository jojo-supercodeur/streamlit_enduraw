import pandas as pd
import plotly.express as px
import streamlit as st
from datetime import datetime, timedelta
import os
import json

# Example simulated data
data = {
    "Distance": range(0, 100),
    "Altitude": [100 + i*10 for i in range(100)],
    "Gradient": [5 - i*0.05 for i in range(100)]
}

# Convert the data to a DataFrame
course_data = pd.DataFrame(data)


# Create an altitude chart
fig_altitude = px.line(
    course_data,
    x="Distance",
    y="Altitude",
    title="Course Altitude Profile",
    labels={"Distance": "Distance (km)", "Altitude": "Altitude (m)"},
)
fig_altitude.update_layout(paper_bgcolor="white", plot_bgcolor="white")
fig_altitude.update_traces(line_color="blue")

# Create a gradient chart
fig_gradient = px.line(
    course_data,
    x="Distance",
    y="Gradient",
    title="Course Gradient Profile",
    labels={"Distance": "Distance (km)", "Gradient": "Gradient (%)"},
)
fig_gradient.update_layout(paper_bgcolor="white", plot_bgcolor="white")
fig_gradient.update_traces(line_color="red")

# Définition des courses disponibles
races = {
    "Your race": {"date": datetime(2024, 5, 4, 15, 0), "location": "Paris"},
    "Boston Marathon": {"date": datetime(2024, 12, 25, 9, 30), "location": "New York"},
    "London Marathon": {"date": datetime(2024, 7, 12, 14, 0), "location": "Tokyo"},
    "Ecotrail": {"date": datetime(2024, 8, 23, 17, 45), "location": "Berlin"}
}

base_path = os.path.dirname(__file__)  # Obtenir le chemin du répertoire du script actuel










import streamlit as st
import gpxpy
import pandas as pd

# Définir une liste de courses prédéfinies (exemple)
predefined_courses = {
    "Sample Course 1": "data/sample_course1.gpx",
    "Sample Course 2": "data/sample_course2.gpx",
    "Sample Course 3": "data/sample_course3.gpx"
}

# Interface utilisateur
st.title("Choose a Race or Upload a GPX File")

# Options pour choisir entre une course prédéfinie ou un fichier personnalisé
selection_mode = st.selectbox("Choose an option", ["Select a predefined course", "Upload a custom GPX file"])

# Variables pour stocker les points GPS
points = []

if selection_mode == "Select a predefined course":
    # Afficher le menu déroulant pour choisir une course prédéfinie
    selected_course = st.selectbox("Select a predefined course", list(predefined_courses.keys()))

    # Charger le fichier GPX prédéfini
    gpx_path = predefined_courses[selected_course]
    with open(gpx_path, "r") as gpx_file:
        gpx = gpxpy.parse(gpx_file)

    # Extraire les points GPS
    track = gpx.tracks[0] if gpx.tracks else None
    segment = track.segments[0] if track and track.segments else None

    if segment:
        points = [(point.latitude, point.longitude, point.elevation) for point in segment.points]
        st.write(f"Number of points in {selected_course}: {len(points)}")

elif selection_mode == "Upload a custom GPX file":
    # Uploader le fichier GPX personnalisé
    uploaded_file = st.file_uploader("Choose a GPX file", type=["gpx"])

    if uploaded_file is not None:
        # Lire le fichier GPX téléchargé
        gpx = gpxpy.parse(uploaded_file)

        # Extraire les points GPS
        track = gpx.tracks[0] if gpx.tracks else None
        segment = track.segments[0] if track and track.segments else None

        if segment:
            points = [(point.latitude, point.longitude, point.elevation) for point in segment.points]
            st.write(f"Number of points in the uploaded GPX file: {len(points)}")
        else:
            st.write("The uploaded GPX file doesn't contain a valid track.")
    else:
        st.write("Upload a GPX file to see its details.")

# Afficher un aperçu des premiers points GPS extraits
if points:
    st.write(f"First 5 points: {points[:5]}")




























# Interface utilisateur

st.title("Course Altitude and Gradient Profile")
selected_race = st.selectbox("Choose your race", list(races.keys()))




#uphill_level = st.slider("Your uphill level - from flat runner to uphill runner", 0, 1, 0.5)  # 0,5 comme valeur par défaut
uphill_level = st.select_slider("Wind Direction (dir)", options=["Flat runner", "Prefer flat section","Average", "Good when hilly", "Uphill runner", "Vertical Kilometer runner"], value="Average")

runner_speed = st.slider("Your expected speed (km/h) - the speed impacts the grade adjusted speed", 6, 22, 17)  # 15 comme valeur par défaut


#st.title(f"Wind Impact on {selected_race}")


if selected_race == "Your race":
    st.write("")
    st.write("")
    st.write("Enter your race and informations")

else : 


    logo_path = os.path.join(base_path, f"logo_race/{selected_race}.png")
    html_file_map = os.path.join(base_path,f"map_race/map_{selected_race}.html")
    html_file_weather = os.path.join(base_path,f"weather_race/wind_help_{selected_race}.html")
    directions_path = os.path.join(base_path,f"directions_race/{selected_race}_directions.json")
    elev_path = os.path.join(base_path, f"elev_race/elevation_profile2_{selected_race}.png")
    grad_path = os.path.join(base_path, f"grad_race/elevation_profile3_{selected_race}.png")




    with open(directions_path, 'r') as file:  # Remplacez 'file.json' par le chemin de votre fichier
        data = json.load(file)
        directions = [item['direction'] for item in data]
        mean_direction = sum(directions)/len(directions)




    st.image(logo_path, width=300)  # Modifie "path_to_logo.png" par le chemin vers ton fichier image ou URL, et ajuste la largeur selon tes besoins.

    st.image(elev_path)
    st.image(grad_path)




# Display the charts in Streamlit
st.plotly_chart(fig_altitude)
st.plotly_chart(fig_gradient)




