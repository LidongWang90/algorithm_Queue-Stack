from collections import deque


class Solution:
    def countStudents(students, sandwiches):
        # use deque
        dst = deque(students)
        dsa = deque(sandwiches)
        count = 0  # taking a counter to count uneaten students.
        while count < len(dst):
            if dst[0] == dsa[0]:
                dsa.popleft()
                dst.popleft()
                count = 0
            else:
                dst.append(dst.popleft())
                count += 1

        return len(dst)


students = [1, 1, 1, 0, 0, 1]
sandwiches = [1, 0, 0, 0, 1, 1]
print(Solution.countStudents(students, sandwiches))
