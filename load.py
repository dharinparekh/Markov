import json
def loadData(N):	
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


	for i in range(0,len(mainList)-(N-1)):
		 if mainList[i+(N-1)]=='*****':
			break
		 insertKey(mainList[i:i+N],dictionary,mainList[i+N])
		 
	with open('dictionary.json', 'wb') as save_file:
	    json.dump({str(k): v for k, v in dictionary.iteritems()},save_file)
	def getN():
		return N
	input_file.close()

