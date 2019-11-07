# Heap sort簡介
  heapsort又叫堆、累堆
  * 最小堆積 (min heap) : 父節點的值小於子節點
 
   <img src='https://github.com/jason880111/My-learning-note/blob/master/image/%E6%93%B7%E5%8F%96.PNG' height=200 weight =200>
   
  * 最大堆積 (max heap) : 父節點的值大於子節點
   <img src='https://github.com/jason880111/My-learning-note/blob/master/image/%E6%93%B7%E5%8F%961.PNG' height=200 weight =200>
   
# 步驟
  * 將資料轉換為 heap 資料結構（遞增排序用 max heap, 遞減排序選擇 min heap）
  * 取出最大／最小值，並與最後一個元素置換
    * 交換 heap 的 root 與最後一個 node
    * 將剩下的資料排序， 使其滿足heap的特性
    
# 學習歷程

一開始實在沒甚麼頭緒，後來上網看了heap sort的流程，在理解完之後也嘗試著自己打打看，但光是heapify的部分就不太順利，所以最後決定直接參考一下網路上的版本，看完之後再試著自己重打一遍


    
    
    
    

```python
def heapify(nums, heap_size, root_index):

    largest = root_index
    left_child = (2 * root_index) + 1
    right_child = (2 * root_index) + 2


    if nums[left_child] > nums[largest]:
        largest = left_child

    if nums[right_child] > nums[largest]:
        largest = right_child

    if largest != root_index:
        nums[root_index], nums[largest] = nums[largest], nums[root_index]
   
        heapify(nums, heap_size, largest)


def heap_sort(nums):
    n = len(nums)

    for i in range(n, -1, -1):
        heapify(nums, n, i)

    for i in range(n , -1, -1):
        nums[i], nums[0] = nums[0], nums[i]
        heapify(nums, i, 0)
```


```python
a = [3,4,6,1,9,5,15,0]
```


```python
heap_sort(a)
```


    ---------------------------------------------------------------------------

    IndexError                                Traceback (most recent call last)

    <ipython-input-3-651ec5f94faa> in <module>
    ----> 1 heap_sort(a)
    

    <ipython-input-1-a0ad8162f68b> in heap_sort(nums)
         22 
         23     for i in range(n, -1, -1):
    ---> 24         heapify(nums, n, i)
         25 
         26     for i in range(n , -1, -1):
    

    <ipython-input-1-a0ad8162f68b> in heapify(nums, heap_size, root_index)
          6 
          7 
    ----> 8     if nums[left_child] > nums[largest]:
          9         largest = left_child
         10 
    

    IndexError: list index out of range


這邊結果跑出來後錯誤似乎是我沒有把index的範圍設好，應該是第八行的地方nums的部分沒有範圍限制，所以要更改一下我的range


```python
def heapify(nums, heap_size, root_index):

    largest = root_index
    left_child = (2 * root_index) + 1
    right_child = (2 * root_index) + 2


    if left_child < heap_size and nums[left_child] > nums[largest]:
        largest = left_child

    if right_child < heap_size and nums[right_child] > nums[largest]:
        largest = right_child

    if largest != root_index:
        nums[root_index], nums[largest] = nums[largest], nums[root_index]
   
        heapify(nums, heap_size, largest)


def heap_sort(nums):
    n = len(nums)

    for i in range(n, -1, -1):
        heapify(nums, n, i)

    for i in range(n , -1, -1):
        nums[i], nums[0] = nums[0], nums[i]
        heapify(nums, i, 0)
```


```python
a = [3,4,6,1,9,5,15,0]
```


```python
heap_sort(a)
```


    ---------------------------------------------------------------------------

    IndexError                                Traceback (most recent call last)

    <ipython-input-6-651ec5f94faa> in <module>
    ----> 1 heap_sort(a)
    

    <ipython-input-4-e92297833c90> in heap_sort(nums)
         25 
         26     for i in range(n , -1, -1):
    ---> 27         nums[i], nums[0] = nums[0], nums[i]
         28         heapify(nums, i, 0)
    

    IndexError: list index out of range


這邊我已經把第八行的子節點設了一個範圍，就是左邊和右邊的兩個子節點都需要比整個heap的範圍小，才能和父節點做比較。
第八行的問題已經解決了，但27行的問題還是存在，error的意思應該也是我26行的range有問題


```python
def heapify(nums, heap_size, root_index):

    largest = root_index
    left_child = (2 * root_index) + 1
    right_child = (2 * root_index) + 2


    if left_child < heap_size and nums[left_child] > nums[largest]:
        largest = left_child

    if right_child < heap_size and nums[right_child] > nums[largest]:
        largest = right_child

    if largest != root_index:
        nums[root_index], nums[largest] = nums[largest], nums[root_index]
   
        heapify(nums, heap_size, largest)


def heap_sort(nums):
    n = len(nums)

    for i in range(n, -1, -1):
        heapify(nums, n, i)

    for i in range(n , 0, -1):
        nums[i], nums[0] = nums[0], nums[i]
        heapify(nums, i, 0)
```


