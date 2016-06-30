import ast
import json
from load import *

f_dictionary={}
word_count=0
words=[]
currentWord=''
prediction=''


with open('dictionary.json') as data_file:    
    loaded_dictionary=json.load(data_file)
for key in loaded_dictionary:
	f_dictionary[ast.literal_eval(key)]=loaded_dictionary[key]

while word_count<3:
	currentWord=raw_input()
	words.append(currentWord)
	word_count+=1
previousKey=()
while True:
	key_find=tuple(words[word_count-3:])
	if f_dictionary.has_key(key_find):
		if f_dictionary.get(key_find)!={}:
			prediction=max(f_dictionary.get(key_find).iterkeys(), key=(lambda key: f_dictionary.get(key_find)[key]))
			print 'prediction',prediction
	else :
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
	key_find=tuple(words[word_count-3:])
	if f_dictionary.has_key(key_find):
		checkKey(currentWord,f_dictionary[previousKey])
	else :
		f_dictionary[key_find]={}
		checkKey(currentWord,f_dictionary[previousKey])
	

