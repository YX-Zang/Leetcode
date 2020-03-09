class Solution:
    def searchInsert(self, nums, target) -> int:
        insert_index = []
        for index in range(len(nums)):
            if target <= nums[index]:
                insert_index.append(index)
        return min(insert_index) if insert_index else len(nums)
