# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 12:08:18 2016
@author: Özlem Yönder
"""
'''For comparison of Delta_K=0 (parallel) transition files
from the output of November 9, 2016 version of pattern_match_nov9.py'''

import os
# import numpy

# User input    
date=input('Please enter the date of the file as yyyy-mm-dd:')
MaxK=eval(input('Please enter the Max K value you searched for:'))
tol_B=eval(input('Please enter a tolerance for the 2B:'))
tol_delta_M=eval(input('Please enter a tolerance for the delta_M:'))
'''        
name_dict={}
for gsK in range(MaxK):
    file_name="delK_0_gsK_"+str(gsK)+"_"+date+".txt"
    print(file_name)
    if os.path.isfile(file_name):
        dicK='K='+str(gsK)
        name_dict[dicK] = file_name 
print(name_dict)
'''
DataSetList=[]
existing_gsK=[] 
      
for gsK in range(MaxK,-1,-1):
    file_name="delK_0_gsK_"+str(gsK)+"_"+date+".txt"

  
    if os.path.isfile(file_name):
        existing_gsK.append(gsK)
        with open(file_name,'r') as rf:
            #Count the number of lines in the file and store the corresponding 
            #K value for the existing files in the list existing_gsK.  
            numlines=0
            while(True):
                numlines+=1
                f_lines=rf.readline()
                if(len(f_lines)==0):
                    break
            
            #Start reading the file from the beginning                
            rf.seek(0)
            
            #Read the first 13 lines which contains only text            
            for i in range(13):
                rf.readline()
                
            #Store the data in the list DataSetList
            for l in range(numlines):
                line=rf.readline()
                a=line.split()
                if(len(a)==9):
                    a=[float(x) for x in a]
                    DataSetList.append(a)  

                
#print(DataSetList)
#print(existing_gsK)

#Find the final index to know how many labels you used.
final_index=int(DataSetList[-1][-1])

#Here we go! This is not the best way to do it probably. But enjoy it... :D
ListofPossibleDummySet=[]
ListofPossibleSet=[]
for first_index in range(final_index,-1,-1):
    for sec_index in range(final_index,-1,-1):
        if(sec_index!=first_index):
            for i in range(len(DataSetList)):
                if int(DataSetList[i][-1])==(first_index):
                 #   first_J=DataSetList[i][-1]
                    for j in range(len(DataSetList)):
                        #If the J values are equal
                        #If the delta_J values are equal
                        #If the K value of the first set (index i) is larger than the the second set (index j)
                        #If the difference between the 2B is within your tolerance
                        #Then calculate the energy difference between them
                        if int(DataSetList[j][-1])==float(sec_index) and \
                            DataSetList[i][4]==DataSetList[j][4] and \
                            DataSetList[i][-3]==DataSetList[j][-3] and \
                            DataSetList[i][-2]>DataSetList[j][-2] and \
                            abs(DataSetList[i][-4]-DataSetList[j][-4])<tol_B:
                            delta_E=DataSetList[i][1]-DataSetList[j][1]
#                            print('The Energy Difference is', delta_E)
                            #If te energy of the higher K is larger then calculate delta_M
                            if delta_E>0:
                                Kfirst=DataSetList[i][-2]
                                Ksec=DataSetList[j][-2]
                                #delta_E=delta_M*(K(higher K)^2-K(lower_K)^2)
                                delta_M=delta_E/(Kfirst*Kfirst-Ksec*Ksec)
                                if delta_M<tol_delta_M:
                                    # print('delta_M=',delta_M)
                                    # Search for the third set which is within this requirement
                                    for third_index in range(final_index,-1,-1):
                                        if(third_index!=first_index and third_index!=sec_index):
                                            for k in range(len(DataSetList)):
                                                if int(DataSetList[k][-1])==float(third_index) and \
                                                    DataSetList[i][4]==DataSetList[k][4] and \
                                                    DataSetList[i][-3]==DataSetList[k][-3] and \
                                                    DataSetList[i][-2]>DataSetList[k][-2] and \
                                                    abs(DataSetList[i][-4]-DataSetList[k][-4])<tol_B:
                                                    delta_E_third=DataSetList[i][1]-DataSetList[j][1]
                                                    Kthird=DataSetList[j][-2]
                                                    delta_E_ref_max=(Kfirst*Kfirst-Kthird*Kthird)*(delta_M+tol_delta_M)
                                                    if delta_E_ref_max>delta_E_third>0:
                                                        ListofPossibleDummySet.append(DataSetList[i])
                                                        ListofPossibleDummySet.append(DataSetList[j])                                                     
                                                        ListofPossibleDummySet.append(DataSetList[k])
                                                        ListofPossibleSet=ListofPossibleDummySet
                                                    else:
                                                        ListofPossibleDummySet=[]
                                                        ListofPossibleSet=[]
                                                    if ListofPossibleSet!=[]:
                                                        with open('ListofPossibleSet.txt','a') as wf:
                                                            wf.write('New Set')
                                                            for s in ListofPossibleSet:
                                                                wf.write(str(s) + '\n')
   #     print('New Set') 
   #     print(ListofPossibleSet)
                                                    #    with open('file_name.txt','w') as wf:
                                                    #        wf.write('New Set')
                                                    #        wf.write(ListofPossibleDummySet)
                                            

   #         matches = [x for x in DataSetList[:][-1] if int(x)==sec_index]
       #     print(matches)
      #      for thrd_index in range(final_index,-1,-1):
         #       if(thrd_index!=first_index and thrd_index!=sec_index):
          #          print("je t'aime mon third_index",thrd_index)
'''
#    with open(file_name,'r') as rf:
#        f_contents=rf.read()
#        print(f_contents)
'''