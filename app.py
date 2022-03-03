import streamlit as st
import pickle
import time
import tensorflow as tf
from pathlib import Path

def load_model(path):
    loaded_model = pickle.load(open(path, 'rb')) 
    return loaded_model

def read_markdown_file(markdown_file):
    return Path(markdown_file).read_text()

def generate(model,num_of_images):
    sample = tf.random.normal(shape=(num_of_images, 100))

    image = model(sample,training=False)
    return image

def show_image(num_of_images_to_create,model):
    model = load_model(model+'.pkl')
    image_tensor = generate(model,num_of_images=num_of_images_to_create)
    image_list = []
    for image in image_tensor:
        image_list.append(image.numpy())

    # if 'image_list' not in st.session_state:
    #     st.session_state['image_list'] = image_list
    # else:
    # st.session_state['image_list'] = image_list
        
    return image_list

def create_slider():
    return st.slider('Images to generate', min_value=4, max_value=32, value=8)

def select_model():
    model_list = ('128x128_dcgan_ada',)
    return st.selectbox('Generator model', options= model_list)


if __name__ == '__main__':
    
    st.title('Butterfly generator')
    with st.form("my_form"):
        cols = st.columns(2)
        with cols[0]:
            image_to_create = create_slider()
        with cols[1]:
            selected_model = select_model()

        submitted = st.form_submit_button("Generate")
       
    with st.container():
         if submitted:
            t0 = time.time()
            image_list = show_image(image_to_create,selected_model)
            st.image(image_list)
            st.write(f'generated in {(time.time() - t0):.2f}s')
    
    
    with st.container():
        st.title('The training')
        st.write('After 600 epochs, took almost 10 hours with Google Colab Pro')
        st.video('https://www.youtube.com/watch?v=3dvJhdYD04c')

        intro_markdown = read_markdown_file("./readme.md")
        st.markdown(intro_markdown, unsafe_allow_html=True)

        # st.video('https://www.youtube.com/watch?v=coQ5dg8wM2o&list=PL3XmeqnUuMw5VFBpSLwF9uMOLvFkE4fds&index=1')

        st.title('Connect')
        st.write('[Twitter](https://twitter.com/AnhKTrinh)')

    
