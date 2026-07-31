class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n=len(cardPoints)
        total=sum(cardPoints)
        w_size=n-k
        
        window_sum=sum(cardPoints[:w_size])
        min_sum=window_sum
        for i in range(w_size,n):
            window_sum+=cardPoints[i]-cardPoints[i-w_size]
            min_sum=min(min_sum,window_sum)
        return total-min_sum