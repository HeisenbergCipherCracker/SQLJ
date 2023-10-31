import os
from itertools import islice

def rockyou(count):
    filename = "rockyou.txt"
    current_directory = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_directory, filename)

    def row_generator():
        with open(file_path, "r", encoding="latin-1") as file:
            for row in file:
                yield row.strip()

    return row_generator()

def run_rockyou(cnt):
    word_generator = rockyou(1000000)

    # Slice the generator to get the first cnt words
    sliced_generator = islice(word_generator, cnt)

    word_list = list(sliced_generator)
    return word_list


print(run_rockyou(1000))