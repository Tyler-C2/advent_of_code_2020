def load_file(file):
    with open(file) as f:
        return [int(line.strip()) for line in f]
        

def find_weakness(lst, preamble_len):
    start = 0
    while True:
        does_equal = False
        search_lst = [lst[i] for i in range(start,preamble_len)]
        num_to_search = lst[preamble_len]
        for num in search_lst:
            if num >= num_to_search:
                search_lst.remove(num)
        for num in search_lst:
            for num2 in search_lst:
                if search_lst.index(num2)+1 <= len(search_lst)-1:
                    num2 = search_lst[search_lst.index(num2)+1]
                    if search_lst.index(num2) > search_lst.index(num):
                        if search_lst.index(num2) < preamble_len:
                            check = num + num2
                            if check == num_to_search:
                                start += 1
                                preamble_len += 1
                                does_equal = True
                                break
            if does_equal == True:
                break
            if does_equal == False and search_lst.index(num) == len(search_lst)-1:
                return num_to_search

def exploit(num, lst):
    total = 0
    nums_that_sum = []
    while total < num:
        for i in lst:
            total += i
            nums_that_sum.append(i)
            if total > num:
                break
            if total == num:
                return nums_that_sum
    lst.pop(0)            
    return exploit(num, lst)


def min_max(lst):
    lower = min(lst)
    higher = max(lst)
    return lower + higher


def main():
    lst_of_nums = load_file("number.txt")
    preamble_len = 25
    weak_num = find_weakness(lst_of_nums, preamble_len)
    exploit_values = exploit(weak_num, lst_of_nums)
    return min_max(exploit_values)

print(main())