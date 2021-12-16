import math
import os
import random
import re
import sys

def gradesystem(grades):
    n = len(grades)
    out = [] #new array grades
    for i in range(n):
        grade = grades[i]
        # checking if the grade is less than 38
        if grade >= 38:
            if grade % 5:
                # check if the diffference between the grade and the next multiple of 5 is less than 3
                next_grade = ((grade//5)*5)+5
                # checking if the grade differnce is less than 3
                if (next_grade - grade) < 3:
                    out.append(next_grade)
                    continue
        out.append(grade)
    return out
grades = [57,73,67,38,33,60]
print(gradesystem(grades))
                
                
             
            
   
            
        
        
    