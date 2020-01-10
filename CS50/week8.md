# Stack
**定義**
  * Heap Sort可以分為Min Heap與Max Heap兩種。兩者用在排序上，Min Heap是「由大到小」而Max Heap則是「由小到大」。
  * 網頁的回到上一頁的功能，「最晚進入Stack」的資料會「最先被取出」，「最早進入Stack」的資料則「最晚被取出」
  * 是一種後進先出(Last-In-First-Out, LIFO)的排程

**Push：把資料放到最上面。**


**Pop：把「最上面」的資料移除。**


**Top：回傳「最上面」的資料，確認「最上面」的是什麼。**


**IsEmpty：確認Stack裡是否有資料。**


**getSize：回傳Stack裡的資料個數。**

# Queue
**定義**
  * 排隊，不能插隊。一次只能執行一個需求，所以需要用 Queue來安排執行順序。
  
**Push：把資料放進Queue的最後面，成新的back。**


**Pop：把front最前面所指向的資料從Queue中移除，並更新front。**


**getFront：回傳front所指向的資料。**


**getBack：回傳back所指向的資料。**


**IsEmpty：確認Queue裡是否有資料。**


**getSize：回傳Queue裡的資料個數。**
