from PR import PRIORITY
import os
from itertools import islice

IMPORTANT_ONE_NOT_NUMBERS = []

def sort_important(count):
    filename = "rockyou.txt"
    current_directory = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_directory, filename)

    def row_generator():
        with open(file_path, "r", encoding="latin-1") as file:
            for row in file:
                yield row.strip()

    return row_generator()

def main_sort(cnt):
    word_generator = sort_important(1000000)

    # Slice the generator to get the first cnt words
    sliced_generator = islice(word_generator, cnt)

    word_list = list(sliced_generator)
    return word_list

def SORT_IMPORTANT_ONE(val):
    try:
        for i in main_sort(val):
            if i.startswith("1"):
                pass
            elif i.startswith("2"):
                pass
            elif i.startswith("3"):
                pass
            elif i.startswith("4"):
                pass
            elif i.startswith("5"):
                pass
            elif i.startswith("6"):
                pass
            elif i.startswith("7"):
                pass
            elif i.startswith("8"):
                pass
            elif i.startswith("9"):
                pass
            elif i.startswith("0"):
                pass
            else:        
                IMPORTANT_ONE_NOT_NUMBERS.append(i)
        
        return IMPORTANT_ONE_NOT_NUMBERS,True
    
    except KeyboardInterrupt:
        print("Aborted")
    
    except IndexError:
        pass
    



print(SORT_IMPORTANT_ONE(98765678))
print(IMPORTANT_ONE_NOT_NUMBERS)
            
