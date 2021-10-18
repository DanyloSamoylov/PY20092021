
all_countries = {}


def make_country(**kwargs):
    if kwargs.get('country', '').isdigit():
        print('Please dont use numbers.')
    else:
        all_countries.update({country: capital})
        print(all_countries)


for i in range(3):
    make_country(country=input('Enter name of the country:'), capital=input('Enter capital:'))


