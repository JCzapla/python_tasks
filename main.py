import numpy as np


def first_task(first_postal, second_postal):
    begin, start    = map(int, first_postal.split('-'))
    second_numbers  = second_postal.split('-')
    final_numbers   = []
    stop            = 1000
    end             = int(second_numbers[0])

    for x in range(begin, end + 1):
        if x == end:
            stop = int(second_numbers[1])
        for y in range(start + 1, stop):
            final_numbers.append(str(x) + '-' + str(y))
        start = 100

    return final_numbers


def second_task(my_list, n):
    full_list = [x for x in range(1, n + 1)]
    return list(set(my_list) ^ set(full_list))


def third_task(begin, end):
    numbers = []
    for x in np.arange(begin, end, 0.5):
        numbers.append(x)
    return numbers


def main():
    postal_codes = first_task('83-400', '83-600')
    #print(postal_codes)
    missing_numbers = second_task([2,3,7,4,9], 10)
    #print(missing_numbers)
    decimal_numbers = third_task(2.0, 6.0)
    print(decimal_numbers)


if __name__ == "__main__":
    main()
