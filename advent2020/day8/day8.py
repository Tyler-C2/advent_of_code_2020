import copy

accumulator = 0
first_pass = True

def load_file(file):
    count = 1
    dict = {}
    with open(file) as f:
        for line in f:
            temp_split = line.strip().split(" ")
            lst = [temp_split[0], int(temp_split[1])]
            dict.update({count:lst})
            count += 1
    return dict

def find_loop(dict):
    global accumulator
    global first_pass
    count = 1
    run_instructions = []
    length = len(dict)
    while True:
        if count > length:
            one_loop = True
            break
        current = dict[count]
        if count in run_instructions:
            one_loop = False
            break
        else:
            run_instructions.append(count)
            if current[0] == "nop":
                count += 1
            elif current[0] == "jmp":
                count = count + current[1]
            elif current[0] == "acc":
                accumulator += current[1]
                count += 1 

    if first_pass == True:
        first_pass = False
        accumulator = 0
        return run_instructions
    else:
        return (accumulator, one_loop)

def fix_loop(lst, o_dict):
    global accumulator
    for item in lst:
        temp_dict = copy.deepcopy(o_dict)
        if o_dict[item][0] == "nop":
            temp_dict[item][0] = "jmp"
            fix_test = find_loop(temp_dict)
        elif o_dict[item][0] == "jmp":
            temp_dict[item][0] = "nop"
            fix_test = find_loop(temp_dict)
        if fix_test[1] == True:
            return fix_test[0]
        else:
            accumulator = 0 

def main():
    instructions = load_file("instruction.txt")
    loop = find_loop(instructions)
    accum_fixed = fix_loop(loop, instructions)
    return accum_fixed
    
print(main())