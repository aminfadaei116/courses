from collections import deque

def main():

    books=(input().split('-'))
    n=int(input())
    case=int(input())

    if case==1:
        print(type1(books,n))
    if case==2:
        print(type2(books,n))
    if case==3:
        print(type3(books,n))

def type1(books,n):

    number_times=0
    local = deque([])

    for j in range(n):

        local.append(0)

    for j in range(len(books)):

        flag=0

        for i in range(n):

            if local[i]==0:

                local[i]=books[j]
                flag=1
                number_times+=1
                break

            if local[i]==books[j]:

                flag=1
                break

        if flag==0:

            number_times+=1
            local[0]=books[j]
            local.reverse()
            local.rotate()
            local.reverse()

    return number_times

def type2(books,n):
    local = deque([])
    number_times=0

    for j in range(n):

        local.append(0)

    for j in range(len(books)):

        flag=0

        for i in range(n):

            if local[i]==0:

                local[i]=books[j]
                flag=1
                number_times+=1
                break

            if local[i]==books[j]:

                flag=1
                break

        if flag==0:

            m=0
            temp=list(local)

            for m in range(j+1,len(books)):

                if len(temp)==1:

                    break

                if books[m] in temp:

                    del temp[temp.index(books[m])]

            if (j+1)!=len(books)-1:

                local[local.index(temp[0])]=books[j]

                number_times+=1

    return number_times

def type3(books,n):

    number_times=0
    local = deque([])

    for j in range(n):

        local.append(0)

    for j in range(len(books)):

        flag=0

        for i in range(n):

            if local[i]==0:

                local[i]=books[j]
                flag=1
                number_times+=1
                break

            if local[i]==books[j]:

                tempt=local[i]

                for k in range(i,n-1,1):

                    local[k]=local[k+1]

                local[n-1]=tempt
                flag=1
                break

        if flag==0:

            number_times+=1
            local[0]=books[j]
            local.reverse()
            local.rotate()
            local.reverse()

    return number_times




if __name__ == '__main__':
    main()

