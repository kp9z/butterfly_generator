import streamlit as st
import pickle
import tensorflow as tf
from pathlib import Path

def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


def load_model(path):
    loaded_model = pickle.load(open(path, 'rb')) 
    return loaded_model

def generate(model,num_of_images):
    sample = tf.random.normal(shape=(num_of_images, 100))
    image = model(sample,training=False)
    return image

def read_markdown_file(markdown_file):
    return Path(markdown_file).read_text()