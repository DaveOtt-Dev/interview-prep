class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        counts = set()

        for val in nums:
            if val in counts:
                return True
            counts.add(val)

        return False