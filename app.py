import streamlit as st
import time
from utils import load_css, load_model, generate,read_markdown_file


def show_image(num_of_images_to_create,model):
    model = load_model(model+'.pkl')
    image_tensor = generate(model,num_of_images=num_of_images_to_create)
    image_list = []
    for image in image_tensor:
        image_list.append(image.numpy())
        
    return image_list

def create_slider():
    return st.slider('Images to generate', min_value=4, max_value=32, value=8)

def select_model():
    model_list = ('128x128_dcgan_ada',)
    return st.selectbox('Generator model', options= model_list)


if __name__ == '__main__':
  
    load_css("./assets/style.css")
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

        st.title('Connect')
        st.write('[Twitter](https://twitter.com/AnhKTrinh)')

    
