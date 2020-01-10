def modulus(n):
    if type(n)==int:
        return n % 2
    else:
        return -1
        
註: 查看n是否為整數，是的話return n除以2的餘數，不是就return -1
