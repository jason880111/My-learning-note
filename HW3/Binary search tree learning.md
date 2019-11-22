# BST原理

BST全名Binary Search Tree，也稱ordered binary tree、orted binary tree


**定義**

* 每個節點最多只有兩個子節點的樹，節點左邊稱為左子樹 (left child)、節點右邊稱為右子樹 (right child)
* 若任意節點的左子樹不為缺值，則左子樹上所有節點的值均大於它的根節點值
* 若任意節點的右子樹不為缺值，則右子樹上所有節點的值均大於它的根節點值
* 任意節點的左、右子樹也分別為二元搜尋樹；

**性能**

最佳情况Olog(n), 最壞情况O(n)


# Insert

```python
def insert(root,node): 
    if root is None: 
        root = node 
    else: 
        if root.val < node.val: 
            if root.right is None: 
                root.right = node 
            else: 
                insert(root.right, node) 
        else: 
            if root.left is None: 
                root.left = node 
            else: 
                insert(root.left, node)
```

我看了很久的insert和search的概念，也看了很多方法後最後自己重打了一次insert，也打得蠻順的。後來想想看有沒有其他方式可以試試，所以就稍微改了一下


```python
class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None
        """
        :type val: int
        :type left: TreeNode or None
        :type right: TreeNode or None
        """
class Solution(object):
    def insert(self,root,val):
        r = root
        
        while True:
            if val > root.val:
                if(root.right):
                    root = root.right
                else:
                    t = TreeNode(val)
                    root.right = t
                    return r
            else:
                if root.left:
                    root = root.left
                else:
                    t = TreeNode(val)
                    root.left = t
                    return r
```


```python
root = TreeNode(10)
```


```python
root.insert(15)
```


    ---------------------------------------------------------------------------

    AttributeError                            Traceback (most recent call last)

    <ipython-input-4-5b53a21d109e> in <module>
    ----> 1 root.insert(15)
    

    AttributeError: 'TreeNode' object has no attribute 'insert'


這邊我就直接改成while的方式，也把格式一起調整成作業要求，但其實我也沒有看得很懂我的error是甚麼原因。
後來覺得似乎根本沒有辦法把我的測值insert進去，越看也覺得越複雜，所以後來我就再想了一個方式改成我自己比較容易理解的狀態


```python
class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None
        """
        :type val: int
        :type left: TreeNode or None
        :type right: TreeNode or None
        """
class Solution(object):
    def insert(self,root,val):
        if root is None:
            root = val
        else:
            root = self.root
            while root is not None:
                if val < root:
                    if root.left is None:
                        root.left = TreeNode(val)
                        return
                    else:
                        root = root.left
                else:
                    if root.right is None:
                        root.right = TreeNode(val)
                        return
                    else:
                        root = root.right
```


```python
root = TreeNode(10)
```


```python
root.insert(15)
```


    ---------------------------------------------------------------------------

    AttributeError                            Traceback (most recent call last)

    <ipython-input-7-5b53a21d109e> in <module>
    ----> 1 root.insert(15)
    

    AttributeError: 'TreeNode' object has no attribute 'insert'


雖然有改成了if else的方式，但還是在裡面放了一個while迴圈，最後跑出來一樣是同一個error，後來覺得我第一個else底下的root = self.root在邏輯上好像根本不需要出現這句。在我比較root和val大小的時候，我的root應該要寫成root.val，這樣他才會是一個數值，也才有辦法比較，所以也做了修改


```python
class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None
        """
        :type val: int
        :type left: TreeNode or None
        :type right: TreeNode or None
        """
class Solution(object):
    def insert(self,root,val):
        if root is None:
            return root
        else:
            while root is not None:
                if val < root.val:
                    if root.left is None:
                        root.left = TreeNode(val)
                        return
                    else:
                        root = root.left
                else:
                    if root.right is None:
                        root.right = TreeNode(val)
                        return 
                    else:
                        root = root.right
```


```python
root = TreeNode(10)
Solution().insert(root,15)
```


```python
print(Solution().insert(root,5)==root.left)
```

    False
    

把上述我所說的都更改完了之後也成功insert數值進去，但在最後測試的時候，本來應該要是True的竟然變成False


```python
root.right
```




    <__main__.TreeNode at 0x1d4c2d33588>




```python
root.right.val
```




    15




```python
Solution().insert(root,5)
```


```python
root.left.val
```




    5



這裡我發現我的node insert進去的方式都是對的，位置和數值也沒有錯，最後重看了幾次程式碼之後才發現原來是我在return的時候根本沒有講說要return到哪裡去


