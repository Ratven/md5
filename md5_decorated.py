import hashlib
import datetime

def decorator_with_file_path(filepath):
    def timing_decorator(function_to_decorate):
        def loger(*args, **kwargs):
            text = (
                f'DATE: {datetime.datetime.date(datetime.datetime.now())}\n'
                f'TIME: {datetime.datetime.time(datetime.datetime.now())}\n'
                f'NAME: {function_to_decorate.__name__}\n'
                f'ARGS: {args, kwargs}\n'
                f'RESULT: {function_to_decorate(*args, **kwargs)}\n\n'
            )
            with open(filepath, 'a', encoding='utf-8') as logfile:
                logfile.write(text)
        return loger
    return timing_decorator

@decorator_with_file_path('logfile.txt')
def md5_hash(any_file):
    with open(any_file) as datafile:
        for line in datafile:
            md5_string = hashlib.md5(line.encode())
            final_string = md5_string.hexdigest()
            yield final_string


if __name__ == '__main__':
    generator = md5_hash('datafile.txt')
    for i in generator:
        print(i)