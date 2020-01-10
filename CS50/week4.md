# MergeSort(合併排序法)

**定義**
  * 把問題先拆解成子問題，逐一處理子問題後，將子問題的結果合併。

  * 最佳時間複雜度：O(nlog n)

  * 平均時間複雜度：O(nlog n)

  * 最差時間複雜度：O(nlog n)

  * 空間複雜度：O(n)

# 遞迴（Recursion）
  * 遞迴（Recursion）是在函式中呼叫自身同名函式，而呼叫者本身會先被置入記憶體堆壘中，等到被呼叫者執行完畢之後，再從堆壘中取出之前被置入的函式繼續執行。堆疊（Stack）是一種「先進後出」的資料結構，就好比您將書本置入箱中，最先放入的書會最後才取出。