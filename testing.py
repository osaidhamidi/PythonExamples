import random
import string
import copy
import itertools
import time


# Python Program to Check Prime Number
def is_prime(n):
    if n == 1 or n == 2:
        return True
    flag = True
    for i in range(2, (n // 2) + 1):
        if n % i == 0:
            flag = False
            break

    return flag


# Python Program to Find the Factorial of a Number
def factorial(n):
    fact = 1
    for i in range(2, n + 1):
        fact *= i

    return fact


# Python Program to Print the Fibonacci sequence
def fib(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1

    prev = 0
    curr = 1

    for i in range(2, n + 1):
        temp = curr
        curr = prev + curr
        prev = temp

    return curr


# Python Program to Get the Class Name of an Instance
def get_class_name(obj):
    return type(obj).__name__


# Python Program to Generate a Random Number
def get_random_number():
    return random.choice(range(100))


# Python Program to Remove Punctuations From a String
def remove_punc(word):
    temp = ""
    for char in word:
        if char not in string.punctuation:
            temp += char

    return temp


# Python Program to Sort Words in Alphabetic Order
def sort_words(words):
    words.sort()


# Python Program to Merge Two Dictionaries
def merge_dicts(dict1, dict2):
    temp = dict1.copy()
    temp.update(dict2)

    return temp



# Python Program to Merge Two Lists and inverse the merged list
def merge_lists(list1, list2):
    temp = list1.copy()
    temp.extend(list2)
    temp.reverse()
    return temp



# Python Program to Remove Duplicate Element From a List
def remove_dup(list1):
    aux = []
    for item in list1:
        if item not in aux:
            aux.append(item)

    return aux


# Python Program to Convert Two Lists Into a Dictionary
def list_to_dict(list1, list2):
    return dict(zip(list1, list2))


# Python Program to Differentiate Between del, remove, and pop on a List
def remove_del_pop(list1):
    c2_list = c1_list = list1.copy()
    print('original :', list1)

    if len(list1) >= 4:
        list1.pop(3)
        print('after pop 4th element: ', list1)

    if len(c1_list) > 0:
        del c1_list[0]
        print('after deleting first element:', c1_list)

    if '2' in c2_list:
        c2_list.remove('2')
        print('after remove "2" value :', c2_list)



# Python Program to Delete an Element From a Dictionary if it exist
def del_from_dic(mydict, key):
    del mydict[key]


# Python Program to Make a Flattened List from Nested List
def flatten_list(list1):
    temp = []
    for item in list1:
        if isinstance(item, list):
            temp.extend(flatten_list(item))
        else:
            temp.append(item)
    return temp


# Python Program to Read and write to a file
def read_write_file(file_path):
    with open(file_path) as file:
        print(file.read())

    with open(file_path, 'w') as file:
        file.write('Hello from the other siiiiideee!!!')


# Python Program to Append to a File
def file_append(file_path):
    with open(file_path, 'a') as file:
        file.write("\nHelloo it's me\n")


# python Program to read user input and print it
def read_info():
    print(input('Enter anything to printed out: '))


# Python Program that uses built in operator with dictionary, list and tuple
def myoperators(list1, dict1, tuple1):
    print('list + operator: ', list1 + list1)
    print('repetition * operator: ', list1 * 3)
    dict2 = {'b': 3, 'c': 4}
    print('dict merging operator: ', dict1 | dict2)
    dict1 |= dict2
    print('adict update operator:', dict1)
    print('tuple + operator: ', tuple1 + tuple1)
    print('tuple * operator: ', tuple1 * 3)


# Python Program that calculates the difference in memory address in list objects
def memory_difference():
    list1 = [1, 4, 5, 5]
    list2 = [3, 4, 5, 6, 1]
    print('list1 id:', id(list1))
    print('list2 id:', id(list2))
    print(abs(id(list1) - id(list2)))


# Python Program to Shuffle Deck of Cards
def shuffle_card():
    deck = list(itertools.product(range(1, 14), ['hears', 'clubs', 'spades', 'diamonds']))
    random.shuffle(deck)

    print("shuffling.... ")
    time.sleep(2)
    print('result: ')
    for i in range(5):
        print(deck[i][0], "of", deck[i][1])


class A:
    pass


print("is_prime(17):", is_prime(17))
print("is_prime(4):", is_prime(4))


print("factorial(5):", factorial(5))


print("fib(10):", fib(10))


print("get_class_name(123):", get_class_name(123))
print("get_class_name('hello'):", get_class_name("hello"))


print("get_random_number():", get_random_number())


print("remove_punc('Hello, World!'):", remove_punc("Hello, World!"))


words = ["banana", "apple", "cherry"]
sort_words(words)
print("Sorted words:", words)


dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
print("merge_dicts(dict1, dict2):", merge_dicts(dict1, dict2))


list1 = [1, 2, 3]
list2 = [4, 5, 6]
print("merge_lists(list1, list2):", merge_lists(list1, list2))  # [6, 5, 4, 3, 2, 1]


print("remove_dup([1, 2, 2, 3, 4, 4]):", remove_dup([1, 2, 2, 3, 4, 4]))


keys = ["a", "b", "c"]
values = [1, 2, 3]
print("list_to_dict(keys, values):", list_to_dict(keys, values))


list3 = [1, 2, 3, 4, 5]
remove_del_pop(list3)


mydict = {"a": 1, "b": 2, "c": 3}
del_from_dic(mydict, "b")
print("After del_from_dic, mydict:", mydict)


mylist = [1, 2, 3, [[4, 5], 6, 7], 8, 9, 10]
print("flatten_list(mylist):", flatten_list(mylist))

try:
    file_path = "test_file.txt"
    read_write_file(file_path)
    file_append(file_path)

    with open(file_path) as file:
        print("Content of file after read_write_file and file_append:\n", file.read())

except:
    print("Invalid file name")

shuffle_card()


memory_difference()