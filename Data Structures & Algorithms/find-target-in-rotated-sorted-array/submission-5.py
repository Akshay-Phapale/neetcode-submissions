class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l, r = 0, len(nums) - 1

        while l<=r:
            mid = (l+r) // 2

            if nums[mid] == target:
                return mid
            
            # check if we are in left sorted array

            if nums[mid] >= nums[l]:
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid -1 
            else: # right part 
                if target < nums[mid] or target > nums[r]:
                    r = mid -1
                else:
                    l = mid + 1

        return -1   
        