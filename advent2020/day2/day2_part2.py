
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
        temp_dict["pos1"] = int(item1[0])-1
        temp_dict["pos2"] = int(item1[1])-1

        item2 = lst[1].replace(":", "")
        temp_dict["char"] = item2

        item3 = lst[2].replace("\n", "")
        temp_dict["phrase"] = item3

        return(temp_dict)
        
def check_if_valid(dict):
    count = 0
    y = dict["phrase"]
    pos1_char = dict["phrase"][dict["pos1"]]
    pos2_char = dict["phrase"][dict["pos2"]]
    if pos1_char == pos2_char:
        return False
    else:
        if pos1_char == dict["char"]:
            return True
        elif pos2_char == dict["char"]:
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