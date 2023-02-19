

def main():
	n=int(input())
	moveTower(n,"A","C","B")


def moveTower(height,fromPole, toPole, withPole):
    if height >= 1:
        moveTower(height-1,fromPole,withPole,toPole)
        moveDisk(fromPole,toPole)
        moveTower(height-1,withPole,toPole,fromPole)

def moveDisk(fp,tp):
    print(fp,tp)


if __name__ == '__main__':
    main()
    