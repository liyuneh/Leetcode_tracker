class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        incoming = [0 for _ in range(numCourses)]
        q = deque()
        sortedone = []
        for course , pre in prerequisites:
            graph[pre].append(course)
            incoming[course] += 1
        
        for course in range(numCourses):
            if incoming[course] == 0:
                q.append(course)
        while q:
            course = q.popleft()
            sortedone.append(course)

            for ne in graph[course]:
                incoming[ne] -= 1
                if incoming[ne] == 0:
                    q.append(ne)
        print(sortedone)
        return len(sortedone) == numCourses