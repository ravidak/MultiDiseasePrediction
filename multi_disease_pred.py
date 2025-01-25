import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Loading the saved models
diabetic_models = pickle.load(open(r"C:\Users\ravid\Desktop\Data Analytics\machine learning\projects\multiple disease prediction system\models\Diabetes_model.sav", "rb"))
heart_disease_models = pickle.load(open(r"C:\Users\ravid\Desktop\Data Analytics\machine learning\projects\multiple disease prediction system\models\Heart_model.sav", "rb"))
parkinson_models = pickle.load(open(r"C:\Users\ravid\Desktop\Data Analytics\machine learning\projects\multiple disease prediction system\models\parkinsons_model.sav", "rb"))

# Sidebar for navigation
with st.sidebar:
    selected = option_menu(
        'Multiple Disease Prediction System using ML',
        ["Diabetes Prediction", "Heart Disease Prediction", "Parkinsons Disease Prediction"],
        icons=['activity','heart','person'],
        default_index=0
    )

# Diabetes Prediction page
if selected == "Diabetes Prediction":
    st.title("Diabetes Prediction using ML")
    
    # Input fields in 3 columns
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input("Number of Pregnancies:")
        SkinThickness = st.text_input("Skin Thickness value:")
        BMI = st.text_input("Body Mass Index value:")
        
    with col2:
        Glucose = st.text_input("Glucose Level:")
        Insulin = st.text_input("Insulin Level:")
        DiabetesPedigreeFunction = st.text_input("Diabetes Pedigree Function value:")
        
    with col3:
        BloodPressure = st.text_input("Blood Pressure Value:")
        Age = st.text_input("Age:")
    
    # Prediction button
    diab_diagnosis = ''
    if st.button('Diabetes Test Result'):
        try:
            input_data = [
                float(Pregnancies), float(Glucose), float(BloodPressure),
                float(SkinThickness), float(Insulin), float(BMI),
                float(DiabetesPedigreeFunction), float(Age)
            ]
            diab_prediction = diabetic_models.predict([input_data])
            if diab_prediction[0] == 1:
                diab_diagnosis = 'The person is diabetic'
            else:
                diab_diagnosis = 'The person is not diabetic'
        except Exception as e:
            diab_diagnosis = f"Error in input: {e}"

    st.success(diab_diagnosis)

# Heart Disease Prediction page
if selected == 'Heart Disease Prediction':
    st.title('Heart Disease Prediction using ML')
    
    # Input fields in 3 columns
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.text_input("Age:")
        cp = st.text_input("Chest Pain Type (0-3):")
        chol = st.text_input("Cholesterol Level:")
        exang = st.text_input("Exercise Induced Angina (0 or 1):")
        
    with col2:
        sex = st.text_input("Sex (1 = male, 0 = female):")
        trestbps = st.text_input("Resting Blood Pressure:")
        fbs = st.text_input("Fasting Blood Sugar > 120 mg/dl (1 = True, 0 = False):")
        oldpeak = st.text_input("ST Depression Induced:")
        
    with col3:
        restecg = st.text_input("Resting ECG Results (0-2):")
        thalach = st.text_input("Maximum Heart Rate Achieved:")
        slope = st.text_input("Slope of ST Segment (0-2):")
        ca = st.text_input("Number of Major Vessels (0-3):")
        thal = st.text_input("Thalassemia (0-3):")
    
    # Prediction button
    heart_diagnosis = ''
    if st.button('Heart Disease Test Result'):
        try:
            input_data = [
                float(age), float(sex), float(cp), float(trestbps), float(chol),
                float(fbs), float(restecg), float(thalach), float(exang),
                float(oldpeak), float(slope), float(ca), float(thal)
            ]
            heart_prediction = heart_disease_models.predict([input_data])
            if heart_prediction[0] == 1:
                heart_diagnosis = 'The person has heart disease'
            else:
                heart_diagnosis = 'The person does not have heart disease'
        except Exception as e:
            heart_diagnosis = f"Error in input: {e}"

    st.success(heart_diagnosis)

# Parkinson's Disease Prediction page
if selected == "Parkinsons Disease Prediction":
    st.title("Parkinson's Disease Prediction using ML")
    
    # Input fields in 3 columns
    col1, col2, col3 = st.columns(3)
    
    with col1:
        MDVP_Fo = st.text_input("MDVP:Fo(Hz):")
        MDVP_Fhi = st.text_input("MDVP:Fhi(Hz):")
        MDVP_Flo = st.text_input("MDVP:Flo(Hz):")
        MDVP_Jitter = st.text_input("MDVP:Jitter(%):")
        MDVP_Jitter_Abs = st.text_input("MDVP:Jitter(Abs):")
        MDVP_RAP = st.text_input("MDVP:RAP:")
        MDVP_PPQ = st.text_input("MDVP:PPQ:")
        
    with col2:
        Jitter_DDP = st.text_input("Jitter:DDP:")
        MDVP_Shimmer = st.text_input("MDVP:Shimmer:")
        MDVP_Shimmer_dB = st.text_input("MDVP:Shimmer(dB):")
        MDVP_APQ = st.text_input("MDVP:APQ:")
        Shimmer_DDA = st.text_input("Shimmer:DDA:")
        NHR = st.text_input("NHR:")
        HNR = st.text_input("HNR:")
    with col3:
        RPDE = st.text_input("RPDE:")
        DFA = st.text_input("DFA:")
        spread1 = st.text_input("Spread1:")
        spread2 = st.text_input("Spread2:")
        D2 = st.text_input("D2:")
        PPE = st.text_input("PPE:")
    
    # Prediction button
    parkinson_diagnosis = ''
    if st.button('Parkinson’s Disease Test Result'):
        try:
            input_data = [
                float(MDVP_Fo), float(MDVP_Fhi), float(MDVP_Flo), float(MDVP_Jitter),
                float(MDVP_Jitter_Abs), float(MDVP_RAP), float(MDVP_PPQ), float(Jitter_DDP),
                float(MDVP_Shimmer), float(MDVP_Shimmer_dB), float(Shimmer_APQ3), float(Shimmer_APQ5),
                float(MDVP_APQ), float(Shimmer_DDA), float(NHR), float(HNR), float(RPDE),
                float(DFA), float(spread1), float(spread2), float(D2), float(PPE)
            ]
            parkinson_prediction = parkinson_models.predict([input_data])
            if parkinson_prediction[0] == 1:
                parkinson_diagnosis = "The person has Parkinson's disease"
            else:
                parkinson_diagnosis = "The person does not have Parkinson's disease"
        except Exception as e:
            parkinson_diagnosis = f"Error in input: {e}"

    st.success(parkinson_diagnosis)
