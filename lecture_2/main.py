def generate_profile(age):
    if 0<=age<=12:
        return 'Child'
    elif 13<=age<=19:
        return 'Teenager'
    elif 20<=age:
        return 'Adult'
    
user_name = input('Enter your full name: ')
birth_year_str = input('Enter your birth year: ')
birth_year = int(birth_year_str)
current_age = 2025 - birth_year
hobbies = []
choose = ''
while True:
    choose = input("Enter a favourite hobby or type 'stop' to finish: ")
    if choose == 'stop':
        break
    else:
        hobbies.append(choose)

life_stage = generate_profile(current_age)
user_profile={'user_name': user_name, 'birth_year_str': birth_year, 'life_stage':life_stage, 'hobbies':hobbies}

print()
print('--------------')
print('Profile Summary:')
for i,z in user_profile.items():
    if i == 'hobbies':
        if len(z)==0:
            print("You didn't mention any hobbies.")
        else:
            for b in z:
                print(f'- {b}')
    else:
        print(f'{i}: {z}')


print('--------------')