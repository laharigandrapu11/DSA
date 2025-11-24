# Last updated: 11/24/2025, 5:43:00 PM
class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        values = []
        nums_str = []
        finalList = []
        for n in nums:
            nums_str.append(str(n)) #['0', '1', '1']
        binary_str = ""
        for n in nums_str:
            binary_str += str(n)
            values.append(binary_str)
        for n in values:
            n = int(n,2)
            finalList.append(n % 5 == 0)
        # int(binary_string, 2)
        # int(binary, 2)
        return finalList
