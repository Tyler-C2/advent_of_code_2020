import re

def read_file(file):
    passport = []
    count = 0
    lst_gen = True
    with open(file) as f:
        for line in f:
            line = line.strip()
            if line != '':
                if lst_gen == False:
                    temp_x = line.split()
                    for i in temp_x: 
                        passport[count].append(i)
                else:
                    temp_y = line.split()
                    passport.append(temp_y)
                    lst_gen = False
            else:
                count += 1
                lst_gen = True
    return passport

def make_dict(lst):
    dict = {}
    for item in lst:
        x = item.split(":")
        dict[x[0]] = x[1]
    return dict

def value_validation(dict):
    count = 0
    if int(dict["byr"]) >= 1920 and int(dict["byr"]) <= 2002:
        count += 1

    if int(dict["iyr"]) >= 2010 and int(dict["iyr"]) <= 2020:
        count += 1

    if int(dict["eyr"]) >= 2020 and int(dict["eyr"]) <= 2030:
        count += 1

    inch = re.search(r"\d{2,3}in", dict["hgt"])
    cent = re.search(r"\d{2,3}cm", dict["hgt"])
    if inch != None: 
        str_num = re.search(r"\d{2,3}",dict["hgt"])
        num = int(str_num.group(0))
        if num >= 59 and num <= 76:
            count += 1
    if cent != None:
        str_num = re.search(r"\d{2,3}",dict["hgt"])
        num = int(str_num.group(0))
        if num >= 150 and num <= 193:
            count += 1
    
    hair = re.search(r"^#[0-9a-f]{6}$",dict["hcl"])
    if hair != None:
        count += 1

    eye_colors = ("amb", "blu", "brn", "gry", "grn", "hzl", "oth")
    if dict["ecl"] in eye_colors:
        count += 1

    id_num = re.search(r"^\d{9}$", dict["pid"])
    if id_num != None:
        count += 1

    if count == 7:
        return True
    else: 
        return False

def check(lst):
    is_valid = 0
    for dict in lst:
        if "cid" in dict:
            dict.pop("cid")        
        if len(dict) == 7:
            content_check = value_validation(dict)
            if content_check == True:
                is_valid += 1
                content_check = False
    return is_valid

def main():
    passports = read_file("passport.txt")
    for i in passports:
        passports[passports.index(i)] = make_dict(i)
    print(check(passports))



main()



