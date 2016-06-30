1)dataset.txt has the stored data or the training data of the model
2)load.py trains the model and saves it in the file dictionary.json
3)testing.py has the complete implementation of real time words

The data model I have followed is
-> I will pair up 3 words of a list
-> create a tuple from the list
-> use the created tuple as the key for the dictionary
-> the value of the dictionary will again be a dictionary which has the next words as keys and its frequency as values

so for example the input is

"hello i am dharin hello i am riteek hello i am ankur hello i am vishwa hello i am dharin and we love to code"

the dictionary will be of the form
{"('dharin', 'and', 'we')": {"love": 1},
 "('am', 'riteek', 'hello')": {"i": 1},
 "('i', 'am', 'ankur')": {"hello": 1},
 "('love', 'to', 'code')": {"*****": 1},
 "('dharin', 'hello', 'i')": {"am": 1},
 "('i', 'am', 'dharin')": {"and": 1, "hello": 1},
 "('and', 'we', 'love')": {"to": 1},
 .....
 .....
 .....
 "('hello', 'i', 'am')": {"riteek": 1, "vishwa": 1, "dharin": 2, "ankur": 1},

This all will happen when we run the file 'load.py'

Now after creating a model we can run 'testing.py' which will first take 3 buffer inputs that is wont predict anything in these inputs as we have a 3rd order model. We cant predict from the first command.

so suppose you type the first three words as 1)hello 2)i 3)am
it will output a simple string saying 'prediction dharin'
you can obviously type anything then
take an example we typed
1)'vishwa'
	It will increase the frequency in the 
		"('hello', 'i', 'am')": {"riteek": 1, "vishwa": 2, "dharin": 2, "ankur": 1},
2)'xyz'
	It will add a new entry with frequency 1
		"('hello', 'i', 'am')": {"riteek": 1, "vishwa": 1, "dharin": 2, "ankur": 1."xyz":1},

Basically the model changes dynamically according to the input
The word 'exit' will end the testing.py and ask us if we want to save the new model or let our old model remain.

this is the work progress yet.


Doubts and Mistakes:
1) what to do In case of same frequency? i think it will choose the one which comes first as i am using the max() function.
2) "('love', 'to', 'code')": {"*****": 1}, i am marking the end of file using '*****' so if we ever type 'love to code' as input it will give prediction '*****'