```python
a = [3,4,6,1,9,5,15,0]
```


```python
heap_sort(a)
```


    ---------------------------------------------------------------------------

    IndexError                                Traceback (most recent call last)

    <ipython-input-3-651ec5f94faa> in <module>
    ----> 1 heap_sort(a)
    

    <ipython-input-1-d530ffc8b793> in heap_sort(nums)
         25 
         26     for i in range(n , 0, -1):
    ---> 27         nums[i], nums[0] = nums[0], nums[i]
         28         heapify(nums, i, 0)
    

    IndexError: list index out of range


原本以為是不是我swap的range打錯了，中止點好像應該要在0，但改成0之後發現這個範圍還是錯的，所以應該不是中止點的問題。
後來上網找了一下發現，我把中止點設在0和-1其實不會影響到最後的答案，所以不是中止點的問題


```python
def heapify(nums, heap_size, root_index):

    largest = root_index
    left_child = (2 * root_index) + 1
    right_child = (2 * root_index) + 2


    if left_child < heap_size and nums[left_child] > nums[largest]:
        largest = left_child

    if right_child < heap_size and nums[right_child] > nums[largest]:
        largest = right_child

    if largest != root_index:
        nums[root_index], nums[largest] = nums[largest], nums[root_index]
   
        heapify(nums, heap_size, largest)


def heap_sort(nums):
    n = len(nums)

    for i in range(n, -1, -1):
        heapify(nums, n, i)

    for i in range(n-1 , -1, -1):
        nums[i], nums[0] = nums[0], nums[i]
        heapify(nums, i, 0)
```


```python
a = [3,4,6,1,9,5,15,0]
```


```python
heap_sort(a)
```


```python
print(a)
```

    [0, 1, 3, 4, 5, 6, 9, 15]
    

最後發現我實在太白癡了，從頭到尾都是我起始點設錯的問題。假設我的長度是6，index從0開始，意思是index會從0~5，當我heapify好了最後要swap的時候，最後的數index應該會是5，所以我的起始點應該要是n-1


```python
class Solution(object):
    def heapsort(self, nums):
        n = len(nums)
        
        for i in range(n, -1, -1):
            self.heapify(nums, n, i)

        for i in range(n-1, -1, -1):
            nums[0], nums[i] = nums[i], nums[0]
            self.heapify(nums, i, 0)
                  
    def heapify(self, nums, heap_size, root_index):
        
        largest = root_index
        left_child = (2 * root_index) + 1
        right_child = (2 * root_index) + 2
        
        if left_child < heap_size and nums[left_child] > nums[largest]:
            largest = left_child

        if right_child < heap_size and nums[right_child] > nums[largest]:
            largest = right_child

        if largest != root_index:
            nums[root_index], nums[largest] = nums[largest], nums[root_index]
   
            heapify(nums, heap_size, largest)
```


```python
a=[8,3,5,1,0,-3,4]
```


```python
Solution().heapsort(a)
```


```python
print(a)
```

    [-3, 0, 1, 3, 4, 5, 8]
    

這邊全部把它改成規定的格式，光是排版就弄了很多次，但最後還是順利產出


```python
class Solution(object):
    def heapsort(self,nums):
        n = len(nums)
        for i in range(n-1, -1, -1):
            self.heapify(nums, n, i)

        for i in range(n - 1, 0, -1):
            nums[i], nums[0] = nums[0], nums[i]
            self.heapify(nums, i, 0)
            
    def heapify(self,nums, heap_size, root_index):

        minnode = root_index
        left_child = (2 * root_index) + 1
        right_child = (2 * root_index) + 2


        if left_child < heap_size and nums[left_child] < nums[minnode]:
            minnode = left_child

        if right_child < heap_size and nums[right_child] < nums[minnode]:
            minnode = right_child

        if minnode != root_index:
            nums[root_index], nums[minnode] = nums[minnode], nums[root_index]
   
            self.heapify(nums, heap_size, minnode)
```


```python
a=[8,3,5,1,0,-3,4]
```


```python
Solution().heapsort(a)
```


```python
print(a)
```

    [8, 5, 4, 3, 1, 0, -3]
    

這邊只是覺得太無聊就把max heap改成min heap


```python

```

# 流程圖
<img src='https://github.com/jason880111/My-learning-note/blob/master/image/heap%E6%B5%81%E7%A8%8B.PNG' height=500 weight =500>


**參考網站**
* [[演算法] 堆積排序法(Heap Sort)](http://www.notepad.yehyeh.net/Content/Algorithm/Sort/Heap/Heap.php)    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    
