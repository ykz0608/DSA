class Solution(object):    
    def merge_sort(self,data):
        if len(data)>1:
            mid = len(data)//2
            left = data[:mid]
            right = data[mid:]
            self.merge_sort(left)
            self.merge_sort(right)
            
            i = 0
            j = 0
            y = 0
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    data[y] = left[i]
                    i += 1
                else:
                    data[y] = right[j]
                    j+=1
                y += 1
            
            while i < len(left):
                data[y] = left[i]
                i += 1
                y += 1
            
            while j < len(right):
                data[y] = right[j]
                j += 1
                y += 1
            
        return data
 
List[int] = Solution().merge_sort(data)
