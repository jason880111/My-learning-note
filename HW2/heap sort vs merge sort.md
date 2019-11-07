 **堆積排序(Heap Sort)**
  * 利用Heap Tree的性質來排序
  * Max Heap Tree的根節點一定是最大值，與最後一個節點交換後，取出加入已排序數列
  * 將原來的樹重新調整為最大堆積樹

 **合併排序(Merge Sort)**
  * 將數列對分成兩個子數列，並遞回對分
  * 對分至只有一個元素時，將元素回傳合併
  
 # 時間複雜度

 Best
  * Heap sort : Ο(n log n)
  * Merge sort : Ο(n log n)
  
 Worst
  * Heap sort : Ο(n log n)
  * Merge sort : Ο(n log n)
  
 Average
  * Heap sort : Ο(n log n)
  * Merge sort : Ο(n log n)
  
 # 空間複雜度
  * Heap sort : Ο(n) + Ο(1)
  * Merge sort : Ο(n)
  
 # 穩定性
  * Heap sort : 不穩定
  * Merge sort : 穩定
  
 # 結論
 理論上Heap sort比merge sort還要來的快速。
 他們倆個最差的時間複雜度都是 O(n log n) , 但是heap sort 是in-place sorting , 不像merge sort 每次都需要去跟記憶體要一個位置 , 所以說Heap sort 理論上是比merge sort還要快
