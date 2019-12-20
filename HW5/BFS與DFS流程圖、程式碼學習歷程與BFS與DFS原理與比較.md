# BFS與DFS原理

* BFS原理

   * BFS (Breadth-First-Search) ——廣度優先搜尋, 是從根節點開始，遍歷完畢整張圖，不考慮結果所在的位置， 無論如何都要遍歷完畢整張地圖才終止。 按照就近      原則進行， 距離原點相同的節點的訪問順序是相近的。


     BFS使用　'queue'　來進行儲存未被檢測的節點，利用佇列的先進先出的特點來按照寬度訪問查詢等待計算的節點。
    
* DFS原理

   * DFS (Depth-First-Search)——深度優先搜尋，是從根節點開始， 逐個訪問每一條路徑， 對於具有多子節點的節點而言，先搜尋到某一條子路的最深處，再逐個回        溯前驅節點。

     DFS使用棧(stack) 這一種資料結構來儲存未訪問的節點，節點按照深度優先的次序被訪問並依次被壓入棧中，並以相反的次序出棧進行新的檢測。
     
     
* BFS與DFS比較

   **BFS**
   * 時間複雜度：O(V+E)（分別遍歷所有節點和各節點的所有鄰居）
   * 空間複雜度：O(V)（Queue中最多可能存放所有節點） 
   
   **DFS**
   * 時間複雜度：O(V+E)
   * 空間複雜度：O(logV)
   
   dfs使用遞迴函式程式可以簡潔地進行書寫，並且狀態管理也很簡單，所以大多數情況還是用dfs來實現相關問題。反之，在求最短路問題時，dfs需要反覆經過同樣的狀    態，所以此時使用bfs為好。

   bfs會把狀態逐個加入佇列，因此通常需要與狀態數成正比的記憶體空間。反之，dfs是與遞迴深度成正比的。一般與狀態數相比，遞迴深度並不會太大，所以dfs更加省    記憶體。
   
  **BFS 的重點在於佇列，而 DFS 的重點在於遞迴。這是它們的本質區別**
  
  # 流程圖
  ## BFS
  <img src='https://github.com/jason880111/My-learning-note/blob/master/image/BFS.jpg' height=400 weight =400>

  ## DFS
  <img src='https://github.com/jason880111/My-learning-note/blob/master/image/DFS.jpg' height=400 weight =400>

  # 學習歷程
  

```python
from collections import defaultdict 
  
class Graph:
    
    def __init__(self): 
        
        self.graph = defaultdict(list) 

    
    def addEdge(self,u,v): 
        self.graph[u].append(v) 
  
   
    def BFS(self, s): 
        
        visited = [] 
        queue = [s] 
        
        while queue:
            s = queue.pop(0)
            for neighbor in self.graph[s]:
                    if neighbor not in visited:
                        visited.append(neighbor)
                        queue.append(neighbor)
        return visited
```

我先寫了兩個集合，visited放走訪過的點，queue放待走訪的點

當queue存在時，把第一個數pop出來

假設有其他的鄰點沒有被走訪過，依序加入倒visited和queue裡
直到全部走訪完，queue裡面有沒東西為止


```python
g = Graph()
g.addEdge(0,1)
g.addEdge(0,2)
g.addEdge(1,2)
g.addEdge(2,0)
g.addEdge(2,3)
g.addEdge(3,3)

print(g.BFS(2))
```

    [0, 3, 1, 2]
    

這樣跑出來的順序是不對的

看起來應該是因為我visited裡面沒放東西，而是把s放在queue裡，然後就馬上把他pop掉了，也沒有加入到visited當中，所以起始值2也不在第一順位


```python
from collections import defaultdict 
  
class Graph:
    
    def __init__(self): 
        
        self.graph = defaultdict(list) 

    
    def addEdge(self,u,v): 
        self.graph[u].append(v) 
  
   
    def BFS(self, s): 
        
        visited = [s] 
        queue = [s] 
        
        while queue:
            s = queue.pop(0)
            for neighbor in self.graph[s]:
                    if neighbor not in visited:
                        visited.append(neighbor)
                        queue.append(neighbor)
        return visited
```

這邊在一開始就直接把初始值放入visited當中，看看這樣會不會有問題


```python
g = Graph()
g.addEdge(0,1)
g.addEdge(0,2)
g.addEdge(1,2)
g.addEdge(2,0)
g.addEdge(2,3)
g.addEdge(3,3)

print(g.BFS(2))
```

    [2, 0, 3, 1]
    

成功!接著繼續做DFS


