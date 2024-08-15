import time
from threading import Thread


def func_gen_dec(text='Функция работала'):
    def time_track(func):
        def surrogate(*args, **kwargs):
            started_at = time.time()

            result = func(*args, **kwargs)

            ended_at = time.time()
            elapsed = round(ended_at - started_at, 4)
            print(f'{text} {elapsed} секунд(ы)')
            return result
        return surrogate
    return time_track


time_track_one = func_gen_dec('Однопоточное заполнение работало')
time_track_multi = func_gen_dec('Многопоточное заполнение работало')


def write_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        for i in range(word_count):
            file.write(f'Какое-то слово № {i+1}\n')
    print(f'Завершилась запись в файл {file_name}')


@time_track_one
def write_one_stream():
    write_words(10, 'example1.txt')
    write_words(30, 'example2.txt')
    write_words(200, 'example3.txt')
    write_words(100, 'example4.txt')


@time_track_multi
def write_multi_stream():
    thr_1 = Thread(target=write_words, args=(10, 'example5.txt'))
    thr_2 = Thread(target=write_words, args=(30, 'example6.txt'))
    thr_3 = Thread(target=write_words, args=(200, 'example7.txt'))
    thr_4 = Thread(target=write_words, args=(100, 'example8.txt'))

    thr_1.start()
    thr_2.start()
    thr_3.start()
    thr_4.start()

    thr_1.join()
    thr_2.join()
    thr_3.join()
    thr_4.join()


write_one_stream()
write_multi_stream()
