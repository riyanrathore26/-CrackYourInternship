from typing import List


class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(arr)
        ple = [-1] * n
        nle = [n] * n
        stack = []
        for i in range(n):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            ple[i] = stack[-1] if stack else -1
            stack.append(i)
        stack = []
        for i in range(n-1, -1, -1):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            nle[i] = stack[-1] if stack else n
            stack.append(i)
        result = 0
        for i in range(n):
            left = i - ple[i]
            right = nle[i] - i
            result = (result + arr[i] * left * right) % MOD
        return result