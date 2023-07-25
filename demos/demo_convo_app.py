# import module numpy
import numpy as np

# import module streamlit
import streamlit as st

with st.chat_message("user"):
    st.markdown("What is up?")
    st.line_chart(np.random.randn(30, 3))

prompt = st.chat_input("What is up?")
if prompt:
    st.write(f'User said: {prompt}')
