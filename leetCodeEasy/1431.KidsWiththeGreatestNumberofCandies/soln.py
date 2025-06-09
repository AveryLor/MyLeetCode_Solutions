class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        
        listReturn = []
        for i in range(len(candies)): 
            max = True
            for j in range(len(candies)): 
                if i == j: 
                    continue
                elif candies[i] + extraCandies < candies[j]:
                    max = False
                    break
            listReturn.append(max)
        return listReturn



        