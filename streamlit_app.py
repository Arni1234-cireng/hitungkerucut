import streamlit as st
import math
st.title("menghitung :blue[volume kerucut] :rocket:")
r = st.number_input("masukan jari-jari (cm):",0) 
t = st.number_input("masukan tinggi (cm):",0)
if st.button("hitung volume", type="primary"):
  v = math.pi*(r**2)*t
  st.success(f'volume kerucut adalah (v:.2f')
