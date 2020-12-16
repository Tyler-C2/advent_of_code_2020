
import re 

bags_in_gold = 0
parent_list = []

def load_file(file):
    with open(file) as f:
        return [line.strip() for line in f]

def sort_to_dict(str):
    main_dict = {}
    temp_lst = []
    break_on_contain = re.search(r"contain", str)
    first_part = str[:break_on_contain.start()].strip()
    second_part = str[break_on_contain.end():].strip()

    second_part = second_part.replace(".","")
    temp_first = first_part.split()
    first_part = " ".join(temp_first[0:2])

    if second_part == "no other bags":
        main_dict.update({first_part:[("no other bags", "no")]})
    else:
        split_second = second_part.split(",")
        for rule in split_second:
            temp_split = rule.split()
            temp_lst.append((" ".join(temp_split[1:3]),int(temp_split[0])))
        main_dict.update({first_part:temp_lst})
    return main_dict

def find_outter_bag(dict, bag_color):
    bag_containing_gold = []
    for key in dict:
        if key != bag_color:
            value = dict[key]
            for tup in value:    
                if bag_color == tup[0]:
                    bag_containing_gold.append(key)
    for i in bag_containing_gold:
        for key in dict:
            if key != bag_color:
                value = dict[key]
                for tup in value:
                    if i == tup[0]:
                        if key not in bag_containing_gold:
                            bag_containing_gold.append(key)
    return len(bag_containing_gold)

def bag_in_bag(bag_color,rule_list,numbags):
    global bags_in_gold
    temp_parent = []
    color_count = 0
    for rule in rule_list:
        if rule == bag_color:
            nextbag = rule
            for child in rule_list[rule]:
                if child[1] != 'no':
                    parent_list.append(nextbag)
                    color_count = int(child[1])*int(numbags)
                    new_rule = (child[0],color_count)
                    temp_parent.append(new_rule)
                    bags_in_gold += (color_count)
    for item in temp_parent:
        bag_in_bag(item[0],rule_list,item[1])

def main():
    bag_color = "shiny gold"
    bag_dict = {}
    bag_rule = load_file("bags.txt")
    for str in bag_rule:
        bag_dict.update(sort_to_dict(str))
    bag_dict.update(sort_to_dict(str))
    outter_count = find_outter_bag(bag_dict, bag_color)
    bag_in_bag(bag_color,bag_dict,1)
    print(outter_count)
    print (bags_in_gold)

main()