# Dijkstra、Kruskal原理

**Dijkstra**
* Dijkstra演算法算是單源最短路徑(Single Souce Shortest Path)的一種方法，計算一個節點到其他所有節點的最短路徑，主要特點是以起始點為中心向外層層擴展，直到擴展到終點為止且沒有負權邊
   * Dijkstra執行步驟

      1.從基準點開始，向外延伸一格能到達的所有vertex，並且從那些vertex當中，選一條路徑最短的

      2.再從剛剛選定的vertex向外延伸一格所有能到達的vertex，並且也是選一條路徑最短的

      3.重複2.這個步驟，直到每個vertex都被拜訪過，那麼最終的答案就出來了

      4.拜訪過的vertex就不會再重複拜訪了

      5.需要紀錄每個vertex的 "上一個節點" 或者是說parent，以便回頭尋找最短路徑所經過的點
      
   * 時間複雜度：
      若使用Binary Heap，需要O((E+V)logV)
      若使用Fibonacci Heap，只需要O(E+VlogV)
      
   <img src='https://github.com/jason880111/My-learning-note/blob/master/image/Dijkstra.jpg' height=400 weight =400>
      
 **Kruskal**
 * Kruskal演算法是一個計算最小生成樹(Minimum Spaning Tree)的方法，按照邊的權重順序（從小到大）將邊加入生成樹中，但是若加入該邊會與生成樹形成環(cycle)則不加入該邊，直到樹中含有「頂點個數-1」條邊為止
    * Kruskal執行步驟

      1.先把所有path按照權重，從小到大排序

      2.需要一個表格來記錄每個edge所屬的 "subset" 或稱 "子集合" 至於子集合要用哪個edge當作代表 可以自行訂定一套規則

      3.每次都會從權重最小的path選一個，並且確認那兩個edge的subset不相同，才可以把這個path加入最小生成樹

      4.重複執行3.這個步驟，直到有V-1個path都被加入最小生成樹，那就可以停止了
      
    * 時間複雜度：O(nlogn)
    
    <img src='https://github.com/jason880111/My-learning-note/blob/master/image/kruskal.gif' height=400 weight =400>
    
 # 流程圖
 **Dijkstra**
 
 <img src='https://github.com/jason880111/My-learning-note/blob/master/image/Dijkstra%20%E6%B5%81%E7%A8%8B%E5%9C%96.jpg' height=400 weight =400>
  
 **Kruskal**
 
<img src='https://github.com/jason880111/My-learning-note/blob/master/image/kruskal%E6%B5%81%E7%A8%8B%E5%9C%96.jpg' height=400 weight =400>

# 學習歷程
經過這六次作業的磨練，對程式碼總算有多了一些新見解。剛開始總是覺得摸不著頭緒，不知從何開始，就算每次在上課時或者回家之後把許多概念都弄懂了，還是沒有辦法把這些想法轉換成程式碼，更不用說從頭尾都靠自己產出了。在後面這幾次作業當中，越來越覺得學習得很扎實，雖然不是百分百原創，可能還要先參考網路上的程式邏輯，慢慢修改後再和同學討論，找出為何有error，但也更能透過邏輯轉換理解程式碼的運作，就算有error，也能馬上理解錯在哪裡，要做甚麼修改。這學期一點一滴的進步實在讓我很開心，雖然可能沒有像前段班同學行雲流水般的將程式融會貫通且運用自如，我要追趕的路還很長，但至少跟期初的自己比起來，除了心態上的進步，成果也慢慢的反映在每次的作業上，謝謝老師讓我們在這堂課對學習有了新的見解!
