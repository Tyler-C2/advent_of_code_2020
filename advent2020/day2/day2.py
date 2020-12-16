
def loader(): 
    with open("passwords.txt") as passwords:
        lst = []
        lst_of_dict = []
        for line in passwords:
            lst.append(line.split(" "))
        for i in lst:
            x = lst_to_dict(i)
            lst_of_dict.append(x)
        return lst_of_dict


def lst_to_dict(lst):
        temp_dict = {}

        item1 = lst[0].split("-")
        temp_dict["min"] = int(item1[0])
        temp_dict["max"] = int(item1[1])

        item2 = lst[1].replace(":", "")
        temp_dict["char"] = item2

        item3 = lst[2].replace("\n", "")
        temp_dict["phrase"] = item3

        return(temp_dict)
        
def check_if_valid(dict):
    count = 0
    for i in dict["phrase"]:
        if i == dict["char"]:
            count += 1
    if count >= dict["min"] and count <= dict["max"]:
        return True
        
    return False


def main():
    is_valid = 0
    ready_lst = loader()

    for dict in ready_lst:
        check = check_if_valid(dict)
        if check == True:
            is_valid += 1
    return is_valid


print(main())