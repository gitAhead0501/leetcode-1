"""This file is a minimal colleciton of solutions to leetcode problems in 
Python3. No algorithm or reasoning is provided for the sake of saving spaces. 
For more details, the readers are suggested to explore on their own effort.
"""

from functools import lru_cache, reduce
from heapq import heappush, heappop, heapify
from itertools import groupby, zip_longest
from math import inf, sqrt, ceil
from operator import gt, lt, or_, xor

class Solution:

	"""1. Two Sum (Easy)
	Given an array of integers, return indices of the two numbers such that 
	they add up to a specific target. You may assume that each input would have 
	exactly one solution, and you may not use the same element twice.

	Example:
	Given nums = [2, 7, 11, 15], target = 9,
	Because nums[0] + nums[1] = 2 + 7 = 9,
	return [0, 1]."""

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = dict()
        for i, x in enumerate(nums): 
            if target - x in seen: return [seen[target-x], i]
            seen[x] = i


    """2. Add Two Numbers (Medium)
	You are given two non-empty linked lists representing two non-negative 
	integers. The digits are stored in reverse order and each of their nodes 
	contain a single digit. Add the two numbers and return it as a linked list. 
	You may assume the two numbers do not contain any leading zero, except the 
	number 0 itself.

	Example:
	Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
	Output: 7 -> 0 -> 8
	Explanation: 342 + 465 = 807."""

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = node = ListNode()
        carry = 0
        while l1 or l2 or carry: 
            if l1: 
                carry += l1.val
                l1 = l1.next
            if l2: 
                carry += l2.val 
                l2 = l2.next 
            carry, x = divmod(carry, 10)
            node.next = node = ListNode(x)
        return head.next 


    """3. Longest Substring Without Repeating Characters (Medium)
	Given a string, find the length of the longest substring without repeating 
	characters.

	Example 1:
	Input: "abcabcbb"
	Output: 3 
	Explanation: The answer is "abc", with the length of 3. 

	Example 2:
	Input: "bbbbb"
	Output: 1
	Explanation: The answer is "b", with the length of 1.

	Example 3:
	Input: "pwwkew"
	Output: 3
	Explanation: The answer is "wke", with the length of 3. 
	Note that the answer must be a substring, "pwke" is a subsequence and not a 
	substring."""

    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = dict()
        ans = j = 0
        for i, x in enumerate(s): 
            if x in seen and seen[x] >= j: j = seen[x] + 1
            ans = max(ans, i-j+1)
            seen[x] = i
        return ans 


    """4. Median of Two Sorted Arrays (Hard)
	There are two sorted arrays nums1 and nums2 of size m and n respectively. 
	Find the median of the two sorted arrays. The overall run time complexity 
	should be O(log (m+n)). You may assume nums1 and nums2 cannot be both empty.

	Example 1:
	nums1 = [1, 3], nums2 = [2]
	The median is 2.0

	Example 2:
	nums1 = [1, 2], nums2 = [3, 4]
	The median is (2 + 3)/2 = 2.5"""

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2): nums1, nums2 = nums2, nums1
        m, n = len(nums1), len(nums2)
        lo, hi = 0, m
        
        while lo <= hi: 
            mid = (lo + hi)//2
            k = (m+n)//2 - mid 
            if mid > 0 and nums1[mid-1] > nums2[k]: hi = mid
            elif mid < m and nums1[mid] < nums2[k-1]: lo = mid+1
            else: 
                if mid == m: right = nums2[k]
                elif k == n: right = nums1[mid]
                else: right = min(nums1[mid], nums2[k])
                
                if (m+n)%2: return right
                
                if mid == 0: left = nums2[k-1]
                elif k == 0: left = nums1[mid-1]
                else: left = max(nums1[mid-1], nums2[k-1])
                
                return (left + right)/2


    """5. Longest Palindromic Substring (Medium)
	Given a string s, find the longest palindromic substring in s. You may 
	assume that the maximum length of s is 1000.

	Example 1:
	Input: "babad"
	Output: "bab"
	Note: "aba" is also a valid answer.

	Example 2:
	Input: "cbbd"
	Output: "bb"""

    def longestPalindrome(self, s: str) -> str:
        ans = ""
        for i in range(2*len(s)-1): 
            lo = i//2
            hi = lo + i%2
            while 0 <= lo and hi < len(s) and s[lo] == s[hi]: lo, hi = lo-1, hi+1
            ans = max(ans, s[lo+1:hi], key=len)
        return ans 


	"""6. ZigZag Conversion (Medium)
	The string "PAYPALISHIRING" is written in a zigzag pattern on a given 
	number of rows like this: (you may want to display this pattern in a fixed 
	font for better legibility)

	P   A   H   N
	A P L S I I G
	Y   I   R
	And then read line by line: "PAHNAPLSIIGYIR"

	Write the code that will take a string and make this conversion given a 
	number of rows:

	string convert(string s, int numRows);

	Example 1:
	Input: s = "PAYPALISHIRING", numRows = 3
	Output: "PAHNAPLSIIGYIR"

	Example 2:
	Input: s = "PAYPALISHIRING", numRows = 4
	Output: "PINALSIGYAHRPI"

	Explanation:

	P     I    N
	A   L S  I G
	Y A   H R
	P     I"""

    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1: return s #edge case 
        ans = [[] for _ in range(numRows)]
        i, di = 0, 1
        for c in s: 
            ans[i].append(c)
            i += di
            if i == 0 or i == numRows-1: di *= -1
        return "".join("".join(x) for x in ans)


	"""7. Reverse Integer (Easy)
	Given a 32-bit signed integer, reverse digits of an integer.

	Example 1:
	Input: 123
	Output: 321

	Example 2:
	Input: -123
	Output: -321

	Example 3:
	Input: 120
	Output: 21

	Note:
	Assume we are dealing with an environment which could only store integers 
	within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose 
	of this problem, assume that your function returns 0 when the reversed 
	integer overflows."""

    def reverse(self, x: int) -> int:
        x = ((x>0) - (x<0)) * int(str(abs(x))[::-1])
        return x if x.bit_length() < 32 else 0


    """8. String to Integer (atoi) (Medium)
	Implement atoi which converts a string to an integer. The function first 
	discards as many whitespace characters as necessary until the first non-
	whitespace character is found. Then, starting from this character, takes 
	an optional initial plus or minus sign followed by as many numerical digits 
	as possible, and interprets them as a numerical value. The string can 
	contain additional characters after those that form the integral number, 
	which are ignored and have no effect on the behavior of this function. If 
	the first sequence of non-whitespace characters in str is not a valid 
	integral number, or if no such sequence exists because either str is empty 
	or it contains only whitespace characters, no conversion is performed. If 
	no valid conversion could be performed, a zero value is returned.

	Note:

	Only the space character ' ' is considered as whitespace character.
	Assume we are dealing with an environment which could only store integers 
	within the 32-bit signed integer range: [−2^31,  2^31 − 1]. If the numerical 
	value is out of the range of representable values, INT_MAX (231 − 1) or 
	INT_MIN (−231) is returned.

	Example 1:
	Input: "42"
	Output: 42

	Example 2:
	Input: "   -42"
	Output: -42
	Explanation: The first non-whitespace character is '-', which is the minus sign.
	             Then take as many numerical digits as possible, which gets 42.

	Example 3:
	Input: "4193 with words"
	Output: 4193
	Explanation: Conversion stops at digit '3' as the next character is not a numerical digit.

	Example 4:
	Input: "words and 987"
	Output: 0
	Explanation: The first non-whitespace character is 'w', which is not a numerical 
	             digit or a +/- sign. Therefore no valid conversion could be performed.

	Example 5:
	Input: "-91283472332"
	Output: -2147483648
	Explanation: The number "-91283472332" is out of the range of a 32-bit signed integer.
	Thefore INT_MIN (−231) is returned."""

    def myAtoi(self, str: str) -> int:
        str = "".join(re.findall('^[\+|\-]?\d+', str.lstrip()))
        return 0 if not str else min(2**31-1, max(-2**31, int(str)))


	"""9. Palindrome Number (Easy)
	Determine whether an integer is a palindrome. An integer is a palindrome 
	when it reads the same backward as forward.

	Example 1:
	Input: 121
	Output: true

	Example 2:
	Input: -121
	Output: false
	Explanation: From left to right, it reads -121. From right to left, it 
	becomes 121-. Therefore it is not a palindrome.

	Example 3:
	Input: 10
	Output: false
	Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

	Follow up: Coud you solve it without converting the integer to a string?"""

    def isPalindrome(self, x: int) -> bool:
        if x < 0 or x % 10 == 0 and x != 0: return False 
        y = 0
        while x > y: 
            y = 10*y + x % 10
            x //= 10
        return x == y or x == y//10 


    """10. Regular Expression Matching (Hard)
	Given an input string (s) and a pattern (p), implement regular expression 
	matching with support for '.' and '*'.

	'.' Matches any single character.
	'*' Matches zero or more of the preceding element.
	The matching should cover the entire input string (not partial).

	Note:
	s could be empty and contains only lowercase letters a-z.
	p could be empty and contains only lowercase letters a-z, and characters like . or *.

	Example 1:
	Input:
	s = "aa"
	p = "a"
	Output: false

	Example 2:
	Input:
	s = "aa"
	p = "a*"
	Output: true

	Example 3:
	Input:
	s = "ab"
	p = ".*"
	Output: true

	Example 4:
	Input:
	s = "aab"
	p = "c*a*b"
	Output: true

	Example 5:
	Input:
	s = "mississippi"
	p = "mis*is*p*."
	Output: false"""

    def isMatch(self, s: str, p: str) -> bool:
        
        @lru_cache(None)
        def fn(i, j): 
            """Return True if s[i:] matches p[j:]"""
            if j == len(p): return i == len(s)
            match = i < len(s) and (s[i] == p[j] or p[j] == ".")
            if j+1 < len(p) and p[j+1] == "*": 
                return fn(i, j+2) or match and fn(i+1, j)
            else: 
                return match and fn(i+1, j+1)
            
        return fn(0, 0)



    """11. Container With Most Water (Medium)
	Given n non-negative integers a1, a2, ..., an , where each represents a 
	point at coordinate (i, ai). n vertical lines are drawn such that the two 
	endpoints of line i is at (i, ai) and (i, 0). Find two lines, which 
	together with x-axis forms a container, such that the container contains 
	the most water.

	Note: You may not slant the container and n is at least 2.

	Example:
	Input: [1,8,6,2,5,4,8,3,7]
	Output: 49"""

    def maxArea(self, height: List[int]) -> int:
        ans = 0
        lo, hi = 0, len(height)-1
        while lo < hi: 
            ans = max(ans, (hi-lo)*min(height[lo], height[hi]))
            if height[lo] < height[hi]: lo += 1
            else: hi -= 1
        return ans 



    """12. Integer to Roman (Medium)
	Roman numerals are represented by seven different symbols: I, V, X, L, C, D 
	and M.

	Symbol       Value
	I             1
	V             5
	X             10
	L             50
	C             100
	D             500
	M             1000
	For example, two is written as II in Roman numeral, just two one's added 
	together. Twelve is written as, XII, which is simply X + II. The number 
	twenty seven is written as XXVII, which is XX + V + II.

	Roman numerals are usually written largest to smallest from left to right. 
	However, the numeral for four is not IIII. Instead, the number four is 
	written as IV. Because the one is before the five we subtract it making 
	four. The same principle applies to the number nine, which is written as 
	IX. There are six instances where subtraction is used:

	I can be placed before V (5) and X (10) to make 4 and 9. 
	X can be placed before L (50) and C (100) to make 40 and 90. 
	C can be placed before D (500) and M (1000) to make 400 and 900.
	Given an integer, convert it to a roman numeral. Input is guaranteed to be 
	within the range from 1 to 3999.

	Example 1:
	Input: 3
	Output: "III"

	Example 2:
	Input: 4
	Output: "IV"

	Example 3:
	Input: 9
	Output: "IX"

	Example 4:
	Input: 58
	Output: "LVIII"
	Explanation: L = 50, V = 5, III = 3.

	Example 5:
	Input: 1994
	Output: "MCMXCIV"
	Explanation: M = 1000, CM = 900, XC = 90 and IV = 4."""

    def intToRoman(self, num: int) -> str:
        mp = {1000:"M", 900:"CM", 500:"D", 400:"CD", 100:"C", 90:"XC", 50:"L", 40:"XL", 10:"X", 9:"IX", 5:"V", 4:"IV", 1:"I"}
        ans = []
        for k, v in mp.items(): 
            ans.append(num//k * v)
            num %= k
        return "".join(ans)

	"""13. Roman to Integer (Easy)
	Roman numerals are represented by seven different symbols: I, V, X, L, C, 
	D and M.

	Symbol       Value
	I             1
	V             5
	X             10
	L             50
	C             100
	D             500
	M             1000
	For example, two is written as II in Roman numeral, just two one's added 
	together. Twelve is written as, XII, which is simply X + II. The number 
	twenty seven is written as XXVII, which is XX + V + II.

	Roman numerals are usually written largest to smallest from left to right. 
	However, the numeral for four is not IIII. Instead, the number four is 
	written as IV. Because the one is before the five we subtract it making 
	four. The same principle applies to the number nine, which is written as 
	IX. There are six instances where subtraction is used:

	I can be placed before V (5) and X (10) to make 4 and 9. 
	X can be placed before L (50) and C (100) to make 40 and 90. 
	C can be placed before D (500) and M (1000) to make 400 and 900.
	Given a roman numeral, convert it to an integer. Input is guaranteed to be 
	within the range from 1 to 3999.

	Example 1:
	Input: "III"
	Output: 3

	Example 2:
	Input: "IV"
	Output: 4

	Example 3:
	Input: "IX"
	Output: 9

	Example 4:
	Input: "LVIII"
	Output: 58
	Explanation: L = 50, V= 5, III = 3.

	Example 5:
	Input: "MCMXCIV"
	Output: 1994
	Explanation: M = 1000, CM = 900, XC = 90 and IV = 4."""

    def romanToInt(self, s: str) -> int:
        mp = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        ans = 0
        for i in range(len(s)):
            if i+1 < len(s) and mp[s[i]] < mp[s[i+1]]: ans -= mp[s[i]]
            else: ans += mp[s[i]]
        return ans


    """14. Longest Common Prefix (Easy)
	Write a function to find the longest common prefix string amongst an array 
	of strings. If there is no common prefix, return an empty string "".

	Example 1:
	Input: ["flower","flow","flight"]
	Output: "fl"

	Example 2:
	Input: ["dog","racecar","car"]
	Output: ""
	Explanation: There is no common prefix among the input strings."""

    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs: return ""
        for i, c in enumerate(zip(*strs)): 
            if len(set(c)) > 1: return strs[0][:i]
        return min(strs)


    """15. 3Sum (Medium)
	Given an array nums of n integers, are there elements a, b, c in nums such 
	that a + b + c = 0? Find all unique triplets in the array which gives the 
	sum of zero.

	Note: The solution set must not contain duplicate triplets.

	Example:
	Given array nums = [-1, 0, 1, 2, -1, -4],
	A solution set is:
	[
	  [-1, 0, 1],
	  [-1, -1, 2]
	]"""

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        for i in range(len(nums)): 
            if nums[i] > 0: break
            if i and nums[i-1] == nums[i]: continue #remove duplicates
            lo, hi = i+1, len(nums)-1
            while lo < hi: 
                x = nums[lo] + nums[hi] + nums[i]
                if x > 0: hi -= 1
                elif x < 0: lo += 1
                else: 
                    ans.append([nums[i], nums[lo], nums[hi]])
                    lo += 1
                    while lo < hi and nums[lo-1] == nums[lo]: lo += 1
        return ans 


    """16. 3Sum Closest (Medium)
	Given an array nums of n integers and an integer target, find three 
	integers in nums such that the sum is closest to target. Return the sum of 
	the three integers. You may assume that each input would have exactly one 
	solution.

	Example 1:
	Input: nums = [-1,2,1,-4], target = 1
	Output: 2
	Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

	Constraints:
	3 <= nums.length <= 10^3
	-10^3 <= nums[i] <= 10^3
	-10^4 <= target <= 10^4"""

    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans = float("inf")
        for i in range(len(nums)): 
            lo, hi = i+1, len(nums)-1
            while lo < hi: 
                val = nums[i] + nums[lo] + nums[hi] 
                if val == target: return val
                elif val > target: hi -= 1
                else: lo += 1
                ans = min(ans, val, key=lambda x: abs(x-target))
        return ans 


    """17. Letter Combinations of a Phone Number (Medium)
	Given a string containing digits from 2-9 inclusive, return all possible 
	letter combinations that the number could represent.

	A mapping of digit to letters (just like on the telephone buttons) is given 
	below. Note that 1 does not map to any letters.

	Example:
	Input: "23"
	Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

	Note: Although the above answer is in lexicographical order, your answer 
	could be in any order you want."""

    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        phone = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        return reduce(lambda x, y: [xx+yy for xx in x for yy in phone[y]], digits, [""])


    """18. 4Sum (Medium)
	Given an array nums of n integers and an integer target, are there elements 
	a, b, c, and d in nums such that a + b + c + d = target? Find all unique 
	quadruplets in the array which gives the sum of target.

	Note: The solution set must not contain duplicate quadruplets.

	Example:
	Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.

	A solution set is:
	[
	  [-1,  0, 0, 1],
	  [-2, -1, 1, 2],
	  [-2,  0, 0, 2]
	]"""

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ans = []
        for i in range(len(nums)):
            if i and nums[i-1] == nums[i]: continue
            for j in range(i+1, len(nums)):
                if j > i+1 and nums[j-1] == nums[j]: continue 
                lo, hi = j+1, len(nums)-1
                while lo < hi: 
                    val = nums[i] + nums[j] + nums[lo] + nums[hi]
                    if val < target: lo += 1
                    elif val > target: hi -= 1
                    else: 
                        ans.append([nums[i], nums[j], nums[lo], nums[hi]])
                        lo += 1
                        while lo < hi and nums[lo-1] == nums[lo]: lo += 1
        return ans


    """19. Remove Nth Node From End of List (Medium)
	Given a linked list, remove the n-th node from the end of list and return 
	its head.

	Example:
	Given linked list: 1->2->3->4->5, and n = 2.
	After removing the second node from the end, the linked list becomes 1->2->3->5.

	Note: Given n will always be valid.
	Follow up: Could you do this in one pass?"""

    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(next=head)
        fast = slow = dummy
        i = 0
        while fast:
            fast = fast.next 
            if (i:=i+1) > n+1: slow = slow.next
        slow.next = slow.next.next
        return dummy.next 


    """20. Valid Parentheses (Easy)
	Given a string containing just the characters '(', ')', '{', '}', '[' and 
	']', determine if the input string is valid.

	An input string is valid if:
	* Open brackets must be closed by the same type of brackets.
	* Open brackets must be closed in the correct order.
	Note: an empty string is also considered valid.

	Example 1:
	Input: "()"
	Output: true
	
	Example 2:
	Input: "()[]{}"
	Output: true

	Example 3:
	Input: "(]"
	Output: false

	Example 4:
	Input: "([)]"
	Output: false

	Example 5:
	Input: "{[]}"
	Output: true"""

    def isValid(self, s: str) -> bool:
        match, stack = {"(":")", "[":"]", "{":"}"}, []
        for x in s:
            if x in match: stack.append(x)
            elif not stack or match[stack.pop()] != x: return False 
        return not stack 


    """21. Merge Two Sorted Lists (Easy)
	Merge two sorted linked lists and return it as a new list. The new list 
	should be made by splicing together the nodes of the first two lists.

	Example:

	Input: 1->2->4, 1->3->4
	Output: 1->1->2->3->4->4"""
    
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = node = ListNode()
        while l1 and l2: 
            if l1.val > l2.val: l1, l2 = l2, l1
            node.next = l1
            l1, node = l1.next, node.next
        node.next = l1 or l2
        return dummy.next 


    """22. Generate Parentheses (Medium)
	Given n pairs of parentheses, write a function to generate all 
	combinations of well-formed parentheses.

	For example, given n = 3, a solution set is:

	[
	  "((()))",
	  "(()())",
	  "(())()",
	  "()(())",
	  "()()()"
	]"""

    def generateParenthesis(self, n: int) -> List[str]:
        
        def fn(s, op, cl):
            """Backtracking to collect parentheses"""
            if cl == n: return ans.append(s)
            if op <  n: fn(s+"(", op+1, cl)
            if cl < op: fn(s+")", op, cl+1)
                
        ans = []
        fn("", 0, 0)
        return ans 


    """23. Merge k Sorted Lists (Hard)
	Merge k sorted linked lists and return it as one sorted list. Analyze and 
	describe its complexity.

	Example:
	Input:
	[
	  1->4->5,
	  1->3->4,
	  2->6
	]
	Output: 1->1->2->3->4->4->5->6"""
    
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        pq = [(x.val, i, x) for i, x in enumerate(lists) if x]
        heapify(pq)
        dummy = node = ListNode()
        
        while pq: 
            _, i, x = heappop(pq)
            node.next = node = x
            if x.next: heappush(pq, (x.next.val, i, x.next))
        return dummy.next 


    """24. Swap Nodes in Pairs (Medium)
	Given a linked list, swap every two adjacent nodes and return its head.

	You may not modify the values in the list's nodes, only nodes itself may be 
	changed.

	Example:
	Given 1->2->3->4, you should return the list as 2->1->4->3."""

    def swapPairs(self, head: ListNode) -> ListNode:
        node = dummy = ListNode(0, head)
        while node.next and node.next.next: 
            node.next.next.next, node.next.next, node.next = node.next, node.next.next.next, node.next.next
            node = node.next.next 
        return dummy.next


    """25. Reverse Nodes in k-Group (Hard)
	Given a linked list, reverse the nodes of a linked list k at a time and 
	return its modified list. k is a positive integer and is less than or 
	equal to the length of the linked list. If the number of nodes is not a 
	multiple of k then left-out nodes in the end should remain as it is.

	Example:
	Given this linked list: 1->2->3->4->5
	For k = 2, you should return: 2->1->4->3->5
	For k = 3, you should return: 3->2->1->4->5

	Note: Only constant extra memory is allowed.
	You may not alter the values in the list's nodes, only nodes itself may be changed."""
    
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        node, i = head, 0
        while node:
            if (i:=i+1) == k: break
            node = node.next 
        if i < k: return head 
        
        prev, node = None, head 
        for _ in range(k): node.next, node, prev = prev, node.next, node
        head.next = self.reverseKGroup(node, k)
        return prev 


    """26. Remove Duplicates from Sorted Array (Easy)
	Given a sorted array nums, remove the duplicates in-place such that each 
	element appear only once and return the new length. Do not allocate extra 
	space for another array, you must do this by modifying the input array in-
	place with O(1) extra memory.

	Example 1:
	Given nums = [1,1,2], your function should return length = 2, with the 
	first two elements of nums being 1 and 2 respectively. It doesn't matter 
	what you leave beyond the returned length.

	Example 2:
	Given nums = [0,0,1,1,1,2,2,3,3,4], your function should return length = 5, 
	with the first five elements of nums being modified to 0, 1, 2, 3, and 4 
	respectively. It doesn't matter what values are set beyond the returned 
	length.
	
	Clarification: Confused why the returned value is an integer but your 
	answer is an array?

	Note that the input array is passed in by reference, which means 
	modification to the input array will be known to the caller as well.

	Internally you can think of this:
	// nums is passed in by reference. (i.e., without making a copy)
	int len = removeDuplicates(nums);
	// any modification to nums in your function would be known by the caller.
	// using the length returned by your function, it prints the first len 
	elements.
	for (int i = 0; i < len; i++) {
	    print(nums[i]);
	}"""

    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        for num in nums:
            if i < 1 or nums[i-1] < num: 
                nums[i] = num
                i += 1
        return i


    """27. Remove Element (Easy)
	Given an array nums and a value val, remove all instances of that value in-
	place and return the new length. Do not allocate extra space for another 
	array, you must do this by modifying the input array in-place with O(1) 
	extra memory. The order of elements can be changed. It doesn't matter what 
	you leave beyond the new length.

	Example 1:
	Given nums = [3,2,2,3], val = 3, your function should return length = 2, 
	with the first two elements of nums being 2. It doesn't matter what you 
	leave beyond the returned length.
	
	Example 2:
	Given nums = [0,1,2,2,3,0,4,2], val = 2, your function should return 
	length = 5, with the first five elements of nums containing 0, 1, 3, 0, 
	and 4. Note that the order of those five elements can be arbitrary. It 
	doesn't matter what values are set beyond the returned length.
	
	Clarification:

	Confused why the returned value is an integer but your answer is an array?

	Note that the input array is passed in by reference, which means 
	modification to the input array will be known to the caller as well.

	Internally you can think of this:
	// nums is passed in by reference. (i.e., without making a copy)
	int len = removeElement(nums, val);
	// any modification to nums in your function would be known by the caller.
	// using the length returned by your function, it prints the first len elements.
	for (int i = 0; i < len; i++) {
	    print(nums[i]);
	}"""

    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        for x in nums: 
            if x != val: nums[i], i = x, i+1
        return i


    """28. Implement strStr() (Easy)
	Implement strStr(). Return the index of the first occurrence of needle in 
	haystack, or -1 if needle is not part of haystack.

	Example 1:
	Input: haystack = "hello", needle = "ll"
	Output: 2

	Example 2:
	Input: haystack = "aaaaa", needle = "bba"
	Output: -1

	Clarification: 	What should we return when needle is an empty string? This 
	is a great question to ask during an interview. For the purpose of this 
	problem, we will return 0 when needle is an empty string. This is 
	consistent to C's strstr() and Java's indexOf()."""

    def strStr(self, haystack: str, needle: str) -> int:
        """Knuth-Morris-Pratt algo (1977)"""
        if not needle: return 0 #edge case 
        
        lps = [0]*len(needle) #longest prefix-suffix table 
        k = 0
        for i in range(1, len(needle)): 
            while k and needle[k] != needle[i]: k = lps[k-1]
            if needle[k] == needle[i]: k += 1
            lps[i] = k 
            
        k = 0
        for i in range(len(haystack)): 
            while k and needle[k] != haystack[i]: k = lps[k-1]
            if needle[k] == haystack[i]: k += 1
            if k == len(needle): return i - len(needle) + 1
        return -1


    """29. Divide Two Integers (Medium)
	Given two integers dividend and divisor, divide two integers without using 
	multiplication, division and mod operator. Return the quotient after 
	dividing dividend by divisor. The integer division should truncate toward 
	zero, which means losing its fractional part. 

	For example, truncate(8.345) = 8 and truncate(-2.7335) = -2.

	Example 1:
	Input: dividend = 10, divisor = 3
	Output: 3
	Explanation: 10/3 = truncate(3.33333..) = 3.

	Example 2:
	Input: dividend = 7, divisor = -3
	Output: -2
	Explanation: 7/-3 = truncate(-2.33333..) = -2.

	Note: Both dividend and divisor will be 32-bit signed integers. The divisor 
	will never be 0. Assume we are dealing with an environment which could only 
	store integers within the 32-bit signed integer range: [−2^31,  2^31 − 1]. 
	For the purpose of this problem, assume that your function returns 2^31 − 1 
	when the division result overflows."""
    
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == -2147483648 and divisor == -1: return 2147483647 #edge case 
        
        neg = (dividend > 0) ^ (divisor > 0)
        ans, dividend, divisor = 0, abs(dividend), abs(divisor)
        for i in reversed(range(32)):
            if dividend >= divisor << i: 
                ans |= 1 << i
                dividend -= divisor << i
        return -ans if neg else ans 


    """30. Substring with Concatenation of All Words (Hard)
	You are given a string, s, and a list of words, words, that are all of the 
	same length. Find all starting indices of substring(s) in s that is a 
	concatenation of each word in words exactly once and without any 
	intervening characters.

	Example 1:
	Input:
	  s = "barfoothefoobarman",
	  words = ["foo","bar"]
	Output: [0,9]

	Explanation: Substrings starting at index 0 and 9 are "barfoo" and "foobar" respectively.
	The output order does not matter, returning [9,0] is fine too.

	Example 2:
	Input:
	  s = "wordgoodgoodgoodbestword",
	  words = ["word","good","best","word"]
	Output: []"""

    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not words: return []
        
        target = dict()
        for word in words: target[word] = target.get(word, 0) + 1
            
        ans, n = [], len(words[0])
        for i in range(n): 
            freq, kk = dict(), i
            for j in range(i, len(s), n): 
                word = s[j:j+n]
                freq[word] = freq.get(word, 0) + 1
                while freq[word] > target.get(word, 0): 
                    freq[s[kk:(kk:=kk+n)]] -= 1
                if j + n - kk == n * len(words): ans.append(kk)
        return ans 


    """31. Next Permutation (Medium)
	Implement next permutation, which rearranges numbers into the 
	lexicographically next greater permutation of numbers. If such arrangement 
	is not possible, it must rearrange it as the lowest possible order (ie, 
	sorted in ascending order). The replacement must be in-place and use only 
	constant extra memory. Here are some examples. Inputs are in the left-hand 
	column and its corresponding outputs are in the right-hand column.

	1,2,3 → 1,3,2
	3,2,1 → 1,2,3
	1,1,5 → 1,5,1"""

    def nextPermutation(self, nums: List[int]) -> None:
        k = len(nums)-1
        while k and nums[k-1] >= nums[k]: k -= 1
            
        if k: 
            lo, hi = k, len(nums)
            while lo < hi:
                mid = (lo + hi)//2
                if nums[mid] <= nums[k-1]: hi = mid
                else: lo = mid+1
            nums[k-1], nums[lo-1] = nums[lo-1], nums[k-1]
        
        lo, hi = k, len(nums)-1
        while lo < hi: 
            nums[lo], nums[hi] = nums[hi], nums[lo]
            lo, hi = lo+1, hi-1  


    """32. Longest Valid Parentheses (Hard)
	Given a string containing just the characters '(' and ')', find the length 
	of the longest valid (well-formed) parentheses substring.

	Example 1:
	Input: "(()"
	Output: 2
	Explanation: The longest valid parentheses substring is "()"

	Example 2:
	Input: ")()())"
	Output: 4
	Explanation: The longest valid parentheses substring is "()()"""

    def longestValidParentheses(self, s: str) -> int:
        
        def fn(fwd, ans=0): 
            op = cl = 0
            for c in s if fwd else reversed(s): 
                if c == "(": op += 1
                else: cl += 1
                if (lt if fwd else gt)(op, cl): op = cl = 0
                elif op == cl: ans = max(ans, op + cl)
            return ans 
        
        return fn(False, fn(True))

    """33. Search in Rotated Sorted Array (Medium)
	Suppose an array sorted in ascending order is rotated at some pivot unknown 
	to you beforehand. (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]). 
	You are given a target value to search. If found in the array return its 
	index, otherwise return -1. You may assume no duplicate exists in the array. 
	Your algorithm's runtime complexity must be in the order of O(log n).

	Example 1:
	Input: nums = [4,5,6,7,0,1,2], target = 0
	Output: 4

	Example 2:
	Input: nums = [4,5,6,7,0,1,2], target = 3
	Output: -1"""

    def search(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums)-1
        while lo <= hi: 
            mid = (lo + hi)//2
            if nums[mid] == target: return mid
            if nums[lo] <= nums[mid]: 
                if nums[lo] <= target < nums[mid]: hi = mid - 1
                else: lo = mid + 1
            else: 
                if nums[mid] < target <= nums[hi]: lo = mid + 1
                else: hi = mid - 1
        return -1


    """34. Find First and Last Position of Element in Sorted Array (Medium)
	Given an array of integers nums sorted in ascending order, find the 
	starting and ending position of a given target value. Your algorithm's 
	runtime complexity must be in the order of O(log n). If the target is not 
	found in the array, return [-1, -1].

	Example 1:
	Input: nums = [5,7,7,8,8,10], target = 8
	Output: [3,4]

	Example 2:
	Input: nums = [5,7,7,8,8,10], target = 6
	Output: [-1,-1]"""

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def fn(x, lo=0, hi=len(nums)):
            while lo < hi:
                mid = (lo + hi)//2
                if nums[mid] >= x: hi = mid
                else: lo = mid+1
            return lo 
        
        lo = fn(target)
        if not lo < len(nums) or nums[lo] != target: return [-1, -1]
        return [lo, fn(target+1, lo)-1]


    """35. Search Insert Position (Easy)
	Given a sorted array and a target value, return the index if the target is 
	found. If not, return the index where it would be if it were inserted in 
	order. You may assume no duplicates in the array.

	Example 1:
	Input: [1,3,5,6], 5
	Output: 2

	Example 2:
	Input: [1,3,5,6], 2
	Output: 1

	Example 3:
	Input: [1,3,5,6], 7
	Output: 4

	Example 4:
	Input: [1,3,5,6], 0
	Output: 0"""

    def searchInsert(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums)
        while lo < hi:
            mid = (lo + hi)//2
            if nums[mid] < target: lo = mid + 1
            else: hi = mid
        return lo 


    """36. Valid Sudoku (Medium)
	Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be 
	validated according to the following rules:

	+ Each row must contain the digits 1-9 without repetition.
	+ Each column must contain the digits 1-9 without repetition.
	+ Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 
	without repetition.

	A partially filled sudoku which is valid. The Sudoku board could be 
	partially filled, where empty cells are filled with the character '.'.

	Example 1:
	Input:
	[
	  ["5","3",".",".","7",".",".",".","."],
	  ["6",".",".","1","9","5",".",".","."],
	  [".","9","8",".",".",".",".","6","."],
	  ["8",".",".",".","6",".",".",".","3"],
	  ["4",".",".","8",".","3",".",".","1"],
	  ["7",".",".",".","2",".",".",".","6"],
	  [".","6",".",".",".",".","2","8","."],
	  [".",".",".","4","1","9",".",".","5"],
	  [".",".",".",".","8",".",".","7","9"]
	]
	Output: true

	Example 2:
	Input:
	[
	  ["8","3",".",".","7",".",".",".","."],
	  ["6",".",".","1","9","5",".",".","."],
	  [".","9","8",".",".",".",".","6","."],
	  ["8",".",".",".","6",".",".",".","3"],
	  ["4",".",".","8",".","3",".",".","1"],
	  ["7",".",".",".","2",".",".",".","6"],
	  [".","6",".",".",".",".","2","8","."],
	  [".",".",".","4","1","9",".",".","5"],
	  [".",".",".",".","8",".",".","7","9"]
	]
	Output: false

	Explanation: Same as Example 1, except with the 5 in the top left corner 
	being modified to 8. Since there are two 8's in the top left 3x3 sub-box, 
	it is invalid.
	
	Note:
	A Sudoku board (partially filled) could be valid but is not necessarily 
	solvable. Only the filled cells need to be validated according to the 
	mentioned rules. The given board contain only digits 1-9 and the character 
	'.'. The given board size is always 9x9."""

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()
        for i, j in product(range(9), range(9)):
            if board[i][j] != ".": 
                item = {(i, board[i][j]), (board[i][j], j), (i//3, board[i][j], j//3)}
                if seen & item: return False 
                seen |= item
        return True


    """37. Sudoku Solver (Hard)
	Write a program to solve a Sudoku puzzle by filling the empty cells. A 
	sudoku solution must satisfy all of the following rules:

	Each of the digits 1-9 must occur exactly once in each row.
	Each of the digits 1-9 must occur exactly once in each column.
	Each of the the digits 1-9 must occur exactly once in each of the 9 3x3 
	sub-boxes of the grid.
	
	Empty cells are indicated by the character '.'.

	Note:
	The given board contain only digits 1-9 and the character '.'.
	You may assume that the given Sudoku puzzle will have a single unique solution.
	The given board size is always 9x9."""

    def solveSudoku(self, board: List[List[str]]) -> None:
        empty = []
        seen = set()
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".": empty.append((i, j))
                else: seen |= {(i, board[i][j]), (board[i][j], j), (i//3, board[i][j], j//3)}
        
        def fn(k, seen): 
            """Return True if Sudoku is filled properly (for early termination)"""
            if k == len(empty): return True
            i, j = empty[k]
            for x in "123456789": 
                if seen & {(i, x), (x, j), (i//3, x, j//3)}: continue
                seen |= {(i, x), (x, j), (i//3, x, j//3)}
                board[i][j] = x
                if fn(k+1, seen): return True 
                seen -= {(i, x), (x, j), (i//3, x, j//3)}
        
        fn(0, seen)


    """38. Count and Say (Easy)
	The count-and-say sequence is the sequence of integers with the first five 
	terms as following:

	1.     1
	2.     11
	3.     21
	4.     1211
	5.     111221
	1 is read off as "one 1" or 11.
	11 is read off as "two 1s" or 21.
	21 is read off as "one 2, then one 1" or 1211.

	Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-
	and-say sequence. You can do so recursively, in other words from the 
	previous member read off the digits, counting the number of digits in 
	groups of the same digit.

	Note: Each term of the sequence of integers will be represented as a string.

	Example 1:
	Input: 1
	Output: "1"
	Explanation: This is the base case.

	Example 2:
	Input: 4
	Output: "1211"
	Explanation: For n = 3 the term was "21" in which we have two groups "2" 
	and "1", "2" can be read as "12" which means frequency = 1 and value = 2, 
	the same way "1" is read as "11", so the answer is the concatenation of 
	"12" and "11" which is "1211"."""

    def countAndSay(self, n: int) -> str:
        if n == 1: return "1"
        return "".join(str(len(list(v))) + g for g, v in groupby(self.countAndSay(n-1)))


    """39. Combination Sum (Medium)
	Given a set of candidate numbers (candidates) (without duplicates) and a 
	target number (target), find all unique combinations in candidates where 
	the candidate numbers sums to target. The same repeated number may be 
	chosen from candidates unlimited number of times.

	Note:
	All numbers (including target) will be positive integers.
	The solution set must not contain duplicate combinations.

	Example 1:
	Input: candidates = [2,3,6,7], target = 7,
	A solution set is:
	[
	  [7],
	  [2,2,3]
	]

	Example 2:
	Input: candidates = [2,3,5], target = 8,
	A solution set is:
	[
	  [2,2,2,2],
	  [2,3,3],
	  [3,5]
	]"""

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        
        def fn(stack, x, k=0):
            """backtracking using a stack"""
            if x == 0: return ans.append(stack.copy()) #store a copy 
            for i in range(k, len(candidates)): 
                if candidates[i] > x: break 
                stack.append(candidates[i])
                fn(stack, x-candidates[i], i)
                stack.pop()
        
        ans = []
        fn([], target)
        return ans 


    """40. Combination Sum II (Medium)
	Given a collection of candidate numbers (candidates) and a target number 
	(target), find all unique combinations in candidates where the candidate 
	numbers sums to target. Each number in candidates may only be used once in 
	the combination.

	Note:
	All numbers (including target) will be positive integers. The solution set 
	must not contain duplicate combinations.
	
	Example 1:
	Input: candidates = [10,1,2,7,6,1,5], target = 8,
	A solution set is:
	[
	  [1, 7],
	  [1, 2, 5],
	  [2, 6],
	  [1, 1, 6]
	]

	Example 2:
	Input: candidates = [2,5,2,1,2], target = 5,
	A solution set is:
	[
	  [1,2,2],
	  [5]
	]"""

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        
        def fn(stack, x, k=0):
            """backtracking using a stack"""
            if x == 0: return ans.append(stack.copy())
            for i in range(k, len(candidates)):
                if candidates[i] > x: break 
                if i > k and candidates[i] == candidates[i-1]: continue
                stack.append(candidates[i])
                fn(stack, x - candidates[i], i+1)
                stack.pop()
                
        ans = []
        fn([], target)
        return ans 


    """41. First Missing Positive (Hard)
	Given an unsorted integer array, find the smallest missing positive integer.

	Example 1:

	Input: [1,2,0]
	Output: 3
	Example 2:

	Input: [3,4,-1,1]
	Output: 2
	Example 3:

	Input: [7,8,9,11,12]
	Output: 1
	Note:

	Your algorithm should run in O(n) time and uses constant extra space."""

    def firstMissingPositive(self, nums: List[int]) -> int:
        
        for i in range(len(nums)):
            k = nums[i]
            while k and 0 < k <= len(nums): 
                nums[k-1], k = None, nums[k-1]
                
        return next((i+1 for i in range(len(nums)) if nums[i] is not None), len(nums)+1)


    """42. Trapping Rain Water (Hard)
	Given n non-negative integers representing an elevation map where the width 
	of each bar is 1, compute how much water it is able to trap after raining.
	The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. 
	In this case, 6 units of rain water (blue section) are being trapped. 

	Example:
	Input: [0,1,0,2,1,0,1,3,2,1,2,1]
	Output: 6"""

    def trap(self, height: List[int]) -> int:
        ans = left = right = 0
        lo, hi = 0, len(height)-1
        while lo < hi: 
            if height[lo] < height[hi]: 
                left = max(left, height[lo])
                ans += left - height[lo]
                lo += 1
            else: 
                right = max(right, height[hi])
                ans += right - height[hi]
                hi -= 1
        return ans 



    """43. Multiply Strings (Medium)
	Given two non-negative integers num1 and num2 represented as strings, 
	return the product of num1 and num2, also represented as a string.

	Example 1:
	Input: num1 = "2", num2 = "3"
	Output: "6"

	Example 2:
	Input: num1 = "123", num2 = "456"
	Output: "56088"

	Note:
	+ The length of both num1 and num2 is < 110.
	+ Both num1 and num2 contain only digits 0-9.
	+ Both num1 and num2 do not contain any leading zero, except the number 0 
	  itself.
	+ You must not use any built-in BigInteger library or convert the inputs to 
	  integer directly."""

    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0": return "0" #edge case 
        
        ans = [0] * (len(num1) + len(num2))
        for i, x in enumerate(reversed(num1)):
            for j, y in enumerate(reversed(num2)): 
                num = (ord(x) - 48) * (ord(y) - 48)
                k = i + j
                while num: 
                    num, ans[k] = divmod(num + ans[k], 10)
                    k += 1
        return "".join(map(str, reversed(ans[:k])))


    """44. Wildcard Matching (Hard)
	Given an input string (s) and a pattern (p), implement wildcard pattern 
	matching with support for '?' and '*'.

	'?' Matches any single character.
	'*' Matches any sequence of characters (including the empty sequence).
	The matching should cover the entire input string (not partial).

	Note:
	s could be empty and contains only lowercase letters a-z.
	p could be empty and contains only lowercase letters a-z, and characters 
	like ? or *.
	
	Example 1:
	Input:
	s = "aa"
	p = "a"
	Output: false
	Explanation: "a" does not match the entire string "aa".
	
	Example 2:
	Input:
	s = "aa"
	p = "*"
	Output: true
	Explanation: '*' matches any sequence.

	Example 3:
	Input:
	s = "cb"
	p = "?a"
	Output: false
	Explanation: '?' matches 'c', but the second letter is 'a', which does not 
	match 'b'.

	Example 4:
	Input:
	s = "adceb"
	p = "*a*b"
	Output: true
	Explanation: The first '*' matches the empty sequence, while the second '*' 
	matches the substring "dce".
	
	Example 5:
	Input:
	s = "acdcb"
	p = "a*c?b"
	Output: false"""

    def isMatch(self, s: str, p: str) -> bool:
        
        @lru_cache(None)
        def fn(i, j): 
            """Return True if s[i:] matches p[j:]"""
            if j == len(p): return i == len(s)
            if i < len(s) and (s[i] == p[j] or p[j] == "?"): return fn(i+1, j+1)
            if p[j] == "*": return fn(i, j+1) or i < len(s) and fn(i+1, j)
            return False 
        
        return fn(0, 0)


    """45. Jump Game II (Hard)
	Given an array of non-negative integers, you are initially positioned at 
	the first index of the array. Each element in the array represents your 
	maximum jump length at that position. Your goal is to reach the last index 
	in the minimum number of jumps.

	Example:
	Input: [2,3,1,1,4]
	Output: 2
	Explanation: The minimum number of jumps to reach the last index is 2.
    Jump 1 step from index 0 to 1, then 3 steps to the last index.

	Note: You can assume that you can always reach the last index."""

    def jump(self, nums: List[int]) -> int:
        curr = next = jump = 0
        for i in range(len(nums)):
            if i > curr: 
                curr = next;
                jump += 1
            next = max(next, i + nums[i])
        return jump 


    """46. Permutations (Medium)
	Given a collection of distinct integers, return all possible permutations.

	Example:
	Input: [1,2,3]
	Output:
	[
	  [1,2,3],
	  [1,3,2],
	  [2,1,3],
	  [2,3,1],
	  [3,1,2],
	  [3,2,1]
	]"""

    def permute(self, nums: List[int]) -> List[List[int]]:
        
        def fn(i):
            """Backtracking to get permutations (not Heap's algo)"""
            if i == len(nums): ans.append(nums.copy())
            for j in range(i, len(nums)): 
                nums[i], nums[j] = nums[j], nums[i]
                fn(i+1)
                nums[i], nums[j] = nums[j], nums[i]
            
        ans = []
        fn(0)
        return ans 


    """47. Permutations II (Medium)
	Given a collection of numbers that might contain duplicates, return all 
	possible unique permutations.

	Example:
	Input: [1,1,2]
	Output:
	[
	  [1,1,2],
	  [1,2,1],
	  [2,1,1]
	]"""

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        
        def fn(i):
            """Backtracking to get permutations (not Heap's algo)"""
            if i == len(nums): ans.append(nums.copy())
            seen = set()
            for k in range(i, len(nums)):
                if nums[k] not in seen:
                    seen.add(nums[k])
                    nums[i], nums[k] = nums[k], nums[i]
                    fn(i+1)
                    nums[i], nums[k] = nums[k], nums[i]
        
        ans = []
        fn(0)
        return ans 

    """48. Rotate Image (Medium)
	You are given an n x n 2D matrix representing an image. Rotate the image by 
	90 degrees (clockwise).

	Note:
	You have to rotate the image in-place, which means you have to modify the 
	input 2D matrix directly. DO NOT allocate another 2D matrix and do the 
	rotation.

	Example 1:
	Given input matrix = 
	[
	  [1,2,3],
	  [4,5,6],
	  [7,8,9]
	],
	rotate the input matrix in-place such that it becomes:
	[
	  [7,4,1],
	  [8,5,2],
	  [9,6,3]
	]

	Example 2:
	Given input matrix =
	[
	  [ 5, 1, 9,11],
	  [ 2, 4, 8,10],
	  [13, 3, 6, 7],
	  [15,14,12,16]
	], 
	rotate the input matrix in-place such that it becomes:
	[
	  [15,13, 2, 5],
	  [14, 3, 4, 1],
	  [12, 6, 8, 9],
	  [16, 7,10,11]
	]"""

    def rotate(self, matrix: List[List[int]]) -> None:
        matrix[:] = [list(x) for x in zip(*matrix[::-1])]


    """49. Group Anagrams (Medium)
	Given an array of strings, group anagrams together.

	Example:
	Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
	Output:
	[
	  ["ate","eat","tea"],
	  ["nat","tan"],
	  ["bat"]
	]
	
	Note:
	All inputs will be in lowercase.
	The order of your output does not matter."""
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = dict()
        for word in strs:
            ans.setdefault("".join(sorted(word)), []).append(word)
        return ans.values()


    """50. Pow(x, n) (Medium)
	Implement pow(x, n), which calculates x raised to the power n (x^n).

	Example 1:
	Input: 2.00000, 10
	Output: 1024.00000

	Example 2:
	Input: 2.10000, 3
	Output: 9.26100

	Example 3:
	Input: 2.00000, -2
	Output: 0.25000
	Explanation: 2-2 = 1/22 = 1/4 = 0.25

	Note:
	-100.0 < x < 100.0
	n is a 32-bit signed integer, within the range [−2^31, 2^31 − 1]"""

    def myPow(self, x: float, n: int) -> float:
        if n < 0: x, n = 1/x, -n
        ans = 1
        while n: 
            if n & 1: ans *= x
            x, n = x*x, n//2
        return ans 


    """51. N-Queens (Hard)
	The n-queens puzzle is the problem of placing n queens on an n×n chessboard 
	such that no two queens attack each other. Given an integer n, return all 
	distinct solutions to the n-queens puzzle. Each solution contains a 
	distinct board configuration of the n-queens' placement, where 'Q' and '.' 
	both indicate a queen and an empty space respectively.

	Example:
	Input: 4
	Output: [
	 [".Q..",  // Solution 1
	  "...Q",
	  "Q...",
	  "..Q."],

	 ["..Q.",  // Solution 2
	  "Q...",
	  "...Q",
	  ".Q.."]
	]
	Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above."""

    def solveNQueens(self, n: int) -> List[List[str]]:
        
        def fn(i, seen):
            """Populate ans through backtracking row by row"""
            if i == n: ans.append(["".join(row) for row in sol])
            for j in range(n):
                place = {("col", j), ("diag", i-j), ("anti", i+j)}
                if not (place & seen): 
                    sol[i][j] = "Q"
                    seen |= place
                    fn(i+1, seen)
                    sol[i][j] = "."
                    seen -= place 
                    
        ans, sol = [], [["."]*n for _ in range(n)]
        fn(0, set())
        return ans 


    """52. N-Queens II (Hard)
	The n-queens puzzle is the problem of placing n queens on an n×n chessboard 
	such that no two queens attack each other. Given an integer n, return the 
	number of distinct solutions to the n-queens puzzle.

	Example:
	Input: 4
	Output: 2
	Explanation: There are two distinct solutions to the 4-queens puzzle as shown below.
	[
	 [".Q..",  // Solution 1
	  "...Q",
	  "Q...",
	  "..Q."],

	 ["..Q.",  // Solution 2
	  "Q...",
	  "...Q",
	  ".Q.."]
	]"""

    def totalNQueens(self, n: int) -> int:
        
        def fn(i, seen=set(), ans=0):
            """Return the number of solutions"""
            if i == n: ans += 1
            for j in range(n):
                place = {("col", j), ("diag", i-j), ("anti", i+j)}
                if not (place & seen): 
                    seen |= place
                    ans = fn(i+1, seen, ans)
                    seen -= place 
            return ans 
        
        return fn(0)


    """53. Maximum Subarray (Easy)
	Given an integer array nums, find the contiguous subarray (containing at 
	least one number) which has the largest sum and return its sum.

	Example:

	Input: [-2,1,-3,4,-1,2,1,-5,4],
	Output: 6
	Explanation: [4,-1,2,1] has the largest sum = 6.
	
	Follow up: If you have figured out the O(n) solution, try coding another 
	solution using the divide and conquer approach, which is more subtle."""

    def maxSubArray(self, nums: List[int]) -> int:
        ans, val = float("-inf"), 0
        for x in nums:
            val = max(0, val) + x
            ans = max(ans, val)
        return ans 


    """54. Spiral Matrix (Medium)
	Given a matrix of m x n elements (m rows, n columns), return all elements 
	of the matrix in spiral order.

	Example 1:
	Input:
	[
	 [ 1, 2, 3 ],
	 [ 4, 5, 6 ],
	 [ 7, 8, 9 ]
	]
	Output: [1,2,3,6,9,8,7,4,5]

	Example 2:
	Input:
	[
	  [1, 2, 3, 4],
	  [5, 6, 7, 8],
	  [9,10,11,12]
	]
	Output: [1,2,3,4,8,12,11,10,9,5,6,7]"""

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix: return [] #edge case 
        ans = []
        m, n = len(matrix), len(matrix[0])
        i, j, di, dj, k = 0, 0, 0, 1, 0  #position, direction & side
        bd = [0, n, m, 0] #boundary (top|right|bottom|left)
        for _ in range(m*n): 
            ans.append(matrix[i][j])
            if not(bd[0] <= i + di < bd[2] and bd[3] <= j + dj < bd[1]): 
                di, dj = dj, -di           #rotate 
                if k in (0, 3): bd[k] += 1 #top or left boundary
                else: bd[k] -= 1           #bottom or right boundary
                k = (k+1)%4
            i, j = i+di, j+dj
        return ans 


    """55. Jump Game (Medium)
	Given an array of non-negative integers, you are initially positioned at 
	the first index of the array. Each element in the array represents your 
	maximum jump length at that position. Determine if you are able to reach 
	the last index.

	Example 1:
	Input: nums = [2,3,1,1,4]
	Output: true
	Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

	Example 2:
	Input: nums = [3,2,1,0,4]
	Output: false
	Explanation: You will always arrive at index 3 no matter what. Its maximum 
	jump length is 0, which makes it impossible to reach the last index.

	Constraints:
	1 <= nums.length <= 3 * 10^4
	0 <= nums[i][j] <= 10^5"""

    def canJump(self, nums: List[int]) -> bool:
        limit = 0
        for i in range(len(nums)): 
            if i > limit: return False 
            limit = max(limit, i + nums[i])
        return True 




    """56. Merge Intervals (Medium)
	Given a collection of intervals, merge all overlapping intervals.

	Example 1:
	Input: [[1,3],[2,6],[8,10],[15,18]]
	Output: [[1,6],[8,10],[15,18]]
	Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into 
	[1,6].

	Example 2:
	Input: [[1,4],[4,5]]
	Output: [[1,5]]
	Explanation: Intervals [1,4] and [4,5] are considered overlapping.

	NOTE: input types have been changed on April 15, 2019. Please reset to 
	default code definition to get new method signature."""

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ans = []
        for interval in intervals: 
            if ans and ans[-1][1] >= interval[0]: 
                ans[-1][1] = max(ans[-1][1], interval[1])
            else: ans.append(interval)
        return ans


    """57. Insert Interval (Hard)
	Given a set of non-overlapping intervals, insert a new interval into the 
	intervals (merge if necessary). You may assume that the intervals were 
	initially sorted according to their start times.

	Example 1:
	Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
	Output: [[1,5],[6,9]]

	Example 2:
	Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
	Output: [[1,2],[3,10],[12,16]]
	Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].

	NOTE: input types have been changed on April 15, 2019. Please reset to 
	default code definition to get new method signature."""

    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans = []
        for i, interval in enumerate(intervals): 
            if interval[1] < newInterval[0]: ans.append(interval)
            elif not (newInterval[1] < interval[0]): 
                newInterval[0] = min(newInterval[0], interval[0])
                newInterval[1] = max(newInterval[1], interval[1])
            else: 
                ans.append(newInterval)
                return ans + intervals[i:]
        return ans + [newInterval]

    """58. Length of Last Word (Easy)
	Given a string s consists of upper/lower-case alphabets and empty space 
	characters ' ', return the length of last word (last word means the last 
	appearing word if we loop from left to right) in the string. If the last 
	word does not exist, return 0.

	Note: A word is defined as a maximal substring consisting of non-space 
	characters only.

	Example:
	Input: "Hello World"
	Output: 5"""

    def lengthOfLastWord(self, s: str) -> int:
        words = s.split()
        return len(words[-1]) if words else 0


    """59. Spiral Matrix II (Medium)
	Given a positive integer n, generate a square matrix filled with elements 
	from 1 to n2 in spiral order.

	Example:
	Input: 3
	Output:
	[
	 [ 1, 2, 3 ],
	 [ 8, 9, 4 ],
	 [ 7, 6, 5 ]
	]"""

    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0]*n for _ in range(n)]
        i, j, di, dj = 0, 0, 0, 1
        for v in range(1, n*n+1):
            matrix[i][j] = v
            if matrix[(i+di)%n][(j+dj)%n]: di, dj = dj, -di
            i, j = i+di, j+dj
        return matrix 


    """60. Permutation Sequence (Medium)
	The set [1,2,3,...,n] contains a total of n! unique permutations. By 
	listing and labeling all of the permutations in order, we get the following 
	sequence for n = 3:

	"123"
	"132"
	"213"
	"231"
	"312"
	"321"

	Given n and k, return the kth permutation sequence.

	Note:
	Given n will be between 1 and 9 inclusive.
	Given k will be between 1 and n! inclusive.

	Example 1:
	Input: n = 3, k = 3
	Output: "213"

	Example 2:
	Input: n = 4, k = 9
	Output: "2314" """

    def getPermutation(self, n: int, k: int) -> str:
        k -= 1
        ans, digits = [], list(range(1, n+1))
        for i in range(n):
            d, k = divmod(k, factorial(n-i-1))
            ans.append(digits.pop(d))
        return "".join(str(x) for x in ans)


    """61. Rotate List (Medium)
	Given a linked list, rotate the list to the right by k places, where k is 
	non-negative.

	Example 1:
	Input: 1->2->3->4->5->NULL, k = 2
	Output: 4->5->1->2->3->NULL
	Explanation:
	rotate 1 steps to the right: 5->1->2->3->4->NULL
	rotate 2 steps to the right: 4->5->1->2->3->NULL

	Example 2:
	Input: 0->1->2->NULL, k = 4
	Output: 2->0->1->NULL
	Explanation:
	rotate 1 steps to the right: 2->0->1->NULL
	rotate 2 steps to the right: 1->2->0->NULL
	rotate 3 steps to the right: 0->1->2->NULL
	rotate 4 steps to the right: 2->0->1->NULL"""

    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head: return None
        
        n, node = 0, head
        while node: n, node = n+1, node.next
        
        k %= n
        if k: 
            fast = slow = head 
            while fast.next: 
                if k == 0: slow = slow.next
                else: k -= 1
                fast = fast.next 
            head, fast.next, slow.next = slow.next, head, None
        return head


    """62. Unique Paths (Medium)
	A robot is located at the top-left corner of a m x n grid (marked 'Start' 
	in the diagram below). The robot can only move either down or right at any 
	point in time. The robot is trying to reach the bottom-right corner of the 
	grid (marked 'Finish' in the diagram below). How many possible unique paths 
	are there?

	Example 1:
	Input: m = 3, n = 2
	Output: 3
	Explanation:
	From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
	1. Right -> Right -> Down
	2. Right -> Down -> Right
	3. Down -> Right -> Right

	Example 2:
	Input: m = 7, n = 3
	Output: 28

	Constraints:
	1 <= m, n <= 100
	It's guaranteed that the answer will be less than or equal to 2 * 10 ^ 9."""
    
    def uniquePaths(self, m: int, n: int) -> int:
        
        def choose(n, k): 
            """Return n choose k"""
            ans, k = 1, min(k, n-k)
            for i in range(k):
                ans *= n-i
                ans //= i+1
            return ans 
        
        return choose(m+n-2, m-1)


    """63. Unique Paths II (Medium)
	A robot is located at the top-left corner of a m x n grid (marked 'Start' 
	in the diagram below). The robot can only move either down or right at any 
	point in time. The robot is trying to reach the bottom-right corner of the 
	grid (marked 'Finish' in the diagram below). Now consider if some obstacles 
	are added to the grids. How many unique paths would there be? An obstacle 
	and empty space is marked as 1 and 0 respectively in the grid.

	Note: m and n will be at most 100.

	Example 1:
	Input:
	[
	  [0,0,0],
	  [0,1,0],
	  [0,0,0]
	]
	Output: 2
	Explanation:
	There is one obstacle in the middle of the 3x3 grid above.
	There are two ways to reach the bottom-right corner:
	1. Right -> Right -> Down -> Down
	2. Down -> Down -> Right -> Right"""

    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        
        @lru_cache(None)
        def fn(i, j): 
            """Return number of unique paths ending at (i, j)"""
            if i < 0 or j < 0 or obstacleGrid[i][j]: return 0
            if i == 0 and j == 0: return 1 
            return fn(i-1, j) + fn(i, j-1)
        
        return fn(m-1, n-1)


    """64. Minimum Path Sum (Medium)
	Given a m x n grid filled with non-negative numbers, find a path from top 
	left to bottom right which minimizes the sum of all numbers along its path.
	Note: You can only move either down or right at any point in time.

	Example:

	Input:
	[
	  [1,3,1],
	  [1,5,1],
	  [4,2,1]
	]
	Output: 7
	Explanation: Because the path 1→3→1→1→1 minimizes the sum."""

    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        @lru_cache(None)
        def fn(i, j): 
            """Return min path sum ending at (i, j)"""
            if i == 0 and j == 0: return grid[i][j]
            if i < 0 or j < 0: return float("inf")
            return grid[i][j] + min(fn(i-1, j), fn(i, j-1))
        
        return fn(m-1, n-1)


    """65. Valid Number (Hard)
	Validate if a given string can be interpreted as a decimal number.

	Some examples:
	"0"         => true
	" 0.1 "     => true
	"abc"       => false
	"1 a"       => false
	"2e10"      => true
	" -90e3   " => true
	" 1e"       => false
	"e3"        => false
	" 6e-1"     => true
	" 99e2.5 "  => false
	"53.5e93"   => true
	" --6 "     => false
	"-+3"       => false
	"95a54e53"  => false

	Note: It is intended for the problem statement to be ambiguous. You should 
	gather all requirements up front before implementing one. However, here is 
	a list of characters that can be in a valid decimal number:

	Numbers 0-9
	Exponent - "e"
	Positive/negative sign - "+"/"-"
	Decimal point - "."
	Of course, the context of these characters also matters in the input.

	Update (2015-02-10): The signature of the C++ function had been updated. If 
	you still see your function signature accepts a const char * argument, 
	please click the reload button to reset your code definition."""

    def isNumber(self, s: str) -> bool:
        dfa = [{'space': 0, 'sign': 1, 'digit': 2, '.': 3}, #state 0 - leading space
               {'digit': 2, '.': 3},                        #state 1 - sign
               {'digit': 2, '.': 4, 'e': 5, 'space': 8},    #state 2 - digit (terminal)
               {'digit': 4},                                #state 3 - dot
               {'digit': 4, 'e': 5, 'space': 8},            #state 4 - digit post dot (terminal)
               {'sign': 6, 'digit': 7},                     #state 5 - exponential 
               {'digit': 7},                                #state 6 - sign post exponential 
               {'digit': 7, 'space': 8},                    #state 7 - digit post exponential (terminal)
               {'space': 8}                                 #state 8 - trailing space (terminal)
              ]
        
        state = 0
        for c in s: 
            if c in "0123456789": c = "digit"
            elif c == " ":  c = "space"
            elif c in "+-": c = "sign"
            
            if c not in dfa[state]: return False 
            state = dfa[state][c]
            
        return state in [2, 4, 7, 8]


    """66. Plus One (Easy)
	Given a non-empty array of digits representing a non-negative integer, plus 
	one to the integer. The digits are stored such that the most significant 
	digit is at the head of the list, and each element in the array contain a 
	single digit. You may assume the integer does not contain any leading zero, 
	except the number 0 itself.

	Example 1:
	Input: [1,2,3]
	Output: [1,2,4]
	Explanation: The array represents the integer 123.

	Example 2:
	Input: [4,3,2,1]
	Output: [4,3,2,2]
	Explanation: The array represents the integer 4321."""

    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        for i in reversed(range(len(digits))):
            carry, digits[i] = divmod(digits[i] + carry, 10)
            if not carry: return digits
        return [carry] + digits


    """67. Add Binary (Easy)
	Given two binary strings, return their sum (also a binary string). The 
	input strings are both non-empty and contains only characters 1 or 0.

	Example 1:
	Input: a = "11", b = "1"
	Output: "100"

	Example 2:
	Input: a = "1010", b = "1011"
	Output: "10101"

	Constraints:
	Each string consists only of '0' or '1' characters.
	1 <= a.length, b.length <= 10^4
	Each string is either "0" or doesn't contain any leading zero."""

    def addBinary(self, a: str, b: str) -> str:
        ans, carry = [], 0
        for x, y in zip_longest(reversed(a), reversed(b), fillvalue=0):
            carry += (x == "1") + (y == "1")
            carry, d = divmod(carry, 2)
            ans.append(d)
        if carry: ans.append(carry)
        return "".join(map(str, reversed(ans)))


    """68. Text Justification (Hard)
	Given an array of words and a width maxWidth, format the text such that 
	each line has exactly maxWidth characters and is fully (left and right) 
	justified. You should pack your words in a greedy approach; that is, pack 
	as many words as you can in each line. Pad extra spaces ' ' when necessary 
	so that each line has exactly maxWidth characters. Extra spaces between 
	words should be distributed as evenly as possible. If the number of spaces 
	on a line do not divide evenly between words, the empty slots on the left 
	will be assigned more spaces than the slots on the right. For the last line 
	of text, it should be left justified and no extra space is inserted between 
	words.

	Note:
	A word is defined as a character sequence consisting of non-space 
	characters only. Each word's length is guaranteed to be greater than 0 and 
	not exceed maxWidth. The input array words contains at least one word.

	Example 1:
	Input:
	words = ["This", "is", "an", "example", "of", "text", "justification."]
	maxWidth = 16
	Output:
	[
	   "This    is    an",
	   "example  of text",
	   "justification.  "
	]
	
	Example 2:
	Input:
	words = ["What","must","be","acknowledgment","shall","be"]
	maxWidth = 16
	Output:
	[
	  "What   must   be",
	  "acknowledgment  ",
	  "shall be        "
	]
	Explanation: Note that the last line is "shall be    " instead of "shall     be",
	             because the last line must be left-justified instead of fully-justified.
	             Note that the second line is also left-justified becase it contains only one word.

	Example 3:
	Input:
	words = ["Science","is","what","we","understand","well","enough","to","explain",
	         "to","a","computer.","Art","is","everything","else","we","do"]
	maxWidth = 20
	Output:
	[
	  "Science  is  what we",
	  "understand      well",
	  "enough to explain to",
	  "a  computer.  Art is",
	  "everything  else  we",
	  "do                  "
	]"""

    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        ans = []
        line, width = [], 0
        
        for word in words: 
            if width + len(line) + len(word) > maxWidth: 
                n, k = divmod(maxWidth - width, max(1, len(line)-1))
                for i in range(max(1, len(line)-1)): 
                    line[i] += " " * (n + (i < k))
                ans.append("".join(line))
                line, width = [], 0
            line.append(word)
            width += len(word)
            
        ans.append(" ".join(line).ljust(maxWidth))
        return ans 


    """64. Minimum Path Sum (Medium)
	Given a m x n grid filled with non-negative numbers, find a path from top 
	left to bottom right which minimizes the sum of all numbers along its path.

	Note: You can only move either down or right at any point in time.

	Example:
	Input:
	[
	  [1,3,1],
	  [1,5,1],
	  [4,2,1]
	]
	Output: 7
	Explanation: Because the path 1→3→1→1→1 minimizes the sum."""

    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        @lru_cache(None)
        def fn(i, j): 
            """Return min path sum ending at (i, j)"""
            if i == 0 and j == 0: return grid[i][j]
            if i < 0 or j < 0: return float("inf")
            return grid[i][j] + min(fn(i-1, j), fn(i, j-1))
        
        return fn(m-1, n-1)


    """70. Climbing Stairs (Easy)
	You are climbing a stair case. It takes n steps to reach to the top. Each 
	time you can either climb 1 or 2 steps. In how many distinct ways can you 
	climb to the top?

	Note: Given n will be a positive integer.

	Example 1:
	Input: 2
	Output: 2
	Explanation: There are two ways to climb to the top.
	1. 1 step + 1 step
	2. 2 steps

	Example 2:
	Input: 3
	Output: 3
	Explanation: There are three ways to climb to the top.
	1. 1 step + 1 step + 1 step
	2. 1 step + 2 steps
	3. 2 steps + 1 step"""

    def climbStairs(self, n: int) -> int:
        
        @lru_cache(None)
        def fn(k): 
            """Return kth Fibonacci number"""
            if k <= 1: return 1
            return fn(k-1) + fn(k-2)
        
        return fn(n)


    """71. Simplify Path (Medium)
	Given an absolute path for a file (Unix-style), simplify it. Or in other 
	words, convert it to the canonical path. In a UNIX-style file system, a 
	period . refers to the current directory. Furthermore, a double period .. 
	moves the directory up a level. Note that the returned canonical path must 
	always begin with a slash /, and there must be only a single slash / 
	between two directory names. The last directory name (if it exists) must 
	not end with a trailing /. Also, the canonical path must be the shortest 
	string representing the absolute path.

	Example 1:
	Input: "/home/"
	Output: "/home"
	Explanation: Note that there is no trailing slash after the last directory name.

	Example 2:
	Input: "/../"
	Output: "/"
	Explanation: Going one level up from the root directory is a no-op, as the root level is the highest level you can go.

	Example 3:
	Input: "/home//foo/"
	Output: "/home/foo"
	Explanation: In the canonical path, multiple consecutive slashes are replaced by a single one.

	Example 4:
	Input: "/a/./b/../../c/"
	Output: "/c"

	Example 5:
	Input: "/a/../../b/../c//.//"
	Output: "/c"

	Example 6:
	Input: "/a//b////c/d//././/.."
	Output: "/a/b/c" """

    def simplifyPath(self, path: str) -> str:
        stack = []
        for x in path.split("/"):
                if x == ".." and stack: stack.pop()
                if x not in (".", "..", ""): stack.append(x)
        return "/" + "/".join(stack)


    """72. Edit Distance (Hard)
	Given two words word1 and word2, find the minimum number of operations 
	required to convert word1 to word2. You have the following 3 operations 
	permitted on a word:
	- Insert a character
	- Delete a character
	- Replace a character
	
	Example 1:
	Input: word1 = "horse", word2 = "ros"
	Output: 3
	Explanation: 
	horse -> rorse (replace 'h' with 'r')
	rorse -> rose (remove 'r')
	rose -> ros (remove 'e')

	Example 2:
	Input: word1 = "intention", word2 = "execution"
	Output: 5
	Explanation: 
	intention -> inention (remove 't')
	inention -> enention (replace 'i' with 'e')
	enention -> exention (replace 'n' with 'x')
	exention -> exection (replace 'n' with 'c')
	exection -> execution (insert 'u')"""

    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        
        @lru_cache(None)
        def fn(i, j): 
            """Return edit distance between word1[i:] and word2[j:]"""
            if i == m or j == n: return m + n - i - j
            if word1[i] == word2[j]: return fn(i+1, j+1)
            return 1 + min(fn(i+1, j), fn(i, j+1), fn(i+1, j+1))
        
        return fn(0, 0)


    """73. Set Matrix Zeroes (Medium)
	Given a m x n matrix, if an element is 0, set its entire row and column to 
	0. Do it in-place.

	Example 1:
	Input: 
	[
	  [1,1,1],
	  [1,0,1],
	  [1,1,1]
	]
	Output: 
	[
	  [1,0,1],
	  [0,0,0],
	  [1,0,1]
	]

	Example 2:
	Input: 
	[
	  [0,1,2,0],
	  [3,4,5,2],
	  [1,3,1,5]
	]
	Output: 
	[
	  [0,0,0,0],
	  [0,4,5,0],
	  [0,3,1,0]
	]

	Follow up:
	A straight forward solution using O(mn) space is probably a bad idea. A 
	simple improvement uses O(m + n) space, but still not the best solution.
	Could you devise a constant space solution?"""

    def setZeroes(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])
        zero = False 
        
        for i in range(m):
            if not matrix[i][0]: zero = True
            for j in range(1, n): 
                if not matrix[i][j]: matrix[i][0] = matrix[0][j] = 0
        
        for i in reversed(range(m)):
            for j in reversed(range(1, n)):
                if not matrix[i][0] or not matrix[0][j]: matrix[i][j] = 0
            if zero: matrix[i][0] = 0


    """74. Search a 2D Matrix (Medium)
	Write an efficient algorithm that searches for a value in an m x n matrix. 
	This matrix has the following properties: 
	- Integers in each row are sorted from left to right.
	- The first integer of each row is greater than the last integer of the 
	previous row.
	
	Example 1:
	Input:
	matrix = [
	  [1,   3,  5,  7],
	  [10, 11, 16, 20],
	  [23, 30, 34, 50]
	]
	target = 3
	Output: true

	Example 2:
	Input:
	matrix = [
	  [1,   3,  5,  7],
	  [10, 11, 16, 20],
	  [23, 30, 34, 50]
	]
	target = 13
	Output: false"""

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix: return False #edge case 
        
        m, n = len(matrix), len(matrix[0])
        lo, hi = 0, m*n
        while lo < hi: 
            mid = (lo + hi)//2
            i, j = divmod(mid, n)
            if matrix[i][j] == target: return True
            elif matrix[i][j] > target: hi = mid
            else: lo = mid+1
        return False 


    """75. Sort Colors (Medium)
	Given an array with n objects colored red, white or blue, sort them in-
	place so that objects of the same color are adjacent, with the colors in 
	the order red, white and blue. Here, we will use the integers 0, 1, and 2 
	to represent the color red, white, and blue respectively.

	Note: You are not suppose to use the library's sort function for this problem.

	Example:
	Input: [2,0,2,1,1,0]
	Output: [0,0,1,1,2,2]
	Follow up:

	A rather straight forward solution is a two-pass algorithm using counting 
	sort. First, iterate the array counting number of 0's, 1's, and 2's, then 
	overwrite array with total number of 0's, then 1's and followed by 2's.
	Could you come up with a one-pass algorithm using only constant space?"""

    def sortColors(self, nums: List[int]) -> None:
        """Dijkstra's three-way partition"""
        lo, mid, hi = 0, 0, len(nums)
        
        while mid < hi: 
            if nums[mid] < 1: 
                nums[lo], nums[mid] = nums[mid], nums[lo]
                lo, mid = lo+1, mid+1
            elif nums[mid] > 1:
                hi -= 1
                nums[mid], nums[hi] = nums[hi], nums[mid]
            else:
                mid += 1
        

    """76. Minimum Window Substring (Hard)
	Given a string S and a string T, find the minimum window in S which will 
	contain all the characters in T in complexity O(n).

	Example:
	Input: S = "ADOBECODEBANC", T = "ABC"
	Output: "BANC"
	Note:

	If there is no such window in S that covers all characters in T, return the 
	empty string "". If there is such window, you are guaranteed that there 
	will always be only one unique minimum window in S."""

    def minWindow(self, s: str, t: str) -> str:
        freq = dict()
        for c in t: freq[c] = 1 + freq.get(c, 0) #target freq table 
        
        count = ii = jj = 0
        queue, ts = deque(), set(t)
        for j, c in enumerate(s):
            if c in ts: 
                queue.append((j, c))
                freq[c] -= 1
                if freq[c] == 0: count += 1 #enough c in s
                while count == len(ts): 
                    i, c = queue.popleft()
                    if not jj or j - i < jj - ii: ii, jj = i, j+1
                    if freq[c] == 0: count -= 1 #not enough c in s
                    freq[c] += 1
        return s[ii:jj]


    """77. Combinations (Medium)
	Given two integers n and k, return all possible combinations of k numbers 
	out of 1 ... n.

	Example:
	Input: n = 4, k = 2
	Output:
	[
	  [2,4],
	  [3,4],
	  [2,3],
	  [1,2],
	  [1,3],
	  [1,4],
	]"""

    def combine(self, n: int, k: int) -> List[List[int]]:
        
        def fn(i): 
            """Populate ans using a stack"""
            if len(stack) == k: return ans.append(stack.copy())
            for ii in range(i+1, n+1): 
                stack.append(ii)
                fn(ii)
                stack.pop()
        
        ans, stack = [], []
        fn(0)
        return ans 


    """78. Subsets (Medium)
	Given a set of distinct integers, nums, return all possible subsets (the 
	power set). Note that the solution set must not contain duplicate subsets.

	Example:
	Input: nums = [1,2,3]
	Output:
	[
	  [3],
	  [1],
	  [2],
	  [1,2,3],
	  [1,3],
	  [2,3],
	  [1,2],
	  []
	]"""

    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        def fn(i):
            """Populate ans using a stack"""
            if len(nums) == i: return ans.append(stack.copy())
            fn(i+1)
            stack.append(nums[i])
            fn(i+1)
            stack.pop()
                
        ans, stack = [], []
        fn(0)
        return ans 


    """79. Word Search (Medium)
	Given a 2D board and a word, find if the word exists in the grid. The word 
	can be constructed from letters of sequentially adjacent cell, where 
	"adjacent" cells are those horizontally or vertically neighboring. The same 
	letter cell may not be used more than once.

	Example:
	board =
	[
	  ['A','B','C','E'],
	  ['S','F','C','S'],
	  ['A','D','E','E']
	]

	Given word = "ABCCED", return true.
	Given word = "SEE", return true.
	Given word = "ABCB", return false.

	Constraints:
	board and word consists only of lowercase and uppercase English letters.
	1 <= board.length <= 200
	1 <= board[i].length <= 200
	1 <= word.length <= 10^3"""

    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        
        def fn(i, j, k):
            """Return True if a series starting from (i, j) matches word[k:]"""
            if k == len(word): return True 
            if not (0 <= i < m and 0 <= j < n) or (i, j) in seen or board[i][j] != word[k]: return False 
            
            seen.add((i, j))
            ans = any(fn(i+di, j+dj, k+1) for di, dj in ((-1, 0), (0, -1), (1, 0), (0, 1)))
            seen.remove((i, j))
            return ans 
        
        seen = set()
        return any(fn(i, j, 0) for i in range(m) for j in range(n))


    """80. Remove Duplicates from Sorted Array II (Medium)
	Given a sorted array nums, remove the duplicates in-place such that 
	duplicates appeared at most twice and return the new length. Do not 
	allocate extra space for another array, you must do this by modifying the 
	input array in-place with O(1) extra memory.

	Example 1:
	Given nums = [1,1,1,2,2,3], your function should return length = 5, with 
	the first five elements of nums being 1, 1, 2, 2 and 3 respectively. It 
	doesn't matter what you leave beyond the returned length.
	
	Example 2:
	Given nums = [0,0,1,1,1,1,2,3,3], your function should return length = 7, 
	with the first seven elements of nums being modified to 0, 0, 1, 1, 2, 3 
	and 3 respectively. It doesn't matter what values are set beyond the 
	returned length.
	
	Clarification:
	Confused why the returned value is an integer but your answer is an array?
	Note that the input array is passed in by reference, which means 
	modification to the input array will be known to the caller as well.

	Internally you can think of this:
	// nums is passed in by reference. (i.e., without making a copy)
	int len = removeDuplicates(nums);

	// any modification to nums in your function would be known by the caller.
	// using the length returned by your function, it prints the first len 
	elements.
	for (int i = 0; i < len; i++) {
	    print(nums[i]);
	}"""

    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        for num in nums:
            if i < 2 or nums[i-2] < num: 
                nums[i] = num
                i += 1
        return i


    """81. Search in Rotated Sorted Array II (Medium)
	Suppose an array sorted in ascending order is rotated at some pivot unknown 
	to you beforehand. (i.e., [0,0,1,2,2,5,6] might become [2,5,6,0,0,1,2]). 
	You are given a target value to search. If found in the array return true, 
	otherwise return false.

	Example 1:
	Input: nums = [2,5,6,0,0,1,2], target = 0
	Output: true

	Example 2:
	Input: nums = [2,5,6,0,0,1,2], target = 3
	Output: false

	Follow up: This is a follow up problem to Search in Rotated Sorted Array, 
	where nums may contain duplicates. Would this affect the run-time 
	complexity? How and why?"""

    def search(self, nums: List[int], target: int) -> bool:
        
        def fn(lo, hi):
            """Return True if target is found in nums[lo:hi+1]"""
            if hi < lo: return False 
            if lo == hi: return nums[lo] == target
            
            mid = (lo + hi)//2
            if nums[mid] == target: return True
            if nums[lo] < nums[mid]: 
                if nums[lo] <= target < nums[mid]: return fn(lo, mid-1)
                else: return fn(mid+1, hi)
            elif nums[mid] < nums[hi]:
                if nums[mid] < target <= nums[hi]: return fn(mid+1, hi)
                else: return fn(lo, mid-1)
            else: #nums[lo] == nums[mid] == nums[hi]
                return fn(lo, mid-1) or fn(mid+1, hi)
        
        return fn(0, len(nums)-1)


    """82. Remove Duplicates from Sorted List II (Medium)
	Given a sorted linked list, delete all nodes that have duplicate numbers, 
	leaving only distinct numbers from the original list. Return the linked 
	list sorted as well.

	Example 1:
	Input: 1->2->3->3->4->4->5
	Output: 1->2->5

	Example 2:
	Input: 1->1->1->2->3
	Output: 2->3"""

    def deleteDuplicates(self, head: ListNode) -> ListNode:
        slow = fast = dummy = ListNode(None, head)
        prev = None
        while fast: 
            if fast.val == prev or (fast.next and fast.val == fast.next.val): 
                slow.next = fast.next
            else: 
                slow = slow.next
            prev = fast.val
            fast = fast.next
        return dummy.next 


    """83. Remove Duplicates from Sorted List (Easy)
	Given a sorted linked list, delete all duplicates such that each element 
	appear only once.

	Example 1:
	Input: 1->1->2
	Output: 1->2

	Example 2:
	Input: 1->1->2->3->3
	Output: 1->2->3"""

    def deleteDuplicates(self, head: ListNode) -> ListNode:
        slow = fast = head 
        while fast:
            if slow.val == fast.val: slow.next = fast.next
            else: slow = slow.next
            fast = fast.next 
        return head 


    """84. Largest Rectangle in Histogram (Hard)
	Given n non-negative integers representing the histogram's bar height where 
	the width of each bar is 1, find the area of largest rectangle in the 
	histogram.

	Example:
	Input: [2,1,5,6,2,3]
	Output: 10"""

    def largestRectangleArea(self, heights: List[int]) -> int:
        ans, stack = 0, [] #mono-stack (non-decreasing)
        for i in range(len(heights)+1): 
            height = heights[i] if i < len(heights) else 0
            
            while stack and heights[stack[-1]] > height: 
                h = heights[stack.pop()]
                w = i - 1 - stack[-1] if stack else i
                ans = max(ans, h*w)
            stack.append(i)
        return ans 


    """85. Maximal Rectangle (Hard)
	Given a 2D binary matrix filled with 0's and 1's, find the largest 
	rectangle containing only 1's and return its area.

	Example:
	Input:
	[
	  ["1","0","1","0","0"],
	  ["1","0","1","1","1"],
	  ["1","1","1","1","1"],
	  ["1","0","0","1","0"]
	]
	Output: 6"""

    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix: return 0
        ans, m, n = 0, len(matrix), len(matrix[0])
        height, lo, hi = [0]*n, [0]*n, [n]*n #height, lower & upper bound 
        
        for i in range(m): 
            left, right = 0, n #[left:right]
            for j in range(n): 
                if matrix[i][j] == "0": 
                    height[j] = lo[j] = 0
                    left = j+1
                else: 
                    height[j] += 1
                    lo[j] = max(lo[j], left)
                    
                if matrix[i][~j] == "0": 
                    right = n-j-1
                    hi[~j] = n
                else: 
                    hi[~j] = min(hi[~j], right)
            ans = max(ans, max(x*(z-y) for x, y, z in zip(height, lo, hi)))
        return ans 


    """86. Partition List (Medium)
	Given a linked list and a value x, partition it such that all nodes less 
	than x come before nodes greater than or equal to x. You should preserve 
	the original relative order of the nodes in each of the two partitions.

	Example:
	Input: head = 1->4->3->2->5->2, x = 3
	Output: 1->2->2->4->3->5"""

    def partition(self, head: ListNode, x: int) -> ListNode:
        dummy1 = node1 = ListNode()
        dummy2 = node2 = ListNode()
        
        while head: 
            if head.val < x: 
                node1.next = head
                node1 = node1.next
            else:
                node2.next = head
                node2 = node2.next
            head = head.next 
        node2.next = None #terminate list (no cycle)
        node1.next = dummy2.next
        return dummy1.next 


    """87. Scramble String (Hard)
	Given a string s1, we may represent it as a binary tree by partitioning it 
	to two non-empty substrings recursively. Below is one possible 
	representation of s1 = "great":

	    great
	   /    \
	  gr    eat
	 / \    /  \
	g   r  e   at
	           / \
	          a   t
	
	To scramble the string, we may choose any non-leaf node and swap its two 
	children. For example, if we choose the node "gr" and swap its two 
	children, it produces a scrambled string "rgeat".

	    rgeat
	   /    \
	  rg    eat
	 / \    /  \
	r   g  e   at
	           / \
	          a   t
	
	We say that "rgeat" is a scrambled string of "great". Similarly, if we 
	continue to swap the children of nodes "eat" and "at", it produces a 
	scrambled string "rgtae".

	    rgtae
	   /    \
	  rg    tae
	 / \    /  \
	r   g  ta  e
	       / \
	      t   a
	
	We say that "rgtae" is a scrambled string of "great". Given two strings s1 
	and s2 of the same length, determine if s2 is a scrambled string of s1.

	Example 1:
	Input: s1 = "great", s2 = "rgeat"
	Output: true

	Example 2:
	Input: s1 = "abcde", s2 = "caebd"
	Output: false"""

    def isScramble(self, s1: str, s2: str) -> bool:
        
        def fn(s1, s2):
            """Return True if s1 is a scrambled string of s2"""
            if len(s1) == 1: return s1 == s2
            if sorted(s1) != sorted(s2): return False #160ms -> 50ms
            return any(fn(s1[:i], s2[:i]) and fn(s1[i:], s2[i:]) or fn(s1[:i], s2[-i:]) and fn(s1[i:], s2[:-i]) for i in range(1, len(s1)))
        
        return fn(s1, s2)


    """88. Merge Sorted Array (Easy)
	Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as 
	one sorted array.

	Note:
	The number of elements initialized in nums1 and nums2 are m and n respectively.
	You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.

	Example:
	Input:
	nums1 = [1,2,3,0,0,0], m = 3
	nums2 = [2,5,6],       n = 3
	Output: [1,2,2,3,5,6]"""

    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        while n: 
            if m and nums1[m-1] >= nums2[n-1]: 
                nums1[m+n] = nums1[(m:=m-1)]
            else: 
                nums1[m+n] = nums2[(n:=n-1)]


    """89. Gray Code (Medium)
	The gray code is a binary numeral system where two successive values differ 
	in only one bit. Given a non-negative integer n representing the total 
	number of bits in the code, print the sequence of gray code. A gray code 
	sequence must begin with 0.

	Example 1:
	Input: 2
	Output: [0,1,3,2]
	Explanation:
	00 - 0
	01 - 1
	11 - 3
	10 - 2

	For a given n, a gray code sequence may not be uniquely defined. For 
	example, [0,2,3,1] is also a valid gray code sequence.

	00 - 0
	10 - 2
	11 - 3
	01 - 1
	
	Example 2:
	Input: 0
	Output: [0]
	Explanation: We define the gray code sequence to begin with 0. A gray code 
	sequence of n has size = 2n, which for n = 0 the size is 20 = 1. Therefore, 
	for n = 0 the gray code sequence is [0]."""

    def grayCode(self, n: int) -> List[int]:
        return [i ^ (i>>1) for i in range(1 << n)]


    """90. Subsets II (Medium)
	Given a collection of integers that might contain duplicates, nums, return 
	all possible subsets (the power set). Note that the solution set must not 
	contain duplicate subsets.

	Example:
	Input: [1,2,2]
	Output:
	[
	  [2],
	  [1],
	  [1,2,2],
	  [2,2],
	  [1,2],
	  []
	]"""

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        def fn(i):
            """Populate ans using a stack"""
            if len(nums) == i: return ans.append(stack.copy())
            if not stack or nums[i] != stack[-1]: fn(i+1)
            stack.append(nums[i])
            fn(i+1)
            stack.pop()
            
        nums.sort()
        ans, stack = [], []
        fn(0)
        return ans 


    """91. Decode Ways (Medium)
	A message containing letters from A-Z is being encoded to numbers using the 
	following mapping:

	'A' -> 1
	'B' -> 2
	...
	'Z' -> 26
	
	Given a non-empty string containing only digits, determine the total number 
	of ways to decode it.

	Example 1:
	Input: "12"
	Output: 2
	Explanation: It could be decoded as "AB" (1 2) or "L" (12).

	Example 2:
	Input: "226"
	Output: 3
	Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6)."""

    def numDecodings(self, s: str) -> int:
        
        @lru_cache(None)
        def fn(i): 
            """Return decode ways of s[i:]"""
            if i >= len(s): return i == len(s) #boundary condition
            return 0 if s[i] == "0" else fn(i+1) + (int(s[i:i+2]) <= 26)*fn(i+2)
            
        return fn(0)



    """92. Reverse Linked List II (Medium)
	Reverse a linked list from position m to n. Do it in one-pass. Note: 
	1 ≤ m ≤ n ≤ length of list.

	Example:
	Input: 1->2->3->4->5->NULL, m = 2, n = 4
	Output: 1->4->3->2->5->NULL"""

    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        dummy = node = ListNode(next=head)
        for _ in range(m-1): node = node.next 
            
        prev, curr = None, node.next 
        for _ in range(m, n+1): curr.next, curr, prev = prev, curr.next, curr
            
        node.next.next = curr
        node.next = prev
        
        return dummy.next 


    """93. Restore IP Addresses (Medium)
	Given a string containing only digits, restore it by returning all possible 
	valid IP address combinations. A valid IP address consists of exactly four 
	integers (each integer is between 0 and 255) separated by single points.

	Example:
	Input: "25525511135"
	Output: ["255.255.11.135", "255.255.111.35"]"""

    def restoreIpAddresses(self, s: str) -> List[str]:
        
        def fn(i, n): 
            """Populate ans with a stack through backtracking"""
            if not (n <= len(s)-i <= 3*n): return 
            if i == len(s): return ans.append(".".join(stack))
            k = i+1 if s[i] == "0" else i+3
            for j in range(i+1, min(k, len(s))+1): 
                if j == i+3 and s[i:j] > "255": continue
                stack.append(s[i:j])
                fn(j, n-1)
                stack.pop()
            
        ans, stack = [], []
        fn(0, 4)
        return ans 


    """94. Binary Tree Inorder Traversal (Medium)
	Given a binary tree, return the inorder traversal of its nodes' values.

	Example:
	Input: [1,null,2,3]
	   1
	    \
	     2
	    /
	   3

	Output: [1,3,2]"""

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        ans, stack = [], []
        node = root
        while stack or node:
            if node: 
                stack.append(node)
                node = node.left
                continue
            node = stack.pop()
            ans.append(node.val)
            node = node.right
        return ans 


    """95. Unique Binary Search Trees II (Medium)
	Given an integer n, generate all structurally unique BST's (binary search 
	trees) that store values 1 ... n.

	Example:
	Input: 3
	Output:
	[
	  [1,null,3,2],
	  [3,2,null,1],
	  [3,1,null,null,2],
	  [2,1,3],
	  [1,null,2,null,3]
	]
	Explanation:
	The above output corresponds to the 5 unique BST's shown below:

	   1         3     3      2      1
	    \       /     /      / \      \
	     3     2     1      1   3      2
	    /     /       \                 \
	   2     1         2                 3
	 
	Constraints: 0 <= n <= 8"""

    def generateTrees(self, n: int) -> List[TreeNode]:
        
        @lru_cache(None)
        def fn(lo, hi): 
            """Return structurally uniq BST using numbers from lo (inclusive) to hi (exclusive)"""
            if lo == hi: return [None]
            ans = []
            for i in range(lo, hi):
                for left in fn(lo, i):
                    for right in fn(i+1, hi): 
                        ans.append(TreeNode(i, left, right))
            return ans 
        
        return fn(1, n+1) if n else []


    """96. Unique Binary Search Trees (Medium)
	Given n, how many structurally unique BST's (binary search trees) that 
	store values 1 ... n?

	Example:
	Input: 3
	Output: 5
	Explanation:
	Given n = 3, there are a total of 5 unique BST's:

	   1         3     3      2      1
	    \       /     /      / \      \
	     3     2     1      1   3      2
	    /     /       \                 \
	   2     1         2                 3"""

    def numTrees(self, n: int) -> int:
        
        @lru_cache(None)
        def fn(n):
            """Return Catalan number in recursive form"""
            if n == 0: return 1
            return sum(fn(i)*fn(n-i-1) for i in range(n))
        
        return fn(n)


    """97. Interleaving String (Hard)
	Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and 
	s2.

	Example 1:
	Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
	Output: true

	Example 2:
	Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
	Output: false"""

    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
        @lru_cache(None)
        def fn(i, j): 
            """Return True if s3[i+j:] is formed by interleaving s1[i:] and s2[j:]"""
            if i == len(s1) and j == len(s2): return True
            ans = False
            if i < len(s1) and s1[i] == s3[i+j]: ans = ans or fn(i+1, j)
            if j < len(s2) and s2[j] == s3[i+j]: ans = ans or fn(i, j+1)
            return ans 
        
        if len(s1) + len(s2) != len(s3): return False 
        return fn(0, 0)


    """98. Validate Binary Search Tree (Medium)
	Given a binary tree, determine if it is a valid binary search tree (BST). 
	Assume a BST is defined as follows: The left subtree of a node contains 
	only nodes with keys less than the node's key. The right subtree of a node 
	contains only nodes with keys greater than the node's key. Both the left 
	and right subtrees must also be binary search trees.

	Example 1:

	    2
	   / \
	  1   3

	Input: [2,1,3]
	Output: true

	Example 2:

	    5
	   / \
	  1   4
	     / \
	    3   6

	Input: [5,1,4,null,null,3,6]
	Output: false
	Explanation: The root node's value is 5 but its right child's value is 4."""

    def isValidBST(self, root: TreeNode) -> bool:
         
        def fn(node, lo=-inf, hi=inf):
            """Return True if tree rooted at node is a valid BST bounded between lo and hi"""
            if not node: return True
            return fn(node.left, lo, node.val) and lo < node.val < hi and fn(node.right, node.val, hi)
        
        return fn(root)


    """99. Recover Binary Search Tree (Hard)
	Two elements of a binary search tree (BST) are swapped by mistake. Recover 
	the tree without changing its structure.

	Example 1:
	Input: [1,3,null,null,2]

	   1
	  /
	 3
	  \
	   2

	Output: [3,1,null,null,2]

	   3
	  /
	 1
	  \
	   2

	Example 2:
	Input: [3,1,4,null,null,2]

	  3
	 / \
	1   4
	   /
	  2

	Output: [2,1,4,null,null,3]

	  2
	 / \
	1   4
	   /
	  3

	Follow up:
	A solution using O(n) space is pretty straight forward.
	Could you devise a constant space solution?"""

    def recoverTree(self, root: TreeNode) -> None:
        node, stack = root, []
        prev = lo = hi = None
        while stack or node:
            if node:
                stack.append(node)
                node = node.left
                continue
            node = stack.pop()
            if prev and prev.val > node.val:
                if not lo: lo, hi = prev, node
                else: hi = node
            prev = node
            node = node.right 
        lo.val, hi.val = hi.val, lo.val 


    """100. Same Tree (Easy)
	Given two binary trees, write a function to check if they are the same or 
	not. Two binary trees are considered the same if they are structurally 
	identical and the nodes have the same value.

	Example 1:
	Input:     1         1
	          / \       / \
	         2   3     2   3

	        [1,2,3],   [1,2,3]

	Output: true

	Example 2:
	Input:     1         1
	          /           \
	         2             2

	        [1,2],     [1,null,2]

	Output: false

	Example 3:
	Input:     1         1
	          / \       / \
	         2   1     1   2

	        [1,2,1],   [1,1,2]

	Output: false"""

    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        
        def fn(p, q): 
            """Return True if trees rooted at p and q are structurally identical"""
            if not p or not q: return p is q
            return fn(p.left, q.left) and p.val == q.val and fn(p.right, q.right)
        
        return fn(p, q)


    """101. Symmetric Tree (Easy)
	Given a binary tree, check whether it is a mirror of itself (ie, symmetric 
	around its center). For example, this binary tree [1,2,2,3,4,4,3] is 
	symmetric:

	    1
	   / \
	  2   2
	 / \ / \
	3  4 4  3

	But the following [1,2,2,null,3,null,3] is not:

	    1
	   / \
	  2   2
	   \   \
	   3    3

	Follow up: Solve it both recursively and iteratively."""

    def isSymmetric(self, root: TreeNode) -> bool:
        
        def fn(m, n):
            """Return True if subtrees rooted at m and n are symmetric"""
            if not m or not n: return m is n
            return fn(m.left, n.right) and m.val == n.val and fn(m.right, n.left)
        
        return fn(root, root)


    """102. Binary Tree Level Order Traversal (Medium)
	Given a binary tree, return the level order traversal of its nodes' values. 
	(ie, from left to right, level by level).

	For example:
	Given binary tree [3,9,20,null,null,15,7],
	    3
	   / \
	  9  20
	    /  \
	   15   7
	return its level order traversal as:
	[
	  [3],
	  [9,20],
	  [15,7]
	]"""

    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        ans, queue = [], [root]
        while queue: 
            tmp, val = [], []
            for node in queue: 
                if node: 
                    val.append(node.val)
                    tmp.extend([node.left, node.right])
            if val: ans.append(val)
            queue = tmp 
        return ans 


    """103. Binary Tree Zigzag Level Order Traversal (Medium)
	Given a binary tree, return the zigzag level order traversal of its nodes' 
	values. (ie, from left to right, then right to left for the next level and 
	alternate between).

	For example:
	Given binary tree [3,9,20,null,null,15,7],
	    3
	   / \
	  9  20
	    /  \
	   15   7
	return its zigzag level order traversal as:
	[
	  [3],
	  [20,9],
	  [15,7]
	]"""

    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        ans, queue = [], [root]
        stride = 1
        while queue: 
            tmp, val = [], []
            for node in queue: 
                if node: 
                    val.append(node.val)
                    tmp.extend([node.left, node.right])
            if val: ans.append(val[::stride])
            stride *= -1
            queue = tmp
        return ans 


    """104. Maximum Depth of Binary Tree (Easy)
	Given a binary tree, find its maximum depth. The maximum depth is the 
	number of nodes along the longest path from the root node down to the 
	farthest leaf node. Note that a leaf is a node with no children.

	Example:
	Given binary tree [3,9,20,null,null,15,7],

	    3
	   / \
	  9  20
	    /  \
	   15   7"""

    def maxDepth(self, root: TreeNode) -> int:
        
        def fn(node):
            """Return depth of BST at given node"""
            if not node: return 0
            return 1 + max(fn(node.left), fn(node.right))
        
        return fn(root)


    """105. Construct Binary Tree from Preorder and Inorder Traversal (Medium)
	Given preorder and inorder traversal of a tree, construct the binary tree.

	Note: You may assume that duplicates do not exist in the tree.

	For example, given
	preorder = [3,9,20,15,7]
	inorder = [9,3,15,20,7]
	Return the following binary tree:

	    3
	   / \
	  9  20
	    /  \
	   15   7"""

    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        mp = {x: i for i, x in enumerate(inorder)} # relative position 
        stack = []
        root = None
        for x in preorder: 
            if not root: root = node = TreeNode(x)
            elif mp[x] < mp[stack[-1].val]: stack[-1].left = node = TreeNode(x)
            else: 
                while stack and mp[stack[-1].val] < mp[x]: node = stack.pop() # retrace 
                node.right = node = TreeNode(x)
            stack.append(node)
        return root


    """106. Construct Binary Tree from Inorder and Postorder Traversal (Medium)
	Given inorder and postorder traversal of a tree, construct the binary tree.

	Note that you may assume that duplicates do not exist in the tree.

	For example, given inorder = [9,3,15,20,7] and postorder = [9,15,7,20,3], 
	return the following binary tree:

	    3
	   / \
	  9  20
	    /  \
	   15   7"""

    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        mp = {x: i for i, x in enumerate(inorder)} # relative position 
        
        root = None
        stack = []
        for x in reversed(postorder): 
            if not root: root = node = TreeNode(x)
            elif mp[x] > mp[stack[-1].val]: stack[-1].right = node = TreeNode(x)
            else: 
                while stack and mp[stack[-1].val] > mp[x]: node = stack.pop() # retrace 
                node.left = node = TreeNode(x)
            stack.append(node)
        return root 


    """107. Binary Tree Level Order Traversal II (Easy)
	Given a binary tree, return the bottom-up level order traversal of its 
	nodes' values. (ie, from left to right, level by level from leaf to root).

	For example:
	Given binary tree [3,9,20,null,null,15,7],
	    3
	   / \
	  9  20
	    /  \
	   15   7
	return its bottom-up level order traversal as:
	[
	  [15,7],
	  [9,20],
	  [3]
	]"""

    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        ans, queue = [], [root]
        while queue: 
            tmp, val = [], []
            for node in queue: 
                if node: 
                    val.append(node.val)
                    tmp.extend([node.left, node.right])
            if val: ans.append(val)
            queue = tmp
        return ans[::-1]


    """108. Convert Sorted Array to Binary Search Tree (Easy)
	Given an array where elements are sorted in ascending order, convert it to 
	a height balanced BST. For this problem, a height-balanced binary tree is 
	defined as a binary tree in which the depth of the two subtrees of every 
	node never differ by more than 1.

	Example:
	Given the sorted array: [-10,-3,0,5,9], one possible answer is: 
	[0,-3,9,-10,null,5], which represents the following height balanced BST:

	      0
	     / \
	   -3   9
	   /   /
	 -10  5"""

    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        
        def fn(lo, hi):
            """Return BST using nums[lo:hi]"""
            if lo == hi: return None
            mid = (lo + hi)//2
            return TreeNode(nums[mid], fn(lo, mid), fn(mid+1, hi))
        
        return fn(0, len(nums))


    """109. Convert Sorted List to Binary Search Tree (Medium)
	Given a singly linked list where elements are sorted in ascending order, 
	convert it to a height balanced BST. For this problem, a height-balanced 
	binary tree is defined as a binary tree in which the depth of the two 
	subtrees of every node never differ by more than 1.

	Example:
	Given the sorted linked list: [-10,-3,0,5,9], one possible answer is: 
	[0,-3,9,-10,null,5], which represents the following height balanced BST:

	      0
	     / \
	   -3   9
	   /   /
	 -10  5"""

    def sortedListToBST(self, head: ListNode) -> TreeNode:
        node, n = head, 0
        while node: node, n = node.next, n+1
            
        def fn(lo, hi, node): 
            """Return root of tree using nodes from lo (inclusive) to hi (exclusive)"""
            if lo == hi: return None, node
            mid = (lo + hi)//2
            left, node = fn(lo, mid, node)
            ans = TreeNode(node.val, left=left)
            node = node.next
            ans.right, node = fn(mid+1, hi, node)
            return ans, node
        
        return fn(0, n, head)[0]


    """110. Balanced Binary Tree (Easy)
	Given a binary tree, determine if it is height-balanced. For this problem, 
	a height-balanced binary tree is defined as: a binary tree in which the 
	left and right subtrees of every node differ in height by no more than 1.

	Example 1:
	Given the following tree [3,9,20,null,null,15,7]:

	    3
	   / \
	  9  20
	    /  \
	   15   7
	Return true.

	Example 2:
	Given the following tree [1,2,2,3,3,null,null,4,4]:

	       1
	      / \
	     2   2
	    / \
	   3   3
	  / \
	 4   4
	Return false."""

    def isBalanced(self, root: TreeNode) -> bool:
        
        def fn(node):
            """Return flag of balance and height of given node"""
            if not node: return True, 0
            tf0, h0 = fn(node.left)
            tf1, h1 = fn(node.right)
            return tf0 and tf1 and abs(h0-h1) <= 1, 1 + max(h0, h1)
        
        return fn(root)[0]


    """111. Minimum Depth of Binary Tree (Easy)
	Given a binary tree, find its minimum depth. The minimum depth is the 
	number of nodes along the shortest path from the root node down to the 
	nearest leaf node. Note that a leaf is a node with no children.

	Example:
	Given binary tree [3,9,20,null,null,15,7],

	    3
	   / \
	  9  20
	    /  \
	   15   7
	return its minimum depth = 2."""

    def minDepth(self, root: TreeNode) -> int:
        
        def fn(node):
            """Return minimum depth of given node"""
            if not node: return 0
            if not node.left or not node.right: return 1 + fn(node.left) + fn(node.right)
            return 1 + min(fn(node.left), fn(node.right))
        
        return fn(root)


    """112. Path Sum (Easy)
	Given a binary tree and a sum, determine if the tree has a root-to-leaf 
	path such that adding up all the values along the path equals the given 
	sum. Note that a leaf is a node with no children.

	Example:
	Given the below binary tree and sum = 22,

	      5
	     / \
	    4   8
	   /   / \
	  11  13  4
	 /  \      \
	7    2      1
	return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22."""

    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        
        def fn(node, x): 
            """Return True if node is on root-to-leaf path"""
            if not node: return False 
            if not node.left and not node.right: return node.val == x
            return fn(node.left, x-node.val) or fn(node.right, x-node.val)
        
        return fn(root, sum)


    """113. Path Sum II (Medium)
	Given a binary tree and a sum, find all root-to-leaf paths where each 
	path's sum equals the given sum. Note that a leaf is a node with no 
	children.

	Example:
	Given the below binary tree and sum = 22,

	      5
	     / \
	    4   8
	   /   / \
	  11  13  4
	 /  \    / \
	7    2  5   1
	Return:

	[
	   [5,4,11,2],
	   [5,8,4,5]
	]"""

    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        
        def fn(node, x): 
            """Populate ans with a stack"""
            if not node: return 
            stack.append(node.val)
            if not node.left and not node.right and node.val == x: ans.append(stack.copy())
            fn(node.left, x-node.val) or fn(node.right, x-node.val)
            stack.pop()
            
        ans, stack = [], []
        fn(root, sum)
        return ans 


    """114. Flatten Binary Tree to Linked List (Medium)
	Given a binary tree, flatten it to a linked list in-place.

	For example, given the following tree:

	    1
	   / \
	  2   5
	 / \   \
	3   4   6

	The flattened tree should look like:

	1
	 \
	  2
	   \
	    3
	     \
	      4
	       \
	        5
	         \
	          6"""

    def flatten(self, root: TreeNode) -> None:
        
        def fn(node, tail=None):
            """Return head of flattened binary tree"""
            if not node: return tail
            node.left, node.right = None, fn(node.left, fn(node.right, tail))
            return node
        
        return fn(root)


    """115. Distinct Subsequences (Hard)
	Given a string S and a string T, count the number of distinct subsequences 
	of S which equals T. A subsequence of a string is a new string which is 
	formed from the original string by deleting some (can be none) of the 
	characters without disturbing the relative positions of the remaining 
	characters. (ie, "ACE" is a subsequence of "ABCDE" while "AEC" is not). 
	It's guaranteed the answer fits on a 32-bit signed integer.

	Example 1:
	Input: S = "rabbbit", T = "rabbit"
	Output: 3
	Explanation:
	As shown below, there are 3 ways you can generate "rabbit" from S.
	(The caret symbol ^ means the chosen letters)

	rabbbit
	^^^^ ^^
	rabbbit
	^^ ^^^^
	rabbbit
	^^^ ^^^

	Example 2:
	Input: S = "babgbag", T = "bag"
	Output: 5
	Explanation:
	As shown below, there are 5 ways you can generate "bag" from S.
	(The caret symbol ^ means the chosen letters)

	babgbag
	^^ ^
	babgbag
	^^    ^
	babgbag
	^    ^^
	babgbag
	  ^  ^^
	babgbag
	    ^^^"""

    def numDistinct(self, s: str, t: str) -> int:
        pos = dict()
        for i, c in enumerate(t): pos.setdefault(c, []).append(i)
            
        ans = [0]*len(t) + [1]
        for c in reversed(s):
            for i in pos.get(c, []):
                ans[i] += ans[i+1]
        return ans[0]


    """116. Populating Next Right Pointers in Each Node (Medium)
	You are given a perfect binary tree where all leaves are on the same 
	level, and every parent has two children. The binary tree has the 
	following definition:

	struct Node {
	  int val;
	  Node *left;
	  Node *right;
	  Node *next;
	}

	Populate each next pointer to point to its next right node. If there is no 
	next right node, the next pointer should be set to NULL. Initially, all 
	next pointers are set to NULL.

	Follow up:
	You may only use constant extra space.
	Recursive approach is fine, you may assume implicit stack space does not 
	count as extra space for this problem.

	Example 1:
	Input: root = [1,2,3,4,5,6,7]
	Output: [1,#,2,3,#,4,5,6,7,#]
	Explanation: Given the above perfect binary tree (Figure A), your function 
	should populate each next pointer to point to its next right node, just 
	like in Figure B. The serialized output is in level order as connected by 
	the next pointers, with '#' signifying the end of each level.

	Constraints:
	The number of nodes in the given tree is less than 4096.
	-1000 <= node.val <= 1000"""

    def connect(self, root: 'Node') -> 'Node':
        head = root
        while head and head.left: 
            node = head
            while node: 
                node.left.next = node.right
                if node.next: node.right.next = node.next.left
                node = node.next
            head = head.left
        return root 


    """117. Populating Next Right Pointers in Each Node II (Medium)
	Given a binary tree

	struct Node {
	  int val;
	  Node *left;
	  Node *right;
	  Node *next;
	}

	Populate each next pointer to point to its next right node. If there is no 
	next right node, the next pointer should be set to NULL. Initially, all 
	next pointers are set to NULL.

	Follow up:
	You may only use constant extra space. Recursive approach is fine, you may 
	assume implicit stack space does not count as extra space for this problem.

	Example 1:
	Input: root = [1,2,3,4,5,null,7]
	Output: [1,#,2,3,#,4,5,7,#]
	Explanation: Given the above binary tree (Figure A), your function should 
	populate each next pointer to point to its next right node, just like in 
	Figure B. The serialized output is in level order as connected by the next 
	pointers, with '#' signifying the end of each level.

	Constraints:
	The number of nodes in the given tree is less than 6000.
	-100 <= node.val <= 100"""

    def connect(self, root: 'Node') -> 'Node':
        parent = root
        while parent:
            child = dummy = Node()
            while parent: 
                if parent.left: child.next = child = parent.left
                if parent.right: child.next = child = parent.right
                parent = parent.next 
            parent = dummy.next 
        return root 


    """118. Pascal's Triangle (Easy)
	Given a non-negative integer numRows, generate the first numRows of 
	Pascal's triangle. In Pascal's triangle, each number is the sum of the two 
	numbers directly above it.

	Example:
	Input: 5
	Output:
	[
	     [1],
	    [1,1],
	   [1,2,1],
	  [1,3,3,1],
	 [1,4,6,4,1]
	]"""

    def generate(self, numRows: int) -> List[List[int]]:
        ans, row = [], []
        for i in range(numRows): 
            row.append(1)
            for j in range(i-1, 0, -1): row[j] += row[j-1]
            ans.append(row.copy())
        return ans


    """119. Pascal's Triangle II (Easy)
	Given a non-negative index k where k ≤ 33, return the kth index row of the 
	Pascal's triangle. Note that the row index starts from 0. In Pascal's 
	triangle, each number is the sum of the two numbers directly above it.

	Example:
	Input: 3
	Output: [1,3,3,1]

	Follow up: Could you optimize your algorithm to use only O(k) extra space?"""

    def getRow(self, rowIndex: int) -> List[int]:
        ans = [1]
        for i in range(rowIndex): #n choose k 
            ans.append(ans[-1]*(rowIndex-i)//(i+1))
        return ans 


    """120. Triangle (Medium)
	Given a triangle, find the minimum path sum from top to bottom. Each step 
	you may move to adjacent numbers on the row below. For example, given the 
	following triangle

	[
	     [2],
	    [3,4],
	   [6,5,7],
	  [4,1,8,3]
	]

	The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

	Note: Bonus point if you are able to do this using only O(n) extra space, 
	where n is the total number of rows in the triangle."""

    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        @lru_cache(None)
        def fn(i, j):
            """Return minimum path sum ending at (i, j)"""
            if i < 0: return 0
            if j < 0 or j > i: return inf
            return triangle[i][j] + min(fn(i-1, j-1), fn(i-1, j))
        
        m = len(triangle)
        return min(fn(m-1, j) for j in range(m))



    """121. Best Time to Buy and Sell Stock (Easy)
	Say you have an array for which the ith element is the price of a given 
	stock on day i. If you were only permitted to complete at most one 
	transaction (i.e., buy one and sell one share of the stock), design an 
	algorithm to find the maximum profit. Note that you cannot sell a stock 
	before you buy one.

	Example 1:
	Input: [7,1,5,3,6,4]
	Output: 5
	Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
	             Not 7-1 = 6, as selling price needs to be larger than buying price.

	Example 2:
	Input: [7,6,4,3,1]
	Output: 0
	Explanation: In this case, no transaction is done, i.e. max profit = 0."""

    def maxProfit(self, prices: List[int]) -> int:
        buy, pnl = inf, 0
        for price in prices:
            buy = min(buy, price)
            pnl = max(pnl, price - buy)
        return pnl 


    """122. Best Time to Buy and Sell Stock II (Easy)
	Say you have an array prices for which the ith element is the price of a 
	given stock on day i. Design an algorithm to find the maximum profit. You 
	may complete as many transactions as you like (i.e., buy one and sell one 
	share of the stock multiple times). Note: You may not engage in multiple 
	transactions at the same time (i.e., you must sell the stock before you buy 
	again).

	Example 1:
	Input: [7,1,5,3,6,4]
	Output: 7
	Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
	             Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.

	Example 2:
	Input: [1,2,3,4,5]
	Output: 4
	Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
	             Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
	             engaging multiple transactions at the same time. You must sell before buying again.

	Example 3:
	Input: [7,6,4,3,1]
	Output: 0
	Explanation: In this case, no transaction is done, i.e. max profit = 0.

	Constraints:
	1 <= prices.length <= 3 * 10 ^ 4
	0 <= prices[i] <= 10 ^ 4"""

    def maxProfit(self, prices: List[int]) -> int:
        return sum(max(0, prices[i] - prices[i-1]) for i in range(1, len(prices))) 



    """123. Best Time to Buy and Sell Stock III (Hard)
	Say you have an array for which the ith element is the price of a given 
	stock on day i. Design an algorithm to find the maximum profit. You may 
	complete at most two transactions. Note that you may not engage in multiple 
	transactions at the same time (i.e., you must sell the stock before you buy 
	again).

	Example 1:
	Input: [3,3,5,0,0,3,1,4]
	Output: 6
	Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
	             Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.

	Example 2:
	Input: [1,2,3,4,5]
	Output: 4
	Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
	             Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
	             engaging multiple transactions at the same time. You must sell before buying again.

	Example 3:
	Input: [7,6,4,3,1]
	Output: 0
	Explanation: In this case, no transaction is done, i.e. max profit = 0."""

    def maxProfit(self, prices: List[int]) -> int:
        buy, pnl = [inf]*2, [0]*2
        for price in prices: 
            buy[0] = min(buy[0], price)
            pnl[0] = max(pnl[0], price - buy[0])
            buy[1] = min(buy[1], price - pnl[0])
            pnl[1] = max(pnl[1], price - buy[1])
        return pnl[1]


    """124. Binary Tree Maximum Path Sum (Hard)
	Given a non-empty binary tree, find the maximum path sum. For this problem, 
	a path is defined as any sequence of nodes from some starting node to any 
	node in the tree along the parent-child connections. The path must contain 
	at least one node and does not need to go through the root.

	Example 1:
	Input: [1,2,3]

	       1
	      / \
	     2   3

	Output: 6

	Example 2:
	Input: [-10,9,20,null,null,15,7]

	   -10
	   / \
	  9  20
	    /  \
	   15   7

	Output: 42"""

    def maxPathSum(self, root: TreeNode) -> int:
        
        def fn(node): 
            """Return path sum ending at node and maximum path sum seen so far"""
            if not node: return 0, -inf
            lh, lps = fn(node.left)
            rh, rps = fn(node.right)
            return node.val + max(0, lh, rh), max(lps, rps, node.val + max(0, lh) + max(0, rh))
        
        return fn(root)[1]


    """125. Valid Palindrome (Easy)
	Given a string, determine if it is a palindrome, considering only 
	alphanumeric characters and ignoring cases. Note that for the purpose of 
	this problem, we define empty string as valid palindrome.

	Example 1:
	Input: "A man, a plan, a canal: Panama"
	Output: true

	Example 2:
	Input: "race a car"
	Output: false"""

    def isPalindrome(self, s: str) -> bool:
        s = "".join(c for c in s.lower() if c.isalnum())
        return s == s[::-1]


    """126. Word Ladder II (Hard)
	Given two words (beginWord and endWord), and a dictionary's word list, find 
	all shortest transformation sequence(s) from beginWord to endWord, such 
	that:
	1) Only one letter can be changed at a time
	2) Each transformed word must exist in the word list. Note that beginWord 
	is not a transformed word.
	
	Note:
	* Return an empty list if there is no such transformation sequence.
	* All words have the same length.
	* All words contain only lowercase alphabetic characters.
	* You may assume no duplicates in the word list.
	* You may assume beginWord and endWord are non-empty and are not the same.
	
	Example 1:
	Input:
	beginWord = "hit",
	endWord = "cog",
	wordList = ["hot","dot","dog","lot","log","cog"]

	Output:
	[
	  ["hit","hot","dot","dog","cog"],
	  ["hit","hot","lot","log","cog"]
	]
	
	Example 2:
	Input:
	beginWord = "hit"
	endWord = "cog"
	wordList = ["hot","dot","dog","lot","log"]

	Output: []

	Explanation: The endWord "cog" is not in wordList, therefore no possible 
	transformation."""

    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if endWord not in wordList: return []
        
        graph = dict()
        for word in wordList:
            for i in range(len(word)):
                graph.setdefault(word[:i] + "*" + word[i+1:], []).append(word)
                
        ans = []
        front0, front1 = {beginWord: [[beginWord]]}, {endWord:[[endWord]]} #word & sequences ending in word
        seen = {beginWord, endWord}
        reverse = False 
        
        while front0 and front1 and not ans:
            if len(front0) > len(front1): front0, front1, reverse = front1, front0, not reverse 
            temp = dict()
            for word, seq in front0.items(): 
                for i in range(len(word)): 
                    for node in graph.get(word[:i] + "*" + word[i+1:], []): 
                        if node in front1: 
                            ans.extend([y + x[::-1] if reverse else x + y[::-1] for x in seq for y in front1[node]])
                        if node in seen: continue
                        for x in seq: 
                            temp.setdefault(node, []).append(x + [node])
            seen |= set(temp.keys()) #has to be updated level-by-level
            front0 = temp 
        return ans 


    """127. Word Ladder (Medium)
	Given two words (beginWord and endWord), and a dictionary's word list, 
	find the length of shortest transformation sequence from beginWord to 
	endWord, such that:
	1) Only one letter can be changed at a time.
	2) Each transformed word must exist in the word list.
	
	Note:
	* Return 0 if there is no such transformation sequence.
	* All words have the same length.
	* All words contain only lowercase alphabetic characters.
	* You may assume no duplicates in the word list.
	* You may assume beginWord and endWord are non-empty and are not the same.
	
	Example 1:
	Input:
	beginWord = "hit",
	endWord = "cog",
	wordList = ["hot","dot","dog","lot","log","cog"]

	Output: 5
	Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> 
	"dog" -> "cog", return its length 5.

	Example 2:
	Input:
	beginWord = "hit"
	endWord = "cog"
	wordList = ["hot","dot","dog","lot","log"]

	Output: 0
	Explanation: The endWord "cog" is not in wordList, therefore no possible 
	transformation."""

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList: return 0 #shortcut 
        
        graph = dict()
        for word in wordList: 
            for i in range(len(word)):
                graph.setdefault(word[:i] + "*" + word[i+1:], []).append(word)
        
        #two-end bfs
        front0, front1 = {beginWord}, {endWord}
        seen = {beginWord, endWord}
        
        ans = 1
        while front0 and front1: 
            ans += 1
            if len(front0) > len(front1): front0, front1 = front1, front0
            #move forward frontier
            temp = set()
            for word in front0: 
                for i in range(len(word)):
                    for node in graph.get(word[:i] + "*" + word[i+1:], []):
                        if node in front1: return ans 
                        if node in seen: continue
                        temp.add(node)
                        seen.add(node)
            front0 = temp
        return 0


    """128. Longest Consecutive Sequence (Hard)
	Given an unsorted array of integers, find the length of the longest 
	consecutive elements sequence. Your algorithm should run in O(n) complexity.

	Example:
	Input: [100, 4, 200, 1, 3, 2]
	Output: 4
	Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. 
	Therefore its length is 4."""

    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        ans = val = 0
        for x in nums: 
            if x-1 not in nums: 
                val = 0
                while x in nums: val, x = val+1, x+1
            ans = max(ans, val)
        return ans 


    """129. Sum Root to Leaf Numbers (Medium)
	Given a binary tree containing digits from 0-9 only, each root-to-leaf path 
	could represent a number. An example is the root-to-leaf path 1->2->3 which 
	represents the number 123. Find the total sum of all root-to-leaf numbers.
	Note that a leaf is a node with no children.

	Example:
	Input: [1,2,3]
	    1
	   / \
	  2   3
	Output: 25
	Explanation:
	The root-to-leaf path 1->2 represents the number 12.
	The root-to-leaf path 1->3 represents the number 13.
	Therefore, sum = 12 + 13 = 25.

	Example 2:
	Input: [4,9,0,5,1]
	    4
	   / \
	  9   0
	 / \
	5   1
	Output: 1026
	Explanation:
	The root-to-leaf path 4->9->5 represents the number 495.
	The root-to-leaf path 4->9->1 represents the number 491.
	The root-to-leaf path 4->0 represents the number 40.
	Therefore, sum = 495 + 491 + 40 = 1026."""

    def sumNumbers(self, root: TreeNode) -> int:
        
        def fn(node, val):
            """Return sum of node-to-leaf numbers"""
            if not node: return 0
            val = 10*val + node.val
            if not node.left and not node.right: return val 
            return fn(node.left, val) + fn(node.right, val)
            
        return fn(root, 0)


    """130. Surrounded Regions (Medium)
	Given a 2D board containing 'X' and 'O' (the letter O), capture all regions 
	surrounded by 'X'. A region is captured by flipping all 'O's into 'X's in 
	that surrounded region.

	Example:
	X X X X
	X O O X
	X X O X
	X O X X
	After running your function, the board should be:

	X X X X
	X X X X
	X X X X
	X O X X

	Explanation:
	Surrounded regions shouldn’t be on the border, which means that any 'O' on 
	the border of the board are not flipped to 'X'. Any 'O' that is not on the 
	border and it is not connected to an 'O' on the border will be flipped to 
	'X'. Two cells are connected if they are adjacent cells connected 
	horizontally or vertically."""

    def solve(self, board: List[List[str]]) -> None:
        if not board: return [] #edge case 
        m, n = len(board), len(board[0])
        
        def fn(i, j):
            """Flood fill "O" with sentinel"""
            if not (0 <= i < m and 0 <= j < n) or board[i][j] != "O": return 
            board[i][j] = "#" #sentinel 
            for ii, jj in (i-1, j), (i, j-1), (i, j+1), (i+1, j): fn(ii, jj)
        
        for i in range(m): fn(i, 0) or fn(i, n-1)
        for j in range(n): fn(0, j) or fn(m-1, j)
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == "O": board[i][j] = "X"
                if board[i][j] == "#": board[i][j] = "O"


    """131. Palindrome Partitioning (Medium)
	Given a string s, partition s such that every substring of the partition 
	is a palindrome. Return all possible palindrome partitioning of s.

	Example:
	Input: "aab"
	Output:
	[
	  ["aa","b"],
	  ["a","a","b"]
	]"""

    def partition(self, s: str) -> List[List[str]]:
        #pre-processing 
        palin = dict()
        for k in range(len(s)):
            for i, j in (k, k), (k, k+1):
                while 0 <= i and j < len(s) and s[i] == s[j]: 
                    palin.setdefault(i, []).append(j)
                    i, j = i-1, j+1
        
        @lru_cache(None)
        def fn(i): 
            """Return palindrome partitioning of s[i:]"""
            if i == len(s): return [[]] 
            return [[s[i:ii+1]] + y for ii in palin[i] for y in fn(ii+1)]
        
        return fn(0)


    """132. Palindrome Partitioning II (Hard)
	Given a string s, partition s such that every substring of the partition is 
	a palindrome. Return the minimum cuts needed for a palindrome partitioning of s.

	Example:
	Input: "aab"
	Output: 1
	Explanation: The palindrome partitioning ["aa","b"] could be produced using 
	1 cut."""

    def minCut(self, s: str) -> int:
        #pre-processing
        palin = dict()
        for k in range(len(s)):
            for i, j in (k, k), (k, k+1):
                while 0 <= i and j < len(s) and s[i] == s[j]: 
                    palin.setdefault(i, []).append(j)
                    i, j = i-1, j+1
                
        @lru_cache(None)
        def fn(i):
            """Return minimum palindrome partitioning of s[i:]"""
            if i == len(s): return 0
            return min(1 + fn(ii+1) for ii in palin[i])
        
        return fn(0)-1


    """133. Clone Graph (Medium)
	Given a reference of a node in a connected undirected graph. Return a deep 
	copy (clone) of the graph. Each node in the graph contains a val (int) and 
	a list (List[Node]) of its neighbors.

	class Node {
	    public int val;
	    public List<Node> neighbors;
	}
	 
	Test case format:
	For simplicity sake, each node's value is the same as the node's index 
	(1-indexed). For example, the first node with val = 1, the second node with 
	val = 2, and so on. The graph is represented in the test case using an 
	adjacency list. Adjacency list is a collection of unordered lists used to 
	represent a finite graph. Each list describes the set of neighbors of a 
	node in the graph. The given node will always be the first node with val = 1. 
	You must return the copy of the given node as a reference to the cloned graph.

	Example 1:
	Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
	Output: [[2,4],[1,3],[2,4],[1,3]]
	Explanation: There are 4 nodes in the graph.
	1st node (val = 1)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
	2nd node (val = 2)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
	3rd node (val = 3)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
	4th node (val = 4)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).

	Example 2:
	Input: adjList = [[]]
	Output: [[]]
	Explanation: Note that the input contains one empty list. The graph consists 
	of only one node with val = 1 and it does not have any neighbors.

	Example 3:
	Input: adjList = []
	Output: []
	Explanation: This an empty graph, it does not have any nodes.
	
	Example 4:
	Input: adjList = [[2],[1]]
	Output: [[2],[1]]

	Constraints:
	+ 1 <= Node.val <= 100
	+ Node.val is unique for each node.
	+ Number of Nodes will not exceed 100.
	+ There is no repeated edges and no self-loops in the graph.
	+ The Graph is connected and all nodes can be visited starting from the given node."""

    def cloneGraph(self, node: 'Node') -> 'Node':
        memo = dict()
        
        def fn(n): 
            """Return (deep) clonded node"""
            if n not in memo: 
                cln = memo[n] = Node(n.val)
                cln.neighbors = [fn(nn) for nn in n.neighbors]
            return memo[n]
            
        return node and fn(node)


    """134. Gas Station (Medium)
	There are N gas stations along a circular route, where the amount of gas at 
	station i is gas[i]. You have a car with an unlimited gas tank and it costs 
	cost[i] of gas to travel from station i to its next station (i+1). You 
	begin the journey with an empty tank at one of the gas stations. Return the 
	starting gas station's index if you can travel around the circuit once in 
	the clockwise direction, otherwise return -1.

	Note:
	If there exists a solution, it is guaranteed to be unique.
	Both input arrays are non-empty and have the same length.
	Each element in the input arrays is a non-negative integer.

	Example 1:
	Input: 
	gas  = [1,2,3,4,5]
	cost = [3,4,5,1,2]

	Output: 3

	Explanation:
	Start at station 3 (index 3) and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
	Travel to station 4. Your tank = 4 - 1 + 5 = 8
	Travel to station 0. Your tank = 8 - 2 + 1 = 7
	Travel to station 1. Your tank = 7 - 3 + 2 = 6
	Travel to station 2. Your tank = 6 - 4 + 3 = 5
	Travel to station 3. The cost is 5. Your gas is just enough to travel back to station 3.
	Therefore, return 3 as the starting index.

	Example 2:
	Input: 
	gas  = [2,3,4]
	cost = [3,4,3]

	Output: -1

	Explanation:
	You can't start at station 0 or 1, as there is not enough gas to travel to the next station. 
	Let's start at station 2 and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
	Travel to station 0. Your tank = 4 - 3 + 2 = 3
	Travel to station 1. Your tank = 3 - 3 + 3 = 3
	You cannot travel back to station 2, as it requires 4 unit of gas but you only have 3.
	Therefore, you can't travel around the circuit once no matter where you start."""

    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        ans = prefix = lowest = 0
        for n, (g, c) in enumerate(zip(gas, cost), 1): 
            prefix += g - c
            if prefix < lowest: 
                lowest = prefix
                ans = n
        return -1 if prefix < 0 else ans%n


    """135. Candy (Hard)
	There are N children standing in a line. Each child is assigned a rating 
	value. You are giving candies to these children subjected to the following 
	requirements:
	+ Each child must have at least one candy.
	+ Children with a higher rating get more candies than their neighbors.
	
	What is the minimum candies you must give?

	Example 1:
	Input: [1,0,2]
	Output: 5
	Explanation: You can allocate to the first, second and third child with 2, 
	1, 2 candies respectively.

	Example 2:
	Input: [1,2,2]
	Output: 4
	Explanation: You can allocate to the first, second and third child with 1, 
	2, 1 candies respectively. The third child gets 1 candy because it 
	satisfies the above two conditions."""

    def candy(self, ratings: List[int]) -> int:
        if not ratings: return 0 # edge case 
        
        ans = 1
        down, up = 0, 1
        for i in range(1, len(ratings)):
            if ratings[i-1] < ratings[i]: 
                if down: down, up = 0, 1 #reset
                up += 1
                ans += up
            elif ratings[i-1] == ratings[i]: 
                down, up = 0, 1 #reset 
                ans += 1
            else: 
                down += 1
                ans += down if down < up else down + 1
        return ans 


    """136. Single Number (Easy)
	Given a non-empty array of integers, every element appears twice except for 
	one. Find that single one. Note that your algorithm should have a linear 
	runtime complexity. Could you implement it without using extra memory?

	Example 1:
	Input: [2,2,1]
	Output: 1

	Example 2:
	Input: [4,1,2,1,2]
	Output: 4"""

    def singleNumber(self, nums: List[int]) -> int:
        return reduce(xor, nums)


    """137. Single Number II (Medium)
	Given a non-empty array of integers, every element appears three times 
	except for one, which appears exactly once. Find that single one. Note that 
	your algorithm should have a linear runtime complexity. Could you implement 
	it without using extra memory?

	Example 1:
	Input: [2,2,3,2]
	Output: 3

	Example 2:
	Input: [0,1,0,1,0,1,99]
	Output: 99"""

    def singleNumber(self, nums: List[int]) -> int:
        one = two = 0
        for x in nums: 
            two |= one & x
            one ^= x
            common = two & one
            two &= ~common
            one &= ~common 
        return one 


    """138. Copy List with Random Pointer (Medium)
	A linked list is given such that each node contains an additional random 
	pointer which could point to any node in the list or null. Return a deep 
	copy of the list. The Linked List is represented in the input/output as a 
	list of n nodes. Each node is represented as a pair of [val, random_index] 
	where:

	val: an integer representing Node.val
	random_index: the index of the node (range from 0 to n-1) where random 
	pointer points to, or null if it does not point to any node.

	Example 1:
	Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
	Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]

	Example 2:
	Input: head = [[1,1],[2,1]]
	Output: [[1,1],[2,1]]

	Example 3:
	Input: head = [[3,null],[3,0],[3,null]]
	Output: [[3,null],[3,0],[3,null]]

	Example 4:
	Input: head = []
	Output: []
	Explanation: Given linked list is empty (null pointer), so return null.

	Constraints:
	+ -10000 <= Node.val <= 10000
	+ Node.random is null or pointing to a node in the linked list.
	+ Number of Nodes will not exceed 1000."""

    def copyRandomList(self, head: 'Node') -> 'Node':
        mp = {}
        
        def fn(node): 
            """Return a deep copy of node."""
            if node and node not in mp:
                temp = mp[node] = Node(node.val)
                temp.next, temp.random = fn(node.next), fn(node.random)
            return mp.get(node)
        
        return fn(head)


    """139. Word Break (Medium)
	Given a non-empty string s and a dictionary wordDict containing a list of 
	non-empty words, determine if s can be segmented into a space-separated 
	sequence of one or more dictionary words. Note that the same word in the 
	dictionary may be reused multiple times in the segmentation. You may assume 
	the dictionary does not contain duplicate words.
	
	Example 1:
	Input: s = "leetcode", wordDict = ["leet", "code"]
	Output: true
	Explanation: Return true because "leetcode" can be segmented as "leet code".

	Example 2:
	Input: s = "applepenapple", wordDict = ["apple", "pen"]
	Output: true
	Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
	             Note that you are allowed to reuse a dictionary word.

	Example 3:
	Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
	Output: false"""

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        @lru_cache(None)
        def fn(i):
            """Return True if s[i:] can be segmented"""
            if i == len(s): return True 
            return any(s[i:i+len(word)] == word and fn(i+len(word)) for word in wordDict)
        
        return fn(0)


    """140. Word Break II (Hard)
	Given a non-empty string s and a dictionary wordDict containing a list of 
	non-empty words, add spaces in s to construct a sentence where each word is 
	a valid dictionary word. Return all such possible sentences. Note that the 
	same word in the dictionary may be reused multiple times in the segmentation.
	You may assume the dictionary does not contain duplicate words.
	
	Example 1:
	Input:
	s = "catsanddog"
	wordDict = ["cat", "cats", "and", "sand", "dog"]
	Output:
	[
	  "cats and dog",
	  "cat sand dog"
	]

	Example 2:
	Input:
	s = "pineapplepenapple"
	wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
	Output:
	[
	  "pine apple pen apple",
	  "pineapple pen apple",
	  "pine applepen apple"
	]
	Explanation: Note that you are allowed to reuse a dictionary word.

	Example 3:
	Input:
	s = "catsandog"
	wordDict = ["cats", "dog", "sand", "and", "cat"]
	Output:
	[]"""

    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        
        @lru_cache(None)
        def fn(i):
            """Return segmentation of s[i:]"""
            if i == len(s): return [[]]
            ans = []
            for word in wordDict: 
                if s[i:i+len(word)] == word: 
                    ans.extend([word] + x for x in fn(i+len(word)))
            return ans 
            
        return [" ".join(x) for x in fn(0)]


    
    """141. Linked List Cycle (Easy)
	Given a linked list, determine if it has a cycle in it. To represent a 
	cycle in the given linked list, we use an integer pos which represents the 
	position (0-indexed) in the linked list where tail connects to. If pos is 
	-1, then there is no cycle in the linked list.

	Example 1:
	Input: head = [3,2,0,-4], pos = 1
	Output: true
	Explanation: There is a cycle in the linked list, where tail connects to 
	the second node.

	Example 2:
	Input: head = [1,2], pos = 0
	Output: true
	Explanation: There is a cycle in the linked list, where tail connects to 
	the first node.

	Example 3:
	Input: head = [1], pos = -1
	Output: false
	Explanation: There is no cycle in the linked list.

	Follow up:
	Can you solve it using O(1) (i.e. constant) memory?"""

    def hasCycle(self, head: ListNode) -> bool:
        """Floyd's tortoise and hare (phase 1)"""
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow: return True
        return False 


    """142. Linked List Cycle II (Medium)
	Given a linked list, return the node where the cycle begins. If there is no 
	cycle, return null. To represent a cycle in the given linked list, we use 
	an integer pos which represents the position (0-indexed) in the linked list 
	where tail connects to. If pos is -1, then there is no cycle in the linked 
	list. Note that do not modify the linked list.

	Example 1:
	Input: head = [3,2,0,-4], pos = 1
	Output: tail connects to node index 1
	Explanation: There is a cycle in the linked list, where tail connects to 
	the second node.

	Example 2:
	Input: head = [1,2], pos = 0
	Output: tail connects to node index 0
	Explanation: There is a cycle in the linked list, where tail connects to 
	the first node.

	Example 3:
	Input: head = [1], pos = -1
	Output: no cycle
	Explanation: There is no cycle in the linked list.

	Follow-up:
	Can you solve it without using extra space?"""

    def detectCycle(self, head: ListNode) -> ListNode:
        """Floyd's tortoise & hare (phase 2)"""
        fast = slow = head 
        while fast and fast.next:
            fast, slow = fast.next.next, slow.next
            if fast == slow: 
                fast = head 
                while fast != slow: fast, slow = fast.next, slow.next
                return fast
        return None 


    """143. Reorder List (Medium)
	Given a singly linked list L: L0→L1→…→Ln-1→Ln, reorder it to: 
	L0→Ln→L1→Ln-1→L2→Ln-2→… You may not modify the values in the list's nodes, 
	only nodes itself may be changed.

	Example 1:
	Given 1->2->3->4, reorder it to 1->4->2->3.

	Example 2:
	Given 1->2->3->4->5, reorder it to 1->5->2->4->3."""

    def reorderList(self, head: ListNode) -> None:
        fast = slow = head 
        while fast and fast.next: 
            fast = fast.next.next
            slow = slow.next 
        if slow: slow.next, slow = None, slow.next
        
        hi = None
        while slow: 
            slow.next, slow, hi = hi, slow.next, slow
            
        lo = head 
        while hi: 
            hi.next, hi, lo.next, lo = lo.next, hi.next, hi, lo.next
            
        return head 

    
    """144. Binary Tree Preorder Traversal (Medium)
	Given a binary tree, return the preorder traversal of its nodes' values.

	Example:
	Input: [1,null,2,3]
	   1
	    \
	     2
	    /
	   3

	Output: [1,2,3]
	Follow up: Recursive solution is trivial, could you do it iteratively?"""

    def preorderTraversal(self, root: TreeNode) -> List[int]:
        ans = []
        stack = [root]
        while stack: 
            node = stack.pop()
            if node: 
                ans.append(node.val)
                stack.append(node.right)
                stack.append(node.left)
        return ans 


    """145. Binary Tree Postorder Traversal (Hard)
	Given a binary tree, return the postorder traversal of its nodes' values.

	Example:
	Input: [1,null,2,3]
	   1
	    \
	     2
	    /
	   3

	Output: [3,2,1]
	Follow up: Recursive solution is trivial, could you do it iteratively?"""

    def postorderTraversal(self, root: TreeNode) -> List[int]:
        ans = []
        node, stack = root, []
        while node or stack: 
            if node: 
                if node.right: stack.append(node.right)
                stack.append(node)
                node = node.left
                continue
            node = stack.pop()
            if stack and stack[-1] == node.right: 
                stack.pop()
                stack.append(node)
                node = node.right
            else:
                ans.append(node.val)
                node = None
        return ans 


    """147. Insertion Sort List (Medium)
	Sort a linked list using insertion sort. A graphical example of insertion 
	sort. The partial sorted list (black) initially contains only the first 
	element in the list. With each iteration one element (red) is removed from 
	the input data and inserted in-place into the sorted list

	Algorithm of Insertion Sort:
	Insertion sort iterates, consuming one input element each repetition, and 
	growing a sorted output list. At each iteration, insertion sort removes one 
	element from the input data, finds the location it belongs within the 
	sorted list, and inserts it there. It repeats until no input elements remain.

	Example 1:
	Input: 4->2->1->3
	Output: 1->2->3->4

	Example 2:
	Input: -1->5->3->4->0
	Output: -1->0->3->4->5"""

    def insertionSortList(self, head: ListNode) -> ListNode:
        node, prev = head, None
        while node: 
            if not prev or prev.val <= node.val: #append node 
                node.next, node, prev = prev, node.next, node
            else: 
                temp = prev
                while temp.next and temp.next.val > node.val: 
                    temp = temp.next
                node.next, node, temp.next = temp.next, node.next, node
                
        node, prev = prev, None
        while node:
            node.next, node, prev = prev, node.next, node
        return prev 


    """148. Sort List (Medium)
	Sort a linked list in O(NlogN) time using constant space complexity.

	Example 1:
	Input: 4->2->1->3
	Output: 1->2->3->4

	Example 2:
	Input: -1->5->3->4->0
	Output: -1->0->3->4->5"""

    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head # boundary condition (null or single node)
        
        fast = prev = slow = head 
        while fast and fast.next: fast, prev, slow = fast.next.next, slow, slow.next
            
        prev.next = None # break list into two pieces 
        list1, list2 = self.sortList(head), self.sortList(slow) # sort two pieces repectively 
        dummy = node = ListNode() # merge 
        while list1 and list2:
            if list1.val > list2.val: list1, list2 = list2, list1
            node.next = node = list1
            list1 = list1.next 
        node.next = list1 or list2 
        return dummy.next


    """149. Max Points on a Line (Hard)
	Given n points on a 2D plane, find the maximum number of points that lie on 
	the same straight line.

	Example 1:
	Input: [[1,1],[2,2],[3,3]]
	Output: 3
	Explanation:
	^
	|
	|        o
	|     o
	|  o  
	+------------->
	0  1  2  3  4

	Example 2:
	Input: [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
	Output: 4
	Explanation:
	^
	|
	|  o
	|     o        o
	|        o
	|  o        o
	+------------------->
	0  1  2  3  4  5  6

	NOTE: input types have been changed on April 15, 2019. Please reset to 
	default code definition to get new method signature."""

    def maxPoints(self, points: List[List[int]]) -> int:
        ans = 0
        for i, (x0, y0) in enumerate(points): #reference 
            dupe = 1 #count of duplicates
            freq = dict() #frequency table 
            for x, y in points[i+1:]:
                if x0 == x and y0 == y: dupe += 1
                elif x0 == x: freq[0, inf] = 1 + freq.get((0, inf), 0)
                elif y0 == y: freq[inf, 0] = 1 + freq.get((inf, 0), 0)
                else: 
                    g = gcd(x-x0, y-y0)
                    x, y = (x-x0)//g, (y-y0)//g
                    if x < 0: x, y = -x, -y
                    freq[x, y] = 1 + freq.get((x, y), 0)
            ans = max(ans, dupe + max(freq.values(), default=0))
        return ans 


    """150. Evaluate Reverse Polish Notation (Medium)
	Evaluate the value of an arithmetic expression in Reverse Polish Notation. 
	Valid operators are +, -, *, /. Each operand may be an integer or another 
	expression.

	Note:
	Division between two integers should truncate toward zero. The given RPN 
	expression is always valid. That means the expression would always evaluate 
	to a result and there won't be any divide by zero operation.
	
	Example 1:
	Input: ["2", "1", "+", "3", "*"]
	Output: 9
	Explanation: ((2 + 1) * 3) = 9

	Example 2:
	Input: ["4", "13", "5", "/", "+"]
	Output: 6
	Explanation: (4 + (13 / 5)) = 6

	Example 3:
	Input: ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
	Output: 22
	Explanation: 
	  ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
	= ((10 * (6 / (12 * -11))) + 17) + 5
	= ((10 * (6 / -132)) + 17) + 5
	= ((10 * 0) + 17) + 5
	= (0 + 17) + 5
	= 17 + 5
	= 22"""

    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens: 
            if token not in "+-*/": stack.append(int(token))
            else: 
                y, x = stack.pop(), stack.pop()
                if token == "/": x = int(x/y)
                else: x = eval(f"{x}{token}{y}")
                stack.append(x)
        return stack.pop()


    """151. Reverse Words in a String (Medium)
	Given an input string, reverse the string word by word.

	Example 1:
	Input: "the sky is blue"
	Output: "blue is sky the"

	Example 2:
	Input: "  hello world!  "
	Output: "world! hello"
	Explanation: Your reversed string should not contain leading or trailing 
	spaces.

	Example 3:
	Input: "a good   example"
	Output: "example good a"
	Explanation: You need to reduce multiple spaces between two words to a 
	single space in the reversed string.

	Note:
	+ A word is defined as a sequence of non-space characters.
	+ Input string may contain leading or trailing spaces. However, your 
	reversed string should not contain leading or trailing spaces.
	+ You need to reduce multiple spaces between two words to a single space in 
	the reversed string.

	Follow up:
	For C programmers, try to solve it in-place in O(1) extra space."""

    def reverseWords(self, s: str) -> str:
        return " ".join(reversed(s.split()))


    """152. Maximum Product Subarray (Medium)
	Given an integer array nums, find the contiguous subarray within an array 
	(containing at least one number) which has the largest product.

	Example 1:
	Input: [2,3,-2,4]
	Output: 6
	Explanation: [2,3] has the largest product 6.

	Example 2:
	Input: [-2,0,-1]
	Output: 0
	Explanation: The result cannot be 2, because [-2,-1] is not a subarray."""

    def maxProduct(self, nums: List[int]) -> int:
        mn = mx = 1
        ans = -inf
        for x in nums:
            if x < 0: mn, mx = mx, mn
            mn, mx = min(x, mn*x), max(x, mx*x)
            ans = max(ans, mx)
        return ans 



    """153. Find Minimum in Rotated Sorted Array (Medium)
	Suppose an array sorted in ascending order is rotated at some pivot unknown 
	to you beforehand. (i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]). 
	Find the minimum element. You may assume no duplicate exists in the array.

	Example 1:
	Input: [3,4,5,1,2] 
	Output: 1

	Example 2:
	Input: [4,5,6,7,0,1,2]
	Output: 0"""

    def findMin(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums)-1
        while lo < hi:
            mid = (lo + hi)//2
            if nums[mid] < nums[hi]: hi = mid
            else: lo = mid + 1
        return nums[lo]


    """154. Find Minimum in Rotated Sorted Array II (Hard)
	Suppose an array sorted in ascending order is rotated at some pivot unknown 
	to you beforehand. (i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]). 
	Find the minimum element. The array may contain duplicates.

	Example 1:
	Input: [1,3,5]
	Output: 1

	Example 2:
	Input: [2,2,2,0,1]
	Output: 0

	Note:
	This is a follow up problem to Find Minimum in Rotated Sorted Array.
	Would allow duplicates affect the run-time complexity? How and why?"""

    def findMin(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums)-1
        while lo < hi:
            mid = (lo + hi)//2
            if nums[mid] < nums[hi]: hi = mid
            elif nums[mid] > nums[hi]: lo = mid + 1
            else: hi -= 1
        return nums[lo]


    """156. Binary Tree Upside Down (Medium)
	Given the root of a binary tree, turn the tree upside down and return the 
	new root. You can turn a binary tree upside down with the following steps:
	* The original left child becomes the new root.
	* The original root becomes the new right child.
	* The original right child becomes the new left child.
	The mentioned steps are done level by level, it is guaranteed that every 
	node in the given tree has either 0 or 2 children.

	Example 1:
	Input: root = [1,2,3,4,5]
	Output: [4,5,2,null,null,3,1]

	Example 2:
	Input: root = []
	Output: []

	Example 3:
	Input: root = [1]
	Output: [1]

	Constraints:
	* The number of nodes in the tree will be in the range [0, 10].
	* 1 <= Node.val <= 10
	* Every node has either 0 or 2 children."""

    def upsideDownBinaryTree(self, root: TreeNode) -> TreeNode:
        if not root or not root.left: return root 
        ans = self.upsideDownBinaryTree(root.left)
        root.left.left = root.right
        root.left.right = root
        root.left = root.right = None
        return ans 


    """157. Read N Characters Given Read4 (Easy)
	Given a file and assume that you can only read the file using a given 
	method read4, implement a method to read n characters. 
	 
	Method read4:
	The API read4 reads 4 consecutive characters from the file, then writes 
	those characters into the buffer array buf4. The return value is the number 
	of actual characters read. Note that read4() has its own file pointer, much 
	like FILE *fp in C.

	Definition of read4:
	    Parameter:  char[] buf4
	    Returns:    int
	Note: buf4[] is destination not source, the results from read4 will be 
	      copied to buf4[]

	Below is a high level example of how read4 works:
	File file("abcde"); // File is "abcde", initially file pointer (fp) points to 'a'
	char[] buf4 = new char[4]; // Create buffer with enough space to store characters
	read4(buf4); // read4 returns 4. Now buf4 = "abcd", fp points to 'e'
	read4(buf4); // read4 returns 1. Now buf4 = "e", fp points to end of file
	read4(buf4); // read4 returns 0. Now buf4 = "", fp points to end of file

	Method read:
	By using the read4 method, implement the method read that reads n 
	characters from the file and store it in the buffer array buf. Consider 
	that you cannot manipulate the file directly. The return value is the 
	number of actual characters read.

	Definition of read:
	    Parameters:	char[] buf, int n
	    Returns:	int
	Note: buf[] is destination not source, you will need to write the results to buf[]

	Example 1:

	Input: file = "abc", n = 4
	Output: 3
	Explanation: After calling your read method, buf should contain "abc". We 
	             read a total of 3 characters from the file, so return 3. Note 
	             that "abc" is the file's content, not buf. buf is the 
	             destination buffer that you will have to write the results to.

	Example 2:
	Input: file = "abcde", n = 5
	Output: 5
	Explanation: After calling your read method, buf should contain "abcde". We 
	             read a total of 5 characters from the file, so return 5.

	Example 3:
	Input: file = "abcdABCD1234", n = 12
	Output: 12
	Explanation: After calling your read method, buf should contain "abcdABCD1234". 
	             We read a total of 12 characters from the file, so return 12.
	
	Example 4:
	Input: file = "leetcode", n = 5
	Output: 5
	Explanation: After calling your read method, buf should contain "leetc". We 
	             read a total of 5 characters from the file, so return 5.

	Note:
	* Consider that you cannot manipulate the file directly, the file is only 
	  accesible for read4 but not for read.
	* The read function will only be called once for each test case.
	* You may assume the destination buffer array, buf, is guaranteed to have 
	  enough space for storing n characters."""

    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)
        """
        ans, k = 0, 4
        buf4 = [" "]*4
        while ans < n and k == 4: 
            k = read4(buf4)
            buf[ans: ans+4] = buf4
            ans += k
        return min(n, ans)


    """159. Longest Substring with At Most Two Distinct Characters (Medium)
	Given a string s , find the length of the longest substring t  that 
	contains at most 2 distinct characters.

	Example 1:
	Input: "eceba"
	Output: 3
	Explanation: t is "ece" which its length is 3.

	Example 2:
	Input: "ccaabbb"
	Output: 5
	Explanation: t is "aabbb" which its length is 5."""

    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        ans, ii = 0, -1 # starting anchor
        queue = deque()
        seen = {} # last seen 
        for i, x in enumerate(s): 
            if not queue or queue[-1] != x: queue.append(x)
            if len(queue) > 2: 
                xx = queue.popleft()
                if xx != x: ii = seen[xx] # update anchor 
            ans = max(ans, i - ii)
            seen[x] = i
        return ans 


    """160. Intersection of Two Linked Lists (Easy)
	Write a program to find the node at which the intersection of two singly 
	linked lists begins. 

	Example 1:
	Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], 
	skipA = 2, skipB = 3
	Output: Reference of the node with value = 8
	Input Explanation: The intersected node's value is 8 (note that this must 
	not be 0 if the two lists intersect). From the head of A, it reads as 
	[4,1,8,4,5]. From the head of B, it reads as [5,6,1,8,4,5]. There are 2 
	nodes before the intersected node in A; There are 3 nodes before the 
	intersected node in B.
	 
	Example 2:
	Input: intersectVal = 2, listA = [1,9,1,2,4], listB = [3,2,4], skipA = 3, 
	skipB = 1
	Output: Reference of the node with value = 2
	Input Explanation: The intersected node's value is 2 (note that this must 
	not be 0 if the two lists intersect). From the head of A, it reads as 
	[1,9,1,2,4]. From the head of B, it reads as [3,2,4]. There are 3 nodes 
	before the intersected node in A; There are 1 node before the intersected 
	node in B.

	Example 3:
	Input: intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, 
	skipB = 2
	Output: null
	Input Explanation: From the head of A, it reads as [2,6,4]. From the head 
	of B, it reads as [1,5]. Since the two lists do not intersect, intersectVal 
	must be 0, while skipA and skipB can be arbitrary values.
	Explanation: The two lists do not intersect, so return null.

	Notes:
	If the two linked lists have no intersection at all, return null.
	The linked lists must retain their original structure after the function returns.
	You may assume there are no cycles anywhere in the entire linked structure.
	Each value on each linked list is in the range [1, 10^9].
	Your code should preferably run in O(n) time and use only O(1) memory."""

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        n0, n1 = headA, headB
        while n0 != n1:
            n0 = n0.next if n0 else headB
            n1 = n1.next if n1 else headA
        return n0


    """161. One Edit Distance (Medium)
	Given two strings s and t, return true if they are both one edit distance 
	apart, otherwise return false. A string s is said to be one distance apart 
	from a string t if you can:
	* Insert exactly one character into s to get t.
	* Delete exactly one character from s to get t.
	* Replace exactly one character of s with a different character to get t.

	Example 1:
	Input: s = "ab", t = "acb"
	Output: true
	Explanation: We can insert 'c' into s to get t.

	Example 2:
	Input: s = "", t = ""
	Output: false
	Explanation: We cannot get t from s by only one step.

	Example 3:
	Input: s = "a", t = ""
	Output: true

	Example 4:
	Input: s = "", t = "A"
	Output: true

	Constraints:
	* 0 <= s.length <= 104
	* 0 <= t.length <= 104
	* s and t consist of lower-case letters, upper-case letters and/or digits."""

    def isOneEditDistance(self, s: str, t: str) -> bool:
        if s == t: return False 
        i = 0
        while i < min(len(t), len(s)): 
            if s[i] != t[i]: break 
            i += 1
        return s[i:] == t[i+1:] or s[i+1:] == t[i+1:] or s[i+1:] == t[i:]

   
    """162. Find Peak Element (Medium)
	A peak element is an element that is greater than its neighbors. Given an 
	input array nums, where nums[i] ≠ nums[i+1], find a peak element and return 
	its index. The array may contain multiple peaks, in that case return the 
	index to any one of the peaks is fine. You may imagine that 
	nums[-1] = nums[n] = -∞.

	Example 1:
	Input: nums = [1,2,3,1]
	Output: 2
	Explanation: 3 is a peak element and your function should return the index 
	number 2.

	Example 2:
	Input: nums = [1,2,1,3,5,6,4]
	Output: 1 or 5 
	Explanation: Your function can return either index number 1 where the peak 
	element is 2, or index number 5 where the peak element is 6.

	Follow up: Your solution should be in logarithmic complexity."""

    def findPeakElement(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums)-1
        while lo < hi:
            mid = (lo + hi)//2
            if nums[mid] < nums[mid+1]: lo = mid + 1
            else: hi = mid
        return lo


    """163. Missing Ranges (Easy)
	You are given an inclusive range [lower, upper] and a sorted unique integer 
	array nums, where all elements are in the inclusive range. A number x is 
	considered missing if x is in the range [lower, upper] and x is not in nums. 
	Return the smallest sorted list of ranges that cover every missing number 
	exactly. That is, no element of nums is in any of the ranges, and each 
	missing number is in one of the ranges. Each range [a,b] in the list should 
	be output as:
	* "a->b" if a != b
	* "a" if a == b

	Example 1:
	Input: nums = [0,1,3,50,75], lower = 0, upper = 99
	Output: ["2","4->49","51->74","76->99"]
	Explanation: The ranges are:
	[2,2] --> "2"
	[4,49] --> "4->49"
	[51,74] --> "51->74"
	[76,99] --> "76->99"

	Example 2:
	Input: nums = [], lower = 1, upper = 1
	Output: ["1"]
	Explanation: The only missing range is [1,1], which becomes "1".

	Example 3:
	Input: nums = [], lower = -3, upper = -1
	Output: ["-3->-1"]
	Explanation: The only missing range is [-3,-1], which becomes "-3->-1".

	Example 4:
	Input: nums = [-1], lower = -1, upper = -1
	Output: []
	Explanation: There are no missing ranges since there are no missing numbers.

	Example 5:
	Input: nums = [-1], lower = -2, upper = -1
	Output: ["-2"]
	 
	Constraints:
	* -109 <= lower <= upper <= 109
	* 0 <= nums.length <= 100
	* lower <= nums[i] <= upper
	* All the values of nums are unique."""

    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        nums = [lower-1] + nums + [upper+1] # augmented nums
        ans = []
        for i in range(len(nums)-1): 
            if nums[i] + 2 == nums[i+1]: 
                ans.append(str(nums[i]+1))
            elif nums[i] + 2 < nums[i+1]: 
                ans.append(str(nums[i]+1) + "->" + str(nums[i+1]-1))
        return ans 


    """164. Maximum Gap (Hard)
	Given an unsorted array, find the maximum difference between the successive 
	elements in its sorted form. Return 0 if the array contains less than 2 
	elements.

	Example 1:
	Input: [3,6,9,1]
	Output: 3
	Explanation: The sorted form of the array is [1,3,6,9], either (3,6) or 
	             (6,9) has the maximum difference 3.

	Example 2:
	Input: [10]
	Output: 0
	Explanation: The array contains less than 2 elements, therefore return 0.
	
	Note:
	You may assume all elements in the array are non-negative integers and fit 
	in the 32-bit signed integer range. Try to solve it in linear time/space."""

    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2: return 0 #edge case 
        
        mn, mx = min(nums), max(nums)
        step = max(1, (mx - mn)//(len(nums) - 1))
        size = (mx - mn)//step + 1
        buckets = [[inf, -inf] for _ in range(size)]
        
        for num in nums: 
            i = (num - mn)//step
            x, xx = buckets[i]
            buckets[i] = [min(x, num), max(xx, num)]
        
        ans = 0
        prev = mn
        for i in range(len(buckets)): 
            x, xx = buckets[i]
            if x < inf: 
                ans = max(ans, x - prev)
                prev = xx
        return ans 


    """165. Compare Version Numbers (Medium)
	Compare two version numbers version1 and version2. If version1 > version2 
	return 1; if version1 < version2 return -1;otherwise return 0. You may 
	assume that the version strings are non-empty and contain only digits and 
	the . character. The . character does not represent a decimal point and is 
	used to separate number sequences. For instance, 2.5 is not "two and a half" 
	or "half way to version three", it is the fifth second-level revision of 
	the second first-level revision. You may assume the default revision number 
	for each level of a version number to be 0. For example, version number 3.4 
	has a revision number of 3 and 4 for its first and second level revision 
	number. Its third and fourth level revision number are both 0.

	Example 1:
	Input: version1 = "0.1", version2 = "1.1"
	Output: -1

	Example 2:
	Input: version1 = "1.0.1", version2 = "1"
	Output: 1

	Example 3:
	Input: version1 = "7.5.2.4", version2 = "7.5.3"
	Output: -1

	Example 4:
	Input: version1 = "1.01", version2 = "1.001"
	Output: 0
	Explanation: Ignoring leading zeroes, both “01” and “001" represent the 
	same number “1”

	Example 5:
	Input: version1 = "1.0", version2 = "1.0.0"
	Output: 0
	Explanation: The first version number does not have a third level revision 
	number, which means its third level revision number is default to "0"
	 
	Note:
	* Version strings are composed of numeric strings separated by dots . and 
	  this numeric strings may have leading zeroes.
	* Version strings do not start or end with dots, and they will not be two 
	  consecutive dots."""

    def compareVersion(self, version1: str, version2: str) -> int:
        for x, y in zip_longest(version1.split("."), version2.split("."), fillvalue="0"):
            if int(x) > int(y): return 1
            elif int(x) < int(y): return -1
        return 0


    """166. Fraction to Recurring Decimal (Medium)
	Given two integers representing the numerator and denominator of a 
	fraction, return the fraction in string format. If the fractional part 
	is repeating, enclose the repeating part in parentheses.

	Example 1:
	Input: numerator = 1, denominator = 2
	Output: "0.5"

	Example 2:
	Input: numerator = 2, denominator = 1
	Output: "2"

	Example 3:
	Input: numerator = 2, denominator = 3
	Output: "0.(6)" """

    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        sign = "-" if numerator * denominator < 0 else ""
        q, r = divmod(abs(numerator), abs(denominator))
        if not r: return sign + str(q)
        
        seen = {r : (i := 0)}
        dcml = ""
        while r: 
            d, r = divmod(10*r, abs(denominator))
            dcml += str(d)
            if r in seen: 
                k = seen[r]
                return sign + f"{q}.{dcml[:k]}({dcml[k:]})"
            seen[r] = (i := i+1)
        return sign + f"{q}.{dcml}"


    """167. Two Sum II - Input array is sorted (Easy)
	Given an array of integers that is already sorted in ascending order, find 
	two numbers such that they add up to a specific target number. The function 
	twoSum should return indices of the two numbers such that they add up to 
	the target, where index1 must be less than index2.

	Note:
	Your returned answers (both index1 and index2) are not zero-based.
	You may assume that each input would have exactly one solution and you may 
	not use the same element twice.

	Example:
	Input: numbers = [2,7,11,15], target = 9
	Output: [1,2]
	Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2."""

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lo, hi = 0, len(numbers)-1
        while lo < hi: 
            val = numbers[lo] + numbers[hi]
            if val == target: return [lo+1, hi+1]
            elif val > target: hi -= 1
            else: lo += 1



    """168. Excel Sheet Column Title (Easy)
	Given a positive integer, return its corresponding column title as appear 
	in an Excel sheet. 	For example:
	    1 -> A
	    2 -> B
	    3 -> C
	    ...
	    26 -> Z
	    27 -> AA
	    28 -> AB 
	    ...

	Example 1:
	Input: 1
	Output: "A"

	Example 2:
	Input: 28
	Output: "AB"

	Example 3:
	Input: 701
	Output: "ZY" """

    def convertToTitle(self, n: int) -> str:
        ans = []
        while n: 
            n, r = divmod(n-1, 26)
            ans.append(r)
        return "".join(chr(r+65) for r in reversed(ans))


    """169. Majority Element (Easy)
	Given an array of size n, find the majority element. The majority element 
	is the element that appears more than ⌊ n/2 ⌋ times. You may assume that 
	the array is non-empty and the majority element always exist in the array.

	Example 1:
	Input: [3,2,3]
	Output: 3

	Example 2:
	Input: [2,2,1,1,1,2,2]
	Output: 2"""

    def majorityElement(self, nums: List[int]) -> int:
        """Boyer-Moore majority voting"""
        ans, vote = None, 0
        for x in nums:
            if vote == 0: ans = x
            vote += 1 if x == ans else -1
        return ans


    """171. Excel Sheet Column Number (Easy)
	Given a column title as appear in an Excel sheet, return its corresponding 
	column number. For example:
	    A -> 1
	    B -> 2
	    C -> 3
	    ...
	    Z -> 26
	    AA -> 27
	    AB -> 28 
	    ...

	Example 1:
	Input: "A"
	Output: 1

	Example 2:
	Input: "AB"
	Output: 28

	Example 3:
	Input: "ZY"
	Output: 701

	Constraints:
	* 1 <= s.length <= 7
	* s consists only of uppercase English letters.
	* s is between "A" and "FXSHRXW"."""

    def titleToNumber(self, s: str) -> int:
        ans = 0
        for c in s:
            ans = 26*ans + ord(c) - 64
        return ans 


    """172. Factorial Trailing Zeroes (Easy)
	Given an integer n, return the number of trailing zeroes in n!.

	Example 1:
	Input: 3
	Output: 0
	Explanation: 3! = 6, no trailing zero.

	Example 2:
	Input: 5
	Output: 1
	Explanation: 5! = 120, one trailing zero.

	Note: Your solution should be in logarithmic time complexity."""

    def trailingZeroes(self, n: int) -> int:
        ans = 0
        while n:
            n //= 5
            ans += n
        return ans 


    """174. Dungeon Game (Hard)
	The demons had captured the princess (P) and imprisoned her in the bottom-
	right corner of a dungeon. The dungeon consists of M x N rooms laid out in 
	a 2D grid. Our valiant knight (K) was initially positioned in the top-left 
	room and must fight his way through the dungeon to rescue the princess. The 
	knight has an initial health point represented by a positive integer. If at 
	any point his health point drops to 0 or below, he dies immediately. Some 
	of the rooms are guarded by demons, so the knight loses health (negative 
	integers) upon entering these rooms; other rooms are either empty (0's) or 
	contain magic orbs that increase the knight's health (positive integers). 
	In order to reach the princess as quickly as possible, the knight decides 
	to move only rightward or downward in each step.

	Write a function to determine the knight's minimum initial health so that 
	he is able to rescue the princess. For example, given the dungeon below, 
	the initial health of the knight must be at least 7 if he follows the 
	optimal path RIGHT-> RIGHT -> DOWN -> DOWN.

	-2 (K)	-3	3
	-5	-10	1
	10	30	-5 (P)

	Note:
	* The knight's health has no upper bound.
	* Any room can contain threats or power-ups, even the first room the knight 
	  enters and the bottom-right room where the princess is imprisoned."""

    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m, n = len(dungeon), len(dungeon[0])
        
        @lru_cache(None)
        def fn(i, j): 
            """Return minimum health at cell (i, j)"""
            if i == m-1 and j == n-1: return max(1, 1 - dungeon[i][j])
            if i > m-1 or j > n-1: return inf
            return max(1, min(fn(i+1, j), fn(i, j+1)) - dungeon[i][j])
        
        return fn(0, 0)


    """179. Largest Number (Medium)
	Given a list of non negative integers, arrange them such that they form the 
	largest number.

	Example 1:
	Input: [10,2]
	Output: "210"

	Example 2:
	Input: [3,30,34,5,9]
	Output: "9534330"

	Note: The result may be very large, so you need to return a string instead 
	of an integer."""

    def largestNumber(self, nums: List[int]) -> str:
        
        def cmp(x, y):
            """Compure two strings and return an integer based on outcome"""
            if x + y > y + x: return 1
            elif x + y == y + x: return 0
            else: return -1
                
        nums = [str(x) for x in nums]
        return "".join(sorted(nums, key=cmp_to_key(cmp), reverse=True)).lstrip("0") or "0"


    """186. Reverse Words in a String II (Medium)
	Given an input string , reverse the string word by word. 

	Example:
	Input:  ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
	Output: ["b","l","u","e"," ","i","s"," ","s","k","y"," ","t","h","e"]

	Note: 
	* A word is defined as a sequence of non-space characters.
	* The input string does not contain leading or trailing spaces.
	* The words are always separated by a single space.
	Follow up: Could you do it in-place without allocating extra space?"""

    def reverseWords(self, s: List[str]) -> None:

        def fn(lo, hi): 
            """Reverse s[lo:hi+1] in-place."""
            while lo < hi: 
                s[lo], s[hi] = s[hi], s[lo]
                lo, hi = lo+1, hi-1
                
        fn(0, len(s)-1)
        lo = 0
        for i in range(len(s)+1): 
            if i == len(s) or s[i] == " ": 
                hi = i - 1
                fn(lo, hi)
                lo = i + 1


    """187. Repeated DNA Sequences (Medium)
	All DNA is composed of a series of nucleotides abbreviated as A, C, G, and 
	T, for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to 
	identify repeated sequences within the DNA. Write a function to find all 
	the 10-letter-long sequences (substrings) that occur more than once in a 
	DNA molecule.

	Example:
	Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
	Output: ["AAAAACCCCC", "CCCCCAAAAA"]"""

    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        htab = {"A":0, "C":1, "G":2, "T":3} #hash table
        
        ans, seen = set(), set()
        hs = 0 
        for i in range(len(s)):
            hs = 4*hs + htab[s[i]]
            if i >= 10: hs -= htab[s[i-10]]*4**10 #rolling hash
            if hs in seen: ans.add(s[i-9:i+1])
            if i >= 9: seen.add(hs)
        return ans


    """188. Best Time to Buy and Sell Stock IV (Hard)
	Say you have an array for which the i-th element is the price of a given 
	stock on day i. Design an algorithm to find the maximum profit. You may 
	complete at most k transactions.

	Note: You may not engage in multiple transactions at the same time (ie, 
	you must sell the stock before you buy again).

	Example 1:
	Input: [2,4,1], k = 2
	Output: 2
	Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), 
	             profit = 4-2 = 2.

	Example 2:
	Input: [3,2,6,5,0,3], k = 2
	Output: 7
	Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), 
	             profit = 6-2 = 4. Then buy on day 5 (price = 0) and sell on 
	             day 6 (price = 3), profit = 3-0 = 3."""

    def maxProfit(self, k: int, prices: List[int]) -> int:
        if k >= len(prices)//2: 
            return sum(max(0, prices[i] - prices[i-1]) for i in range(1, len(prices)))
        
        buy, pnl = [inf]*k, [0]*k
        for price in prices:
            for i in range(k):
                buy[i] = min(buy[i], price - (pnl[i-1] if i else 0))
                pnl[i] = max(pnl[i], price - buy[i])
        return pnl[-1] if prices and k else 0


    """189. Rotate Array (Easy)
	Given an array, rotate the array to the right by k steps, where k is non-
	negative. 

	Follow up:
	Try to come up as many solutions as you can, there are at least 3 different 
	ways to solve this problem. Could you do it in-place with O(1) extra space?

	Example 1:
	Input: nums = [1,2,3,4,5,6,7], k = 3
	Output: [5,6,7,1,2,3,4]
	Explanation:
	rotate 1 steps to the right: [7,1,2,3,4,5,6]
	rotate 2 steps to the right: [6,7,1,2,3,4,5]
	rotate 3 steps to the right: [5,6,7,1,2,3,4]

	Example 2:
	Input: nums = [-1,-100,3,99], k = 2
	Output: [3,99,-1,-100]
	Explanation: 
	rotate 1 steps to the right: [99,-1,-100,3]
	rotate 2 steps to the right: [3,99,-1,-100]

	Constraints:
	* 1 <= nums.length <= 2 * 10^4
	* It's guaranteed that nums[i] fits in a 32 bit-signed integer.
	* k >= 0"""

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        g = gcd(k, (n := len(nums)))
        for i in range(g):
            ii = i
            for _ in range(n//g): 
                ii = (ii + k)%n
                nums[i], nums[ii] = nums[ii], nums[i]


    """190. Reverse Bits (Easy)
	Reverse bits of a given 32 bits unsigned integer.

	Example 1:
	Input: 00000010100101000001111010011100
	Output: 00111001011110000010100101000000
	Explanation: The input binary string 00000010100101000001111010011100 
	represents the unsigned integer 43261596, so return 964176192 which its 
	binary representation is 00111001011110000010100101000000.
	
	Example 2:

	Input: 11111111111111111111111111111101
	Output: 10111111111111111111111111111111
	Explanation: The input binary string 11111111111111111111111111111101 
	represents the unsigned integer 4294967293, so return 3221225471 which its 
	binary representation is 10111111111111111111111111111111.

	Note:
	Note that in some languages such as Java, there is no unsigned integer type. 
	In this case, both input and output will be given as signed integer type and 
	should not affect your implementation, as the internal binary representation 
	of the integer is the same whether it is signed or unsigned. In Java, the 
	compiler represents the signed integers using 2's complement notation. 
	Therefore, in Example 2 above the input represents the signed integer -3 and 
	the output represents the signed integer -1073741825.

	Follow up: If this function is called many times, how would you optimize it?"""

    def reverseBits(self, n: int) -> int:
        return int(bin(n)[2:].zfill(32)[::-1], 2)


    """191. Number of 1 Bits (Easy)
	Write a function that takes an unsigned integer and return the number of 
	'1' bits it has (also known as the Hamming weight).

	Example 1:
	Input: 00000000000000000000000000001011
	Output: 3
	Explanation: The input binary string 00000000000000000000000000001011 has a 
	total of three '1' bits.

	Example 2:
	Input: 00000000000000000000000010000000
	Output: 1
	Explanation: The input binary string 00000000000000000000000010000000 has a 
	total of one '1' bit.

	Example 3:
	Input: 11111111111111111111111111111101
	Output: 31
	Explanation: The input binary string 11111111111111111111111111111101 has a 
	total of thirty one '1' bits.

	Note:
	Note that in some languages such as Java, there is no unsigned integer type. 
	In this case, the input will be given as signed integer type and should not 
	affect your implementation, as the internal binary representation of the 
	integer is the same whether it is signed or unsigned. In Java, the compiler 
	represents the signed integers using 2's complement notation. Therefore, in 
	Example 3 above the input represents the signed integer -3.
	 
	Follow up: If this function is called many times, how would you optimize it?"""

    def hammingWeight(self, n: int) -> int:
        ans = 0
        while n: 
            ans += 1
            n &= n-1
        return ans 


    """198. House Robber (Easy)
	You are a professional robber planning to rob houses along a street. Each 
	house has a certain amount of money stashed, the only constraint stopping 
	you from robbing each of them is that adjacent houses have security system 
	connected and it will automatically contact the police if two adjacent 
	houses were broken into on the same night. Given a list of non-negative 
	integers representing the amount of money of each house, determine the 
	maximum amount of money you can rob tonight without alerting the police.

	Example 1:
	Input: nums = [1,2,3,1]
	Output: 4
	Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
	             Total amount you can rob = 1 + 3 = 4.

	Example 2:
	Input: nums = [2,7,9,3,1]
	Output: 12
	Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 
	             5 (money = 1). Total amount you can rob = 2 + 9 + 1 = 12.

	Constraints:
	0 <= nums.length <= 100
	0 <= nums[i] <= 400"""

    def rob(self, nums: List[int]) -> int:
        
        @lru_cache(None)
        def fn(i):
            """Return the maximum amount of money after robbing ith house"""
            if i < 0: return 0
            return max(fn(i-1), fn(i-2) + nums[i])
        
        return fn(len(nums)-1)


    """199. Binary Tree Right Side View (Medium)
	Given a binary tree, imagine yourself standing on the right side of it, 
	return the values of the nodes you can see ordered from top to bottom.

	Example:
	Input: [1,2,3,null,5,null,4]
	Output: [1, 3, 4]
	Explanation:

	   1            <---
	 /   \
	2     3         <---
	 \     \
	  5     4       <---"""

    def rightSideView(self, root: TreeNode) -> List[int]:
        ans = []
        queue, k = [root], 0
        while queue: 
            tmp = []
            for node in queue: 
                if node: 
                    if len(ans) == k: ans.append(node.val)
                    tmp.append(node.right)
                    tmp.append(node.left)
            queue, k = tmp, k+1
        return ans 


    """200. Number of Islands (Medium)
	Given a 2d grid map of '1's (land) and '0's (water), count the number of 
	islands. An island is surrounded by water and is formed by connecting 
	adjacent lands horizontally or vertically. You may assume all four edges 
	of the grid are all surrounded by water.

	Example 1:
	Input: grid = [
	  ["1","1","1","1","0"],
	  ["1","1","0","1","0"],
	  ["1","1","0","0","0"],
	  ["0","0","0","0","0"]
	]
	Output: 1

	Example 2:
	Input: grid = [
	  ["1","1","0","0","0"],
	  ["1","1","0","0","0"],
	  ["0","0","1","0","0"],
	  ["0","0","0","1","1"]
	]
	Output: 3"""

    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: return 0
        m, n = len(grid), len(grid[0])
        
        def fn(i, j):
            """Flood fill cell with "0"."""
            if 0 <= i < m and 0 <= j < n and grid[i][j] == "1": 
                grid[i][j] = "0"
                for ii, jj in (i-1, j), (i, j-1), (i, j+1), (i+1, j):
                    fn(ii, jj)
                return 1
            return 0
                
        return sum(fn(i, j) for i in range(m) for j in range(n))


   """201. Bitwise AND of Numbers Range (Medium)
	Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise 
	AND of all numbers in this range, inclusive.

	Example 1:
	Input: [5,7]
	Output: 4

	Example 2:
	Input: [0,1]
	Output: 0"""

    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        while n > m: 
            n &= n-1 #unset last set bit
        return n 


    """202. Happy Number (Easy)
	Write an algorithm to determine if a number n is "happy". A happy number is 
	a number defined by the following process: Starting with any positive 
	integer, replace the number by the sum of the squares of its digits, and 
	repeat the process until the number equals 1 (where it will stay), or it 
	loops endlessly in a cycle which does not include 1. Those numbers for 
	which this process ends in 1 are happy numbers. Return True if n is a happy 
	number, and False if not.

	Example: 
	Input: 19
	Output: true
	Explanation: 
	12 + 92 = 82
	82 + 22 = 68
	62 + 82 = 100
	12 + 02 + 02 = 1"""

    def isHappy(self, n: int) -> bool:
        fn = lambda n: sum(int(x)**2 for x in str(n))
        fast, slow = fn(n), n
        while fast != slow:
            fast = fn(fn(fast))
            slow = fn(slow)
        return fast == 1


    """203. Remove Linked List Elements (Easy)
	Remove all elements from a linked list of integers that have value val.

	Example:
	Input:  1->2->6->3->4->5->6, val = 6
	Output: 1->2->3->4->5"""

    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy = node = ListNode(next=head) #head could be removed
        while node.next: 
            if node.next.val == val: node.next = node.next.next 
            else: node = node.next 
        return dummy.next 


    """204. Count Primes (Easy)
	Count the number of prime numbers less than a non-negative number, n.

	Example:
	Input: 10
	Output: 4
	Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7."""

    def countPrimes(self, n: int) -> int:
        """Sieve of Eratosthenes"""
        prime = [False] *2 + [True] * (n-2) #0 and 1 are not prime
        for i in range(int(sqrt(n))+1):
            if prime[i]:
                for k in range(i*i, n, i): 
                    prime[k] = False 
        return sum(prime)


    """205. Isomorphic Strings (Easy)
	Given two strings s and t, determine if they are isomorphic. Two strings 
	are isomorphic if the characters in s can be replaced to get t. All 
	occurrences of a character must be replaced with another character while 
	preserving the order of characters. No two characters may map to the same 
	character but a character may map to itself.

	Example 1:
	Input: s = "egg", t = "add"
	Output: true

	Example 2:
	Input: s = "foo", t = "bar"
	Output: false

	Example 3:
	Input: s = "paper", t = "title"
	Output: true
	Note:
	You may assume both s and t have the same length."""

    def isIsomorphic(self, s: str, t: str) -> bool:
        return len(set(zip(s, t))) == len(set(s)) == len(set(t))


    """206. Reverse Linked List (Easy)
	Reverse a singly linked list.

	Example:
	Input: 1->2->3->4->5->NULL
	Output: 5->4->3->2->1->NULL

	Follow up: A linked list can be reversed either iteratively or recursively. 
	Could you implement both?"""

    def reverseList(self, head: ListNode) -> ListNode:
        prev, node = None, head
        while node:
            node.next, node, prev = prev, node.next, node
        return prev


    """207. Course Schedule (Medium)
	There are a total of numCourses courses you have to take, labeled from 0 to 
	numCourses-1. Some courses may have prerequisites, for example to take 
	course 0 you have to first take course 1, which is expressed as a pair: 
	[0,1]. Given the total number of courses and a list of prerequisite pairs, 
	is it possible for you to finish all courses?

	Example 1:
	Input: numCourses = 2, prerequisites = [[1,0]]
	Output: true
	Explanation: There are a total of 2 courses to take. To take course 1 you 
	             should have finished course 0. So it is possible.

	Example 2:
	Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
	Output: false
	Explanation: There are a total of 2 courses to take. To take course 1 you 
	             should have finished course 0, and to take course 0 you should 
	             also have finished course 1. So it is impossible.
	 

	Constraints:
	* The input prerequisites is a graph represented by a list of edges, not 
	  adjacency matrices. Read more about how a graph is represented.
	* You may assume that there are no duplicate edges in the input 
	  prerequisites.
	* 1 <= numCourses <= 10^5"""

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #graph as adjacency list
        digraph = dict()
        for u, v in prerequisites: digraph.setdefault(u, []).append(v)
            
        def cyclic(n):
            """Return True if cycle is detected involving given node"""
            if seen[n]: return seen[n] == -1
            seen[n] = -1 #GRAY
            if any(cyclic(nn) for nn in digraph.get(n, [])): return True
            seen[n] = 1 #BLACK
            return False 
            
        seen = [0]*numCourses #WHITE
        return not any(cyclic(i) for i in range(numCourses))


    """209. Minimum Size Subarray Sum (Medium)
	Given an array of n positive integers and a positive integer s, find the 
	minimal length of a contiguous subarray of which the sum ≥ s. If there 
	isn't one, return 0 instead.

	Example: 
	Input: s = 7, nums = [2,3,1,2,4,3]
	Output: 2
	Explanation: the subarray [4,3] has the minimal length under the problem 
	             constraint.

	Follow up: If you have figured out the O(n) solution, try coding another 
	           solution of which the time complexity is O(n log n). """

    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        ans, lo = inf, 0
        for hi in range(len(nums)):
            s -= nums[hi]
            while s <= 0:
                ans = min(ans, hi - lo + 1)
                s += nums[lo]
                lo += 1
        return ans if ans < inf else 0


    """210. Course Schedule II (Medium)
	There are a total of n courses you have to take, labeled from 0 to n-1. 
	Some courses may have prerequisites, for example to take course 0 you have 
	to first take course 1, which is expressed as a pair: [0,1]. Given the 
	total number of courses and a list of prerequisite pairs, return the 
	ordering of courses you should take to finish all courses. There may be 
	multiple correct orders, you just need to return one of them. If it is 
	impossible to finish all courses, return an empty array.

	Example 1:
	Input: 2, [[1,0]] 
	Output: [0,1]
	Explanation: There are a total of 2 courses to take. To take course 1 you 
	             should have finished course 0. So the correct course order is 
	             [0,1].

	Example 2:
	Input: 4, [[1,0],[2,0],[3,1],[3,2]]
	Output: [0,1,2,3] or [0,2,1,3]
	Explanation: There are a total of 4 courses to take. To take course 3 you 
	             should have finished both courses 1 and 2. Both courses 1 and 
	             2 should be taken after you finished course 0. So one correct 
	             course order is [0,1,2,3]. Another correct ordering is [0,2,1,3] .

	Note:
	* The input prerequisites is a graph represented by a list of edges, not 
	  adjacency matrices. Read more about how a graph is represented.
	* You may assume that there are no duplicate edges in the input prerequisites."""

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        #graph as adjacency list
        digraph = dict()
        for u, v in prerequisites: digraph.setdefault(u, []).append(v)
            
        def cyclic(n):
            """Return True if cycle is detected involving given node"""
            if seen[n]: return seen[n] == -1
            seen[n] = -1 #GRAY
            if any(cyclic(nn) for nn in digraph.get(n, []) if seen[nn] != 1): return True
            seen[n] = 1 #BLACK
            ans.append(n)
            return False 
        
        ans = []
        seen = [0]*numCourses #WHITE
        return [] if any(cyclic(i) for i in range(numCourses)) else ans 


    """212. Word Search II (Hard)
	Given a 2D board and a list of words from the dictionary, find all words in 
	the board. Each word must be constructed from letters of sequentially 
	adjacent cell, where "adjacent" cells are those horizontally or vertically 
	neighboring. The same letter cell may not be used more than once in a word.

	Example:
	Input: 
	board = [
	  ['o','a','a','n'],
	  ['e','t','a','e'],
	  ['i','h','k','r'],
	  ['i','f','l','v']
	]
	words = ["oath","pea","eat","rain"]

	Output: ["eat","oath"]

	Note:
	All inputs are consist of lowercase letters a-z.
	The values of words are distinct."""

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m, n = len(board), len(board[0])
        
        trie = Trie()
        for word in words: trie.insert(word)
            
        def fn(i, j, node): 
            """Populate ans through backtracking"""
            if node.word: 
                ans.append("".join(stack))
                node.word = False 
            if not (0 <= i < m and 0 <= j < n) or board[i][j] not in node.children: return 
            stack.append(board[i][j])
            board[i][j] = "#" #mark as visited
            for ii, jj in (i-1, j), (i, j-1), (i, j+1), (i+1, j):
                fn(ii, jj, node.children[stack[-1]])
            board[i][j] = stack.pop()
        
        ans, stack = [], []
        for i in range(m):
            for j in range(n): 
                fn(i, j, trie.root)
        return ans


    """213. House Robber II (Medium)
	You are a professional robber planning to rob houses along a street. Each 
	house has a certain amount of money stashed. All houses at this place are 
	arranged in a circle. That means the first house is the neighbor of the 
	last one. Meanwhile, adjacent houses have security system connected and it 
	will automatically contact the police if two adjacent houses were broken 
	into on the same night. Given a list of non-negative integers representing 
	the amount of money of each house, determine the maximum amount of money 
	you can rob tonight without alerting the police.

	Example 1:
	Input: [2,3,2]
	Output: 3
	Explanation: You cannot rob house 1 (money = 2) and then rob house 3 
	             (money = 2), because they are adjacent houses.

	Example 2:
	Input: [1,2,3,1]
	Output: 4
	Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
	             Total amount you can rob = 1 + 3 = 4."""

    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0] #edge case 
        
        def fn(lo, hi):
            """Return money after robbing houses[lo:hi]"""
            f0 = f1 = 0
            for i in range(lo, hi):
                f0, f1 = f1, max(f1, f0 + nums[i])
            return f1
        
        return max(fn(0, len(nums)-1), fn(1, len(nums)))


    """214. Shortest Palindrome (Hard)
	Given a string s, you are allowed to convert it to a palindrome by adding 
	characters in front of it. Find and return the shortest palindrome you can 
	find by performing this transformation.

	Example 1:
	Input: "aacecaaa"
	Output: "aaacecaaa"

	Example 2:
	Input: "abcd"
	Output: "dcbabcd" """

    def shortestPalindrome(self, s: str) -> str:
        ss = s + "#" + s[::-1]
        lps = [0]*len(ss) #longest prefix suffix array
        k = 0
        for i in range(1, len(ss)):
            while k and ss[k] != ss[i]: 
                k = lps[k-1]
            if ss[k] == ss[i]: k += 1
            lps[i] = k
        return s[k:][::-1] + s


    """215. Kth Largest Element in an Array (Medium)
	Find the kth largest element in an unsorted array. Note that it is the kth 
	largest element in the sorted order, not the kth distinct element.

	Example 1:
	Input: [3,2,1,5,6,4] and k = 2
	Output: 5

	Example 2:
	Input: [3,2,3,1,2,4,5,5,6] and k = 4
	Output: 4

	Note: You may assume k is always valid, 1 ≤ k ≤ array's length."""

    def findKthLargest(self, nums: List[int], k: int) -> int:
        h = []
        for x in nums: 
            heappush(h, x)
            if len(h) > k: heappop(h)
        return h[0]


    """216. Combination Sum III (Medium)
	Find all possible combinations of k numbers that add up to a number n, 
	given that only numbers from 1 to 9 can be used and each combination should 
	be a unique set of numbers.

	Note: All numbers will be positive integers. The solution set must not 
	contain duplicate combinations.

	Example 1:
	Input: k = 3, n = 7
	Output: [[1,2,4]]

	Example 2:
	Input: k = 3, n = 9
	Output: [[1,2,6], [1,3,5], [2,3,4]]"""

    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        
        def fn(n, i=1):
            """Populate ans with a stack."""
            if n == 0 and len(stack) == k: return ans.append(stack.copy())
            if n < 0 or len(stack) == k: return 
            for nn in range(i, 10):
                stack.append(nn)
                fn(n-nn, nn+1)
                stack.pop()
            
        ans, stack = [], []
        fn(n)
        return ans 


    """217. Contains Duplicate (Easy)
	Given an array of integers, find if the array contains any duplicates. Your 
	function should return true if any value appears at least twice in the 
	array, and it should return false if every element is distinct.

	Example 1:
	Input: [1,2,3,1]
	Output: true

	Example 2:
	Input: [1,2,3,4]
	Output: false

	Example 3:
	Input: [1,1,1,3,3,4,3,2,4,2]
	Output: true"""

    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))


    """218. The Skyline Problem (Hard)
	A city's skyline is the outer contour of the silhouette formed by all the 
	buildings in that city when viewed from a distance. Now suppose you are 
	given the locations and height of all the buildings as shown on a cityscape 
	photo (Figure A), write a program to output the skyline formed by these 
	buildings collectively (Figure B).

	Buildings Skyline Contour
	The geometric information of each building is represented by a triplet of 
	integers [Li, Ri, Hi], where Li and Ri are the x coordinates of the left 
	and right edge of the ith building, respectively, and Hi is its height. It 
	is guaranteed that 0 ≤ Li, Ri ≤ INT_MAX, 0 < Hi ≤ INT_MAX, and Ri - Li > 0. 
	You may assume all buildings are perfect rectangles grounded on an 
	absolutely flat surface at height 0. For instance, the dimensions of all 
	buildings in Figure A are recorded as: [ [2 9 10], [3 7 15], [5 12 12], 
	[15 20 10], [19 24 8] ]. The output is a list of "key points" (red dots in 
	Figure B) in the format of [ [x1,y1], [x2, y2], [x3, y3], ... ] that 
	uniquely defines a skyline. A key point is the left endpoint of a 
	horizontal line segment. Note that the last key point, where the rightmost 
	building ends, is merely used to mark the termination of the skyline, and 
	always has zero height. Also, the ground in between any two adjacent 
	buildings should be considered part of the skyline contour. For instance, 
	the skyline in Figure B should be represented as:[ [2 10], [3 15], [7 12], 
	[12 0], [15 10], [20 8], [24, 0] ].

	Notes:
	The number of buildings in any input list is guaranteed to be in the range 
	[0, 10000]. The input list is already sorted in ascending order by the left 
	x position Li. The output list must be sorted by the x position. There must 
	be no consecutive horizontal lines of equal height in the output skyline. 
	For instance, [...[2 3], [4 5], [7 5], [11 5], [12 7]...] is not acceptable; 
	the three lines of height 5 should be merged into one in the final output as 
	such: [...[2 3], [4 5], [12 7], ...]"""

    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        ans, hp = [], [] #front of heap => current height 
        buildings.append([inf, inf, 0]) #trick
        for li, ri, hi in buildings:
            #down-slope
            while hp and -hp[0][1] < li:                  #current height cannot reach li
                _, rj = heappop(hp)                       #current height ends at rj
                while hp and -hp[0][1] <= -rj: heappop(hp) #useless height ends earlier than rj
                hj = hp[0][0] if hp else 0                #next height
                ans.append((-rj, -hj))
            #up-slope 
            if hi > 0 and (not hp or -hp[0][0] < hi):     #new height higher than current height
                if ans and ans[-1][0] == li: ans.pop()    #same left => update in-place 
                ans.append([li, hi])
            heappush(hp, (-hi, -ri))
        return ans 


    """219. Contains Duplicate II (Easy)
	Given an array of integers and an integer k, find out whether there are two 
	distinct indices i and j in the array such that nums[i] = nums[j] and the 
	absolute difference between i and j is at most k.

	Example 1:
	Input: nums = [1,2,3,1], k = 3
	Output: true

	Example 2:
	Input: nums = [1,0,1,1], k = 1
	Output: true

	Example 3:
	Input: nums = [1,2,3,1,2,3], k = 2
	Output: false"""

    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = dict()
        for i, x in enumerate(nums):
            if x in seen and i - seen[x] <= k: return True 
            seen[x] = i
        return False 


    """220. Contains Duplicate III (Medium)
	Given an array of integers, find out whether there are two distinct indices 
	i and j in the array such that the absolute difference between nums[i] and 
	nums[j] is at most t and the absolute difference between i and j is at most 
	k.

	Example 1:
	Input: nums = [1,2,3,1], k = 3, t = 0
	Output: true

	Example 2:
	Input: nums = [1,0,1,1], k = 1, t = 2
	Output: true

	Example 3:
	Input: nums = [1,5,9,1,5,9], k = 2, t = 3
	Output: false"""

    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        if t < 0: return False #edge case 
        seen = dict()
        for i in range(len(nums)):
            bkt = nums[i]//(t + 1) #bucket 
            if any(bkt+ii in seen and abs(nums[i]-seen[bkt+ii]) <= t for ii in (-1, 0, 1)): return True 
            seen[bkt] = nums[i]
            if i >= k: seen.pop(nums[i-k]//(t+1)) #memory of length k
        return False 


    """221. Maximal Square (Medium)
	Given a 2D binary matrix filled with 0's and 1's, find the largest square 
	containing only 1's and return its area.

	Example:
	Input: 
	1 0 1 0 0
	1 0 1 1 1
	1 1 1 1 1
	1 0 0 1 0
	Output: 4"""

    def maximalSquare(self, matrix: List[List[str]]) -> int:
        
        @lru_cache(None)
        def fn(i, j):
            """Return the length of max square ending at (i, j)."""
            if i < 0 or j < 0 or matrix[i][j] == "0": return 0
            return 1 + min(fn(i-1, j-1), fn(i-1, j), fn(i, j-1))
        
        return max((fn(i, j) for i in range(len(matrix)) for j in range(len(matrix[0]))), default=0)**2


    """222. Count Complete Tree Nodes (Medium)
	Given a complete binary tree, count the number of nodes. Note the 
	definition of a complete binary tree from Wikipedia: in a complete binary
	tree every level, except possibly the last, is completely filled, and all 
	nodes in the last level are as far left as possible. It can have between 1 
	and 2h nodes inclusive at the last level h.

	Example:
	Input: 
	    1
	   / \
	  2   3
	 / \  /
	4  5 6
	Output: 6"""

    def countNodes(self, root: TreeNode) -> int:
        
        def ht(node):
            """Return height of given node."""
            n = 0
            while node: n, node = n+1, node.left
            return n
        
        def fn(node):
            """Return number of nodes in the tree rooted at given node."""
            if not node: return 0
            h = ht(node.left)
            if h == ht(node.right): return 2**h + fn(node.right)
            else: return 2**(h-1) + fn(node.left)
            
        return fn(root)


    """223. Rectangle Area (Medium)
	Find the total area covered by two rectilinear rectangles in a 2D plane. 
	Each rectangle is defined by its bottom left corner and top right corner as 
	shown in the figure.

	Example:
	Input: A = -3, B = 0, C = 3, D = 4, E = 0, F = -1, G = 9, H = 2
	Output: 45

	Note: Assume that the total area is never beyond the maximum possible value 
	of int."""

    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        area1 = (C-A) * (D-B)
        area2 = (G-E) * (H-F)
        overlap = max(0, min(C, G) - max(A, E)) * max(0, min(D, H) - max(B, F))
        return area1 + area2 - overlap


    """224. Basic Calculator (Hard)
	Implement a basic calculator to evaluate a simple expression string. The 
	expression string may contain open ( and closing parentheses ), the plus + 
	or minus sign -, non-negative integers and empty spaces .

	Example 1:
	Input: "1 + 1"
	Output: 2

	Example 2:
	Input: " 2-1 + 2 "
	Output: 3

	Example 3:
	Input: "(1+(4+5+2)-3)+(6+8)"
	Output: 23

	Note:
	You may assume that the given expression is always valid.
	Do not use the eval built-in library function."""

    def calculate(self, s: str) -> int:
        ans, sign, val = 0, 1, 0
        stack = []
        for c in s:
            if c.isdigit():
                val = 10*val + int(c)
            elif c in "+-":
                ans += sign * val
                sign = 1 if c == "+" else -1
                val = 0
            elif c == "(":
                stack.append(ans)
                stack.append(sign)
                ans, sign = 0, 1
            elif c == ")":
                ans += sign * val
                ans *= stack.pop()
                ans += stack.pop()
                sign, val = 1, 0
        return ans + sign * val 


    """226. Invert Binary Tree (Easy)
	Invert a binary tree.

	Example:
	Input:
	     4
	   /   \
	  2     7
	 / \   / \
	1   3 6   9

	Output:

	     4
	   /   \
	  7     2
	 / \   / \
	9   6 3   1
	
	Trivia: This problem was inspired by this original tweet by Max Howell:
	Google: 90% of our engineers use the software you wrote (Homebrew), but you 
	can’t invert a binary tree on a whiteboard so f*** off."""

    def invertTree(self, root: TreeNode) -> TreeNode:
        
        def fn(node):
            """Return root of tree that is inverted"""
            if not node: return 
            node.left, node.right = fn(node.right), fn(node.left)
            return node 
        
        return fn(root)


    """227. Basic Calculator II (Medium)
	Implement a basic calculator to evaluate a simple expression string. The 
	expression string contains only non-negative integers, +, -, *, / operators 
	and empty spaces . The integer division should truncate toward zero.

	Example 1:
	Input: "3+2*2"
	Output: 7

	Example 2:
	Input: " 3/2 "
	Output: 1

	Example 3:
	Input: " 3+5 / 2 "
	Output: 5

	Note:
	You may assume that the given expression is always valid. Do not use the 
	eval built-in library function."""

    def calculate(self, s: str) -> int:
        op, val = "+", 0
        stack = []
        for i, c in enumerate(s): 
            if c.isdigit(): val = 10*val + int(c)
            if i == len(s) - 1 or c in "+-*/": 
                if   op == "+": stack.append(val)
                elif op == "-": stack.append(-val)
                elif op == "*": stack.append(stack.pop()*val)
                elif op == "/": stack.append(int(stack.pop()/val))
                op, val = c, 0
        return sum(stack)


    """228. Summary Ranges (Medium)
	Given a sorted integer array without duplicates, return the summary of its 
	ranges.

	Example 1:
	Input:  [0,1,2,4,5,7]
	Output: ["0->2","4->5","7"]
	Explanation: 0,1,2 form a continuous range; 4,5 form a continuous range.

	Example 2:
	Input:  [0,2,3,4,6,8,9]
	Output: ["0","2->4","6","8->9"]
	Explanation: 2,3,4 form a continuous range; 8,9 form a continuous range."""

    def summaryRanges(self, nums: List[int]) -> List[str]:
        ans = []
        for i, x in enumerate(nums):
            if not i or nums[i-1]+1 != x: val = [x] #start of a range
            if i == len(nums)-1 or x+1 != nums[i+1]: 
                if val[-1] != x: val.append(x) #end of a range
                ans.append(val)
        return ["->".join(map(str, x)) for x in ans]


    """229. Majority Element II (Medium)
	Given an integer array of size n, find all elements that appear more than 
	⌊ n/3 ⌋ times. Note: The algorithm should run in linear time and in O(1) 
	space.

	Example 1:
	Input: [3,2,3]
	Output: [3]

	Example 2:
	Input: [1,1,1,3,3,2,2,2]
	Output: [1,2]"""

    def majorityElement(self, nums: List[int]) -> List[int]:
        ans, vote = [None]*2, [0]*2
        for x in nums: 
            if vote[0] == 0 and x not in ans: ans[0] = x
            elif vote[1] == 0 and x not in ans: ans[1] = x
            
            if ans[0] == x: vote[0] += 1
            elif ans[1] == x: vote[1] += 1
            else: vote = [x-1 for x in vote]
        return [x for x in ans if nums.count(x) > len(nums)//3]


    """230. Kth Smallest Element in a BST (Medium)
	Given a binary search tree, write a function kthSmallest to find the kth 
	smallest element in it.

	Example 1:
	Input: root = [3,1,4,null,2], k = 1
	   3
	  / \
	 1   4
	  \
	   2
	Output: 1

	Example 2:
	Input: root = [5,3,6,2,4,null,null,1], k = 3
	       5
	      / \
	     3   6
	    / \
	   2   4
	  /
	 1
	Output: 3

	Follow up: What if the BST is modified (insert/delete operations) often and 
	you need to find the kth smallest frequently? How would you optimize the 
	kth Smallest routine?

	Constraints:
	The number of elements of the BST is between 1 to 10^4.
	You may assume k is always valid, 1 ≤ k ≤ BST's total elements."""

    def kthSmallest(self, root: TreeNode, k: int) -> int:
        node = root
        stack = []
        while node or stack:
            if node:
                stack.append(node)
                node = node.left
                continue
            node = stack.pop()
            if not (k := k-1): break
            node = node.right
        return node.val 


    """231. Power of Two (Easy)
	Given an integer, write a function to determine if it is a power of two.

	Example 1:
	Input: 1
	Output: true 
	Explanation: 20 = 1

	Example 2:
	Input: 16
	Output: true
	Explanation: 24 = 16

	Example 3:
	Input: 218
	Output: false"""

    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and n & (n-1) == 0


    """233. Number of Digit One (Hard)
	Given an integer n, count the total number of digit 1 appearing in all non-
	negative integers less than or equal to n.

	Example:
	Input: 13
	Output: 6 

	Explanation: Digit 1 occurred in the following numbers: 1, 10, 11, 12, 13."""

    def countDigitOne(self, n: int) -> int:
        if n < 0: return 0 #edge case 
        
        ans = digit = tail = 0
        magn = 1 #magnitude 
        while n: 
            tail = digit * magn//10 + tail #move digit to tail 
            n, digit = divmod(n, 10) #seprate digit from head 
            
            ans += n * magn
            if digit > 1: ans += magn
            elif digit == 1: ans += tail + 1 #tail + 1 considering 000...
                
            magn *= 10
        return ans 


    """234. Palindrome Linked List (Easy)
	Given a singly linked list, determine if it is a palindrome.

	Example 1:
	Input: 1->2
	Output: false

	Example 2:
	Input: 1->2->2->1
	Output: true

	Follow up: Could you do it in O(n) time and O(1) space?"""

    def isPalindrome(self, head: ListNode) -> bool:
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next 
            
        prev = None
        while slow: slow.next, slow, prev = prev, slow.next, slow
        
        while prev and head.val == prev.val: 
            head = head.next
            prev = prev.next 
        
        return not prev 


    """235. Lowest Common Ancestor of a Binary Search Tree (Easy)
	Given a binary search tree (BST), find the lowest common ancestor (LCA) of 
	two given nodes in the BST. According to the definition of LCA on 
	Wikipedia: "The lowest common ancestor is defined between two nodes p and q 
	as the lowest node in T that has both p and q as descendants (where we 
	allow a node to be a descendant of itself)."

	Given binary search tree:  root = [6,2,8,0,4,7,9,null,null,3,5]

	Example 1:
	Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
	Output: 6
	Explanation: The LCA of nodes 2 and 8 is 6.

	Example 2:
	Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
	Output: 2
	Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a 
	descendant of itself according to the LCA definition.

	Constraints:
	All of the nodes' values will be unique.
	p and q are different and both values will exist in the BST."""

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val > q.val: p, q = q, p
        node = root
        while node: 
            if node.val < p.val: node = node.right
            elif p.val <= node.val <= q.val: return node
            else: node = node.left


    """236. Lowest Common Ancestor of a Binary Tree (Medium)
	Given a binary tree, find the lowest common ancestor (LCA) of two given 
	nodes in the tree. According to the definition of LCA on Wikipedia: “The 
	lowest common ancestor is defined between two nodes p and q as the lowest 
	node in T that has both p and q as descendants (where we allow a node to be 
	a descendant of itself).” Given the following binary tree:  

	root = [3,5,1,6,2,0,8,null,null,7,4]

	Example 1:
	Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
	Output: 3
	Explanation: The LCA of nodes 5 and 1 is 3.

	Example 2:
	Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
	Output: 5
	Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a 
	             descendant of itself according to the LCA definition.

	Note:
	All of the nodes' values will be unique.
	p and q are different and both values will exist in the binary tree."""

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def fn(node): 
            """Return LCA of p and q in the tree rooted at node."""
            if not node or node in (p, q): return node
            left, right = fn(node.left), fn(node.right)
            return node if left and right else left or right
        
        return fn(root)


    """237. Delete Node in a Linked List (Easy)
	Write a function to delete a node (except the tail) in a singly linked 
	list, given only access to that node. Given linked list -- 
	head = [4,5,1,9], which looks like following:

    4 -> 5 -> 1 -> 9

	Example 1:
	Input: head = [4,5,1,9], node = 5
	Output: [4,1,9]
	Explanation: You are given the second node with value 5, the linked list 
	should become 4 -> 1 -> 9 after calling your function.

	Example 2:
	Input: head = [4,5,1,9], node = 1
	Output: [4,5,9]
	Explanation: You are given the third node with value 1, the linked list 
	should become 4 -> 5 -> 9 after calling your function.

	Note:
	* The linked list will have at least two elements.
	* All of the nodes' values will be unique.
	* The given node will not be the tail and it will always be a valid node of
	  the linked list.
	* Do not return anything from your function."""

    def deleteNode(self, node):
        node.val = node.next.val 
        node.next = node.next.next 


    """238. Product of Array Except Self (Medium)
	Given an array nums of n integers where n > 1,  return an array output 
	such that output[i] is equal to the product of all the elements of nums 
	except nums[i].

	Example:
	Input:  [1,2,3,4]
	Output: [24,12,8,6]

	Constraint: 
	It's guaranteed that the product of the elements of any prefix or suffix of 
	the array (including the whole array) fits in a 32 bit integer.

	Note: Please solve it without division and in O(n).

	Follow up:
	Could you solve it with constant space complexity? (The output array does 
	not count as extra space for the purpose of space complexity analysis.)"""

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1] * len(nums)
        prefix = suffix = 1
        for i in range(len(nums)):
            ans[i] *= prefix 
            prefix *= nums[i]
            ans[~i] *= suffix 
            suffix *= nums[~i]
        return ans 


    """239. Sliding Window Maximum (Hard)
	Given an array nums, there is a sliding window of size k which is moving 
	from the very left of the array to the very right. You can only see the k 
	numbers in the window. Each time the sliding window moves right by one 
	position. Return the max sliding window.

	Follow up: Could you solve it in linear time?

	Example:
	Input: nums = [1,3,-1,-3,5,3,6,7], and k = 3
	Output: [3,3,5,5,6,7] 
	Explanation: 

	Window position                Max
	---------------               -----
	[1  3  -1] -3  5  3  6  7       3
	 1 [3  -1  -3] 5  3  6  7       3
	 1  3 [-1  -3  5] 3  6  7       5
	 1  3  -1 [-3  5  3] 6  7       5
	 1  3  -1  -3 [5  3  6] 7       6
	 1  3  -1  -3  5 [3  6  7]      7

	Constraints:
	* 1 <= nums.length <= 10^5
	* -10^4 <= nums[i] <= 10^4
	* 1 <= k <= nums.length"""

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        queue = deque() #decreasing queue 
        for i, x in enumerate(nums): 
            while queue and queue[-1][1] <= x: queue.pop() #remove redundant 
            queue.append((i, x))
            if queue and queue[0][0] <= i-k: queue.popleft() #remove expired 
            if i+1 >= k: ans.append(queue[0][1])
        return ans 


    """240. Search a 2D Matrix II (Medium)
	Write an efficient algorithm that searches for a target value in an m x n 
	integer matrix. The matrix has the following properties:
	* Integers in each row are sorted in ascending from left to right.
	* Integers in each column are sorted in ascending from top to bottom.

	Example 1:
	Input: matrix = [[ 1, 4, 7,11,15],
	                 [ 2, 5, 8,12,19],
	                 [ 3, 6, 9,16,22],
	                 [10,13,14,17,24],
	                 [18,21,23,26,30]], target = 5
	Output: true

	Example 2:
	Input: matrix = [[ 1, 4, 7,11,15],
	                 [ 2, 5, 8,12,19],
	                 [ 3, 6, 9,16,22],
	                 [10,13,14,17,24],
	                 [18,21,23,26,30]], target = 20
	Output: false

	Constraints:
	* m == matrix.length
	* n == matrix[i].length
	* 1 <= n, m <= 300
	* -10^9 <= matix[i][j] <= 10^9
	* All the integers in each row are sorted in ascending order.
	* All the integers in each column are sorted in ascending order.
	* -10^9 <= target <= 10^9"""

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0]) # dimensions
        i, j = 0, n-1
        while i < m and 0 <= j: 
            if matrix[i][j] == target: return True
            elif matrix[i][j] < target: i += 1
            else: j -= 1
        return False 


    """241. Different Ways to Add Parentheses (Medium)
	Given a string of numbers and operators, return all possible results from 
	computing all the different possible ways to group numbers and operators. 
	The valid operators are +, - and *.

	Example 1:
	Input: "2-1-1"
	Output: [0, 2]
	Explanation: 
	((2-1)-1) = 0 
	(2-(1-1)) = 2

	Example 2:
	Input: "2*3-4*5"
	Output: [-34, -14, -10, -10, 10]
	Explanation: 
	(2*(3-(4*5))) = -34 
	((2*3)-(4*5)) = -14 
	((2*(3-4))*5) = -10 
	(2*((3-4)*5)) = -10 
	(((2*3)-4)*5) = 10"""

    def diffWaysToCompute(self, input: str) -> List[int]:
        #pre-processing to tokenize input 
        tokens = re.split(r'(\D)', input)
        mp = {"+": add, "-": sub, "*": mul}
        for i, token in enumerate(tokens):
            if token.isdigit(): tokens[i] = int(token)
            else: tokens[i] = mp[token]
        
        def fn(lo, hi): 
            """Return possible outcomes of tokens[lo:hi]"""
            if lo+1 == hi: return [tokens[lo]]
            ans = []
            for mid in range(lo+1, hi, 2): 
                ans.extend(tokens[mid](x, y) for x in fn(lo, mid) for y in fn(mid+1, hi))
            return ans
        
        return fn(0, len(tokens))



    """242. Valid Anagram (Easy)
	Given two strings s and t , write a function to determine if t is an 
	anagram of s.

	Example 1:
	Input: s = "anagram", t = "nagaram"
	Output: true

	Example 2:
	Input: s = "rat", t = "car"
	Output: false

	Note: You may assume the string contains only lowercase alphabets.

	Follow up: What if the inputs contain unicode characters? How would you 
	           adapt your solution to such case?"""
    
    def isAnagram(self, s: str, t: str) -> bool:
        freq = [0]*26
        for c in s: freq[ord(c)-97] += 1
        for c in t: freq[ord(c)-97] -= 1
        return all(v == 0 for v in freq)


    """243. Shortest Word Distance (Easy)
	Given a list of words and two words word1 and word2, return the shortest 
	distance between these two words in the list.

	Example:
	Assume that words = ["practice", "makes", "perfect", "coding", "makes"].
	Input: word1 = “coding”, word2 = “practice”
	Output: 3
	Input: word1 = "makes", word2 = "coding"
	Output: 1
	Note: You may assume that word1 does not equal to word2, and word1 and 
	      word2 are both in the list."""

    def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:
        ans = i1 = i2 = inf
        for i, word in enumerate(words):
            if word == word1: i1 = i
            elif word == word2: i2 = i 
            ans = min(ans, abs(i1 - i2))
        return ans 


    """245. Shortest Word Distance III (Medium)
	Given a list of words and two words word1 and word2, return the shortest 
	distance between these two words in the list. word1 and word2 may be the 
	same and they represent two individual words in the list.

	Example:
	Assume that words = ["practice", "makes", "perfect", "coding", "makes"].
	Input: word1 = “makes”, word2 = “coding”
	Output: 1
	Input: word1 = "makes", word2 = "makes"
	Output: 3
	
	Note: You may assume word1 and word2 are both in the list."""

    def shortestWordDistance(self, words: List[str], word1: str, word2: str) -> int:
        ans = i1 = i2 = inf
        for i, word in enumerate(words):
            if word == word1: i1 = i2 if word1 == word2 else i
            if word == word2: i2 = i
            ans = min(ans, abs(i1-i2))
        return ans 


    """246. Strobogrammatic Number (Easy)
	A strobogrammatic number is a number that looks the same when rotated 180 
	degrees (looked at upside down). Write a function to determine if a number 
	is strobogrammatic. The number is represented as a string.

	Example 1:
	Input: num = "69"
	Output: true

	Example 2:
	Input: num = "88"
	Output: true

	Example 3:
	Input: num = "962"
	Output: false

	Example 4:
	Input: num = "1"
	Output: true"""

    def isStrobogrammatic(self, num: str) -> bool:
        mp = {"0":"0", "1":"1", "6":"9", "8":"8", "9":"6"}
        return all(mp.get(num[i]) == num[~i] for i in range(len(num)//2+1))


    """247. Strobogrammatic Number II (Medium)
	A strobogrammatic number is a number that looks the same when rotated 180 
	degrees (looked at upside down). Find all strobogrammatic numbers that are 
	of length = n.

	Example:
	Input:  n = 2
	Output: ["11","69","88","96"]"""

    def findStrobogrammatic(self, n: int) -> List[str]:
        mp = ["00", "11", "69", "88", "96"]
        
        def fn(n):
            """Return strobogrammatic number of length n."""
            if n == 0: return [""]
            if n == 1: return ["0", "1", "8"]
            return [x+y+xx for x, xx in mp for y in fn(n-2)]
        
        ans = fn(n)
        return [x for x in ans if not x.startswith("0")] if n > 1 else ans 


    """249. Group Shifted Strings (Medium)
	Given a string, we can "shift" each of its letter to its successive letter, 
	for example: "abc" -> "bcd". We can keep "shifting" which forms the sequence:
	"abc" -> "bcd" -> ... -> "xyz"
	Given a list of non-empty strings which contains only lowercase alphabets, 
	group all strings that belong to the same shifting sequence.

	Example:
	Input: ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"],
	Output: 
	[
	  ["abc","bcd","xyz"],
	  ["az","ba"],
	  ["acef"],
	  ["a","z"]
	]"""

    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        ans = {}
        for string in strings: 
            key = []
            for i in range(1, len(string)):
                key.append((ord(string[i]) - ord(string[0])) % 26)
            ans.setdefault("#".join(map(str, key)), []).append(string)
        return ans.values()


    """250. Count Univalue Subtrees (Medium)
	Given the root of a binary tree, return the number of uni-value subtrees. A 
	uni-value subtree means all nodes of the subtree have the same value.

	Example 1:
	Input: root = [5,1,5,5,5,null,5]
	Output: 4

	Example 2:
	Input: root = []
	Output: 0

	Example 3:
	Input: root = [5,5,5,5,5,null,5]
	Output: 6

	Constraints:
	* The numbrt of the node in the tree will be in the range [0, 1000].
	* -1000 <= Node.val <= 1000"""

    def countUnivalSubtrees(self, root: TreeNode) -> int:
        if not root: return 0 
        
        def fn(node): 
            """Return count of univalue subtrees of sub-tree rooted at node."""
            lc = rc = 0
            lv = rv = node.val 
            if node.left: lc, lv = fn(node.left)
            if node.right: rc, rv = fn(node.right)
            if lv == rv == node.val: return lc + rc + 1, node.val 
            return lc + rc, None
            
        return fn(root)[0]           


    """252. Meeting Rooms (Easy)
	Given an array of meeting time intervals where intervals[i] = [starti, endi], 
	determine if a person could attend all meetings.

	Example 1:
	Input: intervals = [[0,30],[5,10],[15,20]]
	Output: false

	Example 2:
	Input: intervals = [[7,10],[2,4]]
	Output: true

	Constraints:
	* 0 <= intervals.length <= 10^4
	* intervals[i].length == 2
	* 0 <= starti < endi <= 10^6"""

    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort()
        return all(intervals[i-1][1] <= intervals[i][0] for i in range(1, len(intervals)))


    """253. Meeting Rooms II (Medium)
	Given an array of meeting time intervals intervals where 
	intervals[i] = [starti, endi], return the minimum number of conference 
	rooms required.

	Example 1:
	Input: intervals = [[0,30],[5,10],[15,20]]
	Output: 2

	Example 2:
	Input: intervals = [[7,10],[2,4]]
	Output: 1

	Constraints:
	*1 <= intervals.length <= 104
	*0 <= starti < endi <= 106"""

    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        pq = []
        for x, y in intervals: 
            heappush(pq, (x, +1))
            heappush(pq, (y, -1))
            
        ans = prefix = 0
        while pq: 
            _, x = heappop(pq)
            prefix += x
            ans = max(ans, prefix)
        return ans 


    """254. Factor Combinations (Medium)
	Numbers can be regarded as product of its factors. For example,
	8 = 2 x 2 x 2 = = 2 x 4.
	Write a function that takes an integer n and return all possible 
	combinations of its factors.

	Note:
	* You may assume that n is always positive.
	* Factors should be greater than 1 and less than n.
	
	Example 1:
	Input: 1
	Output: []

	Example 2:
	Input: 37
	Output:[]

	Example 3:
	Input: 12
	Output: [[2, 6],
			 [2, 2, 3],
			 [3, 4]]

	Example 4:
	Input: 32
	Output: [[2, 16],
	         [2, 2, 8],
	         [2, 2, 2, 4],
	         [2, 2, 2, 2, 2],
	         [2, 4, 4],
	         [4, 8]]"""

    def getFactors(self, n: int) -> List[List[int]]:
        factors = [k for k in range(2, int(sqrt(n))+1) if n % k == 0]
        
        def fn(i, n): 
            """Populate ans via a stack."""
            if len(stack) > 0 and stack[-1] <= n: ans.append(stack + [n])
            for ii in range(i, len(factors)):
                if n % factors[ii] == 0: 
                    stack.append(factors[ii])
                    fn(ii, n//factors[ii])
                    stack.pop()
            
        ans, stack = [], []
        fn(0, n)
        return ans 


    """255. Verify Preorder Sequence in Binary Search Tree (Medium)
	Given an array of numbers, verify whether it is the correct preorder 
	traversal sequence of a binary search tree. You may assume each number in 
	the sequence is unique. Consider the following binary search tree: 

	     5
	    / \
	   2   6
	  / \
	 1   3
	
	Example 1:
	Input: [5,2,6,1,3]
	Output: false

	Example 2:
	Input: [5,2,1,3,6]
	Output: true

	Follow up: Could you do it using only constant space complexity?"""

    def verifyPreorder(self, preorder: List[int]) -> bool:
        lo = -inf 
        stack = []
        for x in preorder: 
            if x < lo: return False 
            while stack and stack[-1] < x: lo = stack.pop()
            stack.append(x)
        return True 


    """256. Paint House (Medium)
	There is a row of n houses, where each house can be painted one of three 
	colors: red, blue, or green. The cost of painting each house with a certain 
	color is different. You have to paint all the houses such that no two 
	adjacent houses have the same color. The cost of painting each house with a 
	certain color is represented by a n x 3 cost matrix. For example, 
	costs[0][0] is the cost of painting house 0 with the color red; costs[1][2] 
	is the cost of painting house 1 with color green, and so on... Find the 
	minimum cost to paint all houses.

	Example 1:
	Input: costs = [[17,2,17],[16,16,5],[14,3,19]]
	Output: 10
	Explanation: Paint house 0 into blue, paint house 1 into green, paint house 
	             2 into blue. Minimum cost: 2 + 5 + 3 = 10.

	Example 2:
	Input: costs = []
	Output: 0
	
	Example 3:
	Input: costs = [[7,6,2]]
	Output: 2

	Constraints:
	* costs.length == n
	* costs[i].length == 3
	* 0 <= n <= 100
	* 1 <= costs[i][j] <= 20"""

    def minCost(self, costs: List[List[int]]) -> int:
        
        @lru_cache(None)
        def fn(i, j): 
            """Return min cost of painting ith house w/ jth color."""
            if i == len(costs): return 0 # no more houses to paint 
            return costs[i][j] + min(fn(i+1, jj) for jj in range(3) if j != jj)
            
        return min(fn(0, j) for j in range(3))


    """257. Binary Tree Paths (Easy)
	Given a binary tree, return all root-to-leaf paths.

	Note: A leaf is a node with no children.

	Example:
	Input:

	   1
	 /   \
	2     3
	 \
	  5
	Output: ["1->2->5", "1->3"]

	Explanation: All root-to-leaf paths are: 1->2->5, 1->3"""

    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        
        def fn(node):
            """Populate ans with a stack via backtracking."""
            if not node: return #null node
            stack.append(node.val)
            if node.left is node.right: ans.append("->".join(map(str, stack))) #leaf node
            fn(node.left) or fn(node.right)
            stack.pop()
            
        ans, stack = [], []
        fn(root)
        return ans 


    """258. Add Digits (Easy)
	Given a non-negative integer num, repeatedly add all its digits until the 
	result has only one digit.

	Example:
	Input: 38
	Output: 2 
	Explanation: The process is like: 3 + 8 = 11, 1 + 1 = 2. 
	             Since 2 has only one digit, return it.

	Follow up: Could you do it without any loop/recursion in O(1) runtime?"""

    def addDigits(self, num: int) -> int:
        return num and 1 + (num - 1) % 9


    """259. 3Sum Smaller (Medium)
	Given an array of n integers nums and an integer target, find the number of 
	index triplets i, j, k with 0 <= i < j < k < n that satisfy the condition 
	nums[i] + nums[j] + nums[k] < target. 

	Follow up: Could you solve it in O(n2) runtime?

	Example 1:
	Input: nums = [-2,0,1,3], target = 2
	Output: 2
	Explanation: Because there are two triplets which sums are less than 2:
	[-2,0,1]
	[-2,0,3]

	Example 2:
	Input: nums = [], target = 0
	Output: 0

	Example 3:
	Input: nums = [0], target = 0
	Output: 0

	Constraints:
	* n == nums.length
	* 0 <= n <= 300
	* -100 <= nums[i] <= 100
	* -100 <= target <= 100"""

    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans = 0
        for i in range(len(nums)): 
            lo, hi = i+1, len(nums)-1
            while lo < hi: 
                if nums[i] + nums[lo] + nums[hi] >= target: hi -= 1
                else: 
                    ans += hi - lo
                    lo += 1
        return ans 


    """260. Single Number III (Medium)
	Given an array of numbers nums, in which exactly two elements appear only 
	once and all the other elements appear exactly twice. Find the two elements 
	that appear only once.

	Example:
	Input:  [1,2,1,3,2,5]
	Output: [3,5]

	Note:
	The order of the result is not important. So in the above example, [5, 3] 
	is also correct. Your algorithm should run in linear runtime complexity. 
	Could you implement it using only constant space complexity?"""

    def singleNumber(self, nums: List[int]) -> List[int]:
        diff = reduce(xor, nums)
        diff &= -diff 
        ans = [0]*2
        for x in nums:
            ans[bool(diff & x)] ^= x
        return ans 



    """263. Ugly Number (Easy)
	Write a program to check whether a given number is an ugly number. Ugly 
	numbers are positive numbers whose prime factors only include 2, 3, 5.

	Example 1:
	Input: 6
	Output: true
	Explanation: 6 = 2 × 3

	Example 2:
	Input: 8
	Output: true
	Explanation: 8 = 2 × 2 × 2

	Example 3:
	Input: 14
	Output: false 
	Explanation: 14 is not ugly since it includes another prime factor 7.

	Note:
	* 1 is typically treated as an ugly number.
	* Input is within the 32-bit signed integer range: [−231,  231 − 1]."""

    def isUgly(self, num: int) -> bool:
        if num <= 0: return False #edge case 
        
        for f in 2, 3, 5: 
            while num % f == 0: 
                num //= f
        return num == 1


    """264. Ugly Number II (Medium)
	Write a program to find the n-th ugly number. Ugly numbers are positive 
	numbers whose prime factors only include 2, 3, 5. 

	Example:
	Input: n = 10
	Output: 12
	Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 
	             10 ugly numbers.

	Note:  
	* 1 is typically treated as an ugly number.
	* n does not exceed 1690."""

    def nthUglyNumber(self, n: int) -> int:
        ans = [1]*n
        p2 = p3 = p5 = 0
        for i in range(1, n): 
            ans[i] = min(2*ans[p2], 3*ans[p3], 5*ans[p5])
            if 2*ans[p2] == ans[i]: p2 += 1
            if 3*ans[p3] == ans[i]: p3 += 1
            if 5*ans[p5] == ans[i]: p5 += 1
        return ans[-1]


    """266. Palindrome Permutation (Easy)
	Given a string, determine if a permutation of the string could form a 
	palindrome.

	Example 1:
	Input: "code"
	Output: false

	Example 2:
	Input: "aab"
	Output: true

	Example 3:
	Input: "carerac"
	Output: true"""

    def canPermutePalindrome(self, s: str) -> bool:
        freq = {}
        for c in s: freq[c] = 1 + freq.get(c, 0)
        return sum(v&1 for v in freq.values()) <= 1


    """267. Palindrome Permutation II (Medium)
	Given a string s, return all the palindromic permutations (without 
	duplicates) of it. Return an empty list if no palindromic permutation could 
	be form.

	Example 1:
	Input: "aabb"
	Output: ["abba", "baab"]

	Example 2:
	Input: "abc"
	Output: []"""

    def generatePalindromes(self, s: str) -> List[str]:
        freq = {}
        for c in s: freq[c] = 1 + freq.get(c, 0)
        
        mid = []
        for k, v in freq.items(): 
            if v&1: mid.append(k)
        
        ans = []
        if len(mid) <= 1: 
            
            def fn(x):
                """Populate ans via backtracking."""
                if len(x) == len(s): ans.append(x)
                for k, v in freq.items(): 
                    if v >= 2: 
                        freq[k] -= 2
                        fn(k + x + k)
                        freq[k] += 2
            
            fn(mid.pop() if mid else "")
        return ans 


    """268. Missing Number (Easy)
	Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, 
	find the one that is missing from the array.

	Example 1:
	Input: [3,0,1]
	Output: 2

	Example 2:
	Input: [9,6,4,2,3,5,7,0,1]
	Output: 8

	Note: Your algorithm should run in linear runtime complexity. Could you 
	implement it using only constant extra space complexity?"""

    def missingNumber(self, nums: List[int]) -> int:
        ans = 0
        for i, x in enumerate(nums):
            ans ^= i+1 ^ x
        return ans 


    """270. Closest Binary Search Tree Value (Easy)
	Given a non-empty binary search tree and a target value, find the value in 
	the BST that is closest to the target.

	Note:
	* Given target value is a floating point.
	* You are guaranteed to have only one unique value in the BST that is closest to the target.
	
	Example:
	Input: root = [4,2,5,1,3], target = 3.714286
	    4
	   / \
	  2   5
	 / \
	1   3
	Output: 4"""

    def closestValue(self, root: TreeNode, target: float) -> int:
        ans = inf
        node = root
        while node: 
            if node.val == target: return node.val
            ans = min(ans, node.val, key=lambda x: abs(x-target))
            if node.val < target: node = node.right
            else: node = node.left
        return ans 


    """273. Integer to English Words (Hard)
	Convert a non-negative integer to its english words representation. Given 
	input is guaranteed to be less than 231 - 1.

	Example 1:
	Input: 123
	Output: "One Hundred Twenty Three"

	Example 2:
	Input: 12345
	Output: "Twelve Thousand Three Hundred Forty Five"

	Example 3:
	Input: 1234567
	Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty 
	        Seven"

	Example 4:
	Input: 1234567891
	Output: "One Billion Two Hundred Thirty Four Million Five Hundred Sixty 
	        Seven Thousand Eight Hundred Ninety One" """

    def numberToWords(self, num: int) -> str:
        mp = {1: "One",   11: "Eleven",    10: "Ten", 
              2: "Two",   12: "Twelve",    20: "Twenty", 
              3: "Three", 13: "Thirteen",  30: "Thirty", 
              4: "Four",  14: "Fourteen",  40: "Forty",
              5: "Five",  15: "Fifteen",   50: "Fifty", 
              6: "Six",   16: "Sixteen",   60: "Sixty", 
              7: "Seven", 17: "Seventeen", 70: "Seventy", 
              8: "Eight", 18: "Eighteen",  80: "Eighty",
              9: "Nine",  19: "Nineteen",  90: "Ninety"}
        
        def fn(n):
            """Return English words of n (0-999) in array."""
            if not n: return []
            elif n < 20: return [mp[n]]
            elif n < 100: return [mp[n//10*10]] + fn(n%10)
            else: return [mp[n//100], "Hundred"] + fn(n%100)
        
        ans = []
        for i, unit in zip((9, 6, 3, 0), ("Billion", "Million", "Thousand", "")): 
            n, num = divmod(num, 10**i)
            ans.extend(fn(n))
            if n and unit: ans.append(unit)
        return " ".join(ans) or "Zero"


    """274. H-Index (Medium)
	Given an array of citations (each citation is a non-negative integer) of a 
	researcher, write a function to compute the researcher's h-index. According 
	to the definition of h-index on Wikipedia: "A scientist has index h if h of 
	his/her N papers have at least h citations each, and the other N − h papers 
	have no more than h citations each."

	Example:
	Input: citations = [3,0,6,1,5]
	Output: 3 
	Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and 
	             each of them had received 3, 0, 6, 1, 5 citations respectively. 
	             Since the researcher has 3 papers with at least 3 citations 
	             each and the remaining two with no more than 3 citations each, 
	             her h-index is 3.

	Note: If there are several possible values for h, the maximum one is taken 
	      as the h-index."""

    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        arr = [i-c for i, c in enumerate(citations, 1)]
        return bisect_right(arr, 0) #right-most occurrence of i <= c


    """275. H-Index II (Medium)
	Given an array of citations sorted in ascending order (each citation is a 
	non-negative integer) of a researcher, write a function to compute the 
	researcher's h-index. According to the definition of h-index on Wikipedia: 
	"A scientist has index h if h of his/her N papers have at least h citations 
	each, and the other N − h papers have no more than h citations each."

	Example:
	Input: citations = [0,1,3,5,6]
	Output: 3 
	Explanation: [0,1,3,5,6] means the researcher has 5 papers in total and 
	             each of them had received 0, 1, 3, 5, 6 citations respectively. 
	             Since the researcher has 3 papers with at least 3 citations 
	             each and the remaining two with no more than 3 citations each, 
	             her h-index is 3.

	Note: If there are several possible values for h, the maximum one is taken 
	      as the h-index.

	Follow up:
	This is a follow up problem to H-Index, where citations is now guaranteed 
	to be sorted in ascending order. Could you solve it in logarithmic time 
	complexity?"""

    def hIndex(self, citations: List[int]) -> int:
        lo = 0
        hi = n = len(citations)
        while lo < hi: 
            mid = (lo + hi)//2
            if citations[mid] >= n - mid: hi = mid #less paper than citation 
            else: lo = mid + 1
        return n - lo


    """276. Paint Fence (Easy)
	There is a fence with n posts, each post can be painted with one of the k 
	colors. You have to paint all the posts such that no more than two adjacent 
	fence posts have the same color. Return the total number of ways you can 
	paint the fence.

	Note: n and k are non-negative integers.

	Example:
	Input: n = 3, k = 2
	Output: 6
	Explanation: Take c1 as color 1, c2 as color 2. All possible ways are:

	            post1  post2  post3      
	 -----      -----  -----  -----       
	   1         c1     c1     c2 
	   2         c1     c2     c1 
	   3         c1     c2     c2 
	   4         c2     c1     c1  
	   5         c2     c1     c2
	   6         c2     c2     c1"""

    def numWays(self, n: int, k: int) -> int:
        if not n: return 0
        f0, f1 = k, k*k
        for _ in range(1, n):
            f0, f1 = f1, (k-1)*(f0+f1)
        return f0


    """277. Find the Celebrity (Medium)
	Suppose you are at a party with n people (labeled from 0 to n - 1), and 
	among them, there may exist one celebrity. The definition of a celebrity is 
	that all the other n - 1 people know him/her, but he/she does not know any 
	of them. Now you want to find out who the celebrity is or verify that there 
	is not one. The only thing you are allowed to do is to ask questions like: 
	"Hi, A. Do you know B?" to get information about whether A knows B. You 
	need to find out the celebrity (or verify there is not one) by asking as 
	few questions as possible (in the asymptotic sense). You are given a helper 
	function bool knows(a, b) which tells you whether A knows B. Implement a 
	function int findCelebrity(n). There will be exactly one celebrity if 
	he/she is in the party. Return the celebrity's label if there is a 
	celebrity in the party. If there is no celebrity, return -1.

	Example 1:
	Input: graph = [[1,1,0],[0,1,0],[1,1,1]]
	Output: 1
	Explanation: There are three persons labeled with 0, 1 and 2. graph[i][j] = 1 
	             means person i knows person j, otherwise graph[i][j] = 0 means 
	             person i does not know person j. The celebrity is the person 
	             labeled as 1 because both 0 and 2 know him but 1 does not know 
	             anybody.

	Example 2:
	Input: graph = [[1,0,1],[1,1,0],[0,1,1]]
	Output: -1
	Explanation: There is no celebrity.

	Constraints:
	* n == graph.length
	* n == graph[i].length
	* 2 <= n <= 100
	* graph[i][j] is 0 or 1.
	* graph[i][i] == 1
	 
	Follow up: If the maximum number of allowed calls to the API knows is 3 * n, 
	           could you find a solution without exceeding the maximum number 
	           of calls?"""

    def findCelebrity(self, n: int) -> int:
        k = 0
        for i in range(1, n): 
            if knows(k, i): k = i 
        return k if all(knows(i, k) for i in range(n)) and not any(knows(k, i) for i in range(n) if i != k) else -1

        
    """278. First Bad Version (Easy)
	You are a product manager and currently leading a team to develop a new 
	product. Unfortunately, the latest version of your product fails the 
	quality check. Since each version is developed based on the previous 
	version, all the versions after a bad version are also bad. Suppose you 
	have n versions [1, 2, ..., n] and you want to find out the first bad one, 
	which causes all the following ones to be bad. You are given an API bool 
	isBadVersion(version) which will return whether version is bad. Implement 
	a function to find the first bad version. You should minimize the number of
	calls to the API.

	Example:
	Given n = 5, and version = 4 is the first bad version.
	call isBadVersion(3) -> false
	call isBadVersion(5) -> true
	call isBadVersion(4) -> true

	Then 4 is the first bad version. """

    def firstBadVersion(self, n):
        lo, hi = 1, n #hi is bad 
        while lo < hi: #no need to check lo == hi since hi is bad 
            mid = (lo + hi)//2
            if isBadVersion(mid): hi = mid #hi is bad 
            else: lo = mid + 1
        return lo 


    """279. Perfect Squares (Medium)
	Given a positive integer n, find the least number of perfect square numbers 
	(for example, 1, 4, 9, 16, ...) which sum to n.

	Example 1:
	Input: n = 12
	Output: 3 
	Explanation: 12 = 4 + 4 + 4.

	Example 2:
	Input: n = 13
	Output: 2
	Explanation: 13 = 4 + 9."""

    def numSquares(self, n: int) -> int:
        if int(sqrt(n))**2 == n: return 1
        
        for i in range(1, int(sqrt(n))+1): 
            if int(sqrt(n - i*i))**2 == n - i*i: return 2
        
        while n % 4 == 0: n //= 4
            
        return 4 if n%8 == 7 else 3 #Lagrange four-square theorem & Lagendre three-square theorem


    """280. Wiggle Sort (Medium)
	Given an unsorted array nums, reorder it in-place such that 
	nums[0] <= nums[1] >= nums[2] <= nums[3]....

	Example:
	Input: nums = [3,5,2,1,6,4]
	Output: One possible answer is [3,5,1,6,2,4]"""

    def wiggleSort(self, nums: List[int]) -> None:
        for i in range(len(nums)-1):
            if i & 1 and nums[i] < nums[i+1] or not i&1 and nums[i] > nums[i+1]: 
                nums[i], nums[i+1] = nums[i+1], nums[i]


    """282. Expression Add Operators (Hard)
	Given a string that contains only digits 0-9 and a target value, return 
	all possibilities to add binary operators (not unary) +, -, or * between 
	the digits so they evaluate to the target value.

	Example 1:
	Input: num = "123", target = 6
	Output: ["1+2+3", "1*2*3"] 

	Example 2:
	Input: num = "232", target = 8
	Output: ["2*3+2", "2+3*2"]

	Example 3:
	Input: num = "105", target = 5
	Output: ["1*0+5","10-5"]

	Example 4:
	Input: num = "00", target = 0
	Output: ["0+0", "0-0", "0*0"]

	Example 5:
	Input: num = "3456237490", target = 9191
	Output: []

	Constraints:
	0 <= num.length <= 10
	num only contain digits."""

    def addOperators(self, num: str, target: int) -> List[str]:
        if not num: return [] #edge case
        ops = ["*", "+", "-"]
        
        def fn(i): 
            """Populate ans with a stack via backtracking."""
            stack.append(num[i]) #push operand on stack
            if i == len(num)-1: #last position 
                expr = "".join(stack)
                if eval(expr) == target: ans.append(expr)
            else: 
                for op in ops + [""]:
                    if (len(stack) == 1 or stack[-2] in ops) and stack[-1] == "0" and op == "": continue #standalone 0 
                    stack.append(op) #push operator on stack 
                    fn(i+1)
                    stack.pop() #pop out operator 
            stack.pop() #pop out operand 
        
        ans, stack = [], []
        fn(0)
        return ans 


    """283. Move Zeroes (Easy)
	Given an array nums, write a function to move all 0's to the end of it 
	while maintaining the relative order of the non-zero elements.

	Example:
	Input: [0,1,0,3,12]
	Output: [1,3,12,0,0]

	Note:
	You must do this in-place without making a copy of the array.
	Minimize the total number of operations."""

    def moveZeroes(self, nums: List[int]) -> None:
        lo = 0
        for hi in range(len(nums)):
            if nums[hi]: 
                nums[hi], nums[lo] = nums[lo], nums[hi]
                lo += 1


    """286. Walls and Gates (Medium)
	You are given an m x n grid rooms initialized with these three possible 
	values.
	* -1 A wall or an obstacle.
	* 0 A gate.
	* INF Infinity means an empty room. We use the value 231 - 1 = 2147483647 
	  to represent INF as you may assume that the distance to a gate is less 
	  than 2147483647.
	Fill each empty room with the distance to its nearest gate. If it is 
	impossible to reach a gate, it should be filled with INF.

	Example 1:
	Input: rooms = [[2147483647,        -1,         0,2147483647],
	                [2147483647,2147483647,2147483647,        -1],
	                [2147483647,        -1,2147483647,        -1],
	                [         0,        -1,2147483647,2147483647]]
	Output: [[3,-1,0,1],[2,2,1,-1],[1,-1,2,-1],[0,-1,3,4]]
	
	Example 2:
	Input: rooms = [[-1]]
	Output: [[-1]]

	Example 3:
	Input: rooms = [[2147483647]]
	Output: [[2147483647]]

	Example 4:
	Input: rooms = [[0]]
	Output: [[0]]

	Constraints:
	* m == rooms.length
	* n == rooms[i].length
	* 1 <= m, n <= 250
	* rooms[i][j] is -1, 0, or 231 - 1."""

    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        m, n = len(rooms), len(rooms[0]) # dimensions 
        dist = 0
        queue = [(i, j) for i in range(m) for j in range(n) if rooms[i][j] == 0] 
        while queue: 
            dist += 1
            newq = []
            for i, j in queue: 
                for ii, jj in (i-1, j), (i, j-1), (i, j+1), (i+1, j): 
                    if 0 <= ii < m and 0 <= jj < n and rooms[ii][jj] == 2147483647: 
                        rooms[ii][jj] = dist
                        newq.append((ii, jj))
            queue = newq


    """287. Find the Duplicate Number (Medium)
	Given an array nums containing n + 1 integers where each integer is between 
	1 and n (inclusive), prove that at least one duplicate number must exist. 
	Assume that there is only one duplicate number, find the duplicate one.

	Example 1:
	Input: [1,3,4,2,2]
	Output: 2

	Example 2:
	Input: [3,1,3,4,2]
	Output: 3

	Note:
	* You must not modify the array (assume the array is read only).
	* You must use only constant, O(1) extra space.
	* Your runtime complexity should be less than O(n2).
	* There is only one duplicate number in the array, but it could be repeated 
	  more than once."""

    def findDuplicate(self, nums: List[int]) -> int:
        fast = slow = 0
        while True:
            fast = nums[nums[fast]]
            slow = nums[slow]
            if fast == slow: break 
        fast = 0
        while fast != slow:
            fast = nums[fast]
            slow = nums[slow]
        return slow 


    """289. Game of Life (Medium)
	According to the Wikipedia's article: "The Game of Life, also known simply 
	as Life, is a cellular automaton devised by the British mathematician John 
	Horton Conway in 1970."

	Given a board with m by n cells, each cell has an initial state live (1) or
	dead (0). Each cell interacts with its eight neighbors (horizontal, 
	vertical, diagonal) using the following four rules (taken from the above 
	Wikipedia article):

	* Any live cell with fewer than two live neighbors dies, as if caused by under-population.
	* Any live cell with two or three live neighbors lives on to the next generation.
	* Any live cell with more than three live neighbors dies, as if by over-population..
	* Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
	
	Write a function to compute the next state (after one update) of the board 
	given its current state. The next state is created by applying the above 
	rules simultaneously to every cell in the current state, where births and 
	deaths occur simultaneously.

	Example:
	Input: 
	[
	  [0,1,0],
	  [0,0,1],
	  [1,1,1],
	  [0,0,0]
	]
	Output: 
	[
	  [0,0,0],
	  [1,0,1],
	  [0,1,1],
	  [0,1,0]
	]

	Follow up:
	* Could you solve it in-place? Remember that the board needs to be updated 
	  at the same time: You cannot update some cells first and then use their 
	  updated values to update other cells.
	* In this question, we represent the board using a 2D array. In principle, 
	  the board is infinite, which would cause problems when the active area 
	  encroaches the border of the array. How would you address these problems?"""

    def gameOfLife(self, board: List[List[int]]) -> None:
        m, n = len(board), len(board[0])
        
        for i in range(m):
            for j in range(n):
                nbr = 0 #neighbor of live cells
                for ii in range(i-1, i+2):
                    for jj in range(j-1, j+2):
                        if 0 <= ii < m and 0 <= jj < n and (ii != i or jj != j) and board[ii][jj] in (-1, 1): nbr += 1
                            
                if board[i][j] and (nbr < 2 or nbr > 3): board[i][j] = -1 #overshoot
                elif not board[i][j] and nbr == 3: board[i][j] = 2 #overshoot
                    
        for i in range(m):
            for j in range(n):
                board[i][j] = int(board[i][j] > 0)


    """290. Word Pattern (Easy)
	Given a pattern and a string str, find if str follows the same pattern. 
	Here follow means a full match, such that there is a bijection between 
	a letter in pattern and a non-empty word in str.

	Example 1:
	Input: pattern = "abba", str = "dog cat cat dog"
	Output: true

	Example 2:
	Input:pattern = "abba", str = "dog cat cat fish"
	Output: false

	Example 3:
	Input: pattern = "aaaa", str = "dog cat cat dog"
	Output: false

	Example 4:
	Input: pattern = "abba", str = "dog dog dog dog"
	Output: false

	Notes: You may assume pattern contains only lowercase letters, and str 
	       contains lowercase letters that may be separated by a single space."""

    def wordPattern(self, pattern: str, str: str) -> bool:
        string = str.split()
        return len(pattern) == len(string) and len(set(zip(pattern, string))) == len(set(pattern)) == len(set(string))


    """291. Word Pattern II (Medium)
	Given a pattern and a string s, return true if s matches the pattern. A 
	string s matches a pattern if there is some bijective mapping of single 
	characters to strings such that if each character in pattern is replaced by 
	the string it maps to, then the resulting string is s. A bijective mapping 
	means that no two characters map to the same string, and no character maps 
	to two different strings.

	Example 1:
	Input: pattern = "abab", s = "redblueredblue"
	Output: true
	Explanation: One possible mapping is as follows:
	'a' -> "red"
	'b' -> "blue"

	Example 2:
	Input: pattern = "aaaa", s = "asdasdasdasd"
	Output: true
	Explanation: One possible mapping is as follows:
	'a' -> "asd"

	Example 3:
	Input: pattern = "abab", s = "asdasdasdasd"
	Output: true
	Explanation: One possible mapping is as follows:
	'a' -> "a"
	'b' -> "sdasd"
	Note that 'a' and 'b' cannot both map to "asd" since the mapping is a bijection.

	Example 4:
	Input: pattern = "aabb", s = "xyzabcxzyabc"
	Output: false

	Constraints:
	* 1 <= pattern.length, s.length <= 20
	* pattern and s consist of only lower-case English letters."""

    def wordPatternMatch(self, pattern: str, s: str) -> bool:
        
        def fn(i, k):
            """Return True if pattern[i:] can be mapping to s[k:]"""
            if i == len(pattern): return k == len(s) # boundary condition
            if k == len(s): return i == len(pattern) # boundary condition 
            
            if pattern[i] in mp: 
                if mp[pattern[i]] == s[k:k+len(mp[pattern[i]])] and fn(i+1, k+len(mp[pattern[i]])): return True
                return False
            for kk in range(k+1, len(s)+1): 
                if s[k:kk] not in mp: 
                    mp[pattern[i]] = s[k:kk]
                    mp[s[k:kk]] = pattern[i]
                    if fn(i+1, kk): return True 
                    mp.pop(pattern[i])
                    if pattern[i] != s[k:kk]: mp.pop(s[k:kk])
            return False
        
        mp = {}
        return fn(0, 0)


    """292. Nim Game (Easy)
	You are playing the following Nim Game with your friend: There is a heap of
    stones on the table, each time one of you take turns to remove 1 to 3 
    stones. The one who removes the last stone will be the winner. You will 
    take the first turn to remove the stones. Both of you are very clever and 
    have optimal strategies for the game. Write a function to determine whether 
    you can win the game given the number of stones in the heap.

	Example:
	Input: 4
	Output: false 
	Explanation: If there are 4 stones in the heap, then you will never win the game;
	             No matter 1, 2, or 3 stones you remove, the last stone will always be 
	             removed by your friend."""

    def canWinNim(self, n: int) -> bool:
        return n % 4


    """293. Flip Game (Easy)
	You are playing the following Flip Game with your friend: Given a string 
	that contains only these two characters: + and -, you and your friend take 
	turns to flip two consecutive "++" into "--". The game ends when a person 
	can no longer make a move and therefore the other person will be the winner. 
	Write a function to compute all possible states of the string after one 
	valid move.

	Example:
	Input: s = "++++"
	Output: ["--++",
	         "+--+",
	         "++--"]
	Note: If there is no valid move, return an empty list []."""

    def generatePossibleNextMoves(self, s: str) -> List[str]:
        ans = []
        for i in range(len(s)-1):
            if s[i:i+2] == "++": ans.append(s[:i] + "--" + s[i+2:])
        return ans 


    """294. Flip Game II (Medium)
	You are playing the following Flip Game with your friend: Given a string 
	that contains only these two characters: + and -, you and your friend take 
	turns to flip two consecutive "++" into "--". The game ends when a person 
	can no longer make a move and therefore the other person will be the winner. 
	Write a function to determine if the starting player can guarantee a win.

	Example:
	Input: s = "++++"
	Output: true 
	Explanation: The starting player can guarantee a win by flipping the middle 
	             "++" to become "+--+".

	Follow up: Derive your algorithm's runtime complexity."""

    def canWin(self, s: str) -> bool:
        
        @cache
        def fn(s): 
            """Return True if player can win by playing optimally."""
            if "++" not in s: return False # already lost 
            for i in range(len(s)-1): 
                if s[i:i+2] == "++" and not fn(s[:i] + "--" + s[i+2:]): return True 
            return False 
        
        return fn(s)


    """298. Binary Tree Longest Consecutive Sequence (Medium)
	Given a binary tree, find the length of the longest consecutive sequence 
	path. The path refers to any sequence of nodes from some starting node to 
	any node in the tree along the parent-child connections. The longest 
	consecutive path need to be from parent to child (cannot be the reverse).

	Example 1:
	Input:
	   1
	    \
	     3
	    / \
	   2   4
	        \
	         5
	Output: 3
	Explanation: Longest consecutive sequence path is 3-4-5, so return 3.

	Example 2:
	Input:

	   2
	    \
	     3
	    / 
	   2    
	  / 
	 1
	Output: 2 
	Explanation: Longest consecutive sequence path is 2-3, not 3-2-1, so return 2."""

    def longestConsecutive(self, root: TreeNode) -> int:
        if not root: return 0 # edge case 
        
        ans = 0
        stack = [(root, 1)]
        while stack: 
            node, val = stack.pop()
            ans = max(ans, val)
            if node.left: stack.append((node.left, val+1 if node.left.val == node.val+1 else 1))
            if node.right: stack.append((node.right, val+1 if node.right.val == node.val+1 else 1))
        return ans 


    """299. Bulls and Cows (Easy)
	You are playing the following Bulls and Cows game with your friend: You 
	write down a number and ask your friend to guess what the number is. Each 
	time your friend makes a guess, you provide a hint that indicates how many 
	digits in said guess match your secret number exactly in both digit and 
	position (called "bulls") and how many digits match the secret number but 
	locate in the wrong position (called "cows"). Your friend will use 
	successive guesses and hints to eventually derive the secret number. Write 
	a function to return a hint according to the secret number and friend's 
	guess, use A to indicate the bulls and B to indicate the cows. Please note 
	that both secret number and friend's guess may contain duplicate digits.

	Example 1:
	Input: secret = "1807", guess = "7810"
	Output: "1A3B"
	Explanation: 1 bull and 3 cows. The bull is 8, the cows are 0, 1 and 7.

	Example 2:
	Input: secret = "1123", guess = "0111"
	Output: "1A1B"
	Explanation: The 1st 1 in friend's guess is a bull, the 2nd or 3rd 1 is a cow.

	Note: You may assume that the secret number and your friend's guess only 
	      contain digits, and their lengths are always equal."""

    def getHint(self, secret: str, guess: str) -> str:
        bulls = sum(s == g for s, g in zip(secret, guess))
        cows = sum((Counter(secret) & Counter(guess)).values()) - bulls
        return f"{bulls}A{cows}B"


    """300. Longest Increasing Subsequence (Medium)
	Given an unsorted array of integers, find the length of longest increasing 
	subsequence.

	Example:
	Input: [10,9,2,5,3,7,101,18]
	Output: 4 
	Explanation: The longest increasing subsequence is [2,3,7,101], therefore 
	             the length is 4. 

	Note:
	* There may be more than one LIS combination, it is only necessary for you 
	  to return the length.
	* Your algorithm should run in O(n2) complexity.
	
	Follow up: Could you improve it to O(n log n) time complexity?"""

    def lengthOfLIS(self, nums: List[int]) -> int:
        ans = []
        for x in nums: 
            i = bisect_left(ans, x)
            if i == len(ans): ans.append(x)
            else: ans[i] = x
        return len(ans)



    """306. Additive Number (Medium)
	Additive number is a string whose digits can form additive sequence. A 
	valid additive sequence should contain at least three numbers. Except for 
	the first two numbers, each subsequent number in the sequence must be the 
	sum of the preceding two. Given a string containing only digits '0'-'9', 
	write a function to determine if it's an additive number. Note: Numbers in 
	the additive sequence cannot have leading zeros, so sequence 1, 2, 03 or 1, 
	02, 3 is invalid.

	Example 1:
	Input: "112358"
	Output: true
	Explanation: The digits can form an additive sequence: 1, 1, 2, 3, 5, 8. 
	             1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8

	Example 2:
	Input: "199100199"
	Output: true
	Explanation: The additive sequence is: 1, 99, 100, 199. 
	             1 + 99 = 100, 99 + 100 = 199
	 
	Constraints:
	num consists only of digits '0'-'9'.
	1 <= num.length <= 35

	Follow up: gHow would you handle overflow for very large input integers?"""

    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)
        for i in range(1, n//2+1):
            x = num[:i]
            if x.startswith("0") and len(x) > 1: break #no leading zero 
            for j in range(i+1, min(n-i, (n+i)//2)+1): #i <= n-j and j-i <= n-j
                yy = num[i:j]
                if yy.startswith("0") and len(yy) > 1: break #no leading zero
                
                ii, xx = i, x
                while num.startswith(yy, ii):
                    ii += len(yy)
                    xx, yy = yy, str(int(xx) + int(yy))
                if ii == len(num): return True 
                
        return False 


    """311. Sparse Matrix Multiplication (Medium)
	Given two sparse matrices A and B, return the result of AB. You may assume 
	that A's column number is equal to B's row number.

	Example:
	Input:
	A = [
	  [ 1, 0, 0],
	  [-1, 0, 3]
	]

	B = [
	  [ 7, 0, 0 ],
	  [ 0, 0, 0 ],
	  [ 0, 0, 1 ]
	]

	Output:
	     |  1 0 0 |   | 7 0 0 |   |  7 0 0 |
	AB = | -1 0 3 | x | 0 0 0 | = | -7 0 3 |
	                  | 0 0 1 |

	Constraints:
	* 1 <= A.length, B.length <= 100
	* 1 <= A[i].length, B[i].length <= 100
	* -100 <= A[i][j], B[i][j] <= 100"""

    def multiply(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        m, l, n = len(A), len(B), len(B[0]) # dimensions 
        ans = [[0] * n for _ in range(m)]
        for i in range(m):
            for k in range(l): 
                if A[i][k]: 
                    for j in range(n):
                        ans[i][j] += A[i][k] * B[k][j]
        return ans 


    """313. Super Ugly Number (Medium)
	Write a program to find the nth super ugly number. Super ugly numbers are 
	positive numbers whose all prime factors are in the given prime list 
	primes of size k.

	Example:
	Input: n = 12, primes = [2,7,13,19]
	Output: 32 
	Explanation: [1,2,4,7,8,13,14,16,19,26,28,32] is the sequence of the first 12 
	             super ugly numbers given primes = [2,7,13,19] of size 4.

	Note:
	* 1 is a super ugly number for any given primes.
	* The given numbers in primes are in ascending order.
	* 0 < k ≤ 100, 0 < n ≤ 106, 0 < primes[i] < 1000.
	* The nth super ugly number is guaranteed to fit in a 32-bit signed integer."""

    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        ans = [1]
        hp = [(p, 0) for p in primes]
        heapify(hp)
        
        for _ in range(n-1): 
            ans.append(hp[0][0])
            while hp[0][0] == ans[-1]: 
                p, i = heappop(hp)
                heappush(hp, (p*ans[i+1]//ans[i], i+1))
                
        return ans[-1]


    """314. Binary Tree Vertical Order Traversal (Medium)
	Given the root of a binary tree, return the vertical order traversal of its 
	nodes' values. (i.e., from top to bottom, column by column). If two nodes 
	are in the same row and column, the order should be from left to right.

	Example 1:
	Input: root = [3,9,20,null,null,15,7]
	Output: [[9],[3,15],[20],[7]]

	Example 2:
	Input: root = [3,9,8,4,0,1,7]
	Output: [[4],[9],[3,0,1],[8],[7]]

	Example 3:
	Input: root = [3,9,8,4,0,1,7,null,null,null,2,5]
	Output: [[4],[9,5],[3,0,1],[8,2],[7]]

	Example 4:
	Input: root = []
	Output: []

	Constraints:
	* The number of nodes in the tree is in the range [0, 100].
	* -100 <= Node.val <= 100"""

    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        ans = {}
        queue = [(root, 0)]
        for node, k in queue: 
            if node: 
                ans.setdefault(k, []).append(node.val)
                queue.append((node.left, k-1))
                queue.append((node.right, k+1))
        return [ans[k] for k in sorted(ans)]


    """316. Remove Duplicate Letters (Medium)
	Given a string s, remove duplicate letters so that every letter appears 
	once and only once. You must make sure your result is the smallest in 
	lexicographical order among all possible results. Note: This question is 
	the same as 1081: 
	https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/

	Example 1:
	Input: s = "bcabc"
	Output: "abc"

	Example 2:
	Input: s = "cbacdcbc"
	Output: "acdb"

	Constraints:
	* 1 <= s.length <= 104
	* s consists of lowercase English letters."""

    def removeDuplicateLetters(self, s: str) -> str:
        mp = {c: i for i, c in enumerate(s)}
        stack = []
        for i, c in enumerate(s): 
            if c not in stack: 
                while stack and c < stack[-1] and i < mp[stack[-1]]: stack.pop()
                stack.append(c)
        return "".join(map(str, stack))


    """318. Maximum Product of Word Lengths (Medium)
	Given a string array words, find the maximum value of 
	length(word[i]) * length(word[j]) where the two words do not share common 
	letters. You may assume that each word will contain only lower case letters. 
	If no such two words exist, return 0.

	Example 1:
	Input: ["abcw","baz","foo","bar","xtfn","abcdef"]
	Output: 16 
	Explanation: The two words can be "abcw", "xtfn".

	Example 2:
	Input: ["a","ab","abc","d","cd","bcd","abcd"]
	Output: 4 
	Explanation: The two words can be "ab", "cd".

	Example 3:
	Input: ["a","aa","aaa","aaaa"]
	Output: 0 
	Explanation: No such pair of words.

	Constraints:
	* 0 <= words.length <= 10^3
	* 0 <= words[i].length <= 10^3
	* words[i] consists only of lowercase English letters."""

    def maxProduct(self, words: List[str]) -> int:
        mp = {} #mapping from mask to length
        for word in words: 
            mask = reduce(or_, (1 << ord(c)-97 for c in word), 0)
            mp[mask] = max(len(word), mp.get(mask, 0))
        
        return max((mp[x] * mp[y] for x in mp for y in mp if not x&y), default=0)


    """319. Bulb Switcher (Medium)
	There are n bulbs that are initially off. You first turn on all the bulbs. 
	Then, you turn off every second bulb. On the third round, you toggle every 
	third bulb (turning on if it's off or turning off if it's on). For the i-th 
	round, you toggle every i bulb. For the n-th round, you only toggle the 
	last bulb. Find how many bulbs are on after n rounds.

	Example:
	Input: 3
	Output: 1 

	Explanation: 
	At first, the three bulbs are [off, off, off].
	After first round, the three bulbs are [on, on, on].
	After second round, the three bulbs are [on, off, on].
	After third round, the three bulbs are [on, off, off]. 
	So you should return 1, because there is only one bulb is on."""

    def bulbSwitch(self, n: int) -> int:
        return int(sqrt(n))


    """320. Generalized Abbreviation (Medium)
	A word's generalized abbreviation can be constructed by taking any number 
	of non-overlapping substrings and replacing them with their respective 
	lengths. For example, "abcde" can be abbreviated into "a3e" ("bcd" turned 
	into "3"), "1bcd1" ("a" and "e" both turned into "1"), and "23" ("ab" 
	turned into "2" and "cde" turned into "3"). Given a string word, return a 
	list of all the possible generalized abbreviations of word. Return the 
	answer in any order.

	Example 1:
	Input: word = "word"
	Output: ["4","3d","2r1","2rd","1o2","1o1d","1or1","1ord","w3","w2d","w1r1",
	         "w1rd","wo2","wo1d","wor1","word"]

	Example 2:
	Input: word = "a"
	Output: ["1","a"]

	Constraints:
	* 1 <= word.length <= 15
	* word consists of only lowercase English letters."""

    def generateAbbreviations(self, word: str) -> List[str]:
        
        def fn(i, s="", n=0):
            """Populate ans via backtracking."""
            if i == len(word): return ans.append(s + (str(n) if n else ""))
            fn(i+1, s, n+1)
            fn(i+1, s + (str(n) if n else "") + word[i], 0)
        
        ans = []
        fn(0)
        return ans


    """322. Coin Change (Medium)
	You are given coins of different denominations and a total amount of money 
	amount. Write a function to compute the fewest number of coins that you 
	need to make up that amount. If that amount of money cannot be made up by 
	any combination of the coins, return -1.

	Example 1:
	Input: coins = [1, 2, 5], amount = 11
	Output: 3 
	Explanation: 11 = 5 + 5 + 1

	Example 2:
	Input: coins = [2], amount = 3
	Output: -1

	Note: You may assume that you have an infinite number of each kind of coin."""

    def coinChange(self, coins: List[int], amount: int) -> int:
        
        @cache
        def fn(x):
            """Return fewest number of coins to make up to x."""
            if x == 0: return 0
            if x < 0: return inf
            return min(1 + fn(x - coin) for coin in coins)
        
        return fn(amount) if fn(amount) < inf else -1


	"""323. Number of Connected Components in an Undirected Graph (Medium)
	Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each 
	edge is a pair of nodes), write a function to find the number of connected 
	components in an undirected graph.

	Example 1:
	Input: n = 5 and edges = [[0, 1], [1, 2], [3, 4]]
	     0          3
	     |          |
	     1 --- 2    4 
	Output: 2

	Example 2:
	Input: n = 5 and edges = [[0, 1], [1, 2], [2, 3], [3, 4]]

	     0           4
	     |           |
	     1 --- 2 --- 3
	Output:  1

	Note: You can assume that no duplicate edges will appear in edges. Since 
	      all edges are undirected, [0, 1] is the same as [1, 0] and thus will 
	      not appear together in edges.

	class UnionFind: 
	    def __init__(self, n):
	        self.parent = list(range(n))
	        self.rank = [1]*n
	        self.components = n
	        
	    def find(self, p):
	        if p != self.parent[p]:
	            self.parent[p] = self.find(self.parent[p])
	        return self.parent[p]
	    
	    def union(self, p, q):
	        prt, qrt = self.find(p), self.find(q)
	        if prt == qrt: return False 
	        self.components -= 1
	        if self.rank[prt] > self.rank[qrt]: prt, qrt = qrt, prt
	        self.parent[prt] = qrt
	        self.rank[qrt] += self.rank[prt]
	        return True 
	"""

    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)
        for u, v in edges: 
            uf.union(u, v)
        return uf.components


    """325. Maximum Size Subarray Sum Equals k (Medium)
	Given an array nums and a target value k, find the maximum length of a 
	subarray that sums to k. If there isn't one, return 0 instead.

	Note: The sum of the entire nums array is guaranteed to fit within the 
          32-bit signed integer range.

	Example 1:
	Input: nums = [1, -1, 5, -2, 3], k = 3
	Output: 4 
	Explanation: The subarray [1, -1, 5, -2] sums to 3 and is the longest.
	
	Example 2:
	Input: nums = [-2, -1, 2, 1], k = 1
	Output: 2 
	Explanation: The subarray [-1, 2] sums to 1 and is the longest.
	
	Follow Up: Can you do it in O(n) time?"""

    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        ans = prefix = 0
        seen = {0: -1}
        for i, x in enumerate(nums): 
            prefix += x
            if prefix-k in seen: ans = max(ans, i - seen[prefix-k])
            seen.setdefault(prefix, i)
        return ans 


	"""328. Odd Even Linked List (Medium)
	Given a singly linked list, group all odd nodes together followed by the 
	even nodes. Please note here we are talking about the node number and not 
	the value in the nodes. You should try to do it in place. The program 
	should run in O(1) space complexity and O(nodes) time complexity.

	Example 1:
	Input: 1->2->3->4->5->NULL
	Output: 1->3->5->2->4->NULL

	Example 2:
	Input: 2->1->3->5->6->4->7->NULL
	Output: 2->3->6->7->1->5->4->NULL

	Constraints:
	* The relative order inside both the even and odd groups should remain as 
	  it was in the input.
	* The first node is considered odd, the second node even and so on ...
	* The length of the linked list is between [0, 10^4]."""

    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head: return 
        odd = head
        even = ehead = head.next 
        while even and even.next:
            odd.next = odd.next.next
            even.next = even.next.next 
            odd, even = odd.next, even.next
        odd.next = ehead
        return head 


    """331. Verify Preorder Serialization of a Binary Tree (Medium)
	One way to serialize a binary tree is to use pre-order traversal. When we 
	encounter a non-null node, we record the node's value. If it is a null 
	node, we record using a sentinel value such as #.

	     _9_
	    /   \
	   3     2
	  / \   / \
	 4   1  #  6
	/ \ / \   / \
	# # # #   # #

	For example, the above binary tree can be serialized to the string 
	"9,3,4,#,#,1,#,#,2,#,6,#,#", where # represents a null node. Given a string 
	of comma separated values, verify whether it is a correct preorder traversal 
	serialization of a binary tree. Find an algorithm without reconstructing the 
	tree. Each comma separated value in the string must be either an integer or 
	a character '#' representing null pointer. You may assume that the input 
	format is always valid, for example it could never contain two consecutive 
	commas such as "1,,3".

	Example 1:
	Input: "9,3,4,#,#,1,#,#,2,#,6,#,#"
	Output: true

	Example 2:
	Input: "1,#"
	Output: false

	Example 3:
	Input: "9,#,#,1"
	Output: false"""

    def isValidSerialization(self, preorder: str) -> bool:
        cnt = 1
        for x in preorder.split(","): 
            if cnt == 0: return False #intermediate 
            cnt += 1 if x != "#" else -1
        return cnt == 0  #end result 


    """332. Reconstruct Itinerary (Medium)
	Given a list of airline tickets represented by pairs of departure and 
	arrival airports [from, to], reconstruct the itinerary in order. All of the 
	tickets belong to a man who departs from JFK. Thus, the itinerary must 
	begin with JFK.

	Note:
	If there are multiple valid itineraries, you should return the itinerary 
	that has the smallest lexical order when read as a single string. For 
	example, the itinerary ["JFK", "LGA"] has a smaller lexical order than 
	["JFK", "LGB"]. All airports are represented by three capital letters (IATA 
	code). You may assume all tickets form at least one valid itinerary. One 
	must use all the tickets once and only once.
	
	Example 1:
	Input: [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
	Output: ["JFK", "MUC", "LHR", "SFO", "SJC"]

	Example 2:
	Input: [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
	Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]

	Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"].
	             But it is larger in lexical order."""

    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        digraph = defaultdict(list)
        for u, v in tickets: heappush(digraph[u], v)
            
        def fn(n): 
            """Return Eulerian path via Hierholzer's algo."""
            while digraph.get(n, []): fn(heappop(digraph[n]))
            ans.appendleft(n)
            
        ans = deque()
        fn("JFK")
        return ans 


    """333. Largest BST Subtree (Medium)
	Given the root of a binary tree, find the largest subtree, which is also a 
	Binary Search Tree (BST), where the largest means subtree has the largest 
	number of nodes. A Binary Search Tree (BST) is a tree in which all the 
	nodes follow the below-mentioned properties:
	* The left subtree values are less than the value of their parent (root) 
	  node's value.
	* The right subtree values are greater than the value of their parent 
	  (root) node's value.
	Note: A subtree must include all of its descendants.
	Follow up: Can you figure out ways to solve it with O(n) time complexity?

	Example 1:
	Input: root = [10,5,15,1,8,null,7]
	Output: 3
	Explanation: The Largest BST Subtree in this case is the highlighted one. 
	             The return value is the subtree's size, which is 3.

	Example 2:
	Input: root = [4,2,7,2,3,5,null,2,null,null,null,null,null,1]
	Output: 2

	Constraints:
	* The number of nodes in the tree is in the range [0, 104].
	* -104 <= Node.val <= 104"""

    def largestBSTSubtree(self, root: TreeNode) -> int:
        
        def fn(node):
            """Update largest BST subtree."""
            nonlocal ans 
            if not node: return True, 0, inf, -inf # BST? | size | low | high
            ltf, lsz, llo, lhi = fn(node.left)
            rtf, rsz, rlo, rhi = fn(node.right)
            tf = ltf and rtf and lhi < node.val < rlo
            sz = 1 + lsz + rsz
            if tf: ans = max(ans, sz)
            return tf, sz, min(llo, node.val), max(rhi, node.val)
        
        ans = 0
        fn(root)
        return ans 


    """334. Increasing Triplet Subsequence (Medium)
	Given an unsorted array return whether an increasing subsequence of length 
	3 exists or not in the array. Formally the function should return true if 
	there exists i, j, k such that arr[i] < arr[j] < arr[k] given 
	0 ≤ i < j < k ≤ n-1 else return false.
	
	Note: Your algorithm should run in O(n) time complexity and O(1) space 
	      complexity.

	Example 1:
	Input: [1,2,3,4,5]
	Output: true

	Example 2:
	Input: [5,4,3,2,1]
	Output: false"""

    def increasingTriplet(self, nums: List[int]) -> bool:
        ans = [inf]*2
        for x in nums:
            if x <= ans[0]: ans[0] = x
            elif x <= ans[1]: ans[1] = x
            else: return True 
        return False 


    """337. House Robber III (Medium)
	The thief has found himself a new place for his thievery again. There is 
	only one entrance to this area, called the "root." Besides the root, each 
	house has one and only one parent house. After a tour, the smart thief 
	realized that "all houses in this place forms a binary tree". It will 
	automatically contact the police if two directly-linked houses were broken 
	into on the same night. Determine the maximum amount of money the thief can 
	rob tonight without alerting the police.

	Example 1:
	Input: [3,2,3,null,3,null,1]

	     3
	    / \
	   2   3
	    \   \ 
	     3   1
	Output: 7 
	Explanation: Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.

	Example 2:
	Input: [3,4,5,1,3,null,1]

	     3
	    / \
	   4   5
	  / \   \ 
	 1   3   1
	Output: 9
	Explanation: Maximum amount of money the thief can rob = 4 + 5 = 9."""

    def rob(self, root: TreeNode) -> int:
        
        def fn(node): 
            """Return max money possible of robbing & skipping this house."""
            if not node: return 0, 0 # null node 
            if node.left is node.right: return node.val, 0 # leaf node 
            left, right = fn(node.left), fn(node.right) # post-order traversal 
            return node.val+left[1]+right[1], max(left)+max(right)
        
        return max(fn(root))


    """338. Counting Bits (Medium)
	Given a non negative integer number num. For every numbers i in the range 
	0 ≤ i ≤ num calculate the number of 1's in their binary representation and 
	return them as an array.

	Example 1:
	Input: 2
	Output: [0,1,1]

	Example 2:
	Input: 5
	Output: [0,1,1,2,1,2]

	Follow up:
	* It is very easy to come up with a solution with run time 
	  O(n*sizeof(integer)). But can you do it in linear time O(n) /possibly in 
	  a single pass?
	* Space complexity should be O(n).
	* Can you do it like a boss? Do it without using any builtin function like 
	  __builtin_popcount in c++ or in any other language."""

    def countBits(self, num: int) -> List[int]:
        ans = [0]*(1 + num)
        for i in range(1, num+1): 
            ans[i] = 1 + ans[i&(i-1)]
        return ans 


    """339. Nested List Weight Sum (Easy)
	You are given a nested list of integers nestedList. Each element is either 
	an integer or a list whose elements may also be integers or other lists. 
	The depth of an integer is the number of lists that it is inside of. For 
	example, the nested list [1,[2,2],[[3],2],1] has each integer's value set 
	to its depth. Return the sum of each integer in nestedList multiplied by 
	its depth.

	Example 1:
	Input: nestedList = [[1,1],2,[1,1]]
	Output: 10
	Explanation: Four 1's at depth 2, one 2 at depth 1. 1*2 + 1*2 + 2*1 + 1*2 + 1*2 = 10.

	Example 2:
	Input: nestedList = [1,[4,[6]]]
	Output: 27
	Explanation: One 1 at depth 1, one 4 at depth 2, and one 6 at depth 3. 1*1 + 4*2 + 6*3 = 27.

	Example 3:
	Input: nestedList = [0]
	Output: 0

	Constraints:
	* 1 <= nestedList.length <= 50
	* The values of the integers in the nested list is in the range [-100, 100].
	* The maximum depth of any integer is less than or equal to 50."""

    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        ans = wt = 0
        queue = nestedList
        while queue: 
            wt += 1
            newq = []
            for x in queue: 
                if x.isInteger(): ans += wt * x.getInteger()
                else: newq.extend(x.getList())
            queue = newq
        return ans 


    """340. Longest Substring with At Most K Distinct Characters (Medium)
	Given a string s and an integer k, return the length of the longest 
	substring of s that contains at most k distinct characters.

	Example 1:
	Input: s = "eceba", k = 2
	Output: 3
	Explanation: The substring is "ece" with length 3.

	Example 2:
	Input: s = "aa", k = 1
	Output: 2
	Explanation: The substring is "aa" with length 2.

	Constraints:
	* 1 <= s.length <= 5 * 104
	* 0 <= k <= 50"""

    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        ans = ii = 0
        freq = {}
        for i, c in enumerate(s): 
            freq[c] = 1 + freq.get(c, 0)
            while len(freq) > k: 
                freq[s[ii]] -= 1
                if freq[s[ii]] == 0: freq.pop(s[ii])
                ii += 1
            ans = max(ans, i - ii + 1)
        return ans 


    """343. Integer Break (Medium)
	Given a positive integer n, break it into the sum of at least two positive 
	integers and maximize the product of those integers. Return the maximum 
	product you can get.

	Example 1:
	Input: 2
	Output: 1
	Explanation: 2 = 1 + 1, 1 × 1 = 1.

	Example 2:
	Input: 10
	Output: 36
	Explanation: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36.

	Note: You may assume that n is not less than 2 and not larger than 58."""

    def integerBreak(self, n: int) -> int:
        
        @lru_cache(None)
        def fn(n): 
            """Return the max product by splitting n."""
            if n == 1: return 1
            return max(max(i, fn(i))*max(n-i, fn(n-i)) for i in range(1, n//2+1))
        
        return fn(n)


    """347. Top K Frequent Elements (Medium)
	Given a non-empty array of integers, return the k most frequent elements.

	Example 1:
	Input: nums = [1,1,1,2,2,3], k = 2
	Output: [1,2]

	Example 2:
	Input: nums = [1], k = 1
	Output: [1]

	Note:
	* You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
	* Your algorithm's time complexity must be better than O(n log n), where n 
	  is the array's size.
	* It's guaranteed that the answer is unique, in other words the set of the 
	  top k frequent elements is unique.
	* You can return the answer in any order."""

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = dict()
        for x in nums: freq[x] = 1 + freq.get(x, 0)
        
        bucket = [[] for _ in nums]
        for x, v in freq.items(): bucket[-v].append(x)
            
        ans = []
        for x in bucket: 
            ans.extend(x)
            if len(ans) >= k: break
        return ans 


    """356. Line Reflection (Medium)
	Given n points on a 2D plane, find if there is such a line parallel to 
	y-axis that reflect the given points symmetrically, in other words, answer 
	whether or not if there exists a line that after reflecting all points over 
	the given line the set of the original points is the same that the 
	reflected ones. Note that there can be repeated points.

	Follow up: Could you do better than O(n2) ?

	Example 1:
	Input: points = [[1,1],[-1,1]]
	Output: true
	Explanation: We can choose the line x = 0.

	Example 2:
	Input: points = [[1,1],[-1,-1]]
	Output: false
	Explanation: We can't choose a line.

	Constraints:
	* n == points.length
	* 1 <= n <= 10^4
	* -10^8 <= points[i][j] <= 10^8"""

    def isReflected(self, points: List[List[int]]) -> bool:
        points = {(x, y) for x, y in points}
        avg = sum(x for x, _ in points)/len(points)
        for x, y in points: 
            if (2*avg - x, y) not in points: return False 
        return True 


    """357. Count Numbers with Unique Digits (Medium)
	Given a non-negative integer n, count all numbers with unique digits, x, 
	where 0 ≤ x < 10^n.

	Example:
	Input: 2
	Output: 91 
	Explanation: The answer should be the total numbers in the range of 0 ≤ x < 100, 
	             excluding 11,22,33,44,55,66,77,88,99
	 
	Constraints: 0 <= n <= 8"""

    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0: return 1
        ans, val = 10, 9
        for i in range(1, min(n, 10)): 
            val *= 10 - i 
            ans += val 
        return ans 


    """360. Sort Transformed Array (Medium)
	Given a sorted array of integers nums and integer values a, b and c. Apply 
	a quadratic function of the form f(x) = ax2 + bx + c to each element x in 
	the array. The returned array must be in sorted order. Expected time 
	complexity: O(n)

	Example 1:
	Input: nums = [-4,-2,2,4], a = 1, b = 3, c = 5
	Output: [3,9,15,33]

	Example 2:
	Input: nums = [-4,-2,2,4], a = -1, b = 3, c = 5
	Output: [-23,-5,1,7]"""

    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        nums = [a*x*x + b*x + c for x in nums]
        ans = [None]*len(nums)
        
        lo, hi = 0, len(nums)-1 # 2-pointer 
        i, ii = (-1, -1) if a >= 0 else (0, 1)
        while lo <= hi: 
            if nums[lo] * ii > nums[hi] * ii: 
                ans[i] = nums[hi]
                hi -= 1
            else:
                ans[i] = nums[lo]
                lo += 1
            i += ii 
        return ans 


    """361. Bomb Enemy (Medium)
	Given a 2D grid, each cell is either a wall 'W', an enemy 'E' or empty '0' 
	(the number zero), return the maximum enemies you can kill using one bomb. 
	The bomb kills all the enemies in the same row and column from the planted 
	point until it hits the wall since the wall is too strong to be destroyed.
	Note: You can only put the bomb at an empty cell.

	Example:
	Input: [["0","E","0","0"],["E","0","W","E"],["0","E","0","0"]]
	Output: 3 
	Explanation: For the given grid,
	0 E 0 0 
	E 0 W E 
	0 E 0 0
	Placing a bomb at (1,1) kills 3 enemies."""

    def maxKilledEnemies(self, grid: List[List[str]]) -> int:
        if not grid: return 0 # edge case 
        m, n = len(grid), len(grid[0]) # dimensions 
        
        ans = 0
        cnt = [[0]*n for _ in range(m)]
        up, dn = [0]*n, [0]*n
        
        for i in range(m): 
            lt = rt = 0
            for j in range(n): 
                cnt[i][j] += dn[j] + lt
                cnt[i][~j] += rt 
                cnt[~i][j] += up[j]
                
                if grid[i][j] == "E": lt, dn[j] = lt+1, dn[j]+1
                elif grid[i][j] == "W": lt = dn[j] = 0
                else: ans = max(ans, cnt[i][j])
                    
                if grid[i][~j] == "E": rt += 1
                elif grid[i][~j] == "W": rt = 0
                else: ans = max(ans, cnt[i][~j])
                
                if grid[~i][j] == "E": up[j] += 1
                elif grid[~i][j] == "W": up[j] = 0 
                else: ans = max(ans, cnt[~i][j])
        
        return ans


    """364. Nested List Weight Sum II (Medium)
	Given a nested list of integers, return the sum of all integers in the list 
	weighted by their depth. Each element is either an integer, or a list -- 
	whose elements may also be integers or other lists. Different from the 
	previous question where weight is increasing from root to leaf, now the 
	weight is defined from bottom up. i.e., the leaf level integers have weight 
	1, and the root level integers have the largest weight.

	Example 1:
	Input: [[1,1],2,[1,1]]
	Output: 8 
	Explanation: Four 1's at depth 1, one 2 at depth 2.

	Example 2:
	Input: [1,[4,[6]]]
	Output: 17 
	Explanation: One 1 at depth 3, one 4 at depth 2, and one 6 at depth 1; 
	             1*3 + 4*2 + 6*1 = 17."""    

    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
        ans = val = 0 
        queue = nestedList
        while queue: 
            newq = []
            for x in queue: 
                if x.isInteger(): val += x.getInteger()
                else: newq.extend(x.getList())
            queue = newq
            ans += val
        return ans 


    """365. Water and Jug Problem (Medium)
	You are given two jugs with capacities x and y litres. There is an infinite 
	amount of water supply available. You need to determine whether it is 
	possible to measure exactly z litres using these two jugs. If z liters of 
	water is measurable, you must have z liters of water contained within one 
	or both buckets by the end.

	Operations allowed:
	* Fill any of the jugs completely with water.
	* Empty any of the jugs.
	* Pour water from one jug into another till the other jug is completely full or the first jug itself is empty.
	
	Example 1: (From the famous "Die Hard" example)
	Input: x = 3, y = 5, z = 4
	Output: True

	Example 2:
	Input: x = 2, y = 6, z = 5
	Output: False

	Constraints:
	0 <= x <= 10^6
	0 <= y <= 10^6
	0 <= z <= 10^6"""

    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        if not z: return True #edge case 
        
        def gcd(x, y): 
            """Return greatest common divisor via Euclidean algo"""
            if x < y: x, y = y, x
            while y: x, y = y, x%y
            return x
        
        return z <= x + y and z % gcd(x, y) == 0


    """366. Find Leaves of Binary Tree (Medium)
	Given a binary tree, collect a tree's nodes as if you were doing this: 
	Collect and remove all leaves, repeat until the tree is empty.

	Example:
	Input: [1,2,3,4,5]
	          1
	         / \
	        2   3
	       / \     
	      4   5    
	Output: [[4,5,3],[2],[1]]

	Explanation:
	1. Removing the leaves [4,5,3] would result in this tree:
	          1
	         / 
	        2          
	2. Now removing the leaf [2] would result in this tree:
	          1          

	3. Now removing the leaf [1] would result in the empty tree:
	          []         
	[[3,5,4],[2],[1]], [[3,4,5],[2],[1]], etc, are also consider correct 
	answers since per each level it doesn't matter the order on which elements 
	are returned."""

    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        
        def fn(node):
            """Return height of give node."""
            if not node: return 0 
            h = 1 + max(fn(node.left), fn(node.right))
            seen.setdefault(h, []).append(node.val)
            return h 
        
        seen = {}
        fn(root)
        return seen.values()


    """368. Largest Divisible Subset (Medium)
	Given a set of distinct positive integers, find the largest subset such 
	that every pair (Si, Sj) of elements in this subset satisfies:

	Si % Sj = 0 or Sj % Si = 0.

	If there are multiple solutions, return any subset is fine.

	Example 1:
	Input: [1,2,3]
	Output: [1,2] (of course, [1,3] will also be ok)

	Example 2:
	Input: [1,2,4,8]
	Output: [1,2,4,8]"""

    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        ans = []
        seen = {}
        for i, x in enumerate(nums): 
            seen[x] = [x]
            for ii in range(i): 
                if x % nums[ii] == 0: seen[x] = max(seen[x], seen[nums[ii]] + [x], key=len)
            ans = max(ans, seen[x], key=len)
        return ans 


    """369. Plus One Linked List (Medium)
	Given a non-negative integer represented as a linked list of digits, plus 
	one to the integer. The digits are stored such that the most significant 
	digit is at the head of the list.

	Example 1:
	Input: head = [1,2,3]
	Output: [1,2,4]

	Example 2:
	Input: head = [0]
	Output: [1]

	Constraints:
	* The number of nodes in the linked list is in the range [1, 100].
	* 0 <= Node.val <= 9
	* The number represented by the linked list does not contain leading zeros 
	  except for the zero itself. """

    def plusOne(self, head: ListNode) -> ListNode:
        prev, node = None, head
        while node: 
            if node.val < 9: prev = node
            node = node.next 
        
        if not prev: 
            head = ListNode(1, head)
            node = head.next 
        else: 
            prev.val += 1
            node = prev.next 
            
        while node: 
            node.val = 0
            node = node.next 
        return head 


    """370. Range Addition (Medium)
	Assume you have an array of length n initialized with all 0's and are given 
	k update operations. Each operation is represented as a triplet: 
	[startIndex, endIndex, inc] which increments each element of subarray 
	A[startIndex ... endIndex] (startIndex and endIndex inclusive) with inc. 
	Return the modified array after all k operations were executed.

	Example:
	Input: length = 5, updates = [[1,3,2],[2,4,3],[0,2,-2]]
	Output: [-2,0,3,5,3]
	Explanation:
	Initial state: [0,0,0,0,0]
	After applying operation [1,3,2]: [0,2,2,2,0]
	After applying operation [2,4,3]: [0,2,5,5,3]
	After applying operation [0,2,-2]: [-2,0,3,5,3]"""

    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        ans = [0]*length
        for si, ei, inc in updates: 
            ans[si] += inc
            if ei+1 < length: ans[ei+1] -= inc
        for i in range(1, length): ans[i] += ans[i-1]
        return ans 


    """371. Sum of Two Integers (Medium)
	Calculate the sum of two integers a and b, but you are not allowed to use 
	the operator + and -.

	Example 1:
	Input: a = 1, b = 2
	Output: 3

	Example 2:
	Input: a = -2, b = 3
	Output: 1"""

    def getSum(self, a: int, b: int) -> int:
        mask = 0xffffffff
        while b&mask: 
            a, b = a^b, (a&b) << 1
        return a&mask if b > mask else a 


    """372. Super Pow (Medium)
	Your task is to calculate ab mod 1337 where a is a positive integer and b 
	is an extremely large positive integer given in the form of an array.

	Example 1:
	Input: a = 2, b = [3]
	Output: 8

	Example 2:
	Input: a = 2, b = [1,0]
	Output: 1024"""

    def superPow(self, a: int, b: List[int]) -> int:
        ans = 1
        for bb in b: 
            ans = pow(ans, 10, 1337) * pow(a, bb, 1337)
        return ans % 1337


    """373. Find K Pairs with Smallest Sums (Medium)
	You are given two integer arrays nums1 and nums2 sorted in ascending order 
	and an integer k. Define a pair (u,v) which consists of one element from 
	the first array and one element from the second array. Find the k pairs 
	(u1,v1),(u2,v2) ...(uk,vk) with the smallest sums.

	Example 1:
	Input: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
	Output: [[1,2],[1,4],[1,6]] 
	Explanation: The first 3 pairs are returned from the sequence: 
	             [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]

	Example 2:
	Input: nums1 = [1,1,2], nums2 = [1,2,3], k = 2
	Output: [1,1],[1,1]
	Explanation: The first 2 pairs are returned from the sequence: 
	             [1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]

	Example 3:
	Input: nums1 = [1,2], nums2 = [3], k = 3
	Output: [1,3],[2,3]
	Explanation: All possible pairs are returned from the sequence: [1,3],[2,3]"""

    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        if not nums1 or not nums2: return [] # edge case
        
        hp = [(nums1[0] + nums2[j], 0, j) for j in range(len(nums2))]
        heapify(hp)
        
        ans = []
        while k and hp: 
            k -= 1
            _, i, j = heappop(hp)
            ans.append([nums1[i], nums2[j]])
            if i+1 < len(nums1): heappush(hp, (nums1[i+1] + nums2[j], i+1, j))
        return ans 


    """375. Guess Number Higher or Lower II (Medium)
	We are playing the Guess Game. The game is as follows:
	I pick a number from 1 to n. You have to guess which number I picked. Every 
	time you guess wrong, I'll tell you whether the number I picked is higher 
	or lower. However, when you guess a particular number x, and you guess 
	wrong, you pay $x. You win the game when you guess the number I picked.

	Example:
	n = 10, I pick 8.
	First round:  You guess 5, I tell you that it's higher. You pay $5.
	Second round: You guess 7, I tell you that it's higher. You pay $7.
	Third round:  You guess 9, I tell you that it's lower. You pay $9.
	Game over. 8 is the number I picked. You end up paying $5 + $7 + $9 = $21.

	Given a particular n ≥ 1, find out how much money you need to have to 
	guarantee a win."""

    def getMoneyAmount(self, n: int) -> int:
        
        @lru_cache(None)
        def fn(lo, hi): 
            """The cost of guessing a number where lo <= x <= hi."""
            if lo >= hi: return 0 # no need to guess 
            ans = inf
            for mid in range(lo, hi+1): 
                ans = min(ans, mid + max(fn(lo, mid-1), fn(mid+1, hi)))
            return ans 
        
        return fn(1, n)


    """376. Wiggle Subsequence (Medium)
	A sequence of numbers is called a wiggle sequence if the differences 
	between successive numbers strictly alternate between positive and 
	negative. The first difference (if one exists) may be either positive or 
	negative. A sequence with fewer than two elements is trivially a wiggle 
	sequence. For example, [1,7,4,9,2,5] is a wiggle sequence because the 
	differences (6,-3,5,-7,3) are alternately positive and negative. In 
	contrast, [1,4,7,2,5] and [1,7,4,5,5] are not wiggle sequences, the first 
	because its first two differences are positive and the second because its 
	last difference is zero. Given a sequence of integers, return the length of 
	the longest subsequence that is a wiggle sequence. A subsequence is 
	obtained by deleting some number of elements (eventually, also zero) from 
	the original sequence, leaving the remaining elements in their original 
	order.

	Example 1:
	Input: [1,7,4,9,2,5]
	Output: 6
	Explanation: The entire sequence is a wiggle sequence.

	Example 2:
	Input: [1,17,5,10,13,15,10,5,16,8]
	Output: 7
	Explanation: There are several subsequences that achieve this length. One 
	             is [1,17,10,13,10,16,8].

	Example 3:
	Input: [1,2,3,4,5,6,7,8,9]
	Output: 2

	Follow up: Can you do it in O(n) time?"""

    def wiggleMaxLength(self, nums: List[int]) -> int:
        ans = 1
        prev = 0
        for i in range(1, len(nums)): 
            diff = nums[i] - nums[i-1]
            if prev * diff < 0: ans += 1
            if diff: prev = diff
        return ans + bool(prev)


    """377. Combination Sum IV (Medium)
	Given an integer array with all positive numbers and no duplicates, find 
	the number of possible combinations that add up to a positive integer 
	target.

	Example:
	nums = [1, 2, 3]
	target = 4
	The possible combination ways are:
	(1, 1, 1, 1)
	(1, 1, 2)
	(1, 2, 1)
	(1, 3)
	(2, 1, 1)
	(2, 2)
	(3, 1)
	Note that different sequences are counted as different combinations. 
	Therefore the output is 7.

	Follow up:
	* What if negative numbers are allowed in the given array?
	* How does it change the problem?
	* What limitation we need to add to the question to allow negative numbers?

	Credits: Special thanks to @pbrother for adding this problem and creating 
	         all test cases."""

    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        @lru_cache(None)
        def fn(x):
            """Return number of combinations summing up to target."""
            if x <= 0: return int(x == 0)
            return sum(fn(x - xx) for xx in nums)
        
        return fn(target)


    """378. Kth Smallest Element in a Sorted Matrix (Medium)
	Given a n x n matrix where each of the rows and columns are sorted in 
	ascending order, find the kth smallest element in the matrix. Note that 
	it is the kth smallest element in the sorted order, not the kth distinct 
	element.

	Example:
	matrix = [
	   [ 1,  5,  9],
	   [10, 11, 13],
	   [12, 13, 15]
	],
	k = 8,
	return 13.

	Note: You may assume k is always valid, 1 ≤ k ≤ n2."""

    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        hp = [(matrix[i][0], i, 0) for i in range(n)] # heap 
        heapify(hp)
        for _ in range(k): 
            v, i, j = heappop(hp)
            if j+1 < n: heappush(hp, (matrix[i][j+1], i, j+1))
        return v


    """386. Lexicographical Numbers (Medium)
	Given an integer n, return 1 - n in lexicographical order. For example, 
	given 13, return: [1,10,11,12,13,2,3,4,5,6,7,8,9]. Please optimize your 
	algorithm to use less time and space. The input size may be as large as 
	5,000,000."""

    def lexicalOrder(self, n: int) -> List[int]:
        
        def dfs(x):
            """Pre-order traverse the tree."""
            if x <= n:
                ans.append(x)
                for xx in range(10): dfs(10*x + xx)
        
        ans = []
        for x in range(1, 10): dfs(x)
        return ans 


    """388. Longest Absolute File Path (Medium)
	We will represent the file system as a string where "\n\t" mean a 
	subdirectory of the main directory, "\n\t\t" means a subdirectory of the 
	subdirectory of the main directory and so on. Each folder will be 
	represented as a string of letters and/or digits. Each file will be in the 
	form "s1.s2" where s1 and s2 are strings of letters and/or digits. For 
	example, the file system above is represented as 
	"dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext".

	Given a string input representing the file system in the explained format, 
	return the length of the longest absolute path to a file in the abstracted 
	file system. If there is no file in the system, return 0.

	Example 1:
	Input: input = "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"
	Output: 20
	Explanation: We have only one file and its path is "dir/subdir2/file.ext" of length 20.
	The path "dir/subdir1" doesn't contain any files.

	Example 2:
	Input: input = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
	Output: 32
	Explanation: We have two files:
	"dir/subdir1/file1.ext" of length 21
	"dir/subdir2/subsubdir2/file2.ext" of length 32.
	We return 32 since it is the longest path.

	Example 3:
	Input: input = "a"
	Output: 0
	Explanation: We don't have any files.

	Constraints:
	1 <= input.length <= 104
	input may contain lower-case or upper-case English letters, a new line 
	character '\n', a tab character '\t', a dot '.', a space ' ' or digits."""

    def lengthLongestPath(self, input: str) -> int:
        ans = 0
        prefix = {-1: 0}
        for subd in input.split("\n"): # sub-directory
            depth = subd.count("\t")
            prefix[depth] = prefix[depth-1] + len(subd) - depth # not including delimiter
            if "." in subd: ans = max(ans, prefix[depth] + depth) # including delimiter
        return ans


    """389. Find the Difference (Easy)
	Given two strings s and t which consist of only lowercase letters. String t 
	is generated by random shuffling string s and then add one more letter at a 
	random position. Find the letter that was added in t.

	Example:
	Input: s = "abcd" t = "abcde"
	Output: e
	Explanation: 'e' is the letter that was added."""

    def findTheDifference(self, s: str, t: str) -> str:
        return chr(reduce(xor, map(ord, s+t)))


    """390. Elimination Game (Medium)
	There is a list of sorted integers from 1 to n. Starting from left to right, 
	remove the first number and every other number afterward until you reach 
	the end of the list. Repeat the previous step again, but this time from 
	right to left, remove the right most number and every other number from the 
	remaining numbers. We keep repeating the steps again, alternating left to 
	right and right to left, until a single number remains. Find the last 
	number that remains starting with a list of length n.

	Example:
	Input:
	n = 9,
	1 2 3 4 5 6 7 8 9
	2 4 6 8
	2 6
	6

	Output:
	6"""

    def lastRemaining(self, n: int) -> int:
        if n == 1: return 1
        if n&1: n -= 1
        return n + 2 - 2*self.lastRemaining(n//2)


    """391. Perfect Rectangle (Hard)
	Given N axis-aligned rectangles where N > 0, determine if they all together 
	form an exact cover of a rectangular region. Each rectangle is represented 
	as a bottom-left point and a top-right point. For example, a unit square is 
	represented as [1,1,2,2]. (coordinate of bottom-left point is (1, 1) and 
	top-right point is (2, 2)).

	Example 1:
	rectangles = [[1,1,3,3],
	              [3,1,4,2],
	              [3,2,4,4],
	              [1,3,2,4],
	              [2,3,3,4]]
	Return true. All 5 rectangles together form an exact cover of a rectangular 
	region.

	Example 2:
	rectangles = [[1,1,2,3],
	              [1,3,2,4],
	              [3,1,4,2],
	              [3,2,4,4]]
	Return false. Because there is a gap between the two rectangular regions.

	Example 3:
	rectangles = [[1,1,3,3],
	              [3,1,4,2],
	              [1,3,2,4],
	              [3,2,4,4]]
	Return false. Because there is a gap in the top center.

	Example 4:
	rectangles = [[1,1,3,3],
	              [3,1,4,2],
	              [1,3,2,4],
	              [2,2,4,4]]
	Return false. Because two of the rectangles overlap with each other."""

    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        area = 0
        corner = set()
        X0 = Y0 = inf
        X1 = Y1 = -inf
        for x0, y0, x1, y1 in rectangles: 
            area += (x1-x0)*(y1-y0)
            X0 = min(x0, X0)
            Y0 = min(y0, Y0)
            X1 = max(x1, X1)
            Y1 = max(y1, Y1)
            corner ^= {(x0, y0), (x0, y1), (x1, y0), (x1, y1)}
        return area == (X1-X0)*(Y1-Y0) and corner == {(X0, Y0), (X0, Y1), (X1, Y0), (X1, Y1)}


    """393. UTF-8 Validation (Medium)
	A character in UTF8 can be from 1 to 4 bytes long, subjected to the 
	following rules:
	+ For 1-byte character, the first bit is a 0, followed by its unicode code.
	+ For n-bytes character, the first n-bits are all one's, the n+1 bit is 0, 
	  followed by n-1 bytes with most significant 2 bits being 10.
	
	This is how the UTF-8 encoding would work:

	   Char. number range  |        UTF-8 octet sequence
	      (hexadecimal)    |              (binary)
	   --------------------+---------------------------------------------
	   0000 0000-0000 007F | 0xxxxxxx
	   0000 0080-0000 07FF | 110xxxxx 10xxxxxx
	   0000 0800-0000 FFFF | 1110xxxx 10xxxxxx 10xxxxxx
	   0001 0000-0010 FFFF | 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx
	
	Given an array of integers representing the data, return whether it is a 
	valid utf-8 encoding. Note that input is an array of integers. Only the 
	least significant 8 bits of each integer is used to store the data. This 
	means each integer represents only 1 byte of data.

	Example 1:
	data = [197, 130, 1], which represents the octet sequence: 11000101 10000010 00000001.
	Return true.
	It is a valid utf-8 encoding for a 2-bytes character followed by a 1-byte character.

	Example 2:
	data = [235, 140, 4], which represented the octet sequence: 11101011 10001100 00000100.
	Return false.
	The first 3 bits are all one's and the 4th bit is 0 means it is a 3-bytes character.
	The next byte is a continuation byte which starts with 10 and that's correct.
	But the second continuation byte does not start with 10, so it is invalid."""

    def validUtf8(self, data: List[int]) -> bool:
        cnt = 0 
        for x in data:
            x = bin(x)[2:].zfill(8)
            if cnt: # in the middle of multi-byte 
                if x.startswith("10"): cnt -= 1
                else: return False 
            else: # beginning 
                cnt = x.find("0")
                if cnt == -1 or cnt == 1 or cnt > 4: return False 
                if cnt: cnt -= 1
        return cnt == 0


    """394. Decode String (Medium)
	Given an encoded string, return its decoded string. The encoding rule is: 
	k[encoded_string], where the encoded_string inside the square brackets is 
	being repeated exactly k times. Note that k is guaranteed to be a positive 
	integer. You may assume that the input string is always valid; No extra 
	white spaces, square brackets are well-formed, etc. Furthermore, you may 
	assume that the original data does not contain any digits and that digits 
	are only for those repeat numbers, k. For example, there won't be input 
	like 3a or 2[4].

	Example 1:
	Input: s = "3[a]2[bc]"
	Output: "aaabcbc"

	Example 2:
	Input: s = "3[a2[c]]"
	Output: "accaccacc"

	Example 3:
	Input: s = "2[abc]3[cd]ef"
	Output: "abcabccdcdcdef"

	Example 4:
	Input: s = "abc3[cd]xyz"
	Output: "abccdcdcdxyz" """

    def decodeString(self, s: str) -> str:
        stack = []
        nn = ss = ""
        for c in s: 
            if c == "[": 
                stack.append(ss)
                stack.append(nn)
                nn = ss = ""
            elif c == "]": 
                ss *= int(stack.pop())
                ss = stack.pop() + ss
            elif c.isdigit(): nn += c
            else: ss += c
        return ss


    """395. Longest Substring with At Least K Repeating Characters (Medium)
	Find the length of the longest substring T of a given string (consists of 
	lowercase letters only) such that every character in T appears no less than 
	k times.

	Example 1:
	Input: s = "aaabb", k = 3
	Output: 3
	The longest substring is "aaa", as 'a' is repeated 3 times.

	Example 2:
	Input: s = "ababbc", k = 2
	Output:	5
	The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is repeated 3 times."""

    def longestSubstring(self, s: str, k: int) -> int:
        if not s: return 0 # edge case 
        
        freq = {} # frequency table 
        for c in s: freq[c] = 1 + freq.get(c, 0)
            
        if min(freq.values()) < k: 
            m = min(freq, key=freq.get)
            return max(self.longestSubstring(ss, k) for ss in s.split(m))
        return len(s)


    """396. Rotate Function (Medium)
	Given an array of integers A and let n to be its length. Assume Bk to be 
	an array obtained by rotating the array A k positions clock-wise, we define 
	a "rotation function" F on A as follow:

	F(k) = 0 * Bk[0] + 1 * Bk[1] + ... + (n-1) * Bk[n-1].

	Calculate the maximum value of F(0), F(1), ..., F(n-1).

	Note: n is guaranteed to be less than 105.

	Example:
	A = [4, 3, 2, 6]
	F(0) = (0 * 4) + (1 * 3) + (2 * 2) + (3 * 6) = 0 + 3 + 4 + 18 = 25
	F(1) = (0 * 6) + (1 * 4) + (2 * 3) + (3 * 2) = 0 + 4 + 6 + 6 = 16
	F(2) = (0 * 2) + (1 * 6) + (2 * 4) + (3 * 3) = 0 + 6 + 8 + 9 = 23
	F(3) = (0 * 3) + (1 * 2) + (2 * 6) + (3 * 4) = 0 + 2 + 12 + 12 = 26
	So the maximum value of F(0), F(1), F(2), F(3) is F(3) = 26."""

    def maxRotateFunction(self, A: List[int]) -> int:
        ans = val = sum(i*x for i, x in enumerate(A))
        ss = sum(A)
        for x in reversed(A):
            val += ss - len(A)*x
            ans = max(ans, val)
        return ans 


    """397. Integer Replacement (Medium)
	Given a positive integer n and you can do operations as follow: 
	+ If n is even, replace n with n/2.
	+ If n is odd, you can replace n with either n + 1 or n - 1.
	What is the minimum number of replacements needed for n to become 1?

	Example 1:
	Input: 8
	Output: 3
	Explanation: 8 -> 4 -> 2 -> 1
	
	Example 2:
	Input: 7
	Output: 4
	Explanation: 7 -> 8 -> 4 -> 2 -> 1 or 7 -> 6 -> 3 -> 2 -> 1"""

    def integerReplacement(self, n: int) -> int:
        
        @lru_cache(None)
        def fn(n):
            """Return """
            if n == 1: return 0
            if not n&1: return 1 + fn(n//2)
            return 1 + min(fn(n+1), fn(n-1))
        
        return fn(n)


    """399. Evaluate Division (Medium)
	Equations are given in the format A / B = k, where A and B are variables 
	represented as strings, and k is a real number (floating point number). 
	Given some queries, return the answers. If the answer does not exist, 
	return -1.0.

	Example:
	Given a / b = 2.0, b / c = 3.0.
	queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? .
	return [6.0, 0.5, -1.0, 1.0, -1.0 ].

	The input is: vector<pair<string, string>> equations, vector<double>& values, 
	              vector<pair<string, string>> queries , where equations.size() == values.size(), 
	              and the values are positive. This represents the equations. Return vector<double>.

	According to the example above:
	equations = [ ["a", "b"], ["b", "c"] ],
	values = [2.0, 3.0],
	queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ]. 
	The input is always valid. You may assume that evaluating the queries will 
	result in no division by zero and there is no contradiction."""

    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = {}
        for (u, v), w in zip(equations, values): 
            graph.setdefault(u, []).append((v, 1/w))
            graph.setdefault(v, []).append((u, w))

        def dfs(n, g, val=1):
            """Depth-first traverse the graph."""
            if n in vals: return 
            vals[n] = val, g
            for nn, w in graph.get(n, []): dfs(nn, g, w*val)
    
        vals = dict()
        for i, n in enumerate(graph): dfs(n, i)
        
        ans = []
        for u, v in queries: 
            if u in vals and v in vals and vals[u][1] == vals[v][1]: ans.append(vals[u][0]/vals[v][0])
            else: ans.append(-1)
        return ans 


    """400. Nth Digit (Medium)
	Find the nth digit of the infinite integer sequence 1, 2, 3, 4, 5, 6, 7, 8, 
	9, 10, 11, ... Note that n is positive and will fit within the range of a 
	32-bit signed integer (n < 231).

	Example 1:
	Input: 3
	Output: 3
	
	Example 2:
	Input: 11
	Output: 0
	Explanation: The 11th digit of the sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 
	             11, ... is a 0, which is part of the number 10."""

    def findNthDigit(self, n: int) -> int:
        digit = base = 1 # starting from 1 digit
        while n > 9*base*digit: # upper limit of d digits 
            n -= 9*base*digit
            digit += 1
            base *= 10 
        q, r = divmod(n-1, digit)
        return int(str(base + q)[r])


    """402. Remove K Digits (Medium)
	Given a non-negative integer num represented as a string, remove k digits 
	from the number so that the new number is the smallest possible.

	Note:
	+ The length of num is less than 10002 and will be ≥ k.
	+ The given num does not contain any leading zero.
	
	Example 1:
	Input: num = "1432219", k = 3
	Output: "1219"
	Explanation: Remove the three digits 4, 3, and 2 to form the new number 
	             1219 which is the smallest.

	Example 2:
	Input: num = "10200", k = 1
	Output: "200"
	Explanation: Remove the leading 1 and the number is 200. Note that the 
	             output must not contain leading zeroes.
	
	Example 3:
	Input: num = "10", k = 2
	Output: "0"
	Explanation: Remove all the digits from the number and it is left with 
	             nothing which is 0."""

    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for x in num: 
            while k and stack and stack[-1] > x: 
                k -= 1
                stack.pop()
            stack.append(x) 
        return "".join(stack[:-k or None]).lstrip("0") or "0"


    """406. Queue Reconstruction by Height (Medium)
	Suppose you have a random list of people standing in a queue. Each person 
	is described by a pair of integers (h, k), where h is the height of the 
	person and k is the number of people in front of this person who have a 
	height greater than or equal to h. Write an algorithm to reconstruct the 
	queue. 
	Note: The number of people is less than 1,100.
	 
	Example
	Input: [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
	Output: [[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]"""

    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        ans = []
        for h, k in sorted(people, key=lambda x: (-x[0], x[1])): # tallest to shortest 
            ans.insert(k, [h, k])
        return ans 


    """408. Valid Word Abbreviation (Easy)
	Given a non-empty string s and an abbreviation abbr, return whether the 
	string matches with the given abbreviation. A string such as "word" 
	contains only the following valid abbreviations:
	["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", 
	 "1or1", "w1r1", "1o2", "2r1", "3d", "w3", "4"]
	Notice that only the above abbreviations are valid abbreviations of the 
	string "word". Any other string is not a valid abbreviation of "word".

	Note: Assume s contains only lowercase letters and abbr contains only 
	      lowercase letters and digits.

	Example 1:
	Given s = "internationalization", abbr = "i12iz4n":
	Return true.

	Example 2:
	Given s = "apple", abbr = "a2e":
	Return false."""

    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i = j = 0
        while i < len(word) and j < len(abbr): 
            if abbr[j].isalpha(): 
                if word[i] == abbr[j]: i, j = i+1, j+1
                else: return False 
            else: 
                if abbr[j] == "0": return False # edge case 
                jj = j 
                while j < len(abbr) and abbr[j].isdigit(): j += 1
                i += int(abbr[jj:j])
        return i == len(word) and j == len(abbr)


    """413. Arithmetic Slices (Medium)
	A sequence of numbers is called arithmetic if it consists of at least three 
	elements and if the difference between any two consecutive elements is the 
	same. For example, these are arithmetic sequences:
	1, 3, 5, 7, 9
	7, 7, 7, 7
	3, -1, -5, -9

	The following sequence is not arithmetic: 1, 1, 2, 5, 7. A zero-indexed 
	array A consisting of N numbers is given. A slice of that array is any pair 
	of integers (P, Q) such that 0 <= P < Q < N. A slice (P, Q) of the array A 
	is called arithmetic if the sequence: A[P], A[P + 1], ..., A[Q - 1], A[Q] 
	is arithmetic. In particular, this means that P + 1 < Q. The function 
	should return the number of arithmetic slices in the array A.
	 
	Example:
	A = [1, 2, 3, 4]
	return: 3, for 3 arithmetic slices in A: 
	[1, 2, 3], [2, 3, 4] and [1, 2, 3, 4] itself."""

    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        ans = cnt = 0
        for i in range(2, len(A)): 
            if A[i-2] - A[i-1] == A[i-1] - A[i]: 
                cnt += 1
                ans += cnt 
            else: cnt = 0
        return ans 


    """418. Sentence Screen Fitting (Medium)
	Given a rows x cols screen and a sentence represented by a list of non-
	empty words, find how many times the given sentence can be fitted on the 
	screen.

	Note:
	* A word cannot be split into two lines.
	* The order of words in the sentence must remain unchanged.
	* Two consecutive words in a line must be separated by a single space.
	* Total words in the sentence won't exceed 100.
	* Length of each word is greater than 0 and won't exceed 10.
	* 1 ≤ rows, cols ≤ 20,000.
	
	Example 1:
	Input: rows = 2, cols = 8, sentence = ["hello", "world"]
	Output: 1
	Explanation:
		hello---
		world---
	The character '-' signifies an empty space on the screen.

	Example 2:
	Input: rows = 3, cols = 6, sentence = ["a", "bcd", "e"]
	Output: 2
	Explanation:
		a-bcd- 
		e-a---
		bcd-e-
	The character '-' signifies an empty space on the screen.

	Example 3:
	Input: rows = 4, cols = 5, sentence = ["I", "had", "apple", "pie"]
	Output: 1
	Explanation:
		I-had
		apple
		pie-I
		had--
	The character '-' signifies an empty space on the screen."""

    def wordsTyping(self, sentence: List[str], rows: int, cols: int) -> int:
        ss = " ".join(sentence) + " "
        ans = 0
        for _ in range(rows): 
            ans += cols
            while ss[ans % len(ss)] != " ": ans -= 1
            ans += 1
        return ans // len(ss)


    """422. Valid Word Square (Easy)
	Given a sequence of words, check whether it forms a valid word square. A 
	sequence of words forms a valid word square if the kth row and column read 
	the exact same string, where 0 ≤ k < max(numRows, numColumns).

	Note:
	* The number of words given is at least 1 and does not exceed 500.
	* Word length will be at least 1 and does not exceed 500.
	* Each word contains only lowercase English alphabet a-z.

	Example 1:
	Input: ["abcd",
	        "bnrt",
	        "crmy",
	        "dtye"]
	Output: true
	Explanation:
	The first row and first column both read "abcd".
	The second row and second column both read "bnrt".
	The third row and third column both read "crmy".
	The fourth row and fourth column both read "dtye".
	Therefore, it is a valid word square.

	Example 2:
	Input: ["abcd",
	        "bnrt",
	        "crm",
	        "dt"]
	Output:	true
	Explanation:
	The first row and first column both read "abcd".
	The second row and second column both read "bnrt".
	The third row and third column both read "crm".
	The fourth row and fourth column both read "dt".
	Therefore, it is a valid word square.

	Example 3:
	Input: ["ball",
	        "area",
	        "read",
	        "lady"]
	Output: false
	Explanation:
	The third row reads "read" while the third column reads "lead".
	Therefore, it is NOT a valid word square."""

    def validWordSquare(self, words: List[str]) -> bool:
        return words == ["".join(x) for x in zip_longest(*words, fillvalue="")]


    """426. Convert Binary Search Tree to Sorted Doubly Linked List (Medium)
	Convert a Binary Search Tree to a sorted Circular Doubly-Linked List in 
	place. You can think of the left and right pointers as synonymous to the 
	predecessor and successor pointers in a doubly-linked list. For a circular 
	doubly linked list, the predecessor of the first element is the last 
	element, and the successor of the last element is the first element. We 
	want to do the transformation in place. After the transformation, the left 
	pointer of the tree node should point to its predecessor, and the right 
	pointer should point to its successor. You should return the pointer to the 
	smallest element of the linked list.

	Example 1:
	Input: root = [4,2,5,1,3]
	Output: [1,2,3,4,5]
	Explanation: The figure below shows the transformed BST. The solid line 
	             indicates the successor relationship, while the dashed line 
	             means the predecessor relationship.

	Example 2:
	Input: root = [2,1,3]
	Output: [1,2,3]

	Example 3:
	Input: root = []
	Output: []
	Explanation: Input is an empty tree. Output is also an empty Linked List.

	Example 4:
	Input: root = [1]
	Output: [1]

	Constraints:
	* -1000 <= Node.val <= 1000
	* Node.left.val < Node.val < Node.right.val
	* All values of Node.val are unique.
	* 0 <= Number of Nodes <= 2000"""

    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root: return # edge case 
        
        def fn(node): 
            """Return head & tail of flattened tree."""
            head = tail = node 
            if node.left: 
                head, tail0 = fn(node.left)
                tail0.right = node 
                node.left = tail0
            if node.right:
                head1, tail = fn(node.right)
                node.right = head1
                head1.left = node 
            return head, tail 
        
        head, tail = fn(root)
        head.left = tail
        tail.right = head 
        return head 


    """481. Magical String (Medium)
	A magical string S consists of only '1' and '2' and obeys the following 
	rules:
	The string S is magical because concatenating the number of contiguous 
	occurrences of characters '1' and '2' generates the string S itself. The 
	first few elements of string S is the following: S = "1221121221221121122……"
	If we group the consecutive '1's and '2's in S, it will be:
	1 22 11 2 1 22 1 22 11 2 11 22 ......
	and the occurrences of '1's or '2's in each group are:
	1 2 2 1 1 2 1 2 2 1 2 2 ......
	You can see that the occurrence sequence above is the S itself. Given an 
	integer N as input, return the number of '1's in the first N number in the 
	magical string S.

	Example 1:
	Input: 6
	Output: 3
	Explanation: The first 6 elements of magical string S is "12211" and it 
	             contains three 1's, so return 3.

	Note: N will not exceed 100,000."""

    def magicalString(self, n: int) -> int:
        if n == 0: return 0 # edge case 
        
        S = [1,2,2]
        i = 2
        while len(S) < n: 
            S.extend(S[i] * [3 ^ S[-1]])
            i += 1
        return S[:n].count(1)


    """487. Max Consecutive Ones II (Medium)
	Given a binary array, find the maximum number of consecutive 1s in this 
	array if you can flip at most one 0.

	Example 1:
	Input: [1,0,1,1,0]
	Output: 4
	Explanation: Flip the first zero will get the the maximum number of 
	             consecutive 1s. After flipping, the maximum number of 
	             consecutive 1s is 4.
	
	Note:
	* The input array will only contain 0 and 1.
	* The length of input array is a positive integer and will not exceed 10,000
	
	Follow up: What if the input numbers come in one by one as an infinite 
	           stream? In other words, you can't store all numbers coming from 
	           the stream as it's too large to hold in memory. Could you solve 
	           it efficiently?"""

    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans = curr = 0
        prev = -1
        for x in nums: 
            if x == 0: prev, curr = curr, 0
            else: curr += 1
            ans = max(ans, prev + 1 + curr)
        return ans 


    """510. Inorder Successor in BST II (Medium)
	Given a node in a binary search tree, find the in-order successor of that 
	node in the BST. If that node has no in-order successor, return null. The 
	successor of a node is the node with the smallest key greater than node.val.
	You will have direct access to the node but not to the root of the tree. 
	Each node will have a reference to its parent node. Below is the definition 
	for Node:

	class Node {
	    public int val;
	    public Node left;
	    public Node right;
	    public Node parent;
	}
	Follow up: Could you solve it without looking up any of the node's values?

	Example 1:
	Input: tree = [2,1,3], node = 1
	Output: 2
	Explanation: 1's in-order successor node is 2. Note that both the node and 
	             the return value is of Node type.

	Example 2:
	Input: tree = [5,3,6,2,4,null,null,1], node = 6
	Output: null
	Explanation: There is no in-order successor of the current node, so the 
	             answer is null.
	
	Example 3:
	Input: tree = [15,6,18,3,7,17,20,2,4,null,13,null,null,null,null,null,null,null,null,9], node = 15
	Output: 17

	Example 4:
	Input: tree = [15,6,18,3,7,17,20,2,4,null,13,null,null,null,null,null,null,null,null,9], node = 13
	Output: 15

	Example 5:
	Input: tree = [0], node = 0
	Output: null

	Constraints:
	* -10^5 <= Node.val <= 10^5
	* 1 <= Number of Nodes <= 10^4
	* All Nodes will have unique values."""

    def inorderSuccessor(self, node: 'Node') -> 'Node':
        if node.right: 
            node = node.right
            while node.left: node = node.left
            return node 
        
        while node.parent: 
            if node == node.parent.left: return node.parent
            node = node.parent 


    """513. Find Bottom Left Tree Value (Medium)
	Given a binary tree, find the leftmost value in the last row of the tree.

	Example 1:
	Input:

	    2
	   / \
	  1   3

	Output: 1
	
	Example 2:
	Input:

	        1
	       / \
	      2   3
	     /   / \
	    4   5   6
	       /
	      7

	Output: 7
	Note: You may assume the tree (i.e., the given root node) is not NULL."""

    def findBottomLeftValue(self, root: TreeNode) -> int:
        stack = [(root, 0)]
        ii = -1 
        while stack:
            node, i = stack.pop()
            if i > ii: 
                ii = i
                ans = node.val 
            if node.right: stack.append((node.right, i+1))
            if node.left: stack.append((node.left, i+1))
        return ans 


    """515. Find Largest Value in Each Tree Row (Medium)
	Given the root of a binary tree, return an array of the largest value in 
	each row of the tree (0-indexed).

	Example 1:
	Input: root = [1,3,2,5,3,null,9]
	Output: [1,3,9]

	Example 2:
	Input: root = [1,2,3]
	Output: [1,3]

	Example 3:
	Input: root = [1]
	Output: [1]

	Example 4:
	Input: root = [1,null,2]
	Output: [1,2]

	Example 5:
	Input: root = []
	Output: []

	Constraints:
	* The number of nodes in the tree will be in the range [0, 104].
	* -231 <= Node.val <= 231 - 1"""

    def largestValues(self, root: TreeNode) -> List[int]:
        if not root: return [] # edge case 
        
        ans = []
        stack = [(root, 0)]
        while stack: 
            node, i = stack.pop()
            if i == len(ans): ans.append(node.val)
            else: ans[i] = max(ans[i], node.val)
            if node.left: stack.append((node.left, i+1))
            if node.right: stack.append((node.right, i+1))
        return ans 


    """516. Longest Palindromic Subsequence (Medium)
	Given a string s, find the longest palindromic subsequence's length in s. 
	You may assume that the maximum length of s is 1000.

	Example 1:
	Input: "bbbab"
	Output: 4
	One possible longest palindromic subsequence is "bbbb".
	 
	Example 2:
	Input: "cbbd"
	Output: 2
	One possible longest palindromic subsequence is "bb".

	Constraints:
	* 1 <= s.length <= 1000
	* s consists only of lowercase English letters."""

    def longestPalindromeSubseq(self, s: str) -> int:
        
        @lru_cache(None)
        def fn(lo, hi): 
            """Return longest palindromic subsequence."""
            if lo >= hi: return int(lo == hi)
            if s[lo] == s[hi]: return fn(lo+1, hi-1) + 2
            return max(fn(lo+1, hi), fn(lo, hi-1))
        
        return fn(0, len(s)-1)


    """518. Coin Change 2 (Medium)
	You are given coins of different denominations and a total amount of money. 
	Write a function to compute the number of combinations that make up that 
	amount. You may assume that you have infinite number of each kind of coin.

	Example 1:
	Input: amount = 5, coins = [1, 2, 5]
	Output: 4
	Explanation: there are four ways to make up the amount:
	5=5
	5=2+2+1
	5=2+1+1+1
	5=1+1+1+1+1

	Example 2:
	Input: amount = 3, coins = [2]
	Output: 0
	Explanation: the amount of 3 cannot be made up just with coins of 2.

	Example 3:
	Input: amount = 10, coins = [10] 
	Output: 1

	Note that you can assume that:
	* 0 <= amount <= 5000
	* 1 <= coin <= 5000
	* the number of coins is less than 500
	* the answer is guaranteed to fit into signed 32-bit integer"""

    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort(reverse=True)
        
        @lru_cache(None)
        def fn(x, i=0):
            """Return number of combinations making up x."""
            if x <= 0: return int(x == 0)
            return sum(fn(x-coins[ii], ii) for ii in range(i, len(coins)))
        
        return fn(amount)


    """522. Longest Uncommon Subsequence II (Medium)
	Given a list of strings, you need to find the longest uncommon subsequence 
	among them. The longest uncommon subsequence is defined as the longest 
	subsequence of one of these strings and this subsequence should not be any 
	subsequence of the other strings. A subsequence is a sequence that can be 
	derived from one sequence by deleting some characters without changing the 
	order of the remaining elements. Trivially, any string is a subsequence of 
	itself and an empty string is a subsequence of any string. The input will 
	be a list of strings, and the output needs to be the length of the longest 
	uncommon subsequence. If the longest uncommon subsequence doesn't exist, 
	return -1.

	Example 1:
	Input: "aba", "cdc", "eae"
	Output: 3
	
	Note:
	* All the given strings' lengths will not exceed 10.
	* The length of the given list will be in the range of [2, 50]."""

    def findLUSlength(self, strs: List[str]) -> int:
        
        def fn(p, s): 
            """Return True if p is a subsequence of s."""
            ss = iter(s)
            return all(c in ss for c in p)
        
        strs.sort(key=len, reverse=True)
        
        for i in range(len(strs)): 
            if not any(fn(strs[i], strs[ii]) for ii in range(len(strs)) if i != ii): return len(strs[i])
        return -1


    """523. Continuous Subarray Sum (Medium)
	Given a list of non-negative numbers and a target integer k, write a 
	function to check if the array has a continuous subarray of size at least 2 
	that sums up to a multiple of k, that is, sums up to n*k where n is also an 
	integer.

	Example 1:
	Input: [23, 2, 4, 6, 7],  k=6
	Output: True
	Explanation: Because [2, 4] is a continuous subarray of size 2 and sums up to 6.

	Example 2:
	Input: [23, 2, 6, 4, 7],  k=6
	Output: True
	Explanation: Because [23, 2, 6, 4, 7] is an continuous subarray of size 5 and sums up to 42.

	Constraints:
	* The length of the array won't exceed 10,000.
	* You may assume the sum of all the numbers is in the range of a signed 32-bit integer."""

    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefix = 0 # prefix modulo 
        seen = {0: -1}
        for i, x in enumerate(nums): 
            prefix += x
            if k: prefix %= k
            if prefix in seen and i - seen[prefix] >= 2: return True 
            seen.setdefault(prefix, i)
        return False 


    """524. Longest Word in Dictionary through Deleting (Medium)
	Given a string and a string dictionary, find the longest string in the 
	dictionary that can be formed by deleting some characters of the given 
	string. If there are more than one possible results, return the longest 
	word with the smallest lexicographical order. If there is no possible 
	result, return the empty string.

	Example 1:
	Input:
	s = "abpcplea", d = ["ale","apple","monkey","plea"]
	Output: "apple"

	Example 2:
	Input:
	s = "abpcplea", d = ["a","b","c"]
	Output: "a"
	
	Note:
	* All the strings in the input will only contain lower-case letters.
	* The size of the dictionary won't exceed 1,000.
	* The length of all the strings in the input won't exceed 1,000."""

    def findLongestWord(self, s: str, d: List[str]) -> str:
        for word in sorted(d, key=lambda x: (-len(x), x)): 
            it = iter(s)
            if all(c in it for c in word): return word
        return ""


    """525. Contiguous Array (Medium)
	Given a binary array, find the maximum length of a contiguous subarray 
	with equal number of 0 and 1.

	Example 1:
	Input: [0,1]
	Output: 2
	Explanation: [0, 1] is the longest contiguous subarray with equal number of 
	             0 and 1.
	
	Example 2:
	Input: [0,1,0]
	Output: 2
	Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal 
	             number of 0 and 1.

	Note: The length of the given binary array will not exceed 50,000."""

    def findMaxLength(self, nums: List[int]) -> int:
        seen = {0:-1}
        ans = prefix = 0
        for i, x in enumerate(nums):
            prefix += x-0.5
            ans = max(ans, i - seen.setdefault(prefix, i))
        return ans 


    """526. Beautiful Arrangement (Medium)
	Suppose you have N integers from 1 to N. We define a beautiful arrangement 
	as an array that is constructed by these N numbers successfully if one of 
	the following is true for the ith position (1 <= i <= N) in this array:
	* The number at the ith position is divisible by i.
	* i is divisible by the number at the ith position.
	Now given N, how many beautiful arrangements can you construct?

	Example 1:
	Input: 2
	Output: 2

	Explanation: 
	The first beautiful arrangement is [1, 2]:
	Number at the 1st position (i=1) is 1, and 1 is divisible by i (i=1).
	Number at the 2nd position (i=2) is 2, and 2 is divisible by i (i=2).
	The second beautiful arrangement is [2, 1]:
	Number at the 1st position (i=1) is 2, and 2 is divisible by i (i=1).
	Number at the 2nd position (i=2) is 1, and i (i=2) is divisible by 1.

	Note: N is a positive integer and will not exceed 15."""

    def countArrangement(self, N: int) -> int:
        
        def fn(i): 
            """Return the number of beautiful arrangements of N numbers."""
            if i == 0: return 1 # boundary condition 
            ans = 0
            for k in range(1, N+1): 
                if k not in seen and (k%i == 0 or i%k == 0): 
                    seen.add(k)
                    ans += fn(i-1)
                    seen.remove(k)
            return ans 
        
        seen = set()
        return fn(N)


    """529. Minesweeper (Medium)
	Let's play the minesweeper game (Wikipedia, online game)! You are given a 
	2D char matrix representing the game board. 'M' represents an unrevealed 
	mine, 'E' represents an unrevealed empty square, 'B' represents a revealed 
	blank square that has no adjacent (above, below, left, right, and all 4 
	diagonals) mines, digit ('1' to '8') represents how many mines are adjacent 
	to this revealed square, and finally 'X' represents a revealed mine. Now 
	given the next click position (row and column indices) among all the 
	unrevealed squares ('M' or 'E'), return the board after revealing this 
	position according to the following rules:

	* If a mine ('M') is revealed, then the game is over - change it to 'X'.
	* If an empty square ('E') with no adjacent mines is revealed, then change 
	  it to revealed blank ('B') and all of its adjacent unrevealed squares 
	  should be revealed recursively.
	* If an empty square ('E') with at least one adjacent mine is revealed, 
	  then change it to a digit ('1' to '8') representing the number of 
	  adjacent mines.
	* Return the board when no more squares will be revealed.

	Example 1:
	Input: [['E', 'E', 'E', 'E', 'E'],
  	        ['E', 'E', 'M', 'E', 'E'],
  	        ['E', 'E', 'E', 'E', 'E'],
  	        ['E', 'E', 'E', 'E', 'E']]
	Click : [3,0]
	Output:[['B', '1', 'E', '1', 'B'],
	        ['B', '1', 'M', '1', 'B'],
	        ['B', '1', '1', '1', 'B'],
	        ['B', 'B', 'B', 'B', 'B']]

	Example 2:
	Input: [['B', '1', 'E', '1', 'B'],
	        ['B', '1', 'M', '1', 'B'],
	        ['B', '1', '1', '1', 'B'],
	        ['B', 'B', 'B', 'B', 'B']]
	Click : [1,2]
	Output:[['B', '1', 'E', '1', 'B'],
	        ['B', '1', 'X', '1', 'B'],
	        ['B', '1', '1', '1', 'B'],
	        ['B', 'B', 'B', 'B', 'B']]

	Note:
	* The range of the input matrix's height and width is [1,50].
	* The click position will only be an unrevealed square ('M' or 'E'), which 
	  also means the input board contains at least one clickable square.
	* The input board won't be a stage when game is over (some mines have been 
	  revealed).
	* For simplicity, not mentioned rules should be ignored in this problem. 
	  For example, you don't need to reveal all the unrevealed mines when the 
	  game is over, consider any cases that you will win the game or flag any squares."""

    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        m, n = len(board), len(board[0]) # dimensions 
        i, j = click 
        if board[i][j] == "M": board[i][j] = "X"
        elif board[i][j] == "E": 
            stack = [(i, j)]
            while stack: 
                i, j = stack.pop()
                cnt = 0
                for ii, jj in product(range(i-1, i+2), range(j-1, j+2)): 
                    if 0 <= ii < m and 0 <= jj < n and (ii, jj) != (i, j) and board[ii][jj] == "M": cnt += 1
                if cnt: board[i][j] = str(cnt)
                else: 
                    board[i][j] = "B"
                    for ii, jj in product(range(i-1, i+2), range(j-1, j+2)): 
                        if 0 <= ii < m and 0 <= jj < n and (ii, jj) != (i, j) and board[ii][jj] == "E": stack.append((ii, jj))
        return board


    """532. K-diff Pairs in an Array (Medium)
	Given an array of integers nums and an integer k, return the number of 
	unique k-diff pairs in the array. A k-diff pair is an integer pair 
	(nums[i], nums[j]), where the following are true:
	* 0 <= i, j < nums.length
	* i != j
	* a <= b
	* b - a == k

	Example 1:
	Input: nums = [3,1,4,1,5], k = 2
	Output: 2
	Explanation: There are two 2-diff pairs in the array, (1, 3) and (3, 5).
	Although we have two 1s in the input, we should only return the number of unique pairs.

	Example 2:
	Input: nums = [1,2,3,4,5], k = 1
	Output: 4
	Explanation: There are four 1-diff pairs in the array, (1, 2), (2, 3), (3, 4) and (4, 5).

	Example 3:
	Input: nums = [1,3,1,5,4], k = 0
	Output: 1
	Explanation: There is one 0-diff pair in the array, (1, 1).

	Example 4:
	Input: nums = [1,2,4,4,3,3,0,9,2,3], k = 3
	Output: 2

	Example 5:
	Input: nums = [-1,-2,-3], k = 1
	Output: 2

	Constraints:
	* 1 <= nums.length <= 104
	* -107 <= nums[i] <= 107
	* 0 <= k <= 107"""

    def findPairs(self, nums: List[int], k: int) -> int:
        ans, seen = set(), set()
        for x in nums: 
            if x - k in seen: ans.add(x)
            if x + k in seen: ans.add(x+k)
            seen.add(x)
        return len(ans)


    """537. Complex Number Multiplication (Medium)
	Given two strings representing two complex numbers. You need to return a 
	string representing their multiplication. Note i2 = -1 according to the 
	definition.

	Example 1:
	Input: "1+1i", "1+1i"
	Output: "0+2i"
	Explanation: (1 + i) * (1 + i) = 1 + i2 + 2 * i = 2i, and you need convert 
	             it to the form of 0+2i.
	
	Example 2:
	Input: "1+-1i", "1+-1i"
	Output: "0+-2i"
	Explanation: (1 - i) * (1 - i) = 1 + i2 - 2 * i = -2i, and you need convert 
	             it to the form of 0+-2i.
	
	Note: The input strings will not have extra blank. The input strings will 
	be given in the form of a+bi, where the integer a and b will both belong to 
	the range of [-100, 100]. And the output should be also in this form."""

    def complexNumberMultiply(self, a: str, b: str) -> str:
        ar, ac = map(int, a[:-1].split("+"))
        br, bc = map(int, b[:-1].split("+"))
        return f"{ar*br-ac*bc}+{ar*bc+ac*br}i"


    """538. Convert BST to Greater Tree (Medium)
	Given the root of a Binary Search Tree (BST), convert it to a Greater Tree 
	such that every key of the original BST is changed to the original key plus 
	sum of all keys greater than the original key in BST. As a reminder, a 
	binary search tree is a tree that satisfies these constraints:
	* The left subtree of a node contains only nodes with keys less than the node's key.
	* The right subtree of a node contains only nodes with keys greater than the node's key.
	* Both the left and right subtrees must also be binary search trees.
	
	Note: This question is the same as 1038: https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/

	Example 1:
	Input: root = [4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]
	Output: [30,36,21,36,35,26,15,null,null,null,33,null,null,null,8]

	Example 2:
	Input: root = [0,null,1]
	Output: [1,null,1]

	Example 3:
	Input: root = [1,0,2]
	Output: [3,3,2]

	Example 4:
	Input: root = [3,2,4,1]
	Output: [7,9,4,10]

	Constraints:
	* The number of nodes in the tree is in the range [0, 104].
	* -104 <= Node.val <= 104
	* All the values in the tree are unique.
	* root is guaranteed to be a valid binary search tree."""

    def convertBST(self, root: TreeNode) -> TreeNode:
        
        def fn(node, x): 
            """Inorder traverse the tree and update node's value."""
            if not node: return x
            x = fn(node.right, x) # sum of right subtree
            x += node.val 
            node.val = x
            return fn(node.left, x)
        
        fn(root, 0)
        return root 


    """562. Longest Line of Consecutive One in Matrix (Medium)
	Given a 01 matrix M, find the longest line of consecutive one in the matrix. 
	The line could be horizontal, vertical, diagonal or anti-diagonal.
	
	Example:
	Input: [[0,1,1,0],
	        [0,1,1,0],
	        [0,0,0,1]]
	Output: 3
	Hint: The number of elements in the given matrix will not exceed 10,000."""

    def longestLine(self, M: List[List[int]]) -> int:
        ans = 0 
        if M: 
            m, n = len(M), len(M[0]) # dimensions 
            rows, cols = [0]*m, [0]*n
            diag, anti = [0]*(m+n-1), [0]*(m+n-1)
            for i in range(m): 
                for j in range(n): 
                    if M[i][j]: 
                        rows[i] += 1
                        cols[j] += 1
                        diag[j-i+m-1] += 1
                        anti[i+j] += 1
                    else: rows[i] = cols[j] = diag[j-i+m-1] = anti[i+j] = 0
                    ans = max(ans, rows[i], cols[j], diag[j-i+m-1], anti[i+j])
        return ans 


    """565. Array Nesting (Medium)
	A zero-indexed array A of length N contains all integers from 0 to N-1. 
	Find and return the longest length of set S, where 
	S[i] = {A[i], A[A[i]], A[A[A[i]]], ... } subjected to the rule below. 
	Suppose the first element in S starts with the selection of element A[i] of 
	index = i, the next element in S should be A[A[i]], and then A[A[A[i]]]… By 
	that analogy, we stop adding right before a duplicate element occurs in S.

	Example 1:
	Input: A = [5,4,0,3,1,6,2]
	Output: 4
	Explanation: A[0] = 5, A[1] = 4, A[2] = 0, A[3] = 3, A[4] = 1, A[5] = 6, A[6] = 2.
	One of the longest S[K]: S[0] = {A[0], A[5], A[6], A[2]} = {5, 6, 2, 0}

	Note:
	* N is an integer within the range [1, 20,000].
	* The elements of A are all distinct.
	* Each element of A is an integer within the range [0, N-1]."""

    def arrayNesting(self, nums: List[int]) -> int:
        ans = 0
        seen = [False]*len(nums)
        for x in nums: 
            val = 0
            while not seen[x]: 
                seen[x] = True
                x = nums[x]
                val += 1
            ans = max(ans, val)
        return ans 


    """573. Squirrel Simulation (Medium)
	There's a tree, a squirrel, and several nuts. Positions are represented by 
	the cells in a 2D grid. Your goal is to find the minimal distance for the 
	squirrel to collect all the nuts and put them under the tree one by one. 
	The squirrel can only take at most one nut at one time and can move in four 
	directions - up, down, left and right, to the adjacent cell. The distance 
	is represented by the number of moves.
	
	Example 1:
	Input: 
	Height : 5
	Width : 7
	Tree position : [2,2]
	Squirrel : [4,4]
	Nuts : [[3,0], [2,5]]
	Output: 12
	​​​​​
	Note:
	* All given positions won't overlap.
	* The squirrel can take at most one nut at one time.
	* The given positions of nuts have no order.
	* Height and width are positive integers. 3 <= height * width <= 10,000.
	* The given positions contain at least one nut, only one tree and one squirrel."""

    def minDistance(self, height: int, width: int, tree: List[int], squirrel: List[int], nuts: List[List[int]]) -> int:
        ans, mn = 0, inf
        for x, y in nuts: 
            ans += 2*(abs(tree[0]-x) + abs(tree[1]-y))
            mn = min(mn, abs(squirrel[0]-x) + abs(squirrel[1]-y) - abs(tree[0]-x) - abs(tree[1]-y))
        return ans + mn


    """575. Distribute Candies (Easy)
	Alice has n candies, where the ith candy is of type candyType[i]. Alice 
	noticed that she started to gain weight, so she visited a doctor. The 
	doctor advised Alice to only eat n / 2 of the candies she has (n is always 
	even). Alice likes her candies very much, and she wants to eat the maximum 
	number of different types of candies while still following the doctor's 
	advice. Given the integer array candyType of length n, return the maximum 
	number of different types of candies she can eat if she only eats n / 2 of 
	them.

	Example 1:
	Input: candyType = [1,1,2,2,3,3]
	Output: 3
	Explanation: Alice can only eat 6 / 2 = 3 candies. Since there are only 3 
	             types, she can eat one of each type.

	Example 2:
	Input: candyType = [1,1,2,3]
	Output: 2
	Explanation: Alice can only eat 4 / 2 = 2 candies. Whether she eats types 
	             [1,2], [1,3], or [2,3], she still can only eat 2 different 
	             types.
	
	Example 3:
	Input: candyType = [6,6,6,6]
	Output: 1
	Explanation: Alice can only eat 4 / 2 = 2 candies. Even though she can eat 
	             2 candies, she only has 1 type.

	Constraints:
	* n == candyType.length
	* 2 <= n <= 10^4
	* n is even.
	* -10^5 <= candyType[i] <= 10^5"""

    def distributeCandies(self, candyType: List[int]) -> int:
        return min(len(candyType)//2, len(set(candyType)))


    """582. Kill Process (Medium)
	Given n processes, each process has a unique PID (process id) and its PPID 
	(parent process id). Each process only has one parent process, but may have 
	one or more children processes. This is just like a tree structure. Only 
	one process has PPID that is 0, which means this process has no parent 
	process. All the PIDs will be distinct positive integers. We use two list 
	of integers to represent a list of processes, where the first list contains 
	PID for each process and the second list contains the corresponding PPID. 
	Now given the two lists, and a PID representing a process you want to kill, 
	return a list of PIDs of processes that will be killed in the end. You 
	should assume that when a process is killed, all its children processes 
	will be killed. No order is required for the final answer.

	Example 1:
	Input: pid =  [1, 3, 10, 5]
	       ppid = [3, 0, 5, 3]
	       kill = 5
	Output: [5,10]
	Explanation: 
	           3
	         /   \
	        1     5
	             /
	            10
	Kill 5 will also kill 10.
	Note: 
	* The given kill id is guaranteed to be one of the given PIDs.
	* n >= 1."""

    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        tree = {}
        for x, px in zip(pid, ppid): 
            tree.setdefault(px, []).append(x)

        ans, stack = [], [kill]
        while stack: 
            x = stack.pop()
            ans.append(x)
            stack.extend(tree.get(x, []))
        return ans 


    """594. Longest Harmonious Subsequence (Easy)
	We define a harmonious array as an array where the difference between its 
	maximum value and its minimum value is exactly 1. Given an integer array 
	nums, return the length of its longest harmonious subsequence among all its 
	possible subsequences. A subsequence of array is a sequence that can be 
	derived from the array by deleting some or no elements without changing the 
	order of the remaining elements.

	Example 1:
	Input: nums = [1,3,2,2,5,2,3,7]
	Output: 5
	Explanation: The longest harmonious subsequence is [3,2,2,2,3].

	Example 2:
	Input: nums = [1,2,3,4]
	Output: 2

	Example 3:
	Input: nums = [1,1,1,1]
	Output: 0

	Constraints:
	* 1 <= nums.length <= 2 * 104
	* -109 <= nums[i] <= 109"""

    def findLHS(self, nums: List[int]) -> int:
        freq = {}
        for x in nums: freq[x] = 1 + freq.get(x, 0)
        
        ans = 0
        for x in nums: 
            if x + 1 in freq: ans = max(ans, freq[x] + freq[x+1])
        return ans 


    """605. Can Place Flowers (Easy)
	You have a long flowerbed in which some of the plots are planted, and some 
	are not. However, flowers cannot be planted in adjacent plots. Given an 
	integer array flowerbed containing 0's and 1's, where 0 means empty and 1 
	means not empty, and an integer n, return if n new flowers can be planted 
	in the flowerbed without violating the no-adjacent-flowers rule.

	Example 1:
	Input: flowerbed = [1,0,0,0,1], n = 1
	Output: true

	Example 2:
	Input: flowerbed = [1,0,0,0,1], n = 2
	Output: false

	Constraints:
	* 1 <= flowerbed.length <= 2 * 10^4
	* flowerbed[i] is 0 or 1.
	* There are no two adjacent flowers in flowerbed.
	* 0 <= n <= flowerbed.length"""

    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        for i in range(len(flowerbed)):
            if (i == 0 or flowerbed[i-1] == 0) and flowerbed[i] == 0 and (i+1 == len(flowerbed) or flowerbed[i+1] == 0): 
                flowerbed[i] = 1
                n -= 1
        return n <= 0


    """645. Set Mismatch (Easy)
	You have a set of integers s, which originally contains all the numbers 
	from 1 to n. Unfortunately, due to some error, one of the numbers in s got 
	duplicated to another number in the set, which results in repetition of one 
	number and loss of another number. You are given an integer array nums 
	representing the data status of this set after the error. Find the number 
	that occurs twice and the number that is missing and return them in the 
	form of an array.

	Example 1:
	Input: nums = [1,2,2,4]
	Output: [2,3]

	Example 2:
	Input: nums = [1,1]
	Output: [1,2]

	Constraints:
	* 2 <= nums.length <= 10^4
	* 1 <= nums[i] <= 10^4"""

    def findErrorNums(self, nums: List[int]) -> List[int]:
        freq = [0]*len(nums)
        for x in nums: freq[x-1] += 1
        
        ans = [0]*2
        for i, x in enumerate(freq): 
            if x == 2: ans[0] = i+1
            elif x == 0: ans[1] = i+1
        return ans 


    """650. 2 Keys Keyboard (Medium)
	Initially on a notepad only one character 'A' is present. You can perform 
	two operations on this notepad for each step:
	* Copy All: You can copy all the characters present on the notepad (partial 
	  copy is not allowed).
	* Paste: You can paste the characters which are copied last time.
	 
	Given a number n. You have to get exactly n 'A' on the notepad by 
	performing the minimum number of steps permitted. Output the minimum number 
	of steps to get n 'A'.

	Example 1:
	Input: 3
	Output: 3
	Explanation: Intitally, we have one character 'A'.
	In step 1, we use Copy All operation.
	In step 2, we use Paste operation to get 'AA'.
	In step 3, we use Paste operation to get 'AAA'.

	Note: The n will be in the range [1, 1000]."""

    def minSteps(self, n: int) -> int:
        for i in range(2, int(sqrt(n)+1)): 
            if n%i == 0: return i + self.minSteps(n//i)
        return 0 if n == 1 else n 


    """654. Maximum Binary Tree (Medium)
	Given an integer array with no duplicates. A maximum tree building on this 
	array is defined as follow:
	* The root is the maximum number in the array.
	* The left subtree is the maximum tree constructed from left part subarray 
	  divided by the maximum number.
	* The right subtree is the maximum tree constructed from right part 
	  subarray divided by the maximum number.
	Construct the maximum tree by the given array and output the root node of 
	this tree.

	Example 1:
	Input: [3,2,1,6,0,5]
	Output: return the tree root node representing the following tree:
	      6
	    /   \
	   3     5
	    \    / 
	     2  0   
	       \
	        1
	Note: The size of the given array will be in the range [1,1000]."""

    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        stack = []
        for x in nums: 
            node = TreeNode(x)
            while stack and stack[-1].val < x: node.left = stack.pop()
            if stack: stack[-1].right = node 
            stack.append(node)
        return stack[0]


    """655. Print Binary Tree (Medium)
	Print a binary tree in an m*n 2D string array following these rules:
	1 The row number m should be equal to the height of the given binary tree.
	2 The column number n should always be an odd number.
	3 The root node's value (in string format) should be put in the exactly 
	  middle of the first row it can be put. The column and the row where the 
	  root node belongs will separate the rest space into two parts (left-
	  bottom part and right-bottom part). You should print the left subtree in 
	  the left-bottom part and print the right subtree in the right-bottom part. 
	  The left-bottom part and the right-bottom part should have the same size. 
	  Even if one subtree is none while the other is not, you don't need to 
	  print anything for the none subtree but still need to leave the space as 
	  large as that for the other subtree. However, if two subtrees are none, 
	  then you don't need to leave space for both of them.
	4 Each unused space should contain an empty string "".
	5 Print the subtrees following the same rules.
	
	Example 1:
	Input:
	     1
	    /
	   2
	Output:
	[["", "1", ""],
	 ["2", "", ""]]
	
	Example 2:
	Input:
	     1
	    / \
	   2   3
	    \
	     4
	Output:
	[["", "", "", "1", "", "", ""],
	 ["", "2", "", "", "", "3", ""],
	 ["", "", "4", "", "", "", ""]]
	
	Example 3:
	Input:
	      1
	     / \
	    2   5
	   / 
	  3 
	 / 
	4 
	Output:
	[["",  "",  "", "",  "", "", "", "1", "",  "",  "",  "",  "", "", ""]
	 ["",  "",  "", "2", "", "", "", "",  "",  "",  "",  "5", "", "", ""]
	 ["",  "3", "", "",  "", "", "", "",  "",  "",  "",  "",  "", "", ""]
	 ["4", "",  "", "",  "", "", "", "",  "",  "",  "",  "",  "", "", ""]]

	Note: The height of binary tree is in the range of [1, 10]."""

    def printTree(self, root: TreeNode) -> List[List[str]]:
        ht = lambda node: 1 + max(ht(node.left), ht(node.right)) if node else 0 # height of binary tree 
        m = ht(root) # rows 
        n = 2**m - 1 # columns 
        
        def dfs(node, i, lo=0, hi=n): 
            """Populate ans via dfs."""
            if not node: return 
            mid = lo + hi >> 1
            ans[i][mid] = str(node.val)
            dfs(node.left, i+1, lo, mid) or dfs(node.right, i+1, mid+1, hi)

        ans = [[""]*n for _ in range(m)]
        dfs(root, 0)
        return ans


    """658. Find K Closest Elements (Medium)
	Given a sorted array arr, two integers k and x, find the k closest elements 
	to x in the array. The result should also be sorted in ascending order. If 
	there is a tie, the smaller elements are always preferred.

	Example 1:
	Input: arr = [1,2,3,4,5], k = 4, x = 3
	Output: [1,2,3,4]

	Example 2:
	Input: arr = [1,2,3,4,5], k = 4, x = -1
	Output: [1,2,3,4]

	Constraints:
	* 1 <= k <= arr.length
	* 1 <= arr.length <= 10^4
	* Absolute value of elements in the array and x will not exceed 10^4"""

    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        lo, hi = 0, len(arr)-k
        while lo < hi: 
            mid = lo + hi >> 1
            if x - arr[mid] > arr[mid+k] - x: lo = mid + 1
            else: hi = mid
        return arr[lo:lo+k]


    """659. Split Array into Consecutive Subsequences (Medium)
	Given an array nums sorted in ascending order, return true if and only if 
	you can split it into 1 or more subsequences such that each subsequence 
	consists of consecutive integers and has length at least 3.

	Example 1:
	Input: [1,2,3,3,4,5]
	Output: True
	Explanation: You can split them into two consecutive subsequences : 
	1, 2, 3
	3, 4, 5

	Example 2:
	Input: [1,2,3,3,4,4,5,5]
	Output: True
	Explanation: You can split them into two consecutive subsequences : 
	1, 2, 3, 4, 5
	3, 4, 5
	
	Example 3:
	Input: [1,2,3,4,4,5]
	Output: False

	Constraints: 1 <= nums.length <= 10000"""

    def isPossible(self, nums: List[int]) -> bool:
        freq = {}
        for x in nums: freq[x] = 1 + freq.get(x, 0) # frequency table of nums
        
        seen = deque()
        for i, x in enumerate(nums):
            if i == 0 or nums[i-1] != x: 
                if (n := freq[x] - freq.get(x-1, 0)) > 0: seen.extend([x]*n)
                elif any(x - seen.popleft() < 3 for _ in range(-n)): return False 
                if not freq.get(x+1, 0) and any(x - seen.popleft() < 2 for _ in range(freq[x])): return False 
        return True 


    """662. Maximum Width of Binary Tree (Medium)
	Given a binary tree, write a function to get the maximum width of the given 
	tree. The maximum width of a tree is the maximum width among all levels. 
	The width of one level is defined as the length between the end-nodes (the 
	leftmost and right most non-null nodes in the level, where the null nodes 
	between the end-nodes are also counted into the length calculation. It is 
	guaranteed that the answer will in the range of 32-bit signed integer.

	Example 1:
	Input: 
	           1
	         /   \
	        3     2
	       / \     \  
	      5   3     9 
	Output: 4
	Explanation: The maximum width existing in the third level with the length 
	             4 (5,3,null,9).

	Example 2:
	Input: 
	          1
	         /  
	        3    
	       / \       
	      5   3     
	Output: 2
	Explanation: The maximum width existing in the third level with the length 
	             2 (5,3).

	Example 3:
	Input: 
	          1
	         / \
	        3   2 
	       /        
	      5      
	Output: 2
	Explanation: The maximum width existing in the second level with the length 
	             2 (3,2).

	Example 4:
	Input: 
	          1
	         / \
	        3   2
	       /     \  
	      5       9 
	     /         \
	    6           7
	Output: 8
	Explanation:The maximum width existing in the fourth level with the length 
	            8 (6,null,null,null,null,null,null,7).
	 
	Constraints: The given binary tree will have between 1 and 3000 nodes."""

    def widthOfBinaryTree(self, root: TreeNode) -> int:
        ans = 1
        queue = [(root, 0)]
        while queue: 
            ans = max(ans, queue[-1][1] - queue[0][1] + 1)
            newq = []
            for node, i in queue: 
                if node.left: newq.append((node.left, 2*i))
                if node.right: newq.append((node.right, 2*i+1))
            queue = newq
        return ans 


    """678. Valid Parenthesis String (Medium)
	Given a string containing only three types of characters: '(', ')' and '*', 
	write a function to check whether this string is valid. We define the 
	validity of a string by these rules:
	1) Any left parenthesis '(' must have a corresponding right parenthesis ')'.
	2) Any right parenthesis ')' must have a corresponding left parenthesis '('.
	3) Left parenthesis '(' must go before the corresponding right parenthesis ')'.
	4) '*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string.
	5) An empty string is also valid.
	
	Example 1:
	Input: "()"
	Output: True
	
	Example 2:
	Input: "(*)"
	Output: True
	
	Example 3:
	Input: "(*))"
	Output: True
	
	Note: The string size will be in the range [1, 100]."""

    def checkValidString(self, s: str) -> bool:
        op = cl = 0
        for i in range(len(s)):
            op += 1 if s[ i] in "(*" else -1
            cl += 1 if s[~i] in ")*" else -1
            if op < 0 or cl < 0: return False 
        return True 


    """686. Repeated String Match (Medium)
	Given two strings a and b, return the minimum number of times you should 
	repeat string a so that string b is a substring of it. If it is impossible 
	for b​​​​​​ to be a substring of a after repeating it, return -1. Notice: string 
	"abc" repeated 0 times is "",  repeated 1 time is "abc" and repeated 2 
	times is "abcabc".

	Example 1:
	Input: a = "abcd", b = "cdabcdab"
	Output: 3
	Explanation: We return 3 because by repeating a three times "abcdabcdabcd", 
	             b is a substring of it.

	Example 2:
	Input: a = "a", b = "aa"
	Output: 2

	Example 3:
	Input: a = "a", b = "a"
	Output: 1

	Example 4:
	Input: a = "abc", b = "wxyz"
	Output: -1

	Constraints:
	* 1 <= a.length <= 104
	* 1 <= b.length <= 104
	* a and b consist of lower-case English letters."""

    def repeatedStringMatch(self, a: str, b: str) -> int:
        n = ceil(len(b)/len(a)) # ceiling of len(b)/len(a)
        return next((n+i for i in range(2) if b in (n+i)*a), -1)


    """687. Longest Univalue Path (Medium)
	Given the root of a binary tree, return the length of the longest path, 
	where each node in the path has the same value. This path may or may not 
	pass through the root. The length of the path between two nodes is 
	represented by the number of edges between them.

	Example 1:
	Input: root = [5,4,5,1,1,5]
	Output: 2

	Example 2:
	Input: root = [1,4,5,4,4,5]
	Output: 2

	Constraints:
	* The number of nodes in the tree is in the range [0, 104].
	* -1000 <= Node.val <= 1000
	* The depth of the tree will not exceed 1000."""

    def longestUnivaluePath(self, root: TreeNode) -> int:
        
        def dfs(node): 
            """Return longest univalue branch and longest univalue path (post-order traversal)."""
            nonlocal ans 
            if not node: return 0
            lx, rx = dfs(node.left), dfs(node.right) 
            if not node.left or node.left.val != node.val: lx = 0
            if not node.right or node.right.val != node.val: rx = 0 
            ans = max(ans, 1 + lx + rx)
            return 1 + max(lx, rx)
        
        ans = 0
        dfs(root)
        return max(0, ans-1)


    """688. Knight Probability in Chessboard (Medium)
	On an NxN chessboard, a knight starts at the r-th row and c-th column and 
	attempts to make exactly K moves. The rows and columns are 0 indexed, so 
	the top-left square is (0, 0), and the bottom-right square is (N-1, N-1). A 
	chess knight has 8 possible moves it can make, as illustrated below. Each 
	move is two squares in a cardinal direction, then one square in an 
	orthogonal direction. Each time the knight is to move, it chooses one of 
	eight possible moves uniformly at random (even if the piece would go off 
	the chessboard) and moves there. The knight continues moving until it has 
	made exactly K moves or has moved off the chessboard. Return the 
	probability that the knight remains on the board after it has stopped 
	moving.

	Example:
	Input: 3, 2, 0, 0
	Output: 0.0625
	Explanation: There are two moves (to (1,2), (2,1)) that will keep the 
	             knight on the board. From each of those positions, there are 
	             also two moves that will keep the knight on the board. The 
	             total probability the knight stays on the board is 0.0625.
	 
	Note:
	* N will be between 1 and 25.
	* K will be between 0 and 100.
	* The knight always initially starts on the board."""

    def knightProbability(self, N: int, K: int, r: int, c: int) -> float:
        
        @lru_cache(None)
        def fn(k, i, j): 
            """Return probability in chessboard at (i, j) with k moves left."""
            if not (0 <= i < N and 0 <= j < N): return 0
            if k == 0: return 1 
            return 1/8*sum(fn(k-1, i+ii, j+jj) for ii, jj in ((-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)))
            
        return fn(K, r, c)


    """690. Employee Importance (Easy)
	You are given a data structure of employee information, which includes the 
	employee's unique id, their importance value and their direct subordinates' 
	id. For example, employee 1 is the leader of employee 2, and employee 2 is 
	the leader of employee 3. They have importance value 15, 10 and 5, 
	respectively. Then employee 1 has a data structure like [1, 15, [2]], and 
	employee 2 has [2, 10, [3]], and employee 3 has [3, 5, []]. Note that 
	although employee 3 is also a subordinate of employee 1, the relationship 
	is not direct. Now given the employee information of a company, and an 
	employee id, you need to return the total importance value of this employee 
	and all their subordinates.

	Example 1:
	Input: [[1, 5, [2, 3]], [2, 3, []], [3, 3, []]], 1
	Output: 11
	Explanation: Employee 1 has importance value 5, and he has two direct 
	             subordinates: employee 2 and employee 3. They both have 
	             importance value 3. So the total importance value of employee 
	             1 is 5 + 3 + 3 = 11.

	Note:
	* One employee has at most one direct leader and may have several subordinates.
	* The maximum number of employees won't exceed 2000."""

    def getImportance(self, employees: List['Employee'], id: int) -> int:
        mp = {x.id: x for x in employees}
        
        ans = 0
        stack = [id]
        while stack: 
            x = stack.pop()
            ans += mp[x].importance
            stack.extend(mp[x].subordinates)
        return ans 


    """692. Top K Frequent Words (Medium)
	Given a non-empty list of words, return the k most frequent elements. Your 
	answer should be sorted by frequency from highest to lowest. If two words 
	have the same frequency, then the word with the lower alphabetical order 
	comes first.

	Example 1:
	Input: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
	Output: ["i", "love"]
	Explanation: "i" and "love" are the two most frequent words. Note that "i" 
	             comes before "love" due to a lower alphabetical order.
	
	Example 2:
	Input: ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4
	Output: ["the", "is", "sunny", "day"]
	Explanation: "the", "is", "sunny" and "day" are the four most frequent 
	             words, with the number of occurrence being 4, 3, 2 and 1 
	             respectively.
	Note:
	* You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
	* Input words contain only lowercase letters.
	
	Follow up: Try to solve it in O(n log k) time and O(n) extra space."""

    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq = {} # frequency table
        for x in words: freq[x] = 1 + freq.get(x, 0) 
        return nsmallest(k, freq, key=lambda x: (-freq[x], x))


    """694. Number of Distinct Islands (Medium)
	Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's 
	(representing land) connected 4-directionally (horizontal or vertical.) You 
	may assume all four edges of the grid are surrounded by water. Count the 
	number of distinct islands. An island is considered to be the same as 
	another if and only if one island can be translated (and not rotated or 
	reflected) to equal the other.

	Example 1:
	11000
	11000
	00011
	00011
	Given the above grid map, return 1.
	
	Example 2:
	11011
	10000
	00001
	11011
	Given the above grid map, return 3.

	Notice that:
	11 and  1 are considered different island shapes, because we do not consider 
	1      11
	reflection / rotation.
	
	Note: The length of each dimension in the given grid does not exceed 50."""

    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0]) # dimensions 
        seen = set()
        
        def fn(i, j):
            """Travere grid depth-first."""
            grid[i][j] = 0 # mark visited 
            vals.add((i, j))
            for ii, jj in (i-1, j), (i, j-1), (i, j+1), (i+1, j):
                if 0 <= ii < m and 0 <= jj < n and grid[ii][jj]: fn(ii, jj)
        
        for i in range(m):
            for j in range(n): 
                if grid[i][j]: 
                    vals = set()
                    fn(i, j)
                    mi = min(i for i, _ in vals)
                    mj = min(j for _, j in vals) 
                    seen.add(tuple(sorted((i-mi, j-mj) for i, j in vals)))
        return len(seen)


    """695. Max Area of Island (Medium)
	Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's 
	(representing land) connected 4-directionally (horizontal or vertical.) You 
	may assume all four edges of the grid are surrounded by water. Find the 
	maximum area of an island in the given 2D array. (If there is no island, 
	the maximum area is 0.)

	Example 1:
	[[0,0,1,0,0,0,0,1,0,0,0,0,0],
	 [0,0,0,0,0,0,0,1,1,1,0,0,0],
	 [0,1,1,0,1,0,0,0,0,0,0,0,0],
	 [0,1,0,0,1,1,0,0,1,0,1,0,0],
	 [0,1,0,0,1,1,0,0,1,1,1,0,0],
	 [0,0,0,0,0,0,0,0,0,0,1,0,0],
	 [0,0,0,0,0,0,0,1,1,1,0,0,0],
	 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
	Given the above grid, return 6. Note the answer is not 11, because the 
	island must be connected 4-directionally.
	
	Example 2:
	[[0,0,0,0,0,0,0,0]]
	Given the above grid, return 0.

	Note: The length of each dimension in the given grid does not exceed 50."""

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0]) # dimension 
        
        def dfs(i, j): 
            """Depth-first traverse the grid."""
            if 0 <= i < m and 0 <= j < n and grid[i][j] == 1: 
                grid[i][j] = 0 # mark visited 
                return 1 + sum(dfs(ii, jj) for ii, jj in ((i-1, j), (i, j-1), (i, j+1), (i+1, j)))
            return 0
        
        return max(dfs(i, j) for i in range(m) for j in range(n))


    """725. Split Linked List in Parts (Medium)
	Given a (singly) linked list with head node root, write a function to split 
	the linked list into k consecutive linked list "parts". The length of each 
	part should be as equal as possible: no two parts should have a size 
	differing by more than 1. This may lead to some parts being null. The parts 
	should be in order of occurrence in the input list, and parts occurring 
	earlier should always have a size greater than or equal parts occurring 
	later. Return a List of ListNode's representing the linked list parts that 
	are formed. Examples 1->2->3->4, k = 5 // 5 equal parts [ [1], [2], [3], [4], null ]

	Example 1:
	Input: root = [1, 2, 3], k = 5
	Output: [[1],[2],[3],[],[]]
	Explanation: The input and each element of the output are ListNodes, not 
	arrays. For example, the input root has root.val = 1, root.next.val = 2, 
	root.next.next.val = 3, and root.next.next.next = null. The first element 
	output[0] has output[0].val = 1, output[0].next = null. The last element 
	output[4] is null, but it's string representation as a ListNode is [].
	
	Example 2:
	Input: root = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], k = 3
	Output: [[1, 2, 3, 4], [5, 6, 7], [8, 9, 10]]
	Explanation: The input has been split into consecutive parts with size 
	difference at most 1, and earlier parts are a larger size than the later 
	parts.
	
	Note:
	* The length of root will be in the range [0, 1000].
	* Each value of a node in the input will be an integer in the range [0, 999].
	* k will be an integer in the range [1, 50]."""

    def splitListToParts(self, root: ListNode, k: int) -> List[ListNode]:
        n, node = 0, root # length of linked list 
        while node: n, node = n+1, node.next
        
        ans = []
        node = root 
        q, r = divmod(n, k) # quotient & residual
        q += 1
        for i in range(k): 
            ans.append(node)
            if i == r: q -= 1
            prev = None
            for _ in range(q): 
                prev = node
                if node: node = node.next 
            if prev: prev.next = None # break list into parts 
        return ans 


    """734. Sentence Similarity (Easy)
	We can represent a sentence as an array of words, for example, the sentence 
	"I am happy with leetcode" can be represented as 
	arr = ["I","am",happy","with","leetcode"]. Given two sentences sentence1 
	and sentence2 each represented as a string array and given an array of 
	string pairs similarPairs where similarPairs[i] = [xi, yi] indicates that 
	the two words xi and yi are similar. Return true if sentence1 and sentence2 
	are similar, or false if they are not similar.

	Two sentences are similar if:
	* They have the same length (i.e. the same number of words)
	* sentence1[i] and sentence2[i] are similar.
	Notice that a word is always similar to itself, also notice that the 
	similarity relation is not transitive. For example, if the words a and b 
	are similar and the words b and c are similar, a and c are not necessarily 
	similar.

	Example 1:
	Input: sentence1 = ["great","acting","skills"], 
	       sentence2 = ["fine","drama","talent"], 
	       similarPairs = [["great","fine"],["drama","acting"],["skills","talent"]]
	Output: true
	Explanation: The two sentences have the same length and each word i of 
	             sentence1 is also similar to the corresponding word in 
	             sentence2.
	
	Example 2:
	Input: sentence1 = ["great"], 
	       sentence2 = ["great"], 
	       similarPairs = []
	Output: true
	Explanation: A word is similar to itself.

	Example 3:
	Input: sentence1 = ["great"], 
	       sentence2 = ["doubleplus","good"], 
	       similarPairs = [["great","doubleplus"]]
	Output: false
	Explanation: As they don't have the same length, we return false.

	Constraints:
	* 1 <= sentence1.length, sentence2.length <= 1000
	* 1 <= sentence1[i].length, sentence2[i].length <= 20
	* sentence1[i] and sentence2[i] consist of lower-case and upper-case English letters.
	* 0 <= similarPairs.length <= 1000
	* similarPairs[i].length == 2
	* 1 <= xi.length, yi.length <= 20
	* xi and yi consist of lower-case and upper-case English letters.
	* All the pairs (xi, yi) are distinct."""

    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        if len(sentence1) != len(sentence2): return False # edge case 
        
        mp = {}
        for x, y in similarPairs: 
            mp.setdefault(x, set()).add(y)
            mp.setdefault(y, set()).add(x)
        
        for w1, w2 in zip(sentence1, sentence2): 
            if w1 != w2 and w1 not in mp.get(w2, set()): return False 
        return True 


    """739. Daily Temperatures (Medium)
	Given a list of daily temperatures T, return a list such that, for each day 
	in the input, tells you how many days you would have to wait until a warmer 
	temperature. If there is no future day for which this is possible, put 0 
	instead. For example, given the list of temperatures T = [73, 74, 75, 71, 
	69, 72, 76, 73], your output should be [1, 1, 4, 2, 1, 1, 0, 0]. Note that 
	the length of temperatures will be in the range [1, 30000]. Each temperature 
	will be an integer in the range [30, 100]."""

    def dailyTemperatures(self, T: List[int]) -> List[int]:
        ans = [0]*len(T)
        stack = []
        for i in range(len(T)): 
            while stack and T[stack[-1]] < T[i]: 
                ii = stack.pop()
                ans[ii] = i - ii 
            stack.append(i)
        return ans 


    """740. Delete and Earn (Medium)
	Given an array nums of integers, you can perform operations on the array. 
	In each operation, you pick any nums[i] and delete it to earn nums[i] 
	points. After, you must delete every element equal to nums[i] - 1 or 
	nums[i] + 1. You start with 0 points. Return the maximum number of points 
	you can earn by applying such operations.

	Example 1:
	Input: nums = [3, 4, 2]
	Output: 6
	Explanation: Delete 4 to earn 4 points, consequently 3 is also deleted. 
	             Then, delete 2 to earn 2 points. 6 total points are earned.
	Example 2:
	Input: nums = [2, 2, 3, 3, 3, 4]
	Output: 9
	Explanation: Delete 3 to earn 3 points, deleting both 2's and the 4. Then, 
	             delete 3 again to earn 3 points, and 3 again to earn 3 points. 
	             9 total points are earned.
	Note:
	* The length of nums is at most 20000.
	* Each element nums[i] is an integer in the range [1, 10000]."""

    def deleteAndEarn(self, nums: List[int]) -> int:
        mp = {}
        for x in nums: mp[x] = x + mp.get(x, 0)
        
        @lru_cache(None)
        def fn(i): 
            """Return maximum points one can earn from nums[i:]."""
            if i >= len(nums): return 0 
            if nums[i] + 1 not in mp: return mp[nums[i]] + fn(i+1)
            return max(mp[nums[i]] + fn(i+2), fn(i+1))
        
        nums = sorted(set(nums))
        return fn(0)


    """750. Number Of Corner Rectangles (Medium)
	Given a grid where each entry is only 0 or 1, find the number of corner 
	rectangles. A corner rectangle is 4 distinct 1s on the grid that form an 
	axis-aligned rectangle. Note that only the corners need to have the value 
	1. Also, all four 1s used must be distinct.

	Example 1:
	Input: grid = [[1, 0, 0, 1, 0],
         	       [0, 0, 1, 0, 1],
         	       [0, 0, 0, 1, 0],
         	       [1, 0, 1, 0, 1]]
	Output: 1
	Explanation: There is only one corner rectangle, with corners grid[1][2], 
	             grid[1][4], grid[3][2], grid[3][4].

	Example 2:
	Input: grid = [[1, 1, 1],
	               [1, 1, 1],
	               [1, 1, 1]]
	Output: 9
	Explanation: There are four 2x2 rectangles, four 2x3 and 3x2 rectangles, 
	             and one 3x3 rectangle.

	Example 3:
	Input: grid = [[1, 1, 1, 1]]
	Output: 0
	Explanation: Rectangles must have four distinct corners.

	Note:
	* The number of rows and columns of grid will each be in the range [1, 200].
	* Each grid[i][j] will be either 0 or 1.
	* The number of 1s in the grid will be at most 6000."""

    def countCornerRectangles(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0]) # dimensions 
        seen = {}
        ans = 0
        for i in range(m):
            for j in range(n): 
                if grid[i][j]: 
                    for jj in range(j): 
                        if grid[i][jj]: 
                            ans += seen.get((jj, j), 0)
                            seen[jj, j] = 1 + seen.get((jj, j), 0)
        return ans 


    """752. Open the Lock (Medium)
	You have a lock in front of you with 4 circular wheels. Each wheel has 10 
	slots: '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'. The wheels can 
	rotate freely and wrap around: for example we can turn '9' to be '0', or 
	'0' to be '9'. Each move consists of turning one wheel one slot. The lock 
	initially starts at '0000', a string representing the state of the 4 wheels. 
	You are given a list of deadends dead ends, meaning if the lock displays 
	any of these codes, the wheels of the lock will stop turning and you will 
	be unable to open it. Given a target representing the value of the wheels 
	that will unlock the lock, return the minimum total number of turns 
	required to open the lock, or -1 if it is impossible.

	Example 1:
	Input: deadends = ["0201","0101","0102","1212","2002"], target = "0202"
	Output: 6
	Explanation:
	A sequence of valid moves would be "0000" -> "1000" -> "1100" -> "1200" -> "1201" -> "1202" -> "0202".
	Note that a sequence like "0000" -> "0001" -> "0002" -> "0102" -> "0202" would be invalid,
	because the wheels of the lock become stuck after the display becomes the dead end "0102".

	Example 2:
	Input: deadends = ["8888"], target = "0009"
	Output: 1
	Explanation:
	We can turn the last wheel in reverse to move from "0000" -> "0009".

	Example 3:
	Input: deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"], target = "8888"
	Output: -1
	Explanation:
	We can't reach the target without getting stuck.

	Example 4:
	Input: deadends = ["0000"], target = "8888"
	Output: -1

	Constraints:
	* 1 <= deadends.length <= 500
	* deadends[i].length == 4
	* target.length == 4
	* target will not be in the list deadends.
	* target and deadends[i] consist of digits only."""

    def openLock(self, deadends: List[str], target: str) -> int:
        pq = [(0, "0000")] # min priority queue
        seen = set(deadends)
        
        while pq: 
            k, n = heappop(pq)
            if n not in seen: 
                if n == target: return k
                seen.add(n)  # marked as seen upon processing 
                for i in range(4): 
                    for chg in (-1, 1): 
                        nn = n[:i] + str((int(n[i]) + chg)%10) + n[i+1:]
                        if nn not in seen: heappush(pq, (k+1, nn))
        return -1 


    """754. Reach a Number (Medium)
	You are standing at position 0 on an infinite number line. There is a goal 
	at position target. On each move, you can either go left or right. During 
	the n-th move (starting from 1), you take n steps. Return the minimum 
	number of steps required to reach the destination.

	Example 1:
	Input: target = 3
	Output: 2
	Explanation:
	On the first move we step from 0 to 1.
	On the second step we step from 1 to 3.
	
	Example 2:
	Input: target = 2
	Output: 3
	Explanation:
	On the first move we step from 0 to 1.
	On the second move we step  from 1 to -1.
	On the third move we step from -1 to 2.
	
	Note: target will be a non-zero integer in the range [-10^9, 10^9]."""

    def reachNumber(self, target: int) -> int:
        target = abs(target)
        k = ceil((-1 + sqrt(1 + 8*target))/2)
        return k if not k*(k+1)//2 - target & 1 else k + 1 + k%2


    """756. Pyramid Transition Matrix (Medium)
	We are stacking blocks to form a pyramid. Each block has a color which is a 
	one letter string. We are allowed to place any color block C on top of two 
	adjacent blocks of colors A and B, if and only if ABC is an allowed triple. 
	We start with a bottom row of bottom, represented as a single string. We 
	also start with a list of allowed triples allowed. Each allowed triple is 
	represented as a string of length 3. Return true if we can build the pyramid 
	all the way to the top, otherwise false.

	Example 1:
	Input: bottom = "BCD", allowed = ["BCG", "CDE", "GEA", "FFF"]
	Output: true
	Explanation: We can stack the pyramid like this:
	    A
	   / \
	  G   E
	 / \ / \
	B   C   D
	We are allowed to place G on top of B and C because BCG is an allowed triple.  
	Similarly, we can place E on top of C and D, then A on top of G and E.

	Example 2:
	Input: bottom = "AABA", allowed = ["AAA", "AAB", "ABA", "ABB", "BAC"]
	Output: false
	Explanation: We can't stack the pyramid to the top. Note that there could 
	             be allowed triples (A, B, C) and (A, B, D) with C != D.
	 
	Constraints:
	* bottom will be a string with length in range [2, 8].
	* allowed will have length in range [0, 200].
	* Letters in all strings will be chosen from the set {'A', 'B', 'C', 'D', 'E', 'F', 'G'}."""

    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        mp = {}
        for x, y, z in allowed: mp.setdefault((x, y), []).append(z)
        
        def fn(row):
            """Return True if row could be built from allowed transition."""
            if len(row) == 1: return True 
            for xx in product(*(mp.get((x, y), []) for x, y in zip(row, row[1:]))):
                if fn(xx): return True
            return False 
        
        return fn(bottom)


    """758. Bold Words in String (Easy)
	Given a set of keywords words and a string S, make all appearances of all 
	keywords in S bold. Any letters between <b> and </b> tags become bold. The 
	returned string should use the least number of tags possible, and of course 
	the tags should form a valid combination. For example, given that 
	words = ["ab", "bc"] and S = "aabcd", we should return "a<b>abc</b>d". Note 
	that returning "a<b>a<b>b</b>c</b>d" would use more tags, so it is incorrect.

	Constraints:
	* words has length in range [0, 50].
	* words[i] has length in range [1, 10].
	* S has length in range [0, 500].
	* All characters in words[i] and S are lowercase letters.
	* Note: This question is the same as 616: https://leetcode.com/problems/add-bold-tag-in-string/"""

    def boldWords(self, words: List[str], S: str) -> str:
        mark = [False]*len(S)
        
        for word in words: 
            k = -1
            while True: 
                k = S.find(word, k+1)
                if k == -1: break 
                mark[k:k+len(word)] = [True]*len(word)
        
        ans = []
        for i in range(len(S)): 
            if mark[i] and (i == 0 or not mark[i-1]): ans.append("<b>")
            ans.append(S[i])
            if mark[i] and (i+1 == len(S) or not mark[i+1]): ans.append("</b>")
        return "".join(ans)


    """760. Find Anagram Mappings (Easy)
	Given two lists Aand B, and B is an anagram of A. B is an anagram of A 
	means B is made by randomizing the order of the elements in A. We want to 
	find an index mapping P, from A to B. A mapping P[i] = j means the ith 
	element in A appears in B at index j. These lists A and B may contain 
	duplicates. If there are multiple answers, output any of them. For example, 
	given
	A = [12, 28, 46, 32, 50]
	B = [50, 12, 32, 46, 28]

	We should return [1, 4, 3, 2, 0] as P[0] = 1 because the 0th element of A 
	appears at B[1], and P[1] = 4 because the 1st element of A appears at B[4], 
	and so on.
	
	Note:
	* A, B have equal lengths in range [1, 100].
	* A[i], B[i] are integers in range [0, 10^5]."""

    def anagramMappings(self, A: List[int], B: List[int]) -> List[int]:
        mp = {}
        for i, x in enumerate(B):
            mp.setdefault(x, []).append(i)
        
        ans = []
        for x in A: 
            ans.append(mp[x].pop())
        return ans 


    """763. Partition Labels (Medium)
	A string S of lowercase English letters is given. We want to partition this 
	string into as many parts as possible so that each letter appears in at 
	most one part, and return a list of integers representing the size of these 
	parts.

	Example 1:
	Input: S = "ababcbacadefegdehijhklij"
	Output: [9,7,8]
	Explanation: The partition is "ababcbaca", "defegde", "hijhklij". This is a 
	             partition so that each letter appears in at most one part. A 
	             partition like "ababcbacadefegde", "hijhklij" is incorrect, 
	             because it splits S into less parts.
	Note:
	* S will have length in range [1, 500].
	* S will consist of lowercase English letters ('a' to 'z') only."""

    def partitionLabels(self, S: str) -> List[int]:
        mp = {c: i for i, c in enumerate(S)}
        ans = []
        ss = ee = 0
        for i, c in enumerate(S): 
            ee = max(ee, mp[c])
            if ee == i: 
                ans.append(ee - ss + 1)
                ss = ee + 1
        return ans 


    """764. Largest Plus Sign (Medium)
	In a 2D grid from (0, 0) to (N-1, N-1), every cell contains a 1, except 
	those cells in the given list mines which are 0. What is the largest axis-
	aligned plus sign of 1s contained in the grid? Return the order of the 
	plus sign. If there is none, return 0. An "axis-aligned plus sign of 1s of 
	order k" has some center grid[x][y] = 1 along with 4 arms of length k-1 
	going up, down, left, and right, and made of 1s. This is demonstrated in 
	the diagrams below. Note that there could be 0s or 1s beyond the arms of 
	the plus sign, only the relevant area of the plus sign is checked for 1s.

	Examples of Axis-Aligned Plus Signs of Order k:
	Order 1:
	000
	010
	000

	Order 2:
	00000
	00100
	01110
	00100
	00000

	Order 3:
	0000000
	0001000
	0001000
	0111110
	0001000
	0001000
	0000000

	Example 1:
	Input: N = 5, mines = [[4, 2]]
	Output: 2
	Explanation:
	11111
	11111
	11111
	11111
	11011
	In the above grid, the largest plus sign can only be order 2. One of them 
	is marked in bold.

	Example 2:
	Input: N = 2, mines = []
	Output: 1
	Explanation: There is no plus sign of order 2, but there is of order 1.

	Example 3:

	Input: N = 1, mines = [[0, 0]]
	Output: 0
	Explanation:
	There is no plus sign, so return 0.
	
	Note:
	* N will be an integer in the range [1, 500].
	* mines will have length at most 5000.
	* mines[i] will be length 2 and consist of integers in the range [0, N-1].
	* (Additionally, programs submitted in C, C++, or C# will be judged with a 
	  slightly smaller time limit.)"""

    def orderOfLargestPlusSign(self, N: int, mines: List[List[int]]) -> int:
        mines = {(x, y) for x, y in mines}
        dp = [[N]*N for _ in range(N)]
        for i in range(N):
            tt = ll = rr = bb = 0 # top | left | right | bottom 
            for j in range(N): 
                dp[i][j] = min(dp[i][j], ll := 0 if (i, j) in mines else ll+1)
                dp[j][i] = min(dp[j][i], tt := 0 if (j, i) in mines else tt+1)
                dp[~i][~j] = min(dp[~i][~j], rr := 0 if (~i%N, ~j%N) in mines else rr+1)
                dp[~j][~i] = min(dp[~j][~i], bb := 0 if (~j%N, ~i%N) in mines else bb+1)
        return max(map(max, dp))


    """767. Reorganize String (Medium)
	Given a string S, check if the letters can be rearranged so that two 
	characters that are adjacent to each other are not the same. If possible, 
	output any possible result.  If not possible, return the empty string.

	Example 1:
	Input: S = "aab"
	Output: "aba"

	Example 2:
	Input: S = "aaab"
	Output: ""
	Note: S will consist of lowercase letters and have length in range [1, 500]."""

    def reorganizeString(self, S: str) -> str:
        freq = {}
        for c in S: freq[c] = 1 +freq.get(c, 0) # frequency table 
        
        ans = [""]*len(S)
        i = 0
        for k in sorted(freq, reverse=True, key=freq.get): 
            if 2*freq[k] - 1 > len(S): return "" # impossible 
            for _ in range(freq[k]): 
                ans[i] = k
                i = i+2 if i+2 < len(S) else 1 # reset to 1 
        return "".join(ans)


    """769. Max Chunks To Make Sorted (Medium)
	Given an array arr that is a permutation of [0, 1, ..., arr.length - 1], we 
	split the array into some number of "chunks" (partitions), and individually 
	sort each chunk.  After concatenating them, the result equals the sorted 
	array. What is the most number of chunks we could have made?

	Example 1:
	Input: arr = [4,3,2,1,0]
	Output: 1
	Explanation: Splitting into two or more chunks will not return the required 
	             result. For example, splitting into [4, 3], [2, 1, 0] will 
	             result in [3, 4, 0, 1, 2], which isn't sorted.

	Example 2:
	Input: arr = [1,0,2,3,4]
	Output: 4
	Explanation: We can split into two chunks, such as [1, 0], [2, 3, 4]. 
	             However, splitting into [1, 0], [2], [3], [4] is the highest 
	             number of chunks possible.
	
	Note:
	* arr will have length in range [1, 10].
	* arr[i] will be a permutation of [0, 1, ..., arr.length - 1]."""

    def maxChunksToSorted(self, arr: List[int]) -> int:
        ans = prefix = 0
        for i, x in enumerate(arr): 
            prefix = max(prefix, x)
            if i == prefix: ans += 1
        return ans 


    """777. Swap Adjacent in LR String (Medium)
	In a string composed of 'L', 'R', and 'X' characters, like "RXXLRXRXL", a 
	move consists of either replacing one occurrence of "XL" with "LX", or 
	replacing one occurrence of "RX" with "XR". Given the starting string start 
	and the ending string end, return True if and only if there exists a 
	sequence of moves to transform one string to the other.

	Example 1:
	Input: start = "RXXLRXRXL", end = "XRLXXRRLX"
	Output: true
	Explanation: We can transform start to end following these steps:
	RXXLRXRXL ->
	XRXLRXRXL ->
	XRLXRXRXL ->
	XRLXXRRXL ->
	XRLXXRRLX

	Example 2:
	Input: start = "X", end = "L"
	Output: false

	Example 3:
	Input: start = "LLR", end = "RRL"
	Output: false

	Example 4:
	Input: start = "XL", end = "LX"
	Output: true

	Example 5:
	Input: start = "XLLR", end = "LXLX"
	Output: false

	Constraints:
	* 1 <= start.length <= 104
	* start.length == end.length
	* Both start and end will only consist of characters in 'L', 'R', and 'X'."""

    def canTransform(self, start: str, end: str) -> bool:
        ss = [(x, i) for i, x in enumerate(start) if x != "X"]
        ee = [(x, i) for i, x in enumerate(end) if x != "X"]
        
        if len(ss) != len(ee): return False 
        
        for (s, i), (e, j) in zip(ss, ee): 
            if s != e: return False 
            if s == e == "L" and i < j: return False 
            if s == e == "R" and i > j: return False 
        return True 


    """779. K-th Symbol in Grammar (Medium)
	On the first row, we write a 0. Now in every subsequent row, we look at the 
	previous row and replace each occurrence of 0 with 01, and each occurrence 
	of 1 with 10. Given row N and index K, return the K-th indexed symbol in 
	row N. (The values of K are 1-indexed.) (1 indexed).

	Examples:
	Input: N = 1, K = 1
	Output: 0

	Input: N = 2, K = 1
	Output: 0

	Input: N = 2, K = 2
	Output: 1

	Input: N = 4, K = 5
	Output: 1

	Explanation:
	row 1: 0
	row 2: 01
	row 3: 0110
	row 4: 01101001
	
	Note:
	* N will be an integer in the range [1, 30].
	* K will be an integer in the range [1, 2^(N-1)]."""

    def kthGrammar(self, N: int, K: int) -> int:
        return bin(K-1).count("1") & 1


    """781. Rabbits in Forest (Medium)
	In a forest, each rabbit has some color. Some subset of rabbits (possibly 
	all of them) tell you how many other rabbits have the same color as them. 
	Those answers are placed in an array. Return the minimum number of rabbits 
	that could be in the forest.

	Examples:
	Input: answers = [1, 1, 2]
	Output: 5
	Explanation:
	The two rabbits that answered "1" could both be the same color, say red. 
	The rabbit than answered "2" can't be red or the answers would be 
	inconsistent. Say the rabbit that answered "2" was blue. Then there should 
	be 2 other blue rabbits in the forest that didn't answer into the array. 
	The smallest possible number of rabbits in the forest is therefore 5: 3 
	that answered plus 2 that didn't.

	Input: answers = [10, 10, 10]
	Output: 11

	Input: answers = []
	Output: 0
	
	Note:
	* answers will have length at most 1000.
	* Each answers[i] will be an integer in the range [0, 999]."""

    def numRabbits(self, answers: List[int]) -> int:
        ans = 0
        cnt = defaultdict(int)
        for x in answers: 
            if not cnt[x] % (1 + x): ans += 1 + x # reached capacity & update ans
            cnt[x] += 1
        return ans 


    """784. Letter Case Permutation (Medium)
	Given a string S, we can transform every letter individually to be 
	lowercase or uppercase to create another string. Return a list of all 
	possible strings we could create. You can return the output in any order.

	Example 1:
	Input: S = "a1b2"
	Output: ["a1b2","a1B2","A1b2","A1B2"]

	Example 2:
	Input: S = "3z4"
	Output: ["3z4","3Z4"]

	Example 3:
	Input: S = "12345"
	Output: ["12345"]

	Example 4:
	Input: S = "0"
	Output: ["0"]

	Constraints:
	* S will be a string with length between 1 and 12.
	* S will consist only of letters or digits."""

    def letterCasePermutation(self, S: str) -> List[str]:
        ans = [""]
        for c in S: 
            ans = [x + cc for x in ans for cc in {c, c.swapcase()}]
        return ans 


    """785. Is Graph Bipartite? (Medium)
	There is an undirected graph with n nodes, where each node is numbered 
	between 0 and n - 1. You are given a 2D array graph, where graph[u] is an 
	array of nodes that node u is adjacent to. More formally, for each v in 
	graph[u], there is an undirected edge between node u and node v. The graph 
	has the following properties:
	* There are no self-edges (graph[u] does not contain u).
	* There are no parallel edges (graph[u] does not contain duplicate values).
	* If v is in graph[u], then u is in graph[v] (the graph is undirected).
	* The graph may not be connected, meaning there may be two nodes u and v 
	  such that there is no path between them.
	A graph is bipartite if the nodes can be partitioned into two independent 
	sets A and B such that every edge in the graph connects a node in set A and 
	a node in set B. Return true if and only if it is bipartite.

	Example 1:
	Input: graph = [[1,2,3],[0,2],[0,1,3],[0,2]]
	Output: false
	Explanation: There is no way to partition the nodes into two independent 
	             sets such that every edge connects a node in one and a node in 
	             the other.

	Example 2:
	Input: graph = [[1,3],[0,2],[1,3],[0,2]]
	Output: true
	Explanation: We can partition the nodes into two sets: {0, 2} and {1, 3}.

	Constraints:
	* graph.length == n
	* 1 <= n <= 100
	* 0 <= graph[u].length < n
	* 0 <= graph[u][i] <= n - 1
	* graph[u] does not contain u.
	* All the values of graph[u] are unique.
	* If graph[u] contains v, then graph[v] contains u."""

    def isBipartite(self, graph: List[List[int]]) -> bool:
        seen = [0]*len(graph)
        
        for k in range(len(graph)): 
            if not seen[k]: 
                seen[k] = 1
                stack = [k]
                while stack: 
                    n = stack.pop()
                    for nn in graph[n]: 
                        if not seen[nn]: 
                            seen[nn] = seen[n] + 1
                            stack.append(nn)
                        elif seen[n] & 1 == seen[nn] & 1: return False # check parity
        return True 


    """787. Cheapest Flights Within K Stops (Medium)
	There are n cities connected by m flights. Each flight starts from city u 
	and arrives at v with a price w. Now given all the cities and flights, 
	together with starting city src and the destination dst, your task is to 
	find the cheapest price from src to dst with up to k stops. If there is no 
	such route, output -1.

	Example 1:
	Input: 
	n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
	src = 0, dst = 2, k = 1
	Output: 200
	Explanation: The cheapest price from city 0 to city 2 with at most 1 stop 
	             costs 200, as marked red in the picture.

	Example 2:
	Input: 
	n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
	src = 0, dst = 2, k = 0
	Output: 500
	Explanation: The cheapest price from city 0 to city 2 with at most 0 stop 
	             costs 500, as marked blue in the picture.

	Constraints:
	* The number of nodes n will be in range [1, 100], with nodes labeled from 0 to n - 1.
	* The size of flights will be in range [0, n * (n - 1) / 2].
	* The format of each flight will be (src, dst, price).
	* The price of each flight will be in the range [1, 10000].
	* k is in the range of [0, n - 1].
	* There will not be any duplicated flights or self cycles."""

    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        graph = {} # digraph 
        for u, v, p in flights: 
            graph.setdefault(u, []).append((v, p)) 
            
        pq = [(0, -1, src)] # min-heap (cost-stop-city)
        while pq: 
            p, k, u = heappop(pq) # current stop 
            if k <= K: 
                if u == dst: return p
                for v, pp in graph.get(u, []): 
                    heappush(pq, (p + pp, k+1, v))
        return -1


    """789. Escape The Ghosts (Medium)
	You are playing a simplified PAC-MAN game on an infinite 2-D grid. You 
	start at the point [0, 0], and you are given a destination point 
	target = [xtarget, ytarget], which you are trying to get to. There are 
	several ghosts on the map with their starting positions given as an array 
	ghosts, where ghosts[i] = [xi, yi] represents the starting position of the 
	ith ghost. All inputs are integral coordinates. Each turn, you and all the 
	ghosts may independently choose to either move 1 unit in any of the four 
	cardinal directions: north, east, south, or west or stay still. All actions 
	happen simultaneously. You escape if and only if you can reach the target 
	before any ghost reaches you. If you reach any square (including the 
	target) at the same time as a ghost, it does not count as an escape. Return 
	true if it is possible to escape, otherwise return false.

	Example 1:
	Input: ghosts = [[1,0],[0,3]], target = [0,1]
	Output: true
	Explanation: You can reach the destination (0, 1) after 1 turn, while the 
	             ghosts located at (1, 0) and (0, 3) cannot catch up with you.

	Example 2:
	Input: ghosts = [[1,0]], target = [2,0]
	Output: false
	Explanation: You need to reach the destination (2, 0), but the ghost at 
	             (1, 0) lies between you and the destination.
	
	Example 3:
	Input: ghosts = [[2,0]], target = [1,0]
	Output: false
	Explanation: The ghost can reach the target at the same time as you.

	Example 4:
	Input: ghosts = [[5,0],[-10,-2],[0,-5],[-2,-2],[-7,1]], target = [7,7]
	Output: false

	Example 5:
	Input: ghosts = [[-1,0],[0,1],[-1,0],[0,1],[-1,0]], target = [0,0]
	Output: true

	Constraints:
	* 1 <= ghosts.length <= 100
	* ghosts[i].length == 2
	* -10^4 <= xi, yi <= 10^4
	* There can be multiple ghosts in the same location.
	* target.length == 2
	* -10^4 <= xtarget, ytarget <= 10^4"""

    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        xx, yy = target 
        return all(abs(x-xx) + abs(y-yy) > abs(xx) + abs(yy) for x, y in ghosts)


    """790. Domino and Tromino Tiling (Medium)
	We have two types of tiles: a 2x1 domino shape, and an "L" tromino shape. 
	These shapes may be rotated.
	XX  <- domino
	XX  <- "L" tromino
	X
	Given N, how many ways are there to tile a 2 x N board? Return your answer 
	modulo 10^9 + 7. (In a tiling, every square must be covered by a tile. Two 
	tilings are different if and only if there are two 4-directionally adjacent 
	cells on the board such that exactly one of the tilings has both squares 
	occupied by a tile.)

	Example:
	Input: 3
	Output: 5
	Explanation: 
	The five different ways are listed below, different letters indicates different tiles:
	XYZ XXZ XYY XXY XYY
	XYZ YYZ XZZ XYY XXY
	
	Note: N  will be in range [1, 1000]."""

    def numTilings(self, N: int) -> int:
        f0, f1, f2 = 0, 1, 1
        for i in range(N-1): 
            f0, f1, f2 = f1, f2, 2*f2 + f0
        return f2 % 1_000_000_007


    """791. Custom Sort String (Medium)
	S and T are strings composed of lowercase letters. In S, no letter occurs 
	more than once. S was sorted in some custom order previously. We want to 
	permute the characters of T so that they match the order that S was sorted. 
	More specifically, if x occurs before y in S, then x should occur before y 
	in the returned string. Return any permutation of T (as a string) that 
	satisfies this property.

	Example :
	Input: S = "cba"
		   T = "abcd"
	Output: "cbad"
	Explanation: "a", "b", "c" appear in S, so the order of "a", "b", "c" 
	             should be "c", "b", and "a". Since "d" does not appear in S, 
	             it can be at any position in T. "dcba", "cdba", "cbda" are 
	             also valid outputs.
	Note:
	* S has length at most 26, and no character is repeated in S.
	* T has length at most 200.
	* S and T consist of lowercase letters only."""

    def customSortString(self, S: str, T: str) -> str:
        mp = {c: i for i, c in enumerate(S)}
        return "".join(sorted(T, key=lambda x: mp.get(x, 26)))


    """795. Number of Subarrays with Bounded Maximum (Medium)
	We are given an array A of positive integers, and two positive integers L 
	and R (L <= R). Return the number of (contiguous, non-empty) subarrays such 
	that the value of the maximum array element in that subarray is at least L 
	and at most R.

	Example :
	Input: A = [2, 1, 4, 3]
	       L = 2
	       R = 3
	Output: 3
	Explanation: There are three subarrays that meet the requirements: [2], [2, 1], [3].
	
	Note:
	* L, R  and A[i] will be an integer in the range [0, 10^9].
	* The length of A will be in the range of [1, 50000]."""

    def numSubarrayBoundedMax(self, A: List[int], L: int, R: int) -> int:
        ans = val = cnt = 0
        for x in A: 
            if x < L: cnt += 1 # count of <= R
            elif L <= x <= R: val = cnt = cnt + 1
            else: val = cnt = 0 
            ans += val 
        return ans 


    """797. All Paths From Source to Target (Medium)
	Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, 
	find all possible paths from node 0 to node n - 1, and return them in any 
	order. The graph is given as follows: graph[i] is a list of all nodes you 
	can visit from node i (i.e., there is a directed edge from node i to node 
	graph[i][j]).

	Example 1:
	Input: graph = [[1,2],[3],[3],[]]
	Output: [[0,1,3],[0,2,3]]
	Explanation: There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.

	Example 2:
	Input: graph = [[4,3,1],[3,2,4],[3],[4],[]]
	Output: [[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]

	Example 3:
	Input: graph = [[1],[]]
	Output: [[0,1]]

	Example 4:
	Input: graph = [[1,2,3],[2],[3],[]]
	Output: [[0,1,2,3],[0,2,3],[0,3]]

	Example 5:
	Input: graph = [[1,3],[2],[3],[]]
	Output: [[0,1,2,3],[0,3]]

	Constraints:
	* n == graph.length
	* 2 <= n <= 15
	* 0 <= graph[i][j] < n
	* graph[i][j] != i (i.e., there will be no self-loops).
	* The input graph is guaranteed to be a DAG."""

    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        @lru_cache(None)
        def fn(n): 
            """Return path from given node to dst node."""
            if n == len(graph)-1: return [[n]]
            ans = []
            for nn in graph[n]: 
                ans.extend([[n] + x for x in fn(nn)])
            return ans 
        
        return fn(0)


    """800. Similar RGB Color (Easy)
	In the following, every capital letter represents some hexadecimal digit 
	from 0 to f. The red-green-blue color "#AABBCC" can be written as "#ABC" in 
	shorthand.  For example, "#15c" is shorthand for the color "#1155cc". Now, 
	say the similarity between two colors "#ABCDEF" and "#UVWXYZ" is 
	-(AB - UV)^2 - (CD - WX)^2 - (EF - YZ)^2. Given the color "#ABCDEF", return 
	a 7 character color that is most similar to #ABCDEF, and has a shorthand 
	(that is, it can be represented as some "#XYZ"

	Example 1:
	Input: color = "#09f166"
	Output: "#11ee66"
	Explanation: The similarity is 
	             -(0x09 - 0x11)^2 -(0xf1 - 0xee)^2 - (0x66 - 0x66)^2 = -64 -9 -0 = -73.
	             This is the highest among any shorthand color.
	
	Note:
	* color is a string of length 7.
	* color is a valid RGB color: for i > 0, color[i] is a hexadecimal digit from 0 to f
	* Any answer which has the same (highest) similarity as the best answer will be accepted.
	* All inputs and outputs should use lowercase letters, and the output is 7 characters."""

    def similarRGB(self, color: str) -> str:
        
        def fn(c):
            """Return color of xx closest to input."""
            ans = 0
            for k in range(1, 16): 
                ans = min(ans, k*16+k, key=lambda x: abs(x - int(c, 16)))
            return hex(ans)[2:].zfill(2)
        
        return "#" + "".join(fn(color[i:i+2]) for i in (1,3,5))


    """813. Largest Sum of Averages (Medium)
	We partition a row of numbers A into at most K adjacent (non-empty) groups, 
	then our score is the sum of the average of each group. What is the largest 
	score we can achieve? Note that our partition must use every number in A, 
	and that scores are not necessarily integers.

	Example:
	Input: A = [9,1,2,3,9]
	       K = 3
	Output: 20
	Explanation: The best choice is to partition A into [9], [1, 2, 3], [9]. 
	             The answer is 9 + (1 + 2 + 3) / 3 + 9 = 20. We could have also 
	             partitioned A into [9, 1], [2], [3, 9], for example. That 
	             partition would lead to a score of 5 + 2 + 6 = 13, which is worse.
	 
	Note:
	* 1 <= A.length <= 100.
	* 1 <= A[i] <= 10000.
	* 1 <= K <= A.length.
	* Answers within 10^-6 of the correct answer will be accepted as correct."""

    def largestSumOfAverages(self, A: List[int], K: int) -> float:
        prefix = [0]
        for x in A: prefix.append(prefix[-1] + x) # prefix sum 
        
        @lru_cache(None)
        def fn(i, k): 
            """Return largest sum of average of A[lo:hi+1] with at most k groups."""
            if i == 1 or k == 1: return prefix[i]/i # boundary condition 
            if i <= k: return prefix[i] # shortcut
            ans = fn(i, k-1)
            for ii in range(1, i):
                ans = max(ans, fn(i-ii, k-1) + (prefix[i] - prefix[i-ii])/ii)
            return ans 
            
        return fn(len(A), K)


    """816. Ambiguous Coordinates (Medium)
	We had some 2-dimensional coordinates, like "(1, 3)" or "(2, 0.5)".  Then, 
	we removed all commas, decimal points, and spaces, and ended up with the 
	string S.  Return a list of strings representing all possibilities for what 
	our original coordinates could have been. Our original representation never 
	had extraneous zeroes, so we never started with numbers like "00", "0.0", 
	"0.00", "1.0", "001", "00.01", or any other number that can be represented 
	with less digits.  Also, a decimal point within a number never occurs 
	without at least one digit occuring before it, so we never started with 
	numbers like ".1". The final answer list can be returned in any order.  
	Also note that all coordinates in the final answer have exactly one space 
	between them (occurring after the comma.)

	Example 1:
	Input: "(123)"
	Output: ["(1, 23)", "(12, 3)", "(1.2, 3)", "(1, 2.3)"]
	
	Example 2:
	Input: "(00011)"
	Output:  ["(0.001, 1)", "(0, 0.011)"]
	Explanation: 0.0, 00, 0001 or 00.01 are not allowed.
	
	Example 3:
	Input: "(0123)"
	Output: ["(0, 123)", "(0, 12.3)", "(0, 1.23)", "(0.1, 23)", "(0.1, 2.3)", "(0.12, 3)"]
	
	Example 4:
	Input: "(100)"
	Output: [(10, 0)]
	Explanation: 1.0 is not allowed.

	Note:
	* 4 <= S.length <= 12.
	* S[0] = "(", S[S.length - 1] = ")", and the other elements in S are digits."""

    def ambiguousCoordinates(self, S: str) -> List[str]:
        S = S[1:-1] # strip "(" and ")"
        
        def fn(s): 
            """Return valid number derived from s."""
            if len(s) == 1: return [s] # edge case 
            if s.startswith("0") and s.endswith("0"): return []
            if s.startswith("0"): return [s[:1] + "." + s[1:]]
            if s.endswith("0"): return [s]
            return [s] + [s[:i] + "." + s[i:] for i in range(1, len(s))]

        ans = []
        for i in range(1, len(S)): 
            ans.extend([f"({x}, {y})" for x in fn(S[:i]) for y in fn(S[i:])])
        return ans



    """817. Linked List Components (Medium)
	We are given head, the head node of a linked list containing unique integer 
	values. We are also given the list G, a subset of the values in the linked 
	list. Return the number of connected components in G, where two values are 
	connected if they appear consecutively in the linked list.

	Example 1:
	Input: head: 0->1->2->3
	       G = [0, 1, 3]
	Output: 2
	Explanation: 0 and 1 are connected, so [0, 1] and [3] are the two connected 
	             components.

	Example 2:
	Input: head: 0->1->2->3->4
	       G = [0, 3, 1, 4]
	Output: 2
	Explanation: 0 and 1 are connected, 3 and 4 are connected, so [0, 1] and 
	             [3, 4] are the two connected components.
	
	Note:
	* If N is the length of the linked list given by head, 1 <= N <= 10000.
	* The value of each node in the linked list will be in the range [0, N - 1].
	* 1 <= G.length <= 10000.
	* G is a subset of all values in the linked list."""

    def numComponents(self, head: ListNode, G: List[int]) -> int:
        Gs = set(G)
        ans = 0
        while head: 
            if head.val in Gs and (head.next is None or head.next.val not in Gs): ans += 1
            head = head.next 
        return ans 


    """821. Shortest Distance to a Character (Easy)
	Given a string s and a character c that occurs in s, return an array of 
	integers answer where answer.length == s.length and answer[i] is the 
	shortest distance from s[i] to the character c in s.

	Example 1:
	Input: s = "loveleetcode", c = "e"
	Output: [3,2,1,0,1,0,0,1,2,2,1,0]

	Example 2:
	Input: s = "aaab", c = "b"
	Output: [3,2,1,0]

	Constraints:
	* 1 <= s.length <= 104
	* s[i] and c are lowercase English letters.
	* c occurs at least once in s."""

    def shortestToChar(self, s: str, c: str) -> List[int]:
        locs = [i for i, x in enumerate(s) if x == c]
        ans = []
        k = 0
        for i, c in enumerate(s):
            if k+1 < len(locs) and locs[k+1]-i < i - locs[k]: k += 1
            ans.append(abs(i - locs[k]))
        return ans 


    """822. Card Flipping Game (Medium)
	On a table are N cards, with a positive integer printed on the front and 
	back of each card (possibly different). We flip any number of cards, and 
	after we choose one card. If the number X on the back of the chosen card 
	is not on the front of any card, then this number X is good. What is the 
	smallest number that is good?  If no number is good, output 0. Here, 
	fronts[i] and backs[i] represent the number on the front and back of card 
	i. A flip swaps the front and back numbers, so the value on the front is 
	now on the back and vice versa.

	Example:
	Input: fronts = [1,2,4,4,7], backs = [1,3,4,1,3]
	Output: 2
	Explanation: If we flip the second card, the fronts are [1,3,4,4,7] and the 
	             backs are [1,2,4,1,3]. We choose the second card, which has 
	             number 2 on the back, and it isn't on the front of any card, 
	             so 2 is good.
	Note:
	* 1 <= fronts.length == backs.length <= 1000.
	* 1 <= fronts[i] <= 2000.
	* 1 <= backs[i] <= 2000."""

    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        same = {ff for ff, bb in zip(fronts, backs) if ff == bb}
        return min((x for x in fronts+backs if x not in same), default=0)


    """823. Binary Trees With Factors (Medium)
	Given an array of unique integers, each integer is strictly greater than 1. 
	We make a binary tree using these integers and each number may be used for 
	any number of times. Each non-leaf node's value should be equal to the 
	product of the values of it's children. How many binary trees can we make?  
	Return the answer modulo 10 ** 9 + 7.

	Example 1:
	Input: A = [2, 4]
	Output: 3
	Explanation: We can make these trees: [2], [4], [4, 2, 2]

	Example 2:
	Input: A = [2, 4, 5, 10]
	Output: 7
	Explanation: We can make these trees: [2], [4], [5], [10], [4, 2, 2], 
	             [10, 2, 5], [10, 5, 2].

	Note:
	* 1 <= A.length <= 1000.
	* 2 <= A[i] <= 10 ^ 9."""

    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        freq = {}
        for x in sorted(arr): 
            freq[x] = 1
            for xx in freq: 
                freq[x] += freq[xx] * freq.get(x/xx, 0)
        return sum(freq.values()) % 1_000_000_007


    """825. Friends Of Appropriate Ages (Medium)
	Some people will make friend requests. The list of their ages is given and 
	ages[i] is the age of the ith person. Person A will NOT friend request 
	person B (B != A) if any of the following conditions are true:
	* age[B] <= 0.5 * age[A] + 7
	* age[B] > age[A]
	* age[B] > 100 && age[A] < 100
	Otherwise, A will friend request B. Note that if A requests B, B does not 
	necessarily request A.  Also, people will not friend request themselves. 
	How many total friend requests are made?

	Example 1:
	Input: [16,16]
	Output: 2
	Explanation: 2 people friend request each other.
	
	Example 2:
	Input: [16,17,18]
	Output: 2
	Explanation: Friend requests are made 17 -> 16, 18 -> 17.

	Example 3:
	Input: [20,30,100,110,120]
	Output: 3
	Explanation: Friend requests are made 110 -> 100, 120 -> 110, 120 -> 100.

	Notes:
	* 1 <= ages.length <= 20000.
	* 1 <= ages[i] <= 120."""

    def numFriendRequests(self, ages: List[int]) -> int:
        freq = {}
        for x in ages: freq[x] = 1 + freq.get(x, 0)
        
        ans = 0 
        for x in freq: 
            for y in freq: 
                if 0.5*x + 7 < y <= x: 
                    ans += freq[x] * freq[y]
                    if x == y: ans -= freq[x]
        return ans 


    """826. Most Profit Assigning Work (Medium)
	We have jobs: difficulty[i] is the difficulty of the ith job, and profit[i] 
	is the profit of the ith job. Now we have some workers. worker[i] is the 
	ability of the ith worker, which means that this worker can only complete a 
	job with difficulty at most worker[i]. Every worker can be assigned at most 
	one job, but one job can be completed multiple times. For example, if 3 
	people attempt the same job that pays $1, then the total profit will be $3.
	If a worker cannot complete any job, his profit is $0. What is the most 
	profit we can make?

	Example 1:
	Input: difficulty = [2,4,6,8,10], profit = [10,20,30,40,50], worker = [4,5,6,7]
	Output: 100 
	Explanation: Workers are assigned jobs of difficulty [4,4,6,6] and they get 
	             profit of [20,20,30,30] seperately.

	Notes:
	* 1 <= difficulty.length = profit.length <= 10000
	* 1 <= worker.length <= 10000
	* difficulty[i], profit[i], worker[i]  are in range [1, 10^5]"""

    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        job = sorted(zip(difficulty, profit))
        ans = i = mx = 0 
        for w in sorted(worker): 
            while i < len(job) and job[i][0] <= w: 
                mx = max(mx, job[i][1])
                i += 1
            ans += mx 
        return ans 


    """831. Masking Personal Information (Medium)
	We are given a personal information string S, which may represent either an 
	email address or a phone number. We would like to mask this personal 
	information according to the following rules:

	1. Email address:
	We define a name to be a string of length ≥ 2 consisting of only lowercase 
	letters a-z or uppercase letters A-Z. An email address starts with a name, 
	followed by the symbol '@', followed by a name, followed by the dot '.' and 
	followed by a name. All email addresses are guaranteed to be valid and in 
	the format of "name1@name2.name3". To mask an email, all names must be 
	converted to lowercase and all letters between the first and last letter of 
	the first name must be replaced by 5 asterisks '*'.

	2. Phone number:
	A phone number is a string consisting of only the digits 0-9 or the 
	characters from the set {'+', '-', '(', ')', ' '}. You may assume a phone 
	number contains 10 to 13 digits. The last 10 digits make up the local 
	number, while the digits before those make up the country code. Note that 
	the country code is optional. We want to expose only the last 4 digits and 
	mask all other digits. The local number should be formatted and masked as 
	"***-***-1111", where 1 represents the exposed digits. To mask a phone 
	number with country code like "+111 111 111 1111", we write it in the form 
	"+***-***-***-1111".  The '+' sign and the first '-' sign before the local 
	number should only exist if there is a country code.  For example, a 12 
	digit phone number mask should start with "+**-". Note that extraneous 
	characters like "(", ")", " ", as well as extra dashes or plus signs not 
	part of the above formatting scheme should be removed.

	Return the correct "mask" of the information provided.

	Example 1:
	Input: "LeetCode@LeetCode.com"
	Output: "l*****e@leetcode.com"
	Explanation: All names are converted to lowercase, and the letters between 
	             the first and last letter of the first name is replaced by 5 
	             asterisks. Therefore, "leetcode" -> "l*****e".

	Example 2:
	Input: "AB@qq.com"
	Output: "a*****b@qq.com"
	Explanation: There must be 5 asterisks between the first and last letter 
	             of the first name "ab". Therefore, "ab" -> "a*****b".
	
	Example 3:
	Input: "1(234)567-890"
	Output: "***-***-7890"
	Explanation: 10 digits in the phone number, which means all digits make up 
	             the local number.

	Example 4:
	Input: "86-(10)12345678"
	Output: "+**-***-***-5678"
	Explanation: 12 digits, 2 digits for country code and 10 digits for local 
	             number. 

	Notes:
	* S.length <= 40.
	* Emails have length at least 8.
	* Phone numbers have length at least 10."""

    def maskPII(self, S: str) -> str:
        if "@" in S: # email address
            name, domain = S.lower().split("@")
            return f"{name[0]}*****{name[-1]}@{domain}"
        else: # phone number 
            d = "".join(c for c in S if c.isdigit())
            ans = f"***-***-{d[-4:]}"
            return ans if len(d) == 10 else f"+{'*'*(len(d)-10)}-" + ans 


    """832. Flipping an Image (Easy)
	Given a binary matrix A, we want to flip the image horizontally, then 
	invert it, and return the resulting image. To flip an image horizontally 
	means that each row of the image is reversed.  For example, flipping 
	[1, 1, 0] horizontally results in [0, 1, 1]. To invert an image means that 
	each 0 is replaced by 1, and each 1 is replaced by 0. For example, 
	inverting [0, 1, 1] results in [1, 0, 0].

	Example 1:
	Input: [[1,1,0],[1,0,1],[0,0,0]]
	Output: [[1,0,0],[0,1,0],[1,1,1]]
	Explanation: First reverse each row: [[0,1,1],[1,0,1],[0,0,0]]. Then, 
	             invert the image: [[1,0,0],[0,1,0],[1,1,1]]

	Example 2:
	Input: [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
	Output: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
	Explanation: First reverse each row: [[0,0,1,1],[1,0,0,1],[1,1,1,0],[0,1,0,1]]. 
	             Then invert the image: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]

	Notes:
	* 1 <= A.length = A[0].length <= 20
	* 0 <= A[i][j] <= 1"""

    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        m, n = len(A), len(A[0])
        for i in range(m):
            for j in range(n+1 >> 1): 
                A[i][j], A[i][~j] = 1^A[i][~j], 1^A[i][j]
        return A


    """833. Find And Replace in String (Medium)
	To some string S, we will perform some replacement operations that replace 
	groups of letters with new ones (not necessarily the same size). Each 
	replacement operation has 3 parameters: a starting index i, a source word x 
	and a target word y.  The rule is that if x starts at position i in the 
	original string S, then we will replace that occurrence of x with y.  If 
	not, we do nothing. For example, if we have S = "abcd" and we have some 
	replacement operation i = 2, x = "cd", y = "ffff", then because "cd" starts 
	at position 2 in the original string S, we will replace it with "ffff". 
	Using another example on S = "abcd", if we have both the replacement 
	operation i = 0, x = "ab", y = "eee", as well as another replacement 
	operation i = 2, x = "ec", y = "ffff", this second operation does nothing 
	because in the original string S[2] = 'c', which doesn't match x[0] = 'e'. 
	All these operations occur simultaneously.  

	It's guaranteed that there won't be any overlap in replacement: for example, 
	S = "abc", indexes = [0, 1], sources = ["ab","bc"] is not a valid test case.

	Example 1:
	Input: S = "abcd", indexes = [0, 2], sources = ["a", "cd"], targets = ["eee", "ffff"]
	Output: "eeebffff"
	Explanation: "a" starts at index 0 in S, so it's replaced by "eee".
	             "cd" starts at index 2 in S, so it's replaced by "ffff".

	Example 2:
	Input: S = "abcd", indexes = [0, 2], sources = ["ab","ec"], targets = ["eee","ffff"]
	Output: "eeecd"
	Explanation: "ab" starts at index 0 in S, so it's replaced by "eee".
	             "ec" doesn't starts at index 2 in the original S, so we do nothing.

	Constraints:
	* 0 <= S.length <= 1000
	* S consists of only lowercase English letters.
	* 0 <= indexes.length <= 100
	* 0 <= indexes[i] < S.length
	* sources.length == indexes.length
	* targets.length == indexes.length
	* 1 <= sources[i].length, targets[i].length <= 50
	* sources[i] and targets[i] consist of only lowercase English letters."""

    def findReplaceString(self, S: str, indexes: List[int], sources: List[str], targets: List[str]) -> str:
        for i, s, t in sorted(zip(indexes, sources, targets), reverse=True): 
            if S[i:i+len(s)] == s: S = S[:i] + t + S[i+len(s):]
        return S


    """837. New 21 Game (Medium)
	Alice plays the following game, loosely based on the card game "21". Alice 
	starts with 0 points, and draws numbers while she has less than K points. 
	During each draw, she gains an integer number of points randomly from the 
	range [1, W], where W is an integer.  Each draw is independent and the 
	outcomes have equal probabilities. Alice stops drawing numbers when she 
	gets K or more points.  What is the probability that she has N or less 
	points?

	Example 1:
	Input: N = 10, K = 1, W = 10
	Output: 1.00000
	Explanation:  Alice gets a single card, then stops.

	Example 2:
	Input: N = 6, K = 1, W = 10
	Output: 0.60000
	Explanation:  Alice gets a single card, then stops.
	In 6 out of W = 10 possibilities, she is at or below N = 6 points.

	Example 3:
	Input: N = 21, K = 17, W = 10
	Output: 0.73278

	Note:
	* 0 <= K <= N <= 10000
	* 1 <= W <= 10000
	* Answers will be accepted as correct if they are within 10^-5 of the correct answer.
	* The judging time limit has been reduced for this question."""

    def new21Game(self, N: int, K: int, W: int) -> float:
        ans = [0]*K + [1]*(N-K+1) + [0]*W
        val = sum(ans[K:K+W+1])
        for i in reversed(range(K)): 
            ans[i] = val/W
            val += ans[i] - ans[i+W]
        return ans[0]


    """840. Magic Squares In Grid (Medium)
	A 3 x 3 magic square is a 3 x 3 grid filled with distinct numbers from 1 to 
	9 such that each row, column, and both diagonals all have the same sum. 
	Given a row x col grid of integers, how many 3 x 3 "magic square" subgrids 
	are there?  (Each subgrid is contiguous).

	Example 1:
	Input: grid = [[4,3,8,4],[9,5,1,9],[2,7,6,2]]
	Output: 1
	
	Example 2:
	Input: grid = [[8]]
	Output: 0

	Example 3:
	Input: grid = [[4,4],[3,3]]
	Output: 0

	Example 4:
	Input: grid = [[4,7,8],[9,5,1],[2,3,6]]
	Output: 0

	Constraints:
	* row == grid.length
	* col == grid[i].length
	* 1 <= row, col <= 10
	* 0 <= grid[i][j] <= 15"""

    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0]) # dimension 
        
        def fn(i, j): 
            """Return True if grid[i-1:i+2][j-1:j+2] is a magic squre."""
            seen = set()
            row, col = [0]*3, [0]*3 # row sum & column sum 
            diag = anti = 0
            for ii in range(i-1, i+2):
                for jj in range(j-1, j+2):
                    if not 0 <= grid[ii][jj] < 10 or grid[ii][jj] in seen: return False 
                    seen.add(grid[ii][jj])
                    row[ii-i+1] += grid[ii][jj]
                    col[jj-j+1] += grid[ii][jj]
                    if ii-jj == i-j: diag += grid[ii][jj]
                    if ii+jj == i+j: anti += grid[ii][jj]
            return len(set(row)) == 1 and len(set(col)) == 1 and row[0] == col[0] == diag == anti
        
        ans = 0
        for i in range(1, m-1):
            for j in range(1, n-1): 
                if grid[i][j] == 5 and fn(i, j): ans += 1
        return ans 


    """841. Keys and Rooms (Medium)
	There are N rooms and you start in room 0. Each room has a distinct number 
	in 0, 1, 2, ..., N-1, and each room may have some keys to access the next 
	room. Formally, each room i has a list of keys rooms[i], and each key 
	rooms[i][j] is an integer in [0, 1, ..., N-1] where N = rooms.length.  A 
	key rooms[i][j] = v opens the room with number v. Initially, all the rooms 
	start locked (except for room 0). You can walk back and forth between rooms 
	freely. Return true if and only if you can enter every room.

	Example 1:
	Input: [[1],[2],[3],[]]
	Output: true
	Explanation:  
	We start in room 0, and pick up key 1.
	We then go to room 1, and pick up key 2.
	We then go to room 2, and pick up key 3.
	We then go to room 3.  Since we were able to go to every room, we return true.

	Example 2:
	Input: [[1,3],[3,0,1],[2],[0]]
	Output: false
	Explanation: We can't enter the room with number 2.

	Note:
	* 1 <= rooms.length <= 1000
	* 0 <= rooms[i].length <= 1000
	* The number of keys in all rooms combined is at most 3000."""

    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        seen = [False]*len(rooms)
        stack = [0]
        while stack: 
            n = stack.pop()
            if not seen[n]:
                seen[n] = True 
                stack.extend(rooms[n])
        return all(seen)


    """845. Longest Mountain in Array (Medium)
	Let's call any (contiguous) subarray B (of A) a mountain if the following 
	properties hold:
	* B.length >= 3
	* There exists some 0 < i < B.length - 1 such that 
	  B[0] < B[1] < ... B[i-1] < B[i] > B[i+1] > ... > B[B.length - 1]
	(Note that B could be any subarray of A, including the entire array A.)
	Given an array A of integers, return the length of the longest mountain. 
	Return 0 if there is no mountain.

	Example 1:
	Input: [2,1,4,7,3,2,5]
	Output: 5
	Explanation: The largest mountain is [1,4,7,3,2] which has length 5.

	Example 2:
	Input: [2,2,2]
	Output: 0
	Explanation: There is no mountain.

	Note:
	* 0 <= A.length <= 10000
	* 0 <= A[i] <= 10000
	
	Follow up:
	* Can you solve it using only one pass?
	* Can you solve it in O(1) space?"""

    def longestMountain(self, A: List[int]) -> int:
        ans = 0
        for i in range(1, len(A)-1): 
            if A[i-1] < A[i] > A[i+1]: 
                lo = hi = i
                while 0 < lo and A[lo-1] < A[lo]: lo -= 1
                while hi < len(A)-1 and A[hi] > A[hi+1]: hi += 1
                ans = max(ans, hi - lo + 1)
        return ans 


    """848. Shifting Letters (Medium)
	We have a string S of lowercase letters, and an integer array shifts. Call 
	the shift of a letter, the next letter in the alphabet, (wrapping around so 
	that 'z' becomes 'a'). For example, shift('a') = 'b', shift('t') = 'u', and 
	shift('z') = 'a'. Now for each shifts[i] = x, we want to shift the first 
	i+1 letters of S, x times. Return the final string after all such shifts to 
	S are applied.

	Example 1:
	Input: S = "abc", shifts = [3,5,9]
	Output: "rpl"
	Explanation: We start with "abc".
	After shifting the first 1 letters of S by 3, we have "dbc".
	After shifting the first 2 letters of S by 5, we have "igc".
	After shifting the first 3 letters of S by 9, we have "rpl", the answer.

	Note:
	* 1 <= S.length = shifts.length <= 20000
	* 0 <= shifts[i] <= 10 ^ 9"""

    def shiftingLetters(self, S: str, shifts: List[int]) -> str:
        for i in reversed(range(1, len(shifts))): shifts[i-1] += shifts[i]
        return "".join(chr(97 + (ord(c) - 97 + x) % 26) for c, x in zip(S, shifts))


    """849. Maximize Distance to Closest Person (Medium)
	You are given an array representing a row of seats where seats[i] = 1 
	represents a person sitting in the ith seat, and seats[i] = 0 represents 
	that the ith seat is empty (0-indexed). There is at least one empty seat, 
	and at least one person sitting. Alex wants to sit in the seat such that 
	the distance between him and the closest person to him is maximized. Return 
	that maximum distance to the closest person.

	Example 1:
	Input: seats = [1,0,0,0,1,0,1]
	Output: 2
	Explanation: If Alex sits in the second open seat (i.e. seats[2]), then the 
	             closest person has distance 2. If Alex sits in any other open 
	             seat, the closest person has distance 1. Thus, the maximum 
	             distance to the closest person is 2.

	Example 2:
	Input: seats = [1,0,0,0]
	Output: 3
	Explanation: If Alex sits in the last seat (i.e. seats[3]), the closest 
	             person is 3 seats away. This is the maximum distance possible, 
	             so the answer is 3.
	
	Example 3:
	Input: seats = [0,1]
	Output: 1

	Constraints:
	* 2 <= seats.length <= 2 * 104
	* seats[i] is 0 or 1.
	* At least one seat is empty.
	* At least one seat is occupied."""

    def maxDistToClosest(self, seats: List[int]) -> int:
        ans = 0
        ii = -1
        for i, x in enumerate(seats): 
            if x: 
                ans = max(ans, i) if ii < 0 else max(ans, (i-ii)//2)
                ii = i 
        return max(ans, i - ii)


    """851. Loud and Rich (Medium)
	In a group of N people (labelled 0, 1, 2, ..., N-1), each person has 
	different amounts of money, and different levels of quietness. For 
	convenience, we'll call the person with label x, simply "person x". We'll 
	say that richer[i] = [x, y] if person x definitely has more money than 
	person y.  Note that richer may only be a subset of valid observations. 
	Also, we'll say quiet[x] = q if person x has quietness q. Now, return 
	answer, where answer[x] = y if y is the least quiet person (that is, the 
	person y with the smallest value of quiet[y]), among all people who 
	definitely have equal to or more money than person x.

	Example 1:
	Input: richer = [[1,0],[2,1],[3,1],[3,7],[4,3],[5,3],[6,3]], 
	       quiet = [3,2,5,4,6,1,7,0]
	Output: [5,5,2,5,4,5,6,7]
	Explanation: 
	answer[0] = 5.
	Person 5 has more money than 3, which has more money than 1, which has more 
	money than 0. The only person who is quieter (has lower quiet[x]) is person 
	7, but it isn't clear if they have more money than person 0.
	answer[7] = 7.
	Among all people that definitely have equal to or more money than person 7
	(which could be persons 3, 4, 5, 6, or 7), the person who is the quietest 
	(has lower quiet[x]) is person 7. The other answers can be filled out with 
	similar reasoning.
	
	Note:
	* 1 <= quiet.length = N <= 500
	* 0 <= quiet[i] < N, all quiet[i] are different.
	* 0 <= richer.length <= N * (N-1) / 2
	* 0 <= richer[i][j] < N
	* richer[i][0] != richer[i][1]
	* richer[i]'s are all different.
	* The observations in richer are all logically consistent."""

    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        graph = {} # graph as adjacency list 
        for x, y in richer: graph.setdefault(y, []).append(x)
        
        @lru_cache(None)
        def fn(x): 
            """Return richer & loudest person given person."""
            ans = x
            for xx in graph.get(x, []): 
                if quiet[fn(xx)] < quiet[ans]: ans = fn(xx)
            return ans 
        
        return [fn(x) for x in range(len(quiet))]


    """853. Car Fleet (Medium)
	N cars are going to the same destination along a one lane road. The 
	destination is target miles away. Each car i has a constant speed speed[i] 
	(in miles per hour), and initial position position[i] miles towards the 
	target along the road. A car can never pass another car ahead of it, but it 
	can catch up to it, and drive bumper to bumper at the same speed. The 
	distance between these two cars is ignored - they are assumed to have the 
	same position. A car fleet is some non-empty set of cars driving at the 
	same position and same speed.  Note that a single car is also a car fleet. 
	If a car catches up to a car fleet right at the destination point, it will 
	still be considered as one car fleet. How many car fleets will arrive at 
	the destination?

	Example 1:
	Input: target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]
	Output: 3
	Explanation:
	The cars starting at 10 and 8 become a fleet, meeting each other at 12.
	The car starting at 0 doesn't catch up to any other car, so it is a fleet by itself.
	The cars starting at 5 and 3 become a fleet, meeting each other at 6.
	Note that no other cars meet these fleets before the destination, so the answer is 3.

	Note:
	* 0 <= N <= 10 ^ 4
	* 0 < target <= 10 ^ 6
	* 0 < speed[i] <= 10 ^ 6
	* 0 <= position[i] < target
	* All initial positions are different."""

    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        ans = prev = 0
        for pp, ss in sorted(zip(position, speed), reverse=True): 
            tt = (target - pp)/ss # time to arrive at target 
            if prev < tt: 
                ans += 1
                prev = tt
        return ans 


    """856. Score of Parentheses (Medium)
	Given a balanced parentheses string S, compute the score of the string 
	based on the following rule:
	* () has score 1
	* AB has score A + B, where A and B are balanced parentheses strings.
	* (A) has score 2 * A, where A is a balanced parentheses string.

	Example 1:
	Input: "()"
	Output: 1

	Example 2:
	Input: "(())"
	Output: 2

	Example 3:
	Input: "()()"
	Output: 2

	Example 4:
	Input: "(()(()))"
	Output: 6

	Note:
	* S is a balanced parentheses string, containing only ( and ).
	* 2 <= S.length <= 50"""

    def scoreOfParentheses(self, S: str) -> int:
        ans, stack = 0, []
        for c in S: 
            if c == "(": 
                stack.append(ans)
                ans = 0
            else: ans = max(1, 2*ans) + stack.pop()
        return ans


    """865. Smallest Subtree with all the Deepest Nodes (Medium)
	Given the root of a binary tree, the depth of each node is the shortest 
	distance to the root. Return the smallest subtree such that it contains all 
	the deepest nodes in the original tree. A node is called the deepest if it 
	has the largest depth possible among any node in the entire tree. The 
	subtree of a node is tree consisting of that node, plus the set of all 
	descendants of that node.

	Example 1:
	Input: root = [3,5,1,6,2,0,8,null,null,7,4]
	Output: [2,7,4]
	Explanation: We return the node with value 2, colored in yellow in the 
	             diagram. The nodes coloured in blue are the deepest nodes of 
	             the tree. Notice that nodes 5, 3 and 2 contain the deepest 
	             nodes in the tree but node 2 is the smallest subtree among 
	             them, so we return it.

	Example 2:
	Input: root = [1]
	Output: [1]
	Explanation: The root is the deepest node in the tree.
	
	Example 3:
	Input: root = [0,1,3,null,2]
	Output: [2]
	Explanation: The deepest node in the tree is 2, the valid subtrees are the 
	             subtrees of nodes 2, 1 and 0 but the subtree of node 2 is the 
	             smallest.

	Constraints:
	* The number of nodes in the tree will be in the range [1, 500].
	* 0 <= Node.val <= 500
	* The values of the nodes in the tree are unique."""

    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        
        @lru_cache(None)
        def fn(node):
            """Return height of tree rooted at node."""
            if not node: return 0
            return 1 + max(fn(node.left), fn(node.right))
        
        node = root
        while node: 
            left, right = fn(node.left), fn(node.right)
            if left == right: return node
            elif left > right: node = node.left
            else: node = node.right 


    """869. Reordered Power of 2 (Medium)
	Starting with a positive integer N, we reorder the digits in any order 
	(including the original order) such that the leading digit is not zero. 
	Return true if and only if we can do this in a way such that the resulting 
	number is a power of 2.

	Example 1:
	Input: 1
	Output: true

	Example 2:
	Input: 10
	Output: false

	Example 3:
	Input: 16
	Output: true

	Example 4:
	Input: 24
	Output: false

	Example 5:
	Input: 46
	Output: true

	Note: 1 <= N <= 10^9"""

    def reorderedPowerOf2(self, N: int) -> bool:
        return any(Counter(str(N)) == Counter(str(1 << i)) for i in range(30))


    """881. Boats to Save People (Medium)
	The i-th person has weight people[i], and each boat can carry a maximum 
	weight of limit. Each boat carries at most 2 people at the same time, 
	provided the sum of the weight of those people is at most limit. Return the 
	minimum number of boats to carry every given person.  (It is guaranteed 
	each person can be carried by a boat.)

	Example 1:
	Input: people = [1,2], limit = 3
	Output: 1
	Explanation: 1 boat (1, 2)

	Example 2:
	Input: people = [3,2,2,1], limit = 3
	Output: 3
	Explanation: 3 boats (1, 2), (2) and (3)

	Example 3:
	Input: people = [3,5,3,4], limit = 5
	Output: 4
	Explanation: 4 boats (3), (3), (4), (5)

	Note:
	* 1 <= people.length <= 50000
	* 1 <= people[i] <= limit <= 30000"""

    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        
        ans = 0
        lo, hi = 0, len(people)-1
        while lo < hi: 
            if people[lo] + people[hi] <= limit: lo += 1
            ans += 1
            hi -= 1
        return ans + (lo == hi)


    """889. Construct Binary Tree from Preorder and Postorder Traversal (Medium)
	Return any binary tree that matches the given preorder and postorder 
	traversals. Values in the traversals pre and post are distinct positive 
	integers.

	Example 1:
	Input: pre = [1,2,4,5,3,6,7], post = [4,5,2,6,7,3,1]
	Output: [1,2,3,4,5,6,7]

	Note:
	* 1 <= pre.length == post.length <= 30
	* pre[] and post[] are both permutations of 1, 2, ..., pre.length.
	* It is guaranteed an answer exists. If there exists multiple answers, you 
	  can return any of them."""


    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
        mp = {x: i for i, x in enumerate(post)}
        
        root = None 
        stack = []
        for x in pre: 
            if not root: root = node = TreeNode(x)
            elif mp[x] < mp[stack[-1].val]: stack[-1].left = node = TreeNode(x)
            else: 
                while mp[stack[-1].val] < mp[x]: stack.pop() # retrace 
                stack[-1].right = node = TreeNode(x)
            stack.append(node)
        return root 


    """890. Find and Replace Pattern (Medium)
	You have a list of words and a pattern, and you want to know which words in 
	words matches the pattern. A word matches the pattern if there exists a 
	permutation of letters p so that after replacing every letter x in the 
	pattern with p(x), we get the desired word. (Recall that a permutation of 
	letters is a bijection from letters to letters: every letter maps to 
	another letter, and no two letters map to the same letter.) Return a list 
	of the words in words that match the given pattern. You may return the 
	answer in any order.

	Example 1:
	Input: words = ["abc","deq","mee","aqq","dkd","ccc"], pattern = "abb"
	Output: ["mee","aqq"]
	Explanation: "mee" matches the pattern because there is a permutation 
	             {a -> m, b -> e, ...}. "ccc" does not match the pattern 
	             because {a -> c, b -> c, ...} is not a permutation, since a 
	             and b map to the same letter.

	Note:
	* 1 <= words.length <= 50
	* 1 <= pattern.length = words[i].length <= 20"""

    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        fn = lambda x: len(set(zip(x, pattern))) == len(set(x)) == len(set(pattern))
        return [word for word in words if fn(word)]


    """894. All Possible Full Binary Trees (Medium)
	A full binary tree is a binary tree where each node has exactly 0 or 2 
	children. Return a list of all possible full binary trees with N nodes. 
	Each element of the answer is the root node of one possible tree. Each node 
	of each tree in the answer must have node.val = 0. You may return the final 
	list of trees in any order.

	Example 1:
	Input: 7
	Output: [[0,0,0,null,null,0,0,null,null,0,0],[0,0,0,null,null,0,0,0,0],
	         [0,0,0,0,0,0,0],[0,0,0,0,0,null,null,null,null,0,0],
	         [0,0,0,0,0,null,null,0,0]]

	Note: 1 <= N <= 20"""

    def allPossibleFBT(self, N: int) -> List[TreeNode]:
        
        @lru_cache(None)
        def fn(n):
            """Return all full binary trees of n nodes."""
            if n == 1: return [TreeNode()]
            ans = []
            for nn in range(1, n, 2): 
                for left in fn(nn):
                    for right in fn(n-1-nn): 
                        ans.append(TreeNode(left=left, right=right))
            return ans 
        
        return fn(N)


    """897. Increasing Order Search Tree (Easy)
	Given the root of a binary search tree, rearrange the tree in in-order so 
	that the leftmost node in the tree is now the root of the tree, and every 
	node has no left child and only one right child.

	Example 1:
	Input: root = [5,3,6,2,4,null,8,1,null,null,null,7,9]
	Output: [1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]

	Example 2:
	Input: root = [5,1,7]
	Output: [1,null,5,null,7]

	Constraints:
	* The number of nodes in the given tree will be in the range [1, 100].
	* 0 <= Node.val <= 1000"""

    def increasingBST(self, root: TreeNode) -> TreeNode:
        ans = temp = None
        stack = []
        node = root
        while stack or node: 
            if node: 
                stack.append(node)
                node = node.left
                continue
            node = stack.pop()
            if not ans: ans = temp = node 
            else: temp.right = temp = node
            node.left = None 
            node = node.right
        return ans 


    """898. Bitwise ORs of Subarrays (Medium)
	We have an array A of non-negative integers. For every (contiguous) 
	subarray B = [A[i], A[i+1], ..., A[j]] (with i <= j), we take the bitwise 
	OR of all the elements in B, obtaining a result A[i] | A[i+1] | ... | A[j]. 
	Return the number of possible results.  (Results that occur more than once 
	are only counted once in the final answer.)

	Example 1:
	Input: [0]
	Output: 1
	Explanation: There is only one possible result: 0.

	Example 2:
	Input: [1,1,2]
	Output: 3
	Explanation: The possible subarrays are [1], [1], [2], [1, 1], [1, 2], [1, 1, 2].
				 These yield the results 1, 1, 2, 1, 3, 3.
				 There are 3 unique values, so the answer is 3.
	
	Example 3:
	Input: [1,2,4]
	Output: 6
	Explanation: The possible results are 1, 2, 3, 4, 6, and 7.

	Note:
	* 1 <= A.length <= 50000
	* 0 <= A[i] <= 10^9"""

    def subarrayBitwiseORs(self, A: List[int]) -> int:
        ans, vals = set(), set()
        for x in A: 
            vals = {x | xx for xx in vals} | {x}
            ans |= vals
        return len(ans)

    
    """909. Snakes and Ladders (Medium)
	On an N x N board, the numbers from 1 to N*N are written boustrophedonically 
	starting from the bottom left of the board, and alternating direction each 
	row. You start on square 1 of the board (which is always in the last row and 
	first column).  Each move, starting from square x, consists of the following:
	* You choose a destination square S with number x+1, x+2, x+3, x+4, x+5, or 
	  x+6, provided this number is <= N*N.
	  + (This choice simulates the result of a standard 6-sided die roll: ie., 
	    there are always at most 6 destinations, regardless of the size of the 
	    board.)
	* If S has a snake or ladder, you move to the destination of that snake or 
	  ladder.  Otherwise, you move to S.
	A board square on row r and column c has a "snake or ladder" if 
	board[r][c] != -1.  The destination of that snake or ladder is board[r][c]. 
	Note that you only take a snake or ladder at most once per move: if the 
	destination to a snake or ladder is the start of another snake or ladder, 
	you do not continue moving.  (For example, if the board is `[[4,-1],[-1,3]]`, 
	and on the first move your destination square is `2`, then you finish your 
	first move at `3`, because you do not continue moving to `4`.) Return the 
	least number of moves required to reach square N*N.  If it is not possible, 
	return -1.

	Example 1:
	Input: [
	[-1,-1,-1,-1,-1,-1],
	[-1,-1,-1,-1,-1,-1],
	[-1,-1,-1,-1,-1,-1],
	[-1,35,-1,-1,13,-1],
	[-1,-1,-1,-1,-1,-1],
	[-1,15,-1,-1,-1,-1]]
	Output: 4
	Explanation: 
	At the beginning, you start at square 1 [at row 5, column 0].
	You decide to move to square 2, and must take the ladder to square 15.
	You then decide to move to square 17 (row 3, column 5), and must take the snake to square 13.
	You then decide to move to square 14, and must take the ladder to square 35.
	You then decide to move to square 36, ending the game.
	It can be shown that you need at least 4 moves to reach the N*N-th square, so the answer is 4.

	Note:
	* 2 <= board.length = board[0].length <= 20
	* board[i][j] is between 1 and N*N or is equal to -1.
	* The board square with number 1 has no snake or ladder.
	* The board square with number N*N has no snake or ladder."""

    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        ans = 0
        queue = [1]
        seen = {1}
        while queue: # bfs 
            newq = []
            for x in queue: 
                if x == n*n: return ans 
                for xx in range(x+1, x+7): 
                    if xx <= n*n:
                        i, j = divmod(xx-1, n)
                        if board[~i][~j if i&1 else j] != -1: xx = board[~i][~j if i&1 else j]
                        if xx not in seen: 
                            newq.append(xx)
                            seen.add(xx)
            ans += 1
            queue = newq 
        return -1 


    """910. Smallest Range II (Medium)
	Given an array A of integers, for each integer A[i] we need to choose 
	either x = -K or x = K, and add x to A[i] (only once). After this process, 
	we have some array B. Return the smallest possible difference between the 
	maximum value of B and the minimum value of B.

	Example 1:
	Input: A = [1], K = 0
	Output: 0
	Explanation: B = [1]

	Example 2:
	Input: A = [0,10], K = 2
	Output: 6
	Explanation: B = [2,8]

	Example 3:
	Input: A = [1,3,6], K = 3
	Output: 3
	Explanation: B = [4,6,3]

	Note:
	* 1 <= A.length <= 10000
	* 0 <= A[i] <= 10000
	* 0 <= K <= 10000"""

    def smallestRangeII(self, A: List[int], K: int) -> int:
        A.sort()
        ans = A[-1] - A[0]
        for i in range(1, len(A)): 
            mn = min(A[0] + K, A[i] - K) # move up A[:i]
            mx = max(A[i-1]+K, A[-1] - K) # move down A[i:]
            ans = min(ans, mx - mn)
        return ans 


    """912. Sort an Array (Medium)
	Given an array of integers nums, sort the array in ascending order.

	Example 1:
	Input: nums = [5,2,3,1]
	Output: [1,2,3,5]

	Example 2:
	Input: nums = [5,1,1,2,0,0]
	Output: [0,0,1,1,2,5]

	Constraints:
	* 1 <= nums.length <= 50000
	* -50000 <= nums[i] <= 50000"""

    def sortArray(self, nums: List[int]) -> List[int]:
        
        def part(lo, hi): 
            """Return a random partition of nums[lo:hi]."""
            mid = randint(lo, hi-1)
            nums[lo], nums[mid] = nums[mid], nums[lo]
            i, j = lo+1, hi-1
            while i <= j: 
                if nums[i] < nums[lo]: i += 1
                elif nums[j] > nums[lo]: j -= 1
                else: 
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
                    j -= 1
            nums[lo], nums[j] = nums[j], nums[lo]
            return j
                
            
        def sort(lo, hi): 
            """Sort subarray nums[lo:hi] in place."""
            if lo + 1 >= hi: return 
            mid = part(lo, hi)
            sort(lo, mid)
            sort(mid+1, hi)
            
        sort(0, len(nums))
        return nums


    """915. Partition Array into Disjoint Intervals (Medium)
	Given an array A, partition it into two (contiguous) subarrays left and 
	right so that:
	* Every element in left is less than or equal to every element in right.
	* left and right are non-empty.
	* left has the smallest possible size.
	Return the length of left after such a partitioning.  It is guaranteed that 
	such a partitioning exists.

	Example 1:
	Input: [5,0,3,8,6]
	Output: 3
	Explanation: left = [5,0,3], right = [8,6]

	Example 2:
	Input: [1,1,1,0,6,12]
	Output: 4
	Explanation: left = [1,1,1,0], right = [6,12]

	Note:
	* 2 <= A.length <= 30000
	* 0 <= A[i] <= 10^6
	* It is guaranteed there is at least one way to partition A as described."""

    def partitionDisjoint(self, A: List[int]) -> int:
        ans = 0
        mx, val = -inf, inf
        for i, x in enumerate(A, 1): 
            mx = max(mx, x)
            if x < val: 
                ans = i 
                val = mx 
        return ans


    """916. Word Subsets (Medium)
	We are given two arrays A and B of words. Each word is a string of 
	lowercase letters. Now, say that word b is a subset of word a if every 
	letter in b occurs in a, including multiplicity.  For example, "wrr" is a 
	subset of "warrior", but is not a subset of "world". Now say a word a from 
	A is universal if for every b in B, b is a subset of a. Return a list of 
	all universal words in A.  You can return the words in any order.

	Example 1:
	Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["e","o"]
	Output: ["facebook","google","leetcode"]

	Example 2:
	Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["l","e"]
	Output: ["apple","google","leetcode"]

	Example 3:
	Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["e","oo"]
	Output: ["facebook","google"]

	Example 4:
	Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["lo","eo"]
	Output: ["google","leetcode"]

	Example 5:
	Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["ec","oc","ceo"]
	Output: ["facebook","leetcode"]

	Note:
	* 1 <= A.length, B.length <= 10000
	* 1 <= A[i].length, B[i].length <= 10
	* A[i] and B[i] consist only of lowercase letters.
	* All words in A[i] are unique: there isn't i != j with A[i] == A[j]."""

    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        freq = Counter()
        for x in B: freq |= Counter(x)
        return [x for x in A if not freq - Counter(x)]


    """921. Minimum Add to Make Parentheses Valid (Medium)
	Given a string S of '(' and ')' parentheses, we add the minimum number of 
	parentheses ( '(' or ')', and in any positions ) so that the resulting 
	parentheses string is valid. Formally, a parentheses string is valid if and 
	only if:
	* It is the empty string, or
	* It can be written as AB (A concatenated with B), where A and B are valid 
	  strings, or
	* It can be written as (A), where A is a valid string.
	Given a parentheses string, return the minimum number of parentheses we 
	must add to make the resulting string valid.

	Example 1:
	Input: "())"
	Output: 1

	Example 2:
	Input: "((("
	Output: 3

	Example 3:
	Input: "()"
	Output: 0

	Example 4:
	Input: "()))(("
	Output: 4

	Note:
	* S.length <= 1000
	* S only consists of '(' and ')' characters."""

    def minAddToMakeValid(self, S: str) -> int:
        op = cl = 0 # open and closed parenthesis needed 
        for c in S: 
            cl += 1 if c == "(" else -1 # need ) to balance extra (
            if cl < 0: 
                cl = 0
                op += 1 # need ( to balance extra )
        return op + cl 


    """923. 3Sum With Multiplicity (Medium)
	Given an integer array A, and an integer target, return the number of 
	tuples i, j, k  such that i < j < k and A[i] + A[j] + A[k] == target. As 
	the answer can be very large, return it modulo 109 + 7.

	Example 1:
	Input: A = [1,1,2,2,3,3,4,4,5,5], target = 8
	Output: 20
	Explanation: 
	Enumerating by the values (A[i], A[j], A[k]):
	(1, 2, 5) occurs 8 times;
	(1, 3, 4) occurs 8 times;
	(2, 2, 4) occurs 2 times;
	(2, 3, 3) occurs 2 times.

	Example 2:
	Input: A = [1,1,2,2,2,2], target = 5
	Output: 12
	Explanation: 
	A[i] = 1, A[j] = A[k] = 2 occurs 12 times:
	We choose one 1 from [1,1] in 2 ways,
	and two 2s from [2,2,2,2] in 6 ways.

	Constraints:
	* 3 <= A.length <= 3000
	* 0 <= A[i] <= 100
	* 0 <= target <= 300"""

    def threeSumMulti(self, A: List[int], target: int) -> int:
        freq = {} # frequency table 
        for x in A: freq[x] = 1 + freq.get(x, 0) 
        
        A = list(freq)
        ans = 0
        for i in range(len(A)):
            for j in range(i, len(A)):
                x = target - A[i] - A[j]
                if x in freq: 
                    if A[i] == A[j] == x: 
                        ans += freq[x]*(freq[x]-1)*(freq[x]-2)//6
                    elif A[i] == A[j]: 
                        ans += freq[A[i]]*(freq[A[i]]-1)//2*freq[x]
                    elif A[i] < x and A[j] < x: 
                        ans += freq[A[i]] * freq[A[j]] * freq[x]
        return ans % 1_000_000_007


    """926. Flip String to Monotone Increasing (Medium)
	A string of '0's and '1's is monotone increasing if it consists of some 
	number of '0's (possibly 0), followed by some number of '1's (also possibly 
	0.) We are given a string S of '0's and '1's, and we may flip any '0' to a 
	'1' or a '1' to a '0'. Return the minimum number of flips to make S monotone 
	increasing.

	Example 1:
	Input: "00110"
	Output: 1
	Explanation: We flip the last digit to get 00111.

	Example 2:
	Input: "010110"
	Output: 2
	Explanation: We flip to get 011111, or alternatively 000111.

	Example 3:
	Input: "00011000"
	Output: 2
	Explanation: We flip to get 00000000.

	Note:
	* 1 <= S.length <= 20000
	* S only consists of '0' and '1' characters."""

    def minFlipsMonoIncr(self, S: str) -> int:
        ones = flip = 0
        for ch in S: 
            if ch == "1": ones += 1
            else: flip = min(ones, flip + 1)
        return flip 


    """930. Binary Subarrays With Sum (Medium)
	In an array A of 0s and 1s, how many non-empty subarrays have sum S?

	Example 1:
	Input: A = [1,0,1,0,1], S = 2
	Output: 4
	Explanation: 
	The 4 subarrays are bolded below:
	[1,0,1,0,1]
	[1,0,1,0,1]
	[1,0,1,0,1]
	[1,0,1,0,1]

	Note:
	* A.length <= 30000
	* 0 <= S <= A.length
	* A[i] is either 0 or 1."""

    def numSubarraysWithSum(self, A: List[int], S: int) -> int:
        ans = prefix = 0
        seen = {0: 1}
        for x in A:
            prefix += x
            ans += seen.get(prefix - S, 0)
            seen[prefix] = 1 + seen.get(prefix, 0)
        return ans 


    """931. Minimum Falling Path Sum (Medium)
	Given a square array of integers A, we want the minimum sum of a falling 
	path through A. A falling path starts at any element in the first row, and 
	chooses one element from each row.  The next row's choice must be in a 
	column that is different from the previous row's column by at most one.

	Example 1:
	Input: [[1,2,3],[4,5,6],[7,8,9]]
	Output: 12
	Explanation: 
	The possible falling paths are:
	[1,4,7], [1,4,8], [1,5,7], [1,5,8], [1,5,9]
	[2,4,7], [2,4,8], [2,5,7], [2,5,8], [2,5,9], [2,6,8], [2,6,9]
	[3,5,7], [3,5,8], [3,5,9], [3,6,8], [3,6,9]
	The falling path with the smallest sum is [1,4,7], so the answer is 12.

	Constraints:
	* 1 <= A.length == A[0].length <= 100
	* -100 <= A[i][j] <= 100"""

    def minFallingPathSum(self, A: List[List[int]]) -> int:
        n = len(A)
        
        @lru_cache(None)
        def fn(i, j): 
            """Return the minimum falling path ending at (i, j)."""
            if not (0 <= i < n and 0 <= j < n): return inf
            if i == 0: return A[i][j]
            return min(fn(i-1, j-1), fn(i-1, j), fn(i-1, j+1)) + A[i][j]
        
        return min(fn(n-1, j) for j in range(n))


    """934. Shortest Bridge (Medium)
	In a given 2D binary array A, there are two islands.  (An island is a 4-
	directionally connected group of 1s not connected to any other 1s.) Now, we 
	may change 0s to 1s so as to connect the two islands together to form 1 
	island. Return the smallest number of 0s that must be flipped.  (It is 
	guaranteed that the answer is at least 1.)

	Example 1:
	Input: A = [[0,1],[1,0]]
	Output: 1

	Example 2:
	Input: A = [[0,1,0],[0,0,0],[0,0,1]]
	Output: 2

	Example 3:
	Input: A = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
	Output: 1

	Constraints:
	* 2 <= A.length == A[0].length <= 100
	* A[i][j] == 0 or A[i][j] == 1"""

    def shortestBridge(self, A: List[List[int]]) -> int:
        m, n = len(A), len(A[0])
        i, j = next((i, j) for i in range(m) for j in range(n) if A[i][j])
        
        # dfs 
        stack = [(i, j)]
        seen = set(stack)
        while stack: 
            i, j = stack.pop()
            seen.add((i, j)) # mark as visited 
            for ii, jj in (i-1, j), (i, j-1), (i, j+1), (i+1, j): 
                if 0 <= ii < m and 0 <= jj < n and A[ii][jj] and (ii, jj) not in seen: 
                    stack.append((ii, jj))
                    seen.add((ii, jj))
        
        # bfs 
        ans = 0
        queue = list(seen)
        while queue:
            newq = []
            for i, j in queue: 
                for ii, jj in (i-1, j), (i, j-1), (i, j+1), (i+1, j): 
                    if 0 <= ii < m and 0 <= jj < n and (ii, jj) not in seen: 
                        if A[ii][jj] == 1: return ans 
                        newq.append((ii, jj))
                        seen.add((ii, jj))
            queue = newq
            ans += 1


    """935. Knight Dialer (Medium)
	The chess knight has a unique movement, it may move two squares vertically 
	and one square horizontally, or two squares horizontally and one square 
	vertically (with both forming the shape of an L). We have a chess knight 
	and a phone pad as shown below, the knight can only stand on a numeric cell 
	(i.e. blue cell). Given an integer n, return how many distinct phone numbers 
	of length n we can dial. You are allowed to place the knight on any numeric 
	cell initially and then you should perform n - 1 jumps to dial a number of 
	length n. All jumps should be valid knight jumps. As the answer may be very 
	large, return the answer modulo 109 + 7.

	Example 1:
	Input: n = 1
	Output: 10
	Explanation: We need to dial a number of length 1, so placing the knight 
	             over any numeric cell of the 10 cells is sufficient.

	Example 2:
	Input: n = 2
	Output: 20
	Explanation: All the valid number we can dial are [04, 06, 16, 18, 27, 29, 
	             34, 38, 40, 43, 49, 60, 61, 67, 72, 76, 81, 83, 92, 94]
	
	Example 3:
	Input: n = 3
	Output: 46

	Example 4:
	Input: n = 4
	Output: 104

	Example 5:
	Input: n = 3131
	Output: 136006598
	Explanation: Please take care of the mod.
	 
	Constraints: 1 <= n <= 5000"""

    def knightDialer(self, n: int) -> int:
        mp = {0: [4, 6], 1: [6, 8], 2: [7, 9], 3: [4, 8], 4: [0, 3, 9], 
              5: [], 6: [0, 1, 7], 7: [2, 6], 8: [1, 3], 9: [2, 4]}
        ans = [1]*10 
        for _ in range(n-1): 
            temp = [0]*10
            for i in range(10): 
                for ii in mp[i]: temp[i] += ans[ii]
                temp[i] %= 1_000_000_007
            ans = temp 
        return sum(ans) % 1_000_000_007


    """939. Minimum Area Rectangle (Medium)
	Given a set of points in the xy-plane, determine the minimum area of a 
	rectangle formed from these points, with sides parallel to the x and y axes.
	If there isn't any rectangle, return 0.

	Example 1:
	Input: [[1,1],[1,3],[3,1],[3,3],[2,2]]
	Output: 4

	Example 2:
	Input: [[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]]
	Output: 2

	Note:
	* 1 <= points.length <= 500
	* 0 <= points[i][0] <= 40000
	* 0 <= points[i][1] <= 40000
	* All points are distinct."""

    def minAreaRect(self, points: List[List[int]]) -> int:
        ans = inf
        seen = {(x, y) for x, y in points}
        for x, y in points: 
            for xx, yy in points: 
                if x != xx and y != yy and (x, yy) in seen and (xx, y) in seen: 
                    ans = min(ans, abs((xx-x)*(yy-y)))
        return ans if ans < inf else 0


    """945. Minimum Increment to Make Array Unique (Medium)
	Given an array of integers A, a move consists of choosing any A[i], and 
	incrementing it by 1. Return the least number of moves to make every value 
	in A unique.

	Example 1:
	Input: [1,2,2]
	Output: 1
	Explanation: After 1 move, the array could be [1, 2, 3].

	Example 2:
	Input: [3,2,1,2,1,7]
	Output: 6
	Explanation: After 6 moves, the array could be [3, 4, 1, 2, 5, 7]. It can 
	             be shown with 5 or less moves that it is impossible for the 
	             array to have all unique values.

	Note:
	* 0 <= A.length <= 40000
	* 0 <= A[i] < 40000"""

    def minIncrementForUnique(self, A: List[int]) -> int:
        ans = cap = 0
        for x in sorted(A): 
            ans += max(0, cap - x)
            cap = max(cap, x) + 1
        return ans 

    
    """946. Validate Stack Sequences (Medium)
	Given two sequences pushed and popped with distinct values, return true if 
	and only if this could have been the result of a sequence of push and pop 
	operations on an initially empty stack.

	Example 1:
	Input: pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
	Output: true
	Explanation: We might do the following sequence:
	push(1), push(2), push(3), push(4), pop() -> 4,
	push(5), pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1

	Example 2:
	Input: pushed = [1,2,3,4,5], popped = [4,3,5,1,2]
	Output: false
	Explanation: 1 cannot be popped before 2.

	Constraints:
	* 0 <= pushed.length == popped.length <= 1000
	* 0 <= pushed[i], popped[i] < 1000
	* pushed is a permutation of popped.
	* pushed and popped have distinct values."""

    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        i = 0
        stack = []
        for x in pushed: 
            stack.append(x)
            while stack and stack[-1] == popped[i]:
                stack.pop()
                i += 1
        return not stack 


    """948. Bag of Tokens (Medium)
	You have an initial power of P, an initial score of 0, and a bag of tokens 
	where tokens[i] is the value of the ith token (0-indexed). Your goal is to 
	maximize your total score by potentially playing each token in one of two 
	ways:
	* If your current power is at least tokens[i], you may play the ith token 
	  face up, losing tokens[i] power and gaining 1 score.
	* If your current score is at least 1, you may play the ith token face down, 
	  gaining tokens[i] power and losing 1 score.
	Each token may be played at most once and in any order. You do not have to 
	play all the tokens. Return the largest possible score you can achieve 
	after playing any number of tokens.

	Example 1:
	Input: tokens = [100], P = 50
	Output: 0
	Explanation: Playing the only token in the bag is impossible because you 
	             either have too little power or too little score.

	Example 2:
	Input: tokens = [100,200], P = 150
	Output: 1
	Explanation: Play the 0th token (100) face up, your power becomes 50 and 
	             score becomes 1. There is no need to play the 1st token since 
	             you cannot play it face up to add to your score.
	
	Example 3:
	Input: tokens = [100,200,300,400], P = 200
	Output: 2
	Explanation: Play the tokens in this order to get a score of 2:
	1. Play the 0th token (100) face up, your power becomes 100 and score becomes 1.
	2. Play the 3rd token (400) face down, your power becomes 500 and score becomes 0.
	3. Play the 1st token (200) face up, your power becomes 300 and score becomes 1.
	4. Play the 2nd token (300) face up, your power becomes 0 and score becomes 2.

	Constraints:
	* 0 <= tokens.length <= 1000
	* 0 <= tokens[i], P < 104"""

    def bagOfTokensScore(self, tokens: List[int], P: int) -> int:
        tokens.sort()
        score, lo, hi = 0, 0, len(tokens)-1
        while lo <= hi: 
            if tokens[lo] <= P: # exchange power for score
                P -= tokens[lo]
                lo += 1
                score += 1
            elif score and lo < hi: # exchange score for power 
                P += tokens[hi]
                hi -= 1
                score -= 1
            else: break 
        return score


    """949. Largest Time for Given Digits (Medium)
	Given an array arr of 4 digits, find the latest 24-hour time that can be 
	made using each digit exactly once. 24-hour times are formatted as "HH:MM", 
	where HH is between 00 and 23, and MM is between 00 and 59. The earliest 
	24-hour time is 00:00, and the latest is 23:59. Return the latest 24-hour 
	time in "HH:MM" format. If no valid time can be made, return an empty string.

	Example 1:
	Input: A = [1,2,3,4]
	Output: "23:41"
	Explanation: The valid 24-hour times are "12:34", "12:43", "13:24", "13:42", 
	             "14:23", "14:32", "21:34", "21:43", "23:14", and "23:41". Of 
	             these times, "23:41" is the latest.

	Example 2:
	Input: A = [5,5,5,5]
	Output: ""
	Explanation: There are no valid 24-hour times as "55:55" is not valid.
	
	Example 3:
	Input: A = [0,0,0,0]
	Output: "00:00"

	Example 4:
	Input: A = [0,0,1,0]
	Output: "10:00"

	Constraints:
	* arr.length == 4
	* 0 <= arr[i] <= 9"""

    def largestTimeFromDigits(self, arr: List[int]) -> str:
        hh = mm = -1
        for x in permutations(arr):
            h = 10*x[0] + x[1]
            m = 10*x[2] + x[3]
            if h < 24 and m < 60 and 60*hh + mm < 60*h + m: hh, mm = h, m
        return f"{hh:02}:{mm:02}" if hh > -1 else ""


    """950. Reveal Cards In Increasing Order (Medium)
	In a deck of cards, every card has a unique integer. You can order the deck
	in any order you want. Initially, all the cards start face down (unrevealed) 
	in one deck. Now, you do the following steps repeatedly, until all cards are 
	revealed:
	1) Take the top card of the deck, reveal it, and take it out of the deck.
	2) If there are still cards in the deck, put the next top card of the deck 
	   at the bottom of the deck.
	3) If there are still unrevealed cards, go back to step 1.  Otherwise, stop.
	Return an ordering of the deck that would reveal the cards in increasing order.
	The first entry in the answer is considered to be the top of the deck.

	Example 1:
	Input: [17,13,11,2,3,5,7]
	Output: [2,13,3,11,5,17,7]
	Explanation: 
	We get the deck in the order [17,13,11,2,3,5,7] (this order doesn't matter), 
	and reorder it. After reordering, the deck starts as [2,13,3,11,5,17,7], 
	where 2 is the top of the deck.
	We reveal  2, and move 13 to the bottom.  The deck is now [3,11,5,17,7,13].
	We reveal  3, and move 11 to the bottom.  The deck is now [5,17,7,13,11].
	We reveal  5, and move 17 to the bottom.  The deck is now [7,13,11,17].
	We reveal  7, and move 13 to the bottom.  The deck is now [11,17,13].
	We reveal 11, and move 17 to the bottom.  The deck is now [13,17].
	We reveal 13, and move 17 to the bottom.  The deck is now [17].
	We reveal 17.
	Since all the cards revealed are in increasing order, the answer is correct.

	Note:
	* 1 <= A.length <= 1000
	* 1 <= A[i] <= 10^6
	* A[i] != A[j] for all i != j"""

    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        ans = [0]*len(deck)
        idx = deque(range(len(deck)))
        for x in sorted(deck): 
            ans[idx.popleft()] = x
            if idx: idx.append(idx.popleft())
        return ans 


    """951. Flip Equivalent Binary Trees (Medium)
	For a binary tree T, we can define a flip operation as follows: choose any 
	node, and swap the left and right child subtrees. A binary tree X is flip 
	equivalent to a binary tree Y if and only if we can make X equal to Y after 
	some number of flip operations. Given the roots of two binary trees root1 
	and root2, return true if the two trees are flip equivelent or false 
	otherwise.

	Example 1:
	Flipped Trees Diagram
	Input: root1 = [1,2,3,4,5,6,null,null,null,7,8], 
	       root2 = [1,3,2,null,6,4,5,null,null,null,null,8,7]
	Output: true
	Explanation: We flipped at nodes with values 1, 3, and 5.

	Example 2:
	Input: root1 = [], root2 = []
	Output: true

	Example 3:
	Input: root1 = [], root2 = [1]
	Output: false

	Example 4:
	Input: root1 = [0,null,1], root2 = []
	Output: false

	Example 5:
	Input: root1 = [0,null,1], root2 = [0,1]
	Output: true

	Constraints:
	* The number of nodes in each tree is in the range [0, 100].
	* Each tree will have unique node values in the range [0, 99]."""

    def flipEquiv(self, root1: TreeNode, root2: TreeNode) -> bool:
        
        def fn(n1, n2):
            """Return True if n1 is a flip of n2."""
            if not n1 or not n2: return n1 is n2
            return n1.val == n2.val and (fn(n1.left, n2.right) and fn(n1.right, n2.left) or fn(n1.left, n2.left) and fn(n1.right, n2.right))
        
        return fn(root1, root2)


    """1014. Best Sightseeing Pair (Medium)
	Given an array A of positive integers, A[i] represents the value of the 
	i-th sightseeing spot, and two sightseeing spots i and j have distance 
	j - i between them. The score of a pair (i < j) of sightseeing spots is 
	(A[i] + A[j] + i - j) : the sum of the values of the sightseeing spots, 
	minus the distance between them. Return the maximum score of a pair of 
	sightseeing spots.

	Example 1:
	Input: [8,1,5,2,6]
	Output: 11
	Explanation: i = 0, j = 2, A[i] + A[j] + i - j = 8 + 5 + 0 - 2 = 11

	Note:
	* 2 <= A.length <= 50000
	* 1 <= A[i] <= 1000"""

    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        ans = mx = 0
        for i, x in enumerate(A): 
            ans = max(ans, x - i + mx)
            mx = max(mx, x + i)
        return ans 


    """1017. Convert to Base -2 (Medium)
	Given a number N, return a string consisting of "0"s and "1"s that 
	represents its value in base -2 (negative two). The returned string must 
	have no leading zeroes, unless the string is "0".

	Example 1:
	Input: 2
	Output: "110"
	Explantion: (-2) ^ 2 + (-2) ^ 1 = 2

	Example 2:
	Input: 3
	Output: "111"
	Explantion: (-2) ^ 2 + (-2) ^ 1 + (-2) ^ 0 = 3

	Example 3:
	Input: 4
	Output: "100"
	Explantion: (-2) ^ 2 = 4

	Note: 0 <= N <= 10^9"""

    def baseNeg2(self, N: int) -> str:
        ans = []
        while N: 
            ans.append(N & 1)
            N = -(N >> 1)
        return "".join(map(str, ans[::-1] or [0]))


    """1019. Next Greater Node In Linked List (Medium)
	We are given a linked list with head as the first node. Let's number the 
	nodes in the list: node_1, node_2, node_3, ... etc. Each node may have a 
	next larger value: for node_i, next_larger(node_i) is the node_j.val such 
	that j > i, node_j.val > node_i.val, and j is the smallest possible choice.  
	If such a j does not exist, the next larger value is 0. Return an array of 
	integers answer, where answer[i] = next_larger(node_{i+1}). Note that in 
	the example inputs (not outputs) below, arrays such as [2,1,5] represent 
	the serialization of a linked list with a head node value of 2, second node 
	value of 1, and third node value of 5.

	Example 1:
	Input: [2,1,5]
	Output: [5,5,0]

	Example 2:
	Input: [2,7,4,3,5]
	Output: [7,0,5,5,0]

	Example 3:
	Input: [1,7,5,1,9,2,5,1]
	Output: [7,9,9,9,0,5,0,0]

	Note:
	* 1 <= node.val <= 10^9 for each node in the linked list.
	* The given list has length in the range [0, 10000]."""

    def nextLargerNodes(self, head: ListNode) -> List[int]:
        ans, stack = [], []
        while head: 
            while stack and stack[-1][1] < head.val: ans[stack.pop()[0]] = head.val 
            stack.append((len(ans), head.val))
            ans.append(0)
            head = head.next 
        return ans 


    """1020. Number of Enclaves (Medium)
	Given a 2D array A, each cell is 0 (representing sea) or 1 (representing 
	land). A move consists of walking from one land square 4-directionally to 
	another land square, or off the boundary of the grid. Return the number of 
	land squares in the grid for which we cannot walk off the boundary of the 
	grid in any number of moves.

	Example 1:
	Input: [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
	Output: 3
	Explanation: There are three 1s that are enclosed by 0s, and one 1 that 
	             isn't enclosed because its on the boundary.

	Example 2:
	Input: [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
	Output: 0
	Explanation: All 1s are either on the boundary or can reach the boundary.

	Note:
	* 1 <= A.length <= 500
	* 1 <= A[i].length <= 500
	* 0 <= A[i][j] <= 1
	* All rows have the same size."""

    def numEnclaves(self, A: List[List[int]]) -> int:
        m, n = len(A), len(A[0])
        
        stack = []
        for i in range(m):
            if A[i][0]: stack.append((i, 0))
            if A[i][n-1]: stack.append((i, n-1))
        
        for j in range(n):
            if A[0][j]: stack.append((0, j))
            if A[m-1][j]: stack.append((m-1, j))
                
        while stack: 
            i, j = stack.pop()
            A[i][j] = 0 # mark as visited 
            for ii, jj in (i-1, j), (i, j-1), (i, j+1), (i+1, j): 
                if 0 <= ii < m and 0 <= jj < n and A[ii][jj]: stack.append((ii, jj))
        
        return sum(map(sum, A))


    """1023. Camelcase Matching (Medium)
	A query word matches a given pattern if we can insert lowercase letters to 
	the pattern word so that it equals the query. (We may insert each character 
	at any position, and may insert 0 characters.) Given a list of queries, and 
	a pattern, return an answer list of booleans, where answer[i] is true if 
	and only if queries[i] matches the pattern.

	Example 1:
	Input: queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], pattern = "FB"
	Output: [true,false,true,true,false]
	Explanation: "FooBar" can be generated like this "F" + "oo" + "B" + "ar".
 				 "FootBall" can be generated like this "F" + "oot" + "B" + "all".
  				 "FrameBuffer" can be generated like this "F" + "rame" + "B" + "uffer".

	Example 2:
	Input: queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], pattern = "FoBa"
	Output: [true,false,true,false,false]
	Explanation: "FooBar" can be generated like this "Fo" + "o" + "Ba" + "r".
	             "FootBall" can be generated like this "Fo" + "ot" + "Ba" + "ll".

	Example 3:
	Input: queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], pattern = "FoBaT"
	Output: [false,true,false,false,false]
	Explanation: "FooBarTest" can be generated like this "Fo" + "o" + "Ba" + "r" + "T" + "est".

	Note:
	* 1 <= queries.length <= 100
	* 1 <= queries[i].length <= 100
	* 1 <= pattern.length <= 100
	* All strings consists only of lower and upper case English letters."""

    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        
        def fn(query): 
            """Return true if query matches pattern."""
            i = 0
            for x in query:
                if i < len(pattern) and x == pattern[i]: i += 1
                elif x.isupper(): return False
            return i == len(pattern)
        
        return [fn(query) for query in queries]


    """1024. Video Stitching (Medium)
	You are given a series of video clips from a sporting event that lasted T 
	seconds. These video clips can be overlapping with each other and have 
	varied lengths. Each video clip clips[i] is an interval: it starts at time 
	clips[i][0] and ends at time clips[i][1].  We can cut these clips into 
	segments freely: for example, a clip [0, 7] can be cut into segments 
	[0, 1] + [1, 3] + [3, 7]. Return the minimum number of clips needed so that 
	we can cut the clips into segments that cover the entire sporting event 
	([0, T]).  If the task is impossible, return -1.

	Example 1:
	Input: clips = [[0,2],[4,6],[8,10],[1,9],[1,5],[5,9]], T = 10
	Output: 3
	Explanation: 
	We take the clips [0,2], [8,10], [1,9]; a total of 3 clips.
	Then, we can reconstruct the sporting event as follows:
	We cut [1,9] into segments [1,2] + [2,8] + [8,9].
	Now we have segments [0,2] + [2,8] + [8,10] which cover the sporting event [0, 10].

	Example 2:
	Input: clips = [[0,1],[1,2]], T = 5
	Output: -1
	Explanation: We can't cover [0,5] with only [0,1] and [1,2].

	Example 3:
	Input: clips = [[0,1],[6,8],[0,2],[5,6],[0,4],[0,3],[6,7],[1,3],[4,7],[1,4],[2,5],[2,6],[3,4],[4,5],[5,7],[6,9]], T = 9
	Output: 3
	Explanation: We can take clips [0,4], [4,7], and [6,9].

	Example 4:
	Input: clips = [[0,4],[2,8]], T = 5
	Output: 2
	Explanation: Notice you can have extra video after the event ends.

	Constraints:
	* 1 <= clips.length <= 100
	* 0 <= clips[i][0] <= clips[i][1] <= 100
	* 0 <= T <= 100"""

    def videoStitching(self, clips: List[List[int]], T: int) -> int:
        if not T: return 0 # edge case 
        
        ans = yy = mx = 0
        for x, y in sorted(clips):
            if mx < x: return -1 # gap 
            if yy < x <= mx: ans, yy = ans+1, mx
            mx = max(mx, y)
            if T <= mx: return ans + 1
        return -1 # not reaching T


    """1026. Maximum Difference Between Node and Ancestor (Medium)
	Given the root of a binary tree, find the maximum value V for which there 
	exist different nodes A and B where V = |A.val - B.val| and A is an 
	ancestor of B. A node A is an ancestor of B if either: any child of A is 
	equal to B, or any child of A is an ancestor of B.

	Example 1:
	Input: root = [8,3,10,1,6,null,14,null,null,4,7,13]
	Output: 7
	Explanation: We have various ancestor-node differences, some of which are given below :
	|8 - 3| = 5
	|3 - 7| = 4
	|8 - 1| = 7
	|10 - 13| = 3
	Among all possible differences, the maximum value of 7 is obtained by |8 - 1| = 7.

	Example 2:
	Input: root = [1,null,2,null,0,3]
	Output: 3

	Constraints:
	* The number of nodes in the tree is in the range [2, 5000].
	* 0 <= Node.val <= 105"""

    def maxAncestorDiff(self, root: TreeNode) -> int:
        
        def fn(node, mn, mx): 
            """Return maximum difference on sub-tree rooted at node."""
            if not node: return mx - mn 
            mn = min(mn, node.val)
            mx = max(mx, node.val)
            lv = fn(node.left, mn, mx)
            rv = fn(node.right, mn, mx)
            return max(lv, rv)
        
        return fn(root, root.val, root.val)


    """1027. Longest Arithmetic Subsequence (Medium)
	Given an array A of integers, return the length of the longest arithmetic 
	subsequence in A. Recall that a subsequence of A is a list A[i_1], A[i_2],
	..., A[i_k] with 0 <= i_1 < i_2 < ... < i_k <= A.length - 1, and that a 
	sequence B is arithmetic if B[i+1] - B[i] are all the same value (for 
	0 <= i < B.length - 1).

	Example 1:
	Input: A = [3,6,9,12]
	Output: 4
	Explanation: 
	The whole array is an arithmetic sequence with steps of length = 3.

	Example 2:
	Input: A = [9,4,7,2,10]
	Output: 3
	Explanation: 
	The longest arithmetic subsequence is [4,7,10].

	Example 3:
	Input: A = [20,1,15,3,10,5,8]
	Output: 4
	Explanation: 
	The longest arithmetic subsequence is [20,15,10,5].

	Constraints:
	* 2 <= A.length <= 1000
	* 0 <= A[i] <= 500"""

    def longestArithSeqLength(self, A: List[int]) -> int:
        ans = 0
        cnt = defaultdict(lambda: 1)
        seen = set()
        for x in A: 
            for xx in seen: 
                cnt[x, x-xx] = 1 + cnt[xx, x-xx]
                ans = max(ans, cnt[x, x-xx])
            seen.add(x)
        return ans 


    """1029. Two City Scheduling (Medium)
	A company is planning to interview 2n people. Given the array costs where 
	costs[i] = [aCosti, bCosti], the cost of flying the ith person to city a is 
	aCosti, and the cost of flying the ith person to city b is bCosti. Return 
	the minimum cost to fly every person to a city such that exactly n people 
	arrive in each city.

	Example 1:
	Input: costs = [[10,20],[30,200],[400,50],[30,20]]
	Output: 110
	Explanation: 
	The first person goes to city A for a cost of 10.
	The second person goes to city A for a cost of 30.
	The third person goes to city B for a cost of 50.
	The fourth person goes to city B for a cost of 20.
	The total minimum cost is 10 + 30 + 50 + 20 = 110 to have half the people interviewing in each city.

	Example 2:
	Input: costs = [[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]]
	Output: 1859

	Example 3:
	Input: costs = [[515,563],[451,713],[537,709],[343,819],[855,779],[457,60],[650,359],[631,42]]
	Output: 3086

	Constraints:
	* 2 * n == costs.length
	* 2 <= costs.length <= 100
	* costs.length is even.
	* 1 <= aCosti, bCosti <= 1000"""

    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda x: x[1] - x[0])
        ans = 0
        for i, (a, b) in enumerate(costs): 
            if i < len(costs)//2: ans += b
            else: ans += a
        return ans 


    """1031. Maximum Sum of Two Non-Overlapping Subarrays (Medium)
	Given an array A of non-negative integers, return the maximum sum of 
	elements in two non-overlapping (contiguous) subarrays, which have lengths 
	L and M.  (For clarification, the L-length subarray could occur before or 
	after the M-length subarray.) Formally, return the largest V for which 
	V = (A[i] + A[i+1] + ... + A[i+L-1]) + (A[j] + A[j+1] + ... + A[j+M-1]) and 
	either:
	* 0 <= i < i + L - 1 < j < j + M - 1 < A.length, or
	* 0 <= j < j + M - 1 < i < i + L - 1 < A.length.

	Example 1:
	Input: A = [0,6,5,2,2,5,1,9,4], L = 1, M = 2
	Output: 20
	Explanation: One choice of subarrays is [9] with length 1, and [6,5] with length 2.

	Example 2:
	Input: A = [3,8,1,3,2,1,8,9,0], L = 3, M = 2
	Output: 29
	Explanation: One choice of subarrays is [3,8,1] with length 3, and [8,9] with length 2.

	Example 3:
	Input: A = [2,1,5,6,0,9,5,0,3,8], L = 4, M = 3
	Output: 31
	Explanation: One choice of subarrays is [5,6,0,9] with length 4, and [3,8] with length 3.

	Note:
	* L >= 1
	* M >= 1
	* L + M <= A.length <= 1000
	* 0 <= A[i] <= 1000"""

    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        prefix = [0]
        for x in A: prefix.append(prefix[-1] + x) # prefix sum w/ leading 0
        ans = lmx = mmx = -inf 
        for i in range(M+L, len(A)+1): 
            lmx = max(lmx, prefix[i-M] - prefix[i-L-M])
            mmx = max(mmx, prefix[i-L] - prefix[i-L-M])
            ans = max(ans, lmx + prefix[i] - prefix[i-M], mmx + prefix[i] - prefix[i-L])
        return ans 


    """1034. Coloring A Border (Medium)
	Given a 2-dimensional grid of integers, each value in the grid represents 
	the color of the grid square at that location. Two squares belong to the 
	same connected component if and only if they have the same color and are 
	next to each other in any of the 4 directions. The border of a connected 
	component is all the squares in the connected component that are either 
	4-directionally adjacent to a square not in the component, or on the 
	boundary of the grid (the first or last row or column). Given a square at 
	location (r0, c0) in the grid and a color, color the border of the 
	connected component of that square with the given color, and return the 
	final grid.

	Example 1:
	Input: grid = [[1,1],[1,2]], r0 = 0, c0 = 0, color = 3
	Output: [[3, 3], [3, 2]]

	Example 2:
	Input: grid = [[1,2,2],[2,3,2]], r0 = 0, c0 = 1, color = 3
	Output: [[1, 3, 3], [2, 3, 3]]

	Example 3:
	Input: grid = [[1,1,1],[1,1,1],[1,1,1]], r0 = 1, c0 = 1, color = 2
	Output: [[2, 2, 2], [2, 1, 2], [2, 2, 2]]

	Note:
	* 1 <= grid.length <= 50
	* 1 <= grid[0].length <= 50
	* 1 <= grid[i][j] <= 1000
	* 0 <= r0 < grid.length
	* 0 <= c0 < grid[0].length
	* 1 <= color <= 1000"""

    def colorBorder(self, grid: List[List[int]], r0: int, c0: int, color: int) -> List[List[int]]:
        m, n, orig = len(grid), len(grid[0]), grid[r0][c0] # dimensions 
        seen = {(r0, c0)}
        stack = [(r0, c0)]
        while stack: 
            i, j = stack.pop()
            for ii, jj in (i-1, j), (i, j-1), (i, j+1), (i+1, j): 
                if (ii, jj) not in seen:
                    if 0 <= ii < m and 0 <= jj < n and grid[ii][jj] == orig: 
                        stack.append((ii, jj))
                        seen.add((ii, jj))
                    else: 
                        grid[i][j] = color 
        return grid 


    """1035. Uncrossed Lines (Medium)
	We write the integers of A and B (in the order they are given) on two 
	separate horizontal lines. Now, we may draw connecting lines: a straight 
	line connecting two numbers A[i] and B[j] such that:
	* A[i] == B[j];
	* The line we draw does not intersect any other connecting (non-horizontal) 
	  line.
	Note that a connecting lines cannot intersect even at the endpoints: each 
	number can only belong to one connecting line. Return the maximum number of 
	connecting lines we can draw in this way.

	Example 1:
	Input: A = [1,4,2], B = [1,2,4]
	Output: 2
	Explanation: We can draw 2 uncrossed lines as in the diagram. We cannot draw 
	             3 uncrossed lines, because the line from A[1]=4 to B[2]=4 will 
	             intersect the line from A[2]=2 to B[1]=2.

	Example 2:
	Input: A = [2,5,1,2,5], B = [10,5,2,1,5,2]
	Output: 3
	
	Example 3:
	Input: A = [1,3,7,1,7,5], B = [1,9,2,5,1]
	Output: 2

	Note:
	* 1 <= A.length <= 500
	* 1 <= B.length <= 500
	* 1 <= A[i], B[i] <= 2000"""

    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        
        @lru_cache(None)
        def fn(i, j): 
            """Return maximum uncrossed lines of A[i:] and B[j:]."""
            if i == len(A) or j == len(B): return 0
            if A[i] == B[j]: return 1 + fn(i+1, j+1)
            return max(fn(i+1, j), fn(i, j+1))
        
        return fn(0, 0)


    """1038. Binary Search Tree to Greater Sum Tree (Medium)
	Given the root of a Binary Search Tree (BST), convert it to a Greater Tree 
	such that every key of the original BST is changed to the original key plus 
	sum of all keys greater than the original key in BST. As a reminder, a 
	binary search tree is a tree that satisfies these constraints:
	* The left subtree of a node contains only nodes with keys less than the node's key.
	* The right subtree of a node contains only nodes with keys greater than the node's key.
	* Both the left and right subtrees must also be binary search trees.
	Note: This question is the same as 538: https://leetcode.com/problems/convert-bst-to-greater-tree/

	Example 1:
	Input: root = [4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]
	Output: [30,36,21,36,35,26,15,null,null,null,33,null,null,null,8]

	Example 2:
	Input: root = [0,null,1]
	Output: [1,null,1]

	Example 3:
	Input: root = [1,0,2]
	Output: [3,3,2]

	Example 4:
	Input: root = [3,2,4,1]
	Output: [7,9,4,10]

	Constraints:
	* The number of nodes in the tree is in the range [1, 100].
	* 0 <= Node.val <= 100
	* All the values in the tree are unique.
	* root is guaranteed to be a valid binary search tree."""

    def bstToGst(self, root: TreeNode) -> TreeNode:
        val = 0
        node = root
        stack = []
        while stack or node: 
            if node: 
                stack.append(node)
                node = node.right 
            else: 
                node = stack.pop()
                node.val = val = node.val + val 
                node = node.left 
        return root 


    """1041. Robot Bounded In Circle (Medium)
	On an infinite plane, a robot initially stands at (0, 0) and faces north.  
	The robot can receive one of three instructions:
	* "G": go straight 1 unit;
	* "L": turn 90 degrees to the left;
	* "R": turn 90 degress to the right.
	The robot performs the instructions given in order, and repeats them 
	forever. Return true if and only if there exists a circle in the plane such 
	that the robot never leaves the circle.

	Example 1:
	Input: "GGLLGG"
	Output: true
	Explanation: The robot moves from (0,0) to (0,2), turns 180 degrees, and 
	             then returns to (0,0). When repeating these instructions, the 
	             robot remains in the circle of radius 2 centered at the origin.

	Example 2:
	Input: "GG"
	Output: false
	Explanation: The robot moves north indefinitely.
	
	Example 3:
	Input: "GL"
	Output: true
	Explanation: The robot moves from (0, 0) -> (0, 1) -> (-1, 1) -> (-1, 0) -> (0, 0) -> ...

	Note:
	* 1 <= instructions.length <= 100
	* instructions[i] is in {'G', 'L', 'R'}"""

    def isRobotBounded(self, instructions: str) -> bool:
        x = y = 0
        dx, dy = 0, 1
        for instruction in instructions: 
            if instruction == "G": x, y = x+dx, y+dy
            elif instruction == "L": dx, dy = -dy, dx
            else: dx, dy = dy, -dx
        return (x, y) == (0, 0) or (dx, dy) != (0, 1)


    """1042. Flower Planting With No Adjacent (Medium)
	You have n gardens, labeled from 1 to n, and an array paths where 
	paths[i] = [xi, yi] describes a bidirectional path between garden xi to 
	garden yi. In each garden, you want to plant one of 4 types of flowers. All 
	gardens have at most 3 paths coming into or leaving it. Your task is to 
	choose a flower type for each garden such that, for any two gardens 
	connected by a path, they have different types of flowers. Return any such 
	a choice as an array answer, where answer[i] is the type of flower planted 
	in the (i+1)th garden. The flower types are denoted 1, 2, 3, or 4. It is 
	guaranteed an answer exists.

	Example 1:
	Input: n = 3, paths = [[1,2],[2,3],[3,1]]
	Output: [1,2,3]
	Explanation:
	Gardens 1 and 2 have different types.
	Gardens 2 and 3 have different types.
	Gardens 3 and 1 have different types.
	Hence, [1,2,3] is a valid answer. Other valid answers include [1,2,4], [1,4,2], and [3,2,1].

	Example 2:
	Input: n = 4, paths = [[1,2],[3,4]]
	Output: [1,2,1,2]

	Example 3:
	Input: n = 4, paths = [[1,2],[2,3],[3,4],[4,1],[1,3],[2,4]]
	Output: [1,2,3,4]

	Constraints:
	* 1 <= n <= 104
	* 0 <= paths.length <= 2 * 104
	* paths[i].length == 2
	* 1 <= xi, yi <= n
	* xi != yi
	* Every garden has at most 3 paths coming into or leaving it."""

    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        graph = {} # graph as adjacency list 
        for u, v in paths: 
            graph.setdefault(u-1, []).append(v-1)
            graph.setdefault(v-1, []).append(u-1)
            
        ans = [0]*n
        for i in range(n): 
            ans[i] = ({1,2,3,4} - {ans[ii] for ii in graph.get(i, [])}).pop()
        return ans 


    """1043. Partition Array for Maximum Sum (Medium)
	Given an integer array arr, you should partition the array into (contiguous) 
	subarrays of length at most k. After partitioning, each subarray has their 
	values changed to become the maximum value of that subarray. Return the 
	largest sum of the given array after partitioning.

	Example 1:
	Input: arr = [1,15,7,9,2,5,10], k = 3
	Output: 84
	Explanation: arr becomes [15,15,15,9,10,10,10]

	Example 2:
	Input: arr = [1,4,1,5,7,3,6,1,9,9,3], k = 4
	Output: 83

	Example 3:
	Input: arr = [1], k = 1
	Output: 1

	Constraints:
	* 1 <= arr.length <= 500
	* 0 <= arr[i] <= 109
	* 1 <= k <= arr.length"""

    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        
        @lru_cache(None)
        def fn(i):
            """Return maximum sum of arr[:i]."""
            if i == 0: return 0 # boundary condition 
            ans = 0
            for kk in range(1, min(i, k)+1): 
                ans = max(ans, fn(i-kk) + max(arr[ii] for ii in range(i-kk, i)) * kk)
            return ans 
        
        return fn(len(arr))


    """1048. Longest String Chain (Medium)
	Given a list of words, each word consists of English lowercase letters. 
	Let's say word1 is a predecessor of word2 if and only if we can add exactly 
	one letter anywhere in word1 to make it equal to word2.  For example, "abc" 
	is a predecessor of "abac". A word chain is a sequence of words 
	[word_1, word_2, ..., word_k] with k >= 1, where word_1 is a predecessor of 
	word_2, word_2 is a predecessor of word_3, and so on. Return the longest 
	possible length of a word chain with words chosen from the given list of 
	words.

	Example 1:
	Input: words = ["a","b","ba","bca","bda","bdca"]
	Output: 4
	Explanation: One of the longest word chain is "a","ba","bda","bdca".

	Example 2:
	Input: words = ["xbc","pcxbcf","xb","cxbc","pcxbc"]
	Output: 5

	Constraints:
	* 1 <= words.length <= 1000
	* 1 <= words[i].length <= 16
	* words[i] only consists of English lowercase letters."""

    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=len)
        lsc = dict(zip(words, [1]*len(words)))
        for i, word in enumerate(words): 
            for ii in range(len(word)): 
                key = word[:ii] + word[ii+1:]
                if key in lsc: lsc[word] = max(lsc[word], 1 + lsc[key])
        return max(lsc.values())


    """1052. Grumpy Bookstore Owner (Medium)
	Today, the bookstore owner has a store open for customers.length minutes. 
	Every minute, some number of customers (customers[i]) enter the store, and 
	all those customers leave after the end of that minute. On some minutes, 
	the bookstore owner is grumpy.  If the bookstore owner is grumpy on the 
	i-th minute, grumpy[i] = 1, otherwise grumpy[i] = 0.  When the bookstore 
	owner is grumpy, the customers of that minute are not satisfied, otherwise 
	they are satisfied. The bookstore owner knows a secret technique to keep 
	themselves not grumpy for X minutes straight, but can only use it once. 
	Return the maximum number of customers that can be satisfied throughout the 
	day.

	Example 1:
	Input: customers = [1,0,1,2,1,1,7,5], grumpy = [0,1,0,1,0,1,0,1], X = 3
	Output: 16
	Explanation: The bookstore owner keeps themselves not grumpy for the last 3 minutes. 
	The maximum number of customers that can be satisfied = 1 + 1 + 1 + 1 + 7 + 5 = 16.

	Note:
	* 1 <= X <= customers.length == grumpy.length <= 20000
	* 0 <= customers[i] <= 1000
	* 0 <= grumpy[i] <= 1"""

    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        ans = val = ii = mx = 0
        for i in range(len(customers)): 
            if not grumpy[i]: ans += customers[i]
            else: 
                val += customers[i]
                while ii <= i-X: 
                    if grumpy[ii]: val -= customers[ii]
                    ii += 1
                mx = max(mx, val)
        return ans + mx 


    """1054. Distant Barcodes (Medium)
	In a warehouse, there is a row of barcodes, where the ith barcode is 
	barcodes[i]. Rearrange the barcodes so that no two adjacent barcodes are 
	equal. You may return any answer, and it is guaranteed an answer exists.

	Example 1:
	Input: barcodes = [1,1,1,2,2,2]
	Output: [2,1,2,1,2,1]

	Example 2:
	Input: barcodes = [1,1,1,1,2,2,3,3]
	Output: [1,3,1,3,1,2,1,2]

	Constraints:
	* 1 <= barcodes.length <= 10000
	* 1 <= barcodes[i] <= 10000"""

    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        freq = {}
        for x in barcodes: freq[x] = 1 + freq.get(x, 0)
            
        ans, i = [None] * len(barcodes), 0
        for k, v in sorted(freq.items(), key=lambda x: x[1], reverse=True): 
            for _ in range(v): 
                ans[i] = k 
                i = i+2 if i+2 < len(ans) else 1
        return ans 


    """1056. Confusing Number (Easy)
	Given a number N, return true if and only if it is a confusing number, 
	which satisfies the following condition:
	We can rotate digits by 180 degrees to form new digits. When 0, 1, 6, 8, 9 
	are rotated 180 degrees, they become 0, 1, 9, 8, 6 respectively. When 2, 3, 
	4, 5 and 7 are rotated 180 degrees, they become invalid. A confusing number 
	is a number that when rotated 180 degrees becomes a different number with 
	each digit valid.

	Example 1:
	Input: 6
	Output: true
	Explanation: We get 9 after rotating 6, 9 is a valid number and 9!=6.
	
	Example 2:
	Input: 89
	Output: true
	Explanation: We get 68 after rotating 89, 86 is a valid number and 86!=89.
	
	Example 3:
	Input: 11
	Output: false
	Explanation: We get 11 after rotating 11, 11 is a valid number but the 
	             value remains the same, thus 11 is not a confusing number.
	
	Example 4:
	Input: 25
	Output: false
	Explanation: We get an invalid number after rotating 25.

	Note:
	* 0 <= N <= 10^9
	* After the rotation we can ignore leading zeros, for example if after 
	  rotation we have 0008 then this number is considered as just 8."""

    def confusingNumber(self, N: int) -> bool:
        mp = {0:0, 1:1, 6:9, 8:8, 9:6}
        n, nn = N, 0
        while n: 
            n, r = divmod(n, 10)
            if r not in mp: return False
            nn = 10*nn + mp[r]
        return nn != N


    """1064. Fixed Point (Easy)
	Given an array of distinct integers arr, where arr is sorted in ascending 
	order, return the smallest index i that satisfies arr[i] == i. If there is 
	no such index, return -1.

	Example 1:
	Input: arr = [-10,-5,0,3,7]
	Output: 3
	Explanation: For the given array, arr[0] = -10, arr[1] = -5, arr[2] = 0, 
	             arr[3] = 3, thus the output is 3.

	Example 2:
	Input: arr = [0,2,5,8,17]
	Output: 0
	Explanation: arr[0] = 0, thus the output is 0.

	Example 3:
	Input: arr = [-10,-5,3,4,7,9]
	Output: -1
	Explanation: There is no such i that arr[i] == i, thus the output is -1.

	Constraints:
	* 1 <= arr.length < 104
	* -109 <= arr[i] <= 109

	Follow up: The O(n) solution is very straightforward. Can we do better?"""

    def fixedPoint(self, arr: List[int]) -> int:
        lo, hi = 0, len(arr)-1
        while lo < hi: 
            mid = lo + hi >> 1
            if arr[mid] - mid < 0: lo = mid + 1
            else: hi = mid
        return lo if arr[lo] == lo else -1


    """1065. Index Pairs of a String (Easy)
	Given a text string and words (a list of strings), return all index pairs 
	[i, j] so that the substring text[i]...text[j] is in the list of words.

	Example 1:
	Input: text = "thestoryofleetcodeandme", words = ["story","fleet","leetcode"]
	Output: [[3,7],[9,13],[10,17]]

	Example 2:
	Input: text = "ababa", words = ["aba","ab"]
	Output: [[0,1],[0,2],[2,3],[2,4]]
	Explanation: Notice that matches can overlap, see "aba" is found in [0,2] 
	             and [2,4].

	Note:
	* All strings contains only lowercase English letters.
	* It's guaranteed that all strings in words are different.
	* 1 <= text.length <= 100
	* 1 <= words.length <= 20
	* 1 <= words[i].length <= 50
	* Return the pairs [i,j] in sorted order (i.e. sort them by their first 
	  coordinate in case of ties sort them by their second coordinate)."""

    def indexPairs(self, text: str, words: List[str]) -> List[List[int]]:
        ans = []
        for word in words: 
            k = -1
            while True: 
                k = text.find(word, k+1)
                if k == -1: break 
                ans.append([k, k+len(word)-1])
        return sorted(ans)



    """1072. Flip Columns For Maximum Number of Equal Rows (Medium)
	Given a matrix consisting of 0s and 1s, we may choose any number of columns 
	in the matrix and flip every cell in that column.  Flipping a cell changes 
	the value of that cell from 0 to 1 or from 1 to 0. Return the maximum 
	number of rows that have all values equal after some number of flips.

	Example 1:
	Input: [[0,1],[1,1]]
	Output: 1
	Explanation: After flipping no values, 1 row has all values equal.

	Example 2:
	Input: [[0,1],[1,0]]
	Output: 2
	Explanation: After flipping values in the first column, both rows have 
	             equal values.

	Example 3:
	Input: [[0,0,0],[0,0,1],[1,1,0]]
	Output: 2
	Explanation: After flipping values in the first two columns, the last two 
	             rows have equal values.

	Note:
	* 1 <= matrix.length <= 300
	* 1 <= matrix[i].length <= 300
	* All matrix[i].length's are equal
	* matrix[i][j] is 0 or 1"""

    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0]) # dimensions 
        score = [0]*m
        
        for j in range(1, n): 
            for i in range(m):
                score[i] *= 2
                if matrix[i][0] != matrix[i][j]: score[i] += 1
                    
        freq = {}
        for x in score: freq[x] = 1 + freq.get(x, 0)
        return max(freq.values())


    """1073. Adding Two Negabinary Numbers (Medium)
	Given two numbers arr1 and arr2 in base -2, return the result of adding 
	them together. Each number is given in array format:  as an array of 0s and 
	1s, from most significant bit to least significant bit.  For example, 
	arr = [1,1,0,1] represents the number (-2)^3 + (-2)^2 + (-2)^0 = -3.  A 
	number arr in array, format is also guaranteed to have no leading zeros: 
	either arr == [0] or arr[0] == 1. Return the result of adding arr1 and arr2
	in the same format: as an array of 0s and 1s with no leading zeros.

	Example 1:
	Input: arr1 = [1,1,1,1,1], arr2 = [1,0,1]
	Output: [1,0,0,0,0]
	Explanation: arr1 represents 11, arr2 represents 5, the output represents 16.

	Example 2:
	Input: arr1 = [0], arr2 = [0]
	Output: [0]

	Example 3:
	Input: arr1 = [0], arr2 = [1]
	Output: [1]

	Constraints:
	* 1 <= arr1.length, arr2.length <= 1000
	* arr1[i] and arr2[i] are 0 or 1
	* arr1 and arr2 have no leading zeros"""

    def addNegabinary(self, arr1: List[int], arr2: List[int]) -> List[int]:
        ans = []
        carry, i1, i2 = 0, len(arr1), len(arr2)
        while i1 or i2 or carry: 
            if i1: carry += arr1[(i1 := i1 - 1)]
            if i2: carry += arr2[(i2 := i2 - 1)]
            ans.append(carry & 1)
            carry = -(carry >> 1)
        while ans and not ans[-1]: ans.pop()
        return ans[::-1] or [0]


    """1080. Insufficient Nodes in Root to Leaf Paths (Medium)
	Given the root of a binary tree, consider all root to leaf paths: paths 
	from the root to any leaf.  (A leaf is a node with no children.) A node is 
	insufficient if every such root to leaf path intersecting this node has sum 
	strictly less than limit. Delete all insufficient nodes simultaneously, and 
	return the root of the resulting binary tree.

	Example 1:
	Input: root = [1,2,3,4,-99,-99,7,8,9,-99,-99,12,13,-99,14], limit = 1
	Output: [1,2,3,4,null,null,7,8,9,null,14]

	Example 2:
	Input: root = [5,4,8,11,null,17,4,7,1,null,null,5,3], limit = 22
	Output: [5,4,8,11,null,17,4,7,null,null,null,5]

	Example 3:
	Input: root = [1,2,-3,-5,null,4,null], limit = -1
	Output: [1,null,-3,4]

	Note:
	* The given tree will have between 1 and 5000 nodes.
	* -10^5 <= node.val <= 10^5
	* -10^9 <= limit <= 10^9"""

    def sufficientSubset(self, root: TreeNode, limit: int) -> TreeNode:
        
        def fn(node, x): 
            """Return updated node."""
            if not node: return 
            x -= node.val
            if node.left is node.right: return None if x > 0 else node # leaf 
            node.left = fn(node.left, x)
            node.right = fn(node.right, x)
            return node if node.left or node.right else None
        
        return fn(root, limit)


    """1081. Smallest Subsequence of Distinct Characters (Medium)
	Return the lexicographically smallest subsequence of s that contains all 
	the distinct characters of s exactly once. Note: This question is the same 
	as 316: https://leetcode.com/problems/remove-duplicate-letters/

	Example 1:
	Input: s = "bcabc"
	Output: "abc"

	Example 2:
	Input: s = "cbacdcbc"
	Output: "acdb"

	Constraints:
	* 1 <= s.length <= 1000
	* s consists of lowercase English letters."""

    def smallestSubsequence(self, s: str) -> str:
        loc = {x: i for i, x in enumerate(s)}
        stack = []
        for i, x in enumerate(s): 
            if x not in stack: 
                while stack and x < stack[-1] and i < loc[stack[-1]]: stack.pop()
                stack.append(x)
        return "".join(stack)


    """1085. Sum of Digits in the Minimum Number (Easy)
	Given an array A of positive integers, let S be the sum of the digits of 
	the minimal element of A. Return 0 if S is odd, otherwise return 1.

	Example 1:
	Input: [34,23,1,24,75,33,54,8]
	Output: 0
	Explanation: The minimal element is 1, and the sum of those digits is S = 1 
	             which is odd, so the answer is 0.
	
	Example 2:
	Input: [99,77,33,66,55]
	Output: 1
	Explanation: The minimal element is 33, and the sum of those digits is 
	             S = 3 + 3 = 6 which is even, so the answer is 1.

	Constraints:
	* 1 <= A.length <= 100
	* 1 <= A[i] <= 100"""

    def sumOfDigits(self, A: List[int]) -> int:
        return 1 ^ 1&sum(int(x) for x in str(min(A)))


    """1086. High Five (Easy)
	Given a list of the scores of different students, items, where 
	items[i] = [IDi, scorei] represents one score from a student with IDi, 
	calculate each student's top five average. Return the answer as an array of 
	pairs result, where result[j] = [IDj, topFiveAveragej] represents the 
	student with IDj and their top five average. Sort result by IDj in 
	increasing order. A student's top five average is calculated by taking the 
	sum of their top five scores and dividing it by 5 using integer division.

	Example 1:
	Input: items = [[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]
	Output: [[1,87],[2,88]]
	Explanation: 
	The student with ID = 1 got scores 91, 92, 60, 65, 87, and 100. Their top five average is (100 + 92 + 91 + 87 + 65) / 5 = 87.
	The student with ID = 2 got scores 93, 97, 77, 100, and 76. Their top five average is (100 + 97 + 93 + 77 + 76) / 5 = 88.6, but with integer division their average converts to 88.

	Example 2:
	Input: items = [[1,100],[7,100],[1,100],[7,100],[1,100],[7,100],[1,100],[7,100],[1,100],[7,100]]
	Output: [[1,100],[7,100]]

	Constraints:
	* 1 <= items.length <= 1000
	* items[i].length == 2
	* 1 <= IDi <= 1000
	* 0 <= scorei <= 100
	* For each IDi, there will be at least five scores."""

    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        mp = {}
        for x, score in items: 
            mp.setdefault(x, []).append(score)
        
        ans = []
        for x in mp: 
            ans.append([x, sum(sorted(mp[x])[-5:])//5])
        return sorted(ans)


    """1090. Largest Values From Labels (Medium)
	We have a set of items: the i-th item has value values[i] and label labels[i]. 
	Then, we choose a subset S of these items, such that:
	* |S| <= num_wanted
	* For every label L, the number of items in S with label L is <= use_limit.
	Return the largest possible sum of the subset S.

	Example 1:
	Input: values = [5,4,3,2,1], labels = [1,1,2,2,3], num_wanted = 3, use_limit = 1
	Output: 9
	Explanation: The subset chosen is the first, third, and fifth item.

	Example 2:
	Input: values = [5,4,3,2,1], labels = [1,3,3,3,2], num_wanted = 3, use_limit = 2
	Output: 12
	Explanation: The subset chosen is the first, second, and third item.

	Example 3:
	Input: values = [9,8,8,7,6], labels = [0,0,0,1,1], num_wanted = 3, use_limit = 1
	Output: 16
	Explanation: The subset chosen is the first and fourth item.

	Example 4:
	Input: values = [9,8,8,7,6], labels = [0,0,0,1,1], num_wanted = 3, use_limit = 2
	Output: 24
	Explanation: The subset chosen is the first, second, and fourth item.

	Note:
	* 1 <= values.length == labels.length <= 20000
	* 0 <= values[i], labels[i] <= 20000
	* 1 <= num_wanted, use_limit <= values.length"""

    def largestValsFromLabels(self, values: List[int], labels: List[int], num_wanted: int, use_limit: int) -> int:
        ans = 0
        freq = {}
        for value, label in sorted(zip(values, labels), reverse=True):
            if freq.get(label, 0) < use_limit: 
                ans += value
                num_wanted -= 1
                if not num_wanted: break 
                freq[label] = 1 + freq.get(label, 0)
        return ans 


    """1091. Shortest Path in Binary Matrix (Medium)
	In an N by N square grid, each cell is either empty (0) or blocked (1). A 
	clear path from top-left to bottom-right has length k if and only if it is 
	composed of cells C_1, C_2, ..., C_k such that:
	* Adjacent cells C_i and C_{i+1} are connected 8-directionally (ie., they 
	  are different and share an edge or corner)
	* C_1 is at location (0, 0) (ie. has value grid[0][0])
	* C_k is at location (N-1, N-1) (ie. has value grid[N-1][N-1])
	* If C_i is located at (r, c), then grid[r][c] is empty (ie. grid[r][c] == 0).
	Return the length of the shortest such clear path from top-left to bottom-
	right.  If such a path does not exist, return -1.

	Example 1:
	Input: [[0,1],[1,0]]
	Output: 2

	Example 2:
	Input: [[0,0,0],[1,1,0],[1,1,0]]
	Output: 4

	Note:
	* 1 <= grid.length == grid[0].length <= 100
	* grid[r][c] is 0 or 1"""

    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if not grid[0][0]: 
            ans = 1
            queue = [(0, 0)]
            grid[0][0] = 1 # mark as visited 
            while queue: 
                newq = []
                for i, j in queue:
                    if i == j == n-1: return ans 
                    for ii, jj in product(range(i-1, i+2), range(j-1, j+2)): 
                        if 0 <= ii < n and 0 <= jj < n and not grid[ii][jj]: 
                            newq.append((ii, jj))
                            grid[ii][jj] = 1
                queue = newq
                ans += 1
        return -1 


    """1099. Two Sum Less Than K (Easy)
	Given an array nums of integers and integer k, return the maximum sum such 
	that there exists i < j with nums[i] + nums[j] = sum and sum < k. If no i, 
	j exist satisfying this equation, return -1.

	Example 1:
	Input: nums = [34,23,1,24,75,33,54,8], k = 60
	Output: 58
	Explanation: We can use 34 and 24 to sum 58 which is less than 60.

	Example 2:
	Input: nums = [10,20,30], k = 15
	Output: -1
	Explanation: In this case it is not possible to get a pair sum less that 15.

	Constraints:
	* 1 <= nums.length <= 100
	* 1 <= nums[i] <= 1000
	* 1 <= k <= 2000"""

    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans = -1
        lo, hi = 0, len(nums)-1
        while lo < hi: 
            val = nums[lo] + nums[hi]
            if val >= k: hi -= 1
            else: 
                ans = max(ans, val)
                lo += 1
        return ans


    """1118. Number of Days in a Month (Easy)
	Given a year Y and a month M, return how many days there are in that month.

	Example 1:
	Input: Y = 1992, M = 7
	Output: 31

	Example 2:
	Input: Y = 2000, M = 2
	Output: 29

	Example 3:
	Input: Y = 1900, M = 2
	Output: 28

	Note:
	* 1583 <= Y <= 2100
	* 1 <= M <= 12"""

    def numberOfDays(self, Y: int, M: int) -> int:
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        return days[M-1] + (M == 2 and (Y%4 == 0 and Y%100 != 0 or Y%400 == 0))


    """1119. Remove Vowels from a String (Easy)
	Given a string s, remove the vowels 'a', 'e', 'i', 'o', and 'u' from it, 
	and return the new string.

	Example 1:
	Input: s = "leetcodeisacommunityforcoders"
	Output: "ltcdscmmntyfrcdrs"

	Example 2:
	Input: s = "aeiou"
	Output: ""

	Constraints:
	* 1 <= s.length <= 1000
	* s consists of only lowercase English letters."""

    def removeVowels(self, S: str) -> str:
        return "".join(c for c in S if c not in "aeiou")


    """1120. Maximum Average Subtree (Medium)
	Given the root of a binary tree, find the maximum average value of any 
	subtree of that tree. (A subtree of a tree is any node of that tree plus 
	all its descendants. The average value of a tree is the sum of its values, 
	divided by the number of nodes.)

	Example 1:
	Input: [5,6,1]
	Output: 6.00000
	Explanation: 
	For the node with value = 5 we have an average of (5 + 6 + 1) / 3 = 4.
	For the node with value = 6 we have an average of 6 / 1 = 6.
	For the node with value = 1 we have an average of 1 / 1 = 1.
	So the answer is 6 which is the maximum.

	Note:
	* The number of nodes in the tree is between 1 and 5000.
	* Each node will have a value between 0 and 100000.
	* Answers will be accepted as correct if they are within 10^-5 of the 
	  correct answer."""

    def maximumAverageSubtree(self, root: TreeNode) -> float:
        
        def fn(node): 
            """Return sum, count and max average of subtree rooted at node."""
            if not node: return 0, 0, 0
            ls, ln, lv = fn(node.left)
            rs, rn, rv = fn(node.right)
            s = ls + node.val + rs
            n = ln + 1 + rn 
            return s, n, max(s/n, lv, rv)
            
        return fn(root)[2]


    """1133. Largest Unique Number (Easy)
	Given an array of integers A, return the largest integer that only occurs 
	once. If no integer occurs once, return -1.

	Example 1:
	Input: [5,7,3,9,4,9,8,3,1]
	Output: 8
	Explanation: The maximum integer in the array is 9 but it is repeated. The 
	             number 8 occurs only once, so it's the answer.
	
	Example 2:
	Input: [9,9,8,8]
	Output: -1
	Explanation: There is no number that occurs only once.

	Note:
	* 1 <= A.length <= 2000
	* 0 <= A[i] <= 1000"""

    def largestUniqueNumber(self, A: List[int]) -> int:
        freq = {}
        for x in A: freq[x] = 1 + freq.get(x, 0)
        return max((x for x, v in freq.items() if v == 1), default=-1)


    """1134. Armstrong Number (Easy)
	The k-digit number N is an Armstrong number if and only if the k-th power 
	of each digit sums to N. Given a positive integer N, return true if and 
	only if it is an Armstrong number.

	Example 1:
	Input: 153
	Output: true
	Explanation: 153 is a 3-digit number, and 153 = 1^3 + 5^3 + 3^3.
	
	Example 2:
	Input: 123
	Output: false
	Explanation: 123 is a 3-digit number, and 123 != 1^3 + 2^3 + 3^3 = 36.

	Note: 1 <= N <= 10^8"""

    def isArmstrong(self, N: int) -> bool:
        s = str(N)
        return sum(int(x)**len(s) for x in s) == N


    """1150. Check If a Number Is Majority Element in a Sorted Array (Easy)
	Given an array nums sorted in non-decreasing order, and a number target, 
	return True if and only if target is a majority element. A majority element 
	is an element that appears more than N/2 times in an array of length N.

	Example 1:
	Input: nums = [2,4,5,5,5,5,5,6,6], target = 5
	Output: true
	Explanation: The value 5 appears 5 times and the length of the array is 9. 
	             Thus, 5 is a majority element because 5 > 9/2 is true.
	
	Example 2:
	Input: nums = [10,100,101,101], target = 101
	Output: false
	Explanation: The value 101 appears 2 times and the length of the array is 4. 
	             Thus, 101 is not a majority element because 2 > 4/2 is false.

	Constraints:
	* 1 <= nums.length <= 1000
	* 1 <= nums[i] <= 10^9
	* 1 <= target <= 10^9"""

    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        if nums[(len(nums)-1)//2] != target: return False
        k = bisect_left(nums, target, 0, len(nums)//2)
        return nums[k + len(nums)//2] == target 


    """1160. Find Words That Can Be Formed by Characters (Easy)
	You are given an array of strings words and a string chars. A string is 
	good if it can be formed by characters from chars (each character can only 
	be used once). Return the sum of lengths of all good strings in words.

	Example 1:
	Input: words = ["cat","bt","hat","tree"], chars = "atach"
	Output: 6
	Explanation: The strings that can be formed are "cat" and "hat" so the 
	             answer is 3 + 3 = 6.

	Example 2:
	Input: words = ["hello","world","leetcode"], chars = "welldonehoneyr"
	Output: 10
	Explanation: The strings that can be formed are "hello" and "world" so the 
	             answer is 5 + 5 = 10.

	Note:
	* 1 <= words.length <= 1000
	* 1 <= words[i].length, chars.length <= 100
	* All strings contain lowercase English letters only."""

    def countCharacters(self, words: List[str], chars: str) -> int:
        fc = {}
        for c in chars: fc[c] = 1 + fc.get(c, 0)
        
        ans = 0
        for word in words: 
            fw = {}
            for c in word: fw[c] = 1 + fw.get(c, 0)
            if all(fw[c] <= fc.get(c, 0) for c in fw): ans += len(word)
        return ans 


    """1161. Maximum Level Sum of a Binary Tree (Medium)
	Given the root of a binary tree, the level of its root is 1, the level of 
	its children is 2, and so on. Return the smallest level x such that the sum 
	of all the values of nodes at level x is maximal.

	Example 1:
	Input: root = [1,7,0,7,-8,null,null]
	Output: 2
	Explanation: 
	Level 1 sum = 1.
	Level 2 sum = 7 + 0 = 7.
	Level 3 sum = 7 + -8 = -1.
	So we return the level with the maximum sum which is level 2.
	
	Example 2:
	Input: root = [989,null,10250,98693,-89388,null,null,null,-32127]
	Output: 2

	Constraints:
	* The number of nodes in the tree is in the range [1, 10^4].
	* -10^5 <= Node.val <= 10^5"""

    def maxLevelSum(self, root: TreeNode) -> int:
        ans = level = 0
        val = -inf
        queue = [root]
        while queue: 
            level += 1
            newq = []
            tmp = 0
            for node in queue: 
                tmp += node.val
                if node.left: newq.append(node.left)
                if node.right: newq.append(node.right)
            if tmp > val: ans, val = level, tmp
            queue = newq
        return ans 


    """1162. As Far from Land as Possible (Medium)
	Given an n x n grid containing only values 0 and 1, where 0 represents 
	water and 1 represents land, find a water cell such that its distance to 
	the nearest land cell is maximized, and return the distance. If no land or 
	water exists in the grid, return -1. The distance used in this problem is 
	the Manhattan distance: the distance between two cells (x0, y0) and (x1, y1) 
	is |x0 - x1| + |y0 - y1|.

	Example 1:
	Input: grid = [[1,0,1],[0,0,0],[1,0,1]]
	Output: 2
	Explanation: The cell (1, 1) is as far as possible from all the land with distance 2.

	Example 2:
	Input: grid = [[1,0,0],[0,0,0],[0,0,0]]
	Output: 4
	Explanation: The cell (2, 2) is as far as possible from all the land with distance 4.

	Constraints:
	* n == grid.length
	* n == grid[i].length
	* 1 <= n <= 100
	* grid[i][j] is 0 or 1"""

    def maxDistance(self, grid: List[List[int]]) -> int:
        n = len(grid) # dimension
        
        ans = -1
        queue = [(i, j) for i in range(n) for j in range(n) if grid[i][j]]
        while queue: 
            newq = []
            for i, j in queue: 
                for ii, jj in (i-1, j), (i, j-1), (i, j+1), (i+1, j):
                    if 0 <= ii < n and 0 <= jj < n and not grid[ii][jj]: 
                        newq.append((ii, jj))
                        grid[ii][jj] = 1 # mark as visited 
            queue = newq
            ans += 1
        return ans or -1


    """1163. Last Substring in Lexicographical Order (Hard)
	Given a string s, return the last substring of s in lexicographical order.

	Example 1:
	Input: s = "abab"
	Output: "bab"
	Explanation: The substrings are ["a", "ab", "aba", "abab", "b", "ba", "bab"]. 
	             The lexicographically maximum substring is "bab".

	Example 2:
	Input: s = "leetcode"
	Output: "tcode"

	Constraints:
	* 1 <= s.length <= 4 * 105
	* s contains only lowercase English letters."""

    def lastSubstring(self, s: str) -> str:
        ii = k = 0 # anchor
        i = 1 # pointer 
        while i + k < len(s): 
            if s[ii+k] == s[i+k]: k += 1
            else: 
                if s[ii+k] > s[i+k]: i += k+1
                else: 
                    ii = max(ii+k+1, i)
                    i = ii+1
                k = 0
        return s[ii:]


    """1165. Single-Row Keyboard (Easy)
	There is a special keyboard with all keys in a single row. Given a string 
	keyboard of length 26 indicating the layout of the keyboard (indexed from 
	0 to 25), initially your finger is at index 0. To type a character, you 
	have to move your finger to the index of the desired character. The time 
	taken to move your finger from index i to index j is |i - j|. You want to 
	type a string word. Write a function to calculate how much time it takes to 
	type it with one finger.

	Example 1:
	Input: keyboard = "abcdefghijklmnopqrstuvwxyz", word = "cba"
	Output: 4
	Explanation: The index moves from 0 to 2 to write 'c' then to 1 to write 
	             'b' then to 0 again to write 'a'. Total time = 2 + 1 + 1 = 4. 
	
	Example 2:
	Input: keyboard = "pqrstuvwxyzabcdefghijklmno", word = "leetcode"
	Output: 73

	Constraints:
	* keyboard.length == 26
	* keyboard contains each English lowercase letter exactly once in some order.
	* 1 <= word.length <= 10^4
	* word[i] is an English lowercase letter."""

    def calculateTime(self, keyboard: str, word: str) -> int:
        loc = {c: i for i, c in enumerate(keyboard)}
        ans = prev = 0
        for c in word: 
            ans += abs(loc[c] - prev)
            prev = loc[c]
        return ans 


    """1167. Minimum Cost to Connect Sticks (Medium)
	You have some number of sticks with positive integer lengths. These lengths 
	are given as an array sticks, where sticks[i] is the length of the ith 
	stick. You can connect any two sticks of lengths x and y into one stick by 
	paying a cost of x + y. You must connect all the sticks until there is only 
	one stick remaining. Return the minimum cost of connecting all the given 
	sticks into one stick in this way.

	Example 1:
	Input: sticks = [2,4,3]
	Output: 14
	Explanation: You start with sticks = [2,4,3].
	1. Combine sticks 2 and 3 for a cost of 2 + 3 = 5. Now you have sticks = [5,4].
	2. Combine sticks 5 and 4 for a cost of 5 + 4 = 9. Now you have sticks = [9].
	There is only one stick left, so you are done. The total cost is 5 + 9 = 14.

	Example 2:
	Input: sticks = [1,8,3,5]
	Output: 30
	Explanation: You start with sticks = [1,8,3,5].
	1. Combine sticks 1 and 3 for a cost of 1 + 3 = 4. Now you have sticks = [4,8,5].
	2. Combine sticks 4 and 5 for a cost of 4 + 5 = 9. Now you have sticks = [9,8].
	3. Combine sticks 9 and 8 for a cost of 9 + 8 = 17. Now you have sticks = [17].
	There is only one stick left, so you are done. The total cost is 4 + 9 + 17 = 30.

	Example 3:
	Input: sticks = [5]
	Output: 0
	Explanation: There is only one stick, so you don't need to do anything. The total cost is 0.

	Constraints:
	* 1 <= sticks.length <= 104
	* 1 <= sticks[i] <= 104"""

    def connectSticks(self, sticks: List[int]) -> int:
        heapify(sticks)
        ans = 0 
        while len(sticks) > 1: 
            x = heappop(sticks)
            y = heappop(sticks)
            heappush(sticks, x + y)
            ans += x + y 
        return ans 


    """1176. Diet Plan Performance (Easy)
	A dieter consumes calories[i] calories on the i-th day. Given an integer k, 
	for every consecutive sequence of k days (calories[i], calories[i+1], ..., 
	calories[i+k-1] for all 0 <= i <= n-k), they look at T, the total calories 
	consumed during that sequence of k days (calories[i] + calories[i+1] + ... 
	+ calories[i+k-1]):
	* If T < lower, they performed poorly on their diet and lose 1 point; 
	* If T > upper, they performed well on their diet and gain 1 point;
	* Otherwise, they performed normally and there is no change in points.
	Initially, the dieter has zero points. Return the total number of points 
	the dieter has after dieting for calories.length days. Note that the total 
	points can be negative.

	Example 1:
	Input: calories = [1,2,3,4,5], k = 1, lower = 3, upper = 3
	Output: 0
	Explanation: Since k = 1, we consider each element of the array separately and compare it to lower and upper.
	calories[0] and calories[1] are less than lower so 2 points are lost.
	calories[3] and calories[4] are greater than upper so 2 points are gained.

	Example 2:
	Input: calories = [3,2], k = 2, lower = 0, upper = 1
	Output: 1
	Explanation: Since k = 2, we consider subarrays of length 2.
	calories[0] + calories[1] > upper so 1 point is gained.

	Example 3:
	Input: calories = [6,5,0,0], k = 2, lower = 1, upper = 5
	Output: 0
	Explanation:
	calories[0] + calories[1] > upper so 1 point is gained.
	lower <= calories[1] + calories[2] <= upper so no change in points.
	calories[2] + calories[3] < lower so 1 point is lost.

	Constraints:
	* 1 <= k <= calories.length <= 10^5
	* 0 <= calories[i] <= 20000
	* 0 <= lower <= upper"""

    def dietPlanPerformance(self, calories: List[int], k: int, lower: int, upper: int) -> int:
        ans = val = 0
        for i, x in enumerate(calories): 
            val += x
            if i+1 >= k: 
                if val < lower: ans -= 1
                elif val > upper: ans += 1
                val -= calories[i-k+1]
        return ans 


    """1180. Count Substrings with Only One Distinct Letter (Easy)
	Given a string S, return the number of substrings that have only one 
	distinct letter.

	Example 1:
	Input: S = "aaaba"
	Output: 8
	Explanation: The substrings with one distinct letter are "aaa", "aa", "a", "b".
	             "aaa" occurs 1 time.
	             "aa" occurs 2 times.
	             "a" occurs 4 times.
	             "b" occurs 1 time.
	             So the answer is 1 + 2 + 4 + 1 = 8.

	Example 2:
	Input: S = "aaaaaaaaaa"
	Output: 55

	Constraints:
	* 1 <= S.length <= 1000
	* S[i] consists of only lowercase English letters."""

    def countLetters(self, S: str) -> int:
        ans = ii = 0
        for i in range(len(S)):
            if S[ii] != S[i]: ii = i 
            ans += i - ii + 1
        return ans 


    """1196. How Many Apples Can You Put into the Basket (Easy)
	You have some apples, where arr[i] is the weight of the i-th apple. You 
	also have a basket that can carry up to 5000 units of weight. Return the 
	maximum number of apples you can put in the basket.

	Example 1:
	Input: arr = [100,200,150,1000]
	Output: 4
	Explanation: All 4 apples can be carried by the basket since their sum of 
	             weights is 1450.

	Example 2:
	Input: arr = [900,950,800,1000,700,800]
	Output: 5
	Explanation: The sum of weights of the 6 apples exceeds 5000 so we choose 
	             any 5 of them.

	Constraints:
	* 1 <= arr.length <= 10^3
	* 1 <= arr[i] <= 10^3"""

    def maxNumberOfApples(self, arr: List[int]) -> int:
        ans = wt = 0
        for x in sorted(arr): 
            wt += x
            if wt <= 5000: ans += 1
        return ans 


    """1197. Minimum Knight Moves (Medium)
	In an infinite chess board with coordinates from -infinity to +infinity, 
	you have a knight at square [0, 0]. A knight has 8 possible moves it can 
	make, as illustrated below. Each move is two squares in a cardinal 
	direction, then one square in an orthogonal direction. Return the minimum 
	number of steps needed to move the knight to the square [x, y].  It is 
	guaranteed the answer exists.

	Example 1:
	Input: x = 2, y = 1
	Output: 1
	Explanation: [0, 0] → [2, 1]

	Example 2:
	Input: x = 5, y = 5
	Output: 4
	Explanation: [0, 0] → [2, 1] → [4, 2] → [3, 4] → [5, 5]

	Constraints: |x| + |y| <= 300"""

    def minKnightMoves(self, x: int, y: int) -> int:
        
        @cache
        def fn(x, y): 
            """Return minimum moves from (x, y) to (0, 0)."""
            x, y = abs(x), abs(y) # symmetry 
            if x == y == 0: return 0 
            if x + y == 2: return 2
            return 1 + min(fn(x-2, y-1), fn(x-1, y-2))
        
        return fn(x, y)


    """1198. Find Smallest Common Element in All Rows (Medium)
	Given a matrix mat where every row is sorted in strictly increasing order, 
	return the smallest common element in all rows. If there is no common 
	element, return -1.

	Example 1:
	Input: mat = [[1,2,3,4,5],[2,4,5,8,10],[3,5,7,9,11],[1,3,5,7,9]]
	Output: 5

	Constraints:
	* 1 <= mat.length, mat[i].length <= 500
	* 1 <= mat[i][j] <= 10^4
	* mat[i] is sorted in strictly increasing order."""

    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0]) # dimensions
        freq = {}
        for j in range(n):
            for i in range(m): 
                freq[mat[i][j]] = 1 + freq.get(mat[i][j], 0)
                if freq[mat[i][j]] == m: return mat[i][j]
        return -1 


    """1213. Intersection of Three Sorted Arrays (Easy)
	Given three integer arrays arr1, arr2 and arr3 sorted in strictly 
	increasing order, return a sorted array of only the integers that 
	appeared in all three arrays.

	Example 1:
	Input: arr1 = [1,2,3,4,5], 
	       arr2 = [1,2,5,7,9], 
	       arr3 = [1,3,4,5,8]
	Output: [1,5]
	Explanation: Only 1 and 5 appeared in the three arrays.

	Example 2:
	Input: arr1 = [197,418,523,876,1356], 
	       arr2 = [501,880,1593,1710,1870], 
	       arr3 = [521,682,1337,1395,1764]
	Output: []

	Constraints:
	* 1 <= arr1.length, arr2.length, arr3.length <= 1000
	* 1 <= arr1[i], arr2[i], arr3[i] <= 2000"""

    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        ans = []
        i1 = i2 = i3 = 0
        while i1 < len(arr1) and i2 < len(arr2) and i3 < len(arr3): 
            if arr1[i1] == arr2[i2] == arr3[i3]: ans.append(arr1[i1])
            mn = min(arr1[i1], arr2[i2], arr3[i3])
            if arr1[i1] == mn: i1 += 1
            if arr2[i2] == mn: i2 += 1
            if arr3[i3] == mn: i3 += 1
        return ans 


    """1214. Two Sum BSTs (Medium)
	Given the roots of two binary search trees, root1 and root2, return true if 
	and only if there is a node in the first tree and a node in the second tree 
	whose values sum up to a given integer target.

	Example 1:
	Input: root1 = [2,1,4], root2 = [1,0,3], target = 5
	Output: true
	Explanation: 2 and 3 sum up to 5.

	Example 2:
	Input: root1 = [0,-10,10], root2 = [5,1,7,0,2], target = 18
	Output: false

	Constraints:
	* The number of nodes in each tree is in the range [1, 5000].
	* -10^9 <= Node.val, target <= 10^9"""

    def twoSumBSTs(self, root1: TreeNode, root2: TreeNode, target: int) -> bool:
        
        def fn(node): 
            """Return inorder traversal of binary tree."""
            ans, stack = [], []
            while stack or node: 
                if node: 
                    stack.append(node)
                    node = node.left
                else: 
                    node = stack.pop()
                    ans.append(node.val)
                    node = node.right 
            return ans 
        
        val1, val2 = fn(root1), fn(root2)
        lo, hi = 0, len(val2)-1
        while lo < len(val1) and 0 <= hi:
            if val1[lo] + val2[hi] < target: lo += 1
            elif val1[lo] + val2[hi] == target: return True 
            else: hi -= 1
        return False 


    """1217. Minimum Cost to Move Chips to The Same Position (Easy)
	We have n chips, where the position of the ith chip is position[i]. We need 
	to move all the chips to the same position. In one step, we can change the 
	position of the ith chip from position[i] to:
	* position[i] + 2 or position[i] - 2 with cost = 0.
	* position[i] + 1 or position[i] - 1 with cost = 1.
	Return the minimum cost needed to move all the chips to the same position.

	Example 1:
	Input: position = [1,2,3]
	Output: 1
	Explanation: First step: Move the chip at position 3 to position 1 with cost = 0.
          	     Second step: Move the chip at position 2 to position 1 with cost = 1.
	             Total cost is 1.

	Example 2:
	Input: position = [2,2,2,3,3]
	Output: 2
	Explanation: We can move the two chips at position  3 to position 2. Each 
	             move has cost = 1. The total cost = 2.
	
	Example 3:
	Input: position = [1,1000000000]
	Output: 1

	Constraints:
	* 1 <= position.length <= 100
	* 1 <= position[i] <= 10^9"""

    def minCostToMoveChips(self, position: List[int]) -> int:
        odd = even = 0
        for x in position: 
            if x&1: odd += 1
            else: even += 1
        return min(odd, even)


    """1218. Longest Arithmetic Subsequence of Given Difference (Medium)
	Given an integer array arr and an integer difference, return the length of 
	the longest subsequence in arr which is an arithmetic sequence such that 
	the difference between adjacent elements in the subsequence equals 
	difference. A subsequence is a sequence that can be derived from arr by 
	deleting some or no elements without changing the order of the remaining 
	elements.

	Example 1:
	Input: arr = [1,2,3,4], difference = 1
	Output: 4
	Explanation: The longest arithmetic subsequence is [1,2,3,4].

	Example 2:
	Input: arr = [1,3,5,7], difference = 1
	Output: 1
	Explanation: The longest arithmetic subsequence is any single element.

	Example 3:
	Input: arr = [1,5,7,8,5,3,4,2,1], difference = -2
	Output: 4
	Explanation: The longest arithmetic subsequence is [7,5,3,1].

	Constraints:
	* 1 <= arr.length <= 10^5
	* -10^4 <= arr[i], difference <= 10^4"""

    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        ans = 0 
        seen = {}
        for x in arr: 
            seen[x] = 1 + seen.get(x-difference, 0)
            ans = max(ans, seen[x])
        return ans 


    """1219. Path with Maximum Gold (Medium)
	In a gold mine grid of size m * n, each cell in this mine has an integer 
	representing the amount of gold in that cell, 0 if it is empty. Return the 
	maximum amount of gold you can collect under the conditions:
	* Every time you are located in a cell you will collect all the gold in 
	  that cell.
	* From your position you can walk one step to the left, right, up or down.
	* You can't visit the same cell more than once.
	* Never visit a cell with 0 gold.
	* You can start and stop collecting gold from any position in the grid that 
	  has some gold.

	Example 1:
	Input: grid = [[0,6,0],[5,8,7],[0,9,0]]
	Output: 24
	Explanation:
	[[0,6,0],
	 [5,8,7],
	 [0,9,0]]
	Path to get the maximum gold, 9 -> 8 -> 7.

	Example 2:
	Input: grid = [[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]]
	Output: 28
	Explanation:
	[[1,0,7],
	 [2,0,6],
	 [3,4,5],
	 [0,3,0],
	 [9,0,20]]
	Path to get the maximum gold, 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7.

	Constraints:
	* 1 <= grid.length, grid[i].length <= 15
	* 0 <= grid[i][j] <= 100
	* There are at most 25 cells containing gold."""

    def getMaximumGold(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        def fn(i, j): 
            """Collect maximum gold from (i, j) via backtracking."""
            if grid[i][j] <= 0: return 0
            grid[i][j] *= -1 # mark as visited 
            ans = 0
            for ii, jj in (i-1, j), (i, j-1), (i, j+1), (i+1, j): 
                if 0 <= ii < m and 0 <= jj < n: 
                    ans = max(ans, fn(ii, jj) - grid[i][j])
            grid[i][j] *= -1 # backtracking 
            return ans 
        
        return max(fn(i, j) for i in range(m) for j in range(n) if grid[i][j])


    """1220. Count Vowels Permutation (Hard)
	Given an integer n, your task is to count how many strings of length n can 
	be formed under the following rules:
	* Each character is a lower case vowel ('a', 'e', 'i', 'o', 'u')
	* Each vowel 'a' may only be followed by an 'e'.
	* Each vowel 'e' may only be followed by an 'a' or an 'i'.
	* Each vowel 'i' may not be followed by another 'i'.
	* Each vowel 'o' may only be followed by an 'i' or a 'u'.
	* Each vowel 'u' may only be followed by an 'a'.
	Since the answer may be too large, return it modulo 10^9 + 7.

	Example 1:
	Input: n = 1
	Output: 5
	Explanation: All possible strings are: "a", "e", "i" , "o" and "u".

	Example 2:
	Input: n = 2
	Output: 10
	Explanation: All possible strings are: "ae", "ea", "ei", "ia", "ie", "io", "iu", "oi", "ou" and "ua".

	Example 3: 
	Input: n = 5
	Output: 68

	Constraints: 1 <= n <= 2 * 10^4"""

    def countVowelPermutation(self, n: int) -> int:
        a = e = i = o = u = 1
        for _ in range(n-1): 
            a, e, i, o, u = e, a+i, a+e+o+u, i+u, a
        return (a+e+i+o+u) % 1_000_000_007


    """1221. Split a String in Balanced Strings (Easy)
	Balanced strings are those that have an equal quantity of 'L' and 'R' 
	characters. Given a balanced string s, split it in the maximum amount of 
	balanced strings. Return the maximum amount of split balanced strings.

	Example 1:
	Input: s = "RLRRLLRLRL"
	Output: 4
	Explanation: s can be split into "RL", "RRLL", "RL", "RL", each substring 
	             contains same number of 'L' and 'R'.

	Example 2:
	Input: s = "RLLLLRRRLR"
	Output: 3
	Explanation: s can be split into "RL", "LLLRRR", "LR", each substring 
	             contains same number of 'L' and 'R'.
	
	Example 3:
	Input: s = "LLLLRRRR"
	Output: 1
	Explanation: s can be split into "LLLLRRRR".

	Example 4:
	Input: s = "RLRRRLLRLL"
	Output: 2
	Explanation: s can be split into "RL", "RRRLLRLL", since each substring 
	             contains an equal number of 'L' and 'R'

	Constraints:
	* 1 <= s.length <= 1000
	* s[i] is either 'L' or 'R'.
	* s is a balanced string."""

    def balancedStringSplit(self, s: str) -> int:
        ans = prefix = 0
        for c in s: 
            prefix += 1 if c == "R" else -1
            if not prefix: ans += 1
        return ans 


    """1221. Split a String in Balanced Strings (Easy)
	Balanced strings are those that have an equal quantity of 'L' and 'R' 
	characters. Given a balanced string s, split it in the maximum amount of 
	balanced strings. Return the maximum amount of split balanced strings.

	Example 1:
	Input: s = "RLRRLLRLRL"
	Output: 4
	Explanation: s can be split into "RL", "RRLL", "RL", "RL", each substring 
	             contains same number of 'L' and 'R'.

	Example 2:
	Input: s = "RLLLLRRRLR"
	Output: 3
	Explanation: s can be split into "RL", "LLLRRR", "LR", each substring 
	             contains same number of 'L' and 'R'.
	
	Example 3:
	Input: s = "LLLLRRRR"
	Output: 1
	Explanation: s can be split into "LLLLRRRR".

	Example 4:
	Input: s = "RLRRRLLRLL"
	Output: 2
	Explanation: s can be split into "RL", "RRRLLRLL", since each substring 
	             contains an equal number of 'L' and 'R'

	Constraints:
	* 1 <= s.length <= 1000
	* s[i] is either 'L' or 'R'.
	* s is a balanced string."""

    def balancedStringSplit(self, s: str) -> int:
        ans = prefix = 0
        for c in s: 
            prefix += 1 if c == "R" else -1
            if not prefix: ans += 1
        return ans 


    """1222. Queens That Can Attack the King (Medium)
	On an 8x8 chessboard, there can be multiple Black Queens and one White King. 
	Given an array of integer coordinates queens that represents the positions 
	of the Black Queens, and a pair of coordinates king that represent the 
	position of the White King, return the coordinates of all the queens (in any 
	order) that can attack the King.

	Example 1:
	Input: queens = [[0,1],[1,0],[4,0],[0,4],[3,3],[2,4]], king = [0,0]
	Output: [[0,1],[1,0],[3,3]]
	Explanation:  
	The queen at [0,1] can attack the king cause they're in the same row. 
	The queen at [1,0] can attack the king cause they're in the same column. 
	The queen at [3,3] can attack the king cause they're in the same diagnal. 
	The queen at [0,4] can't attack the king cause it's blocked by the queen at [0,1]. 
	The queen at [4,0] can't attack the king cause it's blocked by the queen at [1,0]. 
	The queen at [2,4] can't attack the king cause it's not in the same row/column/diagnal as the king.

	Example 2:
	Input: queens = [[0,0],[1,1],[2,2],[3,4],[3,5],[4,4],[4,5]], king = [3,3]
	Output: [[2,2],[3,4],[4,4]]

	Example 3:
	Input: queens = [[5,6],[7,7],[2,1],[0,7],[1,6],[5,1],[3,7],[0,3],[4,0],
	                 [1,2],[6,3],[5,0],[0,4],[2,2],[1,1],[6,4],[5,4],[0,0],
	                 [2,6],[4,5],[5,2],[1,4],[7,5],[2,3],[0,5],[4,2],[1,0],
	                 [2,7],[0,1],[4,6],[6,1],[0,6],[4,3],[1,7]], king = [3,4]
	Output: [[2,3],[1,4],[1,6],[3,7],[4,3],[5,4],[4,5]]

	Constraints:
	* 1 <= queens.length <= 63
	* queens[i].length == 2
	* 0 <= queens[i][j] < 8
	* king.length == 2
	* 0 <= king[0], king[1] < 8
	* At most one piece is allowed in a cell."""

    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        ans = []
        x, y = king
        queens = {(x, y) for x, y in queens}
        for dx in (-1, 0, 1):
            for dy in (-1, 0, 1):
                for k in range(1, 8):
                    xx, yy = x+k*dx, y+k*dy
                    if (xx, yy) in queens: 
                        ans.append([xx, yy])
                        break 
        return ans 


    """1223. Dice Roll Simulation (Hard)
	A die simulator generates a random number from 1 to 6 for each roll. You 
	introduced a constraint to the generator such that it cannot roll the 
	number i more than rollMax[i] (1-indexed) consecutive times.  Given an 
	array of integers rollMax and an integer n, return the number of distinct 
	sequences that can be obtained with exact n rolls. Two sequences are 
	considered different if at least one element differs from each other. Since 
	the answer may be too large, return it modulo 10^9 + 7.

	Example 1:
	Input: n = 2, rollMax = [1,1,2,2,2,3]
	Output: 34
	Explanation: There will be 2 rolls of die, if there are no constraints on 
	             the die, there are 6 * 6 = 36 possible combinations. In this 
	             case, looking at rollMax array, the numbers 1 and 2 appear at 
	             most once consecutively, therefore sequences (1,1) and (2,2) 
	             cannot occur, so the final answer is 36-2 = 34.

	Example 2:
	Input: n = 2, rollMax = [1,1,1,1,1,1]
	Output: 30
	
	Example 3:
	Input: n = 3, rollMax = [1,1,1,2,2,3]
	Output: 181

	Constraints:
	* 1 <= n <= 5000
	* rollMax.length == 6
	* 1 <= rollMax[i] <= 15"""

    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        
        @cache
        def fn(n, x, r):
            """Return number of sequences with n rolls left with r occurrences of x."""
            if n == 0: return 1
            ans = 0
            for xx in range(6): 
                if xx != x: ans += fn(n-1, xx, 1)
                elif xx == x and r < rollMax[x]: ans += fn(n-1, x, r+1)
            return ans 
        
        return sum(fn(n-1, x, 1) for x in range(6)) % 1_000_000_007


    """1224. Maximum Equal Frequency (Hard)
	Given an array nums of positive integers, return the longest possible 
	length of an array prefix of nums, such that it is possible to remove 
	exactly one element from this prefix so that every number that has appeared 
	in it will have the same number of occurrences. If after removing one 
	element there are no remaining elements, it's still considered that every 
	appeared number has the same number of ocurrences (0).

	Example 1:
	Input: nums = [2,2,1,1,5,3,3,5]
	Output: 7
	Explanation: For the subarray [2,2,1,1,5,3,3] of length 7, if we remove 
	             nums[4]=5, we will get [2,2,1,1,3,3], so that each number 
	             will appear exactly twice.

	Example 2:
	Input: nums = [1,1,1,2,2,2,3,3,3,4,4,4,5]
	Output: 13

	Example 3:
	Input: nums = [1,1,1,2,2,2]
	Output: 5

	Example 4:
	Input: nums = [10,2,8,9,3,8,1,5,2,3,7,6]
	Output: 8

	Constraints:
	* 2 <= nums.length <= 10^5
	* 1 <= nums[i] <= 10^5"""

    def maxEqualFreq(self, nums: List[int]) -> int:
        ans = most = 0
        cnt = defaultdict(int)
        freq = defaultdict(int)
        for i, x in enumerate(nums):
            cnt[x] += 1
            freq[cnt[x]-1] -= 1
            freq[cnt[x]] += 1
            most = max(most, cnt[x])
            if most == 1 or most * freq[most] == i or (most-1)*freq[most-1] + most == i+1: ans = i+1
        return ans 


    """1228. Missing Number In Arithmetic Progression (Easy)
	In some array arr, the values were in arithmetic progression: the values 
	arr[i+1] - arr[i] are all equal for every 0 <= i < arr.length - 1. Then, a 
	value from arr was removed that was not the first or last value in the 
	array. Return the removed value.

	Example 1:
	Input: arr = [5,7,11,13]
	Output: 9
	Explanation: The previous array was [5,7,9,11,13].

	Example 2:
	Input: arr = [15,13,12]
	Output: 14
	Explanation: The previous array was [15,14,13,12].

	Constraints:
	* 3 <= arr.length <= 1000
	* 0 <= arr[i] <= 10^5"""

    def missingNumber(self, arr: List[int]) -> int:
        chg = (arr[-1] - arr[0])//len(arr)
        lo, hi = 0, len(arr)
        while lo < hi: 
            mid = lo + hi >> 1
            if arr[mid] == arr[0] + mid * chg: lo = mid + 1
            else: hi = mid
        return arr[0] + lo * chg


    """1232. Check If It Is a Straight Line (Easy)
	You are given an array coordinates, coordinates[i] = [x, y], where [x, y] 
	represents the coordinate of a point. Check if these points make a straight 
	line in the XY plane.

	Example 1:
	Input: coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
	Output: true

	Example 2:
	Input: coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
	Output: false

	Constraints:
	* 2 <= coordinates.length <= 1000
	* coordinates[i].length == 2
	* -10^4 <= coordinates[i][0], coordinates[i][1] <= 10^4
	* coordinates contains no duplicate point."""

    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        x0, y0 = coordinates[0]
        x1, y1 = coordinates[1]
        for x, y in coordinates[2:]: 
            if (y1-y0)*(x-x0) != (y-y0)*(x1-x0): return False 
        return True 


    """1233. Remove Sub-Folders from the Filesystem (Medium)
	Given a list of folders, remove all sub-folders in those folders and return 
	in any order the folders after removing. If a folder[i] is located within 
	another folder[j], it is called a sub-folder of it. The format of a path is 
	one or more concatenated strings of the form: / followed by one or more 
	lowercase English letters. For example, /leetcode and /leetcode/problems 
	are valid paths while an empty string and / are not.

	Example 1:
	Input: folder = ["/a","/a/b","/c/d","/c/d/e","/c/f"]
	Output: ["/a","/c/d","/c/f"]
	Explanation: Folders "/a/b/" is a subfolder of "/a" and "/c/d/e" is inside 
	             of folder "/c/d" in our filesystem.

	Example 2:
	Input: folder = ["/a","/a/b/c","/a/b/d"]
	Output: ["/a"]
	Explanation: Folders "/a/b/c" and "/a/b/d/" will be removed because they 
	             are subfolders of "/a".
	
	Example 3:
	Input: folder = ["/a/b/c","/a/b/ca","/a/b/d"]
	Output: ["/a/b/c","/a/b/ca","/a/b/d"]

	Constraints:
	* 1 <= folder.length <= 4 * 10^4
	* 2 <= folder[i].length <= 100
	* folder[i] contains only lowercase letters and '/'
	* folder[i] always starts with character '/'
	* Each folder name is unique."""

    def removeSubfolders(self, folder: List[str]) -> List[str]:
        ans = []
        for x in sorted(folder): 
            if not ans or not x.startswith(ans[-1]+"/"): 
                ans.append(x)
        return ans 


    """1234. Replace the Substring for Balanced String (Medium)
	You are given a string containing only 4 kinds of characters 'Q', 'W', 'E' 
	and 'R'. A string is said to be balanced if each of its characters appears 
	n/4 times where n is the length of the string. Return the minimum length of 
	the substring that can be replaced with any other string of the same length 
	to make the original string s balanced. Return 0 if the string is already 
	balanced.

	Example 1:
	Input: s = "QWER"
	Output: 0
	Explanation: s is already balanced.

	Example 2:
	Input: s = "QQWE"
	Output: 1
	Explanation: We need to replace a 'Q' to 'R', so that "RQWE" (or "QRWE") is balanced.

	Example 3:
	Input: s = "QQQW"
	Output: 2
	Explanation: We can replace the first "QQ" to "ER". 

	Example 4:
	Input: s = "QQQQ"
	Output: 3
	Explanation: We can replace the last 3 'Q' to make s = "QWER".

	Constraints:
	* 1 <= s.length <= 10^5
	* s.length is a multiple of 4
	* s contains only 'Q', 'W', 'E' and 'R'."""

    def balancedString(self, s: str) -> int:
        freq = {}
        for c in s: freq[c] = 1 + freq.get(c, 0)
            
        ans = len(s)
        ii = 0
        for i, c in enumerate(s): 
            freq[c] -= 1
            while ii < len(s) and all(freq[x] <= len(s)//4 for x in freq): 
                ans = min(ans, i-ii+1)
                freq[s[ii]] += 1
                ii += 1
        return ans 


    """1235. Maximum Profit in Job Scheduling (Hard)
	We have n jobs, where every job is scheduled to be done from startTime[i] 
	to endTime[i], obtaining a profit of profit[i]. You're given the startTime, 
	endTime and profit arrays, return the maximum profit you can take such that 
	there are no two jobs in the subset with overlapping time range. If you 
	choose a job that ends at time X you will be able to start another job that 
	starts at time X.

	Example 1:
	Input: startTime = [1,2,3,3], endTime = [3,4,5,6], profit = [50,10,40,70]
	Output: 120
	Explanation: The subset chosen is the first and fourth job. Time range 
	             [1-3]+[3-6] , we get profit of 120 = 50 + 70.

	Example 2:
	Input: startTime = [1,2,3,4,6], endTime = [3,5,10,6,9], profit = [20,20,100,70,60]
	Output: 150
	Explanation: The subset chosen is the first, fourth and fifth job. Profit 
	             obtained 150 = 20 + 70 + 60.
	
	Example 3:
	Input: startTime = [1,1,1], endTime = [2,3,4], profit = [5,6,4]
	Output: 6

	Constraints:
	* 1 <= startTime.length == endTime.length == profit.length <= 5 * 10^4
	* 1 <= startTime[i] < endTime[i] <= 10^9
	* 1 <= profit[i] <= 10^4"""

    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        startTime, endTime, profit = zip(*sorted(zip(startTime, endTime, profit)))
        
        @cache
        def fn(i): 
            """Return max profit starting from index i."""
            if i == len(startTime): return 0 
            ii = bisect_left(startTime, endTime[i])
            return max(fn(i+1), profit[i] + fn(ii))
        
        return fn(0)


    """1243. Array Transformation (Easy)
	Given an initial array arr, every day you produce a new array using the 
	array of the previous day. On the i-th day, you do the following operations 
	on the array of day i-1 to produce the array of day i:
	* If an element is smaller than both its left neighbor and its right 
	  neighbor, then this element is incremented.
	* If an element is bigger than both its left neighbor and its right 
	  neighbor, then this element is decremented.
	* The first and last elements never change.
	After some days, the array does not change. Return that final array.

	Example 1:
	Input: arr = [6,2,3,4]
	Output: [6,3,3,4]
	Explanation: On the first day, the array is changed from [6,2,3,4] to 
	             [6,3,3,4]. No more operations can be done to this array.
	
	Example 2:
	Input: arr = [1,6,3,4,3,5]
	Output: [1,4,4,4,4,5]
	Explanation: 
	On the first day, the array is changed from [1,6,3,4,3,5] to [1,5,4,3,4,5].
	On the second day, the array is changed from [1,5,4,3,4,5] to [1,4,4,4,4,5].
	No more operations can be done to this array.

	Constraints:
	* 3 <= arr.length <= 100
	* 1 <= arr[i] <= 100"""

    def transformArray(self, arr: List[int]) -> List[int]:
        prev = [0]*len(arr)
        while prev != arr: 
            prev = arr[:]
            for i in range(1, len(arr)-1): 
                if prev[i-1] < prev[i] > prev[i+1]: arr[i] -= 1
                elif prev[i-1] > prev[i] < prev[i+1]: arr[i] += 1
        return arr


    """1249. Minimum Remove to Make Valid Parentheses (Medium)
	Given a string s of '(' , ')' and lowercase English characters. Your task 
	is to remove the minimum number of parentheses ( '(' or ')', in any 
	positions ) so that the resulting parentheses string is valid and return 
	any valid string. Formally, a parentheses string is valid if and only if:
	* It is the empty string, contains only lowercase characters, or
	* It can be written as AB (A concatenated with B), where A and B are valid strings, or
	* It can be written as (A), where A is a valid string.

	Example 1:
	Input: s = "lee(t(c)o)de)"
	Output: "lee(t(c)o)de"
	Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.

	Example 2:
	Input: s = "a)b(c)d"
	Output: "ab(c)d"

	Example 3:
	Input: s = "))(("
	Output: ""
	Explanation: An empty string is also valid.

	Example 4:
	Input: s = "(a(b(c)d)"
	Output: "a(b(c)d)"

	Constraints:
	* 1 <= s.length <= 10^5
	* s[i] is one of  '(' , ')' and lowercase English letters."""

    def minRemoveToMakeValid(self, s: str) -> str:
        s = list(s)
        stack = []
        for i, c in enumerate(s): 
            if c == "(": stack.append(i)
            elif c == ")": 
                if stack: stack.pop() # matching 
                else: s[i] = "" # extra 
        while stack: s[stack.pop()] = ""
        return "".join(s)


    """1271. Hexspeak (Easy)
	A decimal number can be converted to its Hexspeak representation by first 
	converting it to an uppercase hexadecimal string, then replacing all 
	occurrences of the digit 0 with the letter O, and the digit 1 with the 
	letter I.  Such a representation is valid if and only if it consists only 
	of the letters in the set {"A", "B", "C", "D", "E", "F", "I", "O"}. Given 
	a string num representing a decimal integer N, return the Hexspeak 
	representation of N if it is valid, otherwise return "ERROR".

	Example 1:
	Input: num = "257"
	Output: "IOI"
	Explanation:  257 is 101 in hexadecimal.

	Example 2:
	Input: num = "3"
	Output: "ERROR"

	Constraints:
	* 1 <= N <= 10^12
	* There are no leading zeros in the given string.
	* All answers must be in uppercase letters."""

    def toHexspeak(self, num: str) -> str:
        s = hex(int(num))[2:].upper().translate(str.maketrans("01", "OI"))
        return s if all(c.isalpha() for c in s) else "ERROR"


    """1272. Remove Interval (Medium)
	A set of real numbers can be represented as the union of several disjoint 
	intervals, where each interval is in the form [a, b). A real number x is in 
	the set if one of its intervals [a, b) contains x (i.e. a <= x < b). You 
	are given a sorted list of disjoint intervals intervals representing a set 
	of real numbers as described above, where intervals[i] = [ai, bi] represents 
	the interval [ai, bi). You are also given another interval toBeRemoved. 
	Return the set of real numbers with the interval toBeRemoved removed from 
	intervals. In other words, return the set of real numbers such that every x 
	in the set is in intervals but not in toBeRemoved. Your answer should be a 
	sorted list of disjoint intervals as described above.

	Example 1:
	Input: intervals = [[0,2],[3,4],[5,7]], toBeRemoved = [1,6]
	Output: [[0,1],[6,7]]

	Example 2:
	Input: intervals = [[0,5]], toBeRemoved = [2,3]
	Output: [[0,2],[3,5]]

	Example 3:
	Input: intervals = [[-5,-4],[-3,-2],[1,2],[3,5],[8,9]], toBeRemoved = [-1,4]
	Output: [[-5,-4],[-3,-2],[4,5],[8,9]]

	Constraints:
	* 1 <= intervals.length <= 10^4
	* -10^9 <= ai < bi <= 10^9"""

    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        ans = []
        for x, y in intervals: 
            if x < toBeRemoved[0]: ans.append([x, min(toBeRemoved[0], y)])
            if toBeRemoved[1] < y: ans.append([max(x, toBeRemoved[1]), y])
        return ans 


    """1273. Delete Tree Nodes (Medium)
	A tree rooted at node 0 is given as follows:
	* The number of nodes is nodes;
	* The value of the i-th node is value[i];
	* The parent of the i-th node is parent[i].
	Remove every subtree whose sum of values of nodes is zero. After doing so, 
	return the number of nodes remaining in the tree.

	Example 1:
	Input: nodes = 7, parent = [-1,0,0,1,2,2,2], value = [1,-2,4,0,-2,-1,-1]
	Output: 2

	Example 2:
	Input: nodes = 7, parent = [-1,0,0,1,2,2,2], value = [1,-2,4,0,-2,-1,-2]
	Output: 6

	Example 3:
	Input: nodes = 5, parent = [-1,0,1,0,0], value = [-672,441,18,728,378]
	Output: 5

	Example 4:
	Input: nodes = 5, parent = [-1,0,0,1,1], value = [-686,-842,616,-739,-746]
	Output: 5

	Constraints:
	* 1 <= nodes <= 10^4
	* parent.length == nodes
	* 0 <= parent[i] <= nodes - 1
	* parent[0] == -1 which indicates that 0 is the root.
	* value.length == nodes
	* -10^5 <= value[i] <= 10^5
	* The given input is guaranteed to represent a valid tree."""

    def deleteTreeNodes(self, nodes: int, parent: List[int], value: List[int]) -> int:
        tree = {} # tree as adjacency list 
        for i, x in enumerate(parent): 
            tree.setdefault(x, []).append(i)
        
        def fn(n): 
            """Return sum and count of sub-tree rooted at n."""
            s, c = value[n], 1
            for nn in tree.get(n, []): 
                ss, cc = fn(nn)
                s += ss
                c += cc 
            return (s, c) if s != 0 else (0, 0)
        
        return fn(0)[1]


    """1317. Convert Integer to the Sum of Two No-Zero Integers (Easy)
	Given an integer n. No-Zero integer is a positive integer which doesn't 
	contain any 0 in its decimal representation. Return a list of two integers 
	[A, B] where:
	* A and B are No-Zero integers.
	* A + B = n
	It's guarateed that there is at least one valid solution. If there are many 
	valid solutions you can return any of them.

	Example 1:
	Input: n = 2
	Output: [1,1]
	Explanation: A = 1, B = 1. A + B = n and both A and B don't contain any 0 
	             in their decimal representation.

	Example 2:
	Input: n = 11
	Output: [2,9]
	
	Example 3:
	Input: n = 10000
	Output: [1,9999]

	Example 4:
	Input: n = 69
	Output: [1,68]

	Example 5:
	Input: n = 1010
	Output: [11,999]

	Constraints: 2 <= n <= 10^4"""

    def getNoZeroIntegers(self, n: int) -> List[int]:
        for x in range(1, n//2+1): 
            if "0" not in str(x) and "0" not in str(n-x): 
                return [x, n-x]


    """1318. Minimum Flips to Make a OR b Equal to c (Medium)
	Given 3 positives numbers a, b and c. Return the minimum flips required in 
	some bits of a and b to make ( a OR b == c ). (bitwise OR operation). Flip 
	operation consists of change any single bit 1 to 0 or change the bit 0 to 1 
	in their binary representation.

	Example 1:
	Input: a = 2, b = 6, c = 5
	Output: 3
	Explanation: After flips a = 1 , b = 4 , c = 5 such that (a OR b == c)

	Example 2:
	Input: a = 4, b = 2, c = 7
	Output: 1

	Example 3:
	Input: a = 1, b = 2, c = 3
	Output: 0

	Constraints:
	* 1 <= a <= 10^9
	* 1 <= b <= 10^9
	* 1 <= c <= 10^9"""

    def minFlips(self, a: int, b: int, c: int) -> int:
        return bin((a | b) ^ c).count("1") + bin(a & b & ((a | b) ^ c)).count("1")


	"""1319. Number of Operations to Make Network Connected (Medium)
	There are n computers numbered from 0 to n-1 connected by ethernet cables 
	connections forming a network where connections[i] = [a, b] represents a 
	connection between computers a and b. Any computer can reach any other 
	computer directly or indirectly through the network. Given an initial 
	computer network connections. You can extract certain cables between two 
	directly connected computers, and place them between any pair of 
	disconnected computers to make them directly connected. Return the minimum 
	number of times you need to do this in order to make all the computers 
	connected. If it's not possible, return -1. 

	Example 1:
	Input: n = 4, connections = [[0,1],[0,2],[1,2]]
	Output: 1
	Explanation: Remove cable between computer 1 and 2 and place between 
	             computers 1 and 3.

	Example 2:
	Input: n = 6, connections = [[0,1],[0,2],[0,3],[1,2],[1,3]]
	Output: 2
	
	Example 3:
	Input: n = 6, connections = [[0,1],[0,2],[0,3],[1,2]]
	Output: -1
	Explanation: There are not enough cables.

	Example 4:
	Input: n = 5, connections = [[0,1],[0,2],[3,4],[2,3]]
	Output: 0

	Constraints:
	* 1 <= n <= 10^5
	* 1 <= connections.length <= min(n*(n-1)/2, 10^5)
	* connections[i].length == 2
	* 0 <= connections[i][0], connections[i][1] < n
	* connections[i][0] != connections[i][1]
	* There are no repeated connections.
	* No two computers are connected by more than one cable.

	class UnionFind:
	    def __init__(self, n):
	        self.parent = list(range(n))
	        self.rank = [1] * n
	    
	    def find(self, p):
	        if p != self.parent[p]: 
	            self.parent[p] = self.find(self.parent[p])
	        return self.parent[p]
	    
	    def union(self, p, q): 
	        prt, qrt = self.find(p), self.find(q) 
	        if prt == qrt: return False # already connected 
	        if self.rank[prt] > self.rank[qrt]: prt, qrt = qrt, prt
	        self.parent[prt] = qrt
	        self.rank[qrt] += self.rank[prt]
	        return True"""

    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n-1: return -1 # not enough cables 
        uf = UnionFind(n)
        for u, v in connections: 
        	uf.union(u, v)
        grp = {uf.find(i) for i in range(n)}
        return len(grp) - 1


    """1320. Minimum Distance to Type a Word Using Two Fingers (Hard)
	You have a keyboard layout as shown above in the XY plane, where each 
	English uppercase letter is located at some coordinate, for example, the 
	letter A is located at coordinate (0,0), the letter B is located at 
	coordinate (0,1), the letter P is located at coordinate (2,3) and the 
	letter Z is located at coordinate (4,1). Given the string word, return the 
	minimum total distance to type such string using only two fingers. The 
	distance between coordinates (x1,y1) and (x2,y2) is |x1 - x2| + |y1 - y2|. 
	Note that the initial positions of your two fingers are considered free so 
	don't count towards your total distance, also your two fingers do not have 
	to start at the first letter or the first two letters.

	Example 1:
	Input: word = "CAKE"
	Output: 3
	Explanation: 
	Using two fingers, one optimal way to type "CAKE" is: 
	Finger 1 on letter 'C' -> cost = 0 
	Finger 1 on letter 'A' -> cost = Distance from letter 'C' to letter 'A' = 2 
	Finger 2 on letter 'K' -> cost = 0 
	Finger 2 on letter 'E' -> cost = Distance from letter 'K' to letter 'E' = 1 
	Total distance = 3

	Example 2:
	Input: word = "HAPPY"
	Output: 6
	Explanation: 
	Using two fingers, one optimal way to type "HAPPY" is:
	Finger 1 on letter 'H' -> cost = 0
	Finger 1 on letter 'A' -> cost = Distance from letter 'H' to letter 'A' = 2
	Finger 2 on letter 'P' -> cost = 0
	Finger 2 on letter 'P' -> cost = Distance from letter 'P' to letter 'P' = 0
	Finger 1 on letter 'Y' -> cost = Distance from letter 'A' to letter 'Y' = 4
	Total distance = 6

	Example 3:
	Input: word = "NEW"
	Output: 3

	Example 4:
	Input: word = "YEAR"
	Output: 7

	Constraints:
	* 2 <= word.length <= 300
	* Each word[i] is an English uppercase letter."""

    def minimumDistance(self, word: str) -> int:
        word = [ord(c)-65 for c in word]
        dist = lambda x, y: 0 if -1 in (x, y) else abs(x//6-y//6) + abs(x%6-y%6)
        
        @cache
        def fn(i, f1=-1, f2=-1): 
            """Return minimum distance to type word[i:] with fingers at f1 and f2."""
            if i == len(word): return 0 
            return min(dist(f1, word[i]) + fn(i+1, word[i], f2), dist(f2, word[i]) + fn(i+1, f1, word[i]))
        
        return fn(0)


    """1329. Sort the Matrix Diagonally (Medium)
	A matrix diagonal is a diagonal line of cells starting from some cell in 
	either the topmost row or leftmost column and going in the bottom-right 
	direction until reaching the matrix's end. For example, the matrix diagonal 
	starting from mat[2][0], where mat is a 6 x 3 matrix, includes cells 
	mat[2][0], mat[3][1], and mat[4][2]. Given an m x n matrix mat of integers, 
	sort each matrix diagonal in ascending order and return the resulting matrix.

	Example 1:
	Input: mat = [[3,3,1,1],[2,2,1,2],[1,1,1,2]]
	Output: [[1,1,1,1],[1,2,2,2],[1,2,3,3]]

	Constraints:
	* m == mat.length
	* n == mat[i].length
	* 1 <= m, n <= 100
	* 1 <= mat[i][j] <= 100"""

    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0]) # dimensions 
        
        for k in range(-m+1, n): 
            i, j = (-k, 0) if k < 0 else (0, k)
            vals = []
            while i < m and j < n: 
                vals.append(mat[i][j])
                i, j = i+1, j+1
            vals.sort()
            while vals:
                i, j = i-1, j-1
                mat[i][j] = vals.pop()
        return mat


    """1356. Sort Integers by The Number of 1 Bits (Easy)
	Given an integer array arr. You have to sort the integers in the array in 
	ascending order by the number of 1's in their binary representation and in 
	case of two or more integers have the same number of 1's you have to sort 
	them in ascending order. Return the sorted array.

	Example 1:
	Input: arr = [0,1,2,3,4,5,6,7,8]
	Output: [0,1,2,4,8,3,5,6,7]
	Explantion: [0] is the only integer with 0 bits.
	[1,2,4,8] all have 1 bit.
	[3,5,6] have 2 bits.
	[7] has 3 bits.
	The sorted array by bits is [0,1,2,4,8,3,5,6,7]

	Example 2:
	Input: arr = [1024,512,256,128,64,32,16,8,4,2,1]
	Output: [1,2,4,8,16,32,64,128,256,512,1024]
	Explantion: All integers have 1 bit in the binary representation, you should 
	            just sort them in ascending order.

	Example 3:
	Input: arr = [10000,10000]
	Output: [10000,10000]
	
	Example 4:
	Input: arr = [2,3,5,7,11,13,17,19]
	Output: [2,3,5,17,7,11,13,19]

	Example 5:
	Input: arr = [10,100,1000,10000]
	Output: [10,100,10000,1000]

	Constraints:
	* 1 <= arr.length <= 500
	* 0 <= arr[i] <= 10^4"""

    def sortByBits(self, arr: List[int]) -> List[int]:
        return sorted(arr, key=lambda x: (bin(x).count("1"), x))


    """1358. Number of Substrings Containing All Three Characters (Medium)
	Given a string s consisting only of characters a, b and c. Return the 
	number of substrings containing at least one occurrence of all these 
	characters a, b and c.

	Example 1:
	Input: s = "abcabc"
	Output: 10
	Explanation: The substrings containing at least one occurrence of the 
	             characters a, b and c are "abc", "abca", "abcab", "abcabc", 
	             "bca", "bcab", "bcabc", "cab", "cabc" and "abc" (again). 

	Example 2:
	Input: s = "aaacb"
	Output: 3
	Explanation: The substrings containing at least one occurrence of the 
	             characters a, b and c are "aaacb", "aacb" and "acb". 
	
	Example 3:
	Input: s = "abc"
	Output: 1

	Constraints:
	* 3 <= s.length <= 5 x 10^4
	* s only consists of a, b or c characters."""

    def numberOfSubstrings(self, s: str) -> int:
        ans = 0
        loc = [-1]*3
        for i, c in enumerate(s): 
            loc[ord(c)-97] = i 
            ans += max(0, min(loc)+1)
        return ans 


    """1359. Count All Valid Pickup and Delivery Options (Hard)
	Given n orders, each order consist in pickup and delivery services. Count 
	all valid pickup/delivery possible sequences such that delivery(i) is 
	always after of pickup(i). Since the answer may be too large, return it 
	modulo 10^9 + 7.

	Example 1:
	Input: n = 1
	Output: 1
	Explanation: Unique order (P1, D1), Delivery 1 always is after of Pickup 1.

	Example 2:
	Input: n = 2
	Output: 6
	Explanation: All possible orders: 
	(P1,P2,D1,D2), (P1,P2,D2,D1), (P1,D1,P2,D2), (P2,P1,D1,D2), (P2,P1,D2,D1) and (P2,D2,P1,D1).
	This is an invalid order (P1,D2,P2,D1) because Pickup 2 is after of Delivery 2.

	Example 3:
	Input: n = 3
	Output: 90

	Constraints: 1 <= n <= 500"""

    def countOrders(self, n: int) -> int:
        ans = 1
        for x in range(2, n+1): 
            ans = (ans*x*(2*x-1)) % 1_000_000_007
        return ans 


    """1373. Maximum Sum BST in Binary Tree (Hard)
	Given a binary tree root, the task is to return the maximum sum of all keys 
	of any sub-tree which is also a Binary Search Tree (BST). Assume a BST is 
	defined as follows:
	* The left subtree of a node contains only nodes with keys less than the node's key.
	* The right subtree of a node contains only nodes with keys greater than the node's key.
	* Both the left and right subtrees must also be binary search trees.

	Example 1:
	Input: root = [1,4,3,2,4,2,5,null,null,null,null,null,null,4,6]
	Output: 20
	Explanation: Maximum sum in a valid Binary search tree is obtained in root 
	             node with key equal to 3.

	Example 2:
	Input: root = [4,3,null,1,2]
	Output: 2
	Explanation: Maximum sum in a valid Binary search tree is obtained in a 
	             single root node with key equal to 2.

	Example 3:
	Input: root = [-4,-2,-5]
	Output: 0
	Explanation: All values are negatives. Return an empty BST.

	Example 4:
	Input: root = [2,1,3]
	Output: 6

	Example 5:
	Input: root = [5,4,8,3,null,6,3]
	Output: 7

	Constraints:
	* The given binary tree will have between 1 and 40000 nodes.
	* Each node's value is between [-4 * 10^4 , 4 * 10^4]."""

    def maxSumBST(self, root: TreeNode) -> int:
        
        def fn(node): 
            """Collect info while traversing the tree in post-order."""
            if not node: return True, inf, -inf, 0, 0 # bst flag | min | max | sum
            ltf, lmn, lmx, lsm, lval = fn(node.left)
            rtf, rmn, rmx, rsm, rval = fn(node.right)
            lmn = min(lmn, node.val)
            rmx = max(rmx, node.val)
            sm = lsm + rsm + node.val 
            if ltf and rtf and lmx < node.val < rmn: 
                return True, lmn, rmx, sm, max(lval, rval, sm)
            return False, lmn, rmx, sm, max(lval, rval)
        
        return fn(root)[-1]


    """1387. Sort Integers by The Power Value (Medium)
	The power of an integer x is defined as the number of steps needed to 
	transform x into 1 using the following steps:
	* if x is even then x = x / 2
	* if x is odd then x = 3 * x + 1
	For example, the power of x = 3 is 7 because 3 needs 7 steps to become 1 
	(3 --> 10 --> 5 --> 16 --> 8 --> 4 --> 2 --> 1). Given three integers lo, 
	hi and k. The task is to sort all integers in the interval [lo, hi] by the 
	power value in ascending order, if two or more integers have the same power 
	value sort them by ascending order. Return the k-th integer in the range 
	[lo, hi] sorted by the power value. Notice that for any integer x 
	(lo <= x <= hi) it is guaranteed that x will transform into 1 using these 
	steps and that the power of x is will fit in 32 bit signed integer.

	Example 1:
	Input: lo = 12, hi = 15, k = 2
	Output: 13
	Explanation: The power of 12 is 9 (12 --> 6 --> 3 --> 10 --> 5 --> 16 --> 8 --> 4 --> 2 --> 1)
	             The power of 13 is 9
	             The power of 14 is 17
	             The power of 15 is 17
	             The interval sorted by the power value [12,13,14,15]. For 
	             k = 2 answer is the second element which is 13. Notice that 12 
	             and 13 have the same power value and we sorted them in 
	             ascending order. Same for 14 and 15.

	Example 2:
	Input: lo = 1, hi = 1, k = 1
	Output: 1
	
	Example 3:
	Input: lo = 7, hi = 11, k = 4
	Output: 7
	Explanation: The power array corresponding to the interval [7, 8, 9, 10, 11] 
	             is [16, 3, 19, 6, 14]. The interval sorted by power is 
	             [8, 10, 11, 7, 9]. The fourth number in the sorted array is 7.
	
	Example 4:
	Input: lo = 10, hi = 20, k = 5
	Output: 13

	Example 5:
	Input: lo = 1, hi = 1000, k = 777
	Output: 570

	Constraints:
	* 1 <= lo <= hi <= 1000
	* 1 <= k <= hi - lo + 1"""

    def getKth(self, lo: int, hi: int, k: int) -> int:
        pq = [] # min heap (size hi - lo - k + 2)
        for x in range(lo, hi+1): 
            cnt, xx = 0, x
            while xx > 1: 
                xx = 3*xx + 1 if xx&1 else xx//2
                cnt += 1
            heappush(pq, (cnt, x))
            if len(pq) > hi - lo - k + 2: heappop(pq)
        return pq[0][1]


    """1395. Count Number of Teams (Medium)
	There are n soldiers standing in a line. Each soldier is assigned a unique 
	rating value. You have to form a team of 3 soldiers amongst them under the 
	following rules:
	* Choose 3 soldiers with index (i, j, k) with rating (rating[i], rating[j], rating[k]).
	* A team is valid if: (rating[i] < rating[j] < rating[k]) or (rating[i] > rating[j] > rating[k]) where (0 <= i < j < k < n).
	Return the number of teams you can form given the conditions. (soldiers can 
	be part of multiple teams).

	Example 1:
	Input: rating = [2,5,3,4,1]
	Output: 3
	Explanation: We can form three teams given the conditions. (2,3,4), (5,4,1), (5,3,1). 

	Example 2:
	Input: rating = [2,1,3]
	Output: 0
	Explanation: We can't form any team given the conditions.

	Example 3:
	Input: rating = [1,2,3,4]
	Output: 4

	Constraints:
	* n == rating.length
	* 3 <= n <= 1000
	* 1 <= rating[i] <= 10^5
	* All the integers in rating are unique."""

    def numTeams(self, rating: List[int]) -> int:
        ans = 0
        seen = [[0]*2 for _ in rating]
        for i in range(len(rating)): 
            for ii in range(i): 
                if rating[ii] < rating[i]: 
                    ans += seen[ii][0]
                    seen[i][0] += 1
                elif rating[ii] > rating[i]: 
                    ans += seen[ii][1]
                    seen[i][1] += 1
        return ans 


    """1400. Construct K Palindrome Strings (Medium)
	Given a string s and an integer k. You should construct k non-empty 
	palindrome strings using all the characters in s. Return True if you can 
	use all the characters in s to construct k palindrome strings or False 
	otherwise.

	Example 1:
	Input: s = "annabelle", k = 2
	Output: true
	Explanation: You can construct two palindromes using all characters in s. 
	             Some possible constructions "anna" + "elble", "anbna" + "elle", 
	             "anellena" + "b"

	Example 2:
	Input: s = "leetcode", k = 3
	Output: false
	Explanation: It is impossible to construct 3 palindromes using all the 
	             characters of s.
	
	Example 3:
	Input: s = "true", k = 4
	Output: true
	Explanation: The only possible solution is to put each character in a 
	             separate string.
	
	Example 4:
	Input: s = "yzyzyzyzyzyzyzy", k = 2
	Output: true
	Explanation: Simply you can put all z's in one string and all y's in the 
	             other string. Both strings will be palindrome.
	
	Example 5:
	Input: s = "cr", k = 7
	Output: false
	Explanation: We don't have enough characters in s to construct 7 palindromes.

	Constraints:
	* 1 <= s.length <= 10^5
	* All characters in s are lower-case English letters.
	* 1 <= k <= 10^5"""

    def canConstruct(self, s: str, k: int) -> bool:
        freq = {}
        for c in s: freq[c] = 1 + freq.get(c, 0)
        return sum(freq[c]&1 for c in freq) <= k <= len(s)


    """1403. Minimum Subsequence in Non-Increasing Order (Easy)
	Given the array nums, obtain a subsequence of the array whose sum of 
	elements is strictly greater than the sum of the non included elements in 
	such subsequence.  If there are multiple solutions, return the subsequence 
	with minimum size and if there still exist multiple solutions, return the 
	subsequence with the maximum total sum of all its elements. A subsequence 
	of an array can be obtained by erasing some (possibly zero) elements from 
	the array. Note that the solution with the given constraints is guaranteed 
	to be unique. Also return the answer sorted in non-increasing order.

	Example 1:
	Input: nums = [4,3,10,9,8]
	Output: [10,9] 
	Explanation: The subsequences [10,9] and [10,8] are minimal such that the 
	             sum of their elements is strictly greater than the sum of 
	             elements not included, however, the subsequence [10,9] has 
	             the maximum total sum of its elements. 

	Example 2:
	Input: nums = [4,4,7,6,7]
	Output: [7,7,6] 
	Explanation: The subsequence [7,7] has the sum of its elements equal to 14 
	             which is not strictly greater than the sum of elements not 
	             included (14 = 4 + 4 + 6). Therefore, the subsequence [7,6,7] 
	             is the minimal satisfying the conditions. Note the subsequence 
	             has to returned in non-decreasing order.  
	
	Example 3:
	Input: nums = [6]
	Output: [6]

	Constraints:
	* 1 <= nums.length <= 500
	* 1 <= nums[i] <= 100"""

    def minSubsequence(self, nums: List[int]) -> List[int]:
        ans = []
        total, sm = sum(nums), 0
        for x in sorted(nums, reverse=True):
            ans.append(x)
            sm += x
            if sm > total - sm: return ans 


    """1404. Number of Steps to Reduce a Number in Binary Representation to One(Medium)
	Given a number s in their binary representation. Return the number of steps 
	to reduce it to 1 under the following rules:
	* If the current number is even, you have to divide it by 2.
	* If the current number is odd, you have to add 1 to it.
	It's guaranteed that you can always reach to one for all testcases.

	Example 1:
	Input: s = "1101"
	Output: 6
	Explanation: "1101" corressponds to number 13 in their decimal representation.
	Step 1) 13 is odd, add 1 and obtain 14. 
	Step 2) 14 is even, divide by 2 and obtain 7.
	Step 3) 7 is odd, add 1 and obtain 8.
	Step 4) 8 is even, divide by 2 and obtain 4.  
	Step 5) 4 is even, divide by 2 and obtain 2. 
	Step 6) 2 is even, divide by 2 and obtain 1.  

	Example 2:
	Input: s = "10"
	Output: 1
	Explanation: "10" corressponds to number 2 in their decimal representation.
	Step 1) 2 is even, divide by 2 and obtain 1.  

	Example 3:
	Input: s = "1"
	Output: 0

	Constraints:
	* 1 <= s.length <= 500
	* s consists of characters '0' or '1'
	* s[0] == '1'"""

    def numSteps(self, s: str) -> int:
        n = int(s, 2)
        ans = 0
        while n > 1: 
            ans += 1
            if n&1: n += 1
            else: n //= 2
        return ans 


    """1405. Longest Happy String (Medium)
	A string is called happy if it does not have any of the strings 'aaa', 'bbb' 
	or 'ccc' as a substring. Given three integers a, b and c, return any string 
	s, which satisfies following conditions:
	* s is happy and longest possible.
	* s contains at most a occurrences of the letter 'a', at most b occurrences 
	  of the letter 'b' and at most c occurrences of the letter 'c'.
	* s will only contain 'a', 'b' and 'c' letters.
	If there is no such string s return the empty string "".

	Example 1:
	Input: a = 1, b = 1, c = 7
	Output: "ccaccbcc"
	Explanation: "ccbccacc" would also be a correct answer.

	Example 2:
	Input: a = 2, b = 2, c = 1
	Output: "aabbc"

	Example 3:
	Input: a = 7, b = 1, c = 0
	Output: "aabaa"
	Explanation: It's the only correct answer in this case.

	Constraints:
	* 0 <= a, b, c <= 100
	* a + b + c > 0"""

    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        pq = [] # max-heap 
        for x, c in zip((a, b, c), "abc"): 
            if x: heappush(pq, (-x, c))
        
        ans = []
        while pq: 
            n, x = heappop(pq)
            if ans[-2:] != [x, x]: 
                ans.append(x)
                if n+1: heappush(pq, (n+1, x))
            else: 
                if not pq: break 
                nn, xx = heappop(pq)
                ans.append(xx)
                if nn+1: heappush(pq, (nn+1, xx))
                heappush(pq, (n, x))
        return "".join(ans)


    """1406. Stone Game III (Hard)
	Alice and Bob continue their games with piles of stones. There are several 
	stones arranged in a row, and each stone has an associated value which is 
	an integer given in the array stoneValue. Alice and Bob take turns, with 
	Alice starting first. On each player's turn, that player can take 1, 2 or 3 
	stones from the first remaining stones in the row. The score of each player 
	is the sum of values of the stones taken. The score of each player is 0 
	initially. The objective of the game is to end with the highest score, and 
	the winner is the player with the highest score and there could be a tie. 
	The game continues until all the stones have been taken. Assume Alice and 
	Bob play optimally. Return "Alice" if Alice will win, "Bob" if Bob will win 
	or "Tie" if they end the game with the same score.

	Example 1:
	Input: values = [1,2,3,7]
	Output: "Bob"
	Explanation: Alice will always lose. Her best move will be to take three 
	             piles and the score become 6. Now the score of Bob is 7 and 
	             Bob wins.

	Example 2:
	Input: values = [1,2,3,-9]
	Output: "Alice"
	Explanation: Alice must choose all the three piles at the first move to win 
	             and leave Bob with negative score. If Alice chooses one pile 
	             her score will be 1 and the next move Bob's score becomes 5. 
	             The next move Alice will take the pile with value = -9 and 
	             lose. If Alice chooses two piles her score will be 3 and the 
	             next move Bob's score becomes 3. The next move Alice will take 
	             the pile with value = -9 and also lose. Remember that both 
	             play optimally so here Alice will choose the scenario that 
	             makes her win.
	
	Example 3:
	Input: values = [1,2,3,6]
	Output: "Tie"
	Explanation: Alice cannot win this game. She can end the game in a draw if she decided to choose all the first three piles, otherwise she will lose.

	Example 4:
	Input: values = [1,2,3,-1,-2,-3,7]
	Output: "Alice"

	Example 5:
	Input: values = [-1,-2,-3]
	Output: "Tie"

	Constraints:
	* 1 <= values.length <= 50000
	* -1000 <= values[i] <= 1000"""

    def stoneGameIII(self, stoneValue: List[int]) -> str:
        
        @cache
        def fn(i): 
            """Return max value obtained from stoneValue[i:]."""
            if i >= len(stoneValue): return 0 
            ans = -inf
            for ii in range(i, i+3): 
                ans = max(ans, sum(stoneValue[i:ii+1]) - fn(ii+1))
            return ans 
        
        ans = fn(0)
        if ans > 0: return "Alice"
        if ans == 0: return "Tie"
        return "Bob"


    """1413. Minimum Value to Get Positive Step by Step Sum (Easy)
	Given an array of integers nums, you start with an initial positive value 
	startValue. In each iteration, you calculate the step by step sum of 
	startValue plus elements in nums (from left to right). Return the minimum 
	positive value of startValue such that the step by step sum is never less 
	than 1.

	Example 1:
	Input: nums = [-3,2,-3,4,2]
	Output: 5
	Explanation: If you choose startValue = 4, in the third iteration your step 
	             by step sum is less than 1.
                 step by step sum
                 startValue = 4 | startValue = 5 | nums
                   (4 -3 ) = 1  | (5 -3 ) = 2    |  -3
                   (1 +2 ) = 3  | (2 +2 ) = 4    |   2
                   (3 -3 ) = 0  | (4 -3 ) = 1    |  -3
                   (0 +4 ) = 4  | (1 +4 ) = 5    |   4
                   (4 +2 ) = 6  | (5 +2 ) = 7    |   2

	Example 2:
	Input: nums = [1,2]
	Output: 1
	Explanation: Minimum start value should be positive. 
	
	Example 3:
	Input: nums = [1,-2,-3]
	Output: 5

	Constraints:
	* 1 <= nums.length <= 100
	* -100 <= nums[i] <= 100"""

    def minStartValue(self, nums: List[int]) -> int:
        ans = prefix = 0
        for x in nums: 
            prefix += x
            ans = min(ans, prefix)
        return 1 - ans


    """1414. Find the Minimum Number of Fibonacci Numbers Whose Sum Is K (Medium)
	Given an integer k, return the minimum number of Fibonacci numbers whose 
	sum is equal to k. The same Fibonacci number can be used multiple times. 
	The Fibonacci numbers are defined as:
	F1 = 1
	F2 = 1
	Fn = Fn-1 + Fn-2 for n > 2.
	It is guaranteed that for the given constraints we can always find such 
	Fibonacci numbers that sum up to k.

	Example 1:
	Input: k = 7
	Output: 2 
	Explanation: The Fibonacci numbers are: 1, 1, 2, 3, 5, 8, 13, ... For k = 7 
	             we can use 2 + 5 = 7.

	Example 2:
	Input: k = 10
	Output: 2 
	Explanation: For k = 10 we can use 2 + 8 = 10.
	
	Example 3:
	Input: k = 19
	Output: 3 
	Explanation: For k = 19 we can use 1 + 5 + 13 = 19.

	Constraints: 1 <= k <= 10^9"""

    def findMinFibonacciNumbers(self, k: int) -> int:
        fibo = [1]
        f0 = f1 = 1
        while f1 < k: 
            f0, f1 = f1, f0+f1
            fibo.append(f1)
        
        ans = 0
        while k: 
            ans += 1
            i = bisect_right(fibo, k) - 1
            k -= fibo[i]
        return ans 


    """1415. The k-th Lexicographical String of All Happy Strings of Length n (Medium)
	A happy string is a string that:
	* consists only of letters of the set ['a', 'b', 'c'].
	* s[i] != s[i + 1] for all values of i from 1 to s.length - 1 (string is 1-indexed).
	For example, strings "abc", "ac", "b" and "abcbabcbcb" are all happy strings 
	and strings "aa", "baa" and "ababbc" are not happy strings. Given two 
	integers n and k, consider a list of all happy strings of length n sorted 
	in lexicographical order. Return the kth string of this list or return an 
	empty string if there are less than k happy strings of length n.

	Example 1:
	Input: n = 1, k = 3
	Output: "c"
	Explanation: The list ["a", "b", "c"] contains all happy strings of length 
	             1. The third string is "c".

	Example 2:
	Input: n = 1, k = 4
	Output: ""
	Explanation: There are only 3 happy strings of length 1.
	
	Example 3:
	Input: n = 3, k = 9
	Output: "cab"
	Explanation: There are 12 different happy string of length 3 
	             ["aba", "abc", "aca", "acb", "bab", "bac", 
	              "bca", "bcb", "cab", "cac", "cba", "cbc"]. 
	              You will find the 9th string = "cab"

	Example 4:
	Input: n = 2, k = 7
	Output: ""
	
	Example 5:
	Input: n = 10, k = 100
	Output: "abacbabacb"
	 
	Constraints:
	* 1 <= n <= 10
	* 1 <= k <= 100"""

    def getHappyString(self, n: int, k: int) -> str:
        k -= 1
        if 3*2**(n-1) <= k: return "" # impossible
        
        mp = {"": "abc", "a": "bc", "b": "ac", "c": "ab"}
        ans = [""]
        for i in range(n): 
            q, k = divmod(k, 2**(n-i-1))
            ans.append(mp[ans[-1]][q])
        return "".join(ans)


    """1416. Restore The Array (Hard)
	A program was supposed to print an array of integers. The program forgot to 
	print whitespaces and the array is printed as a string of digits and all we 
	know is that all integers in the array were in the range [1, k] and there 
	are no leading zeros in the array. Given the string s and the integer k. 
	There can be multiple ways to restore the array. Return the number of 
	possible array that can be printed as a string s using the mentioned 
	program. The number of ways could be very large so return it modulo 
	10^9 + 7.

	Example 1:
	Input: s = "1000", k = 10000
	Output: 1
	Explanation: The only possible array is [1000]

	Example 2:
	Input: s = "1000", k = 10
	Output: 0
	Explanation: There cannot be an array that was printed this way and has all 
	             integer >= 1 and <= 10.

	Example 3:
	Input: s = "1317", k = 2000
	Output: 8
	Explanation: Possible arrays are [1317],[131,7],[13,17],[1,317],[13,1,7],[1,31,7],[1,3,17],[1,3,1,7]
	
	Example 4:
	Input: s = "2020", k = 30
	Output: 1
	Explanation: The only possible array is [20,20]. [2020] is invalid because 
	             2020 > 30. [2,020] is ivalid because 020 contains leading zeros.
	
	Example 5:
	Input: s = "1234567890", k = 90
	Output: 34

	Constraints:
	* 1 <= s.length <= 10^5.
	* s consists of only digits and doesn't contain leading zeros.
	* 1 <= k <= 10^9."""

    def numberOfArrays(self, s: str, k: int) -> int:
        dp = [0]*(len(s)+1)
        dp[-1] = sm = 1 
        
        ii = len(s)
        for i in reversed(range(len(s))): 
            if s[i] != "0": 
                while ii - i - 1 > log10(k) or int(s[i:ii]) > k: 
                    sm = (sm - dp[ii]) % 1_000_000_007
                    ii -= 1
                dp[i] = sm
                sm = (sm + dp[i]) % 1_000_000_007
        return dp[0]


    """1417. Reformat The String (Easy)
	Given alphanumeric string s. (Alphanumeric string is a string consisting of 
	lowercase English letters and digits). You have to find a permutation of 
	the string where no letter is followed by another letter and no digit is 
	followed by another digit. That is, no two adjacent characters have the 
	same type. Return the reformatted string or return an empty string if it is 
	impossible to reformat the string.

	Example 1:
	Input: s = "a0b1c2"
	Output: "0a1b2c"
	Explanation: No two adjacent characters have the same type in "0a1b2c". 
	             "a0b1c2", "0a1b2c", "0c2a1b" are also valid permutations.

	Example 2:
	Input: s = "leetcode"
	Output: ""
	Explanation: "leetcode" has only characters so we cannot separate them by 
	             digits.
	
	Example 3:
	Input: s = "1229857369"
	Output: ""
	Explanation: "1229857369" has only digits so we cannot separate them by 
	             characters.
	
	Example 4:
	Input: s = "covid2019" 
	Output: "c2o0v1i9d"
	
	Example 5:
	Input: s = "ab123"
	Output: "1a2b3"

	Constraints:
	* 1 <= s.length <= 500
	* s consists of only lowercase English letters and/or digits."""

    def reformat(self, s: str) -> str:
        alpha, digit = [], []
        for c in s:
            if c.isalpha(): alpha.append(c)
            else: digit.append(c)
        if len(alpha) < len(digit): alpha, digit = digit, alpha
        if len(alpha) - len(digit) > 1: return "" # impossible
        return "".join(x+y for x, y in zip_longest(alpha, digit, fillvalue=""))


    """1418. Display Table of Food Orders in a Restaurant (Medium)
	Given the array orders, which represents the orders that customers have 
	done in a restaurant. More specifically 
	orders[i]=[customerNamei,tableNumberi,foodItemi] where customerNamei is the 
	name of the customer, tableNumberi is the table customer sit at, and 
	foodItemi is the item customer orders. Return the restaurant's “display 
	table”. The “display table” is a table whose row entries denote how many of 
	each food item each table ordered. The first column is the table number and 
	the remaining columns correspond to each food item in alphabetical order. 
	The first row should be a header whose first column is “Table”, followed by 
	the names of the food items. Note that the customer names are not part of 
	the table. Additionally, the rows should be sorted in numerically 
	increasing order.

	Example 1:
	Input: orders = [["David", "3", "Ceviche"      ],
	                 ["Corina","10","Beef Burrito" ],
	                 ["David", "3", "Fried Chicken"],
	                 ["Carla", "5", "Water"        ],
	                 ["Carla", "5", "Ceviche"      ],
	                 ["Rous",  "3", "Ceviche"      ]]
	Output: [["Table","Beef Burrito","Ceviche","Fried Chicken","Water"],["3","0","2","1","0"],["5","0","1","0","1"],["10","1","0","0","0"]] 
	Explanation:
	The displaying table looks like:
	Table,Beef Burrito,Ceviche,Fried Chicken,Water
	3    ,0           ,2      ,1            ,0
	5    ,0           ,1      ,0            ,1
	10   ,1           ,0      ,0            ,0
	For the table 3: David orders "Ceviche" and "Fried Chicken", and Rous orders "Ceviche".
	For the table 5: Carla orders "Water" and "Ceviche".
	For the table 10: Corina orders "Beef Burrito". 

	Example 2:
	Input: orders = [["James",  "12","Fried Chicken"   ],
	                 ["Ratesh", "12","Fried Chicken"   ],
	                 ["Amadeus","12","Fried Chicken"   ],
	                 ["Adam",   "1", "Canadian Waffles"],
	                 ["Brianna","1", "Canadian Waffles"]]
	Output: [["Table","Canadian Waffles","Fried Chicken"],["1","2","0"],["12","0","3"]] 
	Explanation: 
	For the table 1: Adam and Brianna order "Canadian Waffles".
	For the table 12: James, Ratesh and Amadeus order "Fried Chicken".

	Example 3:
	Input: orders = [["Laura",  "2","Bean Burrito"],
	                 ["Jhon",   "2","Beef Burrito"],
	                 ["Melissa","2","Soda"        ]]
	Output: [["Table","Bean Burrito","Beef Burrito","Soda"],["2","1","1","1"]]

	Constraints:
	* 1 <= orders.length <= 5 * 10^4
	* orders[i].length == 3
	* 1 <= customerNamei.length, foodItemi.length <= 20
	* customerNamei and foodItemi consist of lowercase and uppercase English letters and the space character.
	* tableNumberi is a valid integer between 1 and 500."""

    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        freq = {} 
        foods = set()
        
        for _, table, food in orders: 
            freq.setdefault(table, defaultdict(int))[food] += 1
            foods.add(food)
        
        foods = sorted(foods)
        ans = [["Table"] + foods]
        for k in sorted(freq, key=int): 
            row = [k]
            for food in foods: 
                row.append(str(freq[k][food]))
            ans.append(row)
        return ans 


    """1419. Minimum Number of Frogs Croaking (Medium)
	Given the string croakOfFrogs, which represents a combination of the string 
	"croak" from different frogs, that is, multiple frogs can croak at the same 
	time, so multiple “croak” are mixed. Return the minimum number of different 
	frogs to finish all the croak in the given string. A valid "croak" means a 
	frog is printing 5 letters ‘c’, ’r’, ’o’, ’a’, ’k’ sequentially. The frogs 
	have to print all five letters to finish a croak. If the given string is 
	not a combination of valid "croak" return -1.

	Example 1:
	Input: croakOfFrogs = "croakcroak"
	Output: 1 
	Explanation: One frog yelling "croak" twice.

	Example 2:
	Input: croakOfFrogs = "crcoakroak"
	Output: 2 
	Explanation: The minimum number of frogs is two. The first frog could yell 
	             "crcoakroak". The second frog could yell later "crcoakroak".

	Example 3:
	Input: croakOfFrogs = "croakcrook"
	Output: -1
	Explanation: The given string is an invalid combination of "croak" from 
	             different frogs.
	
	Example 4:
	Input: croakOfFrogs = "croakcroa"
	Output: -1

	Constraints:
	* 1 <= croakOfFrogs.length <= 10^5
	* All characters in the string are: 'c', 'r', 'o', 'a' or 'k'."""

    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        ans = 0
        freq = [0]*5 # freq array 
        for c in croakOfFrogs: 
            i = "croak".index(c)
            freq[i] += 1 
            if i and freq[i-1] < freq[i]: return -1 
            if c == "k": 
                ans = max(ans, freq[0])
                for i in range(5): freq[i] -= 1
        if max(freq) == 0: return ans
        return -1


    """1420. Build Array Where You Can Find The Maximum Exactly K Comparisons (Hard)
	Given three integers n, m and k. Consider the following algorithm to find 
	the maximum element of an array of positive integers:
	
	maximum_value = -1
	maximum_index = -1
	seach_cost = 0
	n = arr.length
	for (i = 0; i < n; i++) {
		if (maximum_value < arr[i]) {
			maximum_value = arr[i]
			maximum_index = i
			search_cost = search_cost + 1
		}
	}
	return search_cost

	You should build the array arr which has the following properties:
	* arr has exactly n integers.
	* 1 <= arr[i] <= m where (0 <= i < n).
	* After applying the mentioned algorithm to arr, the value search_cost is 
	  equal to k.
	Return the number of ways to build the array arr under the mentioned 
	conditions. As the answer may grow large, the answer must be computed 
	modulo 10^9 + 7.

	Example 1:
	Input: n = 2, m = 3, k = 1
	Output: 6
	Explanation: The possible arrays are [1, 1], [2, 1], [2, 2], [3, 1], [3, 2] [3, 3]

	Example 2:
	Input: n = 5, m = 2, k = 3
	Output: 0
	Explanation: There are no possible arrays that satisify the mentioned conditions.

	Example 3:
	Input: n = 9, m = 1, k = 1
	Output: 1
	Explanation: The only possible array is [1, 1, 1, 1, 1, 1, 1, 1, 1]

	Example 4:
	Input: n = 50, m = 100, k = 25
	Output: 34549172
	Explanation: Don't forget to compute the answer modulo 1000000007

	Example 5:
	Input: n = 37, m = 17, k = 7
	Output: 418930126

	Constraints:
	* 1 <= n <= 50
	* 1 <= m <= 100
	* 0 <= k <= n"""

    def numOfArrays(self, n: int, m: int, k: int) -> int:
        
        @cache
        def fn(i, x, k): 
            """Return number of ways to build arr[i:] with current max at x and remaining cost at k."""
            if n - i < k: return 0 # impossible 
            if m - x < k: return 0 # impossible 
            if k == 0: return x**(n-i)
            return x*fn(i+1, x, k) + fn(i+1, x+1, k-1) + fn(i, x+1, k) - (x+1)*fn(i+1, x+1, k)
        
        return fn(0, 0, k) % 1_000_000_007


    """1426. Counting Elements (Easy)
	Given an integer array arr, count how many elements x there are, such that 
	x + 1 is also in arr. If there're duplicates in arr, count them seperately.

	Example 1:
	Input: arr = [1,2,3]
	Output: 2
	Explanation: 1 and 2 are counted cause 2 and 3 are in arr.

	Example 2:
	Input: arr = [1,1,3,3,5,5,7,7]
	Output: 0
	Explanation: No numbers are counted, cause there's no 2, 4, 6, or 8 in arr.

	Example 3:
	Input: arr = [1,3,2,3,5,0]
	Output: 3
	Explanation: 0, 1 and 2 are counted cause 1, 2 and 3 are in arr.

	Example 4:
	Input: arr = [1,1,2,2]
	Output: 2
	Explanation: Two 1s are counted cause 2 is in arr.

	Example 5:
	Input: arr = [1,1,2]
	Output: 2
	Explanation: Both 1s are counted because 2 is in the array.

	Constraints:
	* 1 <= arr.length <= 1000
	* 0 <= arr[i] <= 1000"""

    def countElements(self, arr: List[int]) -> int:
        freq = {}
        for x in arr: freq[x] = freq.get(x, 0) + 1
        return sum(v for k, v in freq.items() if k + 1 in freq) 


    """1427. Perform String Shifts (Easy)
	You are given a string s containing lowercase English letters, and a matrix 
	shift, where shift[i] = [direction, amount]:
	* direction can be 0 (for left shift) or 1 (for right shift). 
	* amount is the amount by which string s is to be shifted.
	* A left shift by 1 means remove the first character of s and append it to 
	  the end.
	* Similarly, a right shift by 1 means remove the last character of s and 
	  add it to the beginning.
	Return the final string after all operations.

	Example 1:
	Input: s = "abc", shift = [[0,1],[1,2]]
	Output: "cab"
	Explanation: [0,1] means shift to left by 1. "abc" -> "bca"
	             [1,2] means shift to right by 2. "bca" -> "cab"
	
	Example 2:
	Input: s = "abcdefg", shift = [[1,1],[1,1],[0,2],[1,3]]
	Output: "efgabcd"
	Explanation: [1,1] means shift to right by 1. "abcdefg" -> "gabcdef"
	             [1,1] means shift to right by 1. "gabcdef" -> "fgabcde"
	             [0,2] means shift to left by 2. "fgabcde" -> "abcdefg"
	             [1,3] means shift to right by 3. "abcdefg" -> "efgabcd"
	 
	Constraints:
	* 1 <= s.length <= 100
	* s only contains lower case English letters.
	* 1 <= shift.length <= 100
	* shift[i].length == 2
	* 0 <= shift[i][0] <= 1
	* 0 <= shift[i][1] <= 100"""

    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        amount = 0
        for d, x in shift: 
            amount += x if d == 0 else -x
        amount %= len(s)
        return s[amount:] + s[:amount]


    """1446. Consecutive Characters (Easy)
	Given a string s, the power of the string is the maximum length of a non-
	empty substring that contains only one unique character. Return the power 
	of the string.

	Example 1:
	Input: s = "leetcode"
	Output: 2
	Explanation: The substring "ee" is of length 2 with the character 'e' only.

	Example 2:
	Input: s = "abbcccddddeeeeedcba"
	Output: 5
	Explanation: The substring "eeeee" is of length 5 with the character 'e' only.

	Example 3:
	Input: s = "triplepillooooow"
	Output: 5

	Example 4:
	Input: s = "hooraaaaaaaaaaay"
	Output: 11

	Example 5:
	Input: s = "tourist"
	Output: 1

	Constraints:
	* 1 <= s.length <= 500
	* s contains only lowercase English letters."""

    def maxPower(self, s: str) -> int:
        ans = 0
        for i in range(len(s)):
            if not i or s[i-1] != s[i]: cnt = 0
            cnt += 1
            ans = max(ans, cnt)
        return ans 


    """1447. Simplified Fractions (Medium)
	Given an integer n, return a list of all simplified fractions between 0 and 
	1 (exclusive) such that the denominator is less-than-or-equal-to n. The 
	fractions can be in any order.

	Example 1:
	Input: n = 2
	Output: ["1/2"]
	Explanation: "1/2" is the only unique fraction with a denominator less-than-
	             or-equal-to 2.

	Example 2:
	Input: n = 3
	Output: ["1/2","1/3","2/3"]
	
	Example 3:
	Input: n = 4
	Output: ["1/2","1/3","1/4","2/3","3/4"]
	Explanation: "2/4" is not a simplified fraction because it can be 
	             simplified to "1/2".

	Example 4:
	Input: n = 1
	Output: []

	Constraints: 1 <= n <= 100"""

    def simplifiedFractions(self, n: int) -> List[str]:
        ans = []
        for d in range(2, n+1): 
            for n in range(1, d):
                if gcd(d, n) == 1: ans.append(str(n) + "/" + str(d))
        return ans 


    """1448. Count Good Nodes in Binary Tree (Medium)
	Given a binary tree root, a node X in the tree is named good if in the path 
	from root to X there are no nodes with a value greater than X. Return the 
	number of good nodes in the binary tree.

	Example 1:
	Input: root = [3,1,4,3,null,1,5]
	Output: 4
	Explanation: Nodes in blue are good.
	Root Node (3) is always a good node.
	Node 4 -> (3,4) is the maximum value in the path starting from the root.
	Node 5 -> (3,4,5) is the maximum value in the path
	Node 3 -> (3,1,3) is the maximum value in the path.

	Example 2:
	Input: root = [3,3,null,4,2]
	Output: 3
	Explanation: Node 2 -> (3, 3, 2) is not good, because "3" is higher than it.

	Example 3:
	Input: root = [1]
	Output: 1
	Explanation: Root is considered as good.

	Constraints:
	* The number of nodes in the binary tree is in the range [1, 10^5].
	* Each node's value is between [-10^4, 10^4]."""

    def goodNodes(self, root: TreeNode) -> int:
        ans = 0 
        stack = [(root, -inf)]
        while stack: 
            node, val = stack.pop()
            if node: 
                if node.val >= val: ans += 1
                val = max(val, node.val)
                stack.append((node.left, val))
                stack.append((node.right, val))
        return ans 


    """1449. Form Largest Integer With Digits That Add up to Target (Hard)
	Given an array of integers cost and an integer target. Return the maximum 
	integer you can paint under the following rules:
	* The cost of painting a digit (i+1) is given by cost[i] (0 indexed).
	* The total cost used must be equal to target.
	* Integer does not have digits 0.
	Since the answer may be too large, return it as string. If there is no way 
	to paint any integer given the condition, return "0".

	Example 1:
	Input: cost = [4,3,2,5,6,7,2,5,5], target = 9
	Output: "7772"
	Explanation:  The cost to paint the digit '7' is 2, and the digit '2' is 3. 
	              Then cost("7772") = 2*3+ 3*1 = 9. You could also paint "977", 
	              but "7772" is the largest number.
	Digit    cost
	  1  ->   4
	  2  ->   3
	  3  ->   2
	  4  ->   5
	  5  ->   6
	  6  ->   7
	  7  ->   2
	  8  ->   5
	  9  ->   5
	
	Example 2:
	Input: cost = [7,6,5,5,5,6,8,7,8], target = 12
	Output: "85"
	Explanation: The cost to paint the digit '8' is 7, and the digit '5' is 5. 
	             Then cost("85") = 7 + 5 = 12.

	Example 3:
	Input: cost = [2,4,6,2,4,6,4,4,4], target = 5
	Output: "0"
	Explanation: It's not possible to paint any integer with total cost equal to target.
	
	Example 4:
	Input: cost = [6,10,15,40,40,40,40,40,40], target = 47
	Output: "32211"
	 
	Constraints:
	* cost.length == 9
	* 1 <= cost[i] <= 5000
	* 1 <= target <= 5000"""

    def largestNumber(self, cost: List[int], target: int) -> str:
        
        @cache
        def fn(x): 
            """Return max integer given target x."""
            if x == 0: return 0
            if x < 0: return -inf 
            return max(fn(x - c) * 10 + i + 1 for i, c in enumerate(cost))
        
        return str(max(0, fn(target)))


    """1455. Check If a Word Occurs As a Prefix of Any Word in a Sentence (Easy)
	Given a sentence that consists of some words separated by a single space, 
	and a searchWord. You have to check if searchWord is a prefix of any word 
	in sentence. Return the index of the word in sentence where searchWord is a 
	prefix of this word (1-indexed). If searchWord is a prefix of more than one 
	word, return the index of the first word (minimum index). If there is no 
	such word return -1. A prefix of a string S is any leading contiguous 
	substring of S.

	Example 1:
	Input: sentence = "i love eating burger", searchWord = "burg"
	Output: 4
	Explanation: "burg" is prefix of "burger" which is the 4th word in the sentence.

	Example 2:
	Input: sentence = "this problem is an easy problem", searchWord = "pro"
	Output: 2
	Explanation: "pro" is prefix of "problem" which is the 2nd and the 6th word 
	             in the sentence, but we return 2 as it's the minimal index.
	
	Example 3:
	Input: sentence = "i am tired", searchWord = "you"
	Output: -1
	Explanation: "you" is not a prefix of any word in the sentence.
	
	Example 4:
	Input: sentence = "i use triple pillow", searchWord = "pill"
	Output: 4

	Example 5:
	Input: sentence = "hello from the other side", searchWord = "they"
	Output: -1

	Constraints:
	* 1 <= sentence.length <= 100
	* 1 <= searchWord.length <= 10
	* sentence consists of lowercase English letters and spaces.
	* searchWord consists of lowercase English letters."""

    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        for i, word in enumerate(sentence.split()):
            if word.startswith(searchWord): return i+1
        return -1 


    """1456. Maximum Number of Vowels in a Substring of Given Length (Medium)
	Given a string s and an integer k. Return the maximum number of vowel 
	letters in any substring of s with length k. Vowel letters in English are 
	(a, e, i, o, u).

	Example 1:
	Input: s = "abciiidef", k = 3
	Output: 3
	Explanation: The substring "iii" contains 3 vowel letters.

	Example 2:
	Input: s = "aeiou", k = 2
	Output: 2
	Explanation: Any substring of length 2 contains 2 vowels.

	Example 3:
	Input: s = "leetcode", k = 3
	Output: 2
	Explanation: "lee", "eet" and "ode" contain 2 vowels.

	Example 4:
	Input: s = "rhythms", k = 4
	Output: 0
	Explanation: We can see that s doesn't have any vowel letters.

	Example 5:
	Input: s = "tryhard", k = 4
	Output: 1

	Constraints:
	* 1 <= s.length <= 10^5
	* s consists of lowercase English letters.
	* 1 <= k <= s.length"""

    def maxVowels(self, s: str, k: int) -> int:
        ans = cnt = 0
        for i in range(len(s)): 
            if s[i] in "aeiou": cnt += 1
            if i >= k and s[i-k] in "aeiou": cnt -= 1
            ans = max(ans, cnt)
        return ans 


    """1457. Pseudo-Palindromic Paths in a Binary Tree (Medium)
	Given a binary tree where node values are digits from 1 to 9. A path in the 
	binary tree is said to be pseudo-palindromic if at least one permutation of 
	the node values in the path is a palindrome. Return the number of pseudo-
	palindromic paths going from the root node to leaf nodes.

	Example 1:
	Input: root = [2,3,1,3,1,null,1]
	Output: 2 
	Explanation: The figure above represents the given binary tree. There are 
	             three paths going from the root node to leaf nodes: the red 
	             path [2,3,3], the green path [2,1,1], and the path [2,3,1]. 
	             Among these paths only red path and green path are pseudo-
	             palindromic paths since the red path [2,3,3] can be rearranged 
	             in [3,2,3] (palindrome) and the green path [2,1,1] can be 
	             rearranged in [1,2,1] (palindrome).

	Example 2:
	Input: root = [2,1,1,1,3,null,null,null,null,null,1]
	Output: 1 
	Explanation: The figure above represents the given binary tree. There are 
	             three paths going from the root node to leaf nodes: the green 
	             path [2,1,1], the path [2,1,3,1], and the path [2,1]. Among 
	             these paths only the green path is pseudo-palindromic since 
	             [2,1,1] can be rearranged in [1,2,1] (palindrome).
	
	Example 3:
	Input: root = [9]
	Output: 1

	Constraints:
	* The number of nodes in the tree is in the range [1, 10^5].
	* 1 <= Node.val <= 9"""

    def pseudoPalindromicPaths (self, root: TreeNode) -> int:
        
        def fn(node, mask): 
            """Post-order traverse the tree and update ans."""
            if not node: return 0 
            mask ^= 1 << node.val
            if not node.left and not node.right: # leaf node 
                return 1 if mask & (mask-1) == 0 else 0
            return fn(node.left, mask) + fn(node.right, mask)
        
        return fn(root, 0)


    """1458. Max Dot Product of Two Subsequences (Hard)
	Given two arrays nums1 and nums2. Return the maximum dot product between 
	non-empty subsequences of nums1 and nums2 with the same length. A 
	subsequence of a array is a new array which is formed from the original 
	array by deleting some (can be none) of the characters without disturbing 
	the relative positions of the remaining characters. (ie, [2,3,5] is a 
	subsequence of [1,2,3,4,5] while [1,5,3] is not).

	Example 1:
	Input: nums1 = [2,1,-2,5], nums2 = [3,0,-6]
	Output: 18
	Explanation: Take subsequence [2,-2] from nums1 and subsequence [3,-6] from 
	             nums2. Their dot product is (2*3 + (-2)*(-6)) = 18.

	Example 2:
	Input: nums1 = [3,-2], nums2 = [2,-6,7]
	Output: 21
	Explanation: Take subsequence [3] from nums1 and subsequence [7] from nums2.
	             Their dot product is (3*7) = 21.
	
	Example 3:
	Input: nums1 = [-1,-1], nums2 = [1,1]
	Output: -1
 	Explanation: Take subsequence [-1] from nums1 and subsequence [1] from nums2.
 	             Their dot product is -1.

	Constraints:
	* 1 <= nums1.length, nums2.length <= 500
	* -1000 <= nums1[i], nums2[i] <= 1000"""

    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        
        @cache
        def fn(i, j): 
            """Return max dot product of nums1[i:] and nums2[j:]."""
            if i == len(nums1) or j == len(nums2): return -inf
            return max(nums1[i]*nums2[j] + fn(i+1, j+1), nums1[i]*nums2[j], fn(i+1, j), fn(i, j+1))
        
        return fn(0, 0)


    """1469. Find All The Lonely Nodes (Easy)
	In a binary tree, a lonely node is a node that is the only child of its 
	parent node. The root of the tree is not lonely because it does not have a 
	parent node. Given the root of a binary tree, return an array containing 
	the values of all lonely nodes in the tree. Return the list in any order.

	Example 1:
	Input: root = [1,2,3,null,4]
	Output: [4]
	Explanation: Light blue node is the only lonely node. Node 1 is the root 
	             and is not lonely. Nodes 2 and 3 have the same parent and are 
	             not lonely.

	Example 2:
	Input: root = [7,1,4,6,null,5,3,null,null,null,null,null,2]
	Output: [6,2]
	Explanation: Light blue nodes are lonely nodes. Please remember that order 
	             doesn't matter, [2,6] is also an acceptable answer.

	Example 3:
	Input: root = [11,99,88,77,null,null,66,55,null,null,44,33,null,null,22]
	Output: [77,55,33,66,44,22]
	Explanation: Nodes 99 and 88 share the same parent. Node 11 is the root. 
	             All other nodes are lonely.

	Example 4:
	Input: root = [197]
	Output: []

	Example 5:
	Input: root = [31,null,78,null,28]
	Output: [78,28]

	Constraints:
	* The number of nodes in the tree is in the range [1, 1000].
	* Each node's value is between [1, 10^6]."""

    def getLonelyNodes(self, root: TreeNode) -> List[int]:
        ans = []
        stack = [root]
        while stack: 
            node = stack.pop()
            if node.left: 
                stack.append(node.left)
                if not node.right: ans.append(node.left.val)
            if node.right: 
                stack.append(node.right)
                if not node.left: ans.append(node.right.val)
        return ans 


    """1474. Delete N Nodes After M Nodes of a Linked List (Easy)
	Given the head of a linked list and two integers m and n. Traverse the 
	linked list and remove some nodes in the following way:
	* Start with the head as the current node.
	* Keep the first m nodes starting with the current node.
	* Remove the next n nodes
	* Keep repeating steps 2 and 3 until you reach the end of the list.
	Return the head of the modified list after removing the mentioned nodes. 
	Follow up question: How can you solve this problem by modifying the list 
	in-place?

	Example 1:
	Input: head = [1,2,3,4,5,6,7,8,9,10,11,12,13], m = 2, n = 3
	Output: [1,2,6,7,11,12]
	Explanation: Keep the first (m = 2) nodes starting from the head of the 
	             linked List  (1 ->2) show in black nodes. Delete the next 
	             (n = 3) nodes (3 -> 4 -> 5) show in read nodes. Continue with 
	             the same procedure until reaching the tail of the Linked List. 
	             Head of linked list after removing nodes is returned.

	Example 2:
	Input: head = [1,2,3,4,5,6,7,8,9,10,11], m = 1, n = 3
	Output: [1,5,9]
	Explanation: Head of linked list after removing nodes is returned.

	Example 3:
	Input: head = [1,2,3,4,5,6,7,8,9,10,11], m = 3, n = 1
	Output: [1,2,3,5,6,7,9,10,11]
	
	Example 4:
	Input: head = [9,3,7,7,9,10,8,2], m = 1, n = 2
	Output: [9,7,8]

	Constraints:
	* The given linked list will contain between 1 and 10^4 nodes.
	* The value of each node in the linked list will be in the range [1, 10^6].
	* 1 <= m,n <= 1000"""

    def deleteNodes(self, head: ListNode, m: int, n: int) -> ListNode:
        prev, node, i = None, head, 0
        while node: 
            if i%(m+n) < m: prev = node
            else: prev.next = node.next 
            node, i = node.next, i+1
        return head 


    """1475. Final Prices With a Special Discount in a Shop (Easy)
	Given the array prices where prices[i] is the price of the ith item in a 
	shop. There is a special discount for items in the shop, if you buy the ith 
	item, then you will receive a discount equivalent to prices[j] where j is 
	the minimum index such that j > i and prices[j] <= prices[i], otherwise, 
	you will not receive any discount at all. Return an array where the ith 
	element is the final price you will pay for the ith item of the shop 
	considering the special discount.

	Example 1:
	Input: prices = [8,4,6,2,3]
	Output: [4,2,4,2,3]
	Explanation: 
	For item 0 with price[0]=8 you will receive a discount equivalent to prices[1]=4, therefore, the final price you will pay is 8 - 4 = 4. 
	For item 1 with price[1]=4 you will receive a discount equivalent to prices[3]=2, therefore, the final price you will pay is 4 - 2 = 2. 
	For item 2 with price[2]=6 you will receive a discount equivalent to prices[3]=2, therefore, the final price you will pay is 6 - 2 = 4. 
	For items 3 and 4 you will not receive any discount at all.

	Example 2:
	Input: prices = [1,2,3,4,5]
	Output: [1,2,3,4,5]
	Explanation: In this case, for all items, you will not receive any discount 
	             at all.

	Example 3:
	Input: prices = [10,1,1,6]
	Output: [9,0,1,6]

	Constraints:
	* 1 <= prices.length <= 500
	* 1 <= prices[i] <= 10^3"""

    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = []
        for i, x in enumerate(prices): 
            while stack and prices[stack[-1]] >= x: 
                prices[stack.pop()] -= x
            stack.append(i)
        return prices


    """1477. Find Two Non-overlapping Sub-arrays Each With Target Sum (Medium)
	Given an array of integers arr and an integer target. You have to find two 
	non-overlapping sub-arrays of arr each with sum equal target. There can be 
	multiple answers so you have to find an answer where the sum of the lengths 
	of the two sub-arrays is minimum. Return the minimum sum of the lengths of 
	the two required sub-arrays, or return -1 if you cannot find such two sub-
	arrays.

	Example 1:
	Input: arr = [3,2,2,4,3], target = 3
	Output: 2
	Explanation: Only two sub-arrays have sum = 3 ([3] and [3]). The sum of 
	             their lengths is 2.

	Example 2:
	Input: arr = [7,3,4,7], target = 7
	Output: 2
	Explanation: Although we have three non-overlapping sub-arrays of 
	             sum = 7 ([7], [3,4] and [7]), but we will choose the first and 
	             third sub-arrays as the sum of their lengths is 2.
	
	Example 3:
	Input: arr = [4,3,2,6,2,3,4], target = 6
	Output: -1
	Explanation: We have only one sub-array of sum = 6.

	Example 4:
	Input: arr = [5,5,4,4,5], target = 3
	Output: -1
	Explanation: We cannot find a sub-array of sum = 3.

	Example 5:
	Input: arr = [3,1,1,1,5,1,2,1], target = 3
	Output: 3
	Explanation: Note that sub-arrays [1,2] and [2,1] cannot be an answer 
	             because they overlap.

	Constraints:
	* 1 <= arr.length <= 10^5
	* 1 <= arr[i] <= 1000
	* 1 <= target <= 10^8"""

    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        ans = inf 
        best = [inf]*len(arr) # shortest subarray ending at i
        prefix = 0
        latest = {0: -1}
        for i, x in enumerate(arr): 
            prefix += x
            if prefix - target in latest: 
                ii = latest[prefix - target]
                if ii >= 0: 
                    ans = min(ans, i - ii + best[ii])
                best[i] = i - ii
            if i: best[i] = min(best[i-1], best[i])
            latest[prefix] = i 
        return ans if ans < inf else -1


    """1478. Allocate Mailboxes (Hard)
	Given the array houses and an integer k. where houses[i] is the location of 
	the ith house along a street, your task is to allocate k mailboxes in the 
	street. Return the minimum total distance between each house and its 
	nearest mailbox. The answer is guaranteed to fit in a 32-bit signed integer.

	Example 1:
	Input: houses = [1,4,8,10,20], k = 3
	Output: 5
	Explanation: Allocate mailboxes in position 3, 9 and 20. Minimum total 
	             distance from each houses to nearest mailboxes is 
	             |3-1| + |4-3| + |9-8| + |10-9| + |20-20| = 5 

	Example 2:
	Input: houses = [2,3,5,12,18], k = 2
	Output: 9
	Explanation: Allocate mailboxes in position 3 and 14. Minimum total 
	             distance from each houses to nearest mailboxes is 
	             |2-3| + |3-3| + |5-3| + |12-14| + |18-14| = 9.
	
	Example 3:
	Input: houses = [7,4,6,1], k = 1
	Output: 8

	Example 4:
	Input: houses = [3,6,14,10], k = 4
	Output: 0

	Constraints:
	* n == houses.length
	* 1 <= n <= 100
	* 1 <= houses[i] <= 10^4
	* 1 <= k <= n
	* Array houses contain unique integers."""

    def minDistance(self, houses: List[int], k: int) -> int:
        houses.sort() # ascending order 
        n = len(houses)
        
        mdist = [[0]*n for _ in range(n)] # mdist[i][j] median distance of houses[i:j+1]
        for i in range(n):
            for j in range(i+1, n): 
                mdist[i][j] = mdist[i][j-1] + houses[j] - houses[i+j >> 1]
        
        @cache
        def fn(n, k):
            """Return min distance of allocating k mailboxes to n houses."""
            if n <= k: return 0 # one mailbox for each house
            if k == 1: return mdist[0][n-1]
            ans = inf 
            for nn in range(k-1, n): 
                ans = min(ans, fn(nn, k-1) + mdist[nn][n-1])
            return ans 
        
        return fn(n, k)

    
    """1491. Average Salary Excluding the Minimum and Maximum Salary (Easy)
	Given an array of unique integers salary where salary[i] is the salary of 
	the employee i. Return the average salary of employees excluding the 
	minimum and maximum salary.

	Example 1:
	Input: salary = [4000,3000,1000,2000]
	Output: 2500.00000
	Explanation: Minimum salary and maximum salary are 1000 and 4000 respectively.
	Average salary excluding minimum and maximum salary is (2000+3000)/2= 2500

	Example 2:
	Input: salary = [1000,2000,3000]
	Output: 2000.00000
	Explanation: Minimum salary and maximum salary are 1000 and 3000 respectively.
	Average salary excluding minimum and maximum salary is (2000)/1= 2000

	Example 3:
	Input: salary = [6000,5000,4000,3000,2000,1000]
	Output: 3500.00000

	Example 4:
	Input: salary = [8000,9000,2000,3000,6000,1000]
	Output: 4750.00000

	Constraints:
	* 3 <= salary.length <= 100
	* 10^3 <= salary[i] <= 10^6
	* salary[i] is unique.
	* Answers within 10^-5 of the actual value will be accepted as correct."""

    def average(self, salary: List[int]) -> float:
        return (sum(salary)-max(salary)-min(salary)) / (len(salary)-2)


    """1492. The kth Factor of n (Medium)
	Given two positive integers n and k. A factor of an integer n is defined as 
	an integer i where n % i == 0. Consider a list of all factors of n sorted 
	in ascending order, return the kth factor in this list or return -1 if n 
	has less than k factors.

	Example 1:
	Input: n = 12, k = 3
	Output: 3
	Explanation: Factors list is [1, 2, 3, 4, 6, 12], the 3rd factor is 3.

	Example 2:
	Input: n = 7, k = 2
	Output: 7
	Explanation: Factors list is [1, 7], the 2nd factor is 7.

	Example 3:
	Input: n = 4, k = 4
	Output: -1
	Explanation: Factors list is [1, 2, 4], there is only 3 factors. We should return -1.

	Example 4:
	Input: n = 1, k = 1
	Output: 1
	Explanation: Factors list is [1], the 1st factor is 1.

	Example 5:
	Input: n = 1000, k = 3
	Output: 4
	Explanation: Factors list is [1, 2, 4, 5, 8, 10, 20, 25, 40, 50, 100, 125, 200, 250, 500, 1000].

	Constraints: 1 <= k <= n <= 1000"""

    def kthFactor(self, n: int, k: int) -> int:
        for i in range(1, int(sqrt(n))+1): # forward pass 
            if not n%i: k -= 1
            if not k: return i 
        
        while i > 0: # backward pass 
            if i * i < n: 
                if not n%i: k -= 1
                if not k: return n//i
            i -= 1
        
        return -1 


    """1493. Longest Subarray of 1's After Deleting One Element (Medium)
	Given a binary array nums, you should delete one element from it. Return 
	the size of the longest non-empty subarray containing only 1's in the 
	resulting array. Return 0 if there is no such subarray.

	Example 1:
	Input: nums = [1,1,0,1]
	Output: 3
	Explanation: After deleting the number in position 2, [1,1,1] contains 3 
	             numbers with value of 1's.

	Example 2:
	Input: nums = [0,1,1,1,0,1,1,0,1]
	Output: 5
	Explanation: After deleting the number in position 4, [0,1,1,1,1,1,0,1] 
	             longest subarray with value of 1's is [1,1,1,1,1].
	
	Example 3:
	Input: nums = [1,1,1]
	Output: 2
	Explanation: You must delete one element.
	
	Example 4:
	Input: nums = [1,1,0,0,1,1,1,0,1]
	Output: 4

	Example 5:
	Input: nums = [0,0,0]
	Output: 0

	Constraints:
	* 1 <= nums.length <= 10^5
	* nums[i] is either 0 or 1."""

    def longestSubarray(self, nums: List[int]) -> int:
        ans = 0 
        queue = deque([-1])
        for i, x in enumerate(nums): 
            if not x: queue.append(i)
            if len(queue) > 2: queue.popleft()
            ans = max(ans, i - queue[0] - 1)
        return ans 


    """1494. Parallel Courses II (Hard)
	Given the integer n representing the number of courses at some university 
	labeled from 1 to n, and the array dependencies where 
	dependencies[i] = [xi, yi] represents a prerequisite relationship, that is, 
	the course xi must be taken before the course yi. Also, you are given the 
	integer k. In one semester you can take at most k courses as long as you 
	have taken all the prerequisites for the courses you are taking. Return the 
	minimum number of semesters to take all courses. It is guaranteed that you 
	can take all courses in some way.

	Example 1:
	Input: n = 4, dependencies = [[2,1],[3,1],[1,4]], k = 2
	Output: 3 
	Explanation: The figure above represents the given graph. In this case we 
	             can take courses 2 and 3 in the first semester, then take 
	             course 1 in the second semester and finally take course 4 in 
	             the third semester.

	Example 2:
	Input: n = 5, dependencies = [[2,1],[3,1],[4,1],[1,5]], k = 2
	Output: 4 
	Explanation: The figure above represents the given graph. In this case one 
	             optimal way to take all courses is: take courses 2 and 3 in 
	             the first semester and take course 4 in the second semester, 
	             then take course 1 in the third semester and finally take 
	             course 5 in the fourth semester.
	
	Example 3:
	Input: n = 11, dependencies = [], k = 2
	Output: 6

	Constraints:
	* 1 <= n <= 15
	* 1 <= k <= n
	* 0 <= dependencies.length <= n * (n-1) / 2
	* dependencies[i].length == 2
	* 1 <= xi, yi <= n
	* xi != yi
	* All prerequisite relationships are distinct, that is, dependencies[i] != dependencies[j].
	* The given graph is a directed acyclic graph."""

    def minNumberOfSemesters(self, n: int, dependencies: List[List[int]], k: int) -> int:
        pre = [0]*n # prerequisites 
        for u, v in dependencies: 
            pre[v-1] |= 1 << (u-1) 
            
        @cache
        def fn(mask): 
            """Return min semesters to take remaining courses."""
            if mask == (1 << n) - 1: return 0 # all courses taken 
            can = [] # available courses 
            for i in range(n): 
                if not mask & 1 << i and mask & pre[i] == pre[i]: 
                    can.append(i)
            
            ans = inf
            for courses in combinations(can, min(k, len(can))): 
                temp = mask 
                for c in courses: 
                    temp |= 1 << c
                ans = min(ans, 1 + fn(temp))
            return ans 
        
        return fn(0)


    """1523. Count Odd Numbers in an Interval Range (Easy)
	Given two non-negative integers low and high. Return the count of odd 
	numbers between low and high (inclusive).

	Example 1:
	Input: low = 3, high = 7
	Output: 3
	Explanation: The odd numbers between 3 and 7 are [3,5,7].

	Example 2:
	Input: low = 8, high = 10
	Output: 1
	Explanation: The odd numbers between 8 and 10 are [9].

	Constraints: 0 <= low <= high <= 10^9"""

    def countOdds(self, low: int, high: int) -> int:
        return (high+1)//2 - low//2


    """1524. Number of Sub-arrays With Odd Sum (Medium)
	Given an array of integers arr. Return the number of sub-arrays with odd 
	sum. As the answer may grow large, the answer must be computed modulo 
	10^9 + 7.

	Example 1:
	Input: arr = [1,3,5]
	Output: 4
	Explanation: All sub-arrays are [[1],[1,3],[1,3,5],[3],[3,5],[5]]
	All sub-arrays sum are [1,4,9,3,8,5].
	Odd sums are [1,9,3,5] so the answer is 4.

	Example 2:
	Input: arr = [2,4,6]
	Output: 0
	Explanation: All sub-arrays are [[2],[2,4],[2,4,6],[4],[4,6],[6]]
	All sub-arrays sum are [2,6,12,4,10,6].
	All sub-arrays have even sum and the answer is 0.

	Example 3:
	Input: arr = [1,2,3,4,5,6,7]
	Output: 16

	Example 4:
	Input: arr = [100,100,99,99]
	Output: 4

	Example 5:
	Input: arr = [7]
	Output: 1

	Constraints:
	* 1 <= arr.length <= 10^5
	* 1 <= arr[i] <= 100"""

    def numOfSubarrays(self, arr: List[int]) -> int:
        freq = [1, 0]
        ans = prefix = 0
        for x in arr: 
            prefix += x 
            ans += freq[1 ^ prefix&1]
            freq[prefix&1] += 1
        return ans % 1_000_000_007


    """1525. Number of Good Ways to Split a String (Medium)
	You are given a string s, a split is called good if you can split s into 2 
	non-empty strings p and q where its concatenation is equal to s and the 
	number of distinct letters in p and q are the same. Return the number of 
	good splits you can make in s.

	Example 1:
	Input: s = "aacaba"
	Output: 2
	Explanation: There are 5 ways to split "aacaba" and 2 of them are good. 
	("a", "acaba") Left string and right string contains 1 and 3 different letters respectively.
	("aa", "caba") Left string and right string contains 1 and 3 different letters respectively.
	("aac", "aba") Left string and right string contains 2 and 2 different letters respectively (good split).
	("aaca", "ba") Left string and right string contains 2 and 2 different letters respectively (good split).
	("aacab", "a") Left string and right string contains 3 and 1 different letters respectively.

	Example 2:
	Input: s = "abcd"
	Output: 1
	Explanation: Split the string as follows ("ab", "cd").

	Example 3:
	Input: s = "aaaaa"
	Output: 4
	Explanation: All possible splits are good.

	Example 4:
	Input: s = "acbadbaada"
	Output: 2

	Constraints:
	* s contains only lowercase English letters.
	* 1 <= s.length <= 10^5"""

    def numSplits(self, s: str) -> int:
        freq = {}
        for c in s: freq[c] = 1 + freq.get(c, 0)
        
        ans = 0
        seen = set()
        for i, c in enumerate(s):
            seen.add(c)
            freq[c] -= 1
            if not freq[c]: freq.pop(c)
            if len(seen) == len(freq): ans += 1
        return ans 


    """1526. Minimum Number of Increments on Subarrays to Form a Target Array (Hard)
	Given an array of positive integers target and an array initial of same 
	size with all zeros. Return the minimum number of operations to form a 
	target array from initial if you are allowed to do the following operation:
	* Choose any subarray from initial and increment each value by one.
	The answer is guaranteed to fit within the range of a 32-bit signed integer.

	Example 1:
	Input: target = [1,2,3,2,1]
	Output: 3
	Explanation: We need at least 3 operations to form the target array from the initial array.
	[0,0,0,0,0] increment 1 from index 0 to 4 (inclusive).
	[1,1,1,1,1] increment 1 from index 1 to 3 (inclusive).
	[1,2,2,2,1] increment 1 at index 2.
	[1,2,3,2,1] target array is formed.

	Example 2:
	Input: target = [3,1,1,2]
	Output: 4
	Explanation: (initial)[0,0,0,0] -> [1,1,1,1] -> [1,1,1,2] -> [2,1,1,2] -> [3,1,1,2] (target).

	Example 3:
	Input: target = [3,1,5,4,2]
	Output: 7
	Explanation: (initial)[0,0,0,0,0] -> [1,1,1,1,1] -> [2,1,1,1,1] -> [3,1,1,1,1] 
	                                  -> [3,1,2,2,2] -> [3,1,3,3,2] -> [3,1,4,4,2] -> [3,1,5,4,2] (target).

	Example 4:
	Input: target = [1,1,1,1]
	Output: 1

	Constraints:
	* 1 <= target.length <= 10^5
	* 1 <= target[i] <= 10^5"""

    def minNumberOperations(self, target: List[int]) -> int:
        ans = prev = 0
        for x in target: 
            ans += max(x - prev, 0)
            prev = x
        return ans 


    """1564. Put Boxes Into the Warehouse I (Medium)
	You are given two arrays of positive integers, boxes and warehouse, 
	representing the heights of some boxes of unit width and the heights of n 
	rooms in a warehouse respectively. The warehouse's rooms are labelled from 
	0 to n - 1 from left to right where warehouse[i] (0-indexed) is the height 
	of the ith room. Boxes are put into the warehouse by the following rules:
	* Boxes cannot be stacked.
	* You can rearrange the insertion order of the boxes.
	* Boxes can only be pushed into the warehouse from left to right only.
	* If the height of some room in the warehouse is less than the height of a 
	  box, then that box and all other boxes behind it will be stopped before 
	  that room.
	Return the maximum number of boxes you can put into the warehouse.

	Example 1:
	Input: boxes = [4,3,4,1], warehouse = [5,3,3,4,1]
	Output: 3
	Explanation: We can first put the box of height 1 in room 4. Then we can 
	             put the box of height 3 in either of the 3 rooms 1, 2, or 3. 
	             Lastly, we can put one box of height 4 in room 0. There is no 
	             way we can fit all 4 boxes in the warehouse.

	Example 2:
	Input: boxes = [1,2,2,3,4], warehouse = [3,4,1,2]
	Output: 3
	Explanation: Notice that it's not possible to put the box of height 4 into 
	             the warehouse since it cannot pass the first room of height 3. 
	             Also, for the last two rooms, 2 and 3, only boxes of height 1 
	             can fit. We can fit 3 boxes maximum as shown above. The yellow 
	             box can also be put in room 2 instead. Swapping the orange and 
	             green boxes is also valid, or swapping one of them with the 
	             red box.
	
	Example 3:
	Input: boxes = [1,2,3], warehouse = [1,2,3,4]
	Output: 1
	Explanation: Since the first room in the warehouse is of height 1, we can only put boxes of height 1.

	Example 4:
	Input: boxes = [4,5,6], warehouse = [3,3,3,3,3]
	Output: 0

	Constraints:
	* n == warehouse.length
	* 1 <= boxes.length, warehouse.length <= 10^5
	* 1 <= boxes[i], warehouse[i] <= 10^9"""

    def maxBoxesInWarehouse(self, boxes: List[int], warehouse: List[int]) -> int:
        k = 0
        for box in sorted(boxes, reverse=True): 
            if k < len(warehouse) and box <= warehouse[k]: 
                k += 1
        return k 


    """1580. Put Boxes Into the Warehouse II (Medium)
	You are given two arrays of positive integers, boxes and warehouse, 
	representing the heights of some boxes of unit width and the heights of n 
	rooms in a warehouse respectively. The warehouse's rooms are labeled from 
	0 to n - 1 from left to right where warehouse[i] (0-indexed) is the height 
	of the ith room. Boxes are put into the warehouse by the following rules:
	* Boxes cannot be stacked.
	* You can rearrange the insertion order of the boxes.
	* Boxes can be pushed into the warehouse from either side (left or right)
	* If the height of some room in the warehouse is less than the height of a 
	  box, then that box and all other boxes behind it will be stopped before 
	  that room.
	Return the maximum number of boxes you can put into the warehouse.

	Example 1:
	Input: boxes = [1,2,2,3,4], warehouse = [3,4,1,2]
	Output: 4
	Explanation:
	We can store the boxes in the following order:
	1- Put the yellow box in room 2 from either the left or right side.
	2- Put the orange box in room 3 from the right side.
	3- Put the green box in room 1 from the left side.
	4- Put the red box in room 0 from the left side.
	Notice that there are other valid ways to put 4 boxes such as swapping the 
	red and green boxes or the red and orange boxes.

	Example 2:
	Input: boxes = [3,5,5,2], warehouse = [2,1,3,4,5]
	Output: 3
	Explanation: It's not possible to put the two boxes of height 5 in the 
	             warehouse since there's only 1 room of height >= 5. Other 
	             valid solutions are to put the green box in room 2 or to put 
	             the orange box first in room 2 before putting the green and 
	             red boxes.

	Example 3:
	Input: boxes = [1,2,3], warehouse = [1,2,3,4]
	Output: 3
	
	Example 4:
	Input: boxes = [4,5,6], warehouse = [3,3,3,3,3]
	Output: 0

	Constraints:
	* n == warehouse.length
	* 1 <= boxes.length, warehouse.length <= 10^5
	* 1 <= boxes[i], warehouse[i] <= 10^9"""

    def maxBoxesInWarehouse(self, boxes: List[int], warehouse: List[int]) -> int:
        ans = lo = 0
        hi = len(warehouse) - 1
        for box in sorted(boxes, reverse=True): 
            if lo <= hi: 
                if box <= warehouse[lo]: 
                    ans += 1
                    lo += 1
                elif box <= warehouse[hi]:
                    ans += 1
                    hi -= 1
        return ans 


    """1588. Sum of All Odd Length Subarrays (Easy)
	Given an array of positive integers arr, calculate the sum of all possible 
	odd-length subarrays. A subarray is a contiguous subsequence of the array. 
	Return the sum of all odd-length subarrays of arr.

	Example 1:
	Input: arr = [1,4,2,5,3]
	Output: 58
	Explanation: The odd-length subarrays of arr and their sums are:
	[1] = 1
	[4] = 4
	[2] = 2
	[5] = 5
	[3] = 3
	[1,4,2] = 7
	[4,2,5] = 11
	[2,5,3] = 10
	[1,4,2,5,3] = 15
	If we add all these together we get 1 + 4 + 2 + 5 + 3 + 7 + 11 + 10 + 15 = 58

	Example 2:
	Input: arr = [1,2]
	Output: 3
	Explanation: There are only 2 subarrays of odd length, [1] and [2]. Their sum is 3.

	Example 3:
	Input: arr = [10,11,12]
	Output: 66

	Constraints:
	* 1 <= arr.length <= 100
	* 1 <= arr[i] <= 1000"""

    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        return sum(((i+1)*(len(arr)-i) + 1)//2 * x for i, x in enumerate(arr))


    """1589. Maximum Sum Obtained of Any Permutation (Medium)
	We have an array of integers, nums, and an array of requests where 
	requests[i] = [starti, endi]. The ith request asks for the sum of 
	nums[starti] + nums[starti + 1] + ... + nums[endi - 1] + nums[endi]. Both 
	starti and endi are 0-indexed. Return the maximum total sum of all requests 
	among all permutations of nums. Since the answer may be too large, return 
	it modulo 10^9 + 7.

	Example 1:
	Input: nums = [1,2,3,4,5], requests = [[1,3],[0,1]]
	Output: 19
	Explanation: One permutation of nums is [2,1,3,4,5] with the following result: 
	requests[0] -> nums[1] + nums[2] + nums[3] = 1 + 3 + 4 = 8
	requests[1] -> nums[0] + nums[1] = 2 + 1 = 3
	Total sum: 8 + 3 = 11.
	A permutation with a higher total sum is [3,5,4,2,1] with the following result:
	requests[0] -> nums[1] + nums[2] + nums[3] = 5 + 4 + 2 = 11
	requests[1] -> nums[0] + nums[1] = 3 + 5  = 8
	Total sum: 11 + 8 = 19, which is the best that you can do.

	Example 2:
	Input: nums = [1,2,3,4,5,6], requests = [[0,1]]
	Output: 11
	Explanation: A permutation with the max total sum is [6,5,4,3,2,1] with request sums [11].

	Example 3:
	Input: nums = [1,2,3,4,5,10], requests = [[0,2],[1,3],[1,1]]
	Output: 47
	Explanation: A permutation with the max total sum is [4,10,5,3,2,1] with request sums [19,18,10].

	Constraints:
	* n == nums.length
	* 1 <= n <= 105
	* 0 <= nums[i] <= 105
	* 1 <= requests.length <= 105
	* requests[i].length == 2
	* 0 <= starti <= endi < n"""

    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        chg = [0]*len(nums) # change 
        for i, j in requests: 
            chg[i] += 1
            if j+1 < len(nums): chg[j+1] -= 1
        for i in range(1, len(nums)): chg[i] += chg[i-1] # cumulated change
        return sum(n*c for n, c in zip(sorted(nums), sorted(chg))) % 1_000_000_007


    """1590. Make Sum Divisible by P (Medium)
	Given an array of positive integers nums, remove the smallest subarray 
	(possibly empty) such that the sum of the remaining elements is divisible 
	by p. It is not allowed to remove the whole array. Return the length of the 
	smallest subarray that you need to remove, or -1 if it's impossible. A 
	subarray is defined as a contiguous block of elements in the array.

	Example 1:
	Input: nums = [3,1,4,2], p = 6
	Output: 1
	Explanation: The sum of the elements in nums is 10, which is not divisible 
	             by 6. We can remove the subarray [4], and the sum of the 
	             remaining elements is 6, which is divisible by 6.

	Example 2:
	Input: nums = [6,3,5,2], p = 9
	Output: 2
	Explanation: We cannot remove a single element to get a sum divisible by 9. 
	             The best way is to remove the subarray [5,2], leaving us with 
	             [6,3] with sum 9.
	
	Example 3:
	Input: nums = [1,2,3], p = 3
	Output: 0
	Explanation: Here the sum is 6. which is already divisible by 3. Thus we do 
	             not need to remove anything.

	Example 4:
	Input: nums = [1,2,3], p = 7
	Output: -1
	Explanation: There is no way to remove a subarray in order to get a sum 
	             divisible by 7.

	Example 5:
	Input: nums = [1000000000,1000000000,1000000000], p = 3
	Output: 0

	Constraints:
	* 1 <= nums.length <= 105
	* 1 <= nums[i] <= 109
	* 1 <= p <= 109"""

    def minSubarray(self, nums: List[int], p: int) -> int:
        target = sum(nums) % p # targetted remainder 
        ans = inf
        seen = {(prefix := 0): -1}
        for i, x in enumerate(nums): 
            seen[(prefix := (prefix+x)%p)] = i # update seen before check 
            if (prefix-target) % p in seen: 
                ans = min(ans, i - seen[(prefix-target) % p])
        return ans if ans < len(nums) else -1 # not allowed to remove whole array 



    """1591. Strange Printer II (Hard)
	There is a strange printer with the following two special requirements: 
	1) On each turn, the printer will print a solid rectangular pattern of a 
	   single color on the grid. This will cover up the existing colors in the 
	   rectangle.
	2) Once the printer has used a color for the above operation, the same 
	   color cannot be used again.
	
	You are given a m x n matrix targetGrid, where targetGrid[row][col] is the 
	color in the position (row, col) of the grid. Return true if it is possible 
	to print the matrix targetGrid, otherwise, return false.

	Example 1:
	Input: targetGrid = [[1,1,1,1],[1,2,2,1],[1,2,2,1],[1,1,1,1]]
	Output: true

	Example 2:
	Input: targetGrid = [[1,1,1,1],[1,1,3,3],[1,1,3,4],[5,5,1,4]]
	Output: true

	Example 3:
	Input: targetGrid = [[1,2,1],[2,1,2],[1,2,1]]
	Output: false
	Explanation: It is impossible to form targetGrid because it is not allowed 
	             to print the same color in different turns.

	Example 4:
	Input: targetGrid = [[1,1,1],[3,1,3]]
	Output: false

	Constraints:
	* m == targetGrid.length
	* n == targetGrid[i].length
	* 1 <= m, n <= 60
	* 1 <= targetGrid[row][col] <= 60"""

    def isPrintable(self, targetGrid: List[List[int]]) -> bool:
        m, n = len(targetGrid), len(targetGrid[0]) # dimensions 
        
        # build directed graph (adjacency list)
        digraph = {} 
        for c in range(1, 61): 
            imn = jmn = 60
            imx = jmx = 0
            for i in range(m): 
                for j in range(n): 
                    if targetGrid[i][j] == c: 
                        imn = min(imn, i)
                        imx = max(imx, i)
                        jmn = min(jmn, j)
                        jmx = max(jmx, j)
            for i in range(imn, imx+1):
                for j in range(jmn, jmx+1): 
                    if targetGrid[i][j] != c: 
                        digraph.setdefault(c, set()).add(targetGrid[i][j])
            
        # check for cycle in digraph (tri-color)
        def dfs(n): 
            """Return True if a cycle is detected."""
            if seen[n]: return seen[n] == 1 
            seen[n] = 1
            if any(dfs(nn) for nn in digraph.get(n, set())): return True 
            seen[n] = 2
            return False 
        
        seen = [0]*61
        return not any(dfs(i) for i in range(61)) # cycle, i.e. impossible to print 


    """1592. Rearrange Spaces Between Words (Easy)
	You are given a string text of words that are placed among some number of 
	spaces. Each word consists of one or more lowercase English letters and are 
	separated by at least one space. It's guaranteed that text contains at 
	least one word. Rearrange the spaces so that there is an equal number of 
	spaces between every pair of adjacent words and that number is maximized. 
	If you cannot redistribute all the spaces equally, place the extra spaces 
	at the end, meaning the returned string should be the same length as text. 
	Return the string after rearranging the spaces.

	Example 1:
	Input: text = "  this   is  a sentence "
	Output: "this   is   a   sentence"
	Explanation: There are a total of 9 spaces and 4 words. We can evenly 
	             divide the 9 spaces between the words: 9 / (4-1) = 3 spaces.

	Example 2:
	Input: text = " practice   makes   perfect"
	Output: "practice   makes   perfect "
	Explanation: There are a total of 7 spaces and 3 words. 7 / (3-1) = 3 
	             spaces plus 1 extra space. We place this extra space at the 
	             end of the string.
	
	Example 3:
	Input: text = "hello   world"
	Output: "hello   world"
	
	Example 4:
	Input: text = "  walks  udp package   into  bar a"
	Output: "walks  udp  package  into  bar  a "

	Example 5:
	Input: text = "a"
	Output: "a"

	Constraints:
	* 1 <= text.length <= 100
	* text consists of lowercase English letters and ' '.
	* text contains at least one word."""

    def reorderSpaces(self, text: str) -> str:
        ns = text.count(" ") # count of spaces 
        nw = len(text := text.split()) # count of words 
        if nw > 1: nw, ns = divmod(ns, nw-1) # nw - between word spaces / ns - trailing spaces
        return (" "*nw).join(text) + " "*ns


    """1593. Split a String Into the Max Number of Unique Substrings (Medium)
	Given a string s, return the maximum number of unique substrings that the 
	given string can be split into. You can split string s into any list of 
	non-empty substrings, where the concatenation of the substrings forms the 
	original string. However, you must split the substrings such that all of 
	them are unique. A substring is a contiguous sequence of characters within 
	a string.

	Example 1:
	Input: s = "ababccc"
	Output: 5
	Explanation: One way to split maximally is ['a', 'b', 'ab', 'c', 'cc']. 
	             Splitting like ['a', 'b', 'a', 'b', 'c', 'cc'] is not valid as 
	             you have 'a' and 'b' multiple times.

	Example 2:
	Input: s = "aba"
	Output: 2
	Explanation: One way to split maximally is ['a', 'ba'].
	
	Example 3:
	Input: s = "aa"
	Output: 1
	Explanation: It is impossible to split the string any further.

	Constraints:
	* 1 <= s.length <= 16
	* s contains only lower case English letters."""

    def maxUniqueSplit(self, s: str) -> int:
        
        def fn(i, seen=set()):
            """Find max length via backtracking (not dp)."""
            ans = 0
            if i < len(s): # boundary condition when i == len(s)
                for ii in range(i+1, len(s)+1): 
                    if s[i:ii] not in seen: 
                        seen.add(s[i:ii])
                        ans = max(ans, 1 + fn(ii, seen))
                        seen.remove(s[i:ii])
            return ans 
            
        return fn(0)


    """1594. Maximum Non Negative Product in a Matrix (Medium)
	You are given a rows x cols matrix grid. Initially, you are located at the 
	top-left corner (0, 0), and in each step, you can only move right or down 
	in the matrix. Among all possible paths starting from the top-left corner 
	(0, 0) and ending in the bottom-right corner (rows - 1, cols - 1), find the 
	path with the maximum non-negative product. The product of a path is the 
	product of all integers in the grid cells visited along the path. Return 
	the maximum non-negative product modulo 109 + 7. If the maximum product is 
	negative return -1. Notice that the modulo is performed after getting the 
	maximum product.

	Example 1:
	Input: grid = [[-1,-2,-3],
	               [-2,-3,-3],
	               [-3,-3,-2]]
	Output: -1
	Explanation: It's not possible to get non-negative product in the path from 
	             (0, 0) to (2, 2), so return -1.

	Example 2:
	Input: grid = [[1,-2,1],
	               [1,-2,1],
	               [3,-4,1]]
	Output: 8
	Explanation: Maximum non-negative product is in bold (1 * 1 * -2 * -4 * 1 = 8).
	
	Example 3:
	Input: grid = [[1, 3],
	               [0,-4]]
	Output: 0
	Explanation: Maximum non-negative product is in bold (1 * 0 * -4 = 0).

	Example 4:
	Input: grid = [[ 1, 4,4,0],
	               [-2, 0,0,1],
	               [ 1,-1,1,1]]
	Output: 2
	Explanation: Maximum non-negative product is in bold (1 * -2 * 1 * -1 * 1 * 1 = 2).

	Constraints:
	* 1 <= rows, cols <= 15
	* -4 <= grid[i][j] <= 4"""

    def maxProductPath(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        @lru_cache(None)
        def fn(i, j): 
            """Return maximum & minimum products ending at (i, j)."""
            if i == 0 and j == 0: return grid[0][0], grid[0][0]
            if i < 0 or j < 0: return -inf, inf
            if grid[i][j] == 0: return 0, 0
            mx1, mn1 = fn(i-1, j) # from top
            mx2, mn2 = fn(i, j-1) # from left 
            mx, mn = max(mx1, mx2)*grid[i][j], min(mn1, mn2)*grid[i][j]
            return (mx, mn) if grid[i][j] > 0 else (mn, mx)
        
        mx, _ = fn(m-1, n-1)
        return -1 if mx < 0 else mx % 1_000_000_007


    """1595. Minimum Cost to Connect Two Groups of Points (Hard)
	You are given two groups of points where the first group has size1 points, 
	the second group has size2 points, and size1 >= size2. The cost of the 
	connection between any two points are given in an size1 x size2 matrix 
	where cost[i][j] is the cost of connecting point i of the first group and 
	point j of the second group. The groups are connected if each point in both 
	groups is connected to one or more points in the opposite group. In other 
	words, each point in the first group must be connected to at least one 
	point in the second group, and each point in the second group must be 
	connected to at least one point in the first group. Return the minimum cost 
	it takes to connect the two groups.

	Example 1:
	Input: cost = [[15, 96], [36, 2]]
	Output: 17
	Explanation: The optimal way of connecting the groups is:
	1--A
	2--B
	This results in a total cost of 17.

	Example 2:
	Input: cost = [[1, 3, 5], [4, 1, 1], [1, 5, 3]]
	Output: 4
	Explanation: The optimal way of connecting the groups is:
	1--A
	2--B
	2--C
	3--A
	This results in a total cost of 4.
	Note that there are multiple points connected to point 2 in the first group 
	and point A in the second group. This does not matter as there is no limit 
	to the number of points that can be connected. We only care about the 
	minimum total cost.

	Example 3:
	Input: cost = [[2, 5, 1], [3, 4, 7], [8, 1, 2], [6, 2, 4], [3, 8, 8]]
	Output: 10

	Constraints:
	* size1 == cost.length
	* size2 == cost[i].length
	* 1 <= size1, size2 <= 12
	* size1 >= size2
	* 0 <= cost[i][j] <= 100"""

    def connectTwoGroups(self, cost: List[List[int]]) -> int:
        m, n = len(cost), len(cost[0])
        mn = [min(x) for x in zip(*cost)] # min cost of connecting points in 2nd group 
        
        @lru_cache(None)
        def fn(i, mask):
            """Return min cost of connecting group1[i:] and group2 represented as mask."""
            if i == m: return sum(mn[j] for j in range(n) if not (mask & (1<<j)))
            return min(cost[i][j] + fn(i+1, mask | 1<<j) for j in range(n))
                
        return fn(0, 0)


    """1602. Find Nearest Right Node in Binary Tree (Medium)
	Given the root of a binary tree and a node u in the tree, return the 
	nearest node on the same level that is to the right of u, or return null 
	if u is the rightmost node in its level.

	Example 1:
	Input: root = [1,2,3,null,4,5,6], u = 4
	Output: 5
	Explanation: The nearest node on the same level to the right of node 4 is 
	             node 5.

	Example 2:
	Input: root = [3,null,4,2], u = 2
	Output: null
	Explanation: There are no nodes to the right of 2.

	Example 3:
	Input: root = [1], u = 1
	Output: null

	Example 4:
	Input: root = [3,4,2,null,null,null,1], u = 4
	Output: 2

	Constraints:
	* The number of nodes in the tree is in the range [1, 105].
	* 1 <= Node.val <= 105
	* All values in the tree are distinct.
	* u is a node in the binary tree rooted at root."""

    def findNearestRightNode(self, root: TreeNode, u: TreeNode) -> TreeNode:
        queue = [root]
        while queue: 
            prev = None 
            newq = []
            for node in queue: 
                if node == u: return prev 
                prev = node 
                if node.right: newq.append(node.right)
                if node.left: newq.append(node.left)
            queue = newq


    """1604. Alert Using Same Key-Card Three or More Times in a One Hour Period (Medium)
	LeetCode company workers use key-cards to unlock office doors. Each time a 
	worker uses their key-card, the security system saves the worker's name and 
	the time when it was used. The system emits an alert if any worker uses the 
	key-card three or more times in a one-hour period. You are given a list of 
	strings keyName and keyTime where [keyName[i], keyTime[i]] corresponds to a 
	person's name and the time when their key-card was used in a single day. 
	Access times are given in the 24-hour time format "HH:MM", such as "23:51" 
	and "09:49". Return a list of unique worker names who received an alert for 
	frequent keycard use. Sort the names in ascending order alphabetically. 
	Notice that "10:00" - "11:00" is considered to be within a one-hour period, 
	while "22:51" - "23:52" is not considered to be within a one-hour period.

	Example 1:
	Input: keyName = ["daniel","daniel","daniel","luis","luis","luis","luis"], 
	       keyTime = ["10:00","10:40","11:00","09:00","11:00","13:00","15:00"]
	Output: ["daniel"]
	Explanation: "daniel" used the keycard 3 times in a one-hour period ("10:00","10:40", "11:00").
	
	Example 2:
	Input: keyName = ["alice","alice","alice","bob","bob","bob","bob"], 
	       keyTime = ["12:01","12:00","18:00","21:00","21:20","21:30","23:00"]
	Output: ["bob"]
	Explanation: "bob" used the keycard 3 times in a one-hour period ("21:00","21:20", "21:30").
	
	Example 3:
	Input: keyName = ["john","john","john"], keyTime = ["23:58","23:59","00:01"]
	Output: []

	Example 4:
	Input: keyName = ["leslie","leslie","leslie","clare","clare","clare","clare"], 
	       keyTime = ["13:00","13:20","14:00","18:00","18:51","19:30","19:49"]
	Output: ["clare","leslie"]

	Constraints:
	* 1 <= keyName.length, keyTime.length <= 10^5
	* keyName.length == keyTime.length
	* keyTime[i] is in the format "HH:MM".
	* [keyName[i], keyTime[i]] is unique.
	* 1 <= keyName[i].length <= 10
	* keyName[i] contains only lowercase English letters."""

    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        ans = set()
        seen = {}
        for key, time in sorted(zip(keyName, keyTime)): 
            if key not in ans: 
                h, m = time.split(":")
                time = int(h) * 60 + int(m)
                seen.setdefault(key, deque()).append(time)
                if len(seen[key]) == 3: 
                    if seen[key][-1] <= seen[key][0] + 60: ans.add(key)
                    seen[key].popleft()
        return sorted(ans)


    """1605. Find Valid Matrix Given Row and Column Sums (Medium)
	You are given two arrays rowSum and colSum of non-negative integers where 
	rowSum[i] is the sum of the elements in the ith row and colSum[j] is the 
	sum of the elements of the jth column of a 2D matrix. In other words, you 
	do not know the elements of the matrix, but you do know the sums of each 
	row and column. Find any matrix of non-negative integers of size 
	rowSum.length x colSum.length that satisfies the rowSum and colSum 
	requirements. Return a 2D array representing any matrix that fulfills the 
	requirements. It's guaranteed that at least one matrix that fulfills the 
	requirements exists.

	Example 1:
	Input: rowSum = [3,8], colSum = [4,7]
	Output: [[3,0],
	         [1,7]]
	Explanation:
	0th row: 3 + 0 = 3 == rowSum[0]
	1st row: 1 + 7 = 8 == rowSum[1]
	0th column: 3 + 1 = 4 == colSum[0]
	1st column: 0 + 7 = 7 == colSum[1]
	The row and column sums match, and all matrix elements are non-negative.
	Another possible matrix is: [[1,2],
	                             [3,5]]

	Example 2:
	Input: rowSum = [5,7,10], colSum = [8,6,8]
	Output: [[0,5,0],
	         [6,1,0],
	         [2,0,8]]

	Example 3:
	Input: rowSum = [14,9], colSum = [6,9,8]
	Output: [[0,9,5],
	         [6,0,3]]

	Example 4:
	Input: rowSum = [1,0], colSum = [1]
	Output: [[1],
	         [0]]

	Example 5:
	Input: rowSum = [0], colSum = [0]
	Output: [[0]]

	Constraints:
	* 1 <= rowSum.length, colSum.length <= 500
	* 0 <= rowSum[i], colSum[i] <= 10^8
	* sum(rows) == sum(columns)"""

    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        m, n = len(rowSum), len(colSum) # dimensions 
        ans = [[0]*n for _ in range(m)] 
        
        i = j = 0
        while i < len(rowSum) and j < len(colSum):
            ans[i][j] = min(rowSum[i], colSum[j])
            rowSum[i] -= ans[i][j]
            colSum[j] -= ans[i][j]
            if rowSum[i] == 0: i += 1
            if colSum[j] == 0: j += 1
        return ans 


    """1606. Find Servers That Handled Most Number of Requests (Hard)
	You have k servers numbered from 0 to k-1 that are being used to handle 
	multiple requests simultaneously. Each server has infinite computational 
	capacity but cannot handle more than one request at a time. The requests 
	are assigned to servers according to a specific algorithm:
	* The ith (0-indexed) request arrives.
	* If all servers are busy, the request is dropped (not handled at all).
	* If the (i % k)th server is available, assign the request to that server.
	* Otherwise, assign the request to the next available server (wrapping 
	  around the list of servers and starting from 0 if necessary). For example, 
	  if the ith server is busy, try to assign the request to the (i+1)th 
	  server, then the (i+2)th server, and so on.
	You are given a strictly increasing array arrival of positive integers, 
	where arrival[i] represents the arrival time of the ith request, and 
	another array load, where load[i] represents the load of the ith request 
	(the time it takes to complete). Your goal is to find the busiest server(s). 
	A server is considered busiest if it handled the most number of requests 
	successfully among all the servers. Return a list containing the IDs 
	(0-indexed) of the busiest server(s). You may return the IDs in any order.

	Example 1:
	Input: k = 3, arrival = [1,2,3,4,5], load = [5,2,3,3,3] 
	Output: [1] 
	Explanation:
	All of the servers start out available.
	The first 3 requests are handled by the first 3 servers in order.
	Request 3 comes in. Server 0 is busy, so it's assigned to the next available server, which is 1.
	Request 4 comes in. It cannot be handled since all servers are busy, so it is dropped.
	Servers 0 and 2 handled one request each, while server 1 handled two requests. Hence server 1 is the busiest server.

	Example 2:
	Input: k = 3, arrival = [1,2,3,4], load = [1,2,1,2]
	Output: [0]
	Explanation:
	The first 3 requests are handled by first 3 servers.
	Request 3 comes in. It is handled by server 0 since the server is available.
	Server 0 handled two requests, while servers 1 and 2 handled one request each. Hence server 0 is the busiest server.

	Example 3:
	Input: k = 3, arrival = [1,2,3], load = [10,12,11]
	Output: [0,1,2]
	Explanation: Each server handles a single request, so they are all considered the busiest.

	Example 4:
	Input: k = 3, arrival = [1,2,3,4,8,9,10], load = [5,2,10,3,1,2,2]
	Output: [1]

	Example 5:
	Input: k = 1, arrival = [1], load = [1]
	Output: [0]

	Constraints:
	* 1 <= k <= 10^5
	* 1 <= arrival.length, load.length <= 10^5
	* arrival.length == load.length
	* 1 <= arrival[i], load[i] <= 10^9
	* arrival is strictly increasing."""

    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        busy = [] # min-heap
        free = list(range(k)) # min-heap 
        freq = [0]*k
        
        for i, (ta, tl) in enumerate(zip(arrival, load)): 
            while busy and busy[0][0] <= ta: 
                _, ii = heappop(busy)
                heappush(free, i + (ii - i) % k) # circularly relocate it
            if free: 
                ii = heappop(free) % k 
                freq[ii] += 1
                heappush(busy, (ta+tl, ii))
        
        mx = max(freq)
        return [i for i, x in enumerate(freq) if x == mx]


    """1608. Special Array With X Elements Greater Than or Equal X (Easy)
	You are given an array nums of non-negative integers. nums is considered 
	special if there exists a number x such that there are exactly x numbers in 
	nums that are greater than or equal to x. Notice that x does not have to be 
	an element in nums. Return x if the array is special, otherwise, return -1. 
	It can be proven that if nums is special, the value for x is unique.

	Example 1:
	Input: nums = [3,5]
	Output: 2
	Explanation: There are 2 values (3 and 5) that are greater than or equal to 2.

	Example 2:
	Input: nums = [0,0]
	Output: -1
	Explanation: No numbers fit the criteria for x.
	If x = 0, there should be 0 numbers >= x, but there are 2.
	If x = 1, there should be 1 number >= x, but there are 0.
	If x = 2, there should be 2 numbers >= x, but there are 0.
	x cannot be greater since there are only 2 numbers in nums.

	Example 3:
	Input: nums = [0,4,3,0,4]
	Output: 3
	Explanation: There are 3 values that are greater than or equal to 3.

	Example 4:
	Input: nums = [3,6,7,7,0]
	Output: -1

	Constraints:
	* 1 <= nums.length <= 100
	* 0 <= nums[i] <= 1000"""

    def specialArray(self, nums: List[int]) -> int:
        nums.sort() 
        if len(nums) <= nums[0]: return len(nums) # edge case 
        for i in range(1, len(nums)): 
            if nums[i-1] < len(nums)-i <= nums[i]: return len(nums)-i
        return -1


    """1609. Even Odd Tree (Medium)
	A binary tree is named Even-Odd if it meets the following conditions:
	* The root of the binary tree is at level index 0, its children are at 
	  level index 1, their children are at level index 2, etc.
	* For every even-indexed level, all nodes at the level have odd integer 
	  values in strictly increasing order (from left to right).
	* For every odd-indexed level, all nodes at the level have even integer 
	  values in strictly decreasing order (from left to right).
	Given the root of a binary tree, return true if the binary tree is Even-
	Odd, otherwise return false.

	Example 1:
	Input: root = [1,10,4,3,null,7,9,12,8,6,null,null,2]
	Output: true
	Explanation: The node values on each level are:
	Level 0: [1]
	Level 1: [10,4]
	Level 2: [3,7,9]
	Level 3: [12,8,6,2]
	Since levels 0 and 2 are all odd and increasing, and levels 1 and 3 are all 
	even and decreasing, the tree is Even-Odd.

	Example 2:
	Input: root = [5,4,2,3,3,7]
	Output: false
	Explanation: The node values on each level are:
	Level 0: [5]
	Level 1: [4,2]
	Level 2: [3,3,7]
	Node values in the level 2 must be in strictly increasing order, so the 
	tree is not Even-Odd.

	Example 3:
	Input: root = [5,9,1,3,5,7]
	Output: false
	Explanation: Node values in the level 1 should be even integers.

	Example 4:
	Input: root = [1]
	Output: true

	Example 5:
	Input: root = [11,8,6,1,3,9,11,30,20,18,16,12,10,4,2,17]
	Output: true

	Constraints:
	* The number of nodes in the tree is in the range [1, 105].
	* 1 <= Node.val <= 106"""

    def isEvenOddTree(self, root: TreeNode) -> bool:
        queue = [root]
        even = True # True for even level
        while queue: 
            newq = []
            prev = -inf if even else inf
            for node in queue: 
                if not even and (node.val & 1 or prev <= node.val): return False 
                elif even and (not (node.val & 1) or prev >= node.val): return False 
                prev = node.val 
                if node.left: newq.append(node.left)
                if node.right: newq.append(node.right)
            queue = newq 
            even = not even
        return True 


    """1610. Maximum Number of Visible Points (Hard)
	You are given an array points, an integer angle, and your location, where 
	location = [posx, posy] and points[i] = [xi, yi] both denote integral 
	coordinates on the X-Y plane. Initially, you are facing directly east from 
	your position. You cannot move from your position, but you can rotate. In 
	other words, posx and posy cannot be changed. Your field of view in degrees 
	is represented by angle, determining how wide you can see from any given 
	view direction. Let d be the amount in degrees that you rotate 
	counterclockwise. Then, your field of view is the inclusive range of angles 
	[d - angle/2, d + angle/2]. You can see some set of points if, for each 
	point, the angle formed by the point, your position, and the immediate east 
	direction from your position is in your field of view. There can be 
	multiple points at one coordinate. There may be points at your location, 
	and you can always see these points regardless of your rotation. Points do 
	not obstruct your vision to other points. Return the maximum number of 
	points you can see.

	Example 1:
	Input: points = [[2,1],[2,2],[3,3]], angle = 90, location = [1,1]
	Output: 3
	Explanation: The shaded region represents your field of view. All points 
	             can be made visible in your field of view, including [3,3] 
	             even though [2,2] is in front and in the same line of sight.

	Example 2:
	Input: points = [[2,1],[2,2],[3,4],[1,1]], angle = 90, location = [1,1]
	Output: 4
	Explanation: All points can be made visible in your field of view, 
	             including the one at your location.

	Example 3:
	Input: points = [[1,0],[2,1]], angle = 13, location = [1,1]
	Output: 1
	Explanation: You can only see one of the two points, as shown above.

	Constraints:
	* 1 <= points.length <= 105
	* points[i].length == 2
	* location.length == 2
	* 0 <= angle < 360
	* 0 <= posx, posy, xi, yi <= 109"""

    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        x0, y0 = location
        
        ans = ovlp = 0
        theta = [] 
        for x, y in points: 
            if x == x0 and y == y0: ovlp += 1
            else: theta.append(atan2(y-y0, x-x0)) # (x, y) wrt (x0, y0)
        
        theta.sort()
        theta += [x+2*pi for x in theta]
        ii = 0
        for i in range(len(theta)): 
            while theta[i] - theta[ii] > angle*pi/180: ii += 1
            ans = max(ans, i-ii+1)
        return ans + ovlp


    """1611. Minimum One Bit Operations to Make Integers Zero (Hard)
	Given an integer n, you must transform it into 0 using the following 
	operations any number of times:
	* Change the rightmost (0th) bit in the binary representation of n.
	* Change the ith bit in the binary representation of n if the (i-1)th bit 
	  is set to 1 and the (i-2)th through 0th bits are set to 0.
	Return the minimum number of operations to transform n into 0.

	Example 1:
	Input: n = 0
	Output: 0

	Example 2:
	Input: n = 3
	Output: 2
	Explanation: The binary representation of 3 is "11".
	"11" -> "01" with the 2nd operation since the 0th bit is 1.
	"01" -> "00" with the 1st operation.

	Example 3:
	Input: n = 6
	Output: 4
	Explanation: The binary representation of 6 is "110".
	"110" -> "010" with the 2nd operation since the 1st bit is 1 and 0th through 0th bits are 0.
	"010" -> "011" with the 1st operation.
	"011" -> "001" with the 2nd operation since the 0th bit is 1.
	"001" -> "000" with the 1st operation.

	Example 4:
	Input: n = 9
	Output: 14

	Example 5:
	Input: n = 333
	Output: 393

	Constraints: 0 <= n <= 109"""

    def minimumOneBitOperations(self, n: int) -> int:
        if not n: return 0 # edge case 
        if not (n & (n-1)): return 2*n-1
        b = 1 << n.bit_length()-1 # most significant set bit 
        return self.minimumOneBitOperations((b>>1)^b^n) + b


    """1618. Maximum Font to Fit a Sentence in a Screen (Medium)
	You are given a string text. We want to display text on a screen of width w 
	and height h. You can choose any font size from array fonts, which contains 
	the available font sizes in ascending order. You can use the FontInfo 
	interface to get the width and height of any character at any available 
	font size.

	The FontInfo interface is defined as such:

	interface FontInfo {
	  // Returns the width of character ch on the screen using font size fontSize.
	  // O(1) per call
	  public int getWidth(int fontSize, char ch);

	  // Returns the height of any character on the screen using font size fontSize.
	  // O(1) per call
	  public int getHeight(int fontSize);
	}
	The calculated width of text for some fontSize is the sum of every 
	getWidth(fontSize, text[i]) call for each 0 <= i < text.length (0-indexed). 
	The calculated height of text for some fontSize is getHeight(fontSize). 
	Note that text is displayed on a single line. It is guaranteed that 
	FontInfo will return the same value if you call getHeight or getWidth with 
	the same parameters. It is also guaranteed that for any font size fontSize 
	and any character ch:
	* getHeight(fontSize) <= getHeight(fontSize+1)
	* getWidth(fontSize, ch) <= getWidth(fontSize+1, ch)
	Return the maximum font size you can use to display text on the screen. If 
	text cannot fit on the display with any font size, return -1.

	Example 1:
	Input: text = "helloworld", w = 80, h = 20, fonts = [6,8,10,12,14,16,18,24,36]
	Output: 6

	Example 2:
	Input: text = "leetcode", w = 1000, h = 50, fonts = [1,2,4]
	Output: 4

	Example 3:
	Input: text = "easyquestion", w = 100, h = 100, fonts = [10,15,20,25]
	Output: -1

	Constraints:
	* 1 <= text.length <= 50000
	* text contains only lowercase English letters.
	* 1 <= w <= 10^7
	* 1 <= h <= 10^4
	* 1 <= fonts.length <= 10^5
	* 1 <= fonts[i] <= 10^5
	* fonts is sorted in ascending order and does not contain duplicates."""

    def maxFont(self, text: str, w: int, h: int, fonts: List[int], fontInfo : 'FontInfo') -> int:
        # last True binary search 
        lo, hi = -1, len(fonts)-1
        while lo < hi: 
            mid = lo + hi + 1 >> 1
            hh = fontInfo.getHeight(fonts[mid])
            ww = sum(fontInfo.getWidth(fonts[mid], c) for c in text)
            if hh <= h and ww <= w : lo = mid
            else: hi = mid - 1 
        return fonts[lo] if lo >= 0 else -1  


    """1619. Mean of Array After Removing Some Elements (Easy)
	Given an integer array arr, return the mean of the remaining integers after 
	removing the smallest 5% and the largest 5% of the elements. Answers within 
	10-5 of the actual answer will be considered accepted.

	Example 1:
	Input: arr = [1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3]
	Output: 2.00000
	Explanation: After erasing the minimum and the maximum values of this array, 
	             all elements are equal to 2, so the mean is 2.

	Example 2:
	Input: arr = [6,2,7,5,1,2,0,3,10,2,5,0,5,5,0,8,7,6,8,0]
	Output: 4.00000

	Example 3:
	Input: arr = [6,0,7,0,7,5,7,8,3,4,0,7,8,1,6,8,1,1,2,4,8,1,9,5,4,3,8,5,10,8,6,6,1,0,6,10,8,2,3,4]
	Output: 4.77778

	Example 4:
	Input: arr = [9,7,8,7,7,8,4,4,6,8,8,7,6,8,8,9,2,6,0,0,1,10,8,6,3,3,5,1,10,9,0,7,10,0,10,4,1,10,6,9,3,6,0,0,2,7,0,6,7,2,9,7,7,3,0,1,6,1,10,3]
	Output: 5.27778

	Example 5:
	Input: arr = [4,8,4,10,0,7,1,3,7,8,8,3,4,1,6,2,1,1,8,0,9,8,0,3,9,10,3,10,1,10,7,3,2,1,4,9,10,7,6,4,0,8,5,1,2,1,6,2,5,0,7,10,9,10,3,7,10,5,8,5,7,6,7,6,10,9,5,10,5,5,7,2,10,7,7,8,2,0,1,1]
	Output: 5.29167

	Constraints:
	* 20 <= arr.length <= 1000
	* arr.length is a multiple of 20.
	* 0 <= arr[i] <= 105"""

    def trimMean(self, arr: List[int]) -> float:
        return sum(sorted(arr)[len(arr)//20:-len(arr)//20])/(len(arr)*0.9)


    """1620. Coordinate With Maximum Network Quality (Medium)
	You are given an array of network towers towers and an integer radius, 
	where towers[i] = [xi, yi, qi] denotes the ith network tower with location 
	(xi, yi) and quality factor qi. All the coordinates are integral 
	coordinates on the X-Y plane, and the distance between two coordinates is 
	the Euclidean distance. The integer radius denotes the maximum distance in 
	which the tower is reachable. The tower is reachable if the distance is 
	less than or equal to radius. Outside that distance, the signal becomes 
	garbled, and the tower is not reachable. The signal quality of the ith 
	tower at a coordinate (x, y) is calculated with the formula ⌊qi / (1 + d)⌋, 
	where d is the distance between the tower and the coordinate. The network 
	quality at a coordinate is the sum of the signal qualities from all the 
	reachable towers. Return the integral coordinate where the network quality 
	is maximum. If there are multiple coordinates with the same network quality, 
	return the lexicographically minimum coordinate.

	Note:
	A coordinate (x1, y1) is lexicographically smaller than (x2, y2) if either 
	x1 < x2 or x1 == x2 and y1 < y2. ⌊val⌋ is the greatest integer less than or 
	equal to val (the floor function).

	Example 1:
	Input: towers = [[1,2,5],[2,1,7],[3,1,9]], radius = 2
	Output: [2,1]
	Explanation: 
	At coordinate (2, 1) the total quality is 13
	- Quality of 7 from (2, 1) results in ⌊7 / (1 + sqrt(0)⌋ = ⌊7⌋ = 7
	- Quality of 5 from (1, 2) results in ⌊5 / (1 + sqrt(2)⌋ = ⌊2.07⌋ = 2
	- Quality of 9 from (3, 1) results in ⌊9 / (1 + sqrt(1)⌋ = ⌊4.5⌋ = 4
	No other coordinate has higher quality.

	Example 2:
	Input: towers = [[23,11,21]], radius = 9
	Output: [23,11]

	Example 3:
	Input: towers = [[1,2,13],[2,1,7],[0,1,9]], radius = 2
	Output: [1,2]

	Example 4:
	Input: towers = [[2,1,9],[0,1,9]], radius = 2
	Output: [0,1]
	Explanation: Both (0, 1) and (2, 1) are optimal in terms of quality but 
	             (0, 1) is lexicograpically minimal.

	Constraints:
	* 1 <= towers.length <= 50
	* towers[i].length == 3
	* 0 <= xi, yi, qi <= 50
	* 1 <= radius <= 50"""

    def bestCoordinate(self, towers: List[List[int]], radius: int) -> List[int]:
        mx = -inf
        for x in range(51):
            for y in range(51): 
                val = 0
                for xi, yi, qi in towers: 
                    d = sqrt((x-xi)**2 + (y-yi)**2)
                    if d <= radius: val += int(qi/(1 + d))
                if val > mx: 
                    ans = [x, y]
                    mx = val
        return ans 


    """1621. Number of Sets of K Non-Overlapping Line Segments (Medium)
	Given n points on a 1-D plane, where the ith point (from 0 to n-1) is at 
	x = i, find the number of ways we can draw exactly k non-overlapping line 
	segments such that each segment covers two or more points. The endpoints of 
	each segment must have integral coordinates. The k line segments do not 
	have to cover all n points, and they are allowed to share endpoints. Return 
	the number of ways we can draw k non-overlapping line segments. Since this 
	number can be huge, return it modulo 10^9 + 7.

	Example 1:
	Input: n = 4, k = 2
	Output: 5
	Explanation: The two line segments are shown in red and blue. The image 
	             above shows the 5 different ways {(0,2),(2,3)}, {(0,1),(1,3)}, 
	             {(0,1),(2,3)}, {(1,2),(2,3)}, {(0,1),(1,2)}.

	Example 2:
	Input: n = 3, k = 1
	Output: 3
	Explanation: The 3 ways are {(0,1)}, {(0,2)}, {(1,2)}.
	
	Example 3:
	Input: n = 30, k = 7
	Output: 796297179
	Explanation: The total number of possible ways to draw 7 line segments is 
	             3796297200. Taking this number modulo 10^9 + 7 gives us 
	             796297179.

	Example 4:
	Input: n = 5, k = 3
	Output: 7
	
	Example 5:
	Input: n = 3, k = 2
	Output: 1

	Constraints:
	* 2 <= n <= 1000
	* 1 <= k <= n-1"""

    def numberOfSets(self, n: int, k: int) -> int:
        return comb(n+k-1, 2*k) % 1_000_000_007


    """1624. Largest Substring Between Two Equal Characters (Easy)
	Given a string s, return the length of the longest substring between two 
	equal characters, excluding the two characters. If there is no such 
	substring return -1. A substring is a contiguous sequence of characters 
	within a string.

	Example 1:
	Input: s = "aa"
	Output: 0
	Explanation: The optimal substring here is an empty substring between the 
	             two 'a's.

	Example 2:
	Input: s = "abca"
	Output: 2
	Explanation: The optimal substring here is "bc".

	Example 3:
	Input: s = "cbzxy"
	Output: -1
	Explanation: There are no characters that appear twice in s.

	Example 4:
	Input: s = "cabbac"
	Output: 4
	Explanation: The optimal substring here is "abba". Other non-optimal 
	             substrings include "bb" and "".

	Constraints:
	* 1 <= s.length <= 300
	* s contains only lowercase English letters."""

    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        ans, seen = -1, {}
        for i, c in enumerate(s): 
            ans = max(ans, i - seen.setdefault(c, i) - 1)
        return ans 


    """1625. Lexicographically Smallest String After Applying Operations (Medium)
	You are given a string s of even length consisting of digits from 0 to 9, 
	and two integers a and b. You can apply either of the following two 
	operations any number of times and in any order on s: 
	1) Add a to all odd indices of s (0-indexed). Digits post 9 are cycled back 
	   to 0. For example, if s = "3456" and a = 5, s becomes "3951".
	2) Rotate s to the right by b positions. For example, if s = "3456" and 
	   b = 1, s becomes "6345".
	Return the lexicographically smallest string you can obtain by applying the 
	above operations any number of times on s. A string a is lexicographically 
	smaller than a string b (of the same length) if in the first position where 
	a and b differ, string a has a letter that appears earlier in the alphabet 
	than the corresponding letter in b. For example, "0158" is lexicographically 
	smaller than "0190" because the first position they differ is at the third 
	letter, and '5' comes before '9'.

	Example 1:
	Input: s = "5525", a = 9, b = 2
	Output: "2050"
	Explanation: We can apply the following operations:
	Start:  "5525"
	Rotate: "2555"
	Add:    "2454"
	Add:    "2353"
	Rotate: "5323"
	Add:    "5222"
	​​​​​​​Add:    "5121"
	​​​​​​​Rotate: "2151"
	​​​​​​​Add:    "2050"​​​​​​​​​​​​
	There is no way to obtain a string that is lexicographically smaller then 
	"2050".

	Example 2:
	Input: s = "74", a = 5, b = 1
	Output: "24"
	Explanation: We can apply the following operations:
	Start:  "74"
	Rotate: "47"
	​​​​​​​Add:    "42"
	​​​​​​​Rotate: "24"​​​​​​​​​​​​
	There is no way to obtain a string that is lexicographically smaller then 
	"24".

	Example 3:
	Input: s = "0011", a = 4, b = 2
	Output: "0011"
	Explanation: There are no sequence of operations that will give us a 
	             lexicographically smaller string than "0011".

	Example 4:
	Input: s = "43987654", a = 7, b = 3
	Output: "00553311"
	 
	Constraints:
	* 2 <= s.length <= 100
	* s.length is even.
	* s consists of digits from 0 to 9 only.
	* 1 <= a <= 9
	* 1 <= b <= s.length - 1"""

    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        op1 = lambda s: "".join(str((int(c)+a)%10) if i&1 else c for i, c in enumerate(s))
        op2 = lambda s: s[-b:] + s[:-b]
        
        seen = set()
        stack = [s]
        while stack: 
            s = stack.pop()
            seen.add(s)
            if (ss := op1(s)) not in seen: stack.append(ss)
            if (ss := op2(s)) not in seen: stack.append(ss)
        return min(seen)


    """1626. Best Team With No Conflicts (Medium)
	You are the manager of a basketball team. For the upcoming tournament, you 
	want to choose the team with the highest overall score. The score of the 
	team is the sum of scores of all the players in the team. However, the 
	basketball team is not allowed to have conflicts. A conflict exists if a 
	younger player has a strictly higher score than an older player. A conflict 
	does not occur between players of the same age. Given two lists, scores and 
	ages, where each scores[i] and ages[i] represents the score and age of the 
	ith player, respectively, return the highest overall score of all possible 
	basketball teams.

	Example 1:
	Input: scores = [1,3,5,10,15], ages = [1,2,3,4,5]
	Output: 34
	Explanation: You can choose all the players.

	Example 2:
	Input: scores = [4,5,6,5], ages = [2,1,2,1]
	Output: 16
	Explanation: It is best to choose the last 3 players. Notice that you are 
	             allowed to choose multiple people of the same age.

	Example 3:
	Input: scores = [1,2,3,5], ages = [8,9,10,1]
	Output: 6
	Explanation: It is best to choose the first 3 players. 
	 
	Constraints:
	* 1 <= scores.length, ages.length <= 1000
	* scores.length == ages.length
	* 1 <= scores[i] <= 106
	* 1 <= ages[i] <= 1000"""

    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        ages, scores = zip(*sorted(zip(ages, scores)))
        
        @lru_cache(None)
        def fn(i): 
            """Return max score up to ith player included."""
            if i < 0: return 0 # boundary condition 
            return scores[i] + max((fn(ii) for ii in range(i) if ages[ii] == ages[i] or scores[ii] <= scores[i]), default=0)
        
        return max(fn(i) for i in range(len(scores)))


    """1627. Graph Connectivity With Threshold (Hard)
	We have n cities labeled from 1 to n. Two different cities with labels x 
	and y are directly connected by a bidirectional road if and only if x and y 
	share a common divisor strictly greater than some threshold. More formally, 
	cities with labels x and y have a road between them if there exists an 
	integer z such that all of the following are true:
	x % z == 0,
	y % z == 0, and
	z > threshold.
	Given the two integers, n and threshold, and an array of queries, you must 
	determine for each queries[i] = [ai, bi] if cities ai and bi are connected 
	(i.e. there is some path between them). Return an array answer, where 
	answer.length == queries.length and answer[i] is true if for the ith query, 
	there is a path between ai and bi, or answer[i] is false if there is no 
	path.

	Example 1:
	Input: n = 6, threshold = 2, queries = [[1,4],[2,5],[3,6]]
	Output: [false,false,true]
	Explanation: The divisors for each number:
	1:   1
	2:   1, 2
	3:   1, 3
	4:   1, 2, 4
	5:   1, 5
	6:   1, 2, 3, 6
	Using the underlined divisors above the threshold, only cities 3 and 6 
	share a common divisor, so they are the only ones directly connected. The 
	result of each query:
	[1,4]   1 is not connected to 4
	[2,5]   2 is not connected to 5
	[3,6]   3 is connected to 6 through path 3--6

	Example 2:
	Input: n = 6, threshold = 0, queries = [[4,5],[3,4],[3,2],[2,6],[1,3]]
	Output: [true,true,true,true,true]
	Explanation: The divisors for each number are the same as the previous 
	             example. However, since the threshold is 0, all divisors can 
	             be used. Since all numbers share 1 as a divisor, all cities 
	             are connected.
	
	Example 3:
	Input: n = 5, threshold = 1, queries = [[4,5],[4,5],[3,2],[2,3],[3,4]]
	Output: [false,false,false,false,false]
	Explanation: Only cities 2 and 4 share a common divisor 2 which is strictly 
	             greater than the threshold 1, so they are the only ones 
	             directly connected.
	Please notice that there can be multiple queries for the same pair of nodes 
	[x, y], and that the query [x, y] is equivalent to the query [y, x].

	Constraints:
	* 2 <= n <= 104
	* 0 <= threshold <= n
	* 1 <= queries.length <= 105
	* queries[i].length == 2
	* 1 <= ai, bi <= cities
	* ai != bi"""

""" 
 	class UnionFind:
	    def __init__(self, n):
	        self.parent = list(range(n))
	        self.rank = [1]*n
	        
	    def find(self, p): 
	        if self.parent[p] != p:
	            self.parent[p] = self.find(self.parent[p]) # path compression 
	        return self.parent[p]
	    
	    def union(self, p, q): 
	        prt, qrt = self.find(p), self.find(q)
	        if prt == qrt: return False
	        if self.rank[prt] > self.rank[qrt]: prt, qrt = qrt, prt # union with ranking 
	        self.parent[prt] = qrt
	        self.rank[qrt] += self.rank[prt]
	        return True 
"""

    def areConnected(self, n: int, threshold: int, queries: List[List[int]]) -> List[bool]:
        uf = UnionFind(n)
        
        for u in range(threshold+1, n+1):
            for v in range(u*2, n+1, u): 
                uf.union(u-1, v-1)
        
        return [uf.find(u-1) == uf.find(v-1) for u, v in queries]


    """1629. Slowest Key (Easy)
	A newly designed keypad was tested, where a tester pressed a sequence of n 
	keys, one at a time. You are given a string keysPressed of length n, where 
	keysPressed[i] was the ith key pressed in the testing sequence, and a 
	sorted list releaseTimes, where releaseTimes[i] was the time the ith key 
	was released. Both arrays are 0-indexed. The 0th key was pressed at the 
	time 0, and every subsequent key was pressed at the exact time the previous 
	key was released. The tester wants to know the key of the keypress that had 
	the longest duration. The ith keypress had a duration of 
	releaseTimes[i] - releaseTimes[i - 1], and the 0th keypress had a duration 
	of releaseTimes[0]. Note that the same key could have been pressed multiple 
	times during the test, and these multiple presses of the same key may not 
	have had the same duration. Return the key of the keypress that had the 
	longest duration. If there are multiple such keypresses, return the 
	lexicographically largest key of the keypresses.

	Example 1:
	Input: releaseTimes = [9,29,49,50], keysPressed = "cbcd"
	Output: "c"
	Explanation: The keypresses were as follows:
	1) Keypress for 'c' had a duration of 9 (pressed at time 0 and released at 
	   time 9).
	2) Keypress for 'b' had a duration of 29 - 9 = 20 (pressed at time 9 right 
	   after the release of the previous character and released at time 29).
	3) Keypress for 'c' had a duration of 49 - 29 = 20 (pressed at time 29 
	   right after the release of the previous character and released at time 
	   49).
	4) Keypress for 'd' had a duration of 50 - 49 = 1 (pressed at time 49 right 
	   after the release of the previous character and released at time 50).
	The longest of these was the keypress for 'b' and the second keypress for 
	'c', both with duration 20. 'c' is lexicographically larger than 'b', so 
	the answer is 'c'.

	Example 2:
	Input: releaseTimes = [12,23,36,46,62], keysPressed = "spuda"
	Output: "a"
	Explanation: The keypresses were as follows:
	Keypress for 's' had a duration of 12.
	Keypress for 'p' had a duration of 23 - 12 = 11.
	Keypress for 'u' had a duration of 36 - 23 = 13.
	Keypress for 'd' had a duration of 46 - 36 = 10.
	Keypress for 'a' had a duration of 62 - 46 = 16.
	The longest of these was the keypress for 'a' with duration 16.

	Constraints:
	* releaseTimes.length == n
	* keysPressed.length == n
	* 2 <= n <= 1000
	* 0 <= releaseTimes[i] <= 109
	* releaseTimes[i] < releaseTimes[i+1]
	* keysPressed contains only lowercase English letters."""

    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        ans, mx = "", 0
        for i, (t, k) in enumerate(zip(releaseTimes, keysPressed)):
            if i: t -= releaseTimes[i-1]
            if t > mx or t == mx and k > ans: ans, mx = k, t # update 
        return ans 


    """1630. Arithmetic Subarrays (Medium)
	A sequence of numbers is called arithmetic if it consists of at least two 
	elements, and the difference between every two consecutive elements is the 
	same. More formally, a sequence s is arithmetic if and only if 
	s[i+1] - s[i] == s[1] - s[0] for all valid i.

	For example, these are arithmetic sequences:
	1, 3, 5, 7, 9
	7, 7, 7, 7
	3, -1, -5, -9
	The following sequence is not arithmetic: 1, 1, 2, 5, 7
	You are given an array of n integers, nums, and two arrays of m integers 
	each, l and r, representing the m range queries, where the ith query is the 
	range [l[i], r[i]]. All the arrays are 0-indexed. Return a list of boolean 
	elements answer, where answer[i] is true if the subarray nums[l[i]], 
	nums[l[i]+1], ... , nums[r[i]] can be rearranged to form an arithmetic 
	sequence, and false otherwise.

	Example 1:
	Input: nums = [4,6,5,9,3,7], l = [0,0,2], r = [2,3,5]
	Output: [true,false,true]
	Explanation:
	In the 0th query, the subarray is [4,6,5]. This can be rearranged as [6,5,4], which is an arithmetic sequence.
	In the 1st query, the subarray is [4,6,5,9]. This cannot be rearranged as an arithmetic sequence.
	In the 2nd query, the subarray is [5,9,3,7]. This can be rearranged as [3,5,7,9], which is an arithmetic sequence.

	Example 2:
	Input: nums = [-12,-9,-3,-12,-6,15,20,-25,-20,-15,-10], l = [0,1,6,4,8,7], r = [4,4,9,7,9,10]
	Output: [false,true,false,false,true,true]

	Constraints:
	* n == nums.length
	* m == l.length
	* m == r.length
	* 2 <= n <= 500
	* 1 <= m <= 500
	* 0 <= l[i] < r[i] < n
	* -10^5 <= nums[i] <= 10^5"""

    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        ans = []
        for ll, rr in zip(l, r): 
            seq = sorted(nums[ll:rr+1])
            ans.append(len(set(seq[i] - seq[i-1] for i in range(1, len(seq)))) == 1)
        return ans 


    """1631. Path With Minimum Effort (Medium)
	You are a hiker preparing for an upcoming hike. You are given heights, a 2D 
	array of size rows x columns, where heights[row][col] represents the height 
	of cell (row, col). You are situated in the top-left cell, (0, 0), and you 
	hope to travel to the bottom-right cell, (rows-1, columns-1) (i.e., 
	0-indexed). You can move up, down, left, or right, and you wish to find a 
	route that requires the minimum effort. A route's effort is the maximum 
	absolute difference in heights between two consecutive cells of the route. 
	Return the minimum effort required to travel from the top-left cell to the 
	bottom-right cell.

	Example 1:
	Input: heights = [[1,2,2],[3,8,2],[5,3,5]]
	Output: 2
	Explanation: The route of [1,3,5,3,5] has a maximum absolute difference of 
	             2 in consecutive cells. This is better than the route of 
	             [1,2,2,2,5], where the maximum absolute difference is 3.

	Example 2:
	Input: heights = [[1,2,3],[3,8,4],[5,3,5]]
	Output: 1
	Explanation: The route of [1,2,3,4,5] has a maximum absolute difference of 
	             1 in consecutive cells, which is better than route [1,3,5,3,5].
	
	Example 3:
	Input: heights = [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]
	Output: 0

	Explanation: This route does not require any effort.

	Constraints:
	* rows == heights.length
	* columns == heights[i].length
	* 1 <= rows, columns <= 100
	* 1 <= heights[i][j] <= 106"""

    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m, n = len(heights), len(heights[0])
        seen = [[inf]*n for _ in heights] # lowest height seen
        hp = [(0, 0, 0)] # height|row|column 
        while hp: 
            h, i, j = heappop(hp)
            if i == m-1 and j == n-1: return h # end condition 
            if h < seen[i][j]: 
                seen[i][j] = h
                for ii, jj in (i-1, j), (i, j-1), (i, j+1), (i+1, j): 
                    if 0 <= ii < m and 0 <= jj < n: 
                        hh = max(h, abs(heights[ii][jj] - heights[i][j]))
                        if hh < seen[ii][jj]: heappush(hp, (hh, ii, jj))


    """1632. Rank Transform of a Matrix (Hard)
	Given an m x n matrix, return a new matrix answer where answer[row][col] is 
	the rank of matrix[row][col]. The rank is an integer that represents how 
	large an element is compared to other elements. It is calculated using the 
	following rules:
	* The rank is an integer starting from 1.
	* If two elements p and q are in the same row or column, then:
		- If p < q then rank(p) < rank(q)
		- If p == q then rank(p) == rank(q)
		- If p > q then rank(p) > rank(q)
	* The rank should be as small as possible.
	It is guaranteed that answer is unique under the given rules.

	Example 1:
	Input: matrix = [[1,2],[3,4]]
	Output: [[1,2],[2,3]]
	Explanation:
	The rank of matrix[0][0] is 1 because it is the smallest integer in its row and column.
	The rank of matrix[0][1] is 2 because matrix[0][1] > matrix[0][0] and matrix[0][0] is rank 1.
	The rank of matrix[1][0] is 2 because matrix[1][0] > matrix[0][0] and matrix[0][0] is rank 1.
	The rank of matrix[1][1] is 3 because matrix[1][1] > matrix[0][1], matrix[1][1] > matrix[1][0], and both matrix[0][1] and matrix[1][0] are rank 2.

	Example 2:
	Input: matrix = [[7,7],[7,7]]
	Output: [[1,1],[1,1]]

	Example 3:
	Input: matrix = [[20,-21,14],[-19,4,19],[22,-47,24],[-19,4,19]]
	Output: [[4,2,3],[1,3,4],[5,1,6],[1,3,4]]

	Example 4:
	Input: matrix = [[7,3,6],[1,4,5],[9,8,2]]
	Output: [[5,1,4],[1,2,3],[6,3,1]]

	Constraints:
	* m == matrix.length
	* n == matrix[i].length
	* 1 <= m, n <= 500
	* -10^9 <= matrix[row][col] <= 10^9"""

    def matrixRankTransform(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0]) # dimension 
        # mapping from value to index 
        mp = {} 
        for i in range(m):
            for j in range(n): 
                mp.setdefault(matrix[i][j], []).append((i, j))
        
        def find(p):
            """Find root of p."""
            if p != parent[p]:
                parent[p] = find(parent[p])
            return parent[p]
        
        rank = [0]*(m+n)
        ans = [[0]*n for _ in range(m)]
        
        for k in sorted(mp): # from minimum to maximum 
            parent = list(range(m+n))
            for i, j in mp[k]: 
                ii, jj = find(i), find(m+j) # find 
                parent[ii] = jj # union 
                rank[jj] = max(rank[ii], rank[jj]) # max rank 
            
            seen = set()
            for i, j in mp[k]:
                ii = find(i)
                if ii not in seen: rank[ii] += 1
                seen.add(ii)
                rank[i] = rank[m+j] = ans[i][j] = rank[ii]
        return ans 


    """1634. Add Two Polynomials Represented as Linked Lists (Medium)
	A polynomial linked list is a special type of linked list where every node 
	represents a term in a polynomial expression. Each node has three attributes:
	* coefficient: an integer representing the number multiplier of the term. 
	  The coefficient of the term 9x4 is 9.
	* power: an integer representing the exponent. The power of the term 9x4 is 
	  4.
	* next: a pointer to the next node in the list, or null if it is the last 
	  node of the list.
	The polynomial linked list must be in its standard form: the polynomial 
	must be in strictly descending order by its power value. Also, terms with a 
	coefficient of 0 are omitted. Given two polynomial linked list heads, poly1 
	and poly2, add the polynomials together and return the head of the sum of 
	the polynomials.

	PolyNode format: The input/output format is as a list of n nodes, where 
	                 each node is represented as its [coefficient, power]. For 
	                 example, the polynomial 5x3 + 4x - 7 would be represented 
	                 as: [[5,3],[4,1],[-7,0]].

	Example 1:
	Input: poly1 = [[1,1]], poly2 = [[1,0]]
	Output: [[1,1],[1,0]]
	Explanation: poly1 = x. poly2 = 1. The sum is x + 1.

	Example 2:
	Input: poly1 = [[2,2],[4,1],[3,0]], poly2 = [[3,2],[-4,1],[-1,0]]
	Output: [[5,2],[2,0]]
	Explanation: poly1 = 2x2 + 4x + 3. 
	             poly2 = 3x2 - 4x - 1. 
	             The sum is 5x2 + 2. Notice that we omit the "0x" term.

	Example 3:
	Input: poly1 = [[1,2]], poly2 = [[-1,2]]
	Output: []
	Explanation: The sum is 0. We return an empty list.
	 
	Constraints:
	* 0 <= n <= 10^4
	* -10^9 <= PolyNode.coefficient <= 10^9
	* PolyNode.coefficient != 0
	* 0 <= PolyNode.power <= 10^9
	* PolyNode.power > PolyNode.next.power"""

    def addPoly(self, poly1: 'PolyNode', poly2: 'PolyNode') -> 'PolyNode':
        dummy = node = PolyNode() 
        while poly1 and poly2: 
            if poly1.power > poly2.power: 
                node.next = node = poly1
                poly1 = poly1.next 
            elif poly1.power < poly2.power: 
                node.next = node = poly2
                poly2 = poly2.next 
            else: 
                coef = poly1.coefficient + poly2.coefficient
                if coef: node.next = node = PolyNode(coef, poly1.power)
                poly1 = poly1.next 
                poly2 = poly2.next 
        node.next = poly1 or poly2
        return dummy.next 


    """1636. Sort Array by Increasing Frequency (Easy)
	Given an array of integers nums, sort the array in increasing order based 
	on the frequency of the values. If multiple values have the same frequency, 
	sort them in decreasing order. Return the sorted array.

	Example 1:
	Input: nums = [1,1,2,2,2,3]
	Output: [3,1,1,2,2,2]
	Explanation: '3' has a frequency of 1, '1' has a frequency of 2, and '2' 
	             has a frequency of 3.

	Example 2:
	Input: nums = [2,3,1,3,2]
	Output: [1,3,3,2,2]
	Explanation: '2' and '3' both have a frequency of 2, so they are sorted in 
	             decreasing order.

	Example 3:
	Input: nums = [-1,1,-6,4,5,-6,1,4,1]
	Output: [5,-1,4,4,-6,-6,1,1,1]
	 
	Constraints:
	* 1 <= nums.length <= 100
	* -100 <= nums[i] <= 100"""

    def frequencySort(self, nums: List[int]) -> List[int]:
        freq = {}
        for x in nums: freq[x] = 1 + freq.get(x, 0)
        return sorted(nums, key=lambda x: (freq[x], -x))


    """1637. Widest Vertical Area Between Two Points Containing No Points (Medium)
	Given n points on a 2D plane where points[i] = [xi, yi], Return the widest 
	vertical area between two points such that no points are inside the area. A 
	vertical area is an area of fixed-width extending infinitely along the y-axis 
	(i.e., infinite height). The widest vertical area is the one with the maximum 
	width. Note that points on the edge of a vertical area are not considered 
	included in the area.

	Example 1:
	Input: points = [[8,7],[9,9],[7,4],[9,7]]
	Output: 1
	Explanation: Both the red and the blue area are optimal.

	Example 2:
	Input: points = [[3,1],[9,0],[1,0],[1,4],[5,3],[8,8]]
	Output: 3

	Constraints:
	* n == points.length
	* 2 <= n <= 10^5
	* points[i].length == 2
	* 0 <= xi, yi <= 10^9"""

    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        vals = sorted(x for x, _ in points)
        return max(vals[i] - vals[i-1] for i in range(1, len(vals)))


    """1638. Count Substrings That Differ by One Character (Medium)
	Given two strings s and t, find the number of ways you can choose a non-
	empty substring of s and replace a single character by a different 
	character such that the resulting substring is a substring of t. In other 
	words, find the number of substrings in s that differ from some substring 
	in t by exactly one character. For example, the underlined substrings in 
	"computer" and "computation" only differ by the 'e'/'a', so this is a valid 
	way. Return the number of substrings that satisfy the condition above. A 
	substring is a contiguous sequence of characters within a string.

	Example 1:
	Input: s = "aba", t = "baba"
	Output: 6
	Explanation: The following are the pairs of substrings from s and t that differ by exactly 1 character:
	("aba", "baba")
	("aba", "baba")
	("aba", "baba")
	("aba", "baba")
	("aba", "baba")
	("aba", "baba")
	The underlined portions are the substrings that are chosen from s and t.

	​​Example 2:
	Input: s = "ab", t = "bb"
	Output: 3
	Explanation: The following are the pairs of substrings from s and t that differ by 1 character:
	("ab", "bb")
	("ab", "bb")
	("ab", "bb")
	​​​​The underlined portions are the substrings that are chosen from s and t.

	Example 3:
	Input: s = "a", t = "a"
	Output: 0

	Example 4:
	Input: s = "abe", t = "bbc"
	Output: 10

	Constraints:
	* 1 <= s.length, t.length <= 100
	* s and t consist of lowercase English letters only."""

    def countSubstrings(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        dp0 = [[0]*(n+1) for _ in range(m+1)] # 0-mismatch
        dp1 = [[0]*(n+1) for _ in range(m+1)] # 1-mismatch
        
        ans = 0
        for i in range(m):
            for j in range(n):
                if s[i] == t[j]: 
                    dp0[i+1][j+1] = 1 + dp0[i][j]
                    dp1[i+1][j+1] = dp1[i][j]
                else: 
                    dp0[i+1][j+1] = 0
                    dp1[i+1][j+1] = 1 + dp0[i][j]
                ans += dp1[i+1][j+1]
        return ans 


    """1639. Number of Ways to Form a Target String Given a Dictionary (Hard)
	You are given a list of strings of the same length words and a string 
	target. Your task is to form target using the given words under the 
	following rules:
	* target should be formed from left to right.
	* To form the ith character (0-indexed) of target, you can choose the kth 
	  character of the jth string in words if target[i] = words[j][k].
	* Once you use the kth character of the jth string of words, you can no 
	  longer use the xth character of any string in words where x <= k. In 
	  other words, all characters to the left of or at index k become unusuable 
	  for every string.
	* Repeat the process until you form the string target.
	Notice that you can use multiple characters from the same string in words 
	provided the conditions above are met. Return the number of ways to form 
	target from words. Since the answer may be too large, return it modulo 
	10^9 + 7.

	Example 1:
	Input: words = ["acca","bbbb","caca"], target = "aba"
	Output: 6
	Explanation: There are 6 ways to form target.
	"aba" -> index 0 ("acca"), index 1 ("bbbb"), index 3 ("caca")
	"aba" -> index 0 ("acca"), index 2 ("bbbb"), index 3 ("caca")
	"aba" -> index 0 ("acca"), index 1 ("bbbb"), index 3 ("acca")
	"aba" -> index 0 ("acca"), index 2 ("bbbb"), index 3 ("acca")
	"aba" -> index 1 ("caca"), index 2 ("bbbb"), index 3 ("acca")
	"aba" -> index 1 ("caca"), index 2 ("bbbb"), index 3 ("caca")

	Example 2:
	Input: words = ["abba","baab"], target = "bab"
	Output: 4
	Explanation: There are 4 ways to form target.
	"bab" -> index 0 ("baab"), index 1 ("baab"), index 2 ("abba")
	"bab" -> index 0 ("baab"), index 1 ("baab"), index 3 ("baab")
	"bab" -> index 0 ("baab"), index 2 ("baab"), index 3 ("baab")
	"bab" -> index 1 ("abba"), index 2 ("baab"), index 3 ("baab")

	Example 3:
	Input: words = ["abcd"], target = "abcd"
	Output: 1

	Example 4:
	Input: words = ["abab","baba","abba","baab"], target = "abba"
	Output: 16

	Constraints:
	* 1 <= words.length <= 1000
	* 1 <= words[i].length <= 1000
	* All strings in words have the same length.
	* 1 <= target.length <= 1000
	* words[i] and target contain only lowercase English letters."""

    def numWays(self, words: List[str], target: str) -> int:
        freq = [defaultdict(int) for _ in range(len(words[0]))]
        for word in words: 
            for i, c in enumerate(word): 
                freq[i][c] += 1
        
        @cache
        def fn(i, k): 
            """Return number of ways to form target[i:] w/ col k."""
            if i == len(target): return 1
            if k == len(words[0]): return 0 
            return freq[k][target[i]]*fn(i+1, k+1) + fn(i, k+1)
        
        return fn(0, 0) % 1_000_000_007


    """1640. Check Array Formation Through Concatenation (Easy)
	You are given an array of distinct integers arr and an array of integer 
	arrays pieces, where the integers in pieces are distinct. Your goal is to 
	form arr by concatenating the arrays in pieces in any order. However, you 
	are not allowed to reorder the integers in each array pieces[i]. Return 
	true if it is possible to form the array arr from pieces. Otherwise, return 
	false.

	Example 1:
	Input: arr = [85], pieces = [[85]]
	Output: true

	Example 2:
	Input: arr = [15,88], pieces = [[88],[15]]
	Output: true
	Explanation: Concatenate [15] then [88]

	Example 3:
	Input: arr = [49,18,16], pieces = [[16,18,49]]
	Output: false
	Explanation: Even though the numbers match, we cannot reorder pieces[0].

	Example 4:
	Input: arr = [91,4,64,78], pieces = [[78],[4,64],[91]]
	Output: true
	Explanation: Concatenate [91] then [4,64] then [78]

	Example 5:
	Input: arr = [1,3,5,7], pieces = [[2,4,6,8]]
	Output: false

	Constraints:
	* 1 <= pieces.length <= arr.length <= 100
	* sum(pieces[i].length) == arr.length
	* 1 <= pieces[i].length <= arr.length
	* 1 <= arr[i], pieces[i][j] <= 100
	* The integers in arr are distinct.
	* The integers in pieces are distinct (i.e., If we flatten pieces in a 1D 
	  array, all the integers in this array are distinct)."""

    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        mp = {x[0]: x for x in pieces}
        return sum((mp.get(x, []) for x in arr), []) == arr


    """1641. Count Sorted Vowel Strings (Medium)
	Given an integer n, return the number of strings of length n that consist 
	only of vowels (a, e, i, o, u) and are lexicographically sorted. A string s 
	is lexicographically sorted if for all valid i, s[i] is the same as or 
	comes before s[i+1] in the alphabet.

	Example 1:
	Input: n = 1
	Output: 5
	Explanation: The 5 sorted strings that consist of vowels only are ["a","e","i","o","u"].

	Example 2:
	Input: n = 2
	Output: 15
	Explanation: The 15 sorted strings that consist of vowels only are
	["aa","ae","ai","ao","au","ee","ei","eo","eu","ii","io","iu","oo","ou","uu"].
	Note that "ea" is not a valid string since 'e' comes after 'a' in the alphabet.

	Example 3:
	Input: n = 33
	Output: 66045

	Constraints: 1 <= n <= 50 """

    def countVowelStrings(self, n: int) -> int:
        
        @lru_cache(None)
        def fn(n, k): 
            """Return number of sorted strings of length n consisting of k vowels."""
            if n == 1: return k # base case 
            return sum(fn(n-1, kk) for kk in range(1, k+1))
        
        return fn(n, 5)


    """1642. Furthest Building You Can Reach (Medium)
	You are given an integer array heights representing the heights of 
	buildings, some bricks, and some ladders. You start your journey from 
	building 0 and move to the next building by possibly using bricks or 
	ladders. While moving from building i to building i+1 (0-indexed),
	* If the current building's height is greater than or equal to the next 
	  building's height, you do not need a ladder or bricks.
	* If the current building's height is less than the next building's height, 
	  you can either use one ladder or (h[i+1] - h[i]) bricks.
	Return the furthest building index (0-indexed) you can reach if you use the 
	given ladders and bricks optimally.

	Example 1:
	Input: heights = [4,2,7,6,9,14,12], bricks = 5, ladders = 1
	Output: 4
	Explanation: Starting at building 0, you can follow these steps:
	- Go to building 1 without using ladders nor bricks since 4 >= 2.
	- Go to building 2 using 5 bricks. You must use either bricks or ladders because 2 < 7.
	- Go to building 3 without using ladders nor bricks since 7 >= 6.
	- Go to building 4 using your only ladder. You must use either bricks or ladders because 6 < 9.
	It is impossible to go beyond building 4 because you do not have any more bricks or ladders.

	Example 2:
	Input: heights = [4,12,2,7,3,18,20,3,19], bricks = 10, ladders = 2
	Output: 7

	Example 3:
	Input: heights = [14,3,19,3], bricks = 17, ladders = 0
	Output: 3

	Constraints:
	* 1 <= heights.length <= 105
	* 1 <= heights[i] <= 106
	* 0 <= bricks <= 109
	* 0 <= ladders <= heights.length"""

    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        pq = [] # max heap (priority queue)
        for i in range(1, len(heights)): 
            ht = heights[i] - heights[i-1] # height diff 
            if ht > 0:  
                heappush(pq, -ht)
                bricks -= ht
                if bricks < 0: # not enough bricks
                    if ladders == 0: return i-1 # i not reachable
                    bricks += -heappop(pq) # swapping ladder with most bricks 
                    ladders -= 1
        return i 


    """1643. Kth Smallest Instructions (Hard)
	Bob is standing at cell (0, 0), and he wants to reach destination: 
	(row, column). He can only travel right and down. You are going to help Bob 
	by providing instructions for him to reach destination. The instructions 
	are represented as a string, where each character is either:
	* 'H', meaning move horizontally (go right), or
	* 'V', meaning move vertically (go down).
	Multiple instructions will lead Bob to destination. For example, if 
	destination is (2, 3), both "HHHVV" and "HVHVH" are valid instructions. 
	However, Bob is very picky. Bob has a lucky number k, and he wants the kth 
	lexicographically smallest instructions that will lead him to destination. 
	k is 1-indexed. Given an integer array destination and an integer k, return 
	the kth lexicographically smallest instructions that will take Bob to destination.

	Example 1:
	Input: destination = [2,3], k = 1
	Output: "HHHVV"
	Explanation: All the instructions that reach (2, 3) in lexicographic order are as follows:
	["HHHVV", "HHVHV", "HHVVH", "HVHHV", "HVHVH", "HVVHH", "VHHHV", "VHHVH", "VHVHH", "VVHHH"].

	Example 2:
	Input: destination = [2,3], k = 2
	Output: "HHVHV"

	Example 3:
	Input: destination = [2,3], k = 3
	Output: "HHVVH"

	Constraints:
	* destination.length == 2
	* 1 <= row, column <= 15
	* 1 <= k <= nCr(row + column, row), where nCr(a, b) denotes a choose b​​​​​."""

    def kthSmallestPath(self, destination: List[int], k: int) -> str:
        m, n = destination # m "V" & n "H" in total 
        ans = ""
        while n: 
            kk = comb(m+n-1, n-1) # (m+n-1 choose n-1) instructions starting with "H"  
            if kk >= k: 
                ans += "H"
                n -= 1
            else: 
                ans += "V"
                m -= 1
                k -= kk 
        return ans + m*"V"


    """1644. Lowest Common Ancestor of a Binary Tree II (Medium)
	Given the root of a binary tree, return the lowest common ancestor (LCA) 
	of two given nodes, p and q. If either node p or q does not exist in the 
	tree, return null. All values of the nodes in the tree are unique. 
	According to the definition of LCA on Wikipedia: "The lowest common 
	ancestor of two nodes p and q in a binary tree T is the lowest node that 
	has both p and q as descendants (where we allow a node to be a descendant 
	of itself)". A descendant of a node x is a node y that is on the path from 
	node x to some leaf node.

	Example 1:
	Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
	Output: 3
	Explanation: The LCA of nodes 5 and 1 is 3.

	Example 2:
	Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
	Output: 5
	Explanation: The LCA of nodes 5 and 4 is 5. A node can be a descendant of 
	             itself according to the definition of LCA.

	Example 3:
	Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 10
	Output: null
	Explanation: Node 10 does not exist in the tree, so return null.

	Constraints:
	* The number of nodes in the tree is in the range [1, 104].
	* -10^9 <= Node.val <= 10^9
	* All Node.val are unique.
	* p != q

	Follow up: Can you find the LCA traversing the tree, without checking nodes 
	           existence?"""

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def fn(node):
            """Return LCA of p and q in sub-tree rooted at node (if found)."""
            if node: 
                (ln, lx), (rn, rx) = fn(node.left), fn(node.right)
                if node in (p, q): return node, 1 + lx + rx
                if ln and rn: return node, lx + rx
                return (ln, lx) if ln else (rn, rx)
            return None, 0
            
        ans, x = fn(root)
        return ans if x == 2 else None 


    """1646. Get Maximum in Generated Array (Easy)
	You are given an integer n. An array nums of length n + 1 is generated in 
	the following way:
	* nums[0] = 0
	* nums[1] = 1
	* nums[2 * i] = nums[i] when 2 <= 2 * i <= n
	* nums[2 * i + 1] = nums[i] + nums[i + 1] when 2 <= 2 * i + 1 <= n
	Return the maximum integer in the array nums​​​.

	Example 1:
	Input: n = 7
	Output: 3
	Explanation: According to the given rules:
	  nums[0] = 0
	  nums[1] = 1
	  nums[(1 * 2) = 2] = nums[1] = 1
	  nums[(1 * 2) + 1 = 3] = nums[1] + nums[2] = 1 + 1 = 2
	  nums[(2 * 2) = 4] = nums[2] = 1
	  nums[(2 * 2) + 1 = 5] = nums[2] + nums[3] = 1 + 2 = 3
	  nums[(3 * 2) = 6] = nums[3] = 2
	  nums[(3 * 2) + 1 = 7] = nums[3] + nums[4] = 2 + 1 = 3
	Hence, nums = [0,1,1,2,1,3,2,3], and the maximum is 3.

	Example 2:
	Input: n = 2
	Output: 1
	Explanation: According to the given rules, the maximum between nums[0], 
	             nums[1], and nums[2] is 1.

	Example 3:
	Input: n = 3
	Output: 2
	Explanation: According to the given rules, the maximum between nums[0], 
	             nums[1], nums[2], and nums[3] is 2.

	Constraints:
	* 0 <= n <= 100"""

    def getMaximumGenerated(self, n: int) -> int:
        if not n: return 0 # edge case 
        nums = [0, 1]
        for i in range(2, n+1): 
            if i&1: nums.append(nums[i//2] + nums[i//2+1])
            else: nums.append(nums[i//2])
        return max(nums)


    """1647. Minimum Deletions to Make Character Frequencies Unique (Medium)
	A string s is called good if there are no two different characters in s 
	that have the same frequency. Given a string s, return the minimum number 
	of characters you need to delete to make s good. The frequency of a 
	character in a string is the number of times it appears in the string. For 
	example, in the string "aab", the frequency of 'a' is 2, while the 
	frequency of 'b' is 1.

	Example 1:
	Input: s = "aab"
	Output: 0
	Explanation: s is already good.

	Example 2:
	Input: s = "aaabbbcc"
	Output: 2
	Explanation: You can delete two 'b's resulting in the good string "aaabcc". 
	             Another way it to delete one 'b' and one 'c' resulting in the 
	             good string "aaabbc".

	Example 3:
	Input: s = "ceabaacb"
	Output: 2
	Explanation: You can delete both 'c's resulting in the good string "eabaab". 
	             Note that we only care about characters that are still in the 
	             string at the end (i.e. frequency of 0 is ignored).

	Constraints:
	* 1 <= s.length <= 105
	* s contains only lowercase English letters."""

    def minDeletions(self, s: str) -> int:
        freq = {} # frequency table 
        for c in s: freq[c] = 1 + freq.get(c, 0)
        
        ans = 0
        seen = set()
        for k in freq.values(): 
            while k in seen: 
                k -= 1 
                ans += 1
            if k: seen.add(k)
        return ans 


    """1648. Sell Diminishing-Valued Colored Balls (Medium)
	You have an inventory of different colored balls, and there is a customer 
	that wants orders balls of any color. The customer weirdly values the 
	colored balls. Each colored ball's value is the number of balls of that 
	color you currently have in your inventory. For example, if you own 6 
	yellow balls, the customer would pay 6 for the first yellow ball. After the 
	transaction, there are only 5 yellow balls left, so the next yellow ball is 
	then valued at 5 (i.e., the value of the balls decreases as you sell more 
	to the customer). You are given an integer array, inventory, where 
	inventory[i] represents the number of balls of the ith color that you 
	initially own. You are also given an integer orders, which represents the 
	total number of balls that the customer wants. You can sell the balls in 
	any order. Return the maximum total value that you can attain after selling 
	orders colored balls. As the answer may be too large, return it modulo 
	10^9 + 7.

	Example 1:
	Input: inventory = [2,5], orders = 4
	Output: 14
	Explanation: Sell the 1st color 1 time (2) and the 2nd color 3 times 
	             (5 + 4 + 3). The maximum total value is 2 + 5 + 4 + 3 = 14.

	Example 2:
	Input: inventory = [3,5], orders = 6
	Output: 19
	Explanation: Sell the 1st color 2 times (3 + 2) and the 2nd color 4 times 
	             (5 + 4 + 3 + 2). The maximum total value is 3 + 2 + 5 + 4 + 3 + 2 = 19.
	
	Example 3:
	Input: inventory = [2,8,4,10,6], orders = 20
	Output: 110
	
	Example 4:
	Input: inventory = [1000000000], orders = 1000000000
	Output: 21
	Explanation: Sell the 1st color 1000000000 times for a total value of 
	             500000000500000000. 500000000500000000 modulo 109 + 7 = 21.
	 
	Constraints:
	* 1 <= inventory.length <= 105
	* 1 <= inventory[i] <= 109
	* 1 <= orders <= min(sum(inventory[i]), 109)"""

    def maxProfit(self, inventory: List[int], orders: int) -> int:
        inventory.sort(reverse=True) # inventory high to low 
        inventory.append(0)
        ans = i = 0
        while orders: 
            sell = min(orders, (i+1)*(inventory[i] - inventory[i+1]))
            q, r = divmod(sell, i+1)
            ans += (i+1)*(2*inventory[i] - q + 1)*q//2 + r*(inventory[i] - q)
            orders -= sell 
            i += 1
        return ans % 1_000_000_007


    """1649. Create Sorted Array through Instructions (Hard)
	Given an integer array instructions, you are asked to create a sorted array 
	from the elements in instructions. You start with an empty container nums. 
	For each element from left to right in instructions, insert it into nums. 
	The cost of each insertion is the minimum of the following:
	* The number of elements currently in nums that are strictly less than 
	  instructions[i].
	* The number of elements currently in nums that are strictly greater than 
	  instructions[i].
	For example, if inserting element 3 into nums = [1,2,3,5], the cost of 
	insertion is min(2, 1) (elements 1 and 2 are less than 3, element 5 is 
	greater than 3) and nums will become [1,2,3,3,5]. Return the total cost to 
	insert all elements from instructions into nums. Since the answer may be 
	large, return it modulo 109 + 7

	Example 1:
	Input: instructions = [1,5,6,2]
	Output: 1
	Explanation: Begin with nums = [].
	Insert 1 with cost min(0, 0) = 0, now nums = [1].
	Insert 5 with cost min(1, 0) = 0, now nums = [1,5].
	Insert 6 with cost min(2, 0) = 0, now nums = [1,5,6].
	Insert 2 with cost min(1, 2) = 1, now nums = [1,2,5,6].
	The total cost is 0 + 0 + 0 + 1 = 1.

	Example 2:
	Input: instructions = [1,2,3,6,5,4]
	Output: 3
	Explanation: Begin with nums = [].
	Insert 1 with cost min(0, 0) = 0, now nums = [1].
	Insert 2 with cost min(1, 0) = 0, now nums = [1,2].
	Insert 3 with cost min(2, 0) = 0, now nums = [1,2,3].
	Insert 6 with cost min(3, 0) = 0, now nums = [1,2,3,6].
	Insert 5 with cost min(3, 1) = 1, now nums = [1,2,3,5,6].
	Insert 4 with cost min(3, 2) = 2, now nums = [1,2,3,4,5,6].
	The total cost is 0 + 0 + 0 + 0 + 1 + 2 = 3.

	Example 3:
	Input: instructions = [1,3,3,3,2,4,2,1,2]
	Output: 4
	Explanation: Begin with nums = [].
	Insert 1 with cost min(0, 0) = 0, now nums = [1].
	Insert 3 with cost min(1, 0) = 0, now nums = [1,3].
	Insert 3 with cost min(1, 0) = 0, now nums = [1,3,3].
	Insert 3 with cost min(1, 0) = 0, now nums = [1,3,3,3].
	Insert 2 with cost min(1, 3) = 1, now nums = [1,2,3,3,3].
	Insert 4 with cost min(5, 0) = 0, now nums = [1,2,3,3,3,4].
	​​​​​​​Insert 2 with cost min(1, 4) = 1, now nums = [1,2,2,3,3,3,4].
	​​​​​​​Insert 1 with cost min(0, 6) = 0, now nums = [1,1,2,2,3,3,3,4].
	​​​​​​​Insert 2 with cost min(2, 4) = 2, now nums = [1,1,2,2,2,3,3,3,4].
	The total cost is 0 + 0 + 0 + 0 + 1 + 0 + 1 + 0 + 2 = 4.
	 
	Constraints:
	* 1 <= instructions.length <= 10^5
	* 1 <= instructions[i] <= 10^5

class Fenwick:
    def __init__(self, n):
        self.nums = [0]*(n+1)
        
    def sum(self, k): 
        ans = 0
        while k: 
            ans += self.nums[k]
            k &= k-1
        return ans 
    
    def add(self, i, x): 
        i += 1
        while i < len(self.nums): 
            self.nums[i] += x
            i += i & -i
	"""

    def createSortedArray(self, instructions: List[int]) -> int:
        ans = 0
        fen = Fenwick(10**5)
        freq = {} # frequency of each instructions
        for i, x in enumerate(instructions): 
            less = fen.sum(x)
            more = i - freq.get(x, 0) - less
            ans += min(less, more)
            fen.add(x, 1)
            freq[x] = 1 + freq.get(x, 0)
        return ans % 1_000_000_007


    """1650. Lowest Common Ancestor of a Binary Tree III (Medium)
	Given two nodes of a binary tree p and q, return their lowest common 
	ancestor (LCA). Each node will have a reference to its parent node. The 
	definition for Node is below:
	class Node {
	    public int val;
	    public Node left;
	    public Node right;
	    public Node parent;
	}
	According to the definition of LCA on Wikipedia: "The lowest common 
	ancestor of two nodes p and q in a tree T is the lowest node that has both 
	p and q as descendants (where we allow a node to be a descendant of itself)."

	Example 1:
	Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
	Output: 3
	Explanation: The LCA of nodes 5 and 1 is 3.

	Example 2:
	Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
	Output: 5
	Explanation: The LCA of nodes 5 and 4 is 5 since a node can be a descendant 
	             of itself according to the LCA definition.

	Example 3:
	Input: root = [1,2], p = 1, q = 2
	Output: 1

	Constraints:
	* The number of nodes in the tree is in the range [2, 10^5].
	* -10^9 <= Node.val <= 10^9
	* All Node.val are unique.
	* p != q
	* p and q exist in the tree."""

    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        n0, n1 = p, q
        while n0 != n1: 
            n0 = n0.parent if n0 else q
            n1 = n1.parent if n1 else p
        return n0 


    """1652. Defuse the Bomb (Easy)
	You have a bomb to defuse, and your time is running out! Your informer will 
	provide you with a circular array code of length of n and a key k. To 
	decrypt the code, you must replace every number. All the numbers are 
	replaced simultaneously.
	* If k > 0, replace the ith number with the sum of the next k numbers.
	* If k < 0, replace the ith number with the sum of the previous k numbers.
	* If k == 0, replace the ith number with 0.
	As code is circular, the next element of code[n-1] is code[0], and the 
	previous element of code[0] is code[n-1]. Given the circular array code and 
	an integer key k, return the decrypted code to defuse the bomb!

	Example 1:
	Input: code = [5,7,1,4], k = 3
	Output: [12,10,16,13]
	Explanation: Each number is replaced by the sum of the next 3 numbers. The 
	             decrypted code is [7+1+4, 1+4+5, 4+5+7, 5+7+1]. Notice that 
	             the numbers wrap around.

	Example 2:
	Input: code = [1,2,3,4], k = 0
	Output: [0,0,0,0]
	Explanation: When k is zero, the numbers are replaced by 0. 

	Example 3:
	Input: code = [2,4,9,3], k = -2
	Output: [12,5,6,13]
	Explanation: The decrypted code is [3+9, 2+3, 4+2, 9+4]. Notice that the 
	             numbers wrap around again. If k is negative, the sum is of the 
	             previous numbers.

	Constraints:
	* n == code.length
	* 1 <= n <= 100
	* 1 <= code[i] <= 100
	* -(n - 1) <= k <= n - 1"""

    def decrypt(self, code: List[int], k: int) -> List[int]:
        if k < 0: return self.decrypt(code[::-1], -k)[::-1] 
        
        prefix = [0] # prefix sum (w/ leading 0)
        for x in code*2: prefix.append(prefix[-1] + x)
        
        ans = []
        for i in range(len(code)): 
            ans.append(prefix[i+k+1] - prefix[i+1])
        return ans 


    """1653. Minimum Deletions to Make String Balanced (Medium)
	You are given a string s consisting only of characters 'a' and 'b'​​​​. You 
	can delete any number of characters in s to make s balanced. s is balanced 
	if there is no pair of indices (i,j) such that i < j and s[i] = 'b' and 
	s[j]= 'a'. Return the minimum number of deletions needed to make s balanced.
	 
	Example 1:
	Input: s = "aababbab"
	Output: 2
	Explanation: You can either delete the characters at 0-indexed positions 2 
	             and 6 ("aababbab" -> "aaabbb"), or delete the characters at 
	             0-indexed positions 3 and 6 ("aababbab" -> "aabbbb").

	Example 2:
	Input: s = "bbaaaaabb"
	Output: 2
	Explanation: The only solution is to delete the first two characters.

	Constraints:
	* 1 <= s.length <= 10^5
	* s[i] is 'a' or 'b'​​."""

    def minimumDeletions(self, s: str) -> int:
        ans = suffix = 0
        for c in reversed(s):
            if c == "a": suffix += 1
            else: ans = min(1 + ans, suffix)
        return ans


    """1654. Minimum Jumps to Reach Home (Medium)
	A certain bug's home is on the x-axis at position x. Help them get there 
	from position 0. The bug jumps according to the following rules:
	* It can jump exactly a positions forward (to the right).
	* It can jump exactly b positions backward (to the left).
	* It cannot jump backward twice in a row.
	* It cannot jump to any forbidden positions.
	The bug may jump forward beyond its home, but it cannot jump to positions 
	numbered with negative integers. Given an array of integers forbidden, 
	where forbidden[i] means that the bug cannot jump to the position 
	forbidden[i], and integers a, b, and x, return the minimum number of jumps 
	needed for the bug to reach its home. If there is no possible sequence of 
	jumps that lands the bug on position x, return -1.

	Example 1:
	Input: forbidden = [14,4,18,1,15], a = 3, b = 15, x = 9
	Output: 3
	Explanation: 3 jumps forward (0 -> 3 -> 6 -> 9) will get the bug home.

	Example 2:
	Input: forbidden = [8,3,16,6,12,20], a = 15, b = 13, x = 11
	Output: -1

	Example 3:
	Input: forbidden = [1,6,2,14,5,17,4], a = 16, b = 9, x = 7
	Output: 2
	Explanation: One jump forward (0 -> 16) then one jump backward (16 -> 7) 
	             will get the bug home.

	Constraints:
	* 1 <= forbidden.length <= 1000
	* 1 <= a, b, forbidden[i] <= 2000
	* 0 <= x <= 2000
	* All the elements in forbidden are distinct.
	* Position x is not forbidden."""

    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        forbidden = set(forbidden)
        upper = max(forbidden | {x}) + a + b
        
        ans = 0
        queue = [(0, 0)]
        forbidden.add(0)
        while queue: 
            newq = []
            for n, k in queue: 
                if n == x: return ans
                if n+a <= upper and n+a not in forbidden: 
                    newq.append((n+a, 0))
                    forbidden.add(n+a)
                if k == 0 and 0 <= n-b and n-b not in forbidden: 
                    newq.append((n-b, 1))
            ans += 1
            queue = newq
        return -1 


    """1655. Distribute Repeating Integers (Hard)
	You are given an array of n integers, nums, where there are at most 50 
	unique values in the array. You are also given an array of m customer order 
	quantities, quantity, where quantity[i] is the amount of integers the ith 
	customer ordered. Determine if it is possible to distribute nums such that:
	* The ith customer gets exactly quantity[i] integers,
	* The integers the ith customer gets are all equal, and
	* Every customer is satisfied.
	Return true if it is possible to distribute nums according to the above 
	conditions.

	Example 1:
	Input: nums = [1,2,3,4], quantity = [2]
	Output: false
	Explanation: The 0th customer cannot be given two different integers.

	Example 2:
	Input: nums = [1,2,3,3], quantity = [2]
	Output: true
	Explanation: The 0th customer is given [3,3]. The integers [1,2] are not 
	             used.

	Example 3:
	Input: nums = [1,1,2,2], quantity = [2,2]
	Output: true
	Explanation: The 0th customer is given [1,1], and the 1st customer is given 
	             [2,2].

	Example 4:
	Input: nums = [1,1,2,3], quantity = [2,2]
	Output: false
	Explanation: Although the 0th customer could be given [1,1], the 1st 
	             customer cannot be satisfied.

	Example 5:
	Input: nums = [1,1,1,1,1], quantity = [2,3]
	Output: true
	Explanation: The 0th customer is given [1,1], and the 1st customer is given 
	             [1,1,1].

	Constraints:
	* n == nums.length
	* 1 <= n <= 10^5
	* 1 <= nums[i] <= 1000
	* m == quantity.length
	* 1 <= m <= 10
	* 1 <= quantity[i] <= 10^5
	* There are at most 50 unique values in nums."""

    def canDistribute(self, nums: List[int], quantity: List[int]) -> bool:
        freq = {}
        for x in nums: freq[x] = 1 + freq.get(x, 0)
        
        vals = sorted(freq.values(), reverse=True)
        quantity.sort(reverse=True) # handling large values first 
        
        def fn(i): 
            """Return True if possible to distribute quantity[i:] to remaining."""
            if i == len(quantity): return True 
            seen = set()
            for k in range(len(vals)): 
                if vals[k] >= quantity[i] and vals[k] not in seen: 
                    seen.add(vals[k])
                    vals[k] -= quantity[i]
                    if fn(i+1): return True 
                    vals[k] += quantity[i] # backtracking
                    
        return fn(0)


    """1657. Determine if Two Strings Are Close (Medium)
	Two strings are considered close if you can attain one from the other using 
	the following operations:
	* Operation 1: Swap any two existing characters.
	  + For example, abcde -> aecdb
	* Operation 2: Transform every occurrence of one existing character into 
	  another existing character, and do the same with the other character.
	  + For example, aacabb -> bbcbaa (all a's turn into b's, and all b's turn 
	    into a's)
	You can use the operations on either string as many times as necessary. 
	Given two strings, word1 and word2, return true if word1 and word2 are 
	close, and false otherwise.

	Example 1:
	Input: word1 = "abc", word2 = "bca"
	Output: true
	Explanation: You can attain word2 from word1 in 2 operations.
            	 Apply Operation 1: "abc" -> "acb"
            	 Apply Operation 1: "acb" -> "bca"

	Example 2:
	Input: word1 = "a", word2 = "aa"
	Output: false
	Explanation: It is impossible to attain word2 from word1, or vice versa, in 
	             any number of operations.
	
	Example 3:
	Input: word1 = "cabbba", word2 = "abbccc"
	Output: true
	Explanation: You can attain word2 from word1 in 3 operations.
	             Apply Operation 1: "cabbba" -> "caabbb"
	             Apply Operation 2: "caabbb" -> "baaccc"
	             Apply Operation 2: "baaccc" -> "abbccc"

	Example 4:
	Input: word1 = "cabbba", word2 = "aabbss"
	Output: false
	Explanation: It is impossible to attain word2 from word1, or vice versa, in 
	             any amount of operations.

	Constraints:
	* 1 <= word1.length, word2.length <= 105
	* word1 and word2 contain only lowercase English letters."""

    def closeStrings(self, word1: str, word2: str) -> bool:
        cnt1, cnt2 = Counter(word1), Counter(word2)
        return cnt1.keys() == cnt2.keys() and sorted(cnt1.values()) == sorted(cnt2.values())


    """1660. Correct a Binary Tree (Medium)
	You have a binary tree with a small defect. There is exactly one invalid 
	node where its right child incorrectly points to another node at the same 
	depth but to the invalid node's right. Given the root of the binary tree 
	with this defect, root, return the root of the binary tree after removing 
	this invalid node and every node underneath it (minus the node it 
	incorrectly points to).

	Custom testing:
	The test input is read as 3 lines:
	* TreeNode root
	* int fromNode (not available to correctBinaryTree)
	* int toNode (not available to correctBinaryTree)
	After the binary tree rooted at root is parsed, the TreeNode with value of 
	fromNode will have its right child pointer pointing to the TreeNode with a 
	value of toNode. Then, root is passed to correctBinaryTree.

	Example 1:
	Input: root = [1,2,3], fromNode = 2, toNode = 3
	Output: [1,null,3]
	Explanation: The node with value 2 is invalid, so remove it.

	Example 2:
	Input: root = [8,3,1,7,null,9,4,2,null,null,null,5,6], fromNode = 7, toNode = 4
	Output: [8,3,1,null,null,9,4,null,null,5,6]
	Explanation: The node with value 7 is invalid, so remove it and the node underneath it, node 2.

	Constraints:
	* The number of nodes in the tree is in the range [3, 10^4].
	* -10^9 <= Node.val <= 10^9
	* All Node.val are unique.
	* fromNode != toNode
	* fromNode and toNode will exist in the tree and will be on the same depth.
	* toNode is to the right of fromNode.
	* fromNode.right is null in the initial tree from the test data."""

    def correctBinaryTree(self, root: TreeNode) -> TreeNode:
        queue = [(root, None)]
        seen = set()
        for node, prev in queue: 
            if node.right and node.right.val in seen: 
                if node == prev.left: prev.left = None
                if node == prev.right: prev.right = None
                return root 
            seen.add(node.val)
            if node.right: queue.append((node.right, node))
            if node.left: queue.append((node.left, node))


    """1662. Check If Two String Arrays are Equivalent (Easy)
	Given two string arrays word1 and word2, return true if the two arrays 
	represent the same string, and false otherwise. A string is represented by 
	an array if the array elements concatenated in order forms the string.

	Example 1:
	Input: word1 = ["ab", "c"], word2 = ["a", "bc"]
	Output: true
	Explanation: word1 represents string "ab" + "c" -> "abc"
	             word2 represents string "a" + "bc" -> "abc"
	             The strings are the same, so return true.

	Example 2:
	Input: word1 = ["a", "cb"], word2 = ["ab", "c"]
	Output: false

	Example 3:
	Input: word1  = ["abc", "d", "defg"], word2 = ["abcddefg"]
	Output: true

	Constraints:
	* 1 <= word1.length, word2.length <= 103
	* 1 <= word1[i].length, word2[i].length <= 103
	* 1 <= sum(word1[i].length), sum(word2[i].length) <= 103
	* word1[i] and word2[i] consist of lowercase letters."""

    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        return "".join(word1) == "".join(word2)


    """1663. Smallest String With A Given Numeric Value (Medium)
	The numeric value of a lowercase character is defined as its position 
	(1-indexed) in the alphabet, so the numeric value of a is 1, the numeric 
	value of b is 2, the numeric value of c is 3, and so on. The numeric value 
	of a string consisting of lowercase characters is defined as the sum of its 
	characters' numeric values. For example, the numeric value of the string 
	"abe" is equal to 1 + 2 + 5 = 8. You are given two integers n and k. Return 
	the lexicographically smallest string with length equal to n and numeric 
	value equal to k. Note that a string x is lexicographically smaller than 
	string y if x comes before y in dictionary order, that is, either x is a 
	prefix of y, or if i is the first position such that x[i] != y[i], then 
	x[i] comes before y[i] in alphabetic order.

	Example 1:
	Input: n = 3, k = 27
	Output: "aay"
	Explanation: The numeric value of the string is 1 + 1 + 25 = 27, and it is 
	             the smallest string with such a value and length equal to 3.

	Example 2:
	Input: n = 5, k = 73
	Output: "aaszz"

	Constraints:
	* 1 <= n <= 105
	* n <= k <= 26 * n"""

    def getSmallestString(self, n: int, k: int) -> str:
        ans = []
        for i in range(n): 
            val = max(1, k - (n-i-1)*26)
            ans.append(chr(val + 96))
            k -= val
        return "".join(ans)


    """1664. Ways to Make a Fair Array (Medium)
	You are given an integer array nums. You can choose exactly one index 
	(0-indexed) and remove the element. Notice that the index of the elements 
	may change after the removal. For example, if nums = [6,1,7,4,1]:
	* Choosing to remove index 1 results in nums = [6,7,4,1].
	* Choosing to remove index 2 results in nums = [6,1,4,1].
	* Choosing to remove index 4 results in nums = [6,1,7,4].
	An array is fair if the sum of the odd-indexed values equals the sum of the 
	even-indexed values. Return the number of indices that you could choose 
	such that after the removal, nums is fair.

	Example 1:
	Input: nums = [2,1,6,4]
	Output: 1
	Explanation:
	Remove index 0: [1,6,4] -> Even sum: 1 + 4 = 5. Odd sum: 6. Not fair.
	Remove index 1: [2,6,4] -> Even sum: 2 + 4 = 6. Odd sum: 6. Fair.
	Remove index 2: [2,1,4] -> Even sum: 2 + 4 = 6. Odd sum: 1. Not fair.
	Remove index 3: [2,1,6] -> Even sum: 2 + 6 = 8. Odd sum: 1. Not fair.
	There is 1 index that you can remove to make nums fair.

	Example 2:
	Input: nums = [1,1,1]
	Output: 3
	Explanation: You can remove any index and the remaining array is fair.

	Example 3:
	Input: nums = [1,2,3]
	Output: 0
	Explanation: You cannot make a fair array after removing any index.

	Constraints:
	* 1 <= nums.length <= 10^5
	* 1 <= nums[i] <= 10^4"""

    def waysToMakeFair(self, nums: List[int]) -> int:
        prefix = [0]*2
        suffix = [sum(nums[::2]), sum(nums[1::2])]
        
        ans = 0
        for i, x in enumerate(nums): 
            suffix[i%2] -= x
            if prefix[0] + suffix[1] == prefix[1] + suffix[0]: ans += 1
            prefix[i%2] += x
        return ans 


    """1665. Minimum Initial Energy to Finish Tasks (Hard)
	You are given an array tasks where tasks[i] = [actuali, minimumi]:
	* actuali is the actual amount of energy you spend to finish the ith task.
	* minimumi is the minimum amount of energy you require to begin the ith 
	  task.
	For example, if the task is [10, 12] and your current energy is 11, you 
	cannot start this task. However, if your current energy is 13, you can 
	complete this task, and your energy will be 3 after finishing it. You can 
	finish the tasks in any order you like. Return the minimum initial amount 
	of energy you will need to finish all the tasks.

	Example 1:
	Input: tasks = [[1,2],[2,4],[4,8]]
	Output: 8
	Explanation:
	Starting with 8 energy, we finish the tasks in the following order:
	    - 3rd task. Now energy = 8 - 4 = 4.
	    - 2nd task. Now energy = 4 - 2 = 2.
	    - 1st task. Now energy = 2 - 1 = 1.
	Notice that even though we have leftover energy, starting with 7 energy 
	does not work because we cannot do the 3rd task.

	Example 2:
	Input: tasks = [[1,3],[2,4],[10,11],[10,12],[8,9]]
	Output: 32
	Explanation:
	Starting with 32 energy, we finish the tasks in the following order:
	    - 1st task. Now energy = 32 - 1 = 31.
	    - 2nd task. Now energy = 31 - 2 = 29.
	    - 3rd task. Now energy = 29 - 10 = 19.
	    - 4th task. Now energy = 19 - 10 = 9.
	    - 5th task. Now energy = 9 - 8 = 1.
	
	Example 3:
	Input: tasks = [[1,7],[2,8],[3,9],[4,10],[5,11],[6,12]]
	Output: 27
	Explanation:
	Starting with 27 energy, we finish the tasks in the following order:
	    - 5th task. Now energy = 27 - 5 = 22.
	    - 2nd task. Now energy = 22 - 2 = 20.
	    - 3rd task. Now energy = 20 - 3 = 17.
	    - 1st task. Now energy = 17 - 1 = 16.
	    - 4th task. Now energy = 16 - 4 = 12.
	    - 6th task. Now energy = 12 - 6 = 6.
	 
	Constraints:
	* 1 <= tasks.length <= 10^5
	* 1 <= actual​i <= minimumi <= 10^4"""

    def minimumEffort(self, tasks: List[List[int]]) -> int:
        ans = val = 0
        for x, y in sorted(tasks, key=lambda x: x[0]-x[1]): 
            if val < y: 
                ans += y - val 
                val = y
            val -= x
        return ans 


    """1666. Change the Root of a Binary Tree (Medium)
	Given the root of a binary tree and a leaf node, reroot the tree so that 
	the leaf is the new root. You can reroot the tree with the following steps 
	for each node cur on the path starting from the leaf up to the root​​​ 
	excluding the root:
	* If cur has a left child, then that child becomes cur's right child.
	* cur's original parent becomes cur's left child. Note that in this process 
	  the original parent's pointer to cur becomes null, making it have at most 
	  one child.
	Return the new root of the rerooted tree.

	Note: Ensure that your solution sets the Node.parent pointers correctly 
	      after rerooting or you will receive "Wrong Answer".

	Example 1:
	Input: root = [3,5,1,6,2,0,8,null,null,7,4], leaf = 7
	Output: [7,2,null,5,4,3,6,null,null,null,1,null,null,0,8]

	Example 2:
	Input: root = [3,5,1,6,2,0,8,null,null,7,4], leaf = 0
	Output: [0,1,null,3,8,5,null,null,null,6,2,null,null,7,4]

	Constraints:
	* The number of nodes in the tree is in the range [2, 100].
	* -109 <= Node.val <= 109
	* All Node.val are unique.
	* leaf exist in the tree."""

    def flipBinaryTree(self, root: 'Node', leaf: 'Node') -> 'Node':        
        prev, node = None, leaf
        while node: 
            if node == root:
                if prev == node.right: node.right = None
                else: node.left = None
            else: 
                if prev == node.right: node.right = node.left 
                node.left = node.parent
            node.parent, node, prev = prev, node.parent, node 
        return leaf


    """1668. Maximum Repeating Substring (Easy)
	For a string sequence, a string word is k-repeating if word concatenated k 
	times is a substring of sequence. The word's maximum k-repeating value is 
	the highest value k where word is k-repeating in sequence. If word is not a 
	substring of sequence, word's maximum k-repeating value is 0. Given strings 
	sequence and word, return the maximum k-repeating value of word in sequence.

	Example 1:
	Input: sequence = "ababc", word = "ab"
	Output: 2
	Explanation: "abab" is a substring in "ababc".

	Example 2:
	Input: sequence = "ababc", word = "ba"
	Output: 1
	Explanation: "ba" is a substring in "ababc". "baba" is not a substring in 
	             "ababc".

	Example 3:
	Input: sequence = "ababc", word = "ac"
	Output: 0
	Explanation: "ac" is not a substring in "ababc". 

	Constraints:
	* 1 <= sequence.length <= 100
	* 1 <= word.length <= 100
	* sequence and word contains only lowercase English letters."""

    def maxRepeating(self, sequence: str, word: str) -> int:
        if len(sequence) < len(word): return 0 # edge case 
        
        pattern = word * (len(sequence)//len(word))
        lps = [0] # longest proper prefix also suffix (KMP)
        k = 0
        for i in range(1, len(pattern)):
            while k and pattern[k] != pattern[i]: k = lps[k-1]
            if pattern[i] == pattern[k]: k += 1
            lps.append(k)
        
        ans = k = 0
        for i in range(len(sequence)):
            while k and pattern[k] != sequence[i]: k = lps[k-1]
            if pattern[k] == sequence[i]: k += 1
            ans = max(ans, k//len(word))
            if k == len(pattern): return ans
        return ans 


    """1669. Merge In Between Linked Lists (Medium)
	You are given two linked lists: list1 and list2 of sizes n and m 
	respectively. Remove list1's nodes from the ath node to the bth node, and 
	put list2 in their place. Build the result list and return its head.

	Example 1:
	Input: list1 = [0,1,2,3,4,5], a = 3, b = 4, list2 = [1000000,1000001,1000002]
	Output: [0,1,2,1000000,1000001,1000002,5]
	Explanation: We remove the nodes 3 and 4 and put the entire list2 in their 
	             place. The blue edges and nodes in the above figure indicate 
	             the result.

	Example 2:
	Input: list1 = [0,1,2,3,4,5,6], a = 2, b = 5, 
	       list2 = [1000000,1000001,1000002,1000003,1000004]
	Output: [0,1,1000000,1000001,1000002,1000003,1000004,6]
	Explanation: The blue edges and nodes in the above figure indicate the result.

	Constraints:
	* 3 <= list1.length <= 10^4
	* 1 <= a <= b < list1.length - 1
	* 1 <= list2.length <= 10^4"""

    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        node = list1
        for k in range(b+1): 
            if k == a-1: start = node 
            node = node.next 
        end = node 
        
        start.next = node = list2
        while node.next: node = node.next 
        node.next = end
        return list1 


    """1671. Minimum Number of Removals to Make Mountain Array (Hard)
	You may recall that an array arr is a mountain array if and only if:
	* arr.length >= 3
	* There exists some index i (0-indexed) with 0 < i < arr.length - 1 such 
	  that:
	  + arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
	  + arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
	Given an integer array nums​​​, return the minimum number of elements to 
	remove to make nums​​​ a mountain array.

	Example 1:
	Input: nums = [1,3,1]
	Output: 0
	Explanation: The array itself is a mountain array so we do not need to 
	             remove any elements.

	Example 2:
	Input: nums = [2,1,1,5,6,2,3,1]
	Output: 3
	Explanation: One solution is to remove the elements at indices 0, 1, and 5, 
	             making the array nums = [1,5,6,3,1].
	
	Example 3:
	Input: nums = [4,3,2,1,1,2,3,1]
	Output: 4

	Example 4:
	Input: nums = [1,2,3,4,4,3,2,1]
	Output: 1

	Constraints:
	* 3 <= nums.length <= 1000
	* 1 <= nums[i] <= 10^9
	* It is guaranteed that you can make a mountain array out of nums."""

    def minimumMountainRemovals(self, nums: List[int]) -> int:
        
        def fn(nums): 
            """Return length of LIS (excluding x) ending at x."""
            ans, vals = [], []
            for i, x in enumerate(nums): 
                k = bisect_left(vals, x)
                if k == len(vals): vals.append(x)
                else: vals[k] = x
                ans.append(k)
            return ans 
        
        left, right = fn(nums), fn(nums[::-1])[::-1]
        
        ans = inf
        for i in range(1, len(nums)-1): 
            if left[i] and right[i]:
                ans = min(ans, len(nums) - left[i] - right[i] - 1)
        return ans 


    """1672. Richest Customer Wealth (Easy)
	You are given an m x n integer grid accounts where accounts[i][j] is the 
	amount of money the i​​​​​​​​​​​th​​​​ customer has in the j​​​​​​​​​​​th​​​​ bank. Return the wealth 
	that the richest customer has. A customer's wealth is the amount of money 
	they have in all their bank accounts. The richest customer is the customer 
	that has the maximum wealth.

	Example 1:
	Input: accounts = [[1,2,3],[3,2,1]]
	Output: 6
	Explanation:
	1st customer has wealth = 1 + 2 + 3 = 6
	2nd customer has wealth = 3 + 2 + 1 = 6
	Both customers are considered the richest with a wealth of 6 each, so return 6.

	Example 2:
	Input: accounts = [[1,5],[7,3],[3,5]]
	Output: 10
	Explanation: 
	1st customer has wealth = 6
	2nd customer has wealth = 10 
	3rd customer has wealth = 8
	The 2nd customer is the richest with a wealth of 10.

	Example 3:
	Input: accounts = [[2,8,7],[7,1,3],[1,9,5]]
	Output: 17

	Constraints:
	* m == accounts.length
	* n == accounts[i].length
	* 1 <= m, n <= 50
	* 1 <= accounts[i][j] <= 100"""

    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max(map(sum, accounts))


    """1673. Find the Most Competitive Subsequence (Medium)
	Given an integer array nums and a positive integer k, return the most 
	competitive subsequence of nums of size k. An array's subsequence is a 
	resulting sequence obtained by erasing some (possibly zero) elements from 
	the array. We define that a subsequence a is more competitive than a 
	subsequence b (of the same length) if in the first position where a and b 
	differ, subsequence a has a number less than the corresponding number in b. 
	For example, [1,3,4] is more competitive than [1,3,5] because the first 
	position they differ is at the final number, and 4 is less than 5.

	Example 1:
	Input: nums = [3,5,2,6], k = 2
	Output: [2,6]
	Explanation: Among the set of every possible subsequence: 
	             {[3,5], [3,2], [3,6], [5,2], [5,6], [2,6]}, [2,6] is the most 
	             competitive.

	Example 2:
	Input: nums = [2,4,3,3,5,4,9,6], k = 4
	Output: [2,3,3,4]
	 
	Constraints:
	* 1 <= nums.length <= 105
	* 0 <= nums[i] <= 109
	* 1 <= k <= nums.length"""

    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        stack = [] # (increasing) mono-stack 
        for i, x in enumerate(nums): 
            while stack and stack[-1] > x and len(stack) + len(nums) - i > k: stack.pop()
            if len(stack) < k: stack.append(x)
        return stack 


    """1674. Minimum Moves to Make Array Complementary (Medium)
	You are given an integer array nums of even length n and an integer limit. 
	In one move, you can replace any integer from nums with another integer 
	between 1 and limit, inclusive. The array nums is complementary if for all 
	indices i (0-indexed), nums[i] + nums[n - 1 - i] equals the same number. 
	For example, the array [1,2,3,4] is complementary because for all indices i, 
	nums[i] + nums[n - 1 - i] = 5. Return the minimum number of moves required 
	to make nums complementary.

	Example 1:
	Input: nums = [1,2,4,3], limit = 4
	Output: 1
	Explanation: In 1 move, you can change nums to [1,2,2,3] (underlined elements are changed).
	nums[0] + nums[3] = 1 + 3 = 4.
	nums[1] + nums[2] = 2 + 2 = 4.
	nums[2] + nums[1] = 2 + 2 = 4.
	nums[3] + nums[0] = 3 + 1 = 4.
	Therefore, nums[i] + nums[n-1-i] = 4 for every i, so nums is complementary.

	Example 2:
	Input: nums = [1,2,2,1], limit = 2
	Output: 2
	Explanation: In 2 moves, you can change nums to [2,2,2,2]. You cannot change any number to 3 since 3 > limit.

	Example 3:
	Input: nums = [1,2,1,2], limit = 2
	Output: 0
	Explanation: nums is already complementary.

	Constraints:
	* n == nums.length
	* 2 <= n <= 105
	* 1 <= nums[i] <= limit <= 105
	* n is even."""

    def minMoves(self, nums: List[int], limit: int) -> int:
        diff = [0]*(2*limit+2) # difference array 
        
        for i in range(len(nums)//2): 
            m = min(nums[i], nums[~i]) + 1 # lower bound 
            diff[m] += -1
            x = nums[i] + nums[~i]
            diff[x] += -1
            diff[x+1] += 1
            M = max(nums[i], nums[~i]) + 1 + limit # upper bound 
            diff[M] += 1
        
        for i in range(1, len(diff)): diff[i] += diff[i-1] # prefix sum 
        return len(nums) + min(diff)


    """1675. Minimize Deviation in Array (Hard)
	You are given an array nums of n positive integers. You can perform two 
	types of operations on any element of the array any number of times:

	* If the element is even, divide it by 2.
	  + For example, if the array is [1,2,3,4], then you can do this operation 
	    on the last element, and the array will be [1,2,3,2].
	* If the element is odd, multiply it by 2.
	  + For example, if the array is [1,2,3,4], then you can do this operation 
	    on the first element, and the array will be [2,2,3,4].
	The deviation of the array is the maximum difference between any two 
	elements in the array. Return the minimum deviation the array can have 
	after performing some number of operations.

	Example 1:
	Input: nums = [1,2,3,4]
	Output: 1
	Explanation: You can transform the array to [1,2,3,2], then to [2,2,3,2], 
	             then the deviation will be 3 - 2 = 1.

	Example 2:
	Input: nums = [4,1,5,20,3]
	Output: 3
	Explanation: You can transform the array after two operations to [4,2,5,5,3], 
	             then the deviation will be 5 - 2 = 3.

	Example 3:
	Input: nums = [2,10,8]
	Output: 3

	Constraints:
	* n == nums.length
	* 2 <= n <= 105
	* 1 <= nums[i] <= 109"""

    def minimumDeviation(self, nums: List[int]) -> int:
        pq = [-2*x if x&1 else -x for x in nums] # max-heap 
        heapify(pq)
        
        mn = -max(pq)
        ans = -pq[0] - mn 
        while not pq[0] & 1: 
            x = heappop(pq)
            heappush(pq, x//2)
            mn = min(mn, -x//2)
            ans = min(ans, -pq[0] - mn)
        return ans 


    """1676. Lowest Common Ancestor of a Binary Tree IV (Medium)
	Given the root of a binary tree and an array of TreeNode objects nodes, 
	return the lowest common ancestor (LCA) of all the nodes in nodes. All the 
	nodes will exist in the tree, and all values of the tree's nodes are unique.
	Extending the definition of LCA on Wikipedia: "The lowest common ancestor 
	of n nodes p1, p2, ..., pn in a binary tree T is the lowest node that has 
	every pi as a descendant (where we allow a node to be a descendant of 
	itself) for every valid i". A descendant of a node x is a node y that is on 
	the path from node x to some leaf node.

	Example 1:
	Input: root = [3,5,1,6,2,0,8,null,null,7,4], nodes = [4,7]
	Output: 2
	Explanation: The lowest common ancestor of nodes 4 and 7 is node 2.

	Example 2:
	Input: root = [3,5,1,6,2,0,8,null,null,7,4], nodes = [1]
	Output: 1
	Explanation: The lowest common ancestor of a single node is the node itself.

	Example 3:
	Input: root = [3,5,1,6,2,0,8,null,null,7,4], nodes = [7,6,2,4]
	Output: 5
	Explanation: The lowest common ancestor of the nodes 7, 6, 2, and 4 is node 5.

	Example 4:
	Input: root = [3,5,1,6,2,0,8,null,null,7,4], nodes = [0,1,2,3,4,5,6,7,8]
	Output: 3
	Explanation: The lowest common ancestor of all the nodes is the root node.

	Constraints:
	* The number of nodes in the tree is in the range [1, 104].
	* -109 <= Node.val <= 109
	* All Node.val are unique.
	* All nodes[i] will exist in the tree.
	* All nodes[i] are distinct."""

    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        nodes = set(nodes)
        
        @cache
        def fn(node):
            if not node: return # edge case 
            if node in nodes or fn(node.left) and fn(node.right): return node
            return fn(node.left) or fn(node.right)
        
        return fn(root)


    """1678. Goal Parser Interpretation (Easy)
	You own a Goal Parser that can interpret a string command. The command 
	consists of an alphabet of "G", "()" and/or "(al)" in some order. The Goal 
	Parser will interpret "G" as the string "G", "()" as the string "o", and 
	"(al)" as the string "al". The interpreted strings are then concatenated in 
	the original order. Given the string command, return the Goal Parser's 
	interpretation of command.

	Example 1:
	Input: command = "G()(al)"
	Output: "Goal"
	Explanation: The Goal Parser interprets the command as follows:
	G -> G
	() -> o
	(al) -> al
	The final concatenated result is "Goal".

	Example 2:
	Input: command = "G()()()()(al)"
	Output: "Gooooal"

	Example 3:
	Input: command = "(al)G(al)()()G"
	Output: "alGalooG"

	Constraints:
	* 1 <= command.length <= 100
	* command consists of "G", "()", and/or "(al)" in some order."""

    def interpret(self, command: str) -> str:
        return command.replace("()", "o").replace("(al)", "al")


    """1679. Max Number of K-Sum Pairs (Medium)
	You are given an integer array nums and an integer k. In one operation, you 
	can pick two numbers from the array whose sum equals k and remove them from 
	the array. Return the maximum number of operations you can perform on the 
	array.

	Example 1:
	Input: nums = [1,2,3,4], k = 5
	Output: 2
	Explanation: Starting with nums = [1,2,3,4]:
	- Remove numbers 1 and 4, then nums = [2,3]
	- Remove numbers 2 and 3, then nums = []
	There are no more pairs that sum up to 5, hence a total of 2 operations.

	Example 2:
	Input: nums = [3,1,3,4,3], k = 6
	Output: 1
	Explanation: Starting with nums = [3,1,3,4,3]:
	- Remove the first two 3's, then nums = [1,4,3]
	There are no more pairs that sum up to 6, hence a total of 1 operation.

	Constraints:
	* 1 <= nums.length <= 105
	* 1 <= nums[i] <= 109
	* 1 <= k <= 109"""

    def maxOperations(self, nums: List[int], k: int) -> int:
        freq = {}
        for x in nums: freq[x] = 1 + freq.get(x, 0)
        
        ans = 0
        for x, v in freq.items(): 
            if k - x in freq: 
                if x == k - x: ans += freq[x]//2
                elif x < k - x: ans += min(freq[x], freq[k-x])
        return ans 


    """1680. Concatenation of Consecutive Binary Numbers (Medium)
	Given an integer n, return the decimal value of the binary string formed by 
	concatenating the binary representations of 1 to n in order, modulo 109 + 7.

	Example 1:
	Input: n = 1
	Output: 1
	Explanation: "1" in binary corresponds to the decimal value 1. 

	Example 2:
	Input: n = 3
	Output: 27
	Explanation: In binary, 1, 2, and 3 corresponds to "1", "10", and "11". 
	             After concatenating them, we have "11011", which corresponds 
	             to the decimal value 27.

	Example 3:
	Input: n = 12
	Output: 505379714
	Explanation: The concatenation results in "1101110010111011110001001101010111100".
	             The decimal value of that is 118505380540. After modulo 10^9 + 7, 
	             the result is 505379714.

	Constraints: 1 <= n <= 105"""

    def concatenatedBinary(self, n: int) -> int:
        ans = k = 0
        for x in range(1, n+1): 
            if not x & x-1: k += 1
            ans = ((ans << k) + x) % 1_000_000_007
        return ans 


    """1682. Longest Palindromic Subsequence II (Medium)
	A subsequence of a string s is considered a good palindromic subsequence if:
	* It is a subsequence of s.
	* It is a palindrome (has the same value if reversed).
	* It has an even length.
	* No two consecutive characters are equal, except the two middle ones.
	For example, if s = "abcabcabb", then "abba" is considered a good palindromic 
	subsequence, while "bcb" (not even length) and "bbbb" (has equal consecutive 
	characters) are not. Given a string s, return the length of the longest good 
	palindromic subsequence in s.

	Example 1:
	Input: s = "bbabab"
	Output: 4
	Explanation: The longest good palindromic subsequence of s is "baab".

	Example 2:
	Input: s = "dcbccacdb"
	Output: 4
	Explanation: The longest good palindromic subsequence of s is "dccd".

	Constraints:
	* 1 <= s.length <= 250
	* s consists of lowercase English letters."""

    def longestPalindromeSubseq(self, s: str) -> int:
        dp = [[[0]*27 for _ in s] for _ in s] # n x n x 27 
        
        for i in reversed(range(len(s))):
            for j in range(i+1, len(s)):
                for k in range(27): 
                    if s[i] == s[j] != chr(k+96): 
                        dp[i][j][k] = 2 + dp[i+1][j-1][ord(s[i])-96]
                    else: 
                        dp[i][j][k] = max(dp[i+1][j][k], dp[i][j-1][k])
        return dp[0][-1][0]


    """1684. Count the Number of Consistent Strings (Easy)
	You are given a string allowed consisting of distinct characters and an 
	array of strings words. A string is consistent if all characters in the 
	string appear in the string allowed. Return the number of consistent 
	strings in the array words.

	Example 1:
	Input: allowed = "ab", words = ["ad","bd","aaab","baa","badab"]
	Output: 2
	Explanation: Strings "aaab" and "baa" are consistent since they only 
	             contain characters 'a' and 'b'.

	Example 2:
	Input: allowed = "abc", words = ["a","b","c","ab","ac","bc","abc"]
	Output: 7
	Explanation: All strings are consistent.

	Example 3:
	Input: allowed = "cad", words = ["cc","acd","b","ba","bac","bad","ac","d"]
	Output: 4
	Explanation: Strings "cc", "acd", "ac", and "d" are consistent.

	Constraints:
	* 1 <= words.length <= 104
	* 1 <= allowed.length <= 26
	* 1 <= words[i].length <= 10
	* The characters in allowed are distinct.
	* words[i] and allowed contain only lowercase English letters."""

    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        return sum(all(c in allowed for c in word) for word in words)


    """1688. Count of Matches in Tournament (Easy)
	You are given an integer n, the number of teams in a tournament that has 
	strange rules: 
	* If the current number of teams is even, each team gets paired with another 
	  team. A total of n / 2 matches are played, and n / 2 teams advance to the 
	  next round.
	* If the current number of teams is odd, one team randomly advances in the 
	  tournament, and the rest gets paired. A total of (n - 1) / 2 matches are 
	  played, and (n - 1) / 2 + 1 teams advance to the next round.
	Return the number of matches played in the tournament until a winner is 
	decided.

	Example 1:
	Input: n = 7
	Output: 6
	Explanation: Details of the tournament: 
	- 1st Round: Teams = 7, Matches = 3, and 4 teams advance.
	- 2nd Round: Teams = 4, Matches = 2, and 2 teams advance.
	- 3rd Round: Teams = 2, Matches = 1, and 1 team is declared the winner.
	Total number of matches = 3 + 2 + 1 = 6.

	Example 2:
	Input: n = 14
	Output: 13
	Explanation: Details of the tournament:
	- 1st Round: Teams = 14, Matches = 7, and 7 teams advance.
	- 2nd Round: Teams = 7, Matches = 3, and 4 teams advance.
	- 3rd Round: Teams = 4, Matches = 2, and 2 teams advance.
	- 4th Round: Teams = 2, Matches = 1, and 1 team is declared the winner.
	Total number of matches = 7 + 3 + 2 + 1 = 13.

	Constraints: 1 <= n <= 200"""

    def numberOfMatches(self, n: int) -> int:
        return n-1


    """1689. Partitioning Into Minimum Number Of Deci-Binary Numbers (Medium)
	A decimal number is called deci-binary if each of its digits is either 0 or 
	1 without any leading zeros. For example, 101 and 1100 are deci-binary, 
	while 112 and 3001 are not. Given a string n that represents a positive 
	decimal integer, return the minimum number of positive deci-binary numbers 
	needed so that they sum up to n.

	Example 1:
	Input: n = "32"
	Output: 3
	Explanation: 10 + 11 + 11 = 32

	Example 2:
	Input: n = "82734"
	Output: 8

	Example 3:
	Input: n = "27346209830709182346"
	Output: 9

	Constraints:
	* 1 <= n.length <= 105
	* n consists of only digits.
	* n does not contain any leading zeros and represents a positive integer."""

    def minPartitions(self, n: str) -> int:
        return int(max(n))


    """1690. Stone Game VII (Medium)
	Alice and Bob take turns playing a game, with Alice starting first. There 
	are n stones arranged in a row. On each player's turn, they can remove 
	either the leftmost stone or the rightmost stone from the row and receive 
	points equal to the sum of the remaining stones' values in the row. The 
	winner is the one with the higher score when there are no stones left to 
	remove. Bob found that he will always lose this game (poor Bob, he always 
	loses), so he decided to minimize the score's difference. Alice's goal is 
	to maximize the difference in the score. Given an array of integers stones 
	where stones[i] represents the value of the ith stone from the left, return 
	the difference in Alice and Bob's score if they both play optimally.

	Example 1:
	Input: stones = [5,3,1,4,2]
	Output: 6
	Explanation: 
	- Alice removes 2 and gets 5 + 3 + 1 + 4 = 13 points. Alice = 13, Bob = 0, stones = [5,3,1,4].
	- Bob removes 5 and gets 3 + 1 + 4 = 8 points. Alice = 13, Bob = 8, stones = [3,1,4].
	- Alice removes 3 and gets 1 + 4 = 5 points. Alice = 18, Bob = 8, stones = [1,4].
	- Bob removes 1 and gets 4 points. Alice = 18, Bob = 12, stones = [4].
	- Alice removes 4 and gets 0 points. Alice = 18, Bob = 12, stones = [].
	The score difference is 18 - 12 = 6.

	Example 2:
	Input: stones = [7,90,5,1,100,10,10,2]
	Output: 122

	Constraints:
	* n == stones.length
	* 2 <= n <= 1000
	* 1 <= stones[i] <= 1000"""

    def stoneGameVII(self, stones: List[int]) -> int:
        prefix = [0]
        for x in stones: prefix.append(prefix[-1] + x)
            
        n = len(stones)
        dp = [[0]*(n+1) for _ in range(n+1)]
        
        for lo in reversed(range(n+1)):
            for hi in range(n+1): 
                if lo < hi: 
                    dp[lo][hi] = max(prefix[hi]-prefix[lo+1]-dp[lo+1][hi], prefix[hi-1]-prefix[lo]-dp[lo][hi-1])
        
        return dp[0][-1]


    """1691. Maximum Height by Stacking Cuboids (Hard)
	Given n cuboids where the dimensions of the ith cuboid is 
	cuboids[i] = [widthi, lengthi, heighti] (0-indexed). Choose a subset of 
	cuboids and place them on each other. You can place cuboid i on cuboid j if 
	widthi <= widthj and lengthi <= lengthj and heighti <= heightj. You can 
	rearrange any cuboid's dimensions by rotating it to put it on another 
	cuboid. Return the maximum height of the stacked cuboids.

	Example 1:
	Input: cuboids = [[50,45,20],[95,37,53],[45,23,12]]
	Output: 190
	Explanation:
	Cuboid 1 is placed on the bottom with the 53x37 side facing down with height 95.
	Cuboid 0 is placed next with the 45x20 side facing down with height 50.
	Cuboid 2 is placed next with the 23x12 side facing down with height 45.
	The total height is 95 + 50 + 45 = 190.

	Example 2:
	Input: cuboids = [[38,25,45],[76,35,3]]
	Output: 76
	Explanation:
	You can't place any of the cuboids on the other.
	We choose cuboid 1 and rotate it so that the 35x3 side is facing down and its height is 76.

	Example 3:
	Input: cuboids = [[7,11,17],[7,17,11],[11,7,17],[11,17,7],[17,7,11],[17,11,7]]
	Output: 102
	Explanation:
	After rearranging the cuboids, you can see that all cuboids have the same dimension.
	You can place the 11x7 side down on all cuboids so their heights are 17.
	The maximum height of stacked cuboids is 6 * 17 = 102.

	Constraints:
	* n == cuboids.length
	* 1 <= n <= 100
	* 1 <= widthi, lengthi, heighti <= 100"""

    def maxHeight(self, cuboids: List[List[int]]) -> int:
        cuboids = sorted((sorted(x, reverse=True) for x in cuboids), reverse=True)
        
        @lru_cache(None)
        def fn(i, h, l, w): 
            """Return max heights of stacking cuboids[i:]."""
            if i == len(cuboids): return 0 # no cuboids left 
            hi, li, wi = cuboids[i]
            if hi <= h and li <= l and wi <= w: 
                return max(hi + fn(i+1, hi, li, wi), fn(i+1, h, l, w))
            else:
                return fn(i+1, h, l, w)
            
        return fn(0, inf, inf, inf)


    """1694. Reformat Phone Number (Easy)
	You are given a phone number as a string number. number consists of digits, 
	spaces ' ', and/or dashes '-'. You would like to reformat the phone number 
	in a certain manner. Firstly, remove all spaces and dashes. Then, group the 
	digits from left to right into blocks of length 3 until there are 4 or fewer 
	digits. The final digits are then grouped as follows:
	* 2 digits: A single block of length 2.
	* 3 digits: A single block of length 3.
	* 4 digits: Two blocks of length 2 each.
	The blocks are then joined by dashes. Notice that the reformatting process 
	should never produce any blocks of length 1 and produce at most two blocks 
	of length 2. Return the phone number after formatting.

	Example 1:
	Input: number = "1-23-45 6"
	Output: "123-456"
	Explanation: The digits are "123456".
	Step 1: There are more than 4 digits, so group the next 3 digits. The 1st block is "123".
	Step 2: There are 3 digits remaining, so put them in a single block of length 3. The 2nd block is "456".
	Joining the blocks gives "123-456".

	Example 2:
	Input: number = "123 4-567"
	Output: "123-45-67"
	Explanation: The digits are "1234567".
	Step 1: There are more than 4 digits, so group the next 3 digits. The 1st block is "123".
	Step 2: There are 4 digits left, so split them into two blocks of length 2. The blocks are "45" and "67".
	Joining the blocks gives "123-45-67".

	Example 3:
	Input: number = "123 4-5678"
	Output: "123-456-78"
	Explanation: The digits are "12345678".
	Step 1: The 1st block is "123".
	Step 2: The 2nd block is "456".
	Step 3: There are 2 digits left, so put them in a single block of length 2. The 3rd block is "78".
	Joining the blocks gives "123-456-78".

	Example 4:
	Input: number = "12"
	Output: "12"

	Example 5:
	Input: number = "--17-5 229 35-39475 "
	Output: "175-229-353-94-75"

	Constraints:
	* 2 <= number.length <= 100
	* number consists of digits and the characters '-' and ' '.
	* There are at least two digits in number."""

    def reformatNumber(self, number: str) -> str:
        number = number.replace("-", "").replace(" ", "") # replacing - and space 
        ans = []
        for i in range(0, len(number), 3): 
            if len(number) - i != 4: ans.append(number[i:i+3])
            else: 
                ans.extend([number[i:i+2], number[i+2:]])
                break 
        return "-".join(ans)


    """1695. Maximum Erasure Value (Medium)
	You are given an array of positive integers nums and want to erase a 
	subarray containing unique elements. The score you get by erasing the 
	subarray is equal to the sum of its elements. Return the maximum score you 
	can get by erasing exactly one subarray. An array b is called to be a 
	subarray of a if it forms a contiguous subsequence of a, that is, if it is 
	equal to a[l],a[l+1],...,a[r] for some (l,r).

	Example 1:
	Input: nums = [4,2,4,5,6]
	Output: 17
	Explanation: The optimal subarray here is [2,4,5,6].

	Example 2:
	Input: nums = [5,2,1,2,5,2,1,2,5]
	Output: 8
	Explanation: The optimal subarray here is [5,2,1] or [1,2,5].

	Constraints:
	* 1 <= nums.length <= 105
	* 1 <= nums[i] <= 104"""

    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        prefix = [0]
        for x in nums: prefix.append(prefix[-1] + x)
        
        ans = ii = 0
        seen = {}
        for i, x in enumerate(nums): 
            ii = max(ii, seen.get(x, -1)+1)
            ans = max(ans, prefix[i+1] - prefix[ii])
            seen[x] = i
        return ans 


    """1696. Jump Game VI (Medium)
	You are given a 0-indexed integer array nums and an integer k. You are 
	initially standing at index 0. In one move, you can jump at most k steps 
	forward without going outside the boundaries of the array. That is, you can 
	jump from index i to any index in the range [i + 1, min(n - 1, i + k)] 
	inclusive. You want to reach the last index of the array (index n - 1). 
	Your score is the sum of all nums[j] for each index j you visited in the 
	array. Return the maximum score you can get.

	Example 1:
	Input: nums = [1,-1,-2,4,-7,3], k = 2
	Output: 7
	Explanation: You can choose your jumps forming the subsequence [1,-1,4,3] 
	             (underlined above). The sum is 7.

	Example 2:
	Input: nums = [10,-5,-2,4,0,3], k = 3
	Output: 17
	Explanation: You can choose your jumps forming the subsequence [10,4,3] 
	             (underlined above). The sum is 17.
	
	Example 3:
	Input: nums = [1,-5,-20,4,-1,3,-6,-3], k = 2
	Output: 0

	Constraints:
	* 1 <= nums.length, k <= 105
	* -104 <= nums[i] <= 104"""

    def maxResult(self, nums: List[int], k: int) -> int:
        queue = deque() # (decreasing) mono-queue 
        for i in reversed(range(len(nums))): 
            if queue and queue[0][1] - i > k: queue.popleft() # expired max 
            ans = nums[i] + queue[0][0] if queue else nums[i] # max as of i
            while queue and queue[-1][0] <= ans: queue.pop()
            queue.append((ans, i))
        return ans 


    """1697. Checking Existence of Edge Length Limited Paths (Hard)
	An undirected graph of n nodes is defined by edgeList, where 
	edgeList[i] = [ui, vi, disi] denotes an edge between nodes ui and vi with 
	distance disi. Note that there may be multiple edges between two nodes. 
	Given an array queries, where queries[j] = [pj, qj, limitj], your task is 
	to determine for each queries[j] whether there is a path between pj and qj 
	such that each edge on the path has a distance strictly less than limitj. 
	Return a boolean array answer, where answer.length == queries.length and 
	the jth value of answer is true if there is a path for queries[j] is true, 
	and false otherwise.

	Example 1:
	Input: n = 3, 
	       edgeList = [[0,1,2],[1,2,4],[2,0,8],[1,0,16]], 
	       queries = [[0,1,2],[0,2,5]]
	Output: [false,true]
	Explanation: The above figure shows the given graph. Note that there are 
	             two overlapping edges between 0 and 1 with distances 2 and 16. 
	             For the first query, between 0 and 1 there is no path where 
	             each distance is less than 2, thus we return false for this 
	             query. For the second query, there is a path (0 -> 1 -> 2) of 
	             two edges with distances less than 5, thus we return true for 
	             this query.

	Example 2:
	Input: n = 5, 
	       edgeList = [[0,1,10],[1,2,5],[2,3,9],[3,4,13]], 
	       queries = [[0,4,14],[1,4,13]]
	Output: [true,false]
	Exaplanation: The above figure shows the given graph.

	Constraints:
	* 2 <= n <= 105
	* 1 <= edgeList.length, queries.length <= 105
	* edgeList[i].length == 3
	* queries[j].length == 3
	* 0 <= ui, vi, pj, qj <= n - 1
	* ui != vi
	* pj != qj
	* 1 <= disi, limitj <= 109
	* There may be multiple edges between two nodes."""

    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        queries = sorted((w, p, q, i) for i, (p, q, w) in enumerate(queries))
        edgeList = sorted((w, u, v) for u, v, w in edgeList)
        
        uf = UnionFind(n)
        
        ans = [None] * len(queries)
        ii = 0
        for w, p, q, i in queries: 
            while ii < len(edgeList) and edgeList[ii][0] < w: 
                _, u, v = edgeList[ii]
                uf.union(u, v)
                ii += 1
            ans[i] = uf.find(p) == uf.find(q)
        return ans 


    """1700. Number of Students Unable to Eat Lunch (Easy)
	The school cafeteria offers circular and square sandwiches at lunch break, 
	referred to by numbers 0 and 1 respectively. All students stand in a queue. 
	Each student either prefers square or circular sandwiches. The number of 
	sandwiches in the cafeteria is equal to the number of students. The 
	sandwiches are placed in a stack. At each step:
	* If the student at the front of the queue prefers the sandwich on the top 
	  of the stack, they will take it and leave the queue.
	* Otherwise, they will leave it and go to the queue's end.
	This continues until none of the queue students want to take the top 
	sandwich and are thus unable to eat. You are given two integer arrays 
	students and sandwiches where sandwiches[i] is the type of the i​​​​​​th 
	sandwich in the stack (i = 0 is the top of the stack) and students[j] is 
	the preference of the j​​​​​​th student in the initial queue (j = 0 is the front 
	of the queue). Return the number of students that are unable to eat.

	Example 1:
	Input: students = [1,1,0,0], sandwiches = [0,1,0,1]
	Output: 0 
	Explanation:
	- Front student leaves the top sandwich and returns to the end of the line making students = [1,0,0,1].
	- Front student leaves the top sandwich and returns to the end of the line making students = [0,0,1,1].
	- Front student takes the top sandwich and leaves the line making students = [0,1,1] and sandwiches = [1,0,1].
	- Front student leaves the top sandwich and returns to the end of the line making students = [1,1,0].
	- Front student takes the top sandwich and leaves the line making students = [1,0] and sandwiches = [0,1].
	- Front student leaves the top sandwich and returns to the end of the line making students = [0,1].
	- Front student takes the top sandwich and leaves the line making students = [1] and sandwiches = [1].
	- Front student takes the top sandwich and leaves the line making students = [] and sandwiches = [].
	Hence all students are able to eat.

	Example 2:
	Input: students = [1,1,1,0,0,1], sandwiches = [1,0,0,0,1,1]
	Output: 3

	Constraints:
	* 1 <= students.length, sandwiches.length <= 100
	* students.length == sandwiches.length
	* sandwiches[i] is 0 or 1.
	* students[i] is 0 or 1."""

    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        ss = sum(students)
        for i, x in enumerate(sandwiches): 
            if (x and not ss) or (not x and ss == len(sandwiches) - i): return len(sandwiches)-i
            ss -= x 
        return 0 


    """1701. Average Waiting Time (Medium)
	There is a restaurant with a single chef. You are given an array customers, 
	where customers[i] = [arrivali, timei]:
	* arrivali is the arrival time of the ith customer. The arrival times are 
	  sorted in non-decreasing order.
	* timei is the time needed to prepare the order of the ith customer.
	When a customer arrives, he gives the chef his order, and the chef starts 
	preparing it once he is idle. The customer waits till the chef finishes 
	preparing his order. The chef does not prepare food for more than one 
	customer at a time. The chef prepares food for customers in the order they 
	were given in the input. Return the average waiting time of all customers. 
	Solutions within 10-5 from the actual answer are considered accepted.

	Example 1:
	Input: customers = [[1,2],[2,5],[4,3]]
	Output: 5.00000
	Explanation:
	1) The first customer arrives at time 1, the chef takes his order and starts preparing it immediately at time 1, and finishes at time 3, so the waiting time of the first customer is 3 - 1 = 2.
	2) The second customer arrives at time 2, the chef takes his order and starts preparing it at time 3, and finishes at time 8, so the waiting time of the second customer is 8 - 2 = 6.
	3) The third customer arrives at time 4, the chef takes his order and starts preparing it at time 8, and finishes at time 11, so the waiting time of the third customer is 11 - 4 = 7.
	So the average waiting time = (2 + 6 + 7) / 3 = 5.

	Example 2:
	Input: customers = [[5,2],[5,4],[10,3],[20,1]]
	Output: 3.25000
	Explanation:
	1) The first customer arrives at time 5, the chef takes his order and starts preparing it immediately at time 5, and finishes at time 7, so the waiting time of the first customer is 7 - 5 = 2.
	2) The second customer arrives at time 5, the chef takes his order and starts preparing it at time 7, and finishes at time 11, so the waiting time of the second customer is 11 - 5 = 6.
	3) The third customer arrives at time 10, the chef takes his order and starts preparing it at time 11, and finishes at time 14, so the waiting time of the third customer is 14 - 10 = 4.
	4) The fourth customer arrives at time 20, the chef takes his order and starts preparing it immediately at time 20, and finishes at time 21, so the waiting time of the fourth customer is 21 - 20 = 1.
	So the average waiting time = (2 + 6 + 4 + 1) / 4 = 3.25.
	 
	Constraints:
	* 1 <= customers.length <= 105
	* 1 <= arrivali, timei <= 104
	* arrivali <= arrivali+1"""

    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        ans = t = 0
        for arrvl, tt in customers: 
            t = max(t, arrvl) + tt
            ans += t - arrvl
        return ans/len(customers)


    """1702. Maximum Binary String After Change (Medium)
	You are given a binary string binary consisting of only 0's or 1's. You can 
	apply each of the following operations any number of times:
	* Operation 1: If the number contains the substring "00", you can replace it with "10".
	  - For example, "00010" -> "10010"
	* Operation 2: If the number contains the substring "10", you can replace it with "01".
	  - For example, "00010" -> "00001"
	Return the maximum binary string you can obtain after any number of 
	operations. Binary string x is greater than binary string y if x's decimal 
	representation is greater than y's decimal representation.

	Example 1:
	Input: binary = "000110"
	Output: "111011"
	Explanation: A valid transformation sequence can be:
	"000110" -> "000101" 
	"000101" -> "100101" 
	"100101" -> "110101" 
	"110101" -> "110011" 
	"110011" -> "111011"

	Example 2:
	Input: binary = "01"
	Output: "01"
	Explanation: "01" cannot be transformed any further.

	Constraints:
	* 1 <= binary.length <= 105
	* binary consist of '0' and '1'."""

    def maximumBinaryString(self, binary: str) -> str:
        if binary.count("0") <= 1: return binary 
        ones = binary.count("1", binary.index("0"))
        return (len(binary)-ones-1)*"1" + "0" + ones*"1"


    """1703. Minimum Adjacent Swaps for K Consecutive Ones (Hard)
	You are given an integer array, nums, and an integer k. nums comprises of 
	only 0's and 1's. In one move, you can choose two adjacent indices and swap 
	their values. Return the minimum number of moves required so that nums has 
	k consecutive 1's.

	Example 1:
	Input: nums = [1,0,0,1,0,1], k = 2
	Output: 1
	Explanation: In 1 move, nums could be [1,0,0,0,1,1] and have 2 consecutive 1's.

	Example 2:
	Input: nums = [1,0,0,0,0,0,1,1], k = 3
	Output: 5
	Explanation: In 5 moves, the leftmost 1 can be shifted right until nums = [0,0,0,0,0,1,1,1].

	Example 3:
	Input: nums = [1,1,0,1], k = 2
	Output: 0
	Explanation: nums already has 2 consecutive 1's.

	Constraints:
	* 1 <= nums.length <= 105
	* nums[i] is 0 or 1.
	* 1 <= k <= sum(nums)"""

    def minMoves(self, nums: List[int], k: int) -> int:
        loc = [i for i, x in enumerate(nums) if x]
        prefix = [0]
        for x in loc: prefix.append(prefix[-1] + x)
        
        ans = inf
        for i in range(len(loc)-k+1): 
            ans = min(ans, (prefix[i+k] - prefix[i+(k+1)//2]) - (prefix[i+k//2] - prefix[i]))
        return ans - (k//2)*((k+1)//2)


    """1704. Determine if String Halves Are Alike (Easy)
	You are given a string s of even length. Split this string into two halves 
	of equal lengths, and let a be the first half and b be the second half. Two 
	strings are alike if they have the same number of vowels ('a', 'e', 'i', 
	'o', 'u', 'A', 'E', 'I', 'O', 'U'). Notice that s contains uppercase and 
	lowercase letters. Return true if a and b are alike. Otherwise, return 
	false.

	Example 1:
	Input: s = "book"
	Output: true
	Explanation: a = "bo" and b = "ok". a has 1 vowel and b has 1 vowel. 
	             Therefore, they are alike.

	Example 2:
	Input: s = "textbook"
	Output: false
	Explanation: a = "text" and b = "book". a has 1 vowel whereas b has 2. 
	             Therefore, they are not alike. Notice that the vowel o is 
	             counted twice.

	Example 3:
	Input: s = "MerryChristmas"
	Output: false

	Example 4:
	Input: s = "AbCdEfGh"
	Output: true

	Constraints:
	* 2 <= s.length <= 1000
	* s.length is even.
	* s consists of uppercase and lowercase letters."""

    def halvesAreAlike(self, s: str) -> bool:
        cnt = 0
        for i, c in enumerate(s):
            if c in "aeiouAEIOU": cnt += 1 if i < len(s)//2 else -1
        return cnt == 0


    """1705. Maximum Number of Eaten Apples (Medium)
	There is a special kind of apple tree that grows apples every day for n 
	days. On the ith day, the tree grows apples[i] apples that will rot after 
	days[i] days, that is on day i + days[i] the apples will be rotten and 
	cannot be eaten. On some days, the apple tree does not grow any apples, 
	which are denoted by apples[i] == 0 and days[i] == 0. You decided to eat at 
	most one apple a day (to keep the doctors away). Note that you can keep 
	eating after the first n days. Given two integer arrays days and apples of 
	length n, return the maximum number of apples you can eat.

	Example 1:
	Input: apples = [1,2,3,5,2], days = [3,2,1,4,2]
	Output: 7
	Explanation: You can eat 7 apples:
	- On the first day, you eat an apple that grew on the first day.
	- On the second day, you eat an apple that grew on the second day.
	- On the third day, you eat an apple that grew on the second day. After 
	  this day, the apples that grew on the third day rot.
	- On the fourth to the seventh days, you eat apples that grew on the fourth 
	  day.

	Example 2:
	Input: apples = [3,0,0,0,0,2], days = [3,0,0,0,0,2]
	Output: 5
	Explanation: You can eat 5 apples:
	- On the first to the third day you eat apples that grew on the first day.
	- Do nothing on the fouth and fifth days.
	- On the sixth and seventh days you eat apples that grew on the sixth day.

	Constraints:
	* apples.length == n
	* days.length == n
	* 1 <= n <= 2 * 104
	* 0 <= apples[i], days[i] <= 2 * 104
	* days[i] = 0 if and only if apples[i] = 0."""

    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        ans = 0
        
        pq = [] # min-heap 
        for i, (x, d) in enumerate(zip(apples, days)): 
            while pq and pq[0][0] <= i: heappop(pq) # rotten 
            if x: heappush(pq, (i+d, x))
            if pq: 
                ii, x = heappop(pq)
                if x-1: heappush(pq, (ii, x-1))
                ans += 1
        
        i += 1
        while pq: 
            ii, x = heappop(pq)
            x = min(x, ii-i)
            ans += x
            i += x 
        return ans 


    """1706. Where Will the Ball Fall (Medium)
	You have a 2-D grid of size m x n representing a box, and you have n balls. 
	The box is open on the top and bottom sides. Each cell in the box has a 
	diagonal board spanning two corners of the cell that can redirect a ball to 
	the right or to the left.
	* A board that redirects the ball to the right spans the top-left corner to 
	  the bottom-right corner and is represented in the grid as 1.
	* A board that redirects the ball to the left spans the top-right corner to 
	  the bottom-left corner and is represented in the grid as -1.
	We drop one ball at the top of each column of the box. Each ball can get 
	stuck in the box or fall out of the bottom. A ball gets stuck if it hits a 
	"V" shaped pattern between two boards or if a board redirects the ball into 
	either wall of the box. Return an array answer of size n where answer[i] is 
	the column that the ball falls out of at the bottom after dropping the ball 
	from the ith column at the top, or -1 if the ball gets stuck in the box.

	Example 1:
	Input: grid = [[1,1,1,-1,-1],[1,1,1,-1,-1],[-1,-1,-1,1,1],[1,1,1,1,-1],[-1,-1,-1,-1,-1]]
	Output: [1,-1,-1,-1,-1]
	Explanation: This example is shown in the photo.
	Ball b0 is dropped at column 0 and falls out of the box at column 1.
	Ball b1 is dropped at column 1 and will get stuck in the box between column 2 and 3 and row 1.
	Ball b2 is dropped at column 2 and will get stuck on the box between column 2 and 3 and row 0.
	Ball b3 is dropped at column 3 and will get stuck on the box between column 2 and 3 and row 0.
	Ball b4 is dropped at column 4 and will get stuck on the box between column 2 and 3 and row 1.

	Example 2:
	Input: grid = [[-1]]
	Output: [-1]
	Explanation: The ball gets stuck against the left wall.

	Constraints:
	* m == grid.length
	* n == grid[i].length
	* 1 <= m, n <= 100
	* grid[i][j] is 1 or -1."""

    def findBall(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0]) # dimensions
        ans = [-1]*n 
        for j in range(n): 
            k = j
            for i in range(m):
                kk = k + grid[i][k]
                if not 0 <= kk < n or grid[i][k] * grid[i][kk] < 0: break
                k = kk 
            else: ans[j] = k # no break 
        return ans 


    """1707. Maximum XOR With an Element From Array (Hard)
	You are given an array nums consisting of non-negative integers. You are 
	also given a queries array, where queries[i] = [xi, mi]. The answer to the 
	ith query is the maximum bitwise XOR value of xi and any element of nums 
	that does not exceed mi. In other words, the answer is max(nums[j] XOR xi) 
	for all j such that nums[j] <= mi. If all elements in nums are larger than 
	mi, then the answer is -1. Return an integer array answer where 
	answer.length == queries.length and answer[i] is the answer to the ith 
	query.

	Example 1:
	Input: nums = [0,1,2,3,4], queries = [[3,1],[1,3],[5,6]]
	Output: [3,3,7]
	Explanation:
	1) 0 and 1 are the only two integers not greater than 1. 0 XOR 3 = 3 and 
	   1 XOR 3 = 2. The larger of the two is 3.
	2) 1 XOR 2 = 3.
	3) 5 XOR 2 = 7.

	Example 2:
	Input: nums = [5,2,4,6,6,3], queries = [[12,4],[8,1],[6,3]]
	Output: [15,-1,5]

	Constraints:
	* 1 <= nums.length, queries.length <= 105
	* queries[i].length == 2
	* 0 <= nums[j], xi, mi <= 10^9"""

	# class Trie: 
	#     def __init__(self):
	#         self.root = {}
	        
	#     def __bool__(self):
	#         return bool(self.root)
	    
	#     def insert(self, num):
	#         node = self.root 
	#         for x in bin(num)[2:].zfill(32): 
	#             node = node.setdefault(int(x), {})
	#         node["#"] = num
	    
	#     def query(self, num): 
	#         node = self.root
	#         for x in bin(num)[2:].zfill(32):
	#             node = node.get(1 - int(x)) or node.get(int(x))
	#         return num ^ node["#"]

    def maximizeXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        nums.sort()
        queries = sorted((m, x, i) for i, (x, m) in enumerate(queries))
        
        ans = [-1]*len(queries)
        k = 0
        trie = Trie()
        for m, x, i in queries: 
            while k < len(nums) and nums[k] <= m: 
                trie.insert(nums[k])
                k += 1
            if trie: ans[i] = trie.query(x)
        return ans 


    """1708. Largest Subarray Length K (Easy)
	An array A is larger than some array B if for the first index i where 
	A[i] != B[i], A[i] > B[i]. For example, consider 0-indexing:
	* [1,3,2,4] > [1,2,2,4], since at index 1, 3 > 2.
	* [1,4,4,4] < [2,1,1,1], since at index 0, 1 < 2.
	A subarray is a contiguous subsequence of the array. Given an integer array 
	nums of distinct integers, return the largest subarray of nums of length k.

	Example 1:
	Input: nums = [1,4,5,2,3], k = 3
	Output: [5,2,3]
	Explanation: The subarrays of size 3 are: [1,4,5], [4,5,2], and [5,2,3]. Of 
	             these, [5,2,3] is the largest.

	Example 2:
	Input: nums = [1,4,5,2,3], k = 4
	Output: [4,5,2,3]
	Explanation: The subarrays of size 4 are: [1,4,5,2], and [4,5,2,3]. Of 
	             these, [4,5,2,3] is the largest.
	
	Example 3:
	Input: nums = [1,4,5,2,3], k = 1
	Output: [5]

	Constraints:
	* 1 <= k <= nums.length <= 105
	* 1 <= nums[i] <= 109
	* All the integers of nums are unique.

	Follow up: What if the integers in nums are not distinct?"""

    def largestSubarray(self, nums: List[int], k: int) -> List[int]:
        ii = 0
        for i in range(len(nums)-k+1): 
            if nums[i] > nums[ii]: ii = i
        return nums[ii:ii+k]


    """1710. Maximum Units on a Truck (Easy)
	You are assigned to put some amount of boxes onto one truck. You are given 
	a 2D array boxTypes, where boxTypes[i] = [numberOfBoxesi, numberOfUnitsPerBoxi]:
	* numberOfBoxesi is the number of boxes of type i.
	* numberOfUnitsPerBoxi is the number of units in each box of the type i.
	You are also given an integer truckSize, which is the maximum number of 
	boxes that can be put on the truck. You can choose any boxes to put on the 
	truck as long as the number of boxes does not exceed truckSize. Return the 
	maximum total number of units that can be put on the truck.

	Example 1:
	Input: boxTypes = [[1,3],[2,2],[3,1]], truckSize = 4
	Output: 8
	Explanation: There are:
	- 1 box of the first type that contains 3 units.
	- 2 boxes of the second type that contain 2 units each.
	- 3 boxes of the third type that contain 1 unit each.
	You can take all the boxes of the first and second types, and one box of the third type.
	The total number of units will be = (1 * 3) + (2 * 2) + (1 * 1) = 8.

	Example 2:
	Input: boxTypes = [[5,10],[2,5],[4,7],[3,9]], truckSize = 10
	Output: 91

	Constraints:
	* 1 <= boxTypes.length <= 1000
	* 1 <= numberOfBoxesi, numberOfUnitsPerBoxi <= 1000
	* 1 <= truckSize <= 106"""

    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: x[1], reverse=True)
        ans = 0
        for box, unit in boxTypes: 
            box = min(box, truckSize)
            truckSize -= box
            ans += box * unit
        return ans 


    """1711. Count Good Meals (Medium)
	A good meal is a meal that contains exactly two different food items with a 
	sum of deliciousness equal to a power of two. You can pick any two different 
	foods to make a good meal. Given an array of integers deliciousness where 
	deliciousness[i] is the deliciousness of the i​​​​​​th​​​​​​​​ item of food, return the 
	number of different good meals you can make from this list modulo 10^9 + 7. 
	Note that items with different indices are considered different even if they 
	have the same deliciousness value.

	Example 1:
	Input: deliciousness = [1,3,5,7,9]
	Output: 4
	Explanation: The good meals are (1,3), (1,7), (3,5) and, (7,9).
	Their respective sums are 4, 8, 8, and 16, all of which are powers of 2.

	Example 2:
	Input: deliciousness = [1,1,1,3,3,3,7]
	Output: 15
	Explanation: The good meals are (1,1) with 3 ways, (1,3) with 9 ways, and (1,7) with 3 ways.

	Constraints:
	* 1 <= deliciousness.length <= 105
	* 0 <= deliciousness[i] <= 220"""

    def countPairs(self, deliciousness: List[int]) -> int:
        ans = 0
        freq = defaultdict(int)
        for x in deliciousness: 
            for k in range(22): ans += freq[2**k - x]
            freq[x] += 1
        return ans % 1_000_000_007


    """1712. Ways to Split Array Into Three Subarrays (Medium)
	A split of an integer array is good if:
	* The array is split into three non-empty contiguous subarrays - named left, 
	  mid, right respectively from left to right.
	* The sum of the elements in left is less than or equal to the sum of the 
	  elements in mid, and the sum of the elements in mid is less than or equal 
	  to the sum of the elements in right.
	Given nums, an array of non-negative integers, return the number of good 
	ways to split nums. As the number may be too large, return it modulo 10^9 + 7.

	Example 1:
	Input: nums = [1,1,1]
	Output: 1
	Explanation: The only good way to split nums is [1] [1] [1].

	Example 2:
	Input: nums = [1,2,2,2,5,0]
	Output: 3
	Explanation: There are three good ways of splitting nums:
	[1] [2] [2,2,5,0]
	[1] [2,2] [2,5,0]
	[1,2] [2,2] [5,0]

	Example 3:
	Input: nums = [3,2,1]
	Output: 0
	Explanation: There is no good way to split nums.

	Constraints:
	* 3 <= nums.length <= 105
	* 0 <= nums[i] <= 104"""

    def waysToSplit(self, nums: List[int]) -> int:
        prefix = [0]
        for x in nums: prefix.append(prefix[-1] + x)
        
        ans = j = k = 0 
        for i in range(1, len(nums)): 
            j = max(j, i+1)
            while j < len(nums) and 2*prefix[i] > prefix[j]: j += 1
            k = max(k, j)
            while k < len(nums) and 2*prefix[k] <= prefix[i] + prefix[-1]: k += 1
            ans += k - j 
        return ans % 1_000_000_007


    """1713. Minimum Operations to Make a Subsequence (Hard)
	You are given an array target that consists of distinct integers and 
	another integer array arr that can have duplicates. In one operation, you 
	can insert any integer at any position in arr. For example, if arr = [1,4,1,2], 
	you can add 3 in the middle and make it [1,4,3,1,2]. Note that you can 
	insert the integer at the very beginning or end of the array. Return the 
	minimum number of operations needed to make target a subsequence of arr. A 
	subsequence of an array is a new array generated from the original array by 
	deleting some elements (possibly none) without changing the remaining 
	elements' relative order. For example, [2,7,4] is a subsequence of [4,2,3,7,2,1,4] 
	(the underlined elements), while [2,4,2] is not.

	Example 1:
	Input: target = [5,1,3], arr = [9,4,2,3,4]
	Output: 2
	Explanation: You can add 5 and 1 in such a way that makes arr = [5,9,4,1,2,3,4], then target will be a subsequence of arr.

	Example 2:
	Input: target = [6,4,8,1,3,2], arr = [4,7,6,2,3,8,6,1]
	Output: 3

	Constraints:
	* 1 <= target.length, arr.length <= 105
	* 1 <= target[i], arr[i] <= 109
	* target contains no duplicates."""

    def minOperations(self, target: List[int], arr: List[int]) -> int:
        mp = {x: i for i, x in enumerate(target)}
        stack = []
        for x in arr: 
            if x in mp: 
                i = bisect_left(stack, mp[x])
                if i < len(stack): stack[i] = mp[x]
                else: stack.append(mp[x])
        return len(target) - len(stack)


    """1716. Calculate Money in Leetcode Bank (Easy)
	Hercy wants to save money for his first car. He puts money in the Leetcode 
	bank every day. He starts by putting in $1 on Monday, the first day. Every 
	day from Tuesday to Sunday, he will put in $1 more than the day before. On 
	every subsequent Monday, he will put in $1 more than the previous Monday. 
	Given n, return the total amount of money he will have in the Leetcode bank 
	at the end of the nth day.

	Example 1:
	Input: n = 4
	Output: 10
	Explanation: After the 4th day, the total is 1 + 2 + 3 + 4 = 10.

	Example 2:
	Input: n = 10
	Output: 37
	Explanation: After the 10th day, the total is (1 + 2 + 3 + 4 + 5 + 6 + 7) + 
	             (2 + 3 + 4) = 37. Notice that on the 2nd Monday, Hercy only 
	             puts in $2.

	Example 3:
	Input: n = 20
	Output: 96
	Explanation: After the 20th day, the total is (1 + 2 + 3 + 4 + 5 + 6 + 7) + 
	             (2 + 3 + 4 + 5 + 6 + 7 + 8) + (3 + 4 + 5 + 6 + 7 + 8) = 96.

	Constraints: 1 <= n <= 1000"""

    def totalMoney(self, n: int) -> int:
        q, r = divmod(n, 7)
        return ((7*q + (49+2*r))*q + r*(r+1))//2


    """1721. Swapping Nodes in a Linked List (Medium)
	You are given the head of a linked list, and an integer k. Return the head 
	of the linked list after swapping the values of the kth node from the 
	beginning and the kth node from the end (the list is 1-indexed).

	Example 1:
	Input: head = [1,2,3,4,5], k = 2
	Output: [1,4,3,2,5]

	Example 2:
	Input: head = [7,9,6,6,7,8,3,0,9,5], k = 5
	Output: [7,9,6,6,8,7,3,0,9,5]

	Example 3:
	Input: head = [1], k = 1
	Output: [1]

	Example 4:
	Input: head = [1,2], k = 1
	Output: [2,1]

	Example 5:
	Input: head = [1,2,3], k = 2
	Output: [1,2,3]

	Constraints:
	* The number of nodes in the list is n.
	* 1 <= k <= n <= 10^5
	* 0 <= Node.val <= 100"""

    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        node = n1 = n2 = head 
        while node: 
            k -= 1
            if not k: n1 = node 
            if k < 0: n2 = n2.next 
            node = node.next
        n1.val, n2.val = n2.val, n1.val
        return head 


    """1730. Shortest Path to Get Food (Medium)
	You are starving and you want to eat food as quickly as possible. You want 
	to find the shortest path to arrive at any food cell. You are given an m x n 
	character matrix, grid, of these different types of cells:
	* '*' is your location. There is exactly one '*' cell.
	* '#' is a food cell. There may be multiple food cells.
	* 'O' is free space, and you can travel through these cells.
	* 'X' is an obstacle, and you cannot travel through these cells.
	You can travel to any adjacent cell north, east, south, or west of your 
	current location if there is not an obstacle. Return the length of the 
	shortest path for you to reach any food cell. If there is no path for you 
	to reach food, return -1.

	Example 1:
	Input: grid = [["X","X","X","X","X","X"],
	               ["X","*","O","O","O","X"],
	               ["X","O","O","#","O","X"],
	               ["X","X","X","X","X","X"]]
	Output: 3
	Explanation: It takes 3 steps to reach the food.
	
	Example 2:
	Input: grid = [["X","X","X","X","X"],
	               ["X","*","X","O","X"],
	               ["X","O","X","#","X"],
	               ["X","X","X","X","X"]]
	Output: -1
	Explanation: It is not possible to reach the food.
	
	Example 3:
	Input: grid = [["X","X","X","X","X","X","X","X"],
	               ["X","*","O","X","O","#","O","X"],
	               ["X","O","O","X","O","O","X","X"],
	               ["X","O","O","O","O","#","O","X"],
	               ["X","X","X","X","X","X","X","X"]]
	Output: 6
	Explanation: There can be multiple food cells. It only takes 6 steps to reach the bottom food.
	
	Example 4:
	Input: grid = [["O","*"],
	               ["#","O"]]
	Output: 2

	Example 5:
	Input: grid = [["X","*"],
	               ["#","X"]]
	Output: -1

	Constraints:
	* m == grid.length
	* n == grid[i].length
	* 1 <= m, n <= 200
	* grid[row][col] is '*', 'X', 'O', or '#'.
	* The grid contains exactly one '*'."""

    def getFood(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0]) # dimensions 
        
        for i in range(m):
            for j in range(n): 
                if grid[i][j] == "*": break 
            else: continue 
            break 
            
        ans = 0
        queue = [(i, j)]
        grid[i][j] = "X" # mark visited (upon pushing)
        
        while queue: 
            ans += 1
            newq = []
            for i, j in queue: 
                for ii, jj in (i-1, j), (i, j-1), (i, j+1), (i+1, j): 
                    if 0 <= ii < m and 0 <= jj < n and grid[ii][jj] != "X": 
                        if grid[ii][jj] == "#": return ans 
                        newq.append((ii, jj))
                        grid[ii][jj] = "X" # mark visited 
            queue = newq
        return -1 


    """1732. Find the Highest Altitude (Easy)
	There is a biker going on a road trip. The road trip consists of n + 1 
	points at different altitudes. The biker starts his trip on point 0 with 
	altitude equal 0. You are given an integer array gain of length n where 
	gain[i] is the net gain in altitude between points i​​​​​​ and i + 1 for all 
	(0 <= i < n). Return the highest altitude of a point.

	Example 1:
	Input: gain = [-5,1,5,0,-7]
	Output: 1
	Explanation: The altitudes are [0,-5,-4,1,1,-6]. The highest is 1.

	Example 2:
	Input: gain = [-4,-3,-2,-1,4,3,2]
	Output: 0
	Explanation: The altitudes are [0,-4,-7,-9,-10,-6,-3,-1]. The highest is 0.

	Constraints:
	* n == gain.length
	* 1 <= n <= 100
	* -100 <= gain[i] <= 100"""

    def largestAltitude(self, gain: List[int]) -> int:
        ans = prefix = 0
        for x in gain:
            prefix += x
            ans = max(ans, prefix)
        return ans 


    """1732. Find the Highest Altitude (Easy)
	There is a biker going on a road trip. The road trip consists of n + 1 
	points at different altitudes. The biker starts his trip on point 0 with 
	altitude equal 0. You are given an integer array gain of length n where 
	gain[i] is the net gain in altitude between points i​​​​​​ and i + 1 for all 
	(0 <= i < n). Return the highest altitude of a point.

	Example 1:
	Input: gain = [-5,1,5,0,-7]
	Output: 1
	Explanation: The altitudes are [0,-5,-4,1,1,-6]. The highest is 1.

	Example 2:
	Input: gain = [-4,-3,-2,-1,4,3,2]
	Output: 0
	Explanation: The altitudes are [0,-4,-7,-9,-10,-6,-3,-1]. The highest is 0.

	Constraints:
	* n == gain.length
	* 1 <= n <= 100
	* -100 <= gain[i] <= 100"""

    def largestAltitude(self, gain: List[int]) -> int:
        ans = prefix = 0
        for x in gain: 
            prefix += x
            ans = max(ans, prefix)
        return ans 


    """1733. Minimum Number of People to Teach (Medium)
	On a social network consisting of m users and some friendships between 
	users, two users can communicate with each other if they know a common 
	language. You are given an integer n, an array languages, and an array 
	friendships where:
	* There are n languages numbered 1 through n,
	* languages[i] is the set of languages the i​​​​​​th​​​​ user knows, and
	* friendships[i] = [u​​​​​​i​​​, v​​​​​​i] denotes a friendship between the users u​​​​​​​​​​​i​​​​​ and vi.
	You can choose one language and teach it to some users so that all friends 
	can communicate with each other. Return the minimum number of users you 
	need to teach. Note that friendships are not transitive, meaning if x is a 
	friend of y and y is a friend of z, this doesn't guarantee that x is a 
	friend of z.

	Example 1:
	Input: n = 2, languages = [[1],[2],[1,2]], friendships = [[1,2],[1,3],[2,3]]
	Output: 1
	Explanation: You can either teach user 1 the second language or user 2 the first language.

	Example 2:
	Input: n = 3, languages = [[2],[1,3],[1,2],[3]], friendships = [[1,4],[1,2],[3,4],[2,3]]
	Output: 2
	Explanation: Teach the third language to users 1 and 3, yielding two users to teach.

	Constraints:
	* 2 <= n <= 500
	* languages.length == m
	* 1 <= m <= 500
	* 1 <= languages[i].length <= n
	* 1 <= languages[i][j] <= n
	* 1 <= u​​​​​​i < v​​​​​​i <= languages.length
	* 1 <= friendships.length <= 500
	* All tuples (u​​​​​i, v​​​​​​i) are unique
	* languages[i] contains only unique values"""

    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        languages = [set(x) for x in languages]
        
        users = set()
        for u, v in friendships: 
            if not languages[u-1] & languages[v-1]: 
                users.add(u-1)
                users.add(v-1)
        
        freq = {}
        for i in users: 
            for k in languages[i]:
                freq[k] = 1 + freq.get(k, 0)
        return len(users) - max(freq.values(), default=0)


    """1734. Decode XORed Permutation (Medium)
	There is an integer array perm that is a permutation of the first n 
	positive integers, where n is always odd. It was encoded into another 
	integer array encoded of length n - 1, such that 
	encoded[i] = perm[i] XOR perm[i + 1]. 
	For example, if perm = [1,3,2], then encoded = [2,1]. Given the encoded 
	array, return the original array perm. It is guaranteed that the answer 
	exists and is unique.

	Example 1:
	Input: encoded = [3,1]
	Output: [1,2,3]
	Explanation: If perm = [1,2,3], then encoded = [1 XOR 2,2 XOR 3] = [3,1]

	Example 2:
	Input: encoded = [6,5,4,6]
	Output: [2,4,1,5,3]

	Constraints:
	* 3 <= n < 105
	* n is odd.
	* encoded.length == n - 1"""

    def decode(self, encoded: List[int]) -> List[int]:
        x = reduce(xor, list(range(1, len(encoded) + 2)))
        for i in range(1, len(encoded), 2): x ^= encoded[i]
        ans = [x]
        for x in encoded: ans.append(ans[-1] ^ x)
        return ans 


    """1735. Count Ways to Make Array With Product (Hard)
	You are given a 2D integer array, queries. For each queries[i], where 
	queries[i] = [ni, ki], find the number of different ways you can place 
	positive integers into an array of size ni such that the product of the 
	integers is ki. As the number of ways may be too large, the answer to the 
	ith query is the number of ways modulo 109 + 7. Return an integer array 
	answer where answer.length == queries.length, and answer[i] is the answer 
	to the ith query.

	Example 1:
	Input: queries = [[2,6],[5,1],[73,660]]
	Output: [4,1,50734910]
	Explanation: Each query is independent.
	[2,6]: There are 4 ways to fill an array of size 2 that multiply to 6: [1,6], [2,3], [3,2], [6,1].
	[5,1]: There is 1 way to fill an array of size 5 that multiply to 1: [1,1,1,1,1].
	[73,660]: There are 1050734917 ways to fill an array of size 73 that multiply to 660. 1050734917 modulo 109 + 7 = 50734910.

	Example 2:
	Input: queries = [[1,1],[2,2],[3,3],[4,4],[5,5]]
	Output: [1,2,3,10,5]

	Constraints:
	* 1 <= queries.length <= 104
	* 1 <= ni, ki <= 104"""

    def waysToFillArray(self, queries: List[List[int]]) -> List[int]:
        spf = list(range(10001)) # spf = smallest prime factor 
        for i in range(4, 10001, 2): spf[i] = 2
        for i in range(3, int(sqrt(10001))+1): 
            if spf[i] == i: 
                for ii in range(i*i, 10001, i): 
                    spf[ii] = min(spf[ii], i)
        
        ans = []
        for n, k in queries: 
            freq = {} # prime factorization via sieve
            while k != 1: 
                freq[spf[k]] = 1 + freq.get(spf[k], 0)
                k //= spf[k]
            val = 1
            for x in freq.values(): 
                val *= comb(n+x-1, x)
            ans.append(val % 1_000_000_007)
        return ans 


    """1736. Latest Time by Replacing Hidden Digits (Easy)
	You are given a string time in the form of hh:mm, where some of the digits 
	in the string are hidden (represented by ?). The valid times are those 
	inclusively between 00:00 and 23:59. Return the latest valid time you can 
	get from time by replacing the hidden digits.

	Example 1:
	Input: time = "2?:?0"
	Output: "23:50"
	Explanation: The latest hour beginning with the digit '2' is 23 and the 
	             latest minute ending with the digit '0' is 50.

	Example 2:
	Input: time = "0?:3?"
	Output: "09:39"

	Example 3:
	Input: time = "1?:22"
	Output: "19:22"

	Constraints:
	* time is in the format hh:mm.
	* It is guaranteed that you can produce a valid time from the given string."""

    def maximumTime(self, time: str) -> str:
        time = list(time)
        for i in range(len(time)): 
            if time[i] == "?": 
                if i == 0: time[i] = "2" if time[i+1] in "?0123" else "1"
                elif i == 1: time[i] = "3" if time[0] == "2" else "9"
                elif i == 3: time[i] = "5"
                else: time[i] = "9"
        return "".join(time)


    """1737. Change Minimum Characters to Satisfy One of Three Conditions (Medium)
	You are given two strings a and b that consist of lowercase letters. In one 
	operation, you can change any character in a or b to any lowercase letter. 
	Your goal is to satisfy one of the following three conditions:
	* Every letter in a is strictly less than every letter in b in the alphabet.
	* Every letter in b is strictly less than every letter in a in the alphabet.
	* Both a and b consist of only one distinct letter.
	Return the minimum number of operations needed to achieve your goal.

	Example 1:
	Input: a = "aba", b = "caa"
	Output: 2
	Explanation: Consider the best way to make each condition true:
	1) Change b to "ccc" in 2 operations, then every letter in a is less than 
	   every letter in b.
	2) Change a to "bbb" and b to "aaa" in 3 operations, then every letter in b 
	   is less than every letter in a.
	3) Change a to "aaa" and b to "aaa" in 2 operations, then a and b consist 
	   of one distinct letter.
	The best way was done in 2 operations (either condition 1 or condition 3).

	Example 2:
	Input: a = "dabadd", b = "cda"
	Output: 3
	Explanation: The best way is to make condition 1 true by changing b to "eee".

	Constraints:
	* 1 <= a.length, b.length <= 105
	* a and b consist only of lowercase letters."""

    def minCharacters(self, a: str, b: str) -> int:
        pa, pb = [0]*26, [0]*26
        for x in a: pa[ord(x)-97] += 1
        for x in b: pb[ord(x)-97] += 1
        
        ans = len(a) - max(pa) + len(b) - max(pb) # condition 3
        for i in range(25): 
            pa[i+1] += pa[i]
            pb[i+1] += pb[i]
            ans = min(ans, pa[i] + len(b) - pb[i]) # condition 2
            ans = min(ans, len(a) - pa[i] + pb[i]) # condition 1
        return ans 


    """1738. Find Kth Largest XOR Coordinate Value (Medium)
	You are given a 2D matrix of size m x n, consisting of non-negative 
	integers. You are also given an integer k. The value of coordinate (a, b) 
	of the matrix is the XOR of all matrix[i][j] where 0 <= i <= a < m and 
	0 <= j <= b < n (0-indexed). Find the kth largest value (1-indexed) of all 
	the coordinates of matrix.

	Example 1:
	Input: matrix = [[5,2],[1,6]], k = 1
	Output: 7
	Explanation: The value of coordinate (0,1) is 5 XOR 2 = 7, which is the largest value.

	Example 2:
	Input: matrix = [[5,2],[1,6]], k = 2
	Output: 5
	Explanation: The value of coordinate (0,0) is 5 = 5, which is the 2nd largest value.

	Example 3:
	Input: matrix = [[5,2],[1,6]], k = 3
	Output: 4
	Explanation: The value of coordinate (1,0) is 5 XOR 1 = 4, which is the 3rd largest value.

	Example 4:
	Input: matrix = [[5,2],[1,6]], k = 4
	Output: 0
	Explanation: The value of coordinate (1,1) is 5 XOR 2 XOR 1 XOR 6 = 0, which is the 4th largest value.

	Constraints:
	* m == matrix.length
	* n == matrix[i].length
	* 1 <= m, n <= 1000
	* 0 <= matrix[i][j] <= 106
	* 1 <= k <= m * n"""

    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0]) # dimensions 
        
        pq = []
        for i in range(m): 
            for j in range(n): 
                if i: matrix[i][j] ^= matrix[i-1][j]
                if j: matrix[i][j] ^= matrix[i][j-1]
                if i and j: matrix[i][j] ^= matrix[i-1][j-1]
                heappush(pq, matrix[i][j])
                if len(pq) > k: heappop(pq)
        return pq[0]


    """1739. Building Boxes (Hard)
	You have a cubic storeroom where the width, length, and height of the room 
	are all equal to n units. You are asked to place n boxes in this room where 
	each box is a cube of unit side length. There are however some rules to 
	placing the boxes:
	* You can place the boxes anywhere on the floor.
	* If box x is placed on top of the box y, then each side of the four 
	  vertical sides of the box y must either be adjacent to another box or to 
	  a wall.
	Given an integer n, return the minimum possible number of boxes touching 
	the floor.

	Example 1:
	Input: n = 3
	Output: 3
	Explanation: The figure above is for the placement of the three boxes. 
	             These boxes are placed in the corner of the room, where the 
	             corner is on the left side.

	Example 2:
	Input: n = 4
	Output: 3
	Explanation: The figure above is for the placement of the four boxes. These 
	             boxes are placed in the corner of the room, where the corner 
	             is on the left side.
	
	Example 3:
	Input: n = 10
	Output: 6
	Explanation: The figure above is for the placement of the ten boxes. These 
	             boxes are placed in the corner of the room, where the corner 
	             is on the back side.

	Constraints: 1 <= n <= 10^9"""

    def minimumBoxes(self, n: int) -> int:
        x = int((6*n)**(1/3))
        if x*(x+1)*(x+2) > 6*n: x -= 1
        n -= x*(x+1)*(x+2)//6
        return x*(x+1)//2 + ceil((sqrt(1+8*n)-1)/2)


    """1742. Maximum Number of Balls in a Box (Easy)
	You are working in a ball factory where you have n balls numbered from 
	lowLimit up to highLimit inclusive (i.e., n == highLimit - lowLimit + 1), 
	and an infinite number of boxes numbered from 1 to infinity. Your job at 
	this factory is to put each ball in the box with a number equal to the sum 
	of digits of the ball's number. For example, the ball number 321 will be 
	put in the box number 3 + 2 + 1 = 6 and the ball number 10 will be put in 
	the box number 1 + 0 = 1. Given two integers lowLimit and highLimit, return 
	the number of balls in the box with the most balls.

	Example 1:
	Input: lowLimit = 1, highLimit = 10
	Output: 2
	Explanation:
	Box Number:  1 2 3 4 5 6 7 8 9 10 11 ...
	Ball Count:  2 1 1 1 1 1 1 1 1 0  0  ...
	Box 1 has the most number of balls with 2 balls.

	Example 2:
	Input: lowLimit = 5, highLimit = 15
	Output: 2
	Explanation:
	Box Number:  1 2 3 4 5 6 7 8 9 10 11 ...
	Ball Count:  1 1 1 1 2 2 1 1 1 0  0  ...
	Boxes 5 and 6 have the most number of balls with 2 balls in each.

	Example 3:
	Input: lowLimit = 19, highLimit = 28
	Output: 2
	Explanation:
	Box Number:  1 2 3 4 5 6 7 8 9 10 11 12 ...
	Ball Count:  0 1 1 1 1 1 1 1 1 2  0  0  ...
	Box 10 has the most number of balls with 2 balls.
	 
	Constraints: 1 <= lowLimit <= highLimit <= 10^5"""

    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        freq = {}
        for x in range(lowLimit, highLimit+1):
            key = sum(int(xx) for xx in str(x))
            freq[key] = 1 + freq.get(key, 0) 
        return max(freq.values())


    """1743. Restore the Array From Adjacent Pairs (Medium)
	There is an integer array nums that consists of n unique elements, but you 
	have forgotten it. However, you do remember every pair of adjacent elements 
	in nums. You are given a 2D integer array adjacentPairs of size n - 1 where 
	each adjacentPairs[i] = [ui, vi] indicates that the elements ui and vi are 
	adjacent in nums. It is guaranteed that every adjacent pair of elements 
	nums[i] and nums[i+1] will exist in adjacentPairs, either as [nums[i], 
	nums[i+1]] or [nums[i+1], nums[i]]. The pairs can appear in any order. 
	Return the original array nums. If there are multiple solutions, return any 
	of them.

	Example 1:
	Input: adjacentPairs = [[2,1],[3,4],[3,2]]
	Output: [1,2,3,4]
	Explanation: This array has all its adjacent pairs in adjacentPairs. Notice 
	             that adjacentPairs[i] may not be in left-to-right order.

	Example 2:
	Input: adjacentPairs = [[4,-2],[1,4],[-3,1]]
	Output: [-2,4,1,-3]
	Explanation: There can be negative numbers. Another solution is [-3,1,4,-2], 
	             which would also be accepted.
	
	Example 3:
	Input: adjacentPairs = [[100000,-100000]]
	Output: [100000,-100000]

	Constraints:
	* nums.length == n
	* adjacentPairs.length == n - 1
	* adjacentPairs[i].length == 2
	* 2 <= n <= 105
	* -10^5 <= nums[i], ui, vi <= 10^5
	* There exists some nums that has adjacentPairs as its pairs."""

    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        graph = {}
        for u, v in adjacentPairs: 
            graph.setdefault(u, []).append(v)
            graph.setdefault(v, []).append(u)
        
        ans = []
        seen = set()
        stack = [next(x for x in graph if len(graph[x]) == 1)]
        while stack: 
            n = stack.pop()
            ans.append(n)
            seen.add(n)
            for nn in graph[n]: 
                if nn not in seen: stack.append(nn)
        return ans 


    """1744. Can You Eat Your Favorite Candy on Your Favorite Day? (Medium)
	You are given a (0-indexed) array of positive integers candiesCount where 
	candiesCount[i] represents the number of candies of the ith type you have. 
	You are also given a 2D array queries where 
	queries[i] = [favoriteTypei, favoriteDayi, dailyCapi].

	You play a game with the following rules:
	* You start eating candies on day 0.
	* You cannot eat any candy of type i unless you have eaten all candies of 
	  type i - 1.
	* You must eat at least one candy per day until you have eaten all the 
	  candies.
	Construct a boolean array answer such that answer.length == queries.length 
	and answer[i] is true if you can eat a candy of type favoriteTypei on day 
	favoriteDayi without eating more than dailyCapi candies on any day, and 
	false otherwise. Note that you can eat different types of candy on the same 
	day, provided that you follow rule 2. Return the constructed array answer.

	Example 1:
	Input: candiesCount = [7,4,5,3,8], queries = [[0,2,2],[4,2,4],[2,13,1000000000]]
	Output: [true,false,true]
	Explanation:
	1- If you eat 2 candies (type 0) on day 0 and 2 candies (type 0) on day 1, you will eat a candy of type 0 on day 2.
	2- You can eat at most 4 candies each day.
	   If you eat 4 candies every day, you will eat 4 candies (type 0) on day 0 and 4 candies (type 0 and type 1) on day 1.
	   On day 2, you can only eat 4 candies (type 1 and type 2), so you cannot eat a candy of type 4 on day 2.
	3- If you eat 1 candy each day, you will eat a candy of type 2 on day 13.

	Example 2:
	Input: candiesCount = [5,2,6,4,1], queries = [[3,1,2],[4,10,3],[3,10,100],[4,100,30],[1,3,1]]
	Output: [false,true,true,false,false]

	Constraints:
	* 1 <= candiesCount.length <= 10^5
	* 1 <= candiesCount[i] <= 10^5
	* 1 <= queries.length <= 10^5
	* queries[i].length == 3
	* 0 <= favoriteTypei < candiesCount.length
	* 0 <= favoriteDayi <= 10^9
	* 1 <= dailyCapi <= 10^9"""

    def canEat(self, candiesCount: List[int], queries: List[List[int]]) -> List[bool]:
        prefix = [0]
        for x in candiesCount: prefix.append(prefix[-1] + x) # prefix sum 
        return [prefix[t] < (day+1)*cap and day < prefix[t+1] for t, day, cap in queries]


    """1745. Palindrome Partitioning IV (Hard)
	Given a string s, return true if it is possible to split the string s into 
	three non-empty palindromic substrings. Otherwise, return false.​​​​​ A string 
	is said to be palindrome if it the same string when reversed.

	Example 1:
	Input: s = "abcbdd"
	Output: true
	Explanation: "abcbdd" = "a" + "bcb" + "dd", and all three substrings are 
	             palindromes.

	Example 2:
	Input: s = "bcbddxy"
	Output: false
	Explanation: s cannot be split into 3 palindromes.

	Constraints:
	* 3 <= s.length <= 2000
	* s​​​​​​ consists only of lowercase English letters."""

    def checkPartitioning(self, s: str) -> bool:
        mp = defaultdict(set)
        for i in range(2*len(s)-1): 
            lo, hi = i//2, (i+1)//2
            while 0 <= lo <= hi < len(s) and s[lo] == s[hi]: 
                mp[lo].add(hi)
                lo, hi = lo-1, hi+1
        
        for i in range(len(s)):
            for j in range(i+1, len(s)):
                if i-1 in mp[0] and j-1 in mp[i] and len(s)-1 in mp[j]: return True
        return False 


    """1746. Maximum Subarray Sum After One Operation (Medium)
	You are given an integer array nums. You must perform exactly one operation 
	where you can replace one element nums[i] with nums[i] * nums[i]. Return 
	the maximum possible subarray sum after exactly one operation. The subarray 
	must be non-empty.

	Example 1:
	Input: nums = [2,-1,-4,-3]
	Output: 17
	Explanation: You can perform the operation on index 2 (0-indexed) to make 
	             nums = [2,-1,16,-3]. Now, the maximum subarray sum is 
	             2 + -1 + 16 = 17.

	Example 2:
	Input: nums = [1,-1,1,1,-1,-1,1]
	Output: 4
	Explanation: You can perform the operation on index 1 (0-indexed) to make 
	             nums = [1,1,1,1,-1,-1,1]. Now, the maximum subarray sum is 
	             1 + 1 + 1 + 1 = 4.

	Constraints:
	* 1 <= nums.length <= 105
	* -104 <= nums[i] <= 104"""

    def maxSumAfterOperation(self, nums: List[int]) -> int:
        ans = f0 = f1 = 0 
        for x in nums: 
            f1 = max(max(0, f0) + x*x, f1 + x)
            f0 = max(0, f0) + x 
            ans = max(ans, f1)
        return ans 


    """1748. Sum of Unique Elements (Easy)
	You are given an integer array nums. The unique elements of an array are 
	the elements that appear exactly once in the array. Return the sum of all 
	the unique elements of nums.

	Example 1:
	Input: nums = [1,2,3,2]
	Output: 4
	Explanation: The unique elements are [1,3], and the sum is 4.

	Example 2:
	Input: nums = [1,1,1,1,1]
	Output: 0
	Explanation: There are no unique elements, and the sum is 0.

	Example 3:
	Input: nums = [1,2,3,4,5]
	Output: 15
	Explanation: The unique elements are [1,2,3,4,5], and the sum is 15.

	Constraints:
	* 1 <= nums.length <= 100
	* 1 <= nums[i] <= 100"""

    def sumOfUnique(self, nums: List[int]) -> int:
        freq = {}
        for x in nums: freq[x] = 1 + freq.get(x, 0)
        return sum(x for x in nums if freq[x] == 1)


    """1749. Maximum Absolute Sum of Any Subarray (Medium)
	You are given an integer array nums. The absolute sum of a subarray 
	[numsl, numsl+1, ..., numsr-1, numsr] is abs(numsl + numsl+1 + ... + numsr-1 + numsr).
	Return the maximum absolute sum of any (possibly empty) subarray of nums. 
	Note that abs(x) is defined as follows:
	* If x is a negative integer, then abs(x) = -x.
	* If x is a non-negative integer, then abs(x) = x.

	Example 1:
	Input: nums = [1,-3,2,3,-4]
	Output: 5
	Explanation: The subarray [2,3] has absolute sum = abs(2+3) = abs(5) = 5.

	Example 2:
	Input: nums = [2,-5,1,-4,3,-2]
	Output: 8
	Explanation: The subarray [-5,1,-4] has absolute sum = abs(-5+1-4) = abs(-8) = 8.

	Constraints:
	* 1 <= nums.length <= 105
	* -104 <= nums[i] <= 104"""

    def maxAbsoluteSum(self, nums: List[int]) -> int:
        ans = mx = mn = 0
        for x in nums: 
            mx = max(mx + x, 0)
            mn = min(mn + x, 0)
            ans = max(ans, mx, -mn)
        return ans 


    """1750. Minimum Length of String After Deleting Similar Ends (Medium)
	Given a string s consisting only of characters 'a', 'b', and 'c'. You are 
	asked to apply the following algorithm on the string any number of times:
	* Pick a non-empty prefix from the string s where all the characters in the 
	  prefix are equal.
	* Pick a non-empty suffix from the string s where all the characters in 
	  this suffix are equal.
	* The prefix and the suffix should not intersect at any index.
	* The characters from the prefix and suffix must be the same.
	* Delete both the prefix and the suffix.
	Return the minimum length of s after performing the above operation any 
	number of times (possibly zero times).

	Example 1:
	Input: s = "ca"
	Output: 2
	Explanation: You can't remove any characters, so the string stays as is.

	Example 2:
	Input: s = "cabaabac"
	Output: 0
	Explanation: An optimal sequence of operations is:
	- Take prefix = "c" and suffix = "c" and remove them, s = "abaaba".
	- Take prefix = "a" and suffix = "a" and remove them, s = "baab".
	- Take prefix = "b" and suffix = "b" and remove them, s = "aa".
	- Take prefix = "a" and suffix = "a" and remove them, s = "".

	Example 3:
	Input: s = "aabccabba"
	Output: 3
	Explanation: An optimal sequence of operations is:
	- Take prefix = "aa" and suffix = "a" and remove them, s = "bccabb".
	- Take prefix = "b" and suffix = "bb" and remove them, s = "cca".

	Constraints:
	* 1 <= s.length <= 105
	* s only consists of characters 'a', 'b', and 'c'."""

    def minimumLength(self, s: str) -> int:
        lo, hi = 0, len(s)-1
        while lo < hi and s[lo] == s[hi]:
            ch = s[lo]
            while lo <= hi and s[lo] == ch: lo += 1
            while lo <= hi and s[hi] == ch: hi -= 1
        return hi - lo + 1


    """1751. Maximum Number of Events That Can Be Attended II (Hard)
	You are given an array of events where events[i] = [startDayi, endDayi, valuei]. 
	The ith event starts at startDayi and ends at endDayi, and if you attend 
	this event, you will receive a value of valuei. You are also given an 
	integer k which represents the maximum number of events you can attend. You 
	can only attend one event at a time. If you choose to attend an event, you 
	must attend the entire event. Note that the end day is inclusive: that is, 
	you cannot attend two events where one of them starts and the other ends on 
	the same day. Return the maximum sum of values that you can receive by 
	attending events.

	Example 1:
	Input: events = [[1,2,4],[3,4,3],[2,3,1]], k = 2
	Output: 7
	Explanation: Choose the green events, 0 and 1 (0-indexed) for a total value 
	             of 4 + 3 = 7.

	Example 2:
	Input: events = [[1,2,4],[3,4,3],[2,3,10]], k = 2
	Output: 10
	Explanation: Choose event 2 for a total value of 10. Notice that you cannot 
	             attend any other event as they overlap, and that you do not 
	             have to attend k events.

	Example 3:
	Input: events = [[1,1,1],[2,2,2],[3,3,3],[4,4,4]], k = 3
	Output: 9
	Explanation: Although the events do not overlap, you can only attend 3 
	             events. Pick the highest valued three.

	Constraints:
	* 1 <= k <= events.length
	* 1 <= k * events.length <= 106
	* 1 <= startDayi <= endDayi <= 109
	* 1 <= valuei <= 106"""

    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort()
        starts = [i for i, _, _ in events]
        
        @cache
        def fn(i, k): 
            """Return """
            if i == len(events) or k == 0: return 0 
            ii = bisect_left(starts, events[i][1]+1)
            return max(fn(i+1, k), events[i][2] + fn(ii, k-1))
        
        return fn(0, k)


    """1752. Check if Array Is Sorted and Rotated (Easy)
	Given an array nums, return true if the array was originally sorted in non-
	decreasing order, then rotated some number of positions (including zero). 
	Otherwise, return false. There may be duplicates in the original array. 
	Note: An array A rotated by x positions results in an array B of the same 
	length such that A[i] == B[(i+x) % A.length], where % is the modulo operation.

	Example 1:
	Input: nums = [3,4,5,1,2]
	Output: true
	Explanation: [1,2,3,4,5] is the original sorted array. You can rotate the 
	             array by x = 3 positions to begin on the the element of value 
	             3: [3,4,5,1,2].
	
	Example 2:
	Input: nums = [2,1,3,4]
	Output: false
	Explanation: There is no sorted array once rotated that can make nums.
	
	Example 3:
	Input: nums = [1,2,3]
	Output: true
	Explanation: [1,2,3] is the original sorted array. You can rotate the array 
	             by x = 0 positions (i.e. no rotation) to make nums.
	
	Example 4:
	Input: nums = [1,1,1]
	Output: true
	Explanation: [1,1,1] is the original sorted array. You can rotate any 
	             number of positions to make nums.
	
	Example 5:
	Input: nums = [2,1]
	Output: true
	Explanation: [1,2] is the original sorted array. You can rotate the array 
	             by x = 5 positions to begin on the element of value 2: [2,1].

	Constraints:
	* 1 <= nums.length <= 100
	* 1 <= nums[i] <= 100"""

    def check(self, nums: List[int]) -> bool:
        cnt = 0
        for i in range(len(nums)): 
            if nums[i-1] > nums[i]: cnt += 1
        return cnt <= 1


    """1753. Maximum Score From Removing Stones (Medium)
	You are playing a solitaire game with three piles of stones of sizes 
	a​​​​​​, b,​​​​​​ and c​​​​​​ respectively. Each turn you choose two different non-empty 
	piles, take one stone from each, and add 1 point to your score. The game 
	stops when there are fewer than two non-empty piles (meaning there are no 
	more available moves). Given three integers a​​​​​, b,​​​​​ and c​​​​​, return the 
	maximum score you can get.

	Example 1:
	Input: a = 2, b = 4, c = 6
	Output: 6
	Explanation: The starting state is (2, 4, 6). One optimal set of moves is:
	- Take from 1st and 3rd piles, state is now (1, 4, 5)
	- Take from 1st and 3rd piles, state is now (0, 4, 4)
	- Take from 2nd and 3rd piles, state is now (0, 3, 3)
	- Take from 2nd and 3rd piles, state is now (0, 2, 2)
	- Take from 2nd and 3rd piles, state is now (0, 1, 1)
	- Take from 2nd and 3rd piles, state is now (0, 0, 0)
	There are fewer than two non-empty piles, so the game ends. Total: 6 points.

	Example 2:
	Input: a = 4, b = 4, c = 6
	Output: 7
	Explanation: The starting state is (4, 4, 6). One optimal set of moves is:
	- Take from 1st and 2nd piles, state is now (3, 3, 6)
	- Take from 1st and 3rd piles, state is now (2, 3, 5)
	- Take from 1st and 3rd piles, state is now (1, 3, 4)
	- Take from 1st and 3rd piles, state is now (0, 3, 3)
	- Take from 2nd and 3rd piles, state is now (0, 2, 2)
	- Take from 2nd and 3rd piles, state is now (0, 1, 1)
	- Take from 2nd and 3rd piles, state is now (0, 0, 0)
	There are fewer than two non-empty piles, so the game ends. Total: 7 points.

	Example 3:
	Input: a = 1, b = 8, c = 8
	Output: 8
	Explanation: One optimal set of moves is to take from the 2nd and 3rd piles 
	             for 8 turns until they are empty. After that, there are fewer 
	             than two non-empty piles, so the game ends.

	Constraints: 1 <= a, b, c <= 105"""

    def maximumScore(self, a: int, b: int, c: int) -> int:
        a, b, c = sorted((a, b, c))
        if a + b < c: return a + b
        return (a + b + c)//2

    
    """1754. Largest Merge Of Two Strings (Medium)
	You are given two strings word1 and word2. You want to construct a string 
	merge in the following way: while either word1 or word2 are non-empty, 
	choose one of the following options:
	* If word1 is non-empty, append the first character in word1 to merge and 
	  delete it from word1.
	  + For example, if word1 = "abc" and merge = "dv", then after choosing 
	    this operation, word1 = "bc" and merge = "dva".
	* If word2 is non-empty, append the first character in word2 to merge and 
	  delete it from word2.
	  + For example, if word2 = "abc" and merge = "", then after choosing this 
	    operation, word2 = "bc" and merge = "a".
	Return the lexicographically largest merge you can construct. A string a is 
	lexicographically larger than a string b (of the same length) if in the 
	first position where a and b differ, a has a character strictly larger than 
	the corresponding character in b. For example, "abcd" is lexicographically 
	larger than "abcc" because the first position they differ is at the fourth 
	character, and d is greater than c.

	Example 1:
	Input: word1 = "cabaa", word2 = "bcaaa"
	Output: "cbcabaaaaa"
	Explanation: One way to get the lexicographically largest merge is:
	- Take from word1: merge = "c", word1 = "abaa", word2 = "bcaaa"
	- Take from word2: merge = "cb", word1 = "abaa", word2 = "caaa"
	- Take from word2: merge = "cbc", word1 = "abaa", word2 = "aaa"
	- Take from word1: merge = "cbca", word1 = "baa", word2 = "aaa"
	- Take from word1: merge = "cbcab", word1 = "aa", word2 = "aaa"
	- Append the remaining 5 a's from word1 and word2 at the end of merge.

	Example 2:
	Input: word1 = "abcabc", word2 = "abdcaba"
	Output: "abdcabcabcaba"

	Constraints:
	* 1 <= word1.length, word2.length <= 3000
	* word1 and word2 consist only of lowercase English letters."""

    def largestMerge(self, word1: str, word2: str) -> str:
        ans = []
        i1 = i2 = 0
        while i1 < len(word1) and i2 < len(word2): 
            if word1[i1:] > word2[i2:]: 
                ans.append(word1[i1])
                i1 += 1
            else: 
                ans.append(word2[i2])
                i2 += 1
        return "".join(ans) + word1[i1:] + word2[i2:]


    """1755. Closest Subsequence Sum (Hard)
	You are given an integer array nums and an integer goal. You want to choose 
	a subsequence of nums such that the sum of its elements is the closest 
	possible to goal. That is, if the sum of the subsequence's elements is sum, 
	then you want to minimize the absolute difference abs(sum - goal). Return 
	the minimum possible value of abs(sum - goal). Note that a subsequence of 
	an array is an array formed by removing some elements (possibly all or none) 
	of the original array.

	Example 1:
	Input: nums = [5,-7,3,5], goal = 6
	Output: 0
	Explanation: Choose the whole array as a subsequence, with a sum of 6. This 
	             is equal to the goal, so the absolute difference is 0.

	Example 2:
	Input: nums = [7,-9,15,-2], goal = -5
	Output: 1
	Explanation: Choose the subsequence [7,-9,-2], with a sum of -4. The 
	             absolute difference is abs(-4 - (-5)) = abs(1) = 1, which is 
	             the minimum.
	
	Example 3:
	Input: nums = [1,2,3], goal = -7
	Output: 7

	Constraints:
	* 1 <= nums.length <= 40
	* -10^7 <= nums[i] <= 10^7
	* -10^9 <= goal <= 10^9"""

    def minAbsDifference(self, nums: List[int], goal: int) -> int:
        
        def fn(nums):
            ans = {0}
            for x in nums: 
                ans |= {x + y for y in ans}
            return ans 
        
        nums0 = sorted(fn(nums[:len(nums)//2]))
        nums1 = sorted(fn(nums[len(nums)//2:]))
        
        ans = inf
        k = len(nums1)-1
        for x in nums0: 
            while 0 <= k and x + nums1[k] > goal: k -= 1
            if 0 <= k: ans = min(ans, goal - x - nums1[k])
            if k+1 < len(nums1): ans = min(ans, nums1[k+1] + x - goal)
        return ans 


    """1758. Minimum Changes To Make Alternating Binary String (Easy)
	You are given a string s consisting only of the characters '0' and '1'. In 
	one operation, you can change any '0' to '1' or vice versa. The string is 
	called alternating if no two adjacent characters are equal. For example, 
	the string "010" is alternating, while the string "0100" is not. Return the 
	minimum number of operations needed to make s alternating.

	Example 1:
	Input: s = "0100"
	Output: 1
	Explanation: If you change the last character to '1', s will be "0101", which is alternating.

	Example 2:
	Input: s = "10"
	Output: 0
	Explanation: s is already alternating.

	Example 3:
	Input: s = "1111"
	Output: 2
	Explanation: You need two operations to reach "0101" or "1010".

	Constraints:
	* 1 <= s.length <= 104
	* s[i] is either '0' or '1'."""

    def minOperations(self, s: str) -> int:
        cnt = 0 # "010101..."
        for i, c in enumerate(s): 
            if i&1 == int(c): cnt += 1
        return min(cnt, len(s) - cnt)


    """1759. Count Number of Homogenous Substrings (Medium)
	Given a string s, return the number of homogenous substrings of s. Since 
	the answer may be too large, return it modulo 10^9 + 7.  string is 
	homogenous if all the characters of the string are the same. A substring 
	is a contiguous sequence of characters within a string.

	Example 1:
	Input: s = "abbcccaa"
	Output: 13
	Explanation: The homogenous substrings are listed as below:
	"a"   appears 3 times.
	"aa"  appears 1 time.
	"b"   appears 2 times.
	"bb"  appears 1 time.
	"c"   appears 3 times.
	"cc"  appears 2 times.
	"ccc" appears 1 time.
	3 + 1 + 2 + 1 + 3 + 2 + 1 = 13.

	Example 2:
	Input: s = "xy"
	Output: 2
	Explanation: The homogenous substrings are "x" and "y".

	Example 3:
	Input: s = "zzzzz"
	Output: 15

	Constraints:
	* 1 <= s.length <= 105
	* s consists of lowercase letters."""

    def countHomogenous(self, s: str) -> int:
        ans = ii = 0
        for i in range(len(s)):
            if s[ii] != s[i]: ii = i
            ans += i - ii + 1
        return ans % 1_000_000_007


    """1760. Minimum Limit of Balls in a Bag (Medium)
	You are given an integer array nums where the ith bag contains nums[i] 
	balls. You are also given an integer maxOperations. You can perform the 
	following operation at most maxOperations times:
	* Take any bag of balls and divide it into two new bags with a positive 
	  number of balls.
	  + For example, a bag of 5 balls can become two new bags of 1 and 4 balls, 
	    or two new bags of 2 and 3 balls.
	Your penalty is the maximum number of balls in a bag. You want to minimize 
	your penalty after the operations. Return the minimum possible penalty 
	after performing the operations.

	Example 1:
	Input: nums = [9], maxOperations = 2
	Output: 3
	Explanation: 
	- Divide the bag with 9 balls into two bags of sizes 6 and 3. [9] -> [6,3].
	- Divide the bag with 6 balls into two bags of sizes 3 and 3. [6,3] -> [3,3,3].
	The bag with the most number of balls has 3 balls, so your penalty is 3 and you should return 3.

	Example 2:
	Input: nums = [2,4,8,2], maxOperations = 4
	Output: 2
	Explanation:
	- Divide the bag with 8 balls into two bags of sizes 4 and 4. [2,4,8,2] -> [2,4,4,4,2].
	- Divide the bag with 4 balls into two bags of sizes 2 and 2. [2,4,4,4,2] -> [2,2,2,4,4,2].
	- Divide the bag with 4 balls into two bags of sizes 2 and 2. [2,2,2,4,4,2] -> [2,2,2,2,2,4,2].
	- Divide the bag with 4 balls into two bags of sizes 2 and 2. [2,2,2,2,2,4,2] -> [2,2,2,2,2,2,2,2].
	The bag with the most number of balls has 2 balls, so your penalty is 2 an you should return 2.

	Example 3:
	Input: nums = [7,17], maxOperations = 2
	Output: 7

	Constraints:
	* 1 <= nums.length <= 105
	* 1 <= maxOperations, nums[i] <= 109"""

    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        lo, hi = 1, 1_000_000_000
        while lo < hi: 
            mid = lo + hi >> 1
            if sum((x-1)//mid for x in nums) <= maxOperations: hi = mid
            else: lo = mid + 1
        return lo


    """1761. Minimum Degree of a Connected Trio in a Graph (Hard)
	You are given an undirected graph. You are given an integer n which is the 
	number of nodes in the graph and an array edges, where each edges[i] = [ui, vi] 
	indicates that there is an undirected edge between ui and vi. A connected 
	trio is a set of three nodes where there is an edge between every pair of 
	them. The degree of a connected trio is the number of edges where one 
	endpoint is in the trio, and the other is not. Return the minimum degree of 
	a connected trio in the graph, or -1 if the graph has no connected trios.

	Example 1:
	Input: n = 6, edges = [[1,2],[1,3],[3,2],[4,1],[5,2],[3,6]]
	Output: 3
	Explanation: There is exactly one trio, which is [1,2,3]. The edges that 
	             form its degree are bolded in the figure above.

	Example 2:
	Input: n = 7, edges = [[1,3],[4,1],[4,3],[2,5],[5,6],[6,7],[7,5],[2,6]]
	Output: 0
	Explanation: There are exactly three trios:
	1) [1,4,3] with degree 0.
	2) [2,5,6] with degree 2.
	3) [5,6,7] with degree 2.

	Constraints:
	* 2 <= n <= 400
	* edges[i].length == 2
	* 1 <= edges.length <= n * (n-1) / 2
	* 1 <= ui, vi <= n
	* ui != vi
	* There are no repeated edges."""

    def minTrioDegree(self, n: int, edges: List[List[int]]) -> int:
        graph = [[False]*n for _ in range(n)]
        degree = [0]*n
        
        for u, v in edges: 
            graph[u-1][v-1] = graph[v-1][u-1] = True
            degree[u-1] += 1
            degree[v-1] += 1
        
        ans = inf
        for i in range(n): 
            for j in range(i+1, n):
                if graph[i][j]: 
                    for k in range(j+1, n):
                        if graph[j][k] and graph[k][i]: 
                            ans = min(ans, degree[i] + degree[j] + degree[k] - 6)
        return ans if ans < inf else -1


    """1762. Buildings With an Ocean View (Medium)
	There are n buildings in a line. You are given an integer array heights of 
	size n that represents the heights of the buildings in the line. The ocean 
	is to the right of the buildings. A building has an ocean view if the 
	building can see the ocean without obstructions. Formally, a building has 
	an ocean view if all the buildings to its right have a smaller height. 
	Return a list of indices (0-indexed) of buildings that have an ocean view, 
	sorted in increasing order.

	Example 1:
	Input: heights = [4,2,3,1]
	Output: [0,2,3]
	Explanation: Building 1 (0-indexed) does not have an ocean view because building 2 is taller.

	Example 2:
	Input: heights = [4,3,2,1]
	Output: [0,1,2,3]
	Explanation: All the buildings have an ocean view.

	Example 3:
	Input: heights = [1,3,2,4]
	Output: [3]
	Explanation: Only building 3 has an ocean view.

	Example 4:
	Input: heights = [2,2,2,2]
	Output: [3]
	Explanation: Buildings cannot see the ocean if there are buildings of the same height to its right.

	Constraints:
	* 1 <= heights.length <= 105
	* 1 <= heights[i] <= 109"""

    def findBuildings(self, heights: List[int]) -> List[int]:
        stack = []
        for i, x in enumerate(heights): 
            while stack and heights[stack[-1]] <= x: stack.pop()
            stack.append(i)
        return stack 


    """1763. Longest Nice Substring (Easy)
	A string s is nice if, for every letter of the alphabet that s contains, it 
	appears both in uppercase and lowercase. For example, "abABB" is nice 
	because 'A' and 'a' appear, and 'B' and 'b' appear. However, "abA" is not 
	because 'b' appears, but 'B' does not. Given a string s, return the longest 
	substring of s that is nice. If there are multiple, return the substring of 
	the earliest occurrence. If there are none, return an empty string.

	Example 1:
	Input: s = "YazaAay"
	Output: "aAa"
	Explanation: "aAa" is a nice string because 'A/a' is the only letter of the 
	             alphabet in s, and both 'A' and 'a' appear. "aAa" is the 
	             longest nice substring.

	Example 2:
	Input: s = "Bb"
	Output: "Bb"
	Explanation: "Bb" is a nice string because both 'B' and 'b' appear. The 
	             whole string is a substring.
	
	Example 3:
	Input: s = "c"
	Output: ""
	Explanation: There are no nice substrings.
	
	Example 4:
	Input: s = "dDzeE"
	Output: "dD"
	Explanation: Both "dD" and "eE" are the longest nice substrings. As there 
	             are multiple longest nice substrings, return "dD" since it 
	             occurs earlier.

	Constraints:
	* 1 <= s.length <= 100
	* s consists of uppercase and lowercase English letters."""

    def longestNiceSubstring(self, s: str) -> str:
        if not s: return "" # boundary condition 
        ss = set(s)
        for i, c in enumerate(s):
            if c.swapcase() not in ss: 
                s0 = self.longestNiceSubstring(s[:i])
                s1 = self.longestNiceSubstring(s[i+1:])
                return max(s0, s1, key=len)
        return s


    """1764. Form Array by Concatenating Subarrays of Another Array (Medium)
	You are given a 2D integer array groups of length n. You are also given an 
	integer array nums. You are asked if you can choose n disjoint subarrays 
	from the array nums such that the ith subarray is equal to groups[i] 
	(0-indexed), and if i > 0, the (i-1)th subarray appears before the ith 
	subarray in nums (i.e. the subarrays must be in the same order as groups). 
	Return true if you can do this task, and false otherwise. Note that the 
	subarrays are disjoint if and only if there is no index k such that nums[k] 
	belongs to more than one subarray. A subarray is a contiguous sequence of 
	elements within an array.

	Example 1:
	Input: groups = [[1,-1,-1],[3,-2,0]], nums = [1,-1,0,1,-1,-1,3,-2,0]
	Output: true
	Explanation: You can choose the 0th subarray as [1,-1,0,1,-1,-1,3,-2,0] and 
	             the 1st one as [1,-1,0,1,-1,-1,3,-2,0]. These subarrays are 
	             disjoint as they share no common nums[k] element.

	Example 2:
	Input: groups = [[10,-2],[1,2,3,4]], nums = [1,2,3,4,10,-2]
	Output: false
	Explanation: Note that choosing the subarrays [1,2,3,4,10,-2] and 
	             [1,2,3,4,10,-2] is incorrect because they are not in the same 
	             order as in groups. [10,-2] must come before [1,2,3,4].
	
	Example 3:
	Input: groups = [[1,2,3],[3,4]], nums = [7,7,1,2,3,4,7,7]
	Output: false
	Explanation: Note that choosing the subarrays [7,7,1,2,3,4,7,7] and 
	             [7,7,1,2,3,4,7,7] is invalid because they are not disjoint. 
	             They share a common elements nums[4] (0-indexed).

	Constraints:
	* groups.length == n
	* 1 <= n <= 10^3
	* 1 <= groups[i].length, sum(groups[i].length) <= 10^3
	* 1 <= nums.length <= 10^3
	* -10^7 <= groups[i][j], nums[k] <= 10^7"""

    def canChoose(self, groups: List[List[int]], nums: List[int]) -> bool:
        i = 0
        for grp in groups: 
            for ii in range(i, len(nums)):
                if nums[ii:ii+len(grp)] == grp: 
                    i = ii + len(grp)
                    break 
            else: return False
        return True


    """1765. Map of Highest Peak (Medium)
	You are given an integer matrix isWater of size m x n that represents a map 
	of land and water cells.
	* If isWater[i][j] == 0, cell (i, j) is a land cell.
	* If isWater[i][j] == 1, cell (i, j) is a water cell.
	You must assign each cell a height in a way that follows these rules:
	* The height of each cell must be non-negative.
	* If the cell is a water cell, its height must be 0.
	* Any two adjacent cells must have an absolute height difference of at most 
	  1. A cell is adjacent to another cell if the former is directly north, 
	  east, south, or west of the latter (i.e., their sides are touching).
	Find an assignment of heights such that the maximum height in the matrix is 
	maximized. Return an integer matrix height of size m x n where height[i][j] 
	is cell (i, j)'s height. If there are multiple solutions, return any of them.

	Example 1:
	Input: isWater = [[0,1],[0,0]]
	Output: [[1,0],[2,1]]
	Explanation: The image shows the assigned heights of each cell. The blue 
	             cell is the water cell, and the green cells are the land cells.

	Example 2:
	Input: isWater = [[0,0,1],[1,0,0],[0,0,0]]
	Output: [[1,1,0],[0,1,1],[1,2,2]]
	Explanation: A height of 2 is the maximum possible height of any assignment. 
	             Any height assignment that has a maximum height of 2 while 
	             still meeting the rules will also be accepted.

	Constraints:
	* m == isWater.length
	* n == isWater[i].length
	* 1 <= m, n <= 1000
	* isWater[i][j] is 0 or 1.
	* There is at least one water cell."""

    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        m, n = len(isWater), len(isWater[0]) # dimensions 
        
        ans = [[-1]*n for _ in range(m)]
        queue = deque()
        for i in range(m): 
            for j in range(n):
                if isWater[i][j]:
                    queue.append((i, j))
                    ans[i][j] = 0

        while queue: 
            i, j = queue.popleft()
            for ii, jj in (i-1, j), (i, j-1), (i, j+1), (i+1, j): 
                if 0 <= ii < m and 0 <= jj < n and ans[ii][jj] == -1: 
                    ans[ii][jj] = 1 + ans[i][j]
                    queue.append((ii, jj))
        return ans 


    """1766. Tree of Coprimes (Hard)
	There is a tree (i.e., a connected, undirected graph that has no cycles) 
	consisting of n nodes numbered from 0 to n - 1 and exactly n - 1 edges. 
	Each node has a value associated with it, and the root of the tree is node 
	0. To represent this tree, you are given an integer array nums and a 2D 
	array edges. Each nums[i] represents the ith node's value, and each 
	edges[j] = [uj, vj] represents an edge between nodes uj and vj in the tree. 
	Two values x and y are coprime if gcd(x, y) == 1 where gcd(x, y) is the 
	greatest common divisor of x and y. An ancestor of a node i is any other 
	node on the shortest path from node i to the root. A node is not considered 
	an ancestor of itself. Return an array ans of size n, where ans[i] is the 
	closest ancestor to node i such that nums[i] and nums[ans[i]] are coprime, 
	or -1 if there is no such ancestor.

	Example 1:
	Input: nums = [2,3,3,2], edges = [[0,1],[1,2],[1,3]]
	Output: [-1,0,0,1]
	Explanation: In the above figure, each node's value is in parentheses.
	- Node 0 has no coprime ancestors.
	- Node 1 has only one ancestor, node 0. Their values are coprime 
	  (gcd(2,3) == 1).
	- Node 2 has two ancestors, nodes 1 and 0. Node 1's value is not coprime 
	  (gcd(3,3) == 3), but node 0's value is (gcd(2,3) == 1), so node 0 is the 
	  closest valid ancestor.
	- Node 3 has two ancestors, nodes 1 and 0. It is coprime with node 1 
	  (gcd(3,2) == 1), so node 1 is its closest valid ancestor.

	Example 2:
	Input: nums = [5,6,10,2,3,6,15], edges = [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6]]
	Output: [-1,0,-1,0,0,0,-1]

	Constraints:
	* nums.length == n
	* 1 <= nums[i] <= 50
	* 1 <= n <= 10^5
	* edges.length == n - 1
	* edges[j].length == 2
	* 0 <= uj, vj < n
	* uj != vj"""

    def getCoprimes(self, nums: List[int], edges: List[List[int]]) -> List[int]:
        tree = {} # tree as adjacency list 
        for u, v in edges: 
            tree.setdefault(u, []).append(v)
            tree.setdefault(v, []).append(u)
        
        ans = [-1]*len(nums)
        path = {} # val -> list of position & depth 
        seen = {0}
        
        def fn(k, i): 
            """Populate ans via dfs."""
            ii = -1 
            for x in path:
                if gcd(nums[k], x) == 1: # coprime 
                    if path[x] and path[x][-1][1] > ii: 
                        ans[k] = path[x][-1][0]
                        ii = path[x][-1][1]
                        
            path.setdefault(nums[k], []).append((k, i))
            for kk in tree.get(k, []): 
                if kk not in seen: 
                    seen.add(kk)
                    fn(kk, i+1)
            path[nums[k]].pop()
            
        fn(0, 0)
        return ans 


    """1768. Merge Strings Alternately (Easy)
	You are given two strings word1 and word2. Merge the strings by adding 
	letters in alternating order, starting with word1. If a string is longer 
	than the other, append the additional letters onto the end of the merged 
	string. Return the merged string.

	Example 1:
	Input: word1 = "abc", word2 = "pqr"
	Output: "apbqcr"
	Explanation: The merged string will be merged as so:
	             word1:  a   b   c
	             word2:    p   q   r
	             merged: a p b q c r

	Example 2:
	Input: word1 = "ab", word2 = "pqrs"
	Output: "apbqrs"
	Explanation: Notice that as word2 is longer, "rs" is appended to the end.
	             word1:  a   b 
	             word2:    p   q   r   s
	             merged: a p b q   r   s

	Example 3:
	Input: word1 = "abcd", word2 = "pq"
	Output: "apbqcd"
	Explanation: Notice that as word1 is longer, "cd" is appended to the end.
	             word1:  a   b   c   d
	             word2:    p   q 
	             merged: a p b q c   d
	 
	Constraints:
	* 1 <= word1.length, word2.length <= 100
	* word1 and word2 consist of lowercase English letters."""

    def mergeAlternately(self, word1: str, word2: str) -> str:
        return "".join(x+y for x, y in zip_longest(word1, word2, fillvalue=""))


    """1769. Minimum Number of Operations to Move All Balls to Each Box (Medium)
	You have n boxes. You are given a binary string boxes of length n, where 
	boxes[i] is '0' if the ith box is empty, and '1' if it contains one ball. 
	In one operation, you can move one ball from a box to an adjacent box. Box 
	i is adjacent to box j if abs(i - j) == 1. Note that after doing so, there 
	may be more than one ball in some boxes. Return an array answer of size n, 
	where answer[i] is the minimum number of operations needed to move all the 
	balls to the ith box. Each answer[i] is calculated considering the initial 
	state of the boxes.

	Example 1:
	Input: boxes = "110"
	Output: [1,1,3]
	Explanation: The answer for each box is as follows:
	             1) First box: you will have to move one ball from the second box to the first box in one operation.
	             2) Second box: you will have to move one ball from the first box to the second box in one operation.
	             3) Third box: you will have to move one ball from the first box to the third box in two operations, and move one ball from the second box to the third box in one operation.
	
	Example 2:
	Input: boxes = "001011"
	Output: [11,8,5,4,3,4]

	Constraints:
	* n == boxes.length
	* 1 <= n <= 2000
	* boxes[i] is either '0' or '1'."""

    def minOperations(self, boxes: str) -> List[int]:
        ans = []
        ops = cnt = 0 # count of remaining "1"s
        for i, x in enumerate(boxes):
            if x == "1": 
                ops += i
                cnt += 1
        
        for i, x in enumerate(boxes): 
            ans.append(ops)
            if x == "1": cnt -= 2
            ops -= cnt
        return ans 


    """1770. Maximum Score from Performing Multiplication Operations (Medium)
	You are given two integer arrays nums and multipliers of size n and m 
	respectively, where n >= m. The arrays are 1-indexed. You begin with a 
	score of 0. You want to perform exactly m operations. On the ith operation 
	(1-indexed), you will:
	* Choose one integer x from either the start or the end of the array nums.
	* Add multipliers[i] * x to your score.
	* Remove x from the array nums.
	Return the maximum score after performing m operations.

	Example 1:
	Input: nums = [1,2,3], multipliers = [3,2,1]
	Output: 14
	Explanation: An optimal solution is as follows:
	- Choose from the end, [1,2,3], adding 3 * 3 = 9 to the score.
	- Choose from the end, [1,2], adding 2 * 2 = 4 to the score.
	- Choose from the end, [1], adding 1 * 1 = 1 to the score.
	The total score is 9 + 4 + 1 = 14.

	Example 2:
	Input: nums = [-5,-3,-3,-2,7,1], multipliers = [-10,-5,3,4,6]
	Output: 102
	Explanation: An optimal solution is as follows:
	- Choose from the start, [-5,-3,-3,-2,7,1], adding -5 * -10 = 50 to the score.
	- Choose from the start, [-3,-3,-2,7,1], adding -3 * -5 = 15 to the score.
	- Choose from the start, [-3,-2,7,1], adding -3 * 3 = -9 to the score.
	- Choose from the end, [-2,7,1], adding 1 * 4 = 4 to the score.
	- Choose from the end, [-2,7], adding 7 * 6 = 42 to the score. 
	The total score is 50 + 15 - 9 + 4 + 42 = 102.

	Constraints:
	* n == nums.length
	* m == multipliers.length
	* 1 <= m <= 103
	* m <= n <= 105
	* -1000 <= nums[i], multipliers[i] <= 1000"""

    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        n, m = len(nums), len(multipliers)
        dp = [[0]*m for _ in range(m+1)]
        
        for i in reversed(range(m)):
            for j in range(i, m): 
                k = i + m - j - 1
                dp[i][j] = max(nums[i] * multipliers[k] + dp[i+1][j], nums[j-m+n] * multipliers[k] + dp[i][j-1])
        
        return dp[0][-1]


    """1771. Maximize Palindrome Length From Subsequences (Hard)
	You are given two strings, word1 and word2. You want to construct a string 
	in the following manner:
	* Choose some non-empty subsequence subsequence1 from word1.
	* Choose some non-empty subsequence subsequence2 from word2.
	* Concatenate the subsequences: subsequence1 + subsequence2, to make the 
	  string.
	Return the length of the longest palindrome that can be constructed in the 
	described manner. If no palindromes can be constructed, return 0. A 
	subsequence of a string s is a string that can be made by deleting some 
	(possibly none) characters from s without changing the order of the 
	remaining characters. A palindrome is a string that reads the same forward 
	as well as backward.

	Example 1:
	Input: word1 = "cacb", word2 = "cbba"
	Output: 5
	Explanation: Choose "ab" from word1 and "cba" from word2 to make "abcba", 
	             which is a palindrome.

	Example 2:
	Input: word1 = "ab", word2 = "ab"
	Output: 3
	Explanation: Choose "ab" from word1 and "a" from word2 to make "aba", which 
	             is a palindrome.

	Example 3:
	Input: word1 = "aa", word2 = "bb"
	Output: 0
	Explanation: You cannot construct a palindrome from the described method, 
	             so return 0.

	Constraints:
	* 1 <= word1.length, word2.length <= 1000
	* word1 and word2 consist of lowercase English letters."""

    def longestPalindrome(self, word1: str, word2: str) -> int:
        
        @cache
        def fn(lo, hi):
            """Return length of longest palindromic subsequence."""
            if lo >= hi: return int(lo == hi)
            if word[lo] == word[hi]: return 2 + fn(lo+1, hi-1)
            return max(fn(lo+1, hi), fn(lo, hi-1))
        
        ans = 0
        word = word1 + word2
        for x in ascii_lowercase: 
            i = word1.find(x) 
            j = word2.rfind(x)
            if i != -1 and j != -1: ans = max(ans, fn(i, j+len(word1)))
        return ans 


    """1773. Count Items Matching a Rule (Easy)
	You are given an array items, where each items[i] = [typei, colori, namei] 
	describes the type, color, and name of the ith item. You are also given a 
	rule represented by two strings, ruleKey and ruleValue. The ith item is 
	said to match the rule if one of the following is true:
	* ruleKey == "type" and ruleValue == typei.
	* ruleKey == "color" and ruleValue == colori.
	* ruleKey == "name" and ruleValue == namei.
	Return the number of items that match the given rule.

	Example 1:
	Input: items = [["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]], ruleKey = "color", ruleValue = "silver"
	Output: 1
	Explanation: There is only one item matching the given rule, which is ["computer","silver","lenovo"].
	
	Example 2:
	Input: items = [["phone","blue","pixel"],["computer","silver","phone"],["phone","gold","iphone"]], ruleKey = "type", ruleValue = "phone"
	Output: 2
	Explanation: There are only two items matching the given rule, which are ["phone","blue","pixel"] and ["phone","gold","iphone"]. Note that the item ["computer","silver","phone"] does not match.

	Constraints:
	* 1 <= items.length <= 104
	* 1 <= typei.length, colori.length, namei.length, ruleValue.length <= 10
	* ruleKey is equal to either "type", "color", or "name".
	* All strings consist only of lowercase letters."""

    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        return sum(1 for t, c, n in items if (ruleKey, ruleValue) in (("type", t), ("color", c), ("name", n)))


    """1774. Closest Dessert Cost (Medium)
	You would like to make dessert and are preparing to buy the ingredients. 
	You have n ice cream base flavors and m types of toppings to choose from. 
	You must follow these rules when making your dessert:
	* There must be exactly one ice cream base.
	* You can add one or more types of topping or have no toppings at all.
	* There are at most two of each type of topping.
	You are given three inputs:
	* baseCosts, an integer array of length n, where each baseCosts[i] 
	  represents the price of the ith ice cream base flavor.
	* toppingCosts, an integer array of length m, where each toppingCosts[i] is 
	  the price of one of the ith topping.
	* target, an integer representing your target price for dessert.
	You want to make a dessert with a total cost as close to target as possible. 
	Return the closest possible cost of the dessert to target. If there are 
	multiple, return the lower one.

	Example 1:
	Input: baseCosts = [1,7], toppingCosts = [3,4], target = 10
	Output: 10
	Explanation: Consider the following combination (all 0-indexed):
	- Choose base 1: cost 7
	- Take 1 of topping 0: cost 1 x 3 = 3
	- Take 0 of topping 1: cost 0 x 4 = 0
	Total: 7 + 3 + 0 = 10.

	Example 2:
	Input: baseCosts = [2,3], toppingCosts = [4,5,100], target = 18
	Output: 17
	Explanation: Consider the following combination (all 0-indexed):
	- Choose base 1: cost 3
	- Take 1 of topping 0: cost 1 x 4 = 4
	- Take 2 of topping 1: cost 2 x 5 = 10
	- Take 0 of topping 2: cost 0 x 100 = 0
	Total: 3 + 4 + 10 + 0 = 17. You cannot make a dessert with a total cost of 18.

	Example 3:
	Input: baseCosts = [3,10], toppingCosts = [2,5], target = 9
	Output: 8
	Explanation: It is possible to make desserts with cost 8 and 10. Return 8 as it is the lower cost.

	Example 4:
	Input: baseCosts = [10], toppingCosts = [1], target = 1
	Output: 10
	Explanation: Notice that you don't have to have any toppings, but you must have exactly one base.

	Constraints:
	* n == baseCosts.length
	* m == toppingCosts.length
	* 1 <= n, m <= 10
	* 1 <= baseCosts[i], toppingCosts[i] <= 10^4
	* 1 <= target <= 10^4"""

    def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
        
        @cache
        def fn(i, cost):
            """Return sum of subsequence closest to target."""
            if cost >= target or i == len(toppingCosts): return cost
            return min(fn(i+1, cost), fn(i+1, cost+toppingCosts[i]), key=lambda x: (abs(x-target), x))
        
        ans = inf
        toppingCosts *= 2
        for cost in baseCosts: 
            ans = min(ans, fn(0, cost), key=lambda x: (abs(x-target), x))
        return ans 


    """1775. Equal Sum Arrays With Minimum Number of Operations (Medium)
	You are given two arrays of integers nums1 and nums2, possibly of different 
	lengths. The values in the arrays are between 1 and 6, inclusive. In one 
	operation, you can change any integer's value in any of the arrays to any 
	value between 1 and 6, inclusive. Return the minimum number of operations 
	required to make the sum of values in nums1 equal to the sum of values in 
	nums2. Return -1​​​​​ if it is not possible to make the sum of the two arrays 
	equal.

	Example 1:
	Input: nums1 = [1,2,3,4,5,6], nums2 = [1,1,2,2,2,2]
	Output: 3
	Explanation: You can make the sums of nums1 and nums2 equal with 3 
	operations. All indices are 0-indexed.
	- Change nums2[0] to 6. nums1 = [1,2,3,4,5,6], nums2 = [6,1,2,2,2,2].
	- Change nums1[5] to 1. nums1 = [1,2,3,4,5,1], nums2 = [6,1,2,2,2,2].
	- Change nums1[2] to 2. nums1 = [1,2,2,4,5,1], nums2 = [6,1,2,2,2,2].

	Example 2:
	Input: nums1 = [1,1,1,1,1,1,1], nums2 = [6]
	Output: -1
	Explanation: There is no way to decrease the sum of nums1 or to increase 
	the sum of nums2 to make them equal.

	Example 3:
	Input: nums1 = [6,6], nums2 = [1]
	Output: 3
	Explanation: You can make the sums of nums1 and nums2 equal with 3 
	operations. All indices are 0-indexed. 
	- Change nums1[0] to 2. nums1 = [2,6], nums2 = [1].
	- Change nums1[1] to 2. nums1 = [2,2], nums2 = [1].
	- Change nums2[0] to 4. nums1 = [2,2], nums2 = [4].

	Constraints:
	* 1 <= nums1.length, nums2.length <= 10^5
	* 1 <= nums1[i], nums2[i] <= 6"""

    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        if 6*len(nums1) < len(nums2) or 6*len(nums2) < len(nums1): return -1 # impossible 
        
        if sum(nums1) < sum(nums2): nums1, nums2 = nums2, nums1
        s1, s2 = sum(nums1), sum(nums2) # s1 >= s2
            
        nums1.sort()
        nums2.sort()
        
        ans = j = 0
        i = len(nums1)-1
        
        while s1 > s2: 
            if j >= len(nums2) or 0 <= i and nums1[i] - 1 > 6 - nums2[j]: 
                s1 += 1 - nums1[i]
                i -= 1
            else: 
                s2 += 6 - nums2[j]
                j += 1
            ans += 1
        return ans 


    """1776. Car Fleet II (Hard)
	There are n cars traveling at different speeds in the same direction along 
	a one-lane road. You are given an array cars of length n, where 
	cars[i] = [position_i, speed_i] represents:
	* positioni is the distance between the ith car and the beginning of the 
	  road in meters. It is guaranteed that position_i < position_{i+1}.
	* speedi is the initial speed of the ith car in meters per second.
	For simplicity, cars can be considered as points moving along the number 
	line. Two cars collide when they occupy the same position. Once a car 
	collides with another car, they unite and form a single car fleet. The cars 
	in the formed fleet will have the same position and the same speed, which 
	is the initial speed of the slowest car in the fleet. Return an array 
	answer, where answer[i] is the time, in seconds, at which the ith car 
	collides with the next car, or -1 if the car does not collide with the next 
	car. Answers within 10^-5 of the actual answers are accepted.

	Example 1:
	Input: cars = [[1,2],[2,1],[4,3],[7,2]]
	Output: [1.00000,-1.00000,3.00000,-1.00000]
	Explanation: After exactly one second, the first car will collide with the 
	             second car, and form a car fleet with speed 1 m/s. After 
	             exactly 3 seconds, the third car will collide with the fourth 
	             car, and form a car fleet with speed 2 m/s.

	Example 2:
	Input: cars = [[3,4],[5,4],[6,3],[9,1]]
	Output: [2.00000,1.00000,1.50000,-1.00000]

	Constraints:
	* 1 <= cars.length <= 10^5
	* 1 <= position_i, speedi <= 10^6
	* position_i < position_{i+1}"""

    def getCollisionTimes(self, cars: List[List[int]]) -> List[float]:
        ans = [-1]*len(cars)
        stack = []
        for i, (x, v) in enumerate(reversed(cars)): 
            while stack and (v <= stack[-1][1] or (stack[-1][0] - x)/(v - stack[-1][1]) >= stack[-1][2]): stack.pop()
            if stack: 
                t = (stack[-1][0] - x)/(v - stack[-1][1])
                stack.append((x, v, t))
                ans[~i] = t
            else: 
                stack.append((x, v, inf))
        return ans 


    """1779. Find Nearest Point That Has the Same X or Y Coordinate (Easy)
	You are given two integers, x and y, which represent your current location 
	on a Cartesian grid: (x, y). You are also given an array points where each 
	points[i] = [ai, bi] represents that a point exists at (ai, bi). A point is 
	valid if it shares the same x-coordinate or the same y-coordinate as your 
	location. Return the index (0-indexed) of the valid point with the smallest 
	Manhattan distance from your current location. If there are multiple, 
	return the valid point with the smallest index. If there are no valid 
	points, return -1. The Manhattan distance between two points (x1, y1) and 
	(x2, y2) is abs(x1 - x2) + abs(y1 - y2).

	Example 1:
	Input: x = 3, y = 4, points = [[1,2],[3,1],[2,4],[2,3],[4,4]]
	Output: 2
	Explanation: Of all the points, only [3,1], [2,4] and [4,4] are valid. Of 
	             the valid points, [2,4] and [4,4] have the smallest Manhattan 
	             distance from your current location, with a distance of 1. 
	             [2,4] has the smallest index, so return 2.

	Example 2:
	Input: x = 3, y = 4, points = [[3,4]]
	Output: 0
	Explanation: The answer is allowed to be on the same location as your 
	             current location.
	
	Example 3:
	Input: x = 3, y = 4, points = [[2,3]]
	Output: -1
	Explanation: There are no valid points.

	Constraints:
	* 1 <= points.length <= 10^4
	* points[i].length == 2
	* 1 <= x, y, ai, bi <= 10^4"""

    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        ans = -1
        dist = inf
        for i, (xx, yy) in enumerate(points): 
            if (x == xx or y == yy) and abs(x-xx) + abs(y-yy) < dist: 
                ans = i
                dist = abs(x-xx) + abs(y-yy)
        return ans


    """1780. Check if Number is a Sum of Powers of Three (Medium)
	Given an integer n, return true if it is possible to represent n as the sum 
	of distinct powers of three. Otherwise, return false. An integer y is a 
	power of three if there exists an integer x such that y == 3x.

	Example 1:
	Input: n = 12
	Output: true
	Explanation: 12 = 31 + 32

	Example 2:
	Input: n = 91
	Output: true
	Explanation: 91 = 30 + 32 + 34

	Example 3:
	Input: n = 21
	Output: false

	Constraints: 1 <= n <= 10^7"""

    def checkPowersOfThree(self, n: int) -> bool:
        while n: 
            n, r = divmod(n, 3)
            if r == 2: return False 
        return True 


    """1781. Sum of Beauty of All Substrings (Medium)
	The beauty of a string is the difference in frequencies between the most 
	frequent and least frequent characters. For example, the beauty of "abaacc" 
	is 3 - 1 = 2. Given a string s, return the sum of beauty of all of its 
	substrings.

	Example 1:
	Input: s = "aabcb"
	Output: 5
	Explanation: The substrings with non-zero beauty are 
	             ["aab","aabc","aabcb","abcb","bcb"], each with beauty equal to 1.

	Example 2:
	Input: s = "aabcbaa"
	Output: 17

	Constraints:
	* 1 <= s.length <= 500
	* s consists of only lowercase English letters."""

    def beautySum(self, s: str) -> int:
        ans = 0
        for i in range(len(s)):
            freq = [0]*26
            for ii in range(i, len(s)): 
                freq[ord(s[ii])-97] += 1
                ans += max(freq) - min(x for x in freq if x)
        return ans  


    """1782. Count Pairs Of Nodes (Hard)
	You are given an undirected graph represented by an integer n, which is the 
	number of nodes, and edges, where edges[i] = [ui, vi] which indicates that 
	there is an undirected edge between ui and vi. You are also given an integer 
	array queries. The answer to the jth query is the number of pairs of nodes 
	(a, b) that satisfy the following conditions:
	* a < b
	* cnt is strictly greater than queries[j], where cnt is the number of edges 
	  incident to a or b.
	Return an array answers such that answers.length == queries.length and 
	answers[j] is the answer of the jth query. Note that there can be repeated 
	edges.

	Example 1:
	Input: n = 4, edges = [[1,2],[2,4],[1,3],[2,3],[2,1]], queries = [2,3]
	Output: [6,5]
	Explanation: The number of edges incident to at least one of each pair is 
	             shown above.

	Example 2:
	Input: n = 5, edges = [[1,5],[1,5],[3,4],[2,5],[1,3],[5,1],[2,3],[2,5]], queries = [1,2,3,4,5]
	Output: [10,10,9,8,6]

	Constraints:
	* 2 <= n <= 2 * 10^4
	* 1 <= edges.length <= 10^5
	* 1 <= ui, vi <= n
	* ui != vi
	* 1 <= queries.length <= 20
	* 0 <= queries[j] < edges.length"""

    def countPairs(self, n: int, edges: List[List[int]], queries: List[int]) -> List[int]:
        degree = [0]*n
        freq = defaultdict(int)
        for u, v in edges: 
            degree[u-1] += 1
            degree[v-1] += 1
            freq[min(u-1, v-1), max(u-1, v-1)] += 1
        
        vals = sorted(degree)
        
        ans = []
        for query in queries: 
            cnt = 0 
            lo, hi = 0, n-1
            while lo < hi: 
                if query < vals[lo] + vals[hi]: 
                    cnt += hi - lo # (lo, hi), (lo+1, hi), ..., (hi-1, hi) all valid
                    hi -= 1
                else: lo += 1
            for u, v in freq: 
                if degree[u] + degree[v] - freq[u, v] <= query < degree[u] + degree[v]: cnt -= 1
            ans.append(cnt)
        return ans


    """1784. Check if Binary String Has at Most One Segment of Ones (Easy)
	Given a binary string s ​​​​​without leading zeros, return true​​​ if s contains 
	at most one contiguous segment of ones. Otherwise, return false.

	Example 1:
	Input: s = "1001"
	Output: false
	Explanation: The ones do not form a contiguous segment.

	Example 2:
	Input: s = "110"
	Output: true

	Constraints:
	* 1 <= s.length <= 100
	* s[i]​​​​ is either '0' or '1'.
	* s[0] is '1'."""

    def checkOnesSegment(self, s: str) -> bool:
        return "01" not in s


    """1785. Minimum Elements to Add to Form a Given Sum (Medium)
	You are given an integer array nums and two integers limit and goal. The 
	array nums has an interesting property that abs(nums[i]) <= limit. Return 
	the minimum number of elements you need to add to make the sum of the array 
	equal to goal. The array must maintain its property that 
	abs(nums[i]) <= limit. Note that abs(x) equals x if x >= 0, and -x 
	otherwise.

	Example 1:
	Input: nums = [1,-1,1], limit = 3, goal = -4
	Output: 2
	Explanation: You can add -2 and -3, then the sum of the array will be 
	             1 - 1 + 1 - 2 - 3 = -4.

	Example 2:
	Input: nums = [1,-10,9,1], limit = 100, goal = 0
	Output: 1

	Constraints:
	* 1 <= nums.length <= 10^5
	* 1 <= limit <= 10^6
	* -limit <= nums[i] <= limit
	* -10^9 <= goal <= 10^9"""

    def minElements(self, nums: List[int], limit: int, goal: int) -> int:
        return ceil(abs(goal - sum(nums))/limit)


    """1786. Number of Restricted Paths From First to Last Node (Medium)
	There is an undirected weighted connected graph. You are given a positive 
	integer n which denotes that the graph has n nodes labeled from 1 to n, and 
	an array edges where each edges[i] = [ui, vi, weighti] denotes that there 
	is an edge between nodes ui and vi with weight equal to weighti. A path 
	from node start to node end is a sequence of nodes [z0, z1, z2, ..., zk] 
	such that z0 = start and zk = end and there is an edge between zi and zi+1 
	where 0 <= i <= k-1. The distance of a path is the sum of the weights on 
	the edges of the path. Let distanceToLastNode(x) denote the shortest 
	distance of a path between node n and node x. A restricted path is a path 
	that also satisfies that distanceToLastNode(zi) > distanceToLastNode(zi+1) 
	where 0 <= i <= k-1. Return the number of restricted paths from node 1 to 
	node n. Since that number may be too large, return it modulo 109 + 7.

	Example 1:
	Input: n = 5, edges = [[1,2,3],[1,3,3],[2,3,1],[1,4,2],[5,2,2],[3,5,1],[5,4,10]]
	Output: 3
	Explanation: Each circle contains the node number in black and its 
	             distanceToLastNode value in blue. The three restricted paths 
	             are:
 				 1) 1 --> 2 --> 5
 				 2) 1 --> 2 --> 3 --> 5
				 3) 1 --> 3 --> 5

	Example 2:
	Input: n = 7, edges = [[1,3,1],[4,1,2],[7,3,4],[2,5,3],[5,6,1],[6,7,2],[7,5,3],[2,6,4]]
	Output: 1
	Explanation: Each circle contains the node number in black and its 
	             distanceToLastNode value in blue. The only restricted path is 
	             1 --> 3 --> 7.

	Constraints:
	* 1 <= n <= 2 * 10^4
	* n - 1 <= edges.length <= 4 * 10^4
	* edges[i].length == 3
	* 1 <= ui, vi <= n
	* ui != vi
	* 1 <= weighti <= 10^5
	* There is at most one edge between any two nodes.
	* There is at least one path between any two nodes."""

    def countRestrictedPaths(self, n: int, edges: List[List[int]]) -> int:
        graph = {} # graph as adjacency list 
        for u, v, w in edges: 
            graph.setdefault(u-1, []).append((v-1, w))
            graph.setdefault(v-1, []).append((u-1, w))
        
        # dijkstra's algo
        pq = [(0, n-1)]
        dist = [inf]*(n-1) + [0]
        while pq: 
            d, u = heappop(pq)
            for v, w in graph[u]: 
                if dist[u] + w < dist[v]: 
                    dist[v] = dist[u] + w
                    heappush(pq, (dist[v], v))
        
        @cache
        def fn(u): 
            """Return number of restricted paths from u to n."""
            if u == n-1: return 1 # boundary condition 
            ans = 0
            for v, _ in graph[u]: 
                if dist[u] > dist[v]: ans += fn(v)
            return ans 
        
        return fn(0) % 1_000_000_007


    """1787. Make the XOR of All Segments Equal to Zero (Hard)
	You are given an array nums​​​ and an integer k​​​​​. The XOR of a segment [left, right] 
	where left <= right is the XOR of all the elements with indices between 
	left and right, inclusive: nums[left] XOR nums[left+1] XOR ... XOR nums[right]. 
	Return the minimum number of elements to change in the array such that the 
	XOR of all segments of size k​​​​​​ is equal to zero.

	Example 1:
	Input: nums = [1,2,0,3,0], k = 1
	Output: 3
	Explanation: Modify the array from [1,2,0,3,0] to from [0,0,0,0,0].

	Example 2:
	Input: nums = [3,4,5,2,1,7,3,4,7], k = 3
	Output: 3
	Explanation: Modify the array from [3,4,5,2,1,7,3,4,7] to [3,4,7,3,4,7,3,4,7].

	Example 3:
	Input: nums = [1,2,4,1,2,5,1,2,6], k = 3
	Output: 3
	Explanation: Modify the array from [1,2,4,1,2,5,1,2,6] to [1,2,3,1,2,3,1,2,3].

	Constraints:
	* 1 <= k <= nums.length <= 2000
	* ​​​​​​0 <= nums[i] < 2^10"""

    def minChanges(self, nums: List[int], k: int) -> int:
        freq = defaultdict(lambda: defaultdict(int))
        for i, x in enumerate(nums): freq[i%k][x] += 1 # freq by row
        
        n = 1 << 10
        dp = [0] + [-inf]*(n-1)
        for i in range(k): 
            mx = max(dp)
            tmp = [0]*n
            for x, c in enumerate(dp): 
                for xx, cc in freq[i].items(): 
                    tmp[x^xx] = max(tmp[x^xx], c + cc, mx)
            dp = tmp 
        return len(nums) - dp[0]


    """1790. Check if One String Swap Can Make Strings Equal (Easy)
	You are given two strings s1 and s2 of equal length. A string swap is an 
	operation where you choose two indices in a string (not necessarily 
	different) and swap the characters at these indices. Return true if it is 
	possible to make both strings equal by performing at most one string swap 
	on exactly one of the strings. Otherwise, return false.

	Example 1:
	Input: s1 = "bank", s2 = "kanb"
	Output: true
	Explanation: For example, swap the first character with the last character 
	             of s2 to make "bank".

	Example 2:
	Input: s1 = "attack", s2 = "defend"
	Output: false
	Explanation: It is impossible to make them equal with one string swap.

	Example 3:
	Input: s1 = "kelb", s2 = "kelb"
	Output: true
	Explanation: The two strings are already equal, so no string swap operation 
	             is required.

	Example 4:
	Input: s1 = "abcd", s2 = "dcba"
	Output: false

	Constraints:
	* 1 <= s1.length, s2.length <= 100
	* s1.length == s2.length
	* s1 and s2 consist of only lowercase English letters."""

    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        diff = [[x, y] for x, y in zip(s1, s2) if x != y]
        return not diff or len(diff) == 2 and diff[0][::-1] == diff[1]

    
    """1791. Find Center of Star Graph (Medium)
	There is an undirected star graph consisting of n nodes labeled from 1 to n. 
	A star graph is a graph where there is one center node and exactly n - 1 
	edges that connect the center node with every other node. You are given a 
	2D integer array edges where each edges[i] = [ui, vi] indicates that there 
	is an edge between the nodes ui and vi. Return the center of the given star 
	graph.

	Example 1:
	Input: edges = [[1,2],[2,3],[4,2]]
	Output: 2
	Explanation: As shown in the figure above, node 2 is connected to every 
	             other node, so 2 is the center.

	Example 2:
	Input: edges = [[1,2],[5,1],[1,3],[1,4]]
	Output: 1

	Constraints:
	* 3 <= n <= 10^5
	* edges.length == n - 1
	* edges[i].length == 2
	* 1 <= ui, vi <= n
	* ui != vi
	* The given edges represent a valid star graph."""

    def findCenter(self, edges: List[List[int]]) -> int:
        if edges[0][0] in edges[1]: return edges[0][0]
        else: return edges[0][1]


    """1792. Maximum Average Pass Ratio (Medium)
	There is a school that has classes of students and each class will be 
	having a final exam. You are given a 2D integer array classes, where 
	classes[i] = [passi, totali]. You know beforehand that in the ith class, 
	there are totali total students, but only passi number of students will 
	pass the exam. You are also given an integer extraStudents. There are 
	another extraStudents brilliant students that are guaranteed to pass the 
	exam of any class they are assigned to. You want to assign each of the 
	extraStudents students to a class in a way that maximizes the average pass 
	ratio across all the classes. The pass ratio of a class is equal to the 
	number of students of the class that will pass the exam divided by the 
	total number of students of the class. The average pass ratio is the sum of 
	pass ratios of all the classes divided by the number of the classes. Return 
	the maximum possible average pass ratio after assigning the extraStudents 
	students. Answers within 10-5 of the actual answer will be accepted.

	Example 1:
	Input: classes = [[1,2],[3,5],[2,2]], extraStudents = 2
	Output: 0.78333
	Explanation: You can assign the two extra students to the first class. The 
	             average pass ratio will be equal to 
	             (3/4 + 3/5 + 2/2) / 3 = 0.78333.

	Example 2:
	Input: classes = [[2,4],[3,9],[4,5],[2,10]], extraStudents = 4
	Output: 0.53485

	Constraints:
	* 1 <= classes.length <= 10^5
	* classes[i].length == 2
	* 1 <= passi <= totali <= 10^5
	* 1 <= extraStudents <= 10^5"""

    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        pq = [(p/t - (p+1)/(t+1), p, t) for p, t in classes] # max-heap 
        heapify(pq)
        
        for _ in range(extraStudents):  
            _, p, t = heappop(pq)
            heappush(pq, ((p+1)/(t+1) - (p+2)/(t+2), p+1, t+1))
        
        return sum(p/t for _, p, t in pq)/len(pq)


    """1793. Maximum Score of a Good Subarray (Hard)
	You are given an array of integers nums (0-indexed) and an integer k. The 
	score of a subarray (i, j) is defined as 
	min(nums[i], nums[i+1], ..., nums[j]) * (j - i + 1). 
	A good subarray is a subarray where i <= k <= j. Return the maximum 
	possible score of a good subarray.

	Example 1:
	Input: nums = [1,4,3,7,4,5], k = 3
	Output: 15
	Explanation: The optimal subarray is (1, 5) with a score of 
	             min(4,3,7,4,5) * (5-1+1) = 3 * 5 = 15. 

	Example 2:
	Input: nums = [5,5,4,5,4,1,1,1], k = 0
	Output: 20
	Explanation: The optimal subarray is (0, 4) with a score of 
	             min(5,5,4,5,4) * (4-0+1) = 4 * 5 = 20.

	Constraints:
	* 1 <= nums.length <= 10^5
	* 1 <= nums[i] <= 2 * 10^4
	* 0 <= k < nums.length"""

    def maximumScore(self, nums: List[int], k: int) -> int:
        ans = mn0 = mn1 = nums[k]
        lo = hi = k
        while 0 <= lo-1 or hi+1 < len(nums): 
            if lo == 0 or hi+1 < len(nums) and nums[lo-1] < nums[hi+1]: hi += 1
            else: lo -= 1
            mn0 = min(mn0, nums[lo])
            mn1 = min(mn1, nums[hi])
            ans = max(ans, min(mn0, mn1)*(hi-lo+1))
        return ans 


    """1796. Second Largest Digit in a String (Easy)
	Given an alphanumeric string s, return the second largest numerical digit 
	that appears in s, or -1 if it does not exist. An alphanumeric string is a 
	string consisting of lowercase English letters and digits.

	Example 1:
	Input: s = "dfa12321afd"
	Output: 2
	Explanation: The digits that appear in s are [1, 2, 3]. The second largest 
	             digit is 2.

	Example 2:
	Input: s = "abc1111"
	Output: -1
	Explanation: The digits that appear in s are [1]. There is no second 
	             largest digit. 

	Constraints:
	* 1 <= s.length <= 500
	* s consists of only lowercase English letters and/or digits."""

    def secondHighest(self, s: str) -> int:
        seen = set()
        for c in s: 
            if c.isdigit(): 
                seen.add(int(c))
        return -1 if len(seen) < 2 else sorted(seen)[-2]


    """1798. Maximum Number of Consecutive Values You Can Make (Medium)
	You are given an integer array coins of length n which represents the n 
	coins that you own. The value of the ith coin is coins[i]. You can make 
	some value x if you can choose some of your n coins such that their values 
	sum up to x. Return the maximum number of consecutive integer values that 
	you can make with your coins starting from and including 0. Note that you 
	may have multiple coins of the same value.

	Example 1:
	Input: coins = [1,3]
	Output: 2
	Explanation: You can make the following values:
	- 0: take []
	- 1: take [1]
	You can make 2 consecutive integer values starting from 0.

	Example 2:
	Input: coins = [1,1,1,4]
	Output: 8
	Explanation: You can make the following values:
	- 0: take []
	- 1: take [1]
	- 2: take [1,1]
	- 3: take [1,1,1]
	- 4: take [4]
	- 5: take [4,1]
	- 6: take [4,1,1]
	- 7: take [4,1,1,1]
	You can make 8 consecutive integer values starting from 0.

	Example 3:
	Input: nums = [1,4,10,3,1]
	Output: 20

	Constraints:
	* coins.length == n
	* 1 <= n <= 4 * 10^4
	* 1 <= coins[i] <= 4 * 10^4"""

    def getMaximumConsecutive(self, coins: List[int]) -> int:
        ans = 1
        for x in sorted(coins): 
            if ans < x: break 
            ans += x
        return ans


    """1799. Maximize Score After N Operations (Hard)
	You are given nums, an array of positive integers of size 2 * n. You must 
	perform n operations on this array. In the ith operation (1-indexed), you 
	will:
	* Choose two elements, x and y.
	* Receive a score of i * gcd(x, y).
	* Remove x and y from nums.
	Return the maximum score you can receive after performing n operations. The 
	function gcd(x, y) is the greatest common divisor of x and y.

	Example 1:
	Input: nums = [1,2]
	Output: 1
	Explanation: The optimal choice of operations is: (1 * gcd(1, 2)) = 1

	Example 2:
	Input: nums = [3,4,6,8]
	Output: 11
	Explanation: The optimal choice of operations is: 
	             (1 * gcd(3, 6)) + (2 * gcd(4, 8)) = 3 + 8 = 11
	
	Example 3:
	Input: nums = [1,2,3,4,5,6]
	Output: 14
	Explanation: The optimal choice of operations is:
     	         (1 * gcd(1, 5)) + (2 * gcd(2, 4)) + (3 * gcd(3, 6)) = 1 + 4 + 9 = 14

	Constraints:
	* 1 <= n <= 7
	* nums.length == 2 * n
	* 1 <= nums[i] <= 10^6"""

    def maxScore(self, nums: List[int]) -> int:
        n = len(nums)
        
        @cache
        def fn(mask, k): 
            """Return maximum score at kth operation with available numbers by mask."""
            if mask == 0: return 0 # no more numbers 
            ans = 0
            for i in range(n): 
                if mask & 1 << i:
                    for j in range(i+1, n): 
                        if mask & 1 << j: 
                            mask0 = mask & ~(1<<i) & ~(1<<j) # unset ith & jth bit
                            ans = max(ans, k*gcd(nums[i], nums[j]) + fn(mask0, k+1))
            return ans 
        
        return fn((1<<n) - 1, 1)


    """1800. Maximum Ascending Subarray Sum (Easy)
	Given an array of positive integers nums, return the maximum possible sum 
	of an ascending subarray in nums. A subarray is defined as a contiguous 
	sequence of numbers in an array. A subarray [numsl, numsl+1, ..., numsr-1, 
	numsr] is ascending if for all i where l <= i < r, numsi < numsi+1. Note 
	that a subarray of size 1 is ascending.

	Example 1:
	Input: nums = [10,20,30,5,10,50]
	Output: 65
	Explanation: [5,10,50] is the ascending subarray with the maximum sum of 65.

	Example 2:
	Input: nums = [10,20,30,40,50]
	Output: 150
	Explanation: [10,20,30,40,50] is the ascending subarray with the maximum sum of 150.

	Example 3:
	Input: nums = [12,17,15,13,10,11,12]
	Output: 33
	Explanation: [10,11,12] is the ascending subarray with the maximum sum of 33.

	Example 4:
	Input: nums = [100,10,1]
	Output: 100

	Constraints:
	* 1 <= nums.length <= 100
	* 1 <= nums[i] <= 100"""

    def maxAscendingSum(self, nums: List[int]) -> int:
        ans = val = 0
        for i, x in enumerate(nums): 
            if not i or nums[i-1] >= nums[i]: val = 0 # reset val 
            val += nums[i]
            ans = max(ans, val)
        return ans 


    """1801. Number of Orders in the Backlog (Medium)
	You are given a 2D integer array orders, where each 
	orders[i] = [pricei, amounti, orderTypei] denotes that amounti orders have 
	been placed of type orderTypei at the price pricei. The orderTypei is:
	* 0 if it is a batch of buy orders, or
	* 1 if it is a batch of sell orders.
	Note that orders[i] represents a batch of amounti independent orders with 
	the same price and order type. All orders represented by orders[i] will be 
	placed before all orders represented by orders[i+1] for all valid i. There 
	is a backlog that consists of orders that have not been executed. The 
	backlog is initially empty. When an order is placed, the following happens:
	* If the order is a buy order, you look at the sell order with the smallest 
	  price in the backlog. If that sell order's price is smaller than or equal 
	  to the current buy order's price, they will match and be executed, and 
	  that sell order will be removed from the backlog. Else, the buy order is 
	  added to the backlog.
	* Vice versa, if the order is a sell order, you look at the buy order with 
	  the largest price in the backlog. If that buy order's price is larger 
	  than or equal to the current sell order's price, they will match and be 
	  executed, and that buy order will be removed from the backlog. Else, the 
	  sell order is added to the backlog.
	Return the total amount of orders in the backlog after placing all the 
	orders from the input. Since this number can be large, return it modulo 
	10^9 + 7.

	Example 1:
	Input: orders = [[10,5,0],[15,2,1],[25,1,1],[30,4,0]]
	Output: 6
	Explanation: Here is what happens with the orders:
	- 5 orders of type buy with price 10 are placed. There are no sell orders, so the 5 orders are added to the backlog.
	- 2 orders of type sell with price 15 are placed. There are no buy orders with prices larger than or equal to 15, so the 2 orders are added to the backlog.
	- 1 order of type sell with price 25 is placed. There are no buy orders with prices larger than or equal to 25 in the backlog, so this order is added to the backlog.
	- 4 orders of type buy with price 30 are placed. The first 2 orders are matched with the 2 sell orders of the least price, which is 15 and these 2 sell orders are removed from the backlog. The 3rd order is matched with the sell order of the least price, which is 25 and this sell order is removed from the backlog. Then, there are no more sell orders in the backlog, so the 4th order is added to the backlog.
	Finally, the backlog has 5 buy orders with price 10, and 1 buy order with price 30. So the total number of orders in the backlog is 6.

	Example 2:
	Input: orders = [[7,1000000000,1],[15,3,0],[5,999999995,0],[5,1,1]]
	Output: 999999984
	Explanation: Here is what happens with the orders:
	- 109 orders of type sell with price 7 are placed. There are no buy orders, so the 109 orders are added to the backlog.
	- 3 orders of type buy with price 15 are placed. They are matched with the 3 sell orders with the least price which is 7, and those 3 sell orders are removed from the backlog.
	- 999999995 orders of type buy with price 5 are placed. The least price of a sell order is 7, so the 999999995 orders are added to the backlog.
	- 1 order of type sell with price 5 is placed. It is matched with the buy order of the highest price, which is 5, and that buy order is removed from the backlog.
	Finally, the backlog has (1000000000-3) sell orders with price 7, and (999999995-1) buy orders with price 5. So the total number of orders = 1999999991, which is equal to 999999984 % (109 + 7).

	Constraints:
	* 1 <= orders.length <= 10^5
	* orders[i].length == 3
	* 1 <= pricei, amounti <= 10^9
	* orderTypei is either 0 or 1."""

    def getNumberOfBacklogOrders(self, orders: List[List[int]]) -> int:
        buy, sell = [], [] # max-heap & min-heap 
        for p, q, t in orders: 
            if t: heappush(sell, [p, q])
            else: heappush(buy, [-p, q])
            
            while buy and sell and -buy[0][0] >= sell[0][0]: 
                qty = min(buy[0][1], sell[0][1])
                buy[0][1] -= qty
                sell[0][1] -= qty
                if not buy[0][1]: heappop(buy)
                if not sell[0][1]: heappop(sell)
        return (sum(q for _, q in sell) + sum(q for _, q in buy)) % 1_000_000_007


    """1802. Maximum Value at a Given Index in a Bounded Array (Medium)
	You are given three positive integers n, index and maxSum. You want to 
	construct an array nums (0-indexed) that satisfies the following conditions:
	* nums.length == n
	* nums[i] is a positive integer where 0 <= i < n.
	* abs(nums[i] - nums[i+1]) <= 1 where 0 <= i < n-1.
	* The sum of all the elements of nums does not exceed maxSum.
	* nums[index] is maximized.
	Return nums[index] of the constructed array. ote that abs(x) equals x if 
	x >= 0, and -x otherwise.

	Example 1:
	Input: n = 4, index = 2,  maxSum = 6
	Output: 2
	Explanation: The arrays [1,1,2,1] and [1,2,2,1] satisfy all the conditions. 
	             There are no other valid arrays with a larger value at the 
	             given index.

	Example 2:
	Input: n = 6, index = 1,  maxSum = 10
	Output: 3

	Constraints:
	* 1 <= n <= maxSum <= 10^9
	* 0 <= index < n"""

    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        
        def fn(n, x): 
            if n < x: return n*(2*x-n+1)//2
            return x*(1+x)//2 + n - x
        
        lo, hi = 0, 10**9
        while lo < hi: 
            mid = lo + hi + 1 >> 1
            sm = fn(index, mid-1) + fn(n-index, mid)
            if sm <= maxSum: lo = mid 
            else: hi = mid - 1
        return lo 


    """1803. Count Pairs With XOR in a Range (Hard)
	Given a (0-indexed) integer array nums and two integers low and high, 
	return the number of nice pairs. A nice pair is a pair (i, j) where 
	0 <= i < j < nums.length and low <= (nums[i] XOR nums[j]) <= high.

	Example 1:
	Input: nums = [1,4,2,7], low = 2, high = 6
	Output: 6
	Explanation: All nice pairs (i, j) are as follows:
	    - (0, 1): nums[0] XOR nums[1] = 5 
	    - (0, 2): nums[0] XOR nums[2] = 3
	    - (0, 3): nums[0] XOR nums[3] = 6
	    - (1, 2): nums[1] XOR nums[2] = 6
	    - (1, 3): nums[1] XOR nums[3] = 3
	    - (2, 3): nums[2] XOR nums[3] = 5

	Example 2:
	Input: nums = [9,8,4,2,1], low = 5, high = 14
	Output: 8
	Explanation: All nice pairs (i, j) are as follows:
	​​​​​    - (0, 2): nums[0] XOR nums[2] = 13
	    - (0, 3): nums[0] XOR nums[3] = 11
	    - (0, 4): nums[0] XOR nums[4] = 8
	    - (1, 2): nums[1] XOR nums[2] = 12
	    - (1, 3): nums[1] XOR nums[3] = 10
	    - (1, 4): nums[1] XOR nums[4] = 9
	    - (2, 3): nums[2] XOR nums[3] = 6
	    - (2, 4): nums[2] XOR nums[4] = 5

	Constraints:
	* 1 <= nums.length <= 2 * 10^4
	* 1 <= nums[i] <= 2 * 10^4
	* 1 <= low <= high <= 2 * 10^4

	class Trie: 
	    def __init__(self): 
	        self.root = {}
	        
	    def insert(self, val): 
	        node = self.root 
	        for i in reversed(range(15)):
	            bit = (val >> i) & 1
	            if bit not in node: 
	                node[bit] = {"cnt": 1}
	            else: 
	                node[bit]["cnt"] += 1
	            node = node[bit]
	        
	    def count(self, val, high): 
	        ans = 0 
	        node = self.root
	        for i in reversed(range(15)):
	            if not node: break 
	            bit = (val >> i) & 1 
	            cmp = (high >> i) & 1
	            if cmp: 
	                if node.get(bit, {}): 
	                    ans += node[bit]["cnt"]
	                node = node.get(1^bit, {})
	            else: 
	                node = node.get(bit, {})
	        return ans"""

    def countPairs(self, nums: List[int], low: int, high: int) -> int:
        trie = Trie()
        
        ans = 0
        for x in nums: 
            ans += trie.count(x, high+1) - trie.count(x, low)
            trie.insert(x)
        return ans 


"""146. LRU Cache (Medium)
Design and implement a data structure for Least Recently Used (LRU) cache. It 
should support the following operations: get and put. 
get(key)        - Get the value (will always be positive) of the key if the key 
                  exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. 

When the cache reached its capacity, it should invalidate the least recently 
used item before inserting a new item. The cache is initialized with a positive 
capacity.

Follow up: Could you do both operations in O(1) time complexity?

Example:
LRUCache cache = new LRUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4"""

class ListNode:
    def __init__(self, key=0, val=0, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next
        

class LRUCache:

    def __init__(self, capacity: int):
        """Initialize hash table & dll"""
        self.cpty = capacity
        self.htab = dict() #hash table 
        self.head = ListNode() #doubly linked list
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head 
        
    def _del(self, key: int) -> int: 
        """Delete given key from hash table & dll"""
        node = self.htab.pop(key)
        node.prev.next = node.next
        node.next.prev = node.prev
        return node.val

    def _ins(self, key: int, value: int) -> None: 
        """Insert at tail"""
        node = ListNode(key, value, self.tail.prev, self.tail)
        self.tail.prev.next = self.tail.prev = node
        self.htab[key] = node
        
    def get(self, key: int) -> int:
        if key not in self.htab: return -1
        value = self._del(key)
        self._ins(key, value)
        return value

    def put(self, key: int, value: int) -> None:
        if key in self.htab: self._del(key)
        self._ins(key, value)
        if len(self.htab) > self.cpty: 
            self._del(self.head.next.key)


"""155. Min Stack (Easy)
Design a stack that supports push, pop, top, and retrieving the minimum element 
in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
 
Example 1:
Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2

Constraints:
Methods pop, top and getMin operations will always be called on non-empty stacks."""

class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        if not self.stack: mn = x
        else: mn = min(x, self.stack[-1][1])
        self.stack.append((x, mn))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]


"""170. Two Sum III - Data structure design (Easy)
Design a data structure that accepts a stream of integers and checks if it has 
a pair of integers that sum up to a particular value.

Implement the TwoSum class:
* TwoSum() Initializes the TwoSum object, with an empty array initially.
* void add(int number) Adds number to the data structure.
* boolean find(int value) Returns true if there exists any pair of numbers whose sum is equal to value, otherwise, it returns false.

Example 1:
Input: ["TwoSum", "add", "add", "add", "find", "find"]
       [[], [1], [3], [5], [4], [7]]
Output: [null, null, null, null, true, false]
Explanation: 
TwoSum twoSum = new TwoSum();
twoSum.add(1);   // [] --> [1]
twoSum.add(3);   // [1] --> [1,3]
twoSum.add(5);   // [1,3] --> [1,3,5]
twoSum.find(4);  // 1 + 3 = 4, return true
twoSum.find(7);  // No two integers sum up to 7, return false

Constraints:
* -105 <= number <= 105
* -231 <= value <= 231 - 1
* At most 5 * 104 calls will be made to add and find."""

class TwoSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.freq = {}

    def add(self, number: int) -> None:
        """
        Add the number to an internal data structure..
        """
        self.freq[number] = 1 + self.freq.get(number, 0)

    def find(self, value: int) -> bool:
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        """
        for x in self.freq: 
            if value - x != x and value - x in self.freq: return True 
            elif value - x == x and self.freq[x] > 1: return True 
        return False 


"""173. Binary Search Tree Iterator (Medium)
Implement an iterator over a binary search tree (BST). Your iterator will be 
initialized with the root node of a BST. Calling next() will return the next 
smallest number in the BST.

Example:

BSTIterator iterator = new BSTIterator(root);
iterator.next();    // return 3
iterator.next();    // return 7
iterator.hasNext(); // return true
iterator.next();    // return 9
iterator.hasNext(); // return true
iterator.next();    // return 15
iterator.hasNext(); // return true
iterator.next();    // return 20
iterator.hasNext(); // return false
 
Note:
next() and hasNext() should run in average O(1) time and uses O(h) memory, 
where h is the height of the tree. You may assume that next() call will always 
be valid, that is, there will be at least a next smallest number in the BST 
when next() is called."""

class BSTIterator:

    def __init__(self, root: TreeNode):
        self.stack = []
        self._sink(root)
    
    def _sink(self, node: TreeNode) -> None:
        """Sink along the tree and collect nodes to stack"""
        while node:
            self.stack.append(node)
            node = node.left

    def next(self) -> int:
        """
        @return the next smallest number
        """
        node = self.stack.pop()
        ans = node.val 
        self._sink(node.right)
        return ans 

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return self.stack


"""208. Implement Trie (Prefix Tree) (Medium)
Implement a trie with insert, search, and startsWith methods.

Example:
Trie trie = new Trie();
trie.insert("apple");
trie.search("apple");   // returns true
trie.search("app");     // returns false
trie.startsWith("app"); // returns true
trie.insert("app");   
trie.search("app");     // returns true

Note:
You may assume that all inputs are consist of lowercase letters a-z.
All inputs are guaranteed to be non-empty strings."""

class TrieNode:
    """Node on trie"""
    def __init__(self):
        self.data = [None]*26 #lowercase letter only
        self.word = False     #true if a word terminates here 
        

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self.root
        for i in (ord(x) - 97 for x in word): 
            if not node.data[i]: node.data[i] = TrieNode()
            node = node.data[i]
        node.word = True
        
    def _traverse(self, word): 
        """traverse the trie to find word"""
        node = self.root
        for i in (ord(x)-97 for x in word):
            if not node.data[i]: return None
            node = node.data[i]
        return node
        
    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self._traverse(word)
        return node.word if node else False 
        
    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        return self._traverse(prefix)


"""211. Add and Search Word - Data structure design (Medium)
Design a data structure that supports the following two operations:
void addWord(word)
bool search(word)

search(word) can search a literal word or a regular expression string 
containing only letters a-z or .. A . means it can represent any one letter.

Example:
addWord("bad")
addWord("dad")
addWord("mad")
search("pad") -> false
search("bad") -> true
search(".ad") -> true
search("b..") -> true

Note: You may assume that all words are consist of lowercase letters a-z."""

class WordDictionary:

    def __init__(self):
        self.root = {}

    def addWord(self, word: str) -> None:
        node = self.root
        for letter in word:
            node = node.setdefault(letter, {})
        node["#"] = True #sentinel 

    def search(self, word: str) -> bool:
        
        def fn(node, i): 
            """Return True if word[i:] is found at trie rooted at n"""
            if not node: return False 
            if i == len(word): return node.get("#", False)
            if word[i] == ".": 
                return any(fn(node[k], i+1) for k in node if k != "#")
            else: 
                return fn(node.get(word[i]), i+1)
        
        return fn(self.root, 0)


"""225. Implement Stack using Queues (Easy)
Implement the following operations of a stack using queues.

push(x) -- Push element x onto stack.
pop()   -- Removes the element on top of the stack.
top()   -- Get the top element.
empty() -- Return whether the stack is empty.

Example:
MyStack stack = new MyStack();

stack.push(1);
stack.push(2);  
stack.top();   // returns 2
stack.pop();   // returns 2
stack.empty(); // returns false

Notes:
You must use only standard operations of a queue -- which means only push to 
back, peek/pop from front, size, and is empty operations are valid. Depending 
on your language, queue may not be supported natively. You may simulate a queue 
by using a list or deque (double-ended queue), as long as you use only standard 
operations of a queue. You may assume that all operations are valid (for 
example, no pop or top operations will be called on an empty stack)."""

class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = deque()

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.queue.append(x)
        for _ in range(len(self.queue)-1):
            self.queue.append(self.queue.popleft())

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.queue.popleft()

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.queue[0] 

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return not self.queue 


"""232. Implement Queue using Stacks (Easy)
Implement the following operations of a queue using stacks.
push(x) -- Push element x to the back of queue.
pop()   -- Removes the element from in front of queue.
peek()  -- Get the front element.
empty() -- Return whether the queue is empty.

Example:
MyQueue queue = new MyQueue();
queue.push(1);
queue.push(2);  
queue.peek();  // returns 1
queue.pop();   // returns 1
queue.empty(); // returns false

Notes:
You must use only standard operations of a stack -- which means only push to 
top, peek/pop from top, size, and is empty operations are valid. Depending on 
your language, stack may not be supported natively. You may simulate a stack by 
using a list or deque (double-ended queue), as long as you use only standard 
operations of a stack. You may assume that all operations are valid (for 
example, no pop or peek operations will be called on an empty queue)."""

class MyQueue:

    def __init__(self):
        self.in_ = [] #in stack 
        self.out = [] #out stack

    def push(self, x: int) -> None:
        self.in_.append(x)
        
    def _move(self) -> None: 
        if not self.out:
            while self.in_: self.out.append(self.in_.pop())

    def pop(self) -> int:
        self._move()
        return self.out.pop()

    def peek(self) -> int:
        self._move()
        return self.out[-1]

    def empty(self) -> bool:
        return not self.in_ and not self.out


"""244. Shortest Word Distance II (Medium)
Design a class which receives a list of words in the constructor, and implements 
a method that takes two words word1 and word2 and return the shortest distance 
between these two words in the list. Your method will be called repeatedly many 
times with different parameters. 

Example:
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

Input: word1 = “coding”, word2 = “practice”
Output: 3
Input: word1 = "makes", word2 = "coding"
Output: 1
Note: You may assume that word1 does not equal to word2, and word1 and word2 
      are both in the list."""

class WordDistance:

    def __init__(self, words: List[str]):
        self.loc = {}
        for i, w in enumerate(words):
            self.loc.setdefault(w, []).append(i)

    def shortest(self, word1: str, word2: str) -> int:
        ans = inf
        loc1, loc2 = self.loc[word1], self.loc[word2]
        i1 = i2 = 0 
        while i1 < len(loc1) and i2 < len(loc2):
            ans = min(ans, abs(loc1[i1] - loc2[i2]))
            if loc1[i1] < loc2[i2]: i1 += 1
            else: i2 += 1
        return ans 


"""251. Flatten 2D Vector (Medium)
Design and implement an iterator to flatten a 2d vector. It should support the 
following operations: next and hasNext.

Example:
Vector2D iterator = new Vector2D([[1,2],[3],[4]]);

iterator.next(); // return 1
iterator.next(); // return 2
iterator.next(); // return 3
iterator.hasNext(); // return true
iterator.hasNext(); // return true
iterator.next(); // return 4
iterator.hasNext(); // return false
 
Notes: Please remember to RESET your class variables declared in Vector2D, as 
       static/class variables are persisted across multiple test cases. Please 
       see here for more details. You may assume that next() call will always 
       be valid, that is, there will be at least a next element in the 2d vector 
       when next() is called.
 
Follow up: As an added challenge, try to code it using only iterators in C++ or 
           iterators in Java."""

class Vector2D:

    def __init__(self, v: List[List[int]]):
        
        def fn(arr):
            """Return flattened array."""
            ans = []
            for x in arr:
                if isinstance(x, int): ans.append(x)
                else: ans.extend(fn(x))
            return ans 
        
        self.vals = fn(v)
        self.i = 0                 

    def next(self) -> int:
        i, self.i = self.i, self.i+1
        return self.vals[i]

    def hasNext(self) -> bool:
        return self.i < len(self.vals)


"""271. Encode and Decode Strings (Medium)
Design an algorithm to encode a list of strings to a string. The encoded string 
is then sent over the network and is decoded back to the original list of strings.

Machine 1 (sender) has the function:

string encode(vector<string> strs) {
  // ... your code
  return encoded_string;
}
Machine 2 (receiver) has the function:
vector<string> decode(string s) {
  //... your code
  return strs;
}
So Machine 1 does:

string encoded_string = encode(strs);
and Machine 2 does:

vector<string> strs2 = decode(encoded_string);
strs2 in Machine 2 should be the same as strs in Machine 1. Implement the encode 
and decode methods.

Note:
* The string may contain any possible characters out of 256 valid ascii 
  characters. Your algorithm should be generalized enough to work on any 
  possible characters.
* Do not use class member/global/static variables to store states. Your encode 
  and decode algorithms should be stateless.
* Do not rely on any library method such as eval or serialize methods. You 
  should implement your own encode/decode algorithm."""

class Codec:
    def encode(self, strs: [str]) -> str:
        return "".join(f"{len(ss)}|{ss}" for ss in strs)

    def decode(self, s: str) -> [str]:
        ans = []
        i = 0
        while i < len(s):
            ii = s.find("|", i)
            i = ii+1+int(s[i:ii])
            ans.append(s[ii+1:i])
        return ans 


"""281. Zigzag Iterator (Medium)
Given two 1d vectors, implement an iterator to return their elements alternately.

Example:
Input:
v1 = [1,2]
v2 = [3,4,5,6] 
Output: [1,3,2,4,5,6]
Explanation: By calling next repeatedly until hasNext returns false, the order 
             of elements returned by next should be: [1,3,2,4,5,6].

Follow up: What if you are given k 1d vectors? How well can your code be 
           extended to such cases?

Clarification for the follow up question: The "Zigzag" order is not clearly 
defined and is ambiguous for k > 2 cases. If "Zigzag" does not look right to 
you, replace "Zigzag" with "Cyclic". For example:

Input:
[1,2,3]
[4,5,6,7]
[8,9]
Output: [1,4,8,2,5,9,3,6,7]."""

class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        self.vals = deque()
        if v1: self.vals.append(deque(v1))
        if v2: self.vals.append(deque(v2))

    def next(self) -> int:
        v = self.vals.popleft()
        ans = v.popleft()
        if v: self.vals.append(v)
        return ans 

    def hasNext(self) -> bool:
        return self.vals


"""284. Peeking Iterator (Medium)
Given an Iterator class interface with methods: next() and hasNext(), design 
and implement a PeekingIterator that support the peek() operation -- it 
essentially peek() at the element that will be returned by the next call to 
next().

Example:
Assume that the iterator is initialized to the beginning of the list: [1,2,3].
Call next() gets you 1, the first element in the list.
Now you call peek() and it returns 2, the next element. Calling next() after 
that still return 2. 
You call next() the final time and it returns 3, the last element. 
Calling hasNext() after that should return false.

Follow up: How would you extend your design to be generic and work with all 
           types, not just integer?"""

class PeekingIterator:
    def __init__(self, iterator):
        self.iter = iterator
        self._fill() #fill the buffer 
        
    def _fill(self):
        if self.iter.hasNext(): self.buff = self.iter.next()
        else: self.buff = None

    def peek(self):
        return self.buff

    def next(self):
        tmp = self.buff
        self._fill()
        return tmp

    def hasNext(self):
        return self.buff is not None


"""288. Unique Word Abbreviation (Medium)
The abbreviation of a word is a concatenation of its first letter, the number 
of characters between the first and last letter, and its last letter. If a word 
has only two characters, then it is an abbreviation of itself.

For example:
* dog --> d1g because there is one letter between the first letter 'd' and the 
  last letter 'g'.
* internationalization --> i18n because there are 18 letters between the first 
  letter 'i' and the last letter 'n'.
* it --> it because any word with only two characters is an abbreviation of 
  itself.

Implement the ValidWordAbbr class:
* ValidWordAbbr(String[] dictionary) Initializes the object with a dictionary 
  of words.
* boolean isUnique(string word) Returns true if either of the following 
  conditions are met (otherwise returns false):
  + There is no word in dictionary whose abbreviation is equal to word's 
    abbreviation.
  + For any word in dictionary whose abbreviation is equal to word's 
    abbreviation, that word and word are the same.

Example 1:
Input: ["ValidWordAbbr", "isUnique", "isUnique", "isUnique", "isUnique"]
       [[["deer", "door", "cake", "card"]], ["dear"], ["cart"], ["cane"], ["make"]]
Output: [null, false, true, false, true]

Explanation: 
ValidWordAbbr validWordAbbr = new ValidWordAbbr(["deer", "door", "cake", "card"]);
validWordAbbr.isUnique("dear"); // return false, dictionary word "deer" and word "dear" have the same abbreviation
                                // "d2r" but are not the same.
validWordAbbr.isUnique("cart"); // return true, no words in the dictionary have the abbreviation "c2t".
validWordAbbr.isUnique("cane"); // return false, dictionary word "cake" and word "cane" have the same abbreviation 
                                // "c2e" but are not the same.
validWordAbbr.isUnique("make"); // return true, no words in the dictionary have the abbreviation "m2e".
validWordAbbr.isUnique("cake"); // return true, because "cake" is already in the dictionary and no other word in the dictionary has "c2e" abbreviation.
 
Constraints:
* 1 <= dictionary.length <= 3 * 104
* 1 <= dictionary[i].length <= 20
* dictionary[i] consists of lowercase English letters.
* 1 <= word.length <= 20
* word consists of lowercase English letters.
* At most 5000 calls will be made to isUnique."""

class ValidWordAbbr:

    def __init__(self, dictionary: List[str]):
        self.mp = {}
        for word in set(dictionary): 
            key = word[0] + str(len(word)) + word[-1]
            self.mp.setdefault(key, set()).add(word)

    def isUnique(self, word: str) -> bool:
        key = word[0] + str(len(word)) + word[-1]
        return self.mp.get(key, set()) <= {word}


"""295. Find Median from Data Stream (Hard)
Median is the middle value in an ordered integer list. If the size of the list 
is even, there is no middle value. So the median is the mean of the two middle 
value.

For example, [2,3,4], the median is 3; [2,3], the median is (2 + 3) / 2 = 2.5

Design a data structure that supports the following two operations:
* void addNum(int num) - Add a integer number from the data stream to the data 
  structure.
* double findMedian() - Return the median of all elements so far.

Example:
addNum(1)
addNum(2)
findMedian() -> 1.5
addNum(3) 
findMedian() -> 2

Follow up:
* If all integer numbers from the stream are between 0 and 100, how would you 
  optimize it?
* If 99% of all integer numbers from the stream are between 0 and 100, how 
  would you optimize it?"""

class MedianFinder:

    def __init__(self):
        self.lo = [] #max heap for smaller half
        self.hi = [] #min heap for larger half

    def addNum(self, num: int) -> None:
        heappush(self.lo, -num)
        heappush(self.hi, -heappop(self.lo))
        if len(self.lo) < len(self.hi):
            heappush(self.lo, -heappop(self.hi))

    def findMedian(self) -> float:
        if len(self.lo) == len(self.hi): 
            return (-self.lo[0] + self.hi[0])/2
        return -self.lo[0]


"""304. Range Sum Query 2D - Immutable (Medium)
Given a 2D matrix matrix, find the sum of the elements inside the rectangle 
defined by its upper left corner (row1, col1) and lower right corner (row2, 
col2).

Example:
Given matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]

sumRegion(2, 1, 4, 3) -> 8
sumRegion(1, 1, 2, 2) -> 11
sumRegion(1, 2, 2, 4) -> 12

Note:
You may assume that the matrix does not change.
There are many calls to sumRegion function.
You may assume that row1 ≤ row2 and col1 ≤ col2."""

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        if not matrix: return 
        m, n = len(matrix), len(matrix[0])
        self.prefix = [[0]*(n+1) for _ in range(m+1)]
        for i in range(m):
            for j in range(n):
                self.prefix[i+1][j+1] = matrix[i][j] + self.prefix[i][j+1] + self.prefix[i+1][j] - self.prefix[i][j]
        
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.prefix[row2+1][col2+1] - self.prefix[row1][col2+1] - self.prefix[row2+1][col1] + self.prefix[row1][col1]


"""341. Flatten Nested List Iterator (Medium)
Given a nested list of integers, implement an iterator to flatten it. Each 
element is either an integer, or a list -- whose elements may also be integers 
or other lists.

Example 1:
Input: [[1,1],2,[1,1]]
Output: [1,1,2,1,1]
Explanation: By calling next repeatedly until hasNext returns false, 
             the order of elements returned by next should be: [1,1,2,1,1].

Example 2:
Input: [1,[4,[6]]]
Output: [1,4,6]
Explanation: By calling next repeatedly until hasNext returns false, 
             the order of elements returned by next should be: [1,4,6]."""

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.stack = []
        if nestedList: self.stack.append((nestedList, 0))
        self.val = self._get()
            
    def _get(self) -> int: 
        """Get next value in queue."""
        while self.stack: 
            data, i = self.stack.pop()
            if i+1 < len(data): self.stack.append((data, i+1)) #backtracking point 
            if data[i].isInteger(): return data[i].getInteger()
            if not data[i].getList(): continue #empty list 
            self.stack.append((data[i].getList(), 0)) #push nested list on stack
        return None
    
    def next(self) -> int:
        ans, self.val = self.val, self._get()
        return ans 
    
    def hasNext(self) -> bool:
        return self.val is not None 


"""346. Moving Average from Data Stream (Easy)
Given a stream of integers and a window size, calculate the moving average of 
all integers in the sliding window. 

Implement the MovingAverage class:
* MovingAverage(int size) Initializes the object with the size of the window size.
* double next(int val) Returns the moving average of the last size values of the stream.

Example 1:
Input: ["MovingAverage", "next", "next", "next", "next"]
       [[3], [1], [10], [3], [5]]
Output: [null, 1.0, 5.5, 4.66667, 6.0]
Explanation: 
MovingAverage movingAverage = new MovingAverage(3);
movingAverage.next(1); // return 1.0 = 1 / 1
movingAverage.next(10); // return 5.5 = (1 + 10) / 2
movingAverage.next(3); // return 4.66667 = (1 + 10 + 3) / 3
movingAverage.next(5); // return 6.0 = (10 + 3 + 5) / 3

Constraints:
* 1 <= size <= 1000
* -10^5 <= val <= 10^5
* At most 104 calls will be made to next."""

class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.nums = deque()
        self.size = size 
        self.rsm = 0

    def next(self, val: int) -> float:
        self.nums.append(val)
        self.rsm += val
        if len(self.nums) > self.size: 
            self.rsm -= self.nums.popleft()
        return self.rsm/len(self.nums)


"""348. Design Tic-Tac-Toe (Medium)
Assume the following rules are for the tic-tac-toe game on an n x n board 
between two players:
* A move is guaranteed to be valid and is placed on an empty block.
* Once a winning condition is reached, no more moves are allowed.
* A player who succeeds in placing n of their marks in a horizontal, vertical, 
  or diagonal row wins the game.

Implement the TicTacToe class:
* TicTacToe(int n) Initializes the object the size of the board n.
* int move(int row, int col, int player) Indicates that player with id player 
  plays at the cell (row, col) of the board. The move is guaranteed to be a valid move.

Follow up: Could you do better than O(n2) per move() operation?

Example 1:
Input: ["TicTacToe", "move", "move", "move", "move", "move", "move", "move"]
       [[3], [0, 0, 1], [0, 2, 2], [2, 2, 1], [1, 1, 2], [2, 0, 1], [1, 0, 2], [2, 1, 1]]
Output: [null, 0, 0, 0, 0, 0, 0, 1]
Explanation: 
TicTacToe ticTacToe = new TicTacToe(3);
Assume that player 1 is "X" and player 2 is "O" in the board.
ticTacToe.move(0, 0, 1); // return 0 (no one wins)
|X| | |
| | | |    // Player 1 makes a move at (0, 0).
| | | |

ticTacToe.move(0, 2, 2); // return 0 (no one wins)
|X| |O|
| | | |    // Player 2 makes a move at (0, 2).
| | | |

ticTacToe.move(2, 2, 1); // return 0 (no one wins)
|X| |O|
| | | |    // Player 1 makes a move at (2, 2).
| | |X|

ticTacToe.move(1, 1, 2); // return 0 (no one wins)
|X| |O|
| |O| |    // Player 2 makes a move at (1, 1).
| | |X|

ticTacToe.move(2, 0, 1); // return 0 (no one wins)
|X| |O|
| |O| |    // Player 1 makes a move at (2, 0).
|X| |X|

ticTacToe.move(1, 0, 2); // return 0 (no one wins)
|X| |O|
|O|O| |    // Player 2 makes a move at (1, 0).
|X| |X|

ticTacToe.move(2, 1, 1); // return 1 (player 1 wins)
|X| |O|
|O|O| |    // Player 1 makes a move at (2, 1).
|X|X|X|
 
Constraints:
* 2 <= n <= 100
* player is 1 or 2.
* 1 <= row, col <= n
* (row, col) are unique for each different call to move.
* At most n2 calls will be made to move."""

class TicTacToe:

    def __init__(self, n: int):
        self.n = n
        self.rows = [[0]*n for _ in range(2)]
        self.cols = [[0]*n for _ in range(2)]
        self.diag = [0]*2
        self.anti = [0]*2

    def move(self, row: int, col: int, player: int) -> int:
        self.rows[player-1][row] += 1
        self.cols[player-1][col] += 1
        if row == col: self.diag[player-1] += 1
        if row + col == self.n-1: self.anti[player-1] += 1
        if self.n in (self.rows[player-1][row], self.cols[player-1][col], self.diag[player-1], self.anti[player-1]): return player
        return 0 


"""353. Design Snake Game (Medium)
Design a Snake game that is played on a device with screen size height x width. 
Play the game online if you are not familiar with the game. The snake is 
initially positioned at the top left corner (0, 0) with a length of 1 unit. You 
are given an array food where food[i] = (ri, ci) is the row and column position 
of a piece of food that the snake can eat. When a snake eats a piece of food, 
its length and the game's score both increase by 1. Each piece of food appears 
one by one on the screen, meaning the second piece of food will not appear 
until the snake eats the first piece of food. When a piece of food appears on 
the screen, it is guaranteed that it will not appear on a block occupied by the 
snake. The game is over if the snake goes out of bounds (hits a wall) or if its 
head occupies a space that its body occupies after moving (i.e. a snake of 
length 4 cannot run into itself).

Implement the SnakeGame class:
* SnakeGame(int width, int height, int[][] food) Initializes the object with a 
  screen of size height x width and the positions of the food.
* int move(String direction) Returns the score of the game after applying one 
  direction move by the snake. If the game is over, return -1.

Example 1:
Input: ["SnakeGame", "move", "move", "move", "move", "move", "move"]
       [[3, 2, [[1, 2], [0, 1]]], ["R"], ["D"], ["R"], ["U"], ["L"], ["U"]]
Output: [null, 0, 0, 1, 1, 2, -1]
Explanation:
SnakeGame snakeGame = new SnakeGame(3, 2, [[1, 2], [0, 1]]);
snakeGame.move("R"); // return 0
snakeGame.move("D"); // return 0
snakeGame.move("R"); // return 1, snake eats the first piece of food. The second piece of food appears
                     // at (0, 1).
snakeGame.move("U"); // return 1
snakeGame.move("L"); // return 2, snake eats the second food. No more food appears.
snakeGame.move("U"); // return -1, game over because snake collides with border
 
Constraints:
* 1 <= width, height <= 104
* 1 <= food.length <= 50
* food[i].length == 2
* 0 <= ri < height
* 0 <= ci < width
* direction.length == 1
* direction is 'U', 'D', 'L', or 'R'.
* At most 104 calls will be made to move."""

class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        """
        Initialize your data structure here.
        @param width - screen width
        @param height - screen height 
        @param food - A list of food positions
        E.g food = [[1,1], [1,0]] means the first food is positioned at [1,1], the second is at [1,0].
        """
        self.width = width
        self.height = height 
        self.food = deque(food)
        self.position = OrderedDict({(0,0): 0})

    def move(self, direction: str) -> int:
        """
        Moves the snake.
        @param direction - 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down 
        @return The game's score after the move. Return -1 if game over. 
        Game over when snake crosses the screen boundary or bites its body.
        """
        (i, j), _ = self.position.popitem(last=True) # current position
        self.position[(i, j)] = 0 # add back 
        if direction == "U": i -= 1
        elif direction == "L": j -= 1
        elif direction == "R": j += 1
        else: i += 1
        if self.food and self.food[0] == [i, j]: self.food.popleft()
        else: self.position.popitem(last=False)
        if not (0 <= i < self.height and 0 <= j < self.width) or (i, j) in self.position: return -1 # game over 
        self.position[(i, j)] = 0
        return len(self.position)-1


"""355. Design Twitter (Medium)
Design a simplified version of Twitter where users can post tweets, 
follow/unfollow another user and is able to see the 10 most recent tweets in 
the user's news feed. Your design should support the following methods:
+ postTweet(userId, tweetId): Compose a new tweet.
+ getNewsFeed(userId): Retrieve the 10 most recent tweet ids in the user's news 
  feed. Each item in the news feed must be posted by users who the user followed 
  or by the user herself. Tweets must be ordered from most recent to least recent.
+ follow(followerId, followeeId): Follower follows a followee.
+ unfollow(followerId, followeeId): Follower unfollows a followee.

Example:
Twitter twitter = new Twitter();
// User 1 posts a new tweet (id = 5).
twitter.postTweet(1, 5);
// User 1's news feed should return a list with 1 tweet id -> [5].
twitter.getNewsFeed(1);
// User 1 follows user 2.
twitter.follow(1, 2);
// User 2 posts a new tweet (id = 6).
twitter.postTweet(2, 6);
// User 1's news feed should return a list with 2 tweet ids -> [6, 5].
// Tweet id 6 should precede tweet id 5 because it is posted after tweet id 5.
twitter.getNewsFeed(1);
// User 1 unfollows user 2.
twitter.unfollow(1, 2);
// User 1's news feed should return a list with 1 tweet id -> [5],
// since user 1 is no longer following user 2.
twitter.getNewsFeed(1);"""

class Twitter:

    def __init__(self):
        self.cnt = 0 # global counter 
        self.tweets = {} # mapping from user to tweets
        self.followers = {} # mapping from user to followers

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.cnt += 1
        self.tweets.setdefault(userId, deque()).appendleft((self.cnt, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        hp = [] # max heap 
        for fid in self.followers.get(userId, set()) | {userId}: 
            if fid in self.tweets: # has tweeted 
                cnt, tid = self.tweets[fid][0]
                heappush(hp, (-cnt, tid, fid, 0)) # push follower's tweet on heap 
        ans = []
        for _ in range(10): 
            if not hp: break 
            _, tid, uid, i = heappop(hp)
            ans.append(tid)
            if i+1 < len(self.tweets[uid]): 
                cnt, tid = self.tweets[uid][i+1]
                heappush(hp, (-cnt, tid, uid, i+1))
        return ans 

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followers.setdefault(followerId, set()).add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followers.setdefault(followerId, set()).discard(followeeId)


"""359. Logger Rate Limiter (Easy)
Design a logger system that receives a stream of messages along with their 
timestamps. Each unique message should only be printed at most every 10 seconds 
(i.e. a message printed at timestamp t will prevent other identical messages 
from being printed until timestamp t + 10). All messages will come in 
chronological order. Several messages may arrive at the same timestamp.

Implement the Logger class:
* Logger() Initializes the logger object.
* bool shouldPrintMessage(int timestamp, string message) Returns true if the message should be printed in the given timestamp, otherwise returns false.

Example 1:
Input: ["Logger", "shouldPrintMessage", "shouldPrintMessage", "shouldPrintMessage", "shouldPrintMessage", "shouldPrintMessage", "shouldPrintMessage"]
       [[], [1, "foo"], [2, "bar"], [3, "foo"], [8, "bar"], [10, "foo"], [11, "foo"]]
Output: [null, true, true, false, false, false, true]
Explanation:
Logger logger = new Logger();
logger.shouldPrintMessage(1, "foo");  // return true, next allowed timestamp for "foo" is 1 + 10 = 11
logger.shouldPrintMessage(2, "bar");  // return true, next allowed timestamp for "bar" is 2 + 10 = 12
logger.shouldPrintMessage(3, "foo");  // 3 < 11, return false
logger.shouldPrintMessage(8, "bar");  // 8 < 12, return false
logger.shouldPrintMessage(10, "foo"); // 10 < 11, return false
logger.shouldPrintMessage(11, "foo"); // 11 >= 11, return true, next allowed timestamp for "foo" is
                                      // 11 + 10 = 21
 
Constraints:
* 0 <= timestamp <= 10^9
* Every timestamp will be passed in non-decreasing order (chronological order).
* 1 <= message.length <= 30
* At most 10^4 calls will be made to shouldPrintMessage."""

class Logger:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.seen = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        """
        if timestamp - self.seen.get(message, -inf) >= 10: 
            self.seen[message] = timestamp
            return True
        return False 


"""362. Design Hit Counter (Medium)
Design a hit counter which counts the number of hits received in the past 5 
minutes. Each function accepts a timestamp parameter (in seconds granularity) 
and you may assume that calls are being made to the system in chronological 
order (ie, the timestamp is monotonically increasing). You may assume that the 
earliest timestamp starts at 1. It is possible that several hits arrive roughly 
at the same time.

Example:
HitCounter counter = new HitCounter();

// hit at timestamp 1.
counter.hit(1);

// hit at timestamp 2.
counter.hit(2);

// hit at timestamp 3.
counter.hit(3);

// get hits at timestamp 4, should return 3.
counter.getHits(4);

// hit at timestamp 300.
counter.hit(300);

// get hits at timestamp 300, should return 4.
counter.getHits(300);

// get hits at timestamp 301, should return 3.
counter.getHits(301); 
Follow up:
What if the number of hits per second could be very large? Does your design scale?"""

class HitCounter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = deque()
        self.val = 0

    def hit(self, timestamp: int) -> None:
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        if self.queue and self.queue[-1][0] == timestamp: self.queue[-1][1] += 1
        else: self.queue.append([timestamp, 1])
        self.val += 1

    def getHits(self, timestamp: int) -> int:
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        while self.queue and self.queue[0][0] + 300 <= timestamp: 
            self.val -= self.queue.popleft()[1]
        return self.val 


"""379. Design Phone Directory (Medium)
Design a Phone Directory which supports the following operations:
* get: Provide a number which is not assigned to anyone.
* check: Check if a number is available or not.
* release: Recycle or release a number.

Example:
// Init a phone directory containing a total of 3 numbers: 0, 1, and 2.
PhoneDirectory directory = new PhoneDirectory(3);

// It can return any available phone number. Here we assume it returns 0.
directory.get();

// Assume it returns 1.
directory.get();

// The number 2 is available, so return true.
directory.check(2);

// It returns 2, the only number that is left.
directory.get();

// The number 2 is no longer available, so return false.
directory.check(2);

// Release number 2 back to the pool.
directory.release(2);

// Number 2 is available again, return true.
directory.check(2);
 
Constraints:
* 1 <= maxNumbers <= 10^4
* 0 <= number < maxNumbers
* The total number of call of the methods is between [0 - 20000]"""

class PhoneDirectory:

    def __init__(self, maxNumbers: int):
        """
        Initialize your data structure here
        @param maxNumbers - The maximum numbers that can be stored in the phone directory.
        """
        self.nums = set(range(maxNumbers))

    def get(self) -> int:
        """
        Provide a number which is not assigned to anyone.
        @return - Return an available number. Return -1 if none is available.
        """
        return self.nums.pop() if self.nums else -1 

    def check(self, number: int) -> bool:
        """
        Check if a number is available or not.
        """
        return number in self.nums

    def release(self, number: int) -> None:
        """
        Recycle or release a number.
        """
        self.nums.add(number)


"""380. Insert Delete GetRandom O(1) (Medium)
Design a data structure that supports all following operations in average O(1) 
time.
+ insert(val): Inserts an item val to the set if not already present.
+ remove(val): Removes an item val from the set if present.
+ getRandom: Returns a random element from current set of elements (it's 
             guaranteed that at least one element exists when this method is 
             called). Each element must have the same probability of being 
             returned.
Example:
// Init an empty set.
RandomizedSet randomSet = new RandomizedSet();
// Inserts 1 to the set. Returns true as 1 was inserted successfully.
randomSet.insert(1);
// Returns false as 2 does not exist in the set.
randomSet.remove(2);
// Inserts 2 to the set, returns true. Set now contains [1,2].
randomSet.insert(2);
// getRandom should return either 1 or 2 randomly.
randomSet.getRandom();
// Removes 1 from the set, returns true. Set now contains [2].
randomSet.remove(1);
// 2 was already in the set, so return false.
randomSet.insert(2);
// Since 2 is the only number in the set, getRandom always return 2.
randomSet.getRandom();"""

class RandomizedSet:

    def __init__(self):
        self.val = [] # array of values
        self.map = {} # mapping from value to index 

    def insert(self, val: int) -> bool:
        if val in self.map: return False 
        self.map[val] = len(self.val) # insert to mapping
        self.val.append(val) # insert to array 
        return True 

    def remove(self, val: int) -> bool:
        if val not in self.map: return False 
        i = self.map[val]
        self.map[self.val[-1]] = i
        self.map.pop(val)
        self.val[i] = self.val[-1]
        self.val.pop()
        return True 

    def getRandom(self) -> int:
        return choice(self.val)


"""381. Insert Delete GetRandom O(1) - Duplicates allowed (Hard)
Design a data structure that supports all following operations in average O(1) 
time. Note: Duplicate elements are allowed.
+ insert(val): Inserts an item val to the collection.
+ remove(val): Removes an item val from the collection if present.
+ getRandom: Returns a random element from current collection of elements. The 
             probability of each element being returned is linearly related to 
             the number of same value the collection contains.
Example:
// Init an empty collection.
RandomizedCollection collection = new RandomizedCollection();
// Inserts 1 to the collection. Returns true as the collection did not contain 1.
collection.insert(1);
// Inserts another 1 to the collection. Returns false as the collection contained 1. Collection now contains [1,1].
collection.insert(1);
// Inserts 2 to the collection, returns true. Collection now contains [1,1,2].
collection.insert(2);
// getRandom should return 1 with the probability 2/3, and returns 2 with the probability 1/3.
collection.getRandom();
// Removes 1 from the collection, returns true. Collection now contains [1,2].
collection.remove(1);
// getRandom should return 1 and 2 both equally likely.
collection.getRandom();"""

class RandomizedCollection:

    def __init__(self):
        self.val = [] # val 
        self.mpp = {} # val to set of indices 

    def insert(self, val: int) -> bool:
        self.mpp.setdefault(val, set()).add(len(self.val))
        self.val.append(val)
        return len(self.mpp[val]) == 1

    def remove(self, val: int) -> bool:
        if val not in self.mpp or not self.mpp[val]: return False  # flag 
        i = self.mpp[val].pop()
        self.mpp[self.val[-1]].add(i)
        self.mpp[self.val[-1]].remove(len(self.val)-1)
        self.val[i] = self.val[-1]
        self.val.pop()
        return True

    def getRandom(self) -> int:
        return choice(self.val)


"""382. Linked List Random Node (Medium)
Given a singly linked list, return a random node's value from the linked list. 
Each node must have the same probability of being chosen.

Follow up: What if the linked list is extremely large and its length is unknown 
           to you? Could you solve this efficiently without using extra space?

Example:
// Init a singly linked list [1,2,3].
ListNode head = new ListNode(1);
head.next = new ListNode(2);
head.next.next = new ListNode(3);
Solution solution = new Solution(head);

// getRandom() should return either 1, 2, or 3 randomly. Each element should 
// have equal probability of returning.
solution.getRandom();"""

class Solution:

    def __init__(self, head: ListNode):
        self.head = head # store head of linked list 

    def getRandom(self) -> int:
        cnt = 0
        node = self.head 
        while node: 
            cnt += 1
            if randint(1, cnt) == cnt: ans = node.val # reservoir sampling 
            node = node.next 
        return ans 


"""384. Shuffle an Array (Medium)
Shuffle a set of numbers without duplicates.

Example:
// Init an array with set 1, 2, and 3.
int[] nums = {1,2,3};
Solution solution = new Solution(nums);

// Shuffle the array [1,2,3] and return its result. Any permutation of [1,2,3] must equally likely to be returned.
solution.shuffle();

// Resets the array back to its original configuration [1,2,3].
solution.reset();

// Returns the random shuffling of array [1,2,3].
solution.shuffle();"""

class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.orig = nums.copy() # original array 

    def reset(self) -> List[int]:
        return self.orig

    def shuffle(self) -> List[int]:
        for i in range(1, len(self.nums)): 
            ii = randint(0, i)
            self.nums[ii], self.nums[i] = self.nums[i], self.nums[ii]
        return self.nums


"""398. Random Pick Index (Medium)
Given an array of integers with possible duplicates, randomly output the index 
of a given target number. You can assume that the given target number must 
exist in the array. Note that the array size can be very large. Solution that 
uses too much extra space will not pass the judge.

Example:
int[] nums = new int[] {1,2,3,3,3};
Solution solution = new Solution(nums);
// pick(3) should return either index 2, 3, or 4 randomly. Each index should 
// have equal probability of returning.
solution.pick(3);
// pick(1) should return 0. Since in the array only nums[0] is equal to 1.
solution.pick(1);"""

class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums # store nums

    def pick(self, target: int) -> int:
        """Sample index of target via resevoir sampling."""
		ans = None
        cnt = 0
        for i, x in enumerate(self.nums): 
            if x == target: 
                cnt += 1
                if randint(1, cnt) == cnt: ans = i # prob 1/cnt
        return ans 


"""519. Random Flip Matrix (Medium)
You are given the number of rows n_rows and number of columns n_cols of a 2D 
binary matrix where all values are initially 0. Write a function flip which 
chooses a 0 value uniformly at random, changes it to 1, and then returns the 
position [row.id, col.id] of that value. Also, write a function reset which 
sets all values back to 0. Try to minimize the number of calls to system's 
Math.random() and optimize the time and space complexity.

Note:
* 1 <= n_rows, n_cols <= 10000
* 0 <= row.id < n_rows and 0 <= col.id < n_cols
* flip will not be called when the matrix has no 0 values left.
* the total number of calls to flip and reset will not exceed 1000.

Example 1:
Input: 
["Solution","flip","flip","flip","flip"]
[[2,3],[],[],[],[]]
Output: [null,[0,1],[1,2],[1,0],[1,1]]

Example 2:
Input: 
["Solution","flip","flip","reset","flip"]
[[1,2],[],[],[],[]]
Output: [null,[0,0],[0,1],null,[0,0]]

Explanation of Input Syntax: The input is two lists: the subroutines called and 
their arguments. Solution's constructor has two arguments, n_rows and n_cols. 
flip and reset have no arguments. Arguments are always wrapped with a list, 
even if there aren't any."""

class Solution:

    def __init__(self, n_rows: int, n_cols: int):
        self.mp = {}
        self.cols = n_cols
        self.size = self.cpty = n_rows * n_cols 

    def flip(self) -> List[int]:
        self.size -= 1
        r = randint(0, self.size) 
        rr = self.mp.get(r, r) # mapped random number (remove duplicates)
        self.mp[r] = self.mp.get(self.size, self.size) # move rn at self.size to r
        return rr//self.cols, rr%self.cols

    def reset(self) -> None:
        self.mp = {}
        self.size = self.cpty 


"""528. Random Pick with Weight (Medium)
You are given an array of positive integers w where w[i] describes the weight 
of ith index (0-indexed). We need to call the function pickIndex() which 
randomly returns an integer in the range [0, w.length - 1]. pickIndex() should 
return the integer proportional to its weight in the w array. For example, for 
w = [1, 3], the probability of picking the index 0 is 1 / (1 + 3) = 0.25 
(i.e 25%) while the probability of picking the index 1 is 3 / (1 + 3) = 0.75 
(i.e 75%). More formally, the probability of picking index i is w[i] / sum(w).

Example 1:
Input:
["Solution","pickIndex"]
[[[1]],[]]
Output: [null,0]

Explanation:
Solution solution = new Solution([1]);
solution.pickIndex(); // return 0. Since there is only one single element on the array the only option is to return the first element.

Example 2:
Input:
["Solution","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex"]
[[[1,3]],[],[],[],[],[]]
Output: [null,1,1,1,1,0]
Explanation: 
Solution solution = new Solution([1, 3]);
solution.pickIndex(); // return 1. It's returning the second element (index = 1) that has probability of 3/4.
solution.pickIndex(); // return 1
solution.pickIndex(); // return 1
solution.pickIndex(); // return 1
solution.pickIndex(); // return 0. It's returning the first element (index = 0) that has probability of 1/4.

Since this is a randomization problem, multiple answers are allowed so the following outputs can be considered correct :
[null,1,1,1,1,0]
[null,1,1,1,1,1]
[null,1,1,1,0,0]
[null,1,1,1,0,1]
[null,1,0,1,0,0]
......
and so on.

Constraints:
* 1 <= w.length <= 10000
* 1 <= w[i] <= 10^5
* pickIndex will be called at most 10000 times."""

class Solution:

    def __init__(self, w: List[int]):
        self.prefix = [0]
        for x in w: self.prefix.append(self.prefix[-1] + x)

    def pickIndex(self) -> int:
        r = randint(1, self.prefix[-1])
        
        def fn(arr, x):
            """Return the position of x in arr."""
            lo, hi = 0, len(arr)
            while lo < hi: 
                mid = lo + hi >> 1
                if arr[mid] < x: lo = mid+1
                else: hi = mid
            return lo
        
        return fn(self.prefix, r)-1


"""535. Encode and Decode TinyURL (Medium)
Note: This is a companion problem to the System Design problem: Design TinyURL. 
TinyURL is a URL shortening service where you enter a URL such as 
https://leetcode.com/problems/design-tinyurl and it returns a short URL such as 
http://tinyurl.com/4e9iAk. Design the encode and decode methods for the TinyURL 
service. There is no restriction on how your encode/decode algorithm should 
work. You just need to ensure that a URL can be encoded to a tiny URL and the 
tiny URL can be decoded to the original URL."""

class Codec:
    
    def __init__(self): 
        self.lookup = {}

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL."""
        ans = "http://tinyurl.com/" + hex(abs(hash(longUrl)))
        self.lookup[ans] = longUrl
        return ans 
        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL."""
        return self.lookup[shortUrl]


"""604. Design Compressed String Iterator (Easy)
Design and implement a data structure for a compressed string iterator. The 
given compressed string will be in the form of each letter followed by a 
positive integer representing the number of this letter existing in the original 
uncompressed string.

Implement the StringIterator class:
* next() Returns the next character if the original string still has uncompressed characters, otherwise returns a white space.
* hasNext() Returns true if there is any letter needs to be uncompressed in the original string, otherwise returns false.

Example 1:
Input: ["StringIterator", "next", "next", "next", "next", "next", "next", "hasNext", "next", "hasNext"]
       [["L1e2t1C1o1d1e1"], [], [], [], [], [], [], [], [], []]
Output: [null, "L", "e", "e", "t", "C", "o", true, "d", true]
Explanation:
StringIterator stringIterator = new StringIterator("L1e2t1C1o1d1e1");
stringIterator.next(); // return "L"
stringIterator.next(); // return "e"
stringIterator.next(); // return "e"
stringIterator.next(); // return "t"
stringIterator.next(); // return "C"
stringIterator.next(); // return "o"
stringIterator.hasNext(); // return True
stringIterator.next(); // return "d"
stringIterator.hasNext(); // return True

Constraints:
* 1 <= compressedString.length <= 1000
* compressedString consists of lower-case an upper-case English letters and digits.
* The number of a single character repetitions in compressedString is in the range [1, 10^9]
* At most 100 calls will be made to next and hasNext."""

class StringIterator:

    def __init__(self, compressedString: str):
        self.data = compressedString 
        self.char = None
        self.i = self.n = 0

    def next(self) -> str:
        if not self.hasNext(): return " "
        if not self.n: 
            self.char = self.data[self.i]
            self.i = ii = self.i+1
            while self.i < len(self.data) and self.data[self.i].isdigit(): self.i += 1
            self.n = int(self.data[ii:self.i])
        self.n -= 1
        return self.char 

    def hasNext(self) -> bool:
        return self.i < len(self.data) or self.n 


"""706. Design HashMap (Easy)
Design a HashMap without using any built-in hash table libraries. To be 
specific, your design should include these functions:
* put(key, value) : Insert a (key, value) pair into the HashMap. If the value 
  already exists in the HashMap, update the value.
* get(key): Returns the value to which the specified key is mapped, or -1 if 
  this map contains no mapping for the key.
* remove(key) : Remove the mapping for the value key if this map contains the 
  mapping for the key.

Example:
MyHashMap hashMap = new MyHashMap();
hashMap.put(1, 1);          
hashMap.put(2, 2);         
hashMap.get(1);            // returns 1
hashMap.get(3);            // returns -1 (not found)
hashMap.put(2, 1);         // update the existing value
hashMap.get(2);            // returns 1 
hashMap.remove(2);         // remove the mapping for 2
hashMap.get(2);            // returns -1 (not found) 

Note:
* All keys and values will be in the range of [0, 1000000].
* The number of operations will be in the range of [1, 10000].
* Please do not use the built-in HashMap library."""

class ListNode:
    def __init__(self, key=None, val=None, next=None): 
        self.key = key
        self.val = val
        self.next = next
        
        
class MyHashMap:

    def __init__(self):
        self.data = [ListNode()] * 1000

    def put(self, key: int, value: int) -> None:
        node = self.data[key % len(self.data)]
        while node.next: 
            if node.next.key == key: 
                node.next.val = value
                return 
            node = node.next 
        node.next = ListNode(key, value)

    def get(self, key: int) -> int:
        node = self.data[key % len(self.data)]
        while node: 
            if node.key == key: return node.val
            node = node.next 
        return -1 

    def remove(self, key: int) -> None:
        node = self.data[key % len(self.data)]
        while node.next: 
            if node.next.key == key: 
                node.next = node.next.next
                return 
            node = node.next 


"""716. Max Stack (Easy)
Design a max stack data structure that supports the stack operations and 
supports finding the stack's maximum element.

Implement the MaxStack class:
* MaxStack() Initializes the stack object.
* void push(int x) Pushes element x onto the stack.
* int pop() Removes the element on top of the stack and returns it.
* int top() Gets the element on the top of the stack without removing it.
* int peekMax() Retrieves the maximum element in the stack without removing it.
* int popMax() Retrieves the maximum element in the stack and removes it. If 
  there is more than one maximum element, only remove the top-most one.
 
Example 1:
Input: ["MaxStack", "push", "push", "push", "top", "popMax", "top", "peekMax", "pop", "top"]
       [[], [5], [1], [5], [], [], [], [], [], []]
Output: [null, null, null, null, 5, 5, 1, 5, 1, 5]
Explanation
MaxStack stk = new MaxStack();
stk.push(5);   // [5] the top of the stack and the maximum number is 5.
stk.push(1);   // [5, 1] the top of the stack is 1, but the maximum is 5.
stk.push(5);   // [5, 1, 5] the top of the stack is 5, which is also the maximum, because it is the top most one.
stk.top();     // return 5, [5, 1, 5] the stack did not change.
stk.popMax();  // return 5, [5, 1] the stack is changed now, and the top is different from the max.
stk.top();     // return 1, [5, 1] the stack did not change.
stk.peekMax(); // return 5, [5, 1] the stack did not change.
stk.pop();     // return 1, [5] the top of the stack and the max element is now 5.
stk.top();     // return 5, [5] the stack did not change.
 
Constraints:
* -10^7 <= x <= 10^7
* At most 104 calls will be made to push, pop, top, peekMax, and popMax.
* There will be at least one element in the stack when pop, top, peekMax, or 
  popMax is called.

Follow up: Could you come up with a solution that supports O(1) for each top 
           call and O(logn) for each other call? """

class MaxStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.k = 0              # key
        self.pq = []            # priority queue 
        self.od = OrderedDict() # ordered dict 

    def push(self, x: int) -> None:
        heappush(self.pq, (-x, self.k))
        self.od[self.k] = x
        self.k -= 1

    def pop(self) -> int:
        k, x = self.od.popitem(last=True)
        return x

    def top(self) -> int:
        k, x = self.od.popitem(last=True)
        self.od[k] = x
        return x

    def peekMax(self) -> int:
        while self.pq: 
            x, k = heappop(self.pq)
            if k in self.od: break 
        heappush(self.pq, (x, k))
        return -x

    def popMax(self) -> int:
        while self.pq: 
            x, k = heappop(self.pq)
            if k in self.od: break 
        self.od.pop(k)
        return -x 


"""729. My Calendar I (Medium)
Implement a MyCalendar class to store your events. A new event can be added if 
adding the event will not cause a double booking. Your class will have the 
method, book(int start, int end). Formally, this represents a booking on the 
half open interval [start, end), the range of real numbers x such that 
start <= x < end. A double booking happens when two events have some non-empty 
intersection (ie., there is some time that is common to both events.) For each 
call to the method MyCalendar.book, return true if the event can be added to 
the calendar successfully without causing a double booking. Otherwise, return 
false and do not add the event to the calendar. Your class will be called like 
this: MyCalendar cal = new MyCalendar(); MyCalendar.book(start, end)

Example 1:
MyCalendar();
MyCalendar.book(10, 20); // returns true
MyCalendar.book(15, 25); // returns false
MyCalendar.book(20, 30); // returns true
Explanation: 
The first event can be booked. The second can't because time 15 is already 
booked by another event. The third event can be booked, as the first event 
takes every time less than 20, but not including 20.

Note:
* The number of calls to MyCalendar.book per test case will be at most 1000.
* In calls to MyCalendar.book(start, end), start and end are integers in the 
  range [0, 10^9].

class Node: 
    def __init__(self, val=0, left=None, right=None): 
        self.val = val
        self.left = left
        self.right = right 
"""

class MyCalendar:

    def __init__(self):
        self.root = None

    def book(self, start: int, end: int) -> bool:
        if not self.root: 
            self.root = Node((start, end))
            return True 
        prev = node = self.root 
        while node: 
            prev = node 
            if end <= node.val[0]: node = node.left 
            elif node.val[1] <= start: node = node.right 
            else: return False # double booking 
        if end <= prev.val[0]: prev.left = Node((start, end))
        else: prev.right = Node((start, end))
        return True 


"""911. Online Election (Medium)
In an election, the i-th vote was cast for persons[i] at time times[i]. Now, we 
would like to implement the following query function: TopVotedCandidate.q(int t) 
will return the number of the person that was leading the election at time t. 
Votes cast at time t will count towards our query.  In the case of a tie, the 
most recent vote (among tied candidates) wins.

Example 1:
Input: ["TopVotedCandidate","q","q","q","q","q","q"], [[[0,1,1,0,0,1,0],[0,5,10,15,20,25,30]],[3],[12],[25],[15],[24],[8]]
Output: [null,0,1,1,0,0,1]
Explanation: 
At time 3, the votes are [0], and 0 is leading.
At time 12, the votes are [0,1,1], and 1 is leading.
At time 25, the votes are [0,1,1,0,0,1], and 1 is leading (as ties go to the most recent vote.)
This continues for 3 more queries at time 15, 24, and 8.

Note:
* 1 <= persons.length = times.length <= 5000
* 0 <= persons[i] <= persons.length
* times is a strictly increasing array with all elements in [0, 10^9].
* TopVotedCandidate.q is called at most 10000 times per test case.
* TopVotedCandidate.q(int t) is always called with t >= times[0]."""

class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.times = times 
        self.winner = []
        
        pp = 0 
        freq = {} # frequency table 
        for p in persons: 
            freq[p] = 1 + freq.get(p, 0)
            if freq[p] >= freq.get(pp, 0): pp = p
            self.winner.append(pp)


    def q(self, t: int) -> int:
        """Standard last-true binary search."""
        lo, hi = -1, len(self.times)-1
        while lo < hi: 
            mid = lo + hi + 1 >> 1
            if self.times[mid] <= t: lo = mid
            else: hi = mid - 1
        return self.winner[lo]


"""919. Complete Binary Tree Inserter (Medium)
A complete binary tree is a binary tree in which every level, except possibly 
the last, is completely filled, and all nodes are as far left as possible. 
Write a data structure CBTInserter that is initialized with a complete binary 
tree and supports the following operations:
* CBTInserter(TreeNode root) initializes the data structure on a given tree 
  with head node root;
* CBTInserter.insert(int v) will insert a TreeNode into the tree with value 
  node.val = v so that the tree remains complete, and returns the value of the 
  parent of the inserted TreeNode;
* CBTInserter.get_root() will return the head node of the tree.

Example 1:
Input: inputs = ["CBTInserter","insert","get_root"], inputs = [[[1]],[2],[]]
Output: [null,1,[1,2]]

Example 2:
Input: inputs = ["CBTInserter","insert","insert","get_root"], 
       inputs = [[[1,2,3,4,5,6]],[7],[8],[]]
Output: [null,3,4,[1,2,3,4,5,6,7,8]]

Note:
* The initial given tree is complete and contains between 1 and 1000 nodes.
* CBTInserter.insert is called at most 10000 times per test case.
* Every value of a given or inserted node is between 0 and 5000."""

class CBTInserter:

    def __init__(self, root: TreeNode):
        self.root = root
        self.nodes = deque([]) # nodes with None child
        queue = deque([root])
        while queue: # bfs 
            node = queue.popleft()
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
            else: self.nodes.append(node)

    def insert(self, v: int) -> int:
        node = self.nodes[0]
        ans = node.val
        if not node.left: node.left = node = TreeNode(v)
        else: 
            node.right = node = TreeNode(v)
            self.nodes.popleft()
        self.nodes.append(node)
        return ans 

    def get_root(self) -> TreeNode:
        return self.root


"""1357. Apply Discount Every n Orders (Medium)
There is a sale in a supermarket, there will be a discount every n customer. 
There are some products in the supermarket where the id of the i-th product is 
products[i] and the price per unit of this product is prices[i]. The system 
will count the number of customers and when the n-th customer arrive he/she 
will have a discount on the bill. (i.e if the cost is x the new cost is 
x - (discount * x) / 100). Then the system will start counting customers again. 
The customer orders a certain amount of each product where product[i] is the id 
of the i-th product the customer ordered and amount[i] is the number of units 
the customer ordered of that product. Implement the Cashier class:
* Cashier(int n, int discount, int[] products, int[] prices) Initializes the 
  object with n, the discount, the products and their prices.
* double getBill(int[] product, int[] amount) returns the value of the bill and 
  apply the discount if needed. Answers within 10^-5 of the actual value will 
  be accepted as correct.

Example 1:
Input
["Cashier","getBill","getBill","getBill","getBill","getBill","getBill","getBill"]
[[3,50,[1,2,3,4,5,6,7],[100,200,300,400,300,200,100]],[[1,2],[1,2]],[[3,7],[10,10]],[[1,2,3,4,5,6,7],[1,1,1,1,1,1,1]],[[4],[10]],[[7,3],[10,10]],[[7,5,3,1,6,4,2],[10,10,10,9,9,9,7]],[[2,3,5],[5,3,2]]]
Output
[null,500.0,4000.0,800.0,4000.0,4000.0,7350.0,2500.0]
Explanation
Cashier cashier = new Cashier(3,50,[1,2,3,4,5,6,7],[100,200,300,400,300,200,100]);
cashier.getBill([1,2],[1,2]);                        // return 500.0, bill = 1 * 100 + 2 * 200 = 500.
cashier.getBill([3,7],[10,10]);                      // return 4000.0
cashier.getBill([1,2,3,4,5,6,7],[1,1,1,1,1,1,1]);    // return 800.0, The bill was 1600.0 but as this is the third customer, he has a discount of 50% which means his bill is only 1600 - 1600 * (50 / 100) = 800.
cashier.getBill([4],[10]);                           // return 4000.0
cashier.getBill([7,3],[10,10]);                      // return 4000.0
cashier.getBill([7,5,3,1,6,4,2],[10,10,10,9,9,9,7]); // return 7350.0, Bill was 14700.0 but as the system counted three more customers, he will have a 50% discount and the bill becomes 7350.0
cashier.getBill([2,3,5],[5,3,2]);                    // return 2500.0
 
Constraints:
* 1 <= n <= 10^4
* 0 <= discount <= 100
* 1 <= products.length <= 200
* 1 <= products[i] <= 200
* There are not repeated elements in the array products.
* prices.length == products.length
* 1 <= prices[i] <= 1000
* 1 <= product.length <= products.length
* product[i] exists in products.
* amount.length == product.length
* 1 <= amount[i] <= 1000
* At most 1000 calls will be made to getBill.
* Answers within 10^-5 of the actual value will be accepted as correct."""

class Cashier:

    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.k = 0 # counter 
        self.n = n
        self.discount = discount
        self.prices = dict(zip(products, prices))

    def getBill(self, product: List[int], amount: List[int]) -> float:
        self.k += 1
        cost = sum(self.prices[i]*amt for i, amt in zip(product, amount))
        if self.k == self.n: 
            cost *= 1 - self.discount/100
            self.k = 0
        return cost 


"""1396. Design Underground System (Medium)
Implement the UndergroundSystem class:
* void checkIn(int id, string stationName, int t)
  + A customer with a card id equal to id, gets in the station stationName at time t.
  + A customer can only be checked into one place at a time.
* void checkOut(int id, string stationName, int t)
  + A customer with a card id equal to id, gets out from the station stationName at time t.
* double getAverageTime(string startStation, string endStation)
  + Returns the average time to travel between the startStation and the endStation.
  + The average time is computed from all the previous traveling from startStation to endStation that happened directly.
  + Call to getAverageTime is always valid.
You can assume all calls to checkIn and checkOut methods are consistent. If a 
customer gets in at time t1 at some station, they get out at time t2 with 
t2 > t1. All events happen in chronological order.

Example 1:
Input: ["UndergroundSystem","checkIn","checkIn","checkIn","checkOut","checkOut","checkOut","getAverageTime","getAverageTime","checkIn","getAverageTime","checkOut","getAverageTime"]
       [[],[45,"Leyton",3],[32,"Paradise",8],[27,"Leyton",10],[45,"Waterloo",15],[27,"Waterloo",20],[32,"Cambridge",22],["Paradise","Cambridge"],["Leyton","Waterloo"],[10,"Leyton",24],["Leyton","Waterloo"],[10,"Waterloo",38],["Leyton","Waterloo"]]
Output: [null,null,null,null,null,null,null,14.00000,11.00000,null,11.00000,null,12.00000]
Explanation:
UndergroundSystem undergroundSystem = new UndergroundSystem();
undergroundSystem.checkIn(45, "Leyton", 3);
undergroundSystem.checkIn(32, "Paradise", 8);
undergroundSystem.checkIn(27, "Leyton", 10);
undergroundSystem.checkOut(45, "Waterloo", 15);
undergroundSystem.checkOut(27, "Waterloo", 20);
undergroundSystem.checkOut(32, "Cambridge", 22);
undergroundSystem.getAverageTime("Paradise", "Cambridge");       // return 14.00000. There was only one travel from "Paradise" (at time 8) to "Cambridge" (at time 22)
undergroundSystem.getAverageTime("Leyton", "Waterloo");          // return 11.00000. There were two travels from "Leyton" to "Waterloo", a customer with id=45 from time=3 to time=15 and a customer with id=27 from time=10 to time=20. So the average time is ( (15-3) + (20-10) ) / 2 = 11.00000
undergroundSystem.checkIn(10, "Leyton", 24);
undergroundSystem.getAverageTime("Leyton", "Waterloo");          // return 11.00000
undergroundSystem.checkOut(10, "Waterloo", 38);
undergroundSystem.getAverageTime("Leyton", "Waterloo");          // return 12.00000

Example 2:
Input: ["UndergroundSystem","checkIn","checkOut","getAverageTime","checkIn","checkOut","getAverageTime","checkIn","checkOut","getAverageTime"]
       [[],[10,"Leyton",3],[10,"Paradise",8],["Leyton","Paradise"],[5,"Leyton",10],[5,"Paradise",16],["Leyton","Paradise"],[2,"Leyton",21],[2,"Paradise",30],["Leyton","Paradise"]]
Output: [null,null,null,5.00000,null,null,5.50000,null,null,6.66667]
Explanation:
UndergroundSystem undergroundSystem = new UndergroundSystem();
undergroundSystem.checkIn(10, "Leyton", 3);
undergroundSystem.checkOut(10, "Paradise", 8);
undergroundSystem.getAverageTime("Leyton", "Paradise"); // return 5.00000
undergroundSystem.checkIn(5, "Leyton", 10);
undergroundSystem.checkOut(5, "Paradise", 16);
undergroundSystem.getAverageTime("Leyton", "Paradise"); // return 5.50000
undergroundSystem.checkIn(2, "Leyton", 21);
undergroundSystem.checkOut(2, "Paradise", 30);
undergroundSystem.getAverageTime("Leyton", "Paradise"); // return 6.66667
 
Constraints:
* There will be at most 20000 operations.
* 1 <= id, t <= 10^6
* All strings consist of uppercase and lowercase English letters, and digits.
* 1 <= stationName.length <= 10
* Answers within 10-5 of the actual value will be accepted as correct."""

class UndergroundSystem:

    def __init__(self):
        self.in_ = {}
        self.out = defaultdict(lambda: defaultdict(lambda: [0, 0]))

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.in_[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        ss, tt = self.in_[id]
        self.out[stationName][ss][0] += t - tt
        self.out[stationName][ss][1] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        s, c = self.out[endStation][startStation]
        return s/c 


"""1476. Subrectangle Queries (Medium)
Implement the class SubrectangleQueries which receives a rows x cols rectangle 
as a matrix of integers in the constructor and supports two methods:
1. updateSubrectangle(int row1, int col1, int row2, int col2, int newValue)
  * Updates all values with newValue in the subrectangle whose upper left 
    coordinate is (row1,col1) and bottom right coordinate is (row2,col2).
2. getValue(int row, int col)
  * Returns the current value of the coordinate (row,col) from the rectangle.

Example 1:
Input
["SubrectangleQueries","getValue","updateSubrectangle","getValue","getValue","updateSubrectangle","getValue","getValue"]
[[[[1,2,1],[4,3,4],[3,2,1],[1,1,1]]],[0,2],[0,0,3,2,5],[0,2],[3,1],[3,0,3,2,10],[3,1],[0,2]]
Output
[null,1,null,5,5,null,10,5]
Explanation
SubrectangleQueries subrectangleQueries = new SubrectangleQueries([[1,2,1],[4,3,4],[3,2,1],[1,1,1]]);  
// The initial rectangle (4x3) looks like:
// 1 2 1
// 4 3 4
// 3 2 1
// 1 1 1
subrectangleQueries.getValue(0, 2); // return 1
subrectangleQueries.updateSubrectangle(0, 0, 3, 2, 5);
// After this update the rectangle looks like:
// 5 5 5
// 5 5 5
// 5 5 5
// 5 5 5 
subrectangleQueries.getValue(0, 2); // return 5
subrectangleQueries.getValue(3, 1); // return 5
subrectangleQueries.updateSubrectangle(3, 0, 3, 2, 10);
// After this update the rectangle looks like:
// 5   5   5
// 5   5   5
// 5   5   5
// 10  10  10 
subrectangleQueries.getValue(3, 1); // return 10
subrectangleQueries.getValue(0, 2); // return 5

Example 2:
Input
["SubrectangleQueries","getValue","updateSubrectangle","getValue","getValue","updateSubrectangle","getValue"]
[[[[1,1,1],[2,2,2],[3,3,3]]],[0,0],[0,0,2,2,100],[0,0],[2,2],[1,1,2,2,20],[2,2]]
Output
[null,1,null,100,100,null,20]
Explanation
SubrectangleQueries subrectangleQueries = new SubrectangleQueries([[1,1,1],[2,2,2],[3,3,3]]);
subrectangleQueries.getValue(0, 0); // return 1
subrectangleQueries.updateSubrectangle(0, 0, 2, 2, 100);
subrectangleQueries.getValue(0, 0); // return 100
subrectangleQueries.getValue(2, 2); // return 100
subrectangleQueries.updateSubrectangle(1, 1, 2, 2, 20);
subrectangleQueries.getValue(2, 2); // return 20
 
Constraints:
* There will be at most 500 operations considering both methods: updateSubrectangle and getValue.
* 1 <= rows, cols <= 100
* rows == rectangle.length
* cols == rectangle[i].length
* 0 <= row1 <= row2 < rows
* 0 <= col1 <= col2 < cols
* 1 <= newValue, rectangle[i][j] <= 10^9
* 0 <= row < rows
* 0 <= col < cols"""

class SubrectangleQueries:

    def __init__(self, rectangle: List[List[int]]):
        self.rectangle = rectangle
        self.ops = []

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        self.ops.append([row1, col1, row2, col2, newValue])

    def getValue(self, row: int, col: int) -> int:
        for r1, c1, r2, c2, val in reversed(self.ops): 
            if r1 <= row <= r2 and c1 <= col <= c2: return val
        return self.rectangle[row][col]


"""1603. Design Parking System (Easy)
Design a parking system for a parking lot. The parking lot has three kinds of 
parking spaces: big, medium, and small, with a fixed number of slots for each 
size. Implement the ParkingSystem class:
* ParkingSystem(int big, int medium, int small) Initializes object of the 
  ParkingSystem class. The number of slots for each parking space are given as 
  part of the constructor.
* bool addCar(int carType) Checks whether there is a parking space of carType 
  for the car that wants to get into the parking lot. carType can be of three 
  kinds: big, medium, or small, which are represented by 1, 2, and 3 
  respectively. A car can only park in a parking space of its carType. If there 
  is no space available, return false, else park the car in that size space and 
  return true.

Example 1:
Input: ["ParkingSystem", "addCar", "addCar", "addCar", "addCar"]
       [[1, 1, 0], [1], [2], [3], [1]]
Output: [null, true, true, false, false]
Explanation:
ParkingSystem parkingSystem = new ParkingSystem(1, 1, 0);
parkingSystem.addCar(1); // return true because there is 1 available slot for a big car
parkingSystem.addCar(2); // return true because there is 1 available slot for a medium car
parkingSystem.addCar(3); // return false because there is no available slot for a small car
parkingSystem.addCar(1); // return false because there is no available slot for a big car. It is already occupied.

Constraints:
* 0 <= big, medium, small <= 1000
* carType is 1, 2, or 3
* At most 1000 calls will be made to addCar"""

class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.space = [big, medium, small]

    def addCar(self, carType: int) -> bool:
        self.space[carType-1] -= 1 # space taken 
        return self.space[carType-1] >= 0


"""1622. Fancy Sequence (Hard)
Write an API that generates fancy sequences using the append, addAll, and 
multAll operations. Implement the Fancy class:
* Fancy() Initializes the object with an empty sequence.
* void append(val) Appends an integer val to the end of the sequence.
* void addAll(inc) Increments all existing values in the sequence by an integer 
  inc.
* void multAll(m) Multiplies all existing values in the sequence by an integer 
  m.
* int getIndex(idx) Gets the current value at index idx (0-indexed) of the 
  sequence modulo 109 + 7. If the index is greater or equal than the length of 
  the sequence, return -1.

Example 1:
Input: ["Fancy", "append", "addAll", "append", "multAll", "getIndex", "addAll", "append", "multAll", "getIndex", "getIndex", "getIndex"]
       [[], [2], [3], [7], [2], [0], [3], [10], [2], [0], [1], [2]]
Output: [null, null, null, null, null, 10, null, null, null, 26, 34, 20]
Explanation
Fancy fancy = new Fancy();
fancy.append(2);   // fancy sequence: [2]
fancy.addAll(3);   // fancy sequence: [2+3] -> [5]
fancy.append(7);   // fancy sequence: [5, 7]
fancy.multAll(2);  // fancy sequence: [5*2, 7*2] -> [10, 14]
fancy.getIndex(0); // return 10
fancy.addAll(3);   // fancy sequence: [10+3, 14+3] -> [13, 17]
fancy.append(10);  // fancy sequence: [13, 17, 10]
fancy.multAll(2);  // fancy sequence: [13*2, 17*2, 10*2] -> [26, 34, 20]
fancy.getIndex(0); // return 26
fancy.getIndex(1); // return 34
fancy.getIndex(2); // return 20

Constraints:
* 1 <= val, inc, m <= 100
* 0 <= idx <= 10^5
* At most 10^5 calls total will be made to append, addAll, multAll, and getIndex."""

class Fancy:
    
    def __init__(self):
        self.data = []
        self.cmul = [1]
        self.csum = [0]
        self.mod = 1_000_000_007

    def append(self, val: int) -> None:
        self.data.append(val)
        self.cmul.append(self.cmul[-1])
        self.csum.append(self.csum[-1])

    def addAll(self, inc: int) -> None:
        self.csum[-1] += inc

    def multAll(self, m: int) -> None:
        self.cmul[-1] = (self.cmul[-1] * m) % self.mod
        self.csum[-1] = (self.csum[-1] * m) % self.mod
        
    def getIndex(self, idx: int) -> int:
        if idx < len(self.data): 
            ratio = self.cmul[-1] * pow(self.cmul[idx], self.mod-2, self.mod) # Fermat's little theorem
            return ((self.data[idx] - self.csum[idx]) * ratio + self.csum[-1]) % self.mod
        return -1 


"""1656. Design an Ordered Stream (Easy)
There are n (id, value) pairs, where id is an integer between 1 and n and value 
is a string. No two pairs have the same id. Design a stream that takes the n 
pairs in an arbitrary order, and returns the values over several calls in 
increasing order of their ids. Implement the OrderedStream class:
* OrderedStream(int n) Constructs the stream to take n values and sets a current 
  ptr to 1.
* String[] insert(int id, String value) Stores the new (id, value) pair in the 
  stream. After storing the pair:
  + If the stream has stored a pair with id = ptr, then find the longest 
    contiguous incrementing sequence of ids starting with id = ptr and return a 
    list of the values associated with those ids in order. Then, update ptr to 
    the last id + 1.
  + Otherwise, return an empty list.

Example:
Input: ["OrderedStream", "insert", "insert", "insert", "insert", "insert"]
       [[5], [3, "ccccc"], [1, "aaaaa"], [2, "bbbbb"], [5, "eeeee"], [4, "ddddd"]]
Output: [null, [], ["aaaaa"], ["bbbbb", "ccccc"], [], ["ddddd", "eeeee"]]
Explanation: 
OrderedStream os= new OrderedStream(5);
os.insert(3, "ccccc"); // Inserts (3, "ccccc"), returns [].
os.insert(1, "aaaaa"); // Inserts (1, "aaaaa"), returns ["aaaaa"].
os.insert(2, "bbbbb"); // Inserts (2, "bbbbb"), returns ["bbbbb", "ccccc"].
os.insert(5, "eeeee"); // Inserts (5, "eeeee"), returns [].
os.insert(4, "ddddd"); // Inserts (4, "ddddd"), returns ["ddddd", "eeeee"].
 
Constraints:
* 1 <= n <= 1000
* 1 <= id <= n
* value.length == 5
* value consists only of lowercase letters.
* Each call to insert will have a unique id.
* Exactly n calls will be made to insert."""

class OrderedStream:

    def __init__(self, n: int):
        self.data = [None]*n
        self.ptr = 0

    def insert(self, id: int, value: str) -> List[str]:
        id -= 1
        self.data[id] = value 
        if id == self.ptr: 
            while self.ptr < len(self.data) and self.data[self.ptr]: self.ptr += 1 # update self.ptr 
        return self.data[id:self.ptr]


"""1670. Design Front Middle Back Queue (Medium)
Design a queue that supports push and pop operations in the front, middle, and 
back. Implement the FrontMiddleBack class:
* FrontMiddleBack() Initializes the queue.
* void pushFront(int val) Adds val to the front of the queue.
* void pushMiddle(int val) Adds val to the middle of the queue.
* void pushBack(int val) Adds val to the back of the queue.
* int popFront() Removes the front element of the queue and returns it. If the 
  queue is empty, return -1.
* int popMiddle() Removes the middle element of the queue and returns it. If 
  the queue is empty, return -1.
* int popBack() Removes the back element of the queue and returns it. If the 
  queue is empty, return -1.
Notice that when there are two middle position choices, the operation is 
performed on the frontmost middle position choice. For example:
* Pushing 6 into the middle of [1, 2, 3, 4, 5] results in [1, 2, 6, 3, 4, 5].
* Popping the middle from [1, 2, 3, 4, 5, 6] returns 3 and results in [1, 2, 4, 5, 6].

Example 1:
Input: ["FrontMiddleBackQueue", "pushFront", "pushBack", "pushMiddle", "pushMiddle", "popFront", "popMiddle", "popMiddle", "popBack", "popFront"]
       [[], [1], [2], [3], [4], [], [], [], [], []]
Output: [null, null, null, null, null, 1, 3, 4, 2, -1]
Explanation:
FrontMiddleBackQueue q = new FrontMiddleBackQueue();
q.pushFront(1);   // [1]
q.pushBack(2);    // [1, 2]
q.pushMiddle(3);  // [1, 3, 2]
q.pushMiddle(4);  // [1, 4, 3, 2]
q.popFront();     // return 1 -> [4, 3, 2]
q.popMiddle();    // return 3 -> [4, 2]
q.popMiddle();    // return 4 -> [2]
q.popBack();      // return 2 -> []
q.popFront();     // return -1 -> [] (The queue is empty)
 
Constraints:
* 1 <= val <= 109
* At most 1000 calls will be made to pushFront, pushMiddle, pushBack, popFront, 
  popMiddle, and popBack."""

class FrontMiddleBackQueue:

    def __init__(self):
        self.d0 = deque()
        self.d1 = deque()
        
    def _balance(self):
        if len(self.d0) > len(self.d1): self.d1.appendleft(self.d0.pop())
        elif len(self.d0) + 1 < len(self.d1): self.d0.append(self.d1.popleft())

    def pushFront(self, val: int) -> None:
        self.d0.appendleft(val)
        self._balance()

    def pushMiddle(self, val: int) -> None:
        self.d0.append(val)
        self._balance()

    def pushBack(self, val: int) -> None:
        self.d1.append(val)
        self._balance()
        
    def popFront(self) -> int:
        if self.d0: 
            ans = self.d0.popleft()
            self._balance()
            return ans 
        elif self.d1: return self.d1.pop()
        else: return -1

    def popMiddle(self) -> int:
        if self.d0 and len(self.d0) == len(self.d1): return self.d0.pop()
        elif self.d1: return self.d1.popleft()
        return -1

    def popBack(self) -> int:
        ans = (self.d1 or [-1]).pop()
        self._balance()
        return ans 


"""1756. Design Most Recently Used Queue (Medium)
Design a queue-like data structure that moves the most recently used element to 
the end of the queue. Implement the MRUQueue class:
* MRUQueue(int n) constructs the MRUQueue with n elements: [1,2,3,...,n].
* fetch(int k) moves the kth element (1-indexed) to the end of the queue and returns it.

Example 1:
Input: ["MRUQueue", "fetch", "fetch", "fetch", "fetch"]
       [[8], [3], [5], [2], [8]]
Output: [null, 3, 6, 2, 2]
Explanation:
MRUQueue mRUQueue = new MRUQueue(8); // Initializes the queue to [1,2,3,4,5,6,7,8].
mRUQueue.fetch(3); // Moves the 3rd element (3) to the end of the queue to become [1,2,4,5,6,7,8,3] and returns it.
mRUQueue.fetch(5); // Moves the 5th element (6) to the end of the queue to become [1,2,4,5,7,8,3,6] and returns it.
mRUQueue.fetch(2); // Moves the 2nd element (2) to the end of the queue to become [1,4,5,7,8,3,6,2] and returns it.
mRUQueue.fetch(8); // The 8th element (2) is already at the end of the queue so just return it.

Constraints:
* 1 <= n <= 2000
* 1 <= k <= n
* At most 2000 calls will be made to fetch.

Follow up: Finding an O(n) algorithm per fetch is a bit easy. Can you find an 
           algorithm with a better complexity for each fetch call?"""

from sortedcontainers import SortedList # balanced BST

class MRUQueue:

    def __init__(self, n: int):
        self.data = SortedList((i, i) for i in range(1, n+1))

    def fetch(self, k: int) -> int:
        _, x = self.data.pop(k-1)
        i = self.data[-1][0] + 1 if self.data else 0
        self.data.add((i, x))
        return x


"""1797. Design Authentication Manager (Medium)
There is an authentication system that works with authentication tokens. For 
each session, the user will receive a new authentication token that will expire 
timeToLive seconds after the currentTime. If the token is renewed, the expiry 
time will be extended to expire timeToLive seconds after the (potentially 
different) currentTime. Implement the AuthenticationManager class:
* AuthenticationManager(int timeToLive) constructs the AuthenticationManager 
  and sets the timeToLive.
* generate(string tokenId, int currentTime) generates a new token with the 
  given tokenId at the given currentTime in seconds.
* renew(string tokenId, int currentTime) renews the unexpired token with the 
  given tokenId at the given currentTime in seconds. If there are no unexpired tokens with the given tokenId, the request is ignored, and nothing happens.
* countUnexpiredTokens(int currentTime) returns the number of unexpired tokens 
  at the given currentTime.
Note that if a token expires at time t, and another action happens on time t 
(renew or countUnexpiredTokens), the expiration takes place before the other 
actions.

Example 1:
Input: ["AuthenticationManager", "renew", "generate", "countUnexpiredTokens", "generate", "renew", "renew", "countUnexpiredTokens"]
       [[5], ["aaa", 1], ["aaa", 2], [6], ["bbb", 7], ["aaa", 8], ["bbb", 10], [15]]
Output: [null, null, null, 1, null, null, null, 0]
Explanation: 
AuthenticationManager authenticationManager = new AuthenticationManager(5); // Constructs the AuthenticationManager with timeToLive = 5 seconds.
authenticationManager.renew("aaa", 1); // No token exists with tokenId "aaa" at time 1, so nothing happens.
authenticationManager.generate("aaa", 2); // Generates a new token with tokenId "aaa" at time 2.
authenticationManager.countUnexpiredTokens(6); // The token with tokenId "aaa" is the only unexpired one at time 6, so return 1.
authenticationManager.generate("bbb", 7); // Generates a new token with tokenId "bbb" at time 7.
authenticationManager.renew("aaa", 8); // The token with tokenId "aaa" expired at time 7, and 8 >= 7, so at time 8 the renew request is ignored, and nothing happens.
authenticationManager.renew("bbb", 10); // The token with tokenId "bbb" is unexpired at time 10, so the renew request is fulfilled and now the token will expire at time 15.
authenticationManager.countUnexpiredTokens(15); // The token with tokenId "bbb" expires at time 15, and the token with tokenId "aaa" expired at time 7, so currently no token is unexpired, so return 0.

Constraints:
* 1 <= timeToLive <= 10^8
* 1 <= currentTime <= 10^8
* 1 <= tokenId.length <= 5
* tokenId consists only of lowercase letters.
* All calls to generate will contain unique values of tokenId.
* The values of currentTime across all the function calls will be strictly increasing.
* At most 2000 calls will be made to all functions combined."""

class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.timeToLive = timeToLive
        self.tokens = {}

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.tokens[tokenId] = currentTime + self.timeToLive

    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId in self.tokens and self.tokens[tokenId] > currentTime: 
            self.tokens[tokenId] = currentTime + self.timeToLive

    def countUnexpiredTokens(self, currentTime: int) -> int:
        for token in self.tokens.copy(): 
            if self.tokens[token] <= currentTime: # not expired yet 
                self.tokens.pop(token)
        return len(self.tokens)