#!/usr/bin/env python
# coding: utf-8

# In[11]:


import streamlit as st
from docx import Document
import os
from google import genai


# In[14]:


st.set_page_config("Resume Analyzer",layout='wide')
st.caption("Please upload only word file, As of now this tool only can read word file..")
st.header("Resume Analyzer")
path=st.file_uploader("Upload your Resume",[".docx"])

def cv_anlayzer(upload_file):
    doc=Document(upload_file)
    txt=""
    for p in doc.paragraphs:
        txt+=p.text+"\n"
    return txt
if 'ch' not in st.session_state:
    st.session_state['ch']=False

if path:
    extractedtext=cv_anlayzer(path)
    st.subheader("Extrcated text from Resume")
    st.text_area(label="Resume text",value=extractedtext,height=500)
    st.session_state['ch']=True


if st.session_state['ch']:
    if st.button("Analyse your Resume.."):
        client=genai.Client(api_key="AQ.Ab8RN6KzwB8ETPPM8g-U6Xb2zIszC5pnh7cDmipd9lwyPT0_yQ")
        promot=f"""
        Please analyse the attached Resume and Cv and help me with below feed back.
        #1. Help with improvement part from cv {extractedtext}
        #2. Rate CV 
        #3. Good Points as well
        """
        with st.spinner("Processing your request please wait.."):
            responsetext=client.models.generate_content(model="gemini-2.5-flash",contents=promot)
        st.write(responsetext.text)
        st.success("Done")



# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




