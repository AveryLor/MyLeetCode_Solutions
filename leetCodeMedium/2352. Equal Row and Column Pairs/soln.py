class Solution(object):
    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        count = 0

        for i in range(n): # Iterate through all rows
            for j in range(n): # Iterate through all columns
                match = True

                # Mover through iterating between columns and 
                for k in range(n):
                    if grid[i][k] != grid[k][j]:
                        match = False
                
                if match:
                    count += 1
        
        return count