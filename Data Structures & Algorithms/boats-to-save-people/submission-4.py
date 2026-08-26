class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        n = len(people)
        people.sort()
        boats = 0
        l, r = 0, n - 1
        print(people)

        while l <= r:
            print(l, r, people[l], people[r])
            if people[l] + people[r] <= limit:
                boats += 1
                l += 1
                r -= 1
            else:
                print(f"People at r is heavy")
                boats += 1
                r -= 1
        
        return boats