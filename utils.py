import streamlit as st
import pickle
import numpy as np
from pathlib import Path

def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

@st.cache(allow_output_mutation=True)
def load_model(path):
    with open(path,'rb') as f:
        loaded_model = pickle.load(f)
    return loaded_model

def generate(model,num_of_images):
    # import numpy as np

    sample = np.random.normal(size=(num_of_images,100))
    image = model(sample,training=False)
    return image

def read_markdown_file(markdown_file):
    return Path(markdown_file).read_text()