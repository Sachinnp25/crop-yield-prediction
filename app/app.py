import streamlit as st
import pandas as pd
import numpy as np
import joblib
import plotly.express as px

# ============================
# LOAD MODELS
# ============================

crop_model = joblib.load("models/crop_recommendation.pkl")
yield_model = joblib.load("models/yield_model.pkl")
encoders = joblib.load("models/yield_encoders.pkl")

# ============================
# LOAD DATASET
# ============================

try:
    crop_df = pd.read_csv("dataset/crop_data.csv")
except Exception as e:
    st.error(f"Dataset Error: {e}")
    st.stop()

# ============================
# PAGE CONFIG
# ============================

st.set_page_config(
    page_title="Crop Yield Prediction System",
    page_icon="🌾",
    layout="wide"
)

# ============================
# SIDEBAR
# ============================

st.sidebar.title("🌾 Agriculture AI")
st.sidebar.markdown("""
Machine Learning Project

- Crop Recommendation
- Yield Prediction
- Dashboard Analytics
""")

page = st.sidebar.radio(
    "Navigation",
    [
        "Home",
        "Crop Recommendation",
        "Yield Prediction",
        "Dashboard",
        "About"
    ]
)

# ==================================================
# HOME PAGE
# ==================================================

if page == "Home":

    st.title("🌾 Crop Yield Prediction & Recommendation System")

    st.image(
        "https://images.unsplash.com/photo-1500937386664-56d1dfef3854",
        use_container_width=True
    )

    st.markdown("""
    ### Smart Agriculture using Machine Learning

    This system helps farmers make informed decisions by:

    - 🌱 Recommending the best crop
    - 📈 Predicting crop yield
    - 📊 Analyzing production trends
    - 🤖 Using AI for agriculture
    """)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
    "Crop Records",
    f"{len(crop_df):,}"
)

    with col2:
        st.metric(
    "Recommendation Accuracy",
    "99.3%"
)
    with col3:
        st.metric(
    "Yield Model R²",
    "0.8245"
)

# ==================================================
# CROP RECOMMENDATION
# ==================================================

elif page == "Crop Recommendation":

    st.title("🌱 Crop Recommendation")

    col1, col2 = st.columns(2)

    with col1:
        N = st.number_input("Nitrogen (N)", 0, 200)
        P = st.number_input("Phosphorus (P)", 0, 200)
        K = st.number_input("Potassium (K)", 0, 200)
        temperature = st.number_input("Temperature (°C)")

    with col2:
        humidity = st.number_input("Humidity (%)")
        ph = st.number_input("pH Value")
        rainfall = st.number_input("Rainfall (mm)")

    if st.button("Recommend Crop"):

        data = np.array([
            [N, P, K, temperature,
             humidity, ph, rainfall]
        ])

        prediction = crop_model.predict(data)

        proba = crop_model.predict_proba(data)
        confidence = np.max(proba) * 100

        # FIXED: These components must live INSIDE the button action block
        col1, col2 = st.columns(2)

        with col1:
            st.metric(
                "🌾 Recommended Crop",
                prediction[0]
            )

        with col2:
            st.metric(
                "🎯 Confidence",
                f"{confidence:.2f}%"
            )

        result_df = pd.DataFrame({
            "Recommended Crop": [prediction[0]],
            "Confidence (%)": [round(confidence, 2)]
        })

        st.download_button(
            label="📥 Download Recommendation Report",
            data=result_df.to_csv(index=False),
            file_name="crop_recommendation_report.csv",
            mime="text/csv"
        )

# ==================================================
# YIELD PREDICTION
# ==================================================

