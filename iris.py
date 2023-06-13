import pickle
import streamlit as st

# membaca model
iris_model = pickle.load(open('iris_model.sav', 'rb'))

#judul web
st.title('Prediksi Spesies Tumbuhan Iris')

#membagi kolom
col1, col2 = st.columns(2)

with col1 :
    SLCm = st.number_input ('Panjang Sepal Bungan Dalam Cm')
    SWCm = st.number_input ('Lebar Sepal Bungan Dalam Cm')
with col2:
    PLCm = st.number_input ('Panjang Kelopak Bungan Dalam Cm')
    PWCm = st.number_input ('Lebar Kelopak Bungan Dalam Cm')

# code untuk prediksi
iris_species = ''

# membuat tombol untuk prediksi
if st.button('Test Prediksi iris'):
    iris_predict = iris_model.predict([[SLCm, SWCm, PLCm, PWCm]])

    if iris_predict == 0:
        iris_species = 'Tumbuhan Termasuk Kedalam Kelompok Iris Setosa'
    elif iris_predict == 1:
        iris_species = 'Tumbuhan Termasuk Kedalam Kelompok Iris Versicolor'
    else:
        iris_species = 'Tumbuhan Termasuk Kedalam Kelompok Iris Virginica'
st.success(iris_species)
