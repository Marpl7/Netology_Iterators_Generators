import json
import unidecode
import hashlib


class CountryIterator:
    def __init__(self, file_name):
        with open(file_name, 'r', encoding="utf-8") as f:
            self.data = json.load(f)
        self.i = 0


    def __iter__(self):
        return self

    def __next__(self):
        try:
            country = unidecode.unidecode(self.data[self.i]['name']['common'])
            url = ('https://en.wikipedia.org/wiki/' + country.replace(' ', '_'))
            self.i += 1
            return country, url
        except IndexError:
            raise StopIteration()

def Md5Generator(path):

    with open(path, 'rb') as f:
        while True:
            line = f.readline()
            yield hashlib.md5(line)
            if not line:
                break


if __name__ == '__main__':

    with open('country_url.txt', 'w') as file:
        for country, url in CountryIterator('countries.json'):
            file.write(str(country) + ': ' + str(url) + '\n')

    for item in Md5Generator('country_url.txt'):
        print(item)
