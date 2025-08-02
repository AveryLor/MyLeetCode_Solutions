class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        currentAltitude = 0
        max_altitude = 0
        for i in range(len(gain)):
            currentAltitude += gain[i]
            max_altitude = max(max_altitude, currentAltitude)

        return max_altitude
        