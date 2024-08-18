class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        n = len(positions)
        robots = []
        res = []
        for i in range(n):
            robot = Robot(positions[i],healths[i],directions[i])
            robots.append(robot)
        robots = sort_robot(robots)
        while robots:
            while robots[0].direction == 'L' :
                res.append(robots[0])
                robots.pop(0)
                if not robots: break
            if not robots: break
            while robots[-1].direction == 'R' : 
                res.append(robots[-1])
                robots.pop(-1)
                if not robots: break
            if not robots: break
            i =0
            while not(robots[i].direction == 'R'and robots[i+1].direction=='L'):
                i+=1
            if robots[i].health < robots[i+1].health:
                robots[i+1].health-=1
                robots.pop(i)
            elif robots[i].health == robots[i+1].health:
                robots.pop(i+1)
                robots.pop(i)
            else:
                robots[i].health-=1
                robots.pop(i+1)     
        res = [x.health for x in res]
        return res
            

class Robot(Solution):
    def __init__(self,position : int,health : int,direction : str):
        self.position = position
        self.health = health
        self.direction = direction
def sort_robot(robots):
    return sorted(robots,key = lambda x :x.position)

