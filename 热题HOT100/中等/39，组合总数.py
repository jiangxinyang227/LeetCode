"""
给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

candidates 中的数字可以无限制重复被选取。

说明：

所有数字（包括 target）都是正整数。
解集不能包含重复的组合。 
示例 1:

输入: candidates = [2,3,6,7], target = 7,
所求解集为:
[
  [7],
  [2,2,3]
]
示例 2:

输入: candidates = [2,3,5], target = 8,
所求解集为:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]

"""

import copy


class Solution:
    def combinationSum(self, candidates, target: int):
        result = []
        path = []
        self.back_track(result, candidates, path, target)
        return result

    def back_track(self, result, candidates, path, target):
        for i in range(len(candidates)):
            if sum(path) + candidates[i] > target:
                continue
            path.append(candidates[i])
            if sum(path) < target:
                self.back_track(result, candidates[i:], path, target)
            elif sum(path) == target:
                result.append(copy.deepcopy(path))
            path.pop()


s = Solution()
res = s.combinationSum([2, 3, 6, 7], 7)
print(res)