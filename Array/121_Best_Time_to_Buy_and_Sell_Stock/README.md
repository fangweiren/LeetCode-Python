### 题意
Say you have an array for which the `i**th` element is the price of a given stock on day i.  
给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.  
如果你最多只允许完成一笔交易（即买入和卖出一支股票），设计一个算法来计算你所能获取的最大利润。

Note that you cannot sell a stock before you buy one.  
注意你不能在买入股票前卖出股票。
```python
Example 1:

Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
             Not 7-1 = 6, as selling price needs to be larger than buying price.
             注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格。

Example 2:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。
```
### 思路
动态规划。在遍历的过程中，用一个变量保存目前为止最小的数，用当前的数与目前最小的数相减，判断这个差与此前得到的最大收益的大小，取较大值更新最大收益。
```python
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0:
            return 0
        
        minPrice = prices[0]
        maxProfit = 0
        
        for p in prices:
            if p < minPrice:
                minPrice = p
            if p - minPrice > maxProfit:
                maxProfit = p - minPrice
        return maxProfit
```
[LeetCode 121. Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/)
