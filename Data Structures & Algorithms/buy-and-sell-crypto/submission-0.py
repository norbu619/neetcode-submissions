class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1

        maxi = 0

        while right < len(prices):
            if prices[right] - prices[left] > maxi:
                maxi = prices[right] - prices[left]
                right +=1
            elif prices[right] < prices[left]:
                left = right
                right +=1
            else:
                right += 1
        return maxi