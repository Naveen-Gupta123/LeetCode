#!/usr/bin/env python3
"""LeetCode 1. Two Sum

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
"""

from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    seen = {}
    for i, value in enumerate(nums):
        complement = target - value
        if complement in seen:
            return [seen[complement], i]
        seen[value] = i
    raise ValueError("No two sum solution")


if __name__ == "__main__":
    example_nums = [2, 7, 11, 15]
    example_target = 9
    result = two_sum(example_nums, example_target)
    print(result)
