class Solution:
    def balancedStringSplit(self, s: str) -> int:
        curr = s
        candidates = []

        while len(curr) > 0:
            candidate = self.balancedStringSplitHelper(curr)
            if candidate is None:
                break
            
            candidates.append(candidate)
            curr = curr[len(candidate):]
        
        return len(candidates)

    def balancedStringSplitHelper(self, s: str) -> str:
        for i in range(1, len(s)+1):
            curr = s[:i]

            rCount = curr.count('R')
            lCount = curr.count('L')

            if rCount == lCount:
                return curr

        return None
    
s = Solution()
answer = s.balancedStringSplit('RLRRLLRLRL')
print(answer)