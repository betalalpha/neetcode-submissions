class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            
            if nums[mid] == target:
                return mid
            
            # left sorted portion
            elif nums[mid] >= nums[l]:
                if nums[l] <= target <= nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
                    
            # right sorted portion
            else:
                if nums[mid] <= target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
                    
        return -1
        


        
        #while l < r:
        #    m = ( l + r) // 2
        #    if nums[m] == target:
        #        return m
        #    elif nums[m] > target:
        #        l = m + 1
        #    else: 
        #        r = m - 1
        #return -1
        
        #for i,n in enumerate(nums):
        #    if n == target:
        #        return i
        
        #return -1
            