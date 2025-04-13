import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Set page configuration
st.set_page_config(page_title="Health Assistant",
                   layout="wide",
                   page_icon="🧑‍⚕️")

# Custom CSS for background image and styles
page_bg_img = '''
<style>
body {
    background-image: url("https://your-image-url.com"); /* Replace with your image URL */
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}
.main .block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
    background-color: rgba(255, 255, 255, 0.8); /* To make the background a bit transparent */
    border-radius: 12px;
}
.stButton button {
    background-color: #ff4b4b;
    color: white;
    border-radius: 12px;
    padding: 10px 24px;
    border: none;
    font-size: 16px;
    transition: background-color 0.3s ease;
}
.stButton button:hover {
    background-color: #ff3333;
    color: #f0f2f6;
}
.stTextInput input {
    border-radius: 8px;
    padding: 8px;
    border: 1px solid #ccc;
    margin-bottom: 10px;
}
.title {
    font-size: 2rem;
    font-weight: bold;
    color: #ff4b4b;
    text-align: center;
    margin-top: 1rem;
}
.description {
    text-align: center;
    margin-bottom: 1rem;
    font-size: 1.2rem;
    color: #333;
}
.custom-column {
    text-align: center;
    margin-top: 1rem;
}
</style>
'''

# Inject CSS for background and styling
st.markdown(page_bg_img, unsafe_allow_html=True)

# Sidebar for navigation
with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System',
                           ['BMI Calculator',
                            'Diabetes Prediction',
                            'Heart Disease Prediction',
                            'Parkinsons Prediction'],
                           menu_icon='hospital-fill',
                           icons=['calculator', 'activity', 'heart', 'person'],
                           default_index=0)

# Model loading
diabetes_model = pickle.load(open(f'C:/Users/Prath/OneDrive/Desktop/Multidisease_Prediction_App/Model/diabetes_model.sav', 'rb'))
heart_disease_model = pickle.load(open(f'C:/Users/Prath/OneDrive/Desktop/Multidisease_Prediction_App/Model/heart_disease_model.sav', 'rb'))
parkinsons_model = pickle.load(open(f'C:/Users/Prath/OneDrive/Desktop/Multidisease_Prediction_App/Model/parkinsons_model.sav', 'rb'))

# BMI Calculator Page
if selected == 'BMI Calculator':
    st.markdown('<h1 class="title">BMI Calculator</h1>', unsafe_allow_html=True)
    st.markdown('<p class="description">Enter your height and weight to calculate your Body Mass Index (BMI)</p>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        height = st.text_input('Height (in cm)')

    with col2:
        weight = st.text_input('Weight (in kg)')

    if st.button('Calculate BMI'):
        try:
            if not height or not weight:
                st.error('Please fill in both height and weight.')
            else:
                height_m = float(height) / 100  # Convert height to meters
                weight_kg = float(weight)
                bmi = weight_kg / (height_m ** 2)

                if bmi < 18.5:
                    category = "Underweight"
                elif 18.5 <= bmi < 24.9:
                    category = "Normal weight"
                elif 25 <= bmi < 29.9:
                    category = "Overweight"
                else:
                    category = "Obesity"

                st.success(f'Your BMI is {bmi:.2f}, which falls under the category: {category}')
        except ValueError:
            st.error('Please enter valid numeric values for height and weight.')

# Diabetes Prediction Page
if selected == 'Diabetes Prediction':
    st.markdown('<h1 class="title">Diabetes Prediction</h1>', unsafe_allow_html=True)
    st.markdown('<p class="description">Enter your details to check your diabetes risk</p>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')

    with col2:
        Glucose = st.text_input('Glucose Level')

    with col3:
        BloodPressure = st.text_input('Blood Pressure value')

    with col1:
        SkinThickness = st.text_input('Skin Thickness value')

    with col2:
        Insulin = st.text_input('Insulin Level')

    with col3:
        BMI = st.text_input('BMI value')

    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')

    with col2:
        Age = st.text_input('Age of the Person')

    # Prediction button
    if st.button('Diabetes Test Result'):
        # Check if any field is empty
        if not Pregnancies or not Glucose or not BloodPressure or not SkinThickness or not Insulin or not BMI or not DiabetesPedigreeFunction or not Age:
            st.error('Please fill in all fields before proceeding.')
        else:
            try:
                # Convert inputs to float and predict
                user_input = [float(x) for x in [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]]
                diab_prediction = diabetes_model.predict([user_input])
                diab_diagnosis = 'The person is diabetic' if diab_prediction[0] == 1 else 'The person is not diabetic'
                st.success(diab_diagnosis)
            except ValueError:
                st.error('Please enter valid numeric values for all fields.')

# Heart Disease Prediction Page
if selected == 'Heart Disease Prediction':
    st.markdown('<h1 class="title">Heart Disease Prediction</h1>', unsafe_allow_html=True)
    st.markdown('<p class="description">Enter your details to check your heart disease risk</p>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('Age')

    with col2:
        sex = st.text_input('Sex')

    with col3:
        cp = st.text_input('Chest Pain types')

    with col1:
        trestbps = st.text_input('Resting Blood Pressure')

    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')

    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')

    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')

    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')

    with col3:
        exang = st.text_input('Exercise Induced Angina')

    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')

    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')

    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')

    with col1:
        thal = st.text_input('Thal: 0 = normal; 1 = fixed defect; 2 = reversible defect')

    # Prediction button
    if st.button('Heart Disease Test Result'):
        # Check if any field is empty
        if not age or not sex or not cp or not trestbps or not chol or not fbs or not restecg or not thalach or not exang or not oldpeak or not slope or not ca or not thal:
            st.error('Please fill in all fields before proceeding.')
        else:
            try:
                # Convert inputs to float and predict
                user_input = [float(x) for x in [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]]
                heart_prediction = heart_disease_model.predict([user_input])
                heart_diagnosis = 'The person has heart disease' if heart_prediction[0] == 1 else 'The person does not have heart disease'
                st.success(heart_diagnosis)
            except ValueError:
                st.error('Please enter valid numeric values for all fields.')

# Parkinson's Prediction Page
if selected == "Parkinsons Prediction":

    # page title
    st.title("Parkinson's Disease Prediction using ML")

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')

    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')

    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')

    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%)')

    with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')

    with col1:
        RAP = st.text_input('MDVP:RAP')

    # Prediction button
    if st.button('Parkinsons Test Result'):
        # Check if any field is empty
        if not fo or not fhi or not flo or not Jitter_percent or not Jitter_Abs or not RAP:
            st.error('Please fill in all fields before proceeding.')
        else:
            try:
                # Convert inputs to float and predict
                user_input = [float(x) for x in [fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP]]
                parkinsons_prediction = parkinsons_model.predict([user_input])
                parkinsons_diagnosis = 'The person has Parkinsons Disease' if parkinsons_prediction[0] == 1 else 'The person does not have Parkinsons Disease'
                st.success(parkinsons_diagnosis)
            except ValueError:
                st.error('Please enter valid numeric values for all fields.')
