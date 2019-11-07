class solution(object):
    def msort(self,x):
        if len(x) < 2:
            return x
        result = []
        mid = int(len(x) / 2)
        y = msort(x[:mid])
        z = msort(x[mid:])
        self.msort(y)
        self.msort(z)
    
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


ans=solution().msort([3,4,6,1,9,5,15,0])
ans
[0, 1, 3, 4, 5, 6, 9, 15]
