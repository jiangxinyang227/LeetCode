"""
给定一个整数 n，返回 n! 结果尾数中零的数量。

示例 1:

输入: 3
输出: 0
解释: 3! = 6, 尾数中没有零。
示例 2:

输入: 5
输出: 1
解释: 5! = 120, 尾数中有 1 个零.
说明: 你算法的时间复杂度应为 O(log n) 。

计算0的数量只要在相乘的过程中有一个10就会有一个0。而10 = 2 × 5
在一个连乘的过程中通过将可以拆解成2,5的值拆分后得到的2的数量要大于5，因此只要统计出现的5的个数，而对于5，每隔5会出现一个，而对于25
每个25会出现2个，对于125，每个125会出现3个，依次类推

"""


class Solution:
    def trailingZeroes(self, n):
        count = 0
        while n >= 5:
            count += n // 5
            n = n // 5
        return count


s = Solution()
res = s.trailingZeroes(25)
print(res)
