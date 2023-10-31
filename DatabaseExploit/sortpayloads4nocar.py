from PR import PRIORITY
import os
from itertools import islice

IMPORTANT_ONE_NOT_SPEC_CA = []

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
            if i.startswith("#"):
                pass
            elif i.startswith('/'):
                pass
            elif i.startswith(","):
                pass
            elif i.startswith("."):
                pass
            elif i.startswith(";"):
                pass
            elif i.startswith(":"):
                pass
            elif i.startswith("-"):
                pass
            elif i.startswith("_"):
                pass
            elif i.startswith("["):
                pass
            elif i.startswith("]"):
                pass
            elif i.startswith("{"):
                pass
            elif i.startswith("}"):
                pass
            elif i.startswith("("):
                pass
            elif i.startswith(")"):
                pass
            elif i.startswith("*"):
                pass
            elif i.startswith("`"):
                pass
            elif i.startswith("~"):
                pass
            else:        
                IMPORTANT_ONE_NOT_SPEC_CA.append(i)
        
        return IMPORTANT_ONE_NOT_SPEC_CA,True
    
    except KeyboardInterrupt:
        print("Aborted")
    
    except IndexError:
        pass
    



print(SORT_IMPORTANT_ONE(98765678))
print(IMPORTANT_ONE_NOT_SPEC_CA)
            