```python
class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None
        """
        :type val: int
        :type left: TreeNode or None
        :type right: TreeNode or None
        """
class Solution(object):
    def insert(self,root,val):
        if root is None:
            return root
        else:
            while root is not None:
                if val <= root.val:
                    if root.left is None:
                        root.left = TreeNode(val)
                        return root.left
                    else:
                        root = root.left
                else:
                    if root.right is None:
                        root.right = TreeNode(val)
                        return root.right
                    else:
                        root = root.right
```


```python
root = TreeNode(10)
Solution().insert(root,15)
```




    <__main__.TreeNode at 0x1d4c2d10e48>




```python
print(Solution().insert(root,5)==root.left)
```

    True
    

改完之後就成功了!


# Search

```python
class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None
        """
        :type val: int
        :type left: TreeNode or None
        :type right: TreeNode or None
        """
class Solution(object):
    def search(self, root, target):
        
        if root is None:
               return None
        else:
            if root.val == target:
                return root
            elif root.val < target:
                return self.search(root.right, target)
            else:
                return self.search(root.left, target)
```

search的概念其實跟insert很像，所以打完insert之後我覺得search就蠻好理解的，應該是四個功能當中最不花時間的一個吧!


# Delete
* 這邊先說delete會遇到的三種狀況
  * 沒有child
  * 只有一個child
  * 有兩個child
  
* 若沒有child的話，就直接將預刪除的值刪掉就好
* 假設有一個child或是有兩個child的話，就要來選擇誰要當root
* 兩種方法分別是找左邊sub tree的最大值或者右邊sub tree的最小值


```python
class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None
        """
        :type val: int
        :type left: TreeNode or None
        :type right: TreeNode or None
        """
class Solution(object):


*我這邊選擇的是找右邊的最小值，所以這邊就先建立一個minRightNode function


    
    def minRightNode(node):
        current = node

        while current.left is not None:
            current = current.left

        return current

    def delete(self, root, target):
        if root is None:
            return None

        if target < root.val:
            root.left = self.delete(root.left, target)

        elif target > root.val:
            root.right = self.delete(root.right, target)

        else:
            if root.left is None:
                x = root.right
                root = None
                return x

            elif root.right is None:
                x = root.left
                root = None
                return x

            x = self.minRightNode(root.right)

            root.val = x.val

            root.right = self.delete(root.right, x.val)

        return root
```


```python
import copy
root = TreeNode(5)
Node1 = TreeNode(3)
Node2 = TreeNode(3)
Node3 = TreeNode(-5)
Node4 = TreeNode(8)
Node5 = TreeNode(7)
Node6 = TreeNode(6)
Node7 = TreeNode(10)
root.left = Node1
root.right = Node4
Node1.left = Node2
Node2.left = Node3
Node4.left = Node5
Node5.left = Node6
Node4.right = Node7
root1 = copy.deepcopy(root)
root2 = copy.deepcopy(root)
root3 = copy.deepcopy(root)
root4 = copy.deepcopy(root)
```


```python
print("delete")
root2 = Solution().delete(root2,3)
print(root2.val == 5 and root2.left.val == -5 and root2.left.left == None and root2.left.right == None)
print(root2.right.right.val == 10 and root2.right.left.val == 7 and root2.right.left.left.val == 6)
print(root2.right.right.right == None and root2.right.right.left == None and root2.right.left.right == None)
print(root2.right.left.left.left == None and root2.right.left.left.right == None and root2.right.val == 8)
print("------------------------------------------")
```


這邊丟入測資後，原本想說應該可以跑出正確的結果，但這個delete問題有點大。假設我的root有兩個child，刪除root之後我找了subtree右邊的最小值補上來，當我要再把右邊的最小值刪掉的時候，卻無法刪除這個node，導致我下面跑出來的第一個結果是False




    delete
    False
    True
    True
    True
    ------------------------------------------
    

delete實在是太難了，所以我只好直接上網找了幾個網站看人家是怎麼弄的，看了很多種方法也大概了解運作原理了，剩下的部分就只能自己試看看，邊做邊學，所以我就憑我自己的印象重打了一遍


**參考網站**
* [Delete - geeksforgeeks](https://www.geeksforgeeks.org/binary-search-tree-set-2-delete/) 
* [Binary Search Tree: search、insert](http://alrightchiu.github.io/SecondRound/binary-search-tree-searchsou-xun-zi-liao-insertxin-zeng-zi-liao.html) 
