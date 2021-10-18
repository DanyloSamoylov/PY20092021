import json
import os.path

i = 0
while i < 1:
    if os.path.isfile("phonebook_data.json"):
        print('We found phonebook data')
        break
    else:
        user_test = {"1234567890": {"name": "test_name",
                                    "lastname": "test_lastname",
                                    "city": "test_city"}}
        with open('phonebook_data.json', 'a') as file:
            json.dump(user_test, file, indent=2)
            print('file created')
            i += 1
