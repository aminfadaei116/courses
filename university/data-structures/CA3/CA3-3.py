

def main():
    number = int(input())
    mine_number =(list(map(int, input().split())))
    ans=[]
    thismax=max(mine_number)
    zeros=[]
    for i in range(thismax+1):
        zeros.append(0)
    for i in range(number):
        zeros[mine_number[i]]+=1

    for i in range(number):
        ans.append(zeros[mine_number[i]])

    ans.reverse()

    mine_number.reverse()
    max1=biggest_min(ans,number,mine_number)
    max1.reverse()
    print(*max1)







def biggest_min(Mine,number,min_number):
    bigMin=[Mine[0]]
    minename=[min_number[0]]
    res=[]
    res.append(-1)
    top=0
    for i in range(1,number):
        if(Mine[i]<bigMin[top]):
            res.append(minename[top])
            minename.append(min_number[i])
            bigMin.append(Mine[i])
            top+=1
        else:
            for j in range(top,-1,-1):
                if(bigMin[j]<=Mine[i]):
                    bigMin.pop()
                    minename.pop()
                    top-=1
                    if(len(bigMin)==0):
                        bigMin.append(Mine[i])
                        minename.append(min_number[i])
                        top+=1
                        res.append(-1)
                elif(bigMin[j]>Mine[i]):
                    top+=1
                    bigMin.append(Mine[i])
                    minename.append(min_number[i])
                    res.append(minename[j])
                    break
    return res


if __name__ == '__main__':
    main()
