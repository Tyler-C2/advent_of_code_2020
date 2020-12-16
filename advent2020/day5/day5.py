

def read_file(file):
    with open(file) as f:
        data = f.read().split()
        return data

def decode(str):
    count_section,count_row = 0, 7
    section = [num for num in range(0,128)]
    row = [num for num in range(0,8)]
    low_section, low_row = 0, 0
    high_section, high_row = len(section)-1, len(row)-1

    while count_section < 6:
        center = (low_section + high_section) // 2
        if str[count_section] == "F":
            high_section = center - 1
            del section[section.index(center)+1:]
            count_section += 1
        elif str[count_section] == "B":
            low_section = center + 1
            del section[:section.index(center)+1]
            count_section += 1
    final_section = str[count_section]
    if final_section == "F":
        ticket_section = min(section)
    else:
        ticket_section = max(section)
    
    while count_row < 9:
        center = (low_row + high_row) // 2
        if str[count_row] == "L":
            high_row = center - 1
            del row[row.index(center)+1:]
            count_row += 1 
        elif str[count_row] == "R":
            low_row = center + 1
            del row[:row.index(center)+1]
            count_row += 1
    final_row = str[count_row]
    if final_row == "L":
        ticket_seat = min(row)
    else:
        ticket_seat = max(row)

    return (ticket_section * 8) + ticket_seat
   
def find_seat(lst):
    lst.sort()
    running_num = 15
    for num in lst:
        if num != running_num:
            return running_num
        else:
            running_num += 1
    


def main():
    seat_lst = []
    data = read_file("boarding.txt")
    for i in data:
        seatID = decode(i)
        seat_lst.append(seatID)
    return find_seat(seat_lst)

print(main())