elif page == "Yield Prediction":

    st.title("📈 Yield Prediction")

    states = sorted(
        crop_df["State_Name"].dropna().unique()
    )

    state = st.selectbox(
        "Select State",
        states
    )

    districts = sorted(
        crop_df[crop_df["State_Name"] == state]
        ["District_Name"]
        .dropna()
        .unique()
    )

    district = st.selectbox(
        "Select District",
        districts
    )

    seasons = sorted(
        crop_df["Season"]
        .dropna()
        .unique()
    )

    season = st.selectbox(
        "Select Season",
        seasons
    )

    crops = sorted(
        crop_df["Crop"]
        .dropna()
        .unique()
    )

    crop = st.selectbox(
        "Select Crop",
        crops
    )

    area = st.number_input(
        "Area (Hectares)",
        min_value=1.0
    )

    year = st.number_input(
        "Crop Year",
        min_value=1997,
        max_value=2035,
        value=2025
    )

    if st.button("Predict Yield"):

        try:

            state_encoded = encoders["State_Name"].transform([state])[0]
            district_encoded = encoders["District_Name"].transform([district])[0]
            season_encoded = encoders["Season"].transform([season])[0]
            crop_encoded = encoders["Crop"].transform([crop])[0]

            input_data = np.array([[
                state_encoded,
                district_encoded,
                year,
                season_encoded,
                crop_encoded,
                area
            ]])

            prediction = yield_model.predict(input_data)

            col1, col2 = st.columns(2)

            with col1:
                st.metric(
                    "🌾 Predicted Yield",
                    f"{prediction[0]:.2f}"
                )

            with col2:
                st.metric(
                    "Unit",
                    "Ton/Hectare"
                )

            yield_df = pd.DataFrame({
                "State": [state],
                "District": [district],
                "Crop": [crop],
                "Season": [season],
                "Area": [area],
                "Predicted Yield": [round(prediction[0], 2)]
            })

            st.download_button(
                label="📥 Download Yield Report",
                data=yield_df.to_csv(index=False),
                file_name="yield_prediction_report.csv",
                mime="text/csv"
            )

        except Exception as e:
            st.error(str(e))

# ==================================================
# DASHBOARD
# ==================================================

elif page == "Dashboard":

    st.title("📊 Agriculture Dashboard")

    c1, c2, c3 = st.columns(3)

    c1.metric(
        "States",
        crop_df["State_Name"].nunique()
    )

    c2.metric(
        "Districts",
        crop_df["District_Name"].nunique()
    )

    c3.metric(
        "Crops",
        crop_df["Crop"].nunique()
    )

    st.markdown("---")

    top_crop = (
        crop_df.groupby("Crop")["Production"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
        .reset_index()
    )

    fig1 = px.bar(
        top_crop,
        x="Crop",
        y="Production",
        title="Top 10 Crops by Production"
    )

    st.plotly_chart(fig1, use_container_width=True)

    state_prod = (
        crop_df.groupby("State_Name")["Production"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
        .reset_index()
    )

    fig2 = px.bar(
        state_prod,
        x="State_Name",
        y="Production",
        title="Top Producing States"
    )

    st.plotly_chart(fig2, use_container_width=True)
    
    # FIXED: Re-indented the summary metrics to keep them inside the Dashboard page
    st.subheader("📋 Dataset Summary")

    summary = pd.DataFrame({
        "Metric": [
            "Total States",
            "Total Districts",
            "Total Crops",
            "Total Records"
        ],
        "Value": [
            crop_df["State_Name"].nunique(),
            crop_df["District_Name"].nunique(),
            crop_df["Crop"].nunique(),
            len(crop_df)
        ]
    })

    st.dataframe(summary, use_container_width=True)

    top5 = (
        crop_df.groupby("Crop")["Production"]
        .sum()
        .sort_values(ascending=False)
        .head(5)
        .reset_index()
    )

    fig3 = px.pie(
        top5,
        values="Production",
        names="Crop",
        title="Top 5 Crop Production Share"
    )

    st.plotly_chart(fig3, use_container_width=True)

    st.subheader("Dataset Preview")

    st.dataframe(
        crop_df.head(20),
        use_container_width=True
    )

# ==================================================
# ABOUT
# ==================================================

elif page == "About":

    st.title("ℹ About Project")

    st.markdown("""
    ## Crop Yield Prediction & Recommendation System

    ### Problem Statement
    Farmers often face difficulties selecting the most suitable crop due to changing weather conditions, rainfall variations, and environmental factors.

    ### Solution
    This project uses Machine Learning to:

    - Predict crop yield
    - Recommend suitable crops
    - Analyze agricultural production trends
    - Support smart farming decisions

    ### Technologies Used
    - Python
    - Streamlit
    - Pandas
    - NumPy
    - Scikit-Learn
    - Plotly

    ### Machine Learning Models
    - Random Forest Classifier
    - Random Forest Regressor

    ### Dataset
    - Indian Crop Production Dataset
    - Crop Recommendation Dataset
    """)
    
    st.markdown("### Developer\nSachin<br>[24SCSE1430415]<br>BCA (AI & ML)", unsafe_allow_html=True)

# ==================================================
# FOOTER
# ==================================================

st.markdown("---")

st.markdown(
    """
    <center>
    🌾 <b>Crop Yield Prediction & Recommendation System</b><br>
    Developed by <b>Sachin</b><br>
    BCA (AI & ML) Machine Learning Project 2026
    </center>
    """,
    unsafe_allow_html=True
)