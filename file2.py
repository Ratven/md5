import hashlib


def md5_hash(any_file):
    with open(any_file) as datafile:
        for line in datafile:
            md5_string = hashlib.md5(b'{line}')
            final_string = md5_string.hexdigest()
            yield final_string


if __name__ == '__main__':
    generator = md5_hash('datafile.txt')
    for i in generator:
        print(i)
