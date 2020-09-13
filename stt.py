
#Python Program To Use IBM Watson 
# Studio's Speech To Text Below Code 
# Accepts only .mp3 Format of Audio file  
   
import json 
import csv
from os.path import join, dirname 
from ibm_watson import SpeechToTextV1 
from ibm_watson.websocket import RecognizeCallback, AudioSource 
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator 
import pandas as pd 

#STT code
# Insert API Key in place of  
# 'YOUR UNIQUE API KEY' 
authenticator = IAMAuthenticator('L7TjOs4c3uLRC1Bo8ase4WNnQctkXzl4V5QhDeaTNBaU')
service = SpeechToTextV1(authenticator = authenticator) 
   
#Insert URL in place of 'API_URL'  
service.set_service_url('https://api.us-south.speech-to-text.watson.cloud.ibm.com/instances/84bee29a-fbfb-4478-b663-dee53f596234') 
   
# Insert local mp3 file path in place of 'LOCAL FILE PATH'  
#with open(join(dirname('__file__'), r'./audio2.mp3'), #need to make this dynamic for different file names
with open('audio2.mp3', 'rb') as audio_file: 
      
        dic = json.loads( 
                json.dumps( 
                    service.recognize( 
                        audio=audio_file, 
                        content_type='audio/mp3', #make sure to change content type according to files 
                        model='en-US_NarrowbandModel', #model
                        speaker_labels="true", #speaker labels to identify multiple speakers
                    continuous=True).get_result(), indent=2)) 


  





#We are looking to create a dictionary of the words & speakers, both should be of the same size
#the start & end of timestamps don't match for the 'results' array and 'speaker_labels' array, therefore it's useless, we would need to do some extra manipulation to make it work

word = []
speaker = []

for i in range (len(dic['results'])):
    
    for j in range (len(dic['results'][i]['alternatives'][0]['timestamps'])): #for loop, getting each recognized to put in dictionary 
        word.append(dic['results'][i]['alternatives'][0]['timestamps'][j][0]) #getting the words from the timestamps array. j refers to the timestamps object element that consists of {word, start, end}, 0 index at the end is for the word we want to extract and append to array

for i in range (len(dic['speaker_labels'])):
    speaker.append(dic['speaker_labels'][i]['speaker']) #we only need this
   
clean_words=[]
clean_speakers=[]

#Creating new lists without the "%HESITATION"
for i in range (len(word)):
    if (word[i] != '%HESITATION'):
        clean_words.append(word[i])
        clean_speakers.append(speaker[i])
      
#output word and speaker into csv file
output = {'word':clean_words, 'speaker':clean_speakers}
df = pd.DataFrame(data=output)
df.to_csv('helllooooo.csv',index=True)



#Reconstructing every sentence with its corresponding speaker
transcript_str = ""
speaker_transcript = []
client =[]
agent = []

for i in range(len(clean_speakers)):
    if i==0:
        current_speaker= clean_speakers[i]
       
    if current_speaker == clean_speakers[i]:
        transcript_str += clean_words[i]+" "
        
    else:
        if current_speaker == 0:
            client.append(transcript_str.lower())
        else:
            agent.append(transcript_str.lower())

        transcript_str = ""
        transcript_str += clean_words[i]+" "

        current_speaker = clean_speakers[i]

    if (i==len(clean_speakers)-1):
        if current_speaker == 0:
            client.append(transcript_str.lower())
        else:
            agent.append(transcript_str.lower())    
        #transcript_str = ""    

            
#output transcript and speaker into csv file
output = {'Client':client, 'Agent':agent}
df = pd.DataFrame(data=output)
df.to_csv('transcript_speaker2.csv',index=True)

#print(transcript)

