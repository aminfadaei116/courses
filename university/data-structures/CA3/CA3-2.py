import collections
import operator
def main():
    inputcode = ((input().split()))
    code=((list(map(int, input().split()))))
    size=int(inputcode[0])
    length=int(inputcode[1])
    print(bank(code,length,size))


def bank(code,length,size):
    helper=buid(size,length)
    res=0
    last=0
    first=-length+1
    rang=0
    for i in range(size):
        test=((3-((code[i]+rang)%3))*(((code[i]+rang)%3)>0))
        helper[i]=test
        res+=test
        rang+=helper[last]
        rang-=helper[first]
        first+=1
        last+=1
    return res

def buid(size,length):
    helper=[]
    for i in range (size+length-1):
        helper.append(0)
    return helper




if __name__ == '__main__':
    main()