```python
from collections import defaultdict 
  
class Graph:
    
    def __init__(self): 
        
        self.graph = defaultdict(list) 

    
    def addEdge(self,u,v): 
        self.graph[u].append(v) 
  
   
    def BFS(self, s): 
        
        visited = [s] 
        queue = [s] 
        
        while queue:
            s = queue.pop(0)
            for neighbor in self.graph[s]:
                    if neighbor not in visited:
                        visited.append(neighbor)
                        queue.append(neighbor)
        return visited
    
    def DFS(self, s):
        
        visited = [s]
        stack = [s]
        
        while stack:
            s = stack.pop(-1)
        
            for neighbor in self.graph[s]:
                if neighbor not in visited:
                        visited.append(neighbor)
                        stack.append(neighbor)   
        return visited
```

這裡我只是簡單的想說，bfs的原理是pop queue中的第一個數字，dfs則是pop stack裡面最後進來的數字，所以我就把pop的位置改成-1


```python
g = Graph()
g.addEdge(0,1)
g.addEdge(0,2)
g.addEdge(1,2)
g.addEdge(2,0)
g.addEdge(2,3)
g.addEdge(3,3)

print(g.BFS(2))
print(g.DFS(2))
```

    [2, 0, 3, 1]
    [2, 0, 3, 1]
    

結果好像不是這麼回事，兩個最後跑出來的結果竟然一樣，一定是哪裡有問題

看了很久之後，本來以為是不是因為一次只丟一個數進到queue，就把上把他pop掉了，所以兩者答案才會一樣

後來想了一下發現不是這個原因，也跟pop的位置沒關係，而是如果這行visited.append(neighbor)的位置不改變的話，根本就跟bfs沒甚麼差別

所以我決定先改dfs，至少讓他跑出正確的答案


```python
from collections import defaultdict 
  
class Graph:
    
    def __init__(self): 
        
        self.graph = defaultdict(list) 

    
    def addEdge(self,u,v): 
        self.graph[u].append(v) 
  
   
    def BFS(self, s): 
        
        visited = [s] 
        queue = [s] 
        
        while queue:
            s = queue.pop(0)
            for neighbor in self.graph[s]:
                    if neighbor not in visited:
                        visited.append(neighbor)
                        queue.append(neighbor)
        return visited
    
    def DFS(self, s):
        
        visited = [s]
        stack = [s]
        
        while stack:
            s = stack.pop()
            visited.append(s)
        
            for neighbor in self.graph[s]:
                if neighbor not in visited:
                        stack.append(neighbor)   
        return visited
```

這邊決定把剛剛說的那行刪除，並且把從stack pop出來的數直接放到visited當中，這樣應該就不會發生剛剛那個問題了


```python
g = Graph()
g.addEdge(0,1)
g.addEdge(0,2)
g.addEdge(1,2)
g.addEdge(2,0)
g.addEdge(2,3)
g.addEdge(3,3)

print(g.BFS(2))
print(g.DFS(2))
```

    [2, 0, 3, 1]
    [2, 2, 3, 0, 1]
    

結果出來之後還是不對的，但後來發現只是因為我一開始已經把值丟入visited當中了，後來又append了一次進去，所以才會重複


```python
from collections import defaultdict 
  
class Graph:
    
    def __init__(self): 
        
        self.graph = defaultdict(list) 

    
    def addEdge(self,u,v): 
        self.graph[u].append(v) 
  
   
    def BFS(self, s): 
        
        visited = [s] 
        queue = [s] 
        
        while queue:
            s = queue.pop(0)
            for neighbor in self.graph[s]:
                    if neighbor not in visited:
                        visited.append(neighbor)
                        queue.append(neighbor)
        return visited
    
    def DFS(self, s):
        
        visited = []
        stack = [s]
        
        while stack:
            s = stack.pop()
            visited.append(s)
        
            for neighbor in self.graph[s]:
                if neighbor not in visited:
                        stack.append(neighbor) 
        return visited
```


```python
g = Graph()
g.addEdge(0,1)
g.addEdge(0,2)
g.addEdge(1,2)
g.addEdge(2,0)
g.addEdge(2,3)
g.addEdge(3,3)

print(g.BFS(2))
print(g.DFS(2))
```

    [2, 0, 3, 1]
    [2, 3, 0, 1]
    

最後我就把visited弄成一個空集合，這樣在append的時候，第一個值就不會重複了

  
  
  



**參考網站**

https://www.itread01.com/content/1541297601.html

https://codertw.com/%E7%A8%8B%E5%BC%8F%E8%AA%9E%E8%A8%80/102866/

https://itw01.com/8JWXEHX.html
