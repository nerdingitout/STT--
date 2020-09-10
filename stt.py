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
authenticator = IAMAuthenticator('C_1TyRl0w1rBHDJuz4RMbQZBZGhIzKjgbeegjL3RleSG')
service = SpeechToTextV1(authenticator = authenticator) 
   
#Insert URL in place of 'API_URL'  
service.set_service_url('https://api.eu-gb.speech-to-text.watson.cloud.ibm.com/instances/4504d974-dd28-4a72-9a17-8d25d5818858') 
   
# Insert local mp3 file path in place of 'LOCAL FILE PATH'  
with open(join(dirname('__file__'), r'./audio2.mp3'), #need to make this dynamic for different file names
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

#print(dic['results'][0])
transcript = []
word = []
end = []
speaker = []
start_s = []
end_s = []

#We are looking to create a dictionary of the words & speakers, both should be of the same size
#the start & end of timestamps don't match for the 'results' array and 'speaker_labels' array, therefore it's useless, we would need to do some extra manipulation to make it work

#print(dic['results'][0]['alternatives'][0]['transcript']) #test print of transcript

for i in range (len(dic['results'])):
    #transcript.append(dic['results'][i]['alternatives'][0]['transcript']) #we don't really need this right now
    for j in range (len(dic['results'][i]['alternatives'][0]['timestamps'])): #for loop, getting each recognized to put in dictionary 
        word.append(dic['results'][i]['alternatives'][0]['timestamps'][j][0]) #getting the words from the timestamps array. j refers to the timestamps object element that consists of {word, start, end}, 0 index at the end is for the word we want to extract and append to array
        #end.append(dic['results'][i]['alternatives']) #we dont really need it

for i in range (len(dic['speaker_labels'])):
    speaker.append(dic['speaker_labels'][i]['speaker']) #we only need this
    #start_s.append(dic['speaker_labels'][i]['from'])
    #end_s.append(dic['speaker_labels'][i]['to'])


#output word and speaker into csv file
output = {'word':word, 'speaker':speaker}
df = pd.DataFrame(data=output)
df.to_csv('helllooooo.csv',index=True)

#we will need to append the words for each speaker

transcript_str = ""
transcript = []
speaker_transcript = []
for i in range(len(word)):
    if(i==(len(word)-1)):
        transcript_str+=" "+word[i]
        transcript_str = transcript_str.replace("%HESITATION", "")
        transcript.append(transcript_str)
        speaker_transcript.append(speaker[i])
    elif(speaker[i]==speaker[i+1]):
        transcript_str+=" "+word[i]
    else:
        transcript_str = transcript_str.replace(" %HESITATION ", "")
        transcript.append(transcript_str)
        speaker_transcript.append(speaker[i])
        transcript_str=""

#output transcript and speaker into csv file
output = {'Transcript':transcript, 'speaker':speaker_transcript}
df = pd.DataFrame(data=output)
df.to_csv('transcript_speaker.csv',index=True)

print(transcript)