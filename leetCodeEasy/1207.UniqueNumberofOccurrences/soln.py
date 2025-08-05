class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """

        count_dict = dict()

        for num in arr:
            if num in count_dict:
                count_dict[num] += 1
            else:
                count_dict[num] = 1

        frequencies = list(count_dict.values())
        return len(frequencies) == len(set(frequencies))


