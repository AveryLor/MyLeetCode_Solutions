class Solution(object):
    def predictPartyVictory(self, senate):
        """
        :type senate: str
        :rtype: str
        """
        dires = deque()
        radiant = deque()
        
        n = len(senate)

        for i in range(n):
            
            if senate[i] == "D":
                dires.append(i)
            else:
                radiant.append(i)
            
        
        while radiant and dires:
            r = radiant.popleft()
            d = dires.popleft()

            if r < d:
                radiant.append(r + n)
            else:
                dires.append(d + n)
        
        return "Radiant" if radiant else "Dire"