import json


class WikiIter:
    wiki_link = 'en.wikipedia.org/wiki/'

    def __init__(self, data_list, filename):
        self.count = 0
        self.limit = len(data_list)
        self.data_list = data_list
        self.filename = filename

    def __iter__(self):
        return self

    def __next__(self):
        if self.count < self.limit:
            iter_dict = self.data_list[self.count]
            name = iter_dict['name']['common']
            link_name = self.wiki_link + name
            with open(self.filename,  'a') as f:
                f.write(f'{name}: {link_name}\n')
            self.count += 1
            return name
        else:
            raise StopIteration


if __name__ == '__main__':
    with open('countries.json') as countries_file:
        countries_list = json.load(countries_file)
    my_iterator = WikiIter(countries_list, 'datafile.txt')
    for country in my_iterator:
        print(f'{country} added')
