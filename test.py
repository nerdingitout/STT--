import pandas as pd
import json
import csv



# importing the module 
import json 
  
# Opening JSON file 
with open('response.json') as json_file: 
    data = json.load(json_file) 
  
    # for reading nested data [0] represents 
    # the index value of the list 
    print(data['results'][0]['alternatives']['transcript']) 
      
    # for printing the key-value pair of 
    # nested dictionary for looop can be used 
    print("\nPrinting nested dicitonary as a key-value pair\n") 
    for i in data['people1']: 
        print("Name:", i['name']) 
        print("Website:", i['website']) 
        print("From:", i['from']) 
        print() 


#def json_csv(filename):
#    with open(filename) as data_file: #opening json file
#        data = json.load(data_file) #loading json data
#        normalized_df = pd.json_normalize(data)
#        print(normalized_df['results'][0])
#        normalized_df.to_csv('my_csv_file.csv',index=False)
#    return pd.DataFrame(data['results'])

json_csv('response.json') #calling the json_csv function, paramter is the source json file 

#file = open('response.json')
#obj = json.load(file)
#for element in obj['results']:
#  for alternative in element['alternatives']:
#    for stamp in alternative['timestamps']:
#      name, value1, value2 = stamp
#      print(stamp)
