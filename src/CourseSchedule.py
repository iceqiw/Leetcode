import collections


class Solution:

    def __init__(self) -> None:
        self.record = collections.defaultdict(int)
        self.graph = collections.defaultdict(list)
        self.stack = []

    def canFinish(self, numCourses: int, prerequisites) -> bool:
        self.gen_graph(prerequisites)
        self.stack = [course for course in range(numCourses) if self.record[course] == 0]
        while self.stack:
            course
            for dep in self.graph[course]:
                self.record[dep] -= 1
                if self.record[dep] == 0:
                    self.stack.append(dep)
        return all(self.record[course] == 0 for course in self.record)

    def gen_graph(self, prerequisites):
        for a, b in prerequisites:
            self.graph[b].append(a)
            self.record[a] += 1  # 依赖了多少个值


class Solution2:
    """
    @param: numCourses: a total of n courses
    @param: prerequisites: a list of prerequisite pairs
    @return: true if can finish all courses or false
    """

    def canFinish(self, numCourses, prerequisites):
        # write your code here
        g = collections.defaultdict(list)
        indegree = collections.defaultdict(int)
        for a, b in prerequisites:
            g[a].append(b)
            indegree[b] += 1
        stack = [course for course in range(numCourses) if indegree[course] == 0]
        while stack:
            course = stack.pop()
            for nei in g[course]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    stack.append(nei)
        return all(indegree[course] == 0 for course in indegree)
