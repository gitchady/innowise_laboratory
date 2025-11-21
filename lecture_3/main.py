students = {}
inp = ''
while True:
    print('--------------')
    print('1. Add a new student')
    print('2. Add a grades for a student')
    print('3. Show report (all students)')
    print('4. Find top performer')
    print('5. Exit')
    print('--------------')
    try:
        inp = input('Choose a variant: ')
    except:
        print('Invalid syntax')
    if inp == 'Exit':
        break
    match inp:
        case '1':
            new_student = input('Enter your name: ')
            if new_student in students:
                print("it's a old student")
            else:
                students.update({new_student:[]})
                
        case '2':
            variant = input('Choose a name student: ')
            for i in students:
                if variant == i:
                    new_degree = input('Enter a new degree (0-100) and enter "done" when you finish: ')

                    while True:
                        try:
                            if new_degree == 'done':
                                break
                            elif 0<=int(new_degree)<=100:
                                students[variant].append(int(new_degree))
                                new_degree = input('Enter a new degree (0-100) and enter "done" when you finish: ')
                            else:
                                new_degree = input('Enter a new degree (0-100) and enter "done" when you finish: ')
                        except:
                            print('uncorrect value')
                            new_degree = input('Enter a new degree (0-100) and enter "done" when you finish: ')

                else:
                    print('Student not find')
        case '3':
            print('------Student Report-------')
            if len(students)>0:
                for i in students:
                    try:
                        print(f'{i} average grade is {sum(students[i])/len(students[i]):.2f}')
                    except ZeroDivisionError:
                        print('students has zero grade')
            else:
                print('not find student')
        
        case '4':
            if not students:
                print('not find student')
                continue
            name, grades = max(
                students.items(),
                key=lambda item: sum(item[1]) / len(item[1])
            )
            avg = sum(grades) / len(grades)
            print(f'The student with the highest average is {name} with {avg:.2f}')


        case '5':
            break


