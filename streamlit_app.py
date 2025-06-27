import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Life Expectancy Dashboard", layout="centered")

st.title("Visualising The Impact of Inequality With Different Metrics")
st.markdown("This is a visual exploration of how Gini coefficient, life expectancy and more range both inter-nationally and intra-nationally")

### --- Chart 1: Gini Coefficient Bar Chart --- ###
st.subheader("Gini Coefficients by Country (2002)")

data = {
    "Country": [
        "Spain", "Japan", "Sweden", "Germany", "France",
        "United Kingdom", "United States", "Russia", "Brazil", "India"
    ],
    "Gini Coefficient": [0.08, 0.08, 0.08, 0.08, 0.08, 0.09, 0.10, 0.12, 0.12, 0.21]
}

df = pd.DataFrame(data)
df = df.sort_values(by="Gini Coefficient")

fig1 = px.bar(
    df,
    x="Country",
    y="Gini Coefficient",
    title="Countries ranked according to mortality inequality<br>Gini coefficients in 2002"
)
fig1.update_layout(
    title_x=0.2,
    yaxis_title="Mortality Inequality Gini Coefficient (2002)",
    xaxis_title="",
    uniformtext_minsize=8,
    uniformtext_mode='hide'
)
st.plotly_chart(fig1, use_container_width=True)

### --- Chart 2: Life Expectancy Line Chart --- ###
st.subheader("Life Expectancy by Deprivation Decile (2018–2020)")

life_exp_data = {
    "Decile": ["1st", "2nd", "3rd", "4th", "5th", "6th", "7th", "8th", "9th", "10th"],
    "Male Life Expectancy": [73.5, 75.4, 76.6, 77.6, 78.4, 79.2, 79.9, 80.5, 81.2, 83.2],
    "Female Life Expectancy": [78.3, 80.4, 81.5, 82.4, 83.1, 83.7, 84.3, 84.8, 85.3, 86.3]
}
df_life = pd.DataFrame(life_exp_data)
df_melted = df_life.melt(id_vars="Decile", 
                         value_vars=["Male Life Expectancy", "Female Life Expectancy"],
                         var_name="Gender", 
                         value_name="Life Expectancy")

fig2 = px.line(
    df_melted,
    x="Decile",
    y="Life Expectancy",
    color="Gender",
    title="Life expectancy at birth by deprivation decile in England (2018–2020)",
    markers=True,
    color_discrete_map={
        "Male Life Expectancy": "#1f77b4",
        "Female Life Expectancy": "#ff7f0e"
    }
)

fig2.update_layout(title_x=0.2,
                   yaxis_title="Life Expectancy (years)",
                   xaxis_title="Deprivation decile")

st.plotly_chart(fig2, use_container_width=True)

#Add a Footer with 
st.markdown(
    """
    <style>
        .footer {
            position: fixed;
            left: 0;
            bottom: 0;  
            width: 100%;
            text-align: center;
            font-size: 14px;
            color: gray;
            background-color: white;
            padding: 10px 0;
            z-index: 9999; /* Keeps the footer on top of other elements */
        }
        .stApp {
            padding-bottom: 50px; /* Creates space at the bottom so content doesn't hide behind footer */
        }
    </style>
    <div class="footer">By Luqa Ismail-Keyes</div>
    """,
    unsafe_allow_html=True
)

#add theme selector
theme = st.sidebar.radio("Choose Theme", ["Light", "Blue"])
if theme == "Blue":
    st.markdown('<style>.stApp {background-color: #3498db; color: white;}</style>', unsafe_allow_html=True)
