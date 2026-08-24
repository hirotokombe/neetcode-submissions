class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        students = deque(students)
        numStudents = len(students)
        for sandwich in sandwiches:
            cycle = 0
            while cycle < numStudents and students[0] != sandwich:
                students.append(students[0])
                students.popleft()
                cycle += 1


            if students[0] == sandwich:
                students.popleft()
                numStudents -= 1
                
            else:
                break
        return len(students)