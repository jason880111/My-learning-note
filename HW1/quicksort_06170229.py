# coding: utf-8

# In[1]:



def quicksort(k):
  if len(k) == 1 or len(k)==0: 
      return k
  else:
      standard = k[0]  
      lower = [i for i in k[1:] if i < standard] 
      higher = [i for i in k[1:] if i >= standard]     
      return quicksort(lower) + [standard] + quicksort(higher)
