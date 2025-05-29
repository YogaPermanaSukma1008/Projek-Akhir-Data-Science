import streamlit as st
import numpy as np
import pandas as pd
import pickle

# Load model
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

st.set_page_config(page_title="Prediksi Dropout Mahasiswa", layout="centered")
st.title("🎓 Prediksi Dropout Mahasiswa")
st.markdown("Aplikasi ini memprediksi apakah mahasiswa berpotensi dropout atau tidak berdasarkan data akademik dan sosial ekonomi.")

# Input form
with st.form("dropout_form"):
    st.subheader("📋 Masukkan Data Mahasiswa")
    
    col1, col2 = st.columns(2)
    
    with col1:
        Application_mode = st.number_input("Application Mode", value=1)
        Application_order = st.number_input("Application Order", value=1)
        Course = st.number_input("Course", value=9700)
        Daytime_evening_attendance = st.selectbox("Daytime/Evening Attendance", [0, 1])
        Previous_qualification_grade = st.number_input("Previous Qualification Grade", step=0.01)
        Mothers_qualification = st.number_input("Mother's Qualification", value=1)
        Fathers_qualification = st.number_input("Father's Qualification", value=1)
        Mothers_occupation = st.number_input("Mother's Occupation", value=0)
        Fathers_occupation = st.number_input("Father's Occupation", value=0)
        Admission_grade = st.number_input("Admission Grade", step=0.01)
        Displaced = st.selectbox("Displaced", [0, 1])
        Debtor = st.selectbox("Debtor", [0, 1])
        Tuition_fees_up_to_date = st.selectbox("Tuition Fees Up to Date", [0, 1])
        Gender = st.selectbox("Gender", [0, 1])
        Scholarship_holder = st.selectbox("Scholarship Holder", [0, 1])
        Age_at_enrollment = st.number_input("Age at Enrollment", value=18)

    with col2:
        Curricular_units_1st_sem_enrolled = st.number_input("1st Sem Units Enrolled", value=0)
        Curricular_units_1st_sem_evaluations = st.number_input("1st Sem Units Evaluated", value=0)
        Curricular_units_1st_sem_approved = st.number_input("1st Sem Units Approved", value=0)
        Curricular_units_1st_sem_grade = st.number_input("1st Sem Average Grade", step=0.01)
        Curricular_units_2nd_sem_enrolled = st.number_input("2nd Sem Units Enrolled", value=0)
        Curricular_units_2nd_sem_evaluations = st.number_input("2nd Sem Units Evaluated", value=0)
        Curricular_units_2nd_sem_approved = st.number_input("2nd Sem Units Approved", value=0)
        Curricular_units_2nd_sem_grade = st.number_input("2nd Sem Average Grade", step=0.01)
        Unemployment_rate = st.number_input("Unemployment Rate", step=0.01)
        Inflation_rate = st.number_input("Inflation Rate", step=0.01)
        GDP = st.number_input("GDP", step=0.01)
        SuccessRate_semester1 = st.number_input("Success Rate Semester 1", step=0.01)
        SuccessRate_semester2 = st.number_input("Success Rate Semester 2", step=0.01)
        Grade_improvement = st.number_input("Grade Improvement", step=0.01)
        Total_credit_enrolled = st.number_input("Total Credit Enrolled", value=0)
        Total_credit_approval = st.number_input("Total Credit Approved", value=0)
        is_financially_secure = st.selectbox("Is Financially Secure", [0, 1])
        economic_stress = st.number_input("Economic Stress", step=0.01)

    submitted = st.form_submit_button("🔍 Prediksi")

# Prediction
if submitted:
    # Data input sebagai dictionary
    input_dict = {
        'Application_mode': Application_mode,
        'Application_order': Application_order,
        'Course': Course,
        'Daytime_evening_attendance': Daytime_evening_attendance,
        'Previous_qualification_grade': Previous_qualification_grade,
        'Mothers_qualification': Mothers_qualification,
        'Fathers_qualification': Fathers_qualification,
        'Mothers_occupation': Mothers_occupation,
        'Fathers_occupation': Fathers_occupation,
        'Admission_grade': Admission_grade,
        'Displaced': Displaced,
        'Debtor': Debtor,
        'Tuition_fees_up_to_date': Tuition_fees_up_to_date,
        'Gender': Gender,
        'Scholarship_holder': Scholarship_holder,
        'Age_at_enrollment': Age_at_enrollment,
        'Curricular_units_1st_sem_enrolled': Curricular_units_1st_sem_enrolled,
        'Curricular_units_1st_sem_evaluations': Curricular_units_1st_sem_evaluations,
        'Curricular_units_1st_sem_approved': Curricular_units_1st_sem_approved,
        'Curricular_units_1st_sem_grade': Curricular_units_1st_sem_grade,
        'Curricular_units_2nd_sem_enrolled': Curricular_units_2nd_sem_enrolled,
        'Curricular_units_2nd_sem_evaluations': Curricular_units_2nd_sem_evaluations,
        'Curricular_units_2nd_sem_approved': Curricular_units_2nd_sem_approved,
        'Curricular_units_2nd_sem_grade': Curricular_units_2nd_sem_grade,
        'Unemployment_rate': Unemployment_rate,
        'Inflation_rate': Inflation_rate,
        'GDP': GDP,
        'SuccessRate_semester1': SuccessRate_semester1,
        'SuccessRate_semester2': SuccessRate_semester2,
        'Grade_improvement': Grade_improvement,
        'Total_credit_enrolled': Total_credit_enrolled,
        'Total_credit_approval': Total_credit_approval,
        'is_financially_secure': is_financially_secure,
        'economic_stress': economic_stress
    }

    # Ubah menjadi DataFrame
    input_df = pd.DataFrame([input_dict])

    # Prediksi
    prediction = model.predict(input_df)
    result = "✅ Tidak Dropout" if prediction[0] == 1 else "⚠️ Dropout"
    st.success(f"Hasil Prediksi: **{result}**")
