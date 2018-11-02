# -*- coding: utf-8 -*-
"""
Rod-Cutter eXtreme 3000 VISUAL MAX-QUANTUMIZER

@author nikola jovanovic
@author dylan hudson 

based on the formulation in CLRS third edition

"""
n = 10
prices = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
optimal_sub = [0 for x in range(n+1)]
optimal_string = ["" for x in range(n+1)]


for j in range(1,n+1):
  print ("rod length = %d" % j)  
  q =-10
  
  for i in range(1, j+1):
    #print(i)
    #print(p[i])
    #print(r[j-i])
    #print("|")
    string = ""
    
    for val in range(i):
        string = string + "-"
    string = string + "|"
    
   # for val in range(j-i):
   #     print ("-", end='')   
    #previous q remains larger
    if q > (prices[i] + optimal_sub[j-i]):
        pass
    #if q will be updated with new value
    if q < (prices[i] + optimal_sub[j-i]):
        optimal_string[j] = string + optimal_string[j-i]
    
    print(string + optimal_string[j-i], end='')
    q = max(q, (prices[i] + optimal_sub[j-i]) )
    
    print(" %d" % (prices[i] + optimal_sub[j-i]))
    
  print ("\n * ")  
  optimal_sub[j] = q

print(optimal_sub[n])