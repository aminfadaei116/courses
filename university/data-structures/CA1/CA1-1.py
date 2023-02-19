

def main():

	x=[]
	maxnum=-63 # the max cant be more that -9*6

	for __ in range(6):

	    x.append(list(map(int, input().split(' '))))

	for i in range(4):

	    for j in range(4):

	        tempt=x[i][j]+x[i][j+1]+x[i][j+2]+x[i+1][j+1]+x[i+2][j]+x[i+2][j+1]+x[i+2][j+2]
	        maxnum=max(tempt,maxnum) # evert time it compairs it self with the past amount of max
    
	print(maxnum)


if __name__ == '__main__':
    main()
