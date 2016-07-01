import ast
import json
import os
from load import loadData

N=int(raw_input("Enter the order: ")) #N stands for n-th order markov chain
f_dictionary={}                       #this dictionary contains the original contents in json file and also the ones after changing the data ccording 						to user input
word_count=0			      #counts the number of words
words=[]				#list of all words
currentWord=''				#the current word 
prediction=''				#the value which we predicted

loadData(N)				#calls the loadData from load.py which creates the json dictionary

with open('dictionary.json') as data_file:    #loads data from the json to loaded_dictionary
    loaded_dictionary=json.load(data_file)
for key in loaded_dictionary:			#json cant store dictionaries with tuple as keys so it is stored as string to evaluate it back to tuple
	f_dictionary[ast.literal_eval(key)]=loaded_dictionary[key]

while word_count<N:			#do no prediction for the starting N words
	currentWord=raw_input()
	words.append(currentWord)
	word_count+=1
previousKey=()				#previousKey stores the previous values of key
while True:
	
	key_find=tuple(words[word_count-N:])	#the current value of key
	if f_dictionary.has_key(key_find):
		if f_dictionary.get(key_find)!={}:
			prediction=max(f_dictionary.get(key_find).iterkeys(), key=(lambda key: f_dictionary.get(key_find)[key]))
			if prediction !='*****':
				print 'prediction',prediction
	else :	
		f_dictionary[key_find]={}
		print 'no prediction'
	previousWord=currentWord	
	currentWord=raw_input()
	if currentWord=='exit':
		choice=raw_input('Do you want to save it to json?')
		if choice == 'y' or choice =='yes':
			with open('dictionary.json', 'wb') as save_file:
    				json.dump({str(k): v for k, v in f_dictionary.iteritems()},save_file)
			pass
		exit()
	word_count+=1
	words.append(currentWord)
	previousKey=key_find	
	key_find=tuple(words[word_count-N:])
	if f_dictionary.has_key(key_find):
		if currentWord in f_dictionary[previousKey]:
			 	f_dictionary[previousKey][currentWord]+=1
		else :		
	 			f_dictionary[previousKey][currentWord]=1
	else :
		f_dictionary[key_find]={}
		if currentWord in f_dictionary[previousKey]:
			 	f_dictionary[previousKey][currentWord]+=1
		else :		
	 			f_dictionary[previousKey][currentWord]=1
		
