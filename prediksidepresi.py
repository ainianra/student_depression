import pickle
import streamlit as st
import numpy as np

# Load model yang sudah disimpan
model = pickle.load(open('model_regresi_depresi.sav', 'rb'))

# Judul aplikasi
st.title('Prediksi Tingkat Depresi Mahasiswa')

# Input data dari user
age = st.number_input('Usia Mahasiswa')
academic = st.number_input('Tekanan Akademik (1-5)')
work = st.number_input('Tekanan Pekerjaan (1-5)')
cgpa = st.number_input('IPK')
study_sat_1 = st.checkbox('Kepuasan Studi: Sangat Tidak Puas')
study_sat_2 = st.checkbox('Kepuasan Studi: Tidak Puas')
study_sat_3 = st.checkbox('Kepuasan Studi: Netral')
study_sat_4 = st.checkbox('Kepuasan Studi: Puas')
study_sat_5 = st.checkbox('Kepuasan Studi: Sangat Puas')
job_sat_1 = st.checkbox('Kepuasan Kerja: Sangat Tidak Puas')
job_sat_2 = st.checkbox('Kepuasan Kerja: Tidak Puas')
job_sat_3 = st.checkbox('Kepuasan Kerja: Netral')
job_sat_4 = st.checkbox('Kepuasan Kerja: Puas')
work_study_hrs = st.number_input('Jam Kerja/Belajar per Hari')

# Siapkan input untuk prediksi
input_data = np.array([[
    age, academic, work, cgpa,
    int(study_sat_1), int(study_sat_2), int(study_sat_3),
    int(study_sat_4), int(study_sat_5),
    int(job_sat_1), int(job_sat_2), int(job_sat_3),
    int(job_sat_4), work_study_hrs
]])

# Prediksi saat tombol ditekan
if st.button('Prediksi Tingkat Depresi'):
    prediction = model.predict(input_data)
    st.success(f'Prediksi Skor Depresi: {prediction[0]:.2f}')