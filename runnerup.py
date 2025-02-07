if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    numbered_list = list(arr)
    numbered_list.sort()
    j=0
    result = 0
    new_result=[]
    for i in range(len(numbered_list)):
        if(numbered_list[i]>numbered_list[j]):
            result = numbered_list[i]

    for i in range(len(numbered_list)):
        if numbered_list[i]<result:
            new_result.append(numbered_list[i])
    print(max(new_result))