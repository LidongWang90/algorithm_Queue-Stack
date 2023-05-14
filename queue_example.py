from collections import deque


class Solution:
    def countStudents(students, sandwiches):
        # use deque:
        # dst = deque(students)
        # dsa = deque(sandwiches)
        # count = 0  # taking a counter to count uneaten students.
        # while count < len(dst):
        #     if dst[0] == dsa[0]:
        #         dsa.popleft()
        #         dst.popleft()
        #         count = 0
        #     else:
        #         dst.append(dst.popleft())
        #         count += 1

        # return len(dst)

        # without deque:
        count = 0
        while count < len(students):
            if students[0] == sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
                count = 0
            else:
                students.append(students.pop(0))
                count += 1
        return len(students)


students = [1, 1, 1, 0, 0, 1]
sandwiches = [1, 0, 0, 0, 1, 1]
print(Solution.countStudents(students, sandwiches))
