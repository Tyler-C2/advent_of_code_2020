
lst_of_nums = []

def loader():
    expense_lst = []
    with open("expense_report.txt") as report:
        for line in report:
            expense_lst.append(int(line))
    return expense_lst

def search(lst):
    length = len(lst)-1
    for i in lst:
        count = 0
        while count <= length:
            if count+1 >= length:
                break
            next = lst[count+1]
            is_search_over = sum_of_two_and_search(i, next, lst)
            
            if is_search_over == True:
                return mult_lst(lst_of_nums)
            
            count += 1

    return mult_lst(lst_of_nums)

def sum_of_two_and_search(num1, num2, lst):
    sum = num1 + num2
    dif = 2020 - sum
    for i in lst:
        if i == dif:
            lst_of_nums.append(num1) 
            lst_of_nums.append(num2)
            lst_of_nums.append(i)
            return True

def mult_lst(lst):
    final_lst = list(set(lst))
    product = 1
    for i in lst:
        product *= i 
    return product


def main():
    l = loader()
    print(search(l))

main()


