"""
你和你的朋友，两个人一起玩 Nim 游戏：桌子上有一堆石头，每次你们轮流拿掉 1 - 3 块石头。 拿掉最后一块石头的人就是获胜者。你作为先手。

你们是聪明人，每一步都是最优解。 编写一个函数，来判断你是否可以在给定石头数量的情况下赢得游戏。

示例:

输入: 4
输出: false
解释: 如果堆中有 4 块石头，那么你永远不会赢得比赛；
     因为无论你拿走 1 块、2 块 还是 3 块石头，最后一块石头总是会被你的朋友拿走。

其实这道题给的例子是有一定启发作用的，也就是当只剩下4块给人选择的时候，就必然不是最后拿到的，因为无论你拿几块，
另外一个人都可以拿完，因此对于一个开始拿的人，只要这个值是4的倍数，他的对手都可以控制让他最后拿不到
"""


class Solution:
    def canWinNim(self, n):
        return (n % 4 != 0)


s = Solution()
res = s.canWinNim(4)
print(res)