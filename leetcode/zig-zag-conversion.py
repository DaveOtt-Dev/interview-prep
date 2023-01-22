class Solution:
    def convert(self, s: str, numRows: int) -> str:
        x = [None] * len(s)
        zigZagList = [] * numRows
        for _ in range(numRows):
            zigZagList.append(x[:])

        i = 0
        while s != "":
            for j in range(numRows):
                if s == "":
                    break

                zigZagList[j][i] = s[0]
                s = s[1:]
            
            i += 1

            for j in range(numRows - 2, 0, -1):
                if s == "":
                    break

                zigZagList[j][i] = s[0]
                s = s[1:]
                i += 1
        
        return self.toString(zigZagList)


    def toString(self, zigZagList):
        output = ""

        for zzl in zigZagList:
            for c in zzl:
                if c is None:
                    continue
                output += c
        
        return output

if __name__ == "__main__":
    s = "PAYPALISHIRING"
    print(Solution().convert(s, 3))