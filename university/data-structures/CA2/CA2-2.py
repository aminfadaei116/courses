def main():
    capacity,number = input().split()
    price=list(map(int,input().split(' ')))
    weight=list(map(int,input().split(' ')))

    if number==0:
        print(0)
    else:
        print(findbest(int(capacity), price, weight, int(number)))


def findbest(capacity, price, weight, num):

    if  num == 1 :
            return ( capacity >= weight[0] ) * price[0]

    if weight[num-1] > capacity:
        return findbest(capacity,price[:num-1], weight[:num-1], num-1)


    return max(findbest(capacity-weight[num-1],price[:num-1],weight[:num-1],num-1)+price[num-1],
        findbest(capacity, price[:num-1], weight[:num-1], num-1))


if __name__ == '__main__':
    main()
