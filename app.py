import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import matplotlib.pyplot as plt
from css import get_css

st.markdown(get_css(), unsafe_allow_html=True)
st.subheader("World Overview")

#PAGE LAYOUT
st.sidebar.markdown("# Welcome to War Predictor")
st.sidebar.write("This model predicts war based on following features etc......Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec ac bibendum eros. Cras eleifend ipsum eu massa rutrum, non semper arcu dictum. Integer id est rhoncus, iaculis dolor ac, accumsan ex. Ut porta commodo lorem, pellentesque ultrices nisi. In vehicula magna ut felis auctor, id lobortis leo fermentum. Quisque mollis arcu nibh, non tincidunt eros suscipit ac. Vivamus in felis sed est placerat laoreet ultrices sit amet est. Aenean mattis dapibus sem non tincidunt. Maecenas varius erat lectus, at vulputate mauris finibus vitae. Suspendisse aliquam tortor ut lorem posuere, in cursus dui vestibulum. Nulla tincidunt urna quam.")


#LOAD DATA

prediction = pd.read_csv("country_code_example.csv")
df = prediction[["Country from our model", "probability of war", "Code"]]

full_dataset_df = pd.read_csv("full_dataset.csv")
feature_list = full_dataset_df.columns

col1, col2 = st.columns([6, 1])
with col1:
    fig = go.Figure(data=go.Choropleth(
            locations = df['Code'],
            z = df['probability of war'],
            text = df['Country from our model'],
            colorscale = 'Blackbody',
            autocolorscale=False,
            reversescale=True,
            marker_line_color='darkgray',
            marker_line_width=0.5,
            colorbar_tickprefix = '$',
            colorbar_title = 'Probability of War',
        ),
        )
    fig.update_layout(
            title_text='Probability of War next year',
            geo=dict(
                showframe=False,
                showcoastlines=False,
                projection_type='equirectangular'
            ),
            annotations = [dict(
                x=0.55,
                y=0.1,
                xref='paper',
                yref='paper',
                text='Source: ',
                showarrow = False
            )],
        )

#DISPLAY DATA

    st.write(fig)


#DISPLAY GENERAL METRICS
with col2:
    st.subheader("Key Features")
    st.metric("Average GDP worldwide", "200 USD", "1.2 %")
    st.metric("Political stability index", "0.6", "-8%")
    st.metric("Refugees and displaced persons index", "0.86", "4%")


#Choose Feature

feature_selected = st.multiselect('Select Feature', feature_list)
st.write(feature_selected)


#Choose Country

st.markdown('## Select country of interest')

COUNTIES_SELECTED = st.selectbox('Select countries', df["Country from our model"])
st.write('You selected:', COUNTIES_SELECTED)
