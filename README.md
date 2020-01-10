<h1 align="left">108 DATA STRUCTURES AND ALGORITHMS</h1>
<p align="center">
    <img alt="GitHub stars" src="https://img.shields.io/github/stars/ykz0608/DSA?style=social">
    <img alt="GitHub watchers" src="https://img.shields.io/github/watchers/ykz0608/DSA?style=social">
    <img alt="GitHub forks" src="https://img.shields.io/github/forks/ykz0608/DSA?style=social">
</p>

資料結構與演算法相关领域学习笔记，利用Python完成本課程的作業
<p align="left">
    <img src=https://img.shields.io/badge/python-3.7-blue.svg>
</p>

## :file_folder:Repository檔案結構 
|[image]|[Homework](#pencil2-homework)|[Summary of the course](#datesummary-of-the-course)|[Leetcode]|[Codesigna]|[CS50]|[Learning resources](#bookslearning-resources)|[About Me](#sheepabout-me)|[Review](#love_letterreview)|[Reference](#linkreference)
|---|---|---|---|---|---|---|---|---|---|
|存放圖片|各次作業|每週課程的上課內容概述|練習Leetcode|練習Codesigna|CS50的筆記|個人學習的各種資源|個人的自我簡介|本課程的簡單心得|參考資料

[image]:https://github.com/ykz0608/DSA/tree/master/image
[Leetcode]:https://github.com/ykz0608/DSA/tree/master/Leetcode
[Codesigna]:https://github.com/ykz0608/DSA/tree/master/Codesignal
[CS50]:https://github.com/ykz0608/DSA/tree/master/Codesignal

## :pencil2: Homework
|作業|主題|筆記|程式碼|文件夾|
|---|---|---|---|---|
|1|Quicksort|[qsnote](https://github.com/ykz0608/DSA/blob/master/image/Quick%20sort.svg)|[qspy](https://github.com/ykz0608/DSA/blob/master/HW1/QuickSort.ipynb)|https://github.com/ykz0608/DSA/tree/master/HW1|
|2|Mergesort/Mergesort|[merge sort筆記]/[heap sort筆記]|[mspy]/[hspy]|[HW2]| 
|3|Binary Search Tree|[bst筆記]/[bst功能說明]|[bstpy]|[HW3]|
|4|Hash Table|[hashtable筆記]|[htpy]|[HW4]|
|5|Breadth Frist Search & Depth Frist Search|[bfsdfs筆記]|[bfspy]|[HW5]|
|6|Minimum Spanning Tree & Shortest Path|[Dijkstra筆記]|[Dijpy]|[HW6]|

[merge sort筆記]:https://github.com/ykz0608/DSA/blob/master/HW2/merge_sort%E7%AD%86%E8%A8%98.md
[heap sort筆記]:https://github.com/ykz0608/DSA/blob/master/HW2/heap%20sort%E7%AD%86%E8%A8%98.md
[bst筆記]:https://github.com/ykz0608/DSA/blob/master/HW3/BinarySearchTree%E5%AD%B8%E7%BF%92%E6%AD%B7%E7%A8%8B%26%E6%B5%81%E7%A8%8B%E5%9C%96.md
[bst功能說明]:https://github.com/ykz0608/DSA/blob/master/HW3/BinarySearchTree%E5%8A%9F%E8%83%BD%E8%AA%AA%E6%98%8E.md
[hashtable筆記]:https://github.com/ykz0608/DSA/blob/master/HW4/HashTree%E5%AD%B8%E7%BF%92%E6%AD%B7%E7%A8%8B%26%E6%B5%81%E7%A8%8B%E5%9C%96%26%E5%8E%9F%E7%90%86.md
[bfsdfs筆記]:https://github.com/ykz0608/DSA/blob/master/HW5/BFS%26DFS%E5%AD%B8%E7%BF%92%E6%AD%B7%E7%A8%8B%26%E6%B5%81%E7%A8%8B%E5%9C%96%26%E5%8E%9F%E7%90%86%26%E6%AF%94%E8%BC%83.md
[Dijkstra筆記]:https://github.com/ykz0608/DSA/blob/master/HW6/Dijkstra%26Kruskal%26%E5%AD%B8%E7%BF%92%E6%AD%B7%E7%A8%8B%26%E6%B5%81%E7%A8%8B%E5%9C%96%26%E5%8E%9F%E7%90%86.md

[hspy]:https://github.com/ykz0608/DSA/blob/master/HW2/heap_sort_06170271.py
[mspy]:https://github.com/ykz0608/DSA/blob/master/HW2/merge_sort_06170271.py
[bstpy]:https://github.com/ykz0608/DSA/blob/master/HW3/binary_search_tree_06170271.py
[htpy]:https://github.com/ykz0608/DSA/blob/master/HW4/hash_table_06170271.py
[bfspy]:https://github.com/ykz0608/DSA/blob/master/HW5/BFS_06170271.py
[Dijpy]:https://github.com/ykz0608/DSA/blob/master/HW6/Dijkstra_06170271.py
[HW1]:https://github.com/ykz0608/DSA/tree/master/HW1
[HW2]:https://github.com/ykz0608/DSA/tree/master/HW2
[HW3]:https://github.com/ykz0608/DSA/tree/master/HW3
[HW4]:https://github.com/ykz0608/DSA/tree/master/HW4
[HW5]:https://github.com/ykz0608/DSA/tree/master/HW5
[HW6]:https://github.com/ykz0608/DSA/tree/master/HW6

## :date:Summary of the course
### Week 1:
中秋節放假
---
### Week 2:Linked List
* Linked List是一種特殊的線性表
* 其由一系列的節點組成, 節點的順序是通過節點元素中的指標連接次序來確定的
* Linked List中的節點包含兩個部分, 一個是其自身需存放的資料, 另一個是指向下一個節點的參照

* Linked List的基本操作
> 1. 向list中插入資料
> 2. 從list中移除資料
> 3. 查看list中所有的資料
> 4. 查詢指定的節點
> 5. 刪除指定的節點
* Linked List的效能
> 1. 在表頭插入和刪除非常快, 基本就是修改一下參照值, 時間大約為常量, 即O(1).
> 2. 若為查詢/刪除特定節點, 大約需要O(n)次比較, 跟陣列差不多, 但仍然比陣列快, 因為它不需要移動或複製資料.
* [`上課方式與計分規則說明`](https://docs.google.com/presentation/d/e/2PACX-1vQyAFfgCNbBPBDWV_Xbahc2CtMBr_v-jfffAhaOWw2SntBRd2kJtLZZgdYoRfEZD7flCo4ilfO_msKX/pub?start=false&loop=false&delayms=3000&slide=id.p),[`linked list`](https://docs.google.com/presentation/d/e/2PACX-1vTB218-EdUZ5jpNz6Uv4TOZQc37Y281v128_aRcWC6EhkTQs5bS8fh7yysmcuzb9R2QPN6_PDshFWL_/pub?start=false&loop=false&delayms=3000&slide=id.p),[`class1`](http://isee.scu.edu.tw/mod/page/view.php?id=524515),[`class2`](https://www.youtube.com/watch?v=us0M3nytzoQ&feature=youtu.be),[`LinkedListsreview`](https://www.youtube.com/watch?v=WwfhLC16bis)

---
### Week 3:Stack&Queue
#### Stack(堆疊)
* 線性表:
又稱為順序表, 是一個線性的序列結構, 是一個含有n≥0個節點的有線序列, 對於其中的節點:
>1. 有且僅有一個開始節點, 沒有前驅, 但有後繼節點
>2. 有且僅有一個終端節點, 沒有後繼, 但有前驅節點
>3. 其他的節點都有且僅有一個前驅和後繼節點

* 什麼是Stack(堆疊):
>1. Stack是一種特殊的線性表(Linear List), 限定只能在表的一端進行插入和刪除操作, 俗稱後進先出(LIFO)
>2. 操作資料的這一端就稱為表頭, 或top, 相對地, 另一端叫bottom, 不含任何元素的時候叫做empty stack.

#### Queue(佇列)
* 什麼是Queue:
*  Queue是一種特殊的線性表 
*  只能在表的一端進行插入(隊尾), 而在另一端進行刪除操作(隊頭)
*  特點是"先進先出"(FIFO)
* Queue的基本操作:
> 1. insert:在隊尾插入資料
> 2. remove: 從隊頭移走資料
> 3. peek: 查看隊頭的資料
* [`stack&queue`](https://docs.google.com/presentation/d/e/2PACX-1vQyAFfgCNbBPBDWV_Xbahc2CtMBr_v-jfffAhaOWw2SntBRd2kJtLZZgdYoRfEZD7flCo4ilfO_msKX/pub?start=false&loop=false&delayms=3000&slide=id.p),[`class3`](https://www.youtube.com/watch?v=YBFq7kiIWtk&feature=youtu.be),[`學生課程回饋`](https://www.youtube.com/watch?v=S7FcJ_AL6JY&feature=youtu.be)

---
### Week 4:Set&Insertion Sort&Quick Sort
* Set 是一種用於保存不重複元素的資料結構。常被用作測試歸屬性，故其查找的性能十分重要。
* Insertion Sort 
* 通過構建有序序列，對於未排序序列，從後向前掃描(對於單向鏈表則只能從前往後遍歷)，找到相應位置並插入。實現上通常使用in-place排序(需用到O(1)的額外空間)
>1. 從第一個元素開始，該元素可認為已排序
>2. 取下一個元素，對已排序陣列從後往前掃描
>3. 若從排序陣列中取出的元素大於新元素，則移至下一位置
>4. 重複步驟3，直至找到已排序元素小於或等於新元素的位置
>5. 插入新元素至該位置
>6. 重複2~5

* 性質：

> * 交換操作和陣列中導致的數量相同
> * 比較次數>=倒置數量，<=倒置的數量加上陣列的大小減一
> * 每次交換都改變了兩個順序顛倒的元素的位置，即減少了一對倒置，倒置數量為0時即完成排序。
> * 每次交換對應著一次比較，且1到N-1之間的每個i都可能需要一次額外的記錄(a[i]未到達陣列左端時)


* [`set`](https://docs.google.com/presentation/d/e/2PACX-1vT6BvB7aI9oLgyum8tdIgGVr8kabqtwo8KZV3ayzKKQqGkpAnvrjT3JabWu-Hms9kUaDILyCU8-Qqhl/pub?start=false&loop=false&delayms=3000&slide=id.p),[`insertion sort`](https://docs.google.com/presentation/d/e/2PACX-1vQOTMDM-5-OUaGfnLUOFVgefFwSVRplSwnbicp0CXOQrB5H8RM_1Aq8o_4JxHlncEmhjvqk3tzcoB7s/pub?start=false&loop=false&delayms=3000&slide=id.p),[`quick sort`](https://docs.google.com/presentation/d/e/2PACX-1vSqz8sTxT4xyjgiz-htLvZd7FZ_5ZzgKf60pFEoNLU5S77JxrsGJ2vd15CdxlfLtT3g2aizHP-Ebk9b/pub?start=false&loop=false&delayms=3000&slide=id.p),[`QuickSort review`](https://github.com/Alex-CHUN-YU/SortingAlogorithm/wiki/QuickSort),[`class4`](https://www.youtube.com/watch?v=oBXZmAwNFzY&feature=youtu.be),[`學生課堂回饋
`](https://www.youtube.com/watch?v=rOrNUuafmX8&feature=youtu.be)

---
### Week 5:
放假
---
### Week 6:Heap Sort
* 堆排序通常基於二元堆實現
* 以大根堆(根結點為最大值)爲例，堆排序的實現過程分爲兩個子過程。
* 第一步爲取出大根堆的根節點(當前堆的最大值), 由於取走了一個節點，故需要對餘下的元素重新建堆。
* 重新建堆後繼續取根節點，循環直至取完所有節點，此時數組已經有序。
* [`heap sort`](https://docs.google.com/presentation/d/e/2PACX-1vRAGwnUvg6BcXoML5u9f4gO6YKcz0vXf7bDnPho_S7mG5D0SBR78djt91RKUPMxqNfkVIcu3l5WCXPh/pub?start=false&loop=false&delayms=3000&slide=id.p),[`class6`](https://www.youtube.com/watch?v=NyLbNmPD7HM&feature=youtu.be)

---
### Week 7:Merge Sort
* 資料序列分成兩個子序列, 排序每一半, 然後再把排序好的兩個子序列合併成為一個有序的序列.
* Merge Sort的時間複雜度是O(nlogn)
![](https://algorithm.yuanbin.me/shared-files/images/merge_sort.gif)
* [`merge sort`](https://docs.google.com/presentation/d/e/2PACX-1vToxkEzc1H1RT5MI9G941KQFBC7GO_Efn95wTqXLEdr3LDBSNcQb-M46IOC-_RzZih6IBEwwy3rWQuE/pub?start=false&loop=false&delayms=3000&slide=id.p),[`class7`](https://www.youtube.com/watch?v=7QsqF9-jdtE&feature=youtu.be)

---
### Week 8:Binary Tree 
* 定義: 樹中的每個節點, 最多只能有兩個子節點
1. 對二元樹的理解
* 二元樹與樹的區別為:
>    * a. 樹中節點的子節點樹沒有限制, 而二元樹中限制節點數為不超過兩個
>    * b. 樹的節點沒有左右之分, 但二元樹的節點是分左右的
2. 二元樹有五種基本型態
    * a. 空二元樹, 連根節點都沒有
    * b. 只有一個根節點的二元樹
    * c. 只有左樹
    * d. 只有右樹
    * e. 完全二元樹: 若設二元樹的高度為h, 除了第h層外, 其它各層的節點樹都達到最大個數,
第h層有葉節點, 並且葉節點都是從左到右依次排序, 此即完全二元樹
1. 滿二元樹: 除了葉節點外, 每個節點都有左右子節點, 且葉節點都處在最底層
2. 滿二元樹必為完全二元樹, 完全二元樹不必然為滿二元樹
二元樹常被用作二元搜尋樹, 二元排序樹, 二元堆

* [`binary tree`](https://docs.google.com/presentation/d/e/2PACX-1vSC3P8sGElP48mJTjqT309470SmTFBwJXWsU9hTX2hg5tVpiG4yC703qA7ibPep-Qakmm2Mw_F-ScZh/pub?start=false&loop=false&delayms=3000&slide=id.p),[`class8`](https://www.youtube.com/watch?v=quU2S-cK42k&feature=youtu.be)

---
### Week 9:Binary Search Tree
* 二元搜尋樹的查詢, 插入, 走訪, 查詢最大最小值和刪除操作
* 刪除節點有兩個子節點的時候, 要用它的中序後繼來代替該節點,
* 演算法為: 找到被刪除節點的右子節點, 然後查詢此右子節點下的最後一個左子節點, 即此顆子樹的最小值節點, 這就是被刪除節點的中序後繼節點.

* 何謂前序, 中序, 後序?
* 以上圖右邊的三層樹為例, 看1~2層的子樹:
> * 前序: 6 -> 5 -> 8
> * 中序: 5 -> 6 -> 8
> * 後序: 5 -> 8 -> 6

* 定義: 若一顆二元樹滿足以下兩點:
> * a. 左子節點的值小於節點的值
> * b. 右子節點的值大於節點的值
* 即可稱為二元搜尋樹

* [`binary search tree`](https://docs.google.com/presentation/d/e/2PACX-1vQgUh73yvSdxAvMH50DHWJ5lsCX8-daMxtoltU9rYW7xCmqYz2A1wOv0Vcx_F9KO5ZUvZBv3IF1TjGi/pub?start=false&loop=false&delayms=3000&slide=id.p),[`class9`](https://www.youtube.com/watch?v=1iiub4WFjtE&feature=youtu.be)

---
### Week 10:Red Black Tree
* 樹的平衡: 所謂樹的平衡指的是, 樹中每個節點的左邊後代的數目應該與其右邊後代的數目大致相等(不用完全一樣多).
* 對於用隨機數構成的二元樹, 一般來說是大致平衡的, 但是對於有順序的資料, 就可能導致二元樹極度的不平衡了. 在最極端的情況下, 甚至會退化成list, 此時的時間複雜度會退化到O(n), 而不再是平衡樹的O(logn)了.

* 紅黑樹(R-B Tree): 紅黑樹是增加了某些特性的二元搜尋樹, 它可以保持樹的大致平衡. 主要的思路為: 在插入或刪除節點的時候, 檢查是否破壞了樹的某些特徵, 若破壞了, 則進行糾正, 進而保持樹的平衡.
* 紅黑樹的特徵:
>* 節點都有顏色(紅/黑)
>* 在插入和刪除的過程中, 要遵循保持這些顏色的不同排列的規則
* 紅黑樹的規則(紅黑規則):
> 1. 每個節點不是紅就是黑的
> 2. 根總是黑色的
> 3. 若節點是紅色的, 則其子節點必為黑色, 反之不必為真(亦即若節點是黑色, 則其子節點可為紅也可為黑), 這條規則其實也是在說明就垂直方向來看, 紅色節點不可以相連
> 4. 每個空子節點都是黑色的: 所謂的空子節點指的是, 對非葉節點而言, 本可能有, 但實際沒有的那個子節點. 譬如一個節點只有右子節點, 那麼其空缺的左子節點就是空子節點
> 5. 從根節點到葉節點或空子節點的每條路徑(簡單路徑), 必須包含相同數目的黑色節點(這些黑色節點的數目也稱為黑色高度)

* [`red black tree`](https://docs.google.com/presentation/d/e/2PACX-1vRxyJRARq0BNuGJq_o2cUHIXBWrRSZrAOyXOSt9qCTSjQtyp8XqFq3VuNn3gCt3sXenOZmWLqIjcyFs/pub?start=false&loop=false&delayms=3000&slide=id.p),[`class10`](https://www.youtube.com/watch?v=aC5KcE4GLYw&feature=youtu.be)`

---
### Week 11:Hash Table
* Hash Table是根據關鍵碼值 (Key-Value) 而直接進行訪問的數據結構
>* 通過把關鍵碼值映射到表中壹個位置來訪問記錄，以加快查找的速度
>* 哈希表的實現主要需要解決兩個問題，哈希函數和沖突解決
* 哈希函數
* 哈希函數也叫散列函數
>* 它對不同的輸出值得到一個固定長度的消息摘要
>* 理想的哈希函數對于不同的輸入應該産生不同的結構，
>* 同時散列結果應當具有同一性
* 沖突解決
>* 現實中的哈希函數不是完美的，當兩個不同的輸入值對應一個輸出值時，就會産生“碰撞”，這個時候便需要解決沖突。
>* 常見的沖突解決方法有開放定址法，鏈地址法，建立公共溢出區等。實際的哈希表實現中，使用最多的是鏈地址法
* Hash的應用
>* Hash主要用于信息安全領域中加密算法，它把壹些不同長度的信息轉化成雜亂的128位的編碼,這些編碼值叫做Hash值. 也可以說，Hash就是找到壹種數據內容和數據存放地址之間的映射關系。
>* 查找：哈希表，又稱爲散列，是壹種更加快捷的查找技術。當我知道key值以後，我就可以直接計算出這個元素在集合中的位置，根本不需要壹次又壹次的查找！

* 優缺點
>* 優點：不論哈希表中有多少數據，查找、插入、刪除（有時包括刪除）只需要接近常量的時間即0(1）的時間級。速度比樹快，樹的操作通常需要O(N)的時間級。哈希表不僅速度快，編程實現也相對容易。
>* 缺點：它是基于數組的，數組創建後難于擴展，某些哈希表被基本填滿時，性能下降得非常嚴重。
* [`hash table`](https://docs.google.com/presentation/d/e/2PACX-1vT1HO9Nl475k2bR0l1x8_Tr4V5Wzx0BEqp9bpmHckvj8kTeJehhYVlOJUDVPhLQm6kjGCJ_sLMSBUw5/pub?start=false&loop=false&delayms=3000&slide=id.p),[`class11`](https://www.youtube.com/watch?v=7C5f2ttq79Y&feature=youtu.be)

---
### Week 12:Breadth-First Search
* 寬度優先搜索(Breadth First Search,又稱廣度優先搜索)
* 是從根節點開始，遍歷完畢整張圖，不考慮結果所在的位置， 無論如何都要遍歷完畢整張地圖才終止。
* 按照就近原則進行， 距離原點相同的節點的訪問順序是相近的。
* 基本思路:
    1. 把根節點放到隊列的末尾。
    2. 每次從隊列的頭部取出一個元素，查看這個元素所有的下一級元素，把它們放到隊列的末尾。並把這個元素記爲它下一級元素的前驅。
    3. 找到所要找的元素時結束程序。
    4. 如果遍曆整個樹還沒有找到，結束程序。

1. 數據結構上的運用
    * BFS
        * 用queue的形式
        * 先進先出
        * 需要與節點數成正比的記憶體空間
        * 
2. 複雜度
    * BFS:
        * 空間複雜度為O（v）
        * 時間復雜度為O(|V|+|E|) 
        * 適合大範圍的尋找

3. 思路
    * 廣度優先遍曆使用隊列(queue)來實現,整個過程也可以看作一個倒立的樹形:
        * 把根結點放到隊列的末尾
        * 每次從隊列的頭部取出一個元素,查看這個元素所有的下一級元素,把它們放在隊列的末尾。並且把這個元素記爲下一個元素的前驅
        * 找到所有要找的元素時結束程序
        * 如果遍曆整個樹還沒有找到,結束程序

  
* [`breadth-first search`](https://docs.google.com/presentation/d/e/2PACX-1vSYJYXUXvGAeTZ5fknxj_-EPm3zxgy4ITdImrXzy63Y-iZgs8uwVNmOaZlnx9fUNzsbo8kphvMTa0c4/pub?start=false&loop=false&delayms=3000&slide=id.p),[`class12`](https://www.youtube.com/watch?v=7kyDFh_KdNs&feature=youtu.be),[`Pair Programming`](https://www.youtube.com/watch?v=vgkahOzFH2Q&feature=youtu.be)

---
### Week 13:Depth-First Search
* 深度優先搜索(Depth First Search)屬于算法的一種
* 是從根節點開始，逐個訪問每一條路徑，對於具有多子節點的節點而言，先搜尋到某一條子路的最深處，再逐個回溯前驅節點。
* 基本思路:
    1. 訪問頂點v
    2. 依次從v的未被訪問的鄰接點出發，對圖進行深度優先遍曆；直至圖中和v有路徑相通的頂點都被訪問。
    3. 若此時圖中尚有頂點未被訪問，則從一個未被訪問的頂點出發，重新進行深度優先遍曆，直到圖中所有頂點均被訪問過爲止。

1. 數據結構上的運用
        * 用遞歸的形式，用到了stack
        * 先進後出
        * 較省記憶體空間

2. 複雜度
        * 空問複雜度為O(V）
        * 時間複雜度為O(V+E)
        * 適合目標明確

3. 思路
    * 深度優先遍曆用棧(stack)實現,整個過程可以想象成一個倒立的樹形:
        * 把根結點壓入棧中
        * 每次從棧中彈出一個元素,搜索所有在它下一級的元素,把這些元素壓入棧中。並且把這個元素記爲它下一個元素的前驅。
        * 找到所有要找的元素時結束程序
        * 如果遍曆整個樹還沒有找到，結束程序

* [`depth-first search`](https://docs.google.com/presentation/d/e/2PACX-1vTma_vOZyE70O23KWw4I4Y78aAaT5fJSTq7Mae912kCwka_u5ZMWPoo14D86-x-57kZPbb6hAGktSW4/pub?start=false&loop=false&delayms=3000&slide=id.p),[`class13`](https://www.youtube.com/watch?v=f_lLannWfrM&feature=youtu.be)

---
### Week 14:Minimum Spanning Tree
* 在找最小生成樹結點之前，需要對所有權重邊做從小到大排序。
* 將排序好的權重邊依次加入到最小生成樹中，如果加入時產生迴路就跳過這條邊，加入下一條邊。
* 當所有結點都加入到最小生成樹中之後，就找出了最小生成樹。
*步驟
>* 在給定含n個頂點的帶權值的連通圖表示為G=（V,E）（註：V指頂點集，E指邊集），尋找一條路徑使得權值和最小。設VT為點集表示最小生成樹中的頂點集，ET表示最小生成樹的邊集。
>1. 排序：將E中所有邊按權值大小從小到大排序；
>2. 將每個頂點加入一個集合，即n個點n個集合；
>3. 按順序訪問每條邊，若該邊的兩端點屬於不同集合，則合併兩個集合併將邊加入ET中；
>4. 最後得到的GT=（VT，ET）即為最小生成樹。

* [`minimum spanning tree`](https://docs.google.com/presentation/d/e/2PACX-1vTorNDEyhYA4ZAt5jEqOmFs2cQiUAYvkTp-R0DOn9B3c1MuUecV-a1wNakFIrJxA6AoUFGzbl3OQBIJ/pub?start=false&loop=false&delayms=3000&slide=id.p)[`class14`](https://www.youtube.com/watch?v=lgBja7u5nrI&feature=youtu.be),[`LeetCode 490. The MazeURL`](https://leetcode.com/articles/the-maze/),[`Searching a maze using DFS and BFS in Python 3`](https://codereview.stackexchange.com/questions/197356/searching-a-maze-using-dfs-and-bfs-in-python-3)
---
### Week 15:Shortest Path
* Dijkstra算法是典型最短路徑算法
* 用於計算一個節點到其他節點的最短路徑
* 主要特點是以起始點為中心向外層層擴展(廣度優先搜索思想)，直到擴展到終點為止
* 通過Dijkstra計算圖G中的最短路徑時，需要指定起點s(即從頂點s開始計算)。
* 此外，引進兩個集合S和U。S的作用是記錄已求出最短路徑的頂點(以及相應的最短路徑長度)，而U則是記錄還未求出最短路徑的頂點(以及該頂點到起點s的距離)。
* 初始時，S中只有起點s；U中是除s之外的頂點，並且U中頂點的路徑是"起點s到該頂點的路徑"。然後，從U中找出路徑最短的頂點，並將其加入到S中；接著，更新U中的頂點和頂點對應的路徑。 然後，再從U中找出路徑最短的頂點，並將其加入到S中；接著，更新U中的頂點和頂點對應的路徑。 ... 重複該操作，直到遍歷完所有頂點。
* 操作步驟

>1. 初始時，S只包含起點s；U包含除s外的其他頂點，且U中頂點的距離為"起點s到該頂點的距離"[例如，U中頂點v的距離為(s,v)的長度，然後s和v不相鄰，則v的距離為∞]。
>2. 從U中選出"距離最短的頂點k"，並將頂點k加入到S中；同時，從U中移除頂點k。
>3. 更新U中各個頂點到起點s的距離。之所以更新U中頂點的距離，是由於上一步中確定了k是求出最短路徑的頂點，從而可以利用k來更新其它頂點的距離；例如，(s,v)的距離可能大於(s,k)+(k,v)的距離。

4. 重複步驟(2)和(3)，直到遍歷完所有頂點。
* [`shortest path`](https://docs.google.com/presentation/d/e/2PACX-1vTgHO5AkHJS6iN6bnnBMMdHv6E4rabnrC0KwyTRfjad8Ab3IQjbnGvZuQOjDC9t7nKqeroiwcuasJrI/pub?start=false&loop=false&delayms=3000&slide=id.p),[`class15`](https://www.youtube.com/watch?v=BHoCZYbkri0&feature=youtu.be)

---
### Week 16:
* [`Overview`](https://docs.google.com/presentation/d/e/2PACX-1vSkbZghFr5Y3VG3b-BKCZiLNHyhcMIxFmNDHn-tgWQqH4vaGjulKASn_ex_LLDJwxPIRCacGQnBRYrI/pub?start=false&loop=false&delayms=3000&slide=id.p)

---
### Week 17:
期末考
---
### Week 18:
放假
---


## :books:Learning resources 
* 在線練習:[`codesigna`](https://codesignal.com),[`leetcode`](https://leetcode.com)

* GitHub:[`GitHub秘籍`](https://snowdream86.gitbooks.io/github-cheat-sheet/content/zh/index.html#%E4%BB%BB%E5%8A%A1%E5%88%97%E8%A1%A8),[`Markdown語法說明`](https://github.com/othree/markdown-syntax-zhtw)

* Python:[`learnxinyminutes-zh-cn`](https://github.com/haiiiiiyun/learnxinyminutes-zh-cn/blob/master/book/part1/python3.md),[`Python 3.9文档`](https://www.osgeo.cn/cpython/), [`Python教學`](https://docs.python.org/zh-tw/3/tutorial/index.html)

* 流程圖:[`draw.io`](https://www.draw.io/),[`coggle`](https://coggle.it/)

 
## :sheep:About Me
- **姓名**：楊嘉政
- **學號**: 06170271
- **班級**: 巨資三B 
- **學校**：Soochow University（東吳大學）
- **主修學系**：Big Data Management（巨量資料管理）
- **常用程式語言**：Python、R
- **Email**: yongkahzin@gmail.com
- **崇尚簡約**

## :love_letter:Review
剛開學第一堂課，就知道這堂課有挑戰性，不過經過老師這一學期下來的教導和助教的監督，我的寫程式的能力進步許多了，也感謝我自己沒有放棄，努力撐下來才完成這學期的課程，老師辛苦了，謝謝你。也感謝助教！

## :link:Reference
所有來自網際網路的參考資料皆已附上超連結可供前往原網站 謝謝所有的原作者和协助者
['Data Structures and Algorithms'](https://www.programiz.com/dsa),['Preface · GitBook'](https://yotsuba1022.gitbooks.io/data-structure-note/content/),['Introduction · 資料結構&演算法筆記'](https://algorithm.yuanbin.me/zh-tw/)


