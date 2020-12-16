
def read_file(file):
    with open(file) as f:
        group = []
        count = 0
        lst_gen = True
        for line in f:
            line = line.strip()
            if line != '':
                if lst_gen == False:
                    temp_x = line.split()
                    for i in temp_x: 
                        group[count].append(i)
                else:
                    temp_y = line.split()
                    group.append(temp_y)
                    lst_gen = False
            else:
                count += 1
                lst_gen = True
    return group

def num_of_yes(lst):
    alph_dict = {"a": 0,"b": 0,"c": 0,"d": 0,"e": 0,"f": 0,"g": 0,"h": 0,"i": 0,"j": 0,"k": 0,"l": 0,"m": 0,
                "n": 0,"o": 0,"p": 0,"q": 0,"r": 0,"s": 0,"t": 0,"u": 0,"v": 0, "w": 0,"x": 0,"y":0,"z": 0}
    count = 0
    length = len(lst)
    for str in lst:
        for char in str:
            alph_dict[char] += 1 
    for key in alph_dict:
        if alph_dict[key] == length:
            count += 1 
    return count

def main():
    group_yeses = []
    sum = 0
    lst_of_group_ans = read_file("customs_form.txt")
    for lst in lst_of_group_ans:
        yes = num_of_yes(lst)
        group_yeses.append(yes)
    for num in group_yeses:
        sum += num
    return sum

    
print(main())
