if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    new_list=[]
    new_list_of_list=[new_list.append([x1,y1,z1]) for x1 in range(x+1) for y1 in range(y+1) for z1 in range(z+1) if x1+y1+z1 != n]
    print(new_list)
