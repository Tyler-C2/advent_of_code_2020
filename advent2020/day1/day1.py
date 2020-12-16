
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
            x = i + next
            if x == 2020:
               return i * lst[count+1]
            count += 1

def sum_of_two(num1,num2):
    pass
    
def main():
    l = loader()
    print(search(l))

main()
