class Solution(object):
    def merge_sort(self,x):
        if len(x) < 2:
            return x
        result = []
        mid = int(len(x) / 2)
        left = merge_sort(x[:mid])
        right = merge_sort(x[mid:])
        self.merge_sort(left)
        self.merge_sort(right)
    
        i = 0
        j = 0
        while i < len(left) and j < len(right):
            if left[i] > right[j]:
                result.append(right[j])
                j += 1
            else:
                result.append(left[i])
                i += 1
        result += left[i:]
        result += right[j:]
        return result
    
    
ans=Solution().merge_sort([3,4,6,1,9,5,15,0])
ans
