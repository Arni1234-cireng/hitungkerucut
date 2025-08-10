import streamlit as st

st.title("menghitung :blue[volume kerucut] :rocket:")
r = st.number_input("masukan jari-jari (cm):",0) 
t = st.number_input("masukan tinggi (cm):",0)
if st.button("hitung volume", type="primary"):
  v = math.phi*(r**2)*t
  st.succes(f'volume kerucut adalah(v):.2f)'
