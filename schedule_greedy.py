from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

class Teacher:

    def __init__(self, first_name, last_name, age, email, can_teach_subjects):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.can_teach_subjects = can_teach_subjects
        self.assigned_subjects = set()

    def __repr__(self):
        return f"{self.first_name} {self.last_name}"


def create_schedule(subjects, teachers):
    covered_subjects = set()
    schedule = []

    while subjects - covered_subjects:
        # Find the teacher who can cover the most uncovered subjects
        best_teacher = None
        max_covered = 0

        for teacher in teachers:
            if teacher not in schedule:
                # Calculate the number of uncovered subjects this teacher can cover
                can_cover = teacher.can_teach_subjects & (subjects - covered_subjects)
                if len(can_cover) > max_covered or (len(can_cover) == max_covered and (best_teacher is None or teacher.age < best_teacher.age)):
                    best_teacher = teacher
                    max_covered = len(can_cover)

        if not best_teacher:
            # No teacher can cover the remaining subjects
            return None

        # Assign the subjects to the best teacher
        best_teacher.assigned_subjects = best_teacher.can_teach_subjects & (subjects - covered_subjects)
        covered_subjects.update(best_teacher.assigned_subjects)
        schedule.append(best_teacher)

    return schedule


if __name__ == '__main__':
    # Set of subjects
    subjects = {'Mathematics', 'Physics', 'Chemistry', 'Informatics', 'Biology'}

    # List of teachers
    teachers = [
        Teacher('Alexander', 'Ivanenko', 45, 'a.ivanenko@example.com', {'Mathematics', 'Physics'}),
        Teacher('Maria', 'Petrenko', 38, 'm.petrenko@example.com', {'Chemistry'}),
        Teacher('Sergey', 'Kovalenko', 50, 's.kovalenko@example.com', {'Informatics', 'Mathematics'}),
        Teacher('Natalia', 'Shevchenko', 29, 'n.shevchenko@example.com', {'Biology', 'Chemistry'}),
        Teacher('Dmitry', 'Bondarenko', 35, 'd.bondarenko@example.com', {'Physics', 'Informatics'}),
        Teacher('Elena', 'Grytsenko', 42, 'e.grytsenko@example.com', {'Biology'})
    ]

    # Create the schedule
    schedule = create_schedule(subjects, teachers)

    # Print the schedule
    if schedule:
        print(f"{Fore.GREEN}Class Schedule:")
        for teacher in schedule:
            print(f"{Fore.BLUE}{teacher.first_name} {teacher.last_name}, {teacher.age} years, email: {teacher.email}")
            print(f"{Fore.YELLOW}   Teaches subjects: {', '.join(teacher.assigned_subjects)}\n")
    else:
        print(f"{Fore.RED}Unable to cover all subjects with the available teachers.")