# HW6 Dijkstra/Kruskal
## 學習歷程：

### 原理:

#### Dijkstra
* Dijkstra算法是典型最短路徑算法
* 用於計算一個節點到其他節點的最短路徑
* 主要特點是以起始點為中心向外層層擴展(廣度優先搜索思想)，直到擴展到終點為止


#### 基本思想
* 通過Dijkstra計算圖G中的最短路徑時，需要指定起點s(即從頂點s開始計算)。
* 此外，引進兩個集合S和U。S的作用是記錄已求出最短路徑的頂點(以及相應的最短路徑長度)，而U則是記錄還未求出最短路徑的頂點(以及該頂點到起點s的距離)。
* 初始時，S中只有起點s；U中是除s之外的頂點，並且U中頂點的路徑是"起點s到該頂點的路徑"。然後，從U中找出路徑最短的頂點，並將其加入到S中；接著，更新U中的頂點和頂點對應的路徑。 然後，再從U中找出路徑最短的頂點，並將其加入到S中；接著，更新U中的頂點和頂點對應的路徑。 ... 重複該操作，直到遍歷完所有頂點。


#### 操作步驟

1. 初始時，S只包含起點s；U包含除s外的其他頂點，且U中頂點的距離為"起點s到該頂點的距離"[例如，U中頂點v的距離為(s,v)的長度，然後s和v不相鄰，則v的距離為∞]。

2. 從U中選出"距離最短的頂點k"，並將頂點k加入到S中；同時，從U中移除頂點k。

3. 更新U中各個頂點到起點s的距離。之所以更新U中頂點的距離，是由於上一步中確定了k是求出最短路徑的頂點，從而可以利用k來更新其它頂點的距離；例如，(s,v)的距離可能大於(s,k)+(k,v)的距離。

4. 重複步驟(2)和(3)，直到遍歷完所有頂點。

#### Kruskal
* 在找最小生成樹結點之前，需要對所有權重邊做從小到大排序。
* 將排序好的權重邊依次加入到最小生成樹中，如果加入時產生迴路就跳過這條邊，加入下一條邊。
* 當所有結點都加入到最小生成樹中之後，就找出了最小生成樹。
#### 步驟
* 在給定含n個頂點的帶權值的連通圖表示為G=（V,E）（註：V指頂點集，E指邊集），尋找一條路徑使得權值和最小。設VT為點集表示最小生成樹中的頂點集，ET表示最小生成樹的邊集。

    1. 排序：將E中所有邊按權值大小從小到大排序；

    2. 將每個頂點加入一個集合，即n個點n個集合；

    3. 按順序訪問每條邊，若該邊的兩端點屬於不同集合，則合併兩個集合併將邊加入ET中；

    4. 最後得到的GT=（VT，ET）即為最小生成樹。



