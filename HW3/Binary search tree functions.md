# BST新增、刪除、查詢、修改功能說明

# Insert(新增)
* 新增節點時，能將節點調整到正確的位置

```python
def insert(self,root,val):
    
        if root is None: #如果root沒有東西，把insrert進來的val當作root
            return val
        
        else:
            
            #若root不是空值
            while root is not None:
                                 
                #若新節點的值小於root的值且左節點沒有東西，就把新的子節點當作左子節點
                if val <= root.val:    
                    if root.left is None:
                        root.left = TreeNode(val)
                        return root.left
                    
                    #若左節點有東西，則把左節點當作新的root，並重新再run一次
                    else:
                        root = root.left
                                
                else:
                    
                    #若新節點的值大於root的值且右節點沒有東西，就把新的子節點當作右子節點
                    if root.right is None:
                        root.right = TreeNode(val)
                        return root.right
                    
                    #若右節點有東西，則把右節點當作新的root，並重新再run一次
                    else:
                        root = root.right
```

# Search(查詢)
* 判斷current應該要往左還是往右左來搜尋某個節點的直


```python
def search(self, root, target):
        
        #若root沒有東西，回傳target
        if root is None:
               return target
        else:
            
            #若root不是空值且root的值等於target，回傳該root
            if root.val == target:
                return root
            
            #若target大於root的值，則繼續往右邊找，找到後回傳
            elif root.val < target:
                return self.search(root.right, target)
            
            #若target小於root的值，則繼續往左邊找，找到後回傳
            else:
                return self.search(root.left, target)
```

# Delete(刪除)
* 刪除某一個節點，並讓其他節點也照著規則排出正確的位置


```python
def delete(self, root, target):
    #當查詢到的target不等於空值，繼續這個迴圈
    while self.search(root,target) != None:

        #若target小於root的值，則target在subtree的左側
        if target < root.val:
            root.left = self.delete(root.left, target)
            
        #若target大於root的值，則target在subtree的右側
        elif target > root.val:
            root.right = self.delete(root.right, target)

        else:
            
            #Node只有一個或沒有子節點
            #root的右邊有子節點，用該節點取代原本的root
            if root.left is None:
                x = root.right
                root = None
                return x

            #root的左邊有子節點，用該節點取代原本的root
            elif root.right is None:
                x = root.left
                root = None
                return x
            
            #Node有兩個子節點，找出subtree右側的最小值
            x = self.minRightNode(root.right)

            #複製subtree右側的最小值當作root的值
            root.val = x.val

            #刪除右側的最小值
            root.right = self.delete(root.right, x.val)

        return root
```


# Modify(修改)
* 刪除指定數字後將它改為其他數值，再放入新數值後，依照BST的規則將整個tree排序好

**參考網站**
* [二元搜尋數](https://zh.wikipedia.org/wiki/%E4%BA%8C%E5%85%83%E6%90%9C%E5%B0%8B%E6%A8%B9)
* [我的程式碼](https://github.com/jason880111/My-learning-note/blob/master/HW3/binary_search_tree_06170229.py) 
