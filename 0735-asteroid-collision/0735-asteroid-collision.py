class Solution(object):
    def asteroidCollision(self, asteroids):

        i = 0

        while i < len(asteroids) - 1:

            current = asteroids[i]
            next_asteroid = asteroids[i + 1]

            if current > 0 and next_asteroid < 0:

                if abs(current) > abs(next_asteroid):
                    asteroids.pop(i + 1)

                elif abs(current) < abs(next_asteroid):
                    asteroids.pop(i)

                    if i > 0:
                        i -= 1

                else:
                    asteroids.pop(i + 1)
                    asteroids.pop(i)

                    if i > 0:
                        i -= 1

            else:
                i += 1

        return asteroids