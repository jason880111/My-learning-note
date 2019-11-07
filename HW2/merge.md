# Merge sort簡介

Merge Sort 的原理就是利用拆分和合併把一整個尚未被排序的數字排序好 

Merge Sort大概的步驟如下:
  * 拆分
    * 把大陣列切一半成為兩個小陣列
    * 把切好的兩個小陣列再各自切一半
    * 重複步驟二直到每個小陣列都只剩一個元素
  * 合併
    * 排序兩個只剩一個元素的小陣列並合併
    * 把兩邊排序好的小陣列合併並排序成一個陣列
    * 重複步驟二直到所有小陣列都合併成一個大陣列


# 學習歷程



```python
def mergesort(x):
    result = []
    if len(x) < 2:
        return x
    mid = int(len(x)/2)
    left = mergesort(x[:mid])
    right = mergesort(x[mid:])
    while (len(left) > 0) or (len(right) > 0):
        if len(left) > 0 and len(right) > 0:
            if left[0] > right[0]:
                result.append(right[0])
            else:
                result.append(left[0])
                
        elif len(right) > 0:
            for i in right:
                result.append(j)
        else:
            for i in left:
                result.append(i)
        
    return result
```


```python
x = [3,4,6,1,9,5,15,0]
```


```python
mergesort(x)
```

看完我參考網站後想說不要用他那個方法看看還有沒有其他辦法，所以就照著自己的方式打看看。這邊打完讓他run了之後發現我也看不太懂這是甚麼問題，不知道到底是在merge之後沒有把待的排序數字位子放對還是有少打了甚麼，所以想說看要不要換其他的方法試看看


```python
def mergesort(x):
    result = []
    if len(x) < 2:
        return x
    mid = int(len(x)/2)
    left = mergesort(x[:mid])
    right = mergesort(x[mid:])
    while (len(left) > 0) or (len(right) > 0):
        if len(left) > 0 and len(right) > 0:
            if left[0] > right[0]:
                result.append(right[0])
                right.pop(0)
            else:
                result.append(left[0])
                right.pop(0)
        elif len(right) > 0:
            for i in right:
                result.append(i)
                right.pop(0)
        else:
            for i in left:
                result.append(i)
                left.pop(0)
    return result
```


```python
x = [3,4,6,1,9,5,15,0]
```


```python
mergesort(x)
```




    [0, 1, 1, 1, 1, 3, 3, 3]



後來經過人家指點後發現原來是我在把list裡面的值抓出來合併後，沒有把原本的list裡面的數字往下面一個值推進，所以後來就直接用pop這個方法，把被取出值的位子直接弄掉。最後雖然有跑出東西，但卻跑出了很莫名其妙的答案，完全與我想像的不一樣


```python
def mergesort(x):
    print('split',x)
    result = []
    if len(x) < 2:
        return x
    mid = int(len(x)/2)
    left = mergesort(x[:mid])
    right = mergesort(x[mid:])
    while (len(left) > 0) or (len(right) > 0):
        if len(left) > 0 and len(right) > 0:
            if left[0] > right[0]:
                result.append(right[0])
                right.pop(0)
            else:
                result.append(left[0])
                left.pop(0)
        elif len(right) > 0:
            for i in right:
                result.append(i)
                right.pop(0)
        else:
            for i in left:
                result.append(i)
                left.pop(0)
    print('merge',x)
    return result
```


```python
x = [3,4,6,1,9,5,15,0]
```


```python
mergesort(x)
```

    split [3, 4, 6, 1, 9, 5, 15, 0]
    split [3, 4, 6, 1]
    split [3, 4]
    split [3]
    split [4]
    merge [3, 4]
    split [6, 1]
    split [6]
    split [1]
    merge [6, 1]
    merge [3, 4, 6, 1]
    split [9, 5, 15, 0]
    split [9, 5]
    split [9]
    split [5]
    merge [9, 5]
    split [15, 0]
    split [15]
    split [0]
    merge [15, 0]
    merge [9, 5, 15, 0]
    merge [3, 4, 6, 1, 9, 5, 15, 0]
    




    [0, 1, 3, 4, 5, 6, 9, 15]



