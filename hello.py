#Python Program To Use IBM Watson 
# Studio's Speech To Text Below Code 
# Accepts only .mp3 Format of Audio 
# File  
  
   
import json 
import csv
from os.path import join, dirname 
from ibm_watson import SpeechToTextV1 
from ibm_watson.websocket import RecognizeCallback, AudioSource 
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator 
import pandas as pd 
####################################################################################
#STT code
# Insert API Key in place of  
# 'YOUR UNIQUE API KEY' 
authenticator = IAMAuthenticator('C_1TyRl0w1rBHDJuz4RMbQZBZGhIzKjgbeegjL3RleSG')  
service = SpeechToTextV1(authenticator = authenticator) 
   
#Insert URL in place of 'API_URL'  
service.set_service_url('https://api.eu-gb.speech-to-text.watson.cloud.ibm.com/instances/4504d974-dd28-4a72-9a17-8d25d5818858') 
   
# Insert local mp3 file path in 
# place of 'LOCAL FILE PATH'  
with open(join(dirname('__file__'), r'./audio2.mp3'),  
          'rb') as audio_file: 
      
        dic = json.loads( 
                json.dumps( 
                    service.recognize( 
                        audio=audio_file, 
                        content_type='audio/mp3', #make sure to change content type according to files 
                        model='en-US_NarrowbandModel', #model
                        speaker_labels="true", #speaker labels to identify multiple speakers
                    continuous=True).get_result(), indent=2)) 
  
# Stores the transcribed text 
str = "" 
str2= ""  
results=dic.get('results')
speaker_labels=dic.get('speaker_labels')
print(dic)
#print(speaker_labels)
with open('data.json', 'w') as outfile:
    #for i in range(0, len(results)):
        #json.dump(results[i], outfile)
        #print (results[i])
    normalized_df = pd.json_normalize(results)
        #print(normalized_df['results'])
    df = pd.DataFrame(results, columns= ['transcript', 'confidence'])
    df = pd.DataFrame(speaker_labels, columns= ['from', 'to', 'speaker'])
    normalized_df.to_csv('my_csv_file4.csv',index=False)
#while bool(dic.get('results')):
#    str = dic.get('results').pop().get('alternatives').pop().get('transcript')
       
print(str) 

#print(dic) #dic is the whole json object

################################################################################################
#def json_csv(filename):
#    with open(filename) as data_file:
#        data = json.load(data_file)
#    return pd.DataFrame(data['result'])
#json_csv('response.json')

################################################################################################