## Dijkstra流程圖
![](https://github.com/ykz0608/DSA/blob/master/image/Dijkstra.svg)
* 初始狀態：S是已計算出最短路徑的頂點集合
* U是未計算除最短路徑的頂點的集合 
1. 將頂點D加入到S中。
    * 此時，S={D(0)}, U={A(∞),B(∞),C(3),E(4),F(∞),G(∞)}。     
    * 注:C(3)表示C到起點D的距離是3。

2. 將頂點C加入到S中。
    * 上一步操作之後，U中頂點C到起點D的距離最短；
    * 將C加入到S中，同時更新U中頂點的距離。以頂點F爲例，之前F到D的距離爲∞；但是將C加入到S之後，F到D的距離爲9=(F,C)+(C,D)。
    * 此時，S={D(0),C(3)}, U={A(∞),B(23),E(4),F(9),G(∞)}。

3. 將頂點E加入到S中。
    * 上一步操作之後，U中頂點E到起點D的距離最短；
    * 將E加入到S中，同時更新U中頂點的距離。還是以頂點F爲例，之前F到D的距離爲9；但是將E加入到S之後，F到D的距離爲6=(F,E)+(E,D)。
    * 此時，S={D(0),C(3),E(4)}, U={A(∞),B(23),F(6),G(12)}。

4. 將頂點F加入到S中。
    * 此時，S={D(0),C(3),E(4),F(6)}, U={A(22),B(13),G(12)}。

5. 將頂點G加入到S中。
    * 此時，S={D(0),C(3),E(4),F(6),G(12)}, U={A(22),B(13)}。

6. 將頂點B加入到S中。
    * 此時，S={D(0),C(3),E(4),F(6),G(12),B(13)}, U={A(22)}。

7. 將頂點A加入到S中。
    * 此時，S={D(0),C(3),E(4),F(6),G(12),B(13),A(22)}。

* 此時，起點D到各個頂點的最短距離就計算出來了：A(22) B(13) C(3) D(0) E(4) F(6) G(12)。

## Kruskal流程圖
![](https://github.com/ykz0608/DSA/blob/master/image/Kruskal.svg)
1. 將邊<E,F>加入R中。
    * 邊<E,F>的權值最小，因此將它加入到最小生成樹結果R中。
2. 將邊<C,D>加入R中。
    * 上一步操作之後，邊<C,D>的權值最小
    * 將它加入到最小生成樹結果R中。
3. 將邊<D,E>加入R中。
    * 上一步操作之後，邊<D,E>的權值最小
    * 將它加入到最小生成樹結果R中。
4. 將邊<B,F>加入R中。
    * 上一步操作之後，邊<C,E>的權值最小
    * 但<C,E>會和已有的邊構成迴路
    * 因此，跳過邊<C,E>。同理，跳過邊<C,F>。將邊<B,F>加入到最小生成樹結果R中。
5. 將邊<E,G>加入R中。
    * 上一步操作之後，邊<E,G>的權值最小
    * 將它加入到最小生成樹結果R中。
6. 將邊<A,B>加入R中。
    * 上一步操作之後，邊<F,G>的權值最小，
    * 但<F,G>會和已有的邊構成迴路；因此，跳過邊<F,G>。
    * 跳過邊<B,C>。將邊<A,B>加入到最小生成樹結果R中。

* 此時，最小生成樹構造完成！它包括的邊依次是：<E,F> <C,D> <D,E> <B,F> <E,G> <A,B>。

## 作業格式


```python
# Python program for Dijkstra's single  
# source shortest path algorithm. The program is  
# for adjacency matrix representation of the graph 
# Python program for Kruskal's algorithm to find 
# Minimum Spanning Tree of a given connected,  
# undirected and weighted graph 

from collections import defaultdict 

#Class to represent a graph 
class Graph(): 

    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = [] 
        self.graph_matrix = [[0 for column in range(vertices)]  
                    for row in range(vertices)] 
    def addEdge(self,u,v,w): 
        """
        :type u,v,w: int
        :rtype: None
        """
    def Dijkstra(self, s): 
        """
        :type s: int
        :rtype: dict
        """
    def Kruskal(self):
        """
        :rtype: dict
        """
  
        
  
```        

## 嘗試寫Dijkstra code


```python
from collections import defaultdict 
import math

class add_g:
    def __init__(self,start,bourn,distance):
        if add_g:
            self.s=start
            self.b=bourn
            self.d=distance
        else:
            return 
         
class Graph(): 
    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = [] 
        self.graph_matrix = [[0 for column in range(vertices)]  
                    for row in range(vertices)] 
        
    def addEdge(self,u,v,w): 
        self.graph.append([u,v,w]) 

    def Dijkstra(self, s): 
        z=0
        dict={}
        tem=[]
        weight_list=[math.inf]*self.V
        for i in range(self.V):
            if i != s:
                pass
            else:
                weight_list[i]=0
            
                
                
        while len(tem) < self.V:  
            weight_list_v2 = sorted(weight_list)
            for p in range(self.V):
                if weight_list[p]==weight_list_v2[z] and p not in tem:
                    tem.append(p)
                    break
            if p:        
                if p != 0:
                    for r in range(self.V):       
                        if weight_list[r] != math.inf:
                            if self.graph[p][r]!=0:
                                if weight_list[r] < weight_list[p]+self.graph[p][r]:
                                    pass
                                elif weight_list[r] > weight_list[p]+self.graph[p][r]:
                                    weight_list[r] = weight_list[p]+self.graph[p][r]
                                else:
                                    pass
                        else:
                            if self.graph[p][r] == 0 :
                                pass
                            elif self.graph[p][r] != 0:
                                weight_list[r]=weight_list[p]+self.graph[p][r] 
                            else:
                                pass


                elif p == 0:
                    for q in range(self.V): 
                        if weight_list[q] == math.inf:
                            if self.graph[p][q] != 0 :
                                weight_list[q] = self.graph[p][q]
                else:
                    pass


                z+=1
            
        for jkl in range(self.V):
            dict[str(jkl)]=weight_list[jkl]
        return dict
    
```

助教測值
```python

g = Graph(9)
g.graph = [[0,4,0,0,0,0,0,8,0],
           [4,0,8,0,0,0,0,11,0],
           [0,8,0,7,0,4,0,0,2],
           [0,0,7,0,9,14,0,0,0],
           [0,0,0,9,0,10,0,0,0],
           [0,0,4,14,10,0,2,0,0],
           [0,0,0,0,0,2,0,1,6],
           [8,11,0,0,0,0,1,0,7],
           [0,0,2,0,0,0,6,7,0]]
g.Dijkstra(0)
```


```python
g = Graph(9)
g.graph = [[0,4,0,0,0,0,0,8,0],
           [4,0,8,0,0,0,0,11,0],
           [0,8,0,7,0,4,0,0,2],
           [0,0,7,0,9,14,0,0,0],
           [0,0,0,9,0,10,0,0,0],
           [0,0,4,14,10,0,2,0,0],
           [0,0,0,0,0,2,0,1,6],
           [8,11,0,0,0,0,1,0,7],
           [0,0,2,0,0,0,6,7,0]]
g.Dijkstra(0)
```




    {'0': 0,
     '1': inf,
     '2': inf,
     '3': inf,
     '4': inf,
     '5': inf,
     '6': inf,
     '7': inf,
     '8': inf}



出現了error 再試試


```python
from collections import defaultdict 
import math

class add_g:
    def __init__(self,start,bourn,distance):
        if add_g:
            self.s=start
            self.b=bourn
            self.d=distance
        else:
            return 
         
class Graph(): 
    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = [] 
        self.graph_matrix = [[0 for column in range(vertices)]  
                    for row in range(vertices)] 
        
    def addEdge(self,u,v,w): 
        self.graph.append([u,v,w]) 

    def Dijkstra(self, s): 
        z=0
        dict={}
        tem=[]
        weight_list=[math.inf]*self.V
        for i in range(self.V):
            if i != s:
                pass
            else:
                weight_list[i]=0
            
                
                
        while len(tem) < self.V:  
            weight_list_v2 = sorted(weight_list)
            for p in range(self.V):
                if weight_list[p]==weight_list_v2[z] and p not in tem:
                    tem.append(p)
                    break
                if p != 0:
                    for r in range(self.V):       
                        if weight_list[r] != math.inf:
                            if self.graph[p][r]!=0:
                                if weight_list[r] < weight_list[r]+self.graph[p][p]:
                                    pass
                                elif weight_list[r] > weight_list[r]+self.graph[p][p]:
                                    weight_list[r] = weight_list[p]+self.graph[p][r]
                                else:
                                    pass
                        else:
                            if self.graph[p][r] == 0 :
                                pass
                            elif self.graph[p][r] != 0:
                                weight_list[r]=weight_list[p]+self.graph[p][r] 
                            else:
                                pass


                elif p == 0:
                    for q in range(self.V): 
                        if weight_list[q] == math.inf:
                            if self.graph[p][q] != 0 :
                                weight_list[q] = self.graph[p][q]
                else:
                    pass


                z+=1
            
        for jkl in range(self.V):
            dict[str(jkl)]=weight_list[jkl]
        return dict
    
```


```python
g = Graph(9)
g.graph = [[0,4,0,0,0,0,0,8,0],
           [4,0,8,0,0,0,0,11,0],
           [0,8,0,7,0,4,0,0,2],
           [0,0,7,0,9,14,0,0,0],
           [0,0,0,9,0,10,0,0,0],
           [0,0,4,14,10,0,2,0,0],
           [0,0,0,0,0,2,0,1,6],
           [8,11,0,0,0,0,1,0,7],
           [0,0,2,0,0,0,6,7,0]]
g.Dijkstra(0)
```


    ---------------------------------------------------------------------------

    IndexError                                Traceback (most recent call last)

    <ipython-input-23-47e73fc8b64a> in <module>
          9            [8,11,0,0,0,0,1,0,7],
         10            [0,0,2,0,0,0,6,7,0]]
    ---> 11 g.Dijkstra(0)
    

    <ipython-input-22-b6f7ae230fb6> in Dijkstra(self, s)
         37             weight_list_v2 = sorted(weight_list)
         38             for p in range(self.V):
    ---> 39                 if weight_list[p]==weight_list_v2[z] and p not in tem:
         40                     tem.append(p)
         41                     break
    

    IndexError: list index out of range


還是error 在試試

最後我發現要改變p和r的位置 2個變數的位置錯了


```python
from collections import defaultdict 
import math

class add_g:
    def __init__(self,start,bourn,distance):
        if add_g:
            self.s=start
            self.b=bourn
            self.d=distance
        else:
            return 
         
class Graph(): 
    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = [] 
        self.graph_matrix = [[0 for column in range(vertices)]  
                    for row in range(vertices)] 
        
    def addEdge(self,u,v,w): 
        self.graph.append([u,v,w]) 

    def Dijkstra(self, s): 
        z=0
        dict={}
        tem=[]
        weight_list=[math.inf]*self.V
        for i in range(self.V):
            if i != s:
                pass
            else:
                weight_list[i]=0
            
                
                
        while len(tem) < self.V:  
            weight_list_v2 = sorted(weight_list)
            for p in range(self.V):
                if weight_list[p]==weight_list_v2[z] and p not in tem:
                    tem.append(p)
                    break
            if tem:        
                if p != 0:
                    for r in range(self.V):       
                        if weight_list[r] != math.inf:
                            if self.graph[p][r]!=0:
                                if weight_list[r] < weight_list[p]+self.graph[p][r]:
                                    pass
                                elif weight_list[r] > weight_list[p]+self.graph[p][r]:
                                    weight_list[r] = weight_list[p]+self.graph[p][r]
                                else:
                                    pass
                        else:
                            if self.graph[p][r] == 0 :
                                pass
                            elif self.graph[p][r] != 0:
                                weight_list[r]=weight_list[p]+self.graph[p][r] 
                            else:
                                pass


                elif p == 0:
                    for q in range(self.V): 
                        if weight_list[q] == math.inf:
                            if self.graph[p][q] != 0 :
                                weight_list[q] = self.graph[p][q]
                else:
                    pass


                z+=1
            
        for jkl in range(self.V):
            dict[str(jkl)]=weight_list[jkl]
        return dict
```


```python
g = Graph(9)
g.graph = [[0,4,0,0,0,0,0,8,0],
           [4,0,8,0,0,0,0,11,0],
           [0,8,0,7,0,4,0,0,2],
           [0,0,7,0,9,14,0,0,0],
           [0,0,0,9,0,10,0,0,0],
           [0,0,4,14,10,0,2,0,0],
           [0,0,0,0,0,2,0,1,6],
           [8,11,0,0,0,0,1,0,7],
           [0,0,2,0,0,0,6,7,0]]
g.Dijkstra(0)
```




    {'0': 0, '1': 4, '2': 12, '3': 19, '4': 21, '5': 11, '6': 9, '7': 8, '8': 14}




```python
g = Graph(9)
g.graph =  [[0,4,0,0,0,0,0,8,0],
            [4,0,8,0,0,0,0,11,0],
            [0,8,0,7,0,4,0,0,2],
            [0,0,7,0,9,14,0,0,0],
            [0,0,0,9,0,10,0,0,0],
            [0,0,4,14,10,0,2,0,0],
            [0,0,0,0,0,2,0,1,6],
            [8,11,0,0,0,0,1,0,7],
            [0,0,2,0,0,0,6,7,0]]
g.Dijkstra(4)
```




    {'0': 21, '1': 22, '2': 14, '3': 9, '4': 0, '5': 10, '6': 12, '7': 13, '8': 16}



成功!是接下來Kruskal

有點難 所以參考了[Pseudocode](https://iq.opengenus.org/kruskal-minimum-spanning-tree-algorithm/) 
```python
Kruskal()
	solve all edges in ascending order of their weight in an array e
	ans = 0
	for i = 1 to m
		v = e.first
		u = e.second
		w = e.weight
		if merge(v,u) // there will be no cycle
			then ans += w
```


```python
from collections import defaultdict 
import math

class add_g:
    def __init__(self,start,bourn,distance):
        if add_g:
            self.s=start
            self.b=bourn
            self.d=distance
        else:
            return 
         
class Graph(): 
    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = [] 
        self.graph_matrix = [[0 for column in range(vertices)]  
                    for row in range(vertices)] 
        
    def addEdge(self,u,v,w): 
        self.graph.append([u,v,w]) 

    def Dijkstra(self, s): 
        z=0
        dict={}
        tem=[]
        weight_list=[math.inf]*self.V
        for i in range(self.V):
            if i != s:
                pass
            else:
                weight_list[i]=0
            
                
                
        while len(tem) < self.V:  
            weight_list_v2 = sorted(weight_list)
            for p in range(self.V):
                if weight_list[p]==weight_list_v2[z] and p not in tem:
                    tem.append(p)
                    break
            if tem:        
                if p != 0:
                    for r in range(self.V):       
                        if weight_list[r] != math.inf:
                            if self.graph[p][r]!=0:
                                if weight_list[r] < weight_list[p]+self.graph[p][r]:
                                    pass
                                elif weight_list[r] > weight_list[p]+self.graph[p][r]:
                                    weight_list[r] = weight_list[p]+self.graph[p][r]
                                else:
                                    pass
                        else:
                            if self.graph[p][r] == 0 :
                                pass
                            elif self.graph[p][r] != 0:
                                weight_list[r]=weight_list[p]+self.graph[p][r] 
                            else:
                                pass


                elif p == 0:
                    for q in range(self.V): 
                        if weight_list[q] == math.inf:
                            if self.graph[p][q] != 0 :
                                weight_list[q] = self.graph[p][q]
                else:
                    pass


                z+=1
            
        for jkl in range(self.V):
            dict[str(jkl)]=weight_list[jkl]
        return dict
    
    def find(self, pa_node, m): 
        
        if pa_node[m] != m: 
            return self.find(pa_node, pa_node[m]) 
        elif pa_node[m] == m:
            return m
        else:
            pass 
  

    def union(self, pa_node, tem_v2, x, y): 
        
        xroot = self.find(pa_node, x) 
        yroot = self.find(pa_node, y) 
        
        if pa_node:
            
            if tem_v2[xroot] > tem_v2[yroot]: 
                pa_node[yroot] = xroot 
                
            elif tem_v2[xroot] < tem_v2[yroot]: 
                pa_node[xroot] = yroot 
                
            else : 
                pa_node[yroot] = xroot 
                tem_v2[xroot] += 1
        else:
            pass

    def Kruskal(self):
        final = dict();result =[] 
        m = 0;n = 0
        pa_node = [] ; tem_v2 = [] 
        self.graph =  sorted(self.graph,key=lambda item: item[2]) 
  
        for node in range(self.V): 
            pa_node.append(node) 
            tem_v2.append(0) 
      
        while n < self.V -1 : 

            u,v,w =  self.graph[m] 
            m = m + 1
            x = self.find(pa_node, u) ;y = self.find(pa_node ,v) 
  
            if x ==y:
                pass
            elif x != y: 
                n = n + 1     
                result.append([u,v,w]) 
                self.union(pa_node, tem_v2, x, y)
            else:
                pass
            for u,v,weight  in result: 
                return result
```

助教測值
```python
g = Graph(4)
g.addEdge(0,1,10)
g.addEdge(0,2,6)
g.addEdge(0,3,5)
g.addEdge(1,3,15)
g.addEdge(2,3,4)
g.Kruskal()
```



```python
g = Graph(4)
g.addEdge(0,1,10)
g.addEdge(0,2,6)
g.addEdge(0,3,5)
g.addEdge(1,3,15)
g.addEdge(2,3,4)
g.Kruskal()
```




    [[2, 3, 4]]



只有一個

修改後:


```python
from collections import defaultdict 
import math

class add_g:
    def __init__(self,start,bourn,distance):
        if add_g:
            self.s=start
            self.b=bourn
            self.d=distance
        else:
            return 
         
class Graph(): 
    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = [] 
        self.graph_matrix = [[0 for column in range(vertices)]  
                    for row in range(vertices)] 
        
    def addEdge(self,u,v,w): 
        self.graph.append([u,v,w]) 

    def Dijkstra(self, s): 
        z=0
        dict={}
        tem=[]
        weight_list=[math.inf]*self.V
        for i in range(self.V):
            if i != s:
                pass
            else:
                weight_list[i]=0
            
                
                
        while len(tem) < self.V:  
            weight_list_v2 = sorted(weight_list)
            for p in range(self.V):
                if weight_list[p]==weight_list_v2[z] and p not in tem:
                    tem.append(p)
                    break
            if tem:        
                if p != 0:
                    for r in range(self.V):       
                        if weight_list[r] != math.inf:
                            if self.graph[p][r]!=0:
                                if weight_list[r] < weight_list[p]+self.graph[p][r]:
                                    pass
                                elif weight_list[r] > weight_list[p]+self.graph[p][r]:
                                    weight_list[r] = weight_list[p]+self.graph[p][r]
                                else:
                                    pass
                        else:
                            if self.graph[p][r] == 0 :
                                pass
                            elif self.graph[p][r] != 0:
                                weight_list[r]=weight_list[p]+self.graph[p][r] 
                            else:
                                pass


                elif p == 0:
                    for q in range(self.V): 
                        if weight_list[q] == math.inf:
                            if self.graph[p][q] != 0 :
                                weight_list[q] = self.graph[p][q]
                else:
                    pass


                z+=1
            
        for jkl in range(self.V):
            dict[str(jkl)]=weight_list[jkl]
        return dict
    
    def find(self, pa_node, m): 
        
        if pa_node[m] != m: 
            return self.find(pa_node, pa_node[m]) 
        elif pa_node[m] == m:
            return m
        else:
            pass 
  

    def union(self, pa_node, tem_v2, x, y): 
        
        xroot = self.find(pa_node, x) 
        yroot = self.find(pa_node, y) 
        
        if pa_node:
            
            if tem_v2[xroot] > tem_v2[yroot]: 
                pa_node[yroot] = xroot 
                
            elif tem_v2[xroot] < tem_v2[yroot]: 
                pa_node[xroot] = yroot 
                
            else : 
                pa_node[yroot] = xroot 
                tem_v2[xroot] += 1
        else:
            pass

    def Kruskal(self):
        final = dict();result =[] 
        m = 0;n = 0
        pa_node = [] ; tem_v2 = [] 
        self.graph =  sorted(self.graph,key=lambda item: item[2]) 
  
        for node in range(self.V): 
            pa_node.append(node) 
            tem_v2.append(0) 
      
        while n < self.V -1 : 

            u,v,w =  self.graph[m] 
            m = m + 1
            x = self.find(pa_node, u) ;y = self.find(pa_node ,v) 
  
            if x ==y:
                pass
            elif x != y: 
                n = n + 1     
                result.append([u,v,w]) 
                self.union(pa_node, tem_v2, x, y)
            else:
                pass
                
        for u, v, w in result:
            final[str(u)+'-'+str(v)]  = w
        return final
```


```python
g = Graph(4)
g.addEdge(0,1,10)
g.addEdge(0,2,6)
g.addEdge(0,3,5)
g.addEdge(1,3,15)
g.addEdge(2,3,4)
g.Kruskal()
```




    {'2-3': 4, '0-3': 5, '0-1': 10}



成功!


```python
g = Graph(9)
g.addEdge(0,1,4)
g.addEdge(0,7,8)
g.addEdge(1,7,11)
g.addEdge(1,2,8)
g.addEdge(7,8,7)
g.addEdge(7,6,1)
g.addEdge(2,8,2)
g.addEdge(8,6,6)
g.addEdge(2,3,7)
g.addEdge(2,5,4)
g.addEdge(6,5,2)
g.addEdge(3,5,14)
g.addEdge(3,4,9)
g.addEdge(5,4,10)
g.Kruskal()

```




    {'7-6': 1,
     '2-8': 2,
     '6-5': 2,
     '0-1': 4,
     '2-5': 4,
     '2-3': 7,
     '0-7': 8,
     '3-4': 9}



Final code:


```python
from collections import defaultdict 
import math

class add_g:
    def __init__(self,start,bourn,distance):
        if add_g:
            self.s=start
            self.b=bourn
            self.d=distance
        else:
            return 
         
class Graph(): 
    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = [] 
        self.graph_matrix = [[0 for column in range(vertices)]  
                    for row in range(vertices)] 
        
    def addEdge(self,u,v,w): 
        self.graph.append([u,v,w]) 

    def Dijkstra(self, s): 
        z=0
        dict={}
        tem=[]
        weight_list=[math.inf]*self.V
        for i in range(self.V):
            if i != s:
                pass
            else:
                weight_list[i]=0
            
                
                
        while len(tem) < self.V:  
            weight_list_v2 = sorted(weight_list)
            for p in range(self.V):
                if weight_list[p]==weight_list_v2[z] and p not in tem:
                    tem.append(p)
                    break
            if tem:        
                if p != 0:
                    for r in range(self.V):       
                        if weight_list[r] != math.inf:
                            if self.graph[p][r]!=0:
                                if weight_list[r] < weight_list[p]+self.graph[p][r]:
                                    pass
                                elif weight_list[r] > weight_list[p]+self.graph[p][r]:
                                    weight_list[r] = weight_list[p]+self.graph[p][r]
                                else:
                                    pass
                        else:
                            if self.graph[p][r] == 0 :
                                pass
                            elif self.graph[p][r] != 0:
                                weight_list[r]=weight_list[p]+self.graph[p][r] 
                            else:
                                pass


                elif p == 0:
                    for q in range(self.V): 
                        if weight_list[q] == math.inf:
                            if self.graph[p][q] != 0 :
                                weight_list[q] = self.graph[p][q]
                else:
                    pass


                z+=1
            
        for jkl in range(self.V):
            dict[str(jkl)]=weight_list[jkl]
        return dict
    
    def find(self, pa_node, m): 
        
        if pa_node[m] != m: 
            return self.find(pa_node, pa_node[m]) 
        elif pa_node[m] == m:
            return m
        else:
            pass 
  

    def union(self, pa_node, tem_v2, x, y): 
        
        xroot = self.find(pa_node, x) 
        yroot = self.find(pa_node, y) 
        
        if pa_node:
            
            if tem_v2[xroot] > tem_v2[yroot]: 
                pa_node[yroot] = xroot 
                
            elif tem_v2[xroot] < tem_v2[yroot]: 
                pa_node[xroot] = yroot 
                
            else : 
                pa_node[yroot] = xroot 
                tem_v2[xroot] += 1
        else:
            pass

    def Kruskal(self):
        final = dict();result =[] 
        m = 0;n = 0
        pa_node = [] ; tem_v2 = [] 
        self.graph =  sorted(self.graph,key=lambda item: item[2]) 
  
        for node in range(self.V): 
            pa_node.append(node) 
            tem_v2.append(0) 
      
        while n < self.V -1 : 

            u,v,w =  self.graph[m] 
            m = m + 1
            x = self.find(pa_node, u) ;y = self.find(pa_node ,v) 
  
            if x ==y:
                pass
            elif x != y: 
                n = n + 1     
                result.append([u,v,w]) 
                self.union(pa_node, tem_v2, x, y)
            else:
                pass
                
        for u, v, w in result:
            final[str(u)+'-'+str(v)]  = w
        return final
```

## 參考資料

### 參考網站:
>* https://www.youtube.com/watch?v=NLp9C7AvJhk
>* https://ithelp.ithome.com.tw/articles/10209593
>* https://github.com/qiwsir/algorithm/blob/master/dijkstra_algorithm.md
>* https://github.com/qiwsir/algorithm/blob/master/dijkstra_algorithm.py
>* https://github.com/luojilab/algorithm/blob/master/doc/Graph/Dijkstra/Dijkstra%E7%AE%97%E6%B3%95.md
>* https://www.programiz.com/dsa/dijkstra-algorithm
>* https://wangkuiwu.github.io/2013/04/14/dijkstra-cplus/
>* https://lance.moe/post-317.html
>* https://www.geeksforgeeks.org/kruskals-minimum-spanning-tree-algorithm-greedy-algo-2/
>* https://wiki.jsswsq.com/index.php?title=Kruskal%E7%AE%97%E6%B3%95&variant=zh-tw
>* https://www.cnblogs.com/skywang12345/p/3711500.html
>* https://www.w3schools.com/python/python_conditions.asp
>* https://blog.csdn.net/lanchunhui/article/details/51077079
>* https://blog.csdn.net/chenKFKevin/article/details/76549560
>* https://blog.csdn.net/sunchaoyiA/article/details/81177125
>* http://www.jeepxie.net/article/249013.html
>* https://www.cxyxiaowu.com/1195.html
>* https://zhuanlan.zhihu.com/p/34922624
>* https://blog.csdn.net/luomingjun12315/article/details/47700237
>* https://iq.opengenus.org/kruskal-minimum-spanning-tree-algorithm/
