
def main():

    number = int(input())
    tower_height =(list(map(int, input().split())))
    max1=tower(tower_height,number)
    tower_height.reverse()
    max2=tower(tower_height,number)
    max2.reverse()
    res=[]
    for i in range(number):
        if(max1[i]>max2[i]):
            res.append(max1[i])
        else:
            res.append(max2[i])
    print(*res)




def tower(tower_height,number):
    max=[0]
    top=0
    s=[tower_height[0]]
    numberlist=[0]
    for i in range(1,number):
        if (s[top] > tower_height[i]):
            max.append(i-numberlist[top])
            top+=1

            s.append(tower_height[i])
            numberlist.append(i)

        else:
            dumy=0
            for j in range(top,-1,-1):

                if(s[j]<=tower_height[i]):
                    s.pop()
                    dumy=numberlist.pop()
                    top-=1
                else:
                    s.append(tower_height[i])
                    numberlist.append(i)
                    top+=1
                    break
            if len(s)==0:
                s.append(tower_height[i])
                numberlist.append(i)
                top += 1


            max.append((i-numberlist[top-1])*int(len(s)!=1)+i*int(len(s)==1))
    return max


if __name__ == '__main__':
    main()
