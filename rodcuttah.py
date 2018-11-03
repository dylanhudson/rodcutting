# -*- coding: utf-8 -*-
"""
Rod-Cutter eXtreme 3000 VISUAL MAX-QUANTUMIZER

@author nikola jovanovic
@author dylan hudson 

based on the formulation in CLRS third edition

"""
n = 10
prices = [0, 100, 5, 8, 9, 10, 17, 17, 20, 24, 30]
optimal_sub = [0 for x in range(n+1)]
optimal_string = ["" for x in range(n+1)]
cost_per_cut = 1000

for j in range(1,n+1):
  print ("rod length = %d" % j)  
  q =-10
  
  for i in range(1, j+1):
    string = ""
    
    for val in range(i):
        string = string + "-"
    string = string + "|"
     
    # if q will be updated with new value
    if q < (prices[i] + optimal_sub[j-i]):
        optimal_string[j] = string + optimal_string[j-i]
    
    print(string + optimal_string[j-i], end='')
    
    if j - i == 0:
        q = max(q, (prices[i] + optimal_sub[j-i] ) )
    else:
        q = max(q, (prices[i] + optimal_sub[j-i] - cost_per_cut ) )
        
    print(" %d" % (prices[i] + optimal_sub[j-i]))
    
  print ("\n * ")  
  optimal_sub[j] = q

print(optimal_sub[n])
