#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install ibm_watson


# In[2]:


pip install ibm_cloud_sdk_core


# In[3]:


from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator


# In[10]:


api=IAMAuthenticator("3jY6Ru2dhR1dXbWpIly2Oujo2AgEfudLpbGw2a8adQXS")
text_2_speech=TextToSpeechV1(authenticator=api)


# In[11]:


text_2_speech.set_service_url("https://api.eu-gb.text-to-speech.watson.cloud.ibm.com/instances/2ff794a9-c7cf-4066-9274-1f79dcfab64a")


# In[15]:


with open("welcome3.mp3","wb") as audiofile:
    audiofile.write(
    text_2_speech.synthesize("hi latha.", accept="audio/mp3").get_result().content)


# In[ ]:




