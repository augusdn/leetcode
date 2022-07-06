class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # make pair for each position and speed
        pair = [[p,s] for p,s in zip(position, speed)]
        
        fleet = []
        # loop each position and speed in reversed sorted list
        for p,s in sorted(pair)[::-1]:
            fleet.append((target-p)/s)
            """
            if higher positioned car (fleet[-2]) 
            takes equal or greater time than current car
            pop the current car and leave the old one
            they become one fleet
            """
            if len(fleet) >= 2 and fleet[-2] >= fleet[-1]:
                fleet.pop()
            
        return len(fleet)
