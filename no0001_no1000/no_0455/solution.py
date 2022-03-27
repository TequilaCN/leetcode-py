#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    solution.py
    ~~~~~~~~~~~~~~~~~~~~~~~
    
    link:
        https://leetcode.com/problems/assign-cookies/
    solution:
        贪心算法, 优先用小分量的食物满足食物分量要求小的小孩
    :author: Nacht
    :copyright: (c) 2022, Nacht Zhong
    :date created: 2022/3/27
    
"""
from typing import List


class Solution(object):
    @staticmethod
    def find_content_children(g: List[int], s: List[int]) -> int:
        g = sorted(g)
        s = sorted(s)
        if not len(g) or not len(s):
            return 0
        g_index = 0
        s_index = 0
        result = 0
        while g_index < len(g) and s_index < len(s):
            if s[s_index] >= g[g_index]:
                g_index += 1
                result +=1
            s_index += 1
        return result




if __name__ == '__main__':
    Solution().find_content_children([1,], [2,])


