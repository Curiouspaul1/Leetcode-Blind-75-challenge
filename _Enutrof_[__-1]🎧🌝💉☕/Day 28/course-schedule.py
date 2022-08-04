from collections import defaultdict, deque
class Solution:
    def assist(self,val):
        d = deque([val])
        seen = set()
        while d:
            course = d.pop()
            if course is not None:
                try:
                    if self.approval[course]:
                        continue
                    else:
                        return False
                except:
                    d.extend(self.adj[course])
                    if course not in seen:
                        seen.add(course)
                    else:
                        if course == val:
                            return False
                        elif not self.assist(course):
                            return False
        return True
                
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        self.adj = defaultdict(lambda: [])
        for i in prerequisites:
            self.adj[i[0]].append(i[1])
        self.approval = {}
        self.visited = set()
        can= 0
        for i in range(numCourses):
            if self.assist(i):
                can += 1
                self.approval[i] = True
            else:
                self.approval[i] = False
                
        
        return can == numCourses
                
