import random

def merge_sort(array):

    if len(array) <= 1:
        return array

    midpoint = int(len(array) / 2)

    left, right = merge_sort(array[:midpoint]), merge_sort(array[midpoint:])

    return merge(left, right)


def merge(left, right):

    result = []
    left_pointer = right_pointer = 0

    while left_pointer < len(left) and right_pointer < len(right):

        if len(left[left_pointer]) < len(right[right_pointer]):

            result.append(left[left_pointer])
            left_pointer += 1

        else:

            result.append(right[right_pointer])
            right_pointer += 1

    result.extend(left[left_pointer:])
    result.extend(right[right_pointer:])

    return result

def pickWord(worldLen_int):
    indexStart = 0

    with open("words.txt", "r") as file:
        words_str = file.readlines()
        
        for i, word_str in enumerate(words_str):
            if len(word_str) - 1 == worldLen_int:
                indexStart = i + 1
                break
    
        return(words_str[random.randint(indexStart, len(words_str))])



def main():
    print(pickWord(5))

    # final_list = []


    # with open("words.txt", "r") as file:
    #     words_str = file.readlines()
    #     final_list = merge_sort(words_str)

    # with open("words.txt", "w") as file:
    #     for line in final_list:
    #         file.write(line)
        
                
if __name__ == "__main__":
    main()