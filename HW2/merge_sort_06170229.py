class Solution(object):
    def merge_sort(self,x):
        if len(x) < 2:
            return x
        result = []
        mid = int(len(x) / 2)
        y = merge_sort(x[:mid])
        z = merge_sort(x[mid:])
        self.merge_sort(y)
        self.merge_sort(z)
    
        i = 0
        j = 0
        while i < len(y) and j < len(z):
            if y[i] > z[j]:
                result.append(z[j])
                j += 1
            else:
                result.append(y[i])
                i += 1
        result += y[i:]
        result += z[j:]
        return result


ans=Solution().merge_sort([3,4,6,1,9,5,15,0])
ans
[0, 1, 3, 4, 5, 6, 9, 15]
