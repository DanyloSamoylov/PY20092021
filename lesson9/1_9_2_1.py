import json


def create_json():
    with open("/home/dany/Projects/my_project/lesson9/1_9_2_2.py", "r") as f:
        exec(f.read())


create_json()


def menu_():
    print('1. Print Phonebook')
    print('2. Add a Phone Number')
    print('3. Remove a phone Number')
    print('4. Search and Update info')
    print('5. Quit')
    print('-----------------------------------------------------------------------------')


menu_choice = 0
menu_()
while menu_choice != 5:
    menu_choice = int(input('Type in a number (1-5): '))
    if menu_choice == 1:
        with open('phonebook_data.json', 'r') as file:
            data = json.load(file)
            print('Telephone Numbers:')
            for key in data:
                print(key, data[key])

        print('-------------------------------------------------------------------------------')
    elif menu_choice == 2:
        print('Add Name, Lastname, telephone and city.')
        user_name = input('Name: ')
        user_lastname = input('Lastname: ')
        telephone = input('Number: ')
        user_city = input('City: ')
        user_info = {telephone: {"name": user_name,
                                 "lastname": user_lastname,
                                 "city": user_city}}
        with open('phonebook_data.json', 'r') as file:
            data = json.load(file)
            data.update(user_info)
        with open('phonebook_data.json', 'w') as file:
            json.dump(data, file, indent=2)
            print('--------------------------------------------------------------------------')
    elif menu_choice == 3:
        print('Remove by telephone number')
        user_info = input('Please enter telephone number: ')
        with open('phonebook_data.json', 'r') as file_secure:
            data = json.load(file_secure)
            for key in data:
                if key == user_info:
                    print(key, data[key])
                    print(f'Telephone: {key}, we have this data {data[key]}')
                    del_question = input('Do you want to delete this data? Type yes/no:')
                    if del_question == "yes":
                        del data[key]
                        with open('phonebook_data.json', 'w') as file:
                            json.dump(data, file, indent=2)
                    elif del_question == "no":
                        menu_()
                    else:
                        menu_()
            print('--------------------------------------------------------------------------')
    elif menu_choice == 4:
        print('Search for info')
        any_info = input('Any info: ')
        with open('phonebook_data.json', 'r') as file_secure:
            data = json.load(file_secure)
            for key in data:
                if key == any_info:
                    search_info = data[key]
                    print(f'For telephone: {any_info}, we have this data.')
                    for k, v in search_info.items():
                        print(k, ':', v)
                else:
                    for k, v in data.items():
                        if any_info == v:
                            print(f'For telephone: {any_info}, we have this data.', v)

                # else:
                #     print(any_info, 'was not found')
            print('--------------------------------------------------------------------------')
    elif menu_choice != 5:
        menu_()
