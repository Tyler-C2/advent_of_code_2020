
def read_file(file):
    with open(file) as f:
        data = f.read().split()
        return data

def detect_trees(data, right, down):
    pos = 0
    trees = 0
    first_row = True
    for line in data[::down]:
        line = line * 100
        if pos != 0:
            char = line[:pos][-1]
        if first_row == True:
            pos += right+1
            first_row = False
        else:
            pos += right
            if char == "#":
                trees += 1
    print(f"Num of trees: {trees}")
    return trees


def main():
    product = 1
    sets = [(1,1), (3,1),(5,1),(7,1),(1,2)]
    lst = read_file("map.txt")
    for tup in sets:
        path = detect_trees(lst, tup[0], tup[1])
        product *= path
    print(product)

main()