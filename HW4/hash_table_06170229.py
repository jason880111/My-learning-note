class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyHashSet:
    def __init__(self, capacity=5):
        self.capacity = capacity
        self.data = [None] * capacity
    
    def MD5(self,key):
        from Crypto.Hash import MD5
        h = MD5.new()
        h.update(key.encode("utf-8"))
        return int(h.hexdigest(), 16)

    def add(self, key):
        key = self.MD5(key)
        num = key % self.capacity
        
        if self.data[num] == None:
            self.data[num] = ListNode(key)
        else:
            head = self.data[num]
            while head.next:
                head = head.next
            if head.val != key:
                head.next = ListNode(key)
        
        
    def remove(self, key):
        key = self.MD5(key)
        num = key % self.capacity
        
        if self.data[num] == None:
            return
    
        if self.data[num].val == key:
            self.data[num] = self.data[num].next
            return
        
        head = self.data[num]
        while head.next.val != key:
            head = head.next
        
        
    def contains(self, key):
        key = self.MD5(key)
        num = key % self.capacity
        
        head = self.data[num]
        while head:
            if head.val == key:
                return True
            head = head.next
        return False
