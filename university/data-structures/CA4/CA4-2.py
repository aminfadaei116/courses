import heapq


def main():
    N = int(input())
    roomfather = [int(i) for i in input().split()]
    roomlight = [int(i) for i in input().split()]
    number = int(input())
    list=[0]
    for j in range(1,N+1,1):
        list.append(tree())
        list[j].condition = roomlight[j-1]


    for i in range(N-1):
        list[roomfather[i]].child.append(i+2)


    for i in range(number):
        mm = input().split()
        if mm[0] == "report":
            print(list[int(mm[1])].report(list))
        if mm[0] == "toggle":
            list[int(mm[1])].toggle(list)

class tree(object):
    def __init__(self):
        self.child = []
        self.condition = None
    def report(self, list):
        if not self.child:
            return self.condition
        sum = 0
        for i in range(len(self.child)):
            sum = sum+list[self.child[i]].report(list)
        return sum+self.condition
    def toggle(self,list):
        self.condition = int(not self.condition)
        for i in range(len(self.child)):
            list[self.child[i]].toggle(list)


if __name__ == '__main__':
    main()
