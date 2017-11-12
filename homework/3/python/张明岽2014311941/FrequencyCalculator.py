# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 23:55:02 2017

@author: user
"""

"""
关于readlines()方法：
1、一次性读取整个文件。
2、自动将文件内容分析成一个行的列表。
"""
file_object2 = open("data/01010101.txt",'r')

''' first test, output all
try:
  lines = file_object2.readlines()
  print("type(lines)=",type(lines)) #type(lines)= <type 'list'>
  for line in lines:
      print("line=",line)  
finally:
    file_object2.close()
'''

''' test2 get frequency of words in a single file
word_lst = []  
word_dict= {} 
try:
  lines = file_object2.readlines()
  for line in lines:
      words=line.split();
      for word in words:  
          if word not in word_dict:   
              word_dict[word] = 1  
          else:  
              word_dict[word] += 1    
finally:
    file_object2.close()
    
for key in word_dict:  
    print(key,word_dict[key])
'''

''' second test, calculate frequency and ignore the POS
import os

rootdir = '.\data'
word_dict= {} 
list = os.listdir(rootdir) #列出文件夹下所有的目录与文件
for i in range(0,len(list)):
    path = os.path.join(rootdir,list[i])
    if os.path.isfile(path):
        #你想对文件的操作      
        file_object2 = open(path,'r')
        try:
            lines = file_object2.readlines()
            for line in lines:
                words=line.split();
                for word in words:  
                    if word not in word_dict:   
                        word_dict[word] = 1  
                    else:  
                        word_dict[word] += 1    
        finally:
            file_object2.close()
            
word_dict= sorted(word_dict.items(), key=lambda d:d[1], reverse = True)
#print(word_dict)
for key in word_dict:  
    print(key[0],",",key[1])

'''

import os

ignoredPOS=['m','w','t'];

rootdir = '.\data'
word_dict= {} 
word_POS={}
list = os.listdir(rootdir) #列出文件夹下所有的目录与文件
for i in range(0,len(list)):
    path = os.path.join(rootdir,list[i])
    if os.path.isfile(path):
        #你想对文件的操作      
        file_object2 = open(path,'r')
        try:
            # read a line
            lines = file_object2.readlines()
            for line in lines:
                # split the line into words
                words=line.split();
                for word in words:  
                    wordAndPOS=word.split("/");
                    if(len(wordAndPOS)==2 and (wordAndPOS[1] not in ignoredPOS)):
                        if wordAndPOS[0] not in word_dict:   
                            word_dict[ wordAndPOS[0]] = 1  
                            word_POS[ wordAndPOS[0]] = wordAndPOS[1]  
                        else:  
                            word_dict[ wordAndPOS[0]] += 1    
        finally:
            file_object2.close()
            
word_dict= sorted(word_dict.items(), key=lambda d:d[1], reverse = True)
#print(word_dict)
with open('1.txt', 'wt') as f:
    for key in word_dict:  
#        print(key[0],"\t",word_POS[key[0]],"\t",key[1],file=f)
        print(key[0],"\t",key[1],file=f)
        
        
# draw scatterplot
from matplotlib import pyplot as plt
import numpy as np
import matplotlib

# Fixing random state for reproducibility
np.random.seed(19680801)


x = np.arange(0,len(word_dict),1);
y = [];
for key in word_dict:  
    y.append(key[1]);
x=np.log(x);
y=np.log(y);

plt.scatter(x, y, alpha=0.5,s=1, label="Zipf's Plot")
plt.xlabel("Rank(log)")
plt.ylabel("Frequency(log)")
plt.show()        

