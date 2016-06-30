import json
input_file=open('dataset.txt','r')
dictionary={}
mainList=input_file.read().split()
mainList.append('*****')

def checkKey(key,dicti):
	if key in dicti:
		 	dicti[key]+=1
	else :		
 			dicti[key]=1
 

def insertKey(temp,dictionary,nextWord):
	 tupleMain=tuple(temp)
	 if tupleMain in dictionary:
		checkKey(nextWord,dictionary[tupleMain])
	 else :
		dictionary[tupleMain]={nextWord:1}


for i in range(0,len(mainList)-2):
	 if mainList[i+2]=='*****':
		break
	 insertKey(mainList[i:i+3],dictionary,mainList[i+3])
	 
with open('dictionary.json', 'wb') as save_file:
    json.dump({str(k): v for k, v in dictionary.iteritems()},save_file)

input_file.close()

