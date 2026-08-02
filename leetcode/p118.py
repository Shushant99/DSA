class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        output=[]
        for i in range(numRows):
            new_row = [1]* (i+1)

            for j in range(1,i):
                new_row[j]=output[i-1][j-1]+output[i-1][j]
            output.append(new_row)
        return output