### 题意
Say you have an array for which the ith element is the price of a given stock on day i.  
给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).  
设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).  
注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
```python
Example 1:

Input: [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 3 天（股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
             Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
             随后，在第 4 天（股票价格 = 3）的时候买入，在第 5 天（股票价格 = 6）的时候卖出, 这笔交易所能获得利润 = 6-3 = 3 。

Example 2:

Input: [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
解释: 在第 1 天（股票价格 = 1）的时候买入，在第 5 天 （股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
             Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are engaging multiple transactions at the same time. You must sell before buying again.
             注意你不能在第 1 天和第 2 天接连购买股票，之后再将它们卖出。因为这样属于同时参与了多笔交易，你必须在再次购买前出售掉之前的股票。

Example 3:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。
```
### 思路
由于可以进行无限次的交易，那么只要是递增序列，就可以进行利润的累加。所以算法就是：遍历 prices，如果 prices[i+1] 比 prices[i] 大，那么 prices[i+1] – prices[i] 就可以计入最后的利润中。这样扫描一次 O(n) 就可以获得最大收益了。
```python
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        for i in range(0, len(prices)-1):
            if prices[i+1] > prices[i]:
                profit += prices[i+1] - prices[i]
        return profit
```
[LeetCode 122. Best Time to Buy and Sell Stock II](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/)
