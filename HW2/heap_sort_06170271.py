class Solution(object):
    #import random
    #import pandas 
    #import numpy as np

    #x = np.random.randint(-100,100,10)
    #arr = x.tolist()

    def MinH(self,data,i):
        n = len(data)-1
        left = 2 * i + 1
        right = 2 * i + 2
        s = i 
        if left <= n and data[left] < data[i]:
            s = left
        if right <= n and data[right] < data[s] :
            s = right
        if s != i:
            data[i],data[s] = data[s],data[i]
            self.MinH(data,s)
            
    def heap_sort(self,data):
        data = data.copy()
        for i in reversed(range(len(data)//2)):
            self.MinH(data,i)
        sort_d = []
        for _ in range(len(data)):
            data[0],data[-1] = data[-1],data[0]
            sort_d.append(data.pop())
            self.MinH(data,0)
        return sort_d
    
    #def main(data):
    #HeapS(data)
    #print(HeapS(data))
    # result
    
List[int] = Solution().merge_sort(data)
