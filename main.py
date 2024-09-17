def calculate_class_averages(classrooms):
    class_averages = {}

    for classroom, students in classrooms.items():
        if not students: 
            class_averages[classroom] = 0
            continue

        scores = 0 
        num_grades = 0

        for grades in students.values():
            for grade in grades:
                scores += grade
                num_grades += 1

        average = scores / num_grades
        class_averages[classroom] = average

    return class_averages