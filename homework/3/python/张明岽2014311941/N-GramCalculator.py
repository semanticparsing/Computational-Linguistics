# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 23:55:02 2017

@author: user
"""


file_object2 = open("data/01010101.txt",'r')

import os
#sentence="扶贫 开发 工作 取得 很 大 成绩";
sentence="扶贫 开发 工作 得到 很 大 成绩";

sentenceWords=sentence.split();
sLen=len(sentenceWords);

# calculate words frequency
rootdir = '.\data'
word_dict= {} 
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
                    if wordAndPOS[0] not in word_dict:   
                        word_dict[ wordAndPOS[0]] = 1  
                    else:  
                        word_dict[ wordAndPOS[0]] += 1    
        finally:
            file_object2.close()
            
#word_dict= sorted(word_dict.items(), key=lambda d:d[1], reverse = True)

#calculate frequency
# total number            
totalNum=0;
for key in word_dict:  
    totalNum+=word_dict.get(key);

# frequency 1    
frequency1=[];
sentenceFreq1=1.0;
for word in sentenceWords:
    freq=word_dict.get(word)/totalNum;
    sentenceFreq1*=freq;
    frequency1.append(freq);


print(sentenceFreq1,"\t")
for freq in frequency1:
    print(freq,"\t")
    
# frequency 2
frequency2=[];
numerator2=[0]*(len(sentenceWords)+1);
Denominator2=[0]*(len(sentenceWords)+1);

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
                rawWords=[];        #words without POS
                words=line.split();
                for word in words:  
                    wordAndPOS=word.split("/");
                    rawWords.append(wordAndPOS[0]);
                
                if rawWords[0]== sentenceWords[0]:
                    numerator2[0]=numerator2[0]+1;
                if rawWords[len(rawWords)-1]==sentenceWords[len(sentenceWords)-1]:
                    numerator2[len(sentenceWords)]=numerator2[len(sentenceWords)]+1;   
                for i in range(0,len(sentenceWords)-1):
                    for j in range(0,len(rawWords)-1):
                        if sentenceWords[i]==rawWords[j] and sentenceWords[i+1]==rawWords[j+1]:
                            numerator2[i+1]=numerator2[i+1]+1;
        finally:
            file_object2.close()


frequency2.append(word_dict.get(sentenceWords[0])/totalNum)
sentenceFreq2=frequency2[0];
for i in range(1,len(sentenceWords)):
    freq=numerator2[i]/word_dict.get(sentenceWords[i-1]);
    frequency2.append(freq);
    sentenceFreq2*=freq;
    

print("sentence2")
print(sentenceFreq2,"\t")
for freq in frequency2:
    print(freq,"\t")
    
#frequency3
freqHead=numerator2[0]/word_dict.get(sentenceWords[0]);
freqTail=numerator2[sLen-1]/word_dict.get(sentenceWords[sLen-1]);
sentenceFreq3=freqHead
for i in range(1,len(sentenceWords)):
    freq=numerator2[i]/word_dict.get(sentenceWords[i-1]);
    sentenceFreq3*=freq;
sentenceFreq4=sentenceFreq3*freqTail;
    

print("sentence2")
print(sentenceFreq2,"\t")
for freq in frequency2:
    print(freq,"\t")
        
#print(word_dict)
with open('4.txt', 'wt') as f:
    print(sentenceFreq1,"\t",file=f,end="")
    for freq in frequency1:
        print(freq,"\t",file=f,end="")
    print("",file=f);    
    print(sentenceFreq2,"\t",file=f,end="")
    for freq in frequency2:
        print(freq,"\t",file=f,end="")    
    
    print("",file=f);    
    print(sentenceFreq3,"\t",freqHead,file=f)
    print(sentenceFreq4,"\t",freqHead,freqTail,file=f)
        
           

