class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        stack = []

        for asteroid in asteroids:

            alive = True

            while stack and asteroid < 0 < stack[-1]: # Ensuring new element is less than 0
                if abs(asteroid) > stack[-1]: # Incoming asteroid larger
                    stack.pop()
                    continue

                elif abs(asteroid) == stack[-1]: # Both are destroyed
                    stack.pop()

                alive = False
                break

            if alive:
                stack.append(asteroid)
        
        return stack
            

