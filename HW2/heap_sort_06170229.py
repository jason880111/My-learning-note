class Solution(object):
    def heapsort(self,nums):
        n = len(nums)
        for i in range(n-1, -1, -1):
            self.heapify(nums, n, i)

        for i in range(n - 1, 0, -1):
            nums[i], nums[0] = nums[0], nums[i]
            self.heapify(nums, i, 0)
            
    def heapify(self,nums, heap_size, root_index):

        minnode = root_index
        left_child = (2 * root_index) + 1
        right_child = (2 * root_index) + 2


        if left_child < heap_size and nums[left_child] < nums[minnode]:
            minnode = left_child

        if right_child < heap_size and nums[right_child] < nums[minnode]:
            minnode = right_child

        if minnode != root_index:
            nums[root_index], nums[minnode] = nums[minnode], nums[root_index]
   
            self.heapify(nums, heap_size, minnode)
            
            
a=[8,3,5,1,0,-3,4]
Solution().heapsort(a)
print(a)
[8, 5, 4, 3, 1, 0, -3]
