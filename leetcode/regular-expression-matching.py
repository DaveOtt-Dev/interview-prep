class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if "." not in p and "*" not in p:
            return s == p

        sIndex = 0

        for pIndex in range(len(p)):
            c = p[pIndex]

            if c == ".":
                if pIndex + 1 < len(p):
                    if p[pIndex + 1] == "*":
                        return True
                else:
                    return False

                sIndex += 1
                continue

            if c == "*":
                pattern = ""
                for i in range(pIndex-1, -1, -1):
                    if p[i] == "." or p[i] == "*":
                        break
                    pattern += p[i]
                
                pattern = pattern[::-1]
                if pattern == "":
                    continue

                step = len(pattern)
                while sIndex < len(s) - step:
                    if pattern != s[sIndex:step]:
                        break
                    sIndex += step
                continue
        
        return True

s = "mississippi"
p = "mis*is*ip*."

print(Solution().isMatch(s, p))