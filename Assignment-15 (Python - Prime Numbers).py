#!/usr/bin/env python
# coding: utf-8

# In[5]:


n = int(input("Enter the max prime number: "))
prime_list = []
for num in range(2, n+1):
    prime = True
    for i in range(2, num):
        if (num % i == 0):
            prime = False
    if prime:
        prime_list.append(num)
print(prime_list)

