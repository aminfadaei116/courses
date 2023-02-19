

def main():
    n=input()
    my_list= (input().split(' '))
    print(str((find(my_list,None))))


def find (word, result):
    if  result == '':
        return "NULL"
    if word == []:
        return result
    if result == None:
        result = word.pop()
        return find(word,result)
    temp=word.pop()
    output=""
    for i in range(min(len(result),len(temp))):
        if temp[i] != result[i]:
            break
        output+=temp[i]
    return find(word,output)




if __name__ == '__main__':
    main()
    