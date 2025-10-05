import streamlit as st
import pickle
from PIL import Image
import numpy as np

def main():
    st.markdown("<h1 style='color:purple'>IRIS FLOWER CLASSIFICATION</h1>", unsafe_allow_html=True)

   
    image = Image.open(r"C:\Users\acer\Downloads\IRIS\iris.jpg")
    st.image(image, width=600)

    st.markdown("### Enter flower details:")

    sl = st.text_input('Sepal Length (cm)', '')
    sw = st.text_input('Sepal Width (cm)', '')
    pl = st.text_input('Petal Length (cm)', '')
    pw = st.text_input('Petal Width (cm)', '')

   
    model = pickle.load(open('iris_model_knn.sav1', 'rb'))
    scaler = pickle.load(open('iris_scaler_knn.sav1', 'rb'))

 
    if st.button('PREDICT'):
        try:
        
            features = [float(sl), float(sw), float(pl), float(pw)]
            
           
            scaled_features = scaler.transform([features])

   
            pred_array = model.predict(scaled_features)

        
            if pred_array.ndim > 1:
                prediction = pred_array.argmax(axis=1)[0]
            else:
                prediction = pred_array[0]

        
            if prediction == 0:
                st.success("🌸 The flower is Iris-setosa")
            elif prediction == 1:
                st.success("🌼 The flower is Iris-versicolor")
            else:
                st.success("🌺 The flower is Iris-virginica")
        
        except ValueError:
            st.error("❌ Please enter valid numeric values for all fields.")

if __name__ == '__main__':
    main()
