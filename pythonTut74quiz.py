user_input = int(input(' Please enter how many items you want: '))
user_choice = int(input('press\n'
                         '1 for List Comprehension\n'
                         '2 for Dictionary Comprehension\n'
                         '3 for Set Comprehension\n'))

if user_choice == 1:
    list1 = [i for i in range(user_input)]
    print(list1)

if user_choice == 2:
    dict1 = {i:f"item{i}" for i in range(user_input)}
    print(dict1)

if user_choice == 3:
    set1 = {i for i in range(user_input)}
    print(set1)