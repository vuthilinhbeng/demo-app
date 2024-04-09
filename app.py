import easyocr as ocr  #OCR
import streamlit as st  #Web App
from PIL import Image #Image Processing
import numpy as np #Image Processing 

#title
st.title("Easy OCR - Extract Text from Images- hi hi")

#subtitle
st.markdown("## Optical Character Recognition - Using `easyocr`, `streamlit` -  hosted on 🤗 Spaces")

<<<<<<< HEAD
st.markdown("Link to the app - [image-to-text-app on 🤗 Spaces](https://huggingface.co/spaces/BENGGIA/Demo-new)")
=======
st.markdown("Link to the app - [image-to-text-app on 🤗 Spaces](https://huggingface.co/spaces/BENGGIA/Demo-newp)")
>>>>>>> 66adbf22539b9627a9ece20333441088cc9afedc

#image uploader
image = st.file_uploader(label = "Upload your image here",type=['png','jpg','jpeg'])


@st.cache
def load_model(): 
    reader = ocr.Reader(['en'],model_storage_directory='.')
    return reader 

reader = load_model() #load model

if image is not None:

    input_image = Image.open(image) #read image
    st.image(input_image) #display image

    with st.spinner("🤖 AI is at Work! "):
        

        result = reader.readtext(np.array(input_image))

        result_text = [] #empty list for results


        for text in result:
            result_text.append(text[1])

        st.write(result_text)
    #st.success("Here you go!")
    st.balloons()
else:
    st.write("Upload an Image")

st.caption("Made with ❤️ by @1littlecoder. Credits to 🤗 Spaces for Hosting this ")
