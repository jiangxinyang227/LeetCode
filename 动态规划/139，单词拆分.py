"""
给定一个非空字符串 s 和一个包含非空单词列表的字典 wordDict，判定 s 是否可以被空格拆分为一个或多个在字典中出现的单词。

说明：

拆分时可以重复使用字典中的单词。
你可以假设字典中没有重复的单词。
示例 1：

输入: s = "leetcode", wordDict = ["leet", "code"]
输出: true
解释: 返回 true 因为 "leetcode" 可以被拆分成 "leet code"。
示例 2：

输入: s = "applepenapple", wordDict = ["apple", "pen"]
输出: true
解释: 返回 true 因为 "applepenapple" 可以被拆分成 "apple pen apple"。
     注意你可以重复使用字典中的单词。
示例 3：

输入: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
输出: false

"""


class Solution:
    def wordBreak(self, s: str, wordDict) -> bool:
        """
        完全背包问题，即列表中的元素可以重复选择，是否能组合成s
        :param s:
        :param wordDict:
        :return:
        """
        n = len(s)
        dp = [False for i in range(n + 1)]
        dp[0] = True

        for i in range(n):
            if not dp[i]:
                continue
            for j in range(i + 1, n + 1):
                if s[i: j] in wordDict:
                    dp[j] = True
            print(dp)
        return dp[-1]


s = Solution()
res = s.wordBreak("applepenapple", ["apple", "pen"])
print(res)