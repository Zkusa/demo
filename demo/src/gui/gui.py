import streamlit as st
import requests

st.set_page_config(
    page_title="Preprocessing Text",
    layout="wide",
)

st.title("Ứng dụng tiền xử lý văn bản Tiếng Việt", )

text_input = st.text_area("Nhập văn bản cần xử lý:")
                
if st.button("Xử lý"):
    response = requests.post("http://fastapi:8000/process", json={"text": text_input})
    result = response.json()
    st.write(result)