這裡我在程式碼中加了兩行，想看看他拆跟合併的過程到底是怎麼樣，結果發現他拆的過程一切都很正常，但當要開始merge的時候，完全沒有照著數字的大小來merge。我預設的list裡面總共有八個數字，最後merge起來變成4、4個數字的list的時候，他的順序完全沒有改變，跟我丟進去的順序一模一樣，但奇怪的是，最後他又可以merge出正確的答案，想說應該不可行，但還是試著class它一下好了


```python
class Solution(object):
    def mergesort(self,x):
        result = []
        if len(x) < 2:
            return x
    
        else:
            mid = int(len(x)/2)
            left = mergesort(x[:mid])
            right = mergesort(x[mid:])
            self.mergesort(left)
            self.mergesort(right)
        while (len(left) > 0) or (len(right) > 0):
            if len(left) > 0 and len(right) > 0:
                if left[0] > right[0]:
                    result.append(right[0])
                    right.pop(0)
                else:
                    result.append(left[0])
                    left.pop(0)
            elif len(right) > 0:
                for i in right:
                    result.append(i)
                    right.pop(0)
            else:
                for i in left:
                    result.append(i)
                    left.pop(0)
        return result
```


```python
ans=Solution().mergesort([3,4,6,1,9,5,15,0])
ans
```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-1-dfb3b64d4d17> in <module>
    ----> 1 ans=Solution().mergesort([3,4,6,1,9,5,15,0])
          2 ans
    

    NameError: name 'Solution' is not defined


class之後不知道為什麼就沒有辦法執行了，不知道是不是因為我merge了兩次還是怎麼樣，但感覺很無解，所以還是直接改改看，看有沒有其他的方法可以用好了


```python
def mergesort(x):
    if len(x) < 2:
        return x
    result = []
    mid = int(len(x) / 2)
    left = mergesort(x[:mid])
    right = mergesort(x[mid:])
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] > right[j]:
            result.append(right[j])
            j += 1
        else:
            result.append(left[i])
            i += 1
    result += left[i:]
    result += right[j:]
    return result
```


```python
x = [3,4,6,1,9,5,15,0]
```


```python
mergesort(x)
```




    [0, 1, 3, 4, 5, 6, 9, 15]



後來我就看了一下參考網站，設了i、j，直接把他們當作左、右list的第一個位子，假如最後只剩下左邊或右邊的list當中還有數字的話，就把他們都擺到result裡面，不需要再寫迴圈或者if else，也成功地排出順序


```python
class Solution(object):
    def mergesort(self,x):
        if len(x) < 2:
            return x
        result = []
        mid = int(len(x) / 2)
        left = mergesort(x[:mid])
        right = mergesort(x[mid:])
        self.mergesort(left)
        self.mergesort(right)
    
        i = 0
        j = 0
        while i < len(left) and j < len(right):
            if left[i] > right[j]:
                result.append(right[j])
                j += 1
            else:
                result.append(left[i])
                i += 1
        result += left[i:]
        result += right[j:]
        return result
```


```python
ans=Solution().mergesort([3,4,6,1,9,5,15,0])
ans
```




    [0, 1, 3, 4, 5, 6, 9, 15]



這邊純粹就是class它弄成規定的格式


# 流程圖
<img src='https://github.com/jason880111/My-learning-note/blob/master/image/merge%E6%B5%81%E7%A8%8B.PNG' height=500 weight =500>



**參考網站**
* [merge sort - geeksforgeeks](http://www.notepad.yehyeh.net/Content/Algorithm/Sort/Heap/Heap.php) 
* [初學者演算法](https://medium.com/appworks-school/%E5%88%9D%E5%AD%B8%E8%80%85%E5%AD%B8%E6%BC%94%E7%AE%97%E6%B3%95-%E6%8E%92%E5%BA%8F%E6%B3%95%E9%80%B2%E9%9A%8E-%E5%90%88%E4%BD%B5%E6%8E%92%E5%BA%8F%E6%B3%95-6252651c6f7e) 
