# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 14:16:06 2024

@author: USER
"""

#task 1

def SearchA(Arr,x):
    index=[i for i in range (len(Arr)) if Arr[i] == x]
    return index
           
        
arr=[22,2,1,7,11,13,5,2,9]
#n=int(input("Enter the number:"))
i=SearchA(arr, 2)
print("Index=", i)


#task 2

def SearchA(Arr,x):
    index=[i for i in range (len(Arr)) if Arr[i] == x]
    return index
            
arr=[22,2,1,7,11,13,5,2,9]
sortedArr=sorted(arr)
#n=int(input("Enter the number:"))
i=SearchA(sortedArr, 2)
print("Index=", i)

#task 3
def Minimum(Arr,starting,ending):
    integer=starting
    for i in range(starting, ending+1):
        if Arr[i]<Arr[integer]:
            integer=i
                 
    return integer

arr=[3,4,7,8,0,1,23,-2,-5]   
startingIndex=4
endingIndex=7
output=Minimum(arr, startingIndex, endingIndex)
print("Output=" , output)

#task 4
def Sort4(Arr):
    for i in range(len(Arr)):
        minIndex=Minimum(Arr, i, len(Arr)-1)
        Arr[i],Arr[minIndex]=Arr[minIndex],Arr[i]
    return Arr

arr=[3,4,7,8,0,1,23,-2,-5]   
sort=Sort4(arr)
print(sort)  

#task 5
def StringReverse(str,starting, ending):
    return str[starting:ending][::-1]

    
s="University of Engineering and Technology Lahore"
output=StringReverse(s, 27, 41)
print(output)

#task 6
def SumIterative(number):
    n=0
    while number > 0:
        n += number % 10
        number //= 10
    return n
    
output=SumIterative(1524)

print("Sum of Integer is: ", output)
def SumRecursive(number):      
    if number == 0:
        return 0
    else:
        return number % 10 + SumRecursive(number // 10)
    
output1=SumRecursive(1524)
print("Sum of Integer is: ", output1)

#task 7
def RowWiseSum(Mat):
    rowMat=[]
    for row in Mat:
        rowSum=0
        for element in row:
            rowSum=rowSum+element
        rowMat.append(rowSum)
        
    return rowMat

def ColumnWiseSum(Mat):
    colNum=len(Mat[0])
    ColMat=[0] * colNum
    for row in Mat:
        for i in range(colNum):
            ColMat[i]+=row[i]
    return ColMat
        
A=[[1,13,13],[5,11,6],[4,4,9]]
print("Row-wise: ",RowWiseSum(A))
print("Column-wise: ", ColumnWiseSum(A))

#task 8
def SortedMerge(Arr1,Arr2):
    result=[]
    i=0
    j=0
    
    while i<len(Arr1) and j<len(Arr2):
        if Arr1[i]<Arr2[j]:
            result.append(Arr1[i])
            i+=1
        else:
            result.append(Arr2[j])
            j+=1
            
    while i<len(Arr1):
        result.append(Arr1[i])
        i=i+1
        
    while j<len(Arr2):
        result.append(Arr2[j])
        j+=1
    return result 

A=[0,3,4,10,11]
B=[1,8,13,24]

print("Output=", SortedMerge(A, B))

#task 9
def PalindromeRecursive(str):
    if len(str) <=1:
        return True
    if str[0] != str[-1]:
        return False
    return PalindromeRecursive(str[1:-1])
        
word="radar"
if PalindromeRecursive(word):
    print("Palindrome")
else:
    print("Not palindrome")
    
#task 10
def Sort10(Arr):
    pos=sorted([i for i in Arr if i>=0])
    neg=sorted([j for j in Arr if j<0])
    
    result=[]
    posIndex=0
    negIndex=0
    
    for i in range (len(Arr)):
        if i%2 == 0 and negIndex<len(neg):
            result.append(neg[negIndex])
            negIndex+=1
            
        elif posIndex<len(pos):
            result.append(pos[posIndex])
            posIndex+=1
            
    return result
    
arr=[10,-1,9,20,-3,-8,22,9,7]
print("Output: ", Sort10(arr))
            
