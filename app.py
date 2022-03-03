import streamlit as st
import pickle
import time
import tensorflow as tf

def load_model(path):
    loaded_model = pickle.load(open(path, 'rb')) 
    return loaded_model

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
    st.session_state['image_list'] = image_list
        
    return image_list

def create_slider():
    return st.slider('Images to generate', min_value=4, max_value=32, value=8)

def select_model():
    model_list = ('128x128_dcgan_ada',)
    return st.selectbox('Generator model', options= model_list)


if __name__ == '__main__':
    t0 = time.time()
    st.title('Butterfly generator')

    
    with st.container():
    # print(image)
        image_to_create = create_slider()
        selected_model = select_model()
      
        st.button('Generate', on_click=show_image,args = [image_to_create,selected_model] )
        st.write(f'total time {time.time() - t0}')
    
    if 'image_list' in st.session_state:
        st.image(st.session_state['image_list'])
    



    
