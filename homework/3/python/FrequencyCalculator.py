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