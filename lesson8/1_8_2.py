
all_countries = {}


def make_country(country_name, capital):
    if country_name.isdigit() and capital.isdigit():
        print('Please dont use numbers.')
    else:
        all_countries.update({country_name: capital})
        print(all_countries)


for i in range(3):
    make_country(input('Enter name of the country:'), input('Enter capital:'))


