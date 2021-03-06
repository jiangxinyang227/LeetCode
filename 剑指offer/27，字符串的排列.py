"""
输入一个字符串,按字典序打印出该字符串中字符的所有排列。
例如输入字符串abc,则打印出由字符a,b,c所能排列出来的所有字符串abc,acb,bac,bca,cab和cba

解题思路：递归求解子问题，用递归实现n层for循环来实现
"""


def my_permutation(s):
    str_set = []
    ret = []  # 最后的结果

    def permutation(string):
        for i in range(len(string)):
            str_tem = string[:i] + string[i+1:]
            str_set.append(string[i])
            if len(str_tem) > 0:
                permutation(str_tem)
            else:
                ret.append(''.join(str_set))
            str_set.pop()  # 在递归结束后，开始回转的时候需要去掉相应的字符

    permutation(s)
    ret = sorted(list(set(ret)))
    return ret


import copy


class Solution:
    def Permutation(self, ss):
        # write code here
        result = []
        path = []

        self.back_trace(result, path, ss, len(ss))
        return result

    def back_trace(self, result, path, ss, length):
        for i in range(len(ss)):
            if i > 0 and ss[i] == ss[i - 1]:
                continue
            path.append(ss[i])
            if len(path) == length:
                result.append("".join(path))
            else:
                self.back_trace(result, path, ss[:i] + ss[i + 1:], length)
            path.pop()


text = "abca"
res = my_permutation(text)
print(res)

s = Solution()
res1 = s.Permutation(text)
print(res1)