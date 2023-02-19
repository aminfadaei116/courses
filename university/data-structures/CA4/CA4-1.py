import heapq
def main():
    incode = input().split()
    N = int(incode[0])
    T = int(incode[1])
    gold = [-1 * int(i) for i in input().split()]
    gold_sorted = (sorted(gold))
    easy = []
    sums = 0


    for i in range(N):
        easy.append(gold_sorted[i])
        
    heapq.heapify(easy)
    for i in range(T):
        k = heapq.heappop(easy)
        sums=sums+k
        heapq.heappush(easy,int(k/2))
    print(-sums)




if __name__ == '__main__':
    main()






