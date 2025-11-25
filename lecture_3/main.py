def main():
    # Initialize an empty list to store all students
    students = []

    def new_student(students: list):
        """Add a new student to the system with validation"""
        while True:
            raw_name = input("Enter student's name: ").strip()
            try:
                # Validation: Check for empty input
                if not raw_name:
                    raise ValueError('Name cannot be empty.\n')

                # Validation: Check if name contains any digits
                if any(char.isdigit() for char in raw_name):
                    raise ValueError('The name must not contain numbers\n')

                # Validation: Check for punctuation and special characters
                forbidden_chars = set('!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~')
                if any(char in forbidden_chars for char in raw_name):
                    raise ValueError(
                        ' The name must not contain punctuation marks or special characters\n')

                # Normalize the name: Capitalize first letter of each word
                name = ''.join(word.capitalize() for word in raw_name.split())

                for student in students:
                    if name in student:
                        print(
                            f"Name '{name}' already exists. Choose another name.\n")
                        break
                else:
                    students.append({name: []})
                    print(f'{name} has been added.\n')
                    break

            except ValueError as e:
                print(f'Error: {e}')

    def add_grade(students: list):
        while True:
            raw_name = input("Enter student's name: ").strip()
            try:
                # Validation: Check for empty input
                if not raw_name:
                    raise ValueError('Name cannot be empty.\n')

                # Validation: Check if name contains any digits
                if any(char.isdigit() for char in raw_name):
                    raise ValueError('The name must not contain numbers\n')

                # Validation: Check for punctuation and special characters
                forbidden_chars = set('!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~')
                if any(char in forbidden_chars for char in raw_name):
                    raise ValueError(
                        ' The name must not contain punctuation marks or special characters\n')

                # Normalize the name: Capitalize first letter of each word
                name = ''.join(word.capitalize() for word in raw_name.split())

                student_found = None
                for student in students:
                    if name in student:
                        while True:
                            grade_input = input(
                                "Enter a grade or 'done' to finish ").strip().lower()
                            if grade_input == 'done':
                                return
                            try:
                                if any(char.isalpha() for char in grade_input):
                                    raise ValueError(
                                        'The name must not contain numbers\n')
                                if not grade_input.isdigit():
                                    raise ValueError(
                                        'The grade must be a number\n')
                                grade_val = int(grade_input)
                                if grade_val < 0 or grade_val > 100:
                                    raise ValueError(
                                        'Invalid input. Please enter a number between 0 and 100\n')
                                student[name].append(grade_val)

                            except ValueError as error:
                                print(error)

                        return

                else:
                    print('Student is not found')
                    return
            except ValueError as e:
                print(f'Error: {e}')

    def show_report(students: list):
        if not students:
            print("The list of students is empty.")
            return

        report_text = "--- Student Report ---\n"
        averages = []

        for student in students:
            for name, grades in student.items():
                try:
                    average_value = round(sum(grades) / len(grades), 1)
                    averages.append(average_value)
                except ZeroDivisionError:
                    average_value = "N/A"

                report_text += f"{name}'s average grade is {average_value}\n"

        report_text += "-" * 10

        if not averages:
            print("Students haven't grades")
            return

        max_avg = max(averages)
        min_avg = min(averages)
        overall_avg = round(sum(averages) / len(averages), 1)

        report_text += (
            f"\nMax average: {max_avg}"
            f"\nMin average: {min_avg}"
            f"\nOverall average: {overall_avg}"
        )

        print(report_text)

    def get_top_performer(students: list):
        if not students:
            print("The list of students is empty.")
            return

        # Filter students who have grades
        students_with_grades = []
        for student in students:
            name = list(student.keys())[0]
            grades = list(student.values())[0]
            if grades:  # Only include students with at least one grade
                students_with_grades.append((name, grades))

        if not students_with_grades:
            print("No students have grades yet.")
            return

        # Use max() with a lambda function to find the student with highest average
        top_student_info = max(students_with_grades,
                               key=lambda student_data: sum(student_data[1]) / len(student_data[1]))

        name, grades = top_student_info
        avg_grade = sum(grades) / len(grades)
        print(
            f"The student with the highest average is {name} with a grade of {round(avg_grade, 1)}")

    while True:
        try:
            # Display menu options
            print('1. Add a new student')
            print('2. Add a grades for a student')
            print('3. Show report(all students)')
            print('4. Find a top performer')
            print('5. Exit')

            choice = int(input('Enter option:'))

            if choice == 1:
                new_student(students)
            elif choice == 2:
                add_grade(students)
            elif choice == 3:
                show_report(students)
            elif choice == 4:
                get_top_performer(students)
            elif choice == 5:
                print('Exiting program...')
                break

        except Exception as e:
            print(f'ошибка {e}')


if __name__ == '__main__':
    main()
