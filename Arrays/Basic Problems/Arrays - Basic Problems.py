#!/usr/bin/env python
# coding: utf-8

# ## Given an array of integers size N. Count that have atleast 1 element greater than itself. 

# ### Brute Force

# In[1]:


arr = [3,-2,6,8,4,8,5]

n = len(arr)
cnt = 0
for i in range (n):
    for j in range(n):
        if arr[j] > arr[i]:
            cnt += 1
            break

print("Count ", cnt)


# ### Time Complexity = O(n*n)

# In[ ]:





# ### Max Element approach
# - Find max element in the array
# - Count no. of time max element represent in the array

# In[4]:


arr = [2,5,1,4,8,0,8,1,3,8]

n = len(arr)

maxNum = arr[0]

for i in range(1,n):
    if maxNum < arr[i]:
        maxNum = arr[i]
cnt = 0

for j in range(n):
    if maxNum == arr[j]:
        cnt += 1

print("Count ", cnt)


# ### Time Complexity = O(n)

# In[ ]:





# ## Given an array of integers size N. Count no. of Arrays [i,j] such that arr[i] + arr[j] == k

# ### Brute Force

# In[7]:


arr = [3,-2,6,8,4,8,5]
k = 10

n = len(arr)
count = 0

for i in range(n):
    for j in range(i+1,n):
        if arr[i] + arr[j] == k:
            count += 1

print(count)
        


# ### Time Compexity = O(n*n)

# In[ ]:





# ## Given an array of integers size N. Need to reverse the Array.

# In[9]:


arr = [3,-1,6,2,4,5,7,9,10]

n = len(arr)

i = 0
j = n-1

while i<j:
    arr[i] = arr[i] ^ arr[j]
    arr[j] = arr[i] ^ arr[j]
    arr[i] = arr[i] ^ arr[j]
    
    i += 1
    j -= 1

print(arr)


# ### Time Complexity = O(n)

# In[ ]:




