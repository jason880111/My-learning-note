# Hash Table原理


Hash Table 是儲存 (key, value) 這種 mapping 關係的一種資料結構，如下圖


<img src='https://github.com/jason880111/My-learning-note/blob/master/image/hash-table.png' height=350 weight =350>

因為 hash function 的關係，如果先把 n 個數字儲存在 Hash Table 裡面，那如果要判斷這個數字 A 是不是已經被存在 Hash Table 裡面，只要先把這個數字丟進 hash function，就可以直接知道 A 對應到 Hash Table 中哪一格。

若把Table想像成「書桌」，slot想像成書桌的「抽屜」，每一個抽屜只放一個物品，

如此一來，只要拿著Key，透過Hash Function找到對應的抽屜(Hash Function的功能是指出「第幾個」抽屜，也就是抽屜的index)，就能保證是該Key所要找的物品。


反之，如果同一個抽屜裡有兩個以上的物品時，便有可能找錯物品。
