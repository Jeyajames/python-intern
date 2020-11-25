Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #merge two python dictionaries
>>> dict1={1:"welcome",2:"to",3:"our"}
>>> dict2={4:"python",5:"internship"}
>>> dict1.update(dict2)
>>> dict1
{1: 'welcome', 2: 'to', 3: 'our', 4: 'python', 5: 'internship'}
>>> #remove a key from a dictionary
>>> stud={"name":"janu","age":20,"state":"tamilnadu"}
>>> del stud['state']
>>> print(stud)
{'name': 'janu', 'age': 20}
>>> #to map  two list into a dictionary
>>> key=['tamilnadu','bihar','karnataka']
>>> value=['chennai','patna','bengaluru']
>>> dictionary=dict(zip(key,value))
>>> print(dictionary)
{'tamilnadu': 'chennai', 'bihar': 'patna', 'karnataka': 'bengaluru'}
>>> #to find the length of a set
>>> set={9,5,2,7,1,3,4}
>>> print(len(set))
7
>>> # to remove the intersection of a 2nd set from the 1st set
>>> s1={'c','y','w','p','m'}
>>> s2={'v','a','m','x','q'}
>>> print(s1-s2)
{'p', 'y', 'w', 'c'}
>>> 