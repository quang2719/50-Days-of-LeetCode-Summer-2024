from queue import PriorityQueue
class People:
    def __init__(self,name,heigh):
        self.name = name
        self.heigh = heigh
    def __lt__(self, other):
        return self.heigh > other.heigh
class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        res = []
        pq = PriorityQueue()
        for i in range(len(names)):
            person = People(names[i],heights[i])
            pq.put(person)
        while not pq.empty():
            res.append(pq.get().name)
        return res