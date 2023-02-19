

def main():
    inp_li = int(input())//4
    sentence = input()
    charlist=['A','C','T','G']
    res=0
    numA = sentence.count(charlist[0])-inp_li
    numC = sentence.count(charlist[1])-inp_li
    numT = sentence.count(charlist[2])-inp_li
    numG = sentence.count(charlist[3])-inp_li

    if numC==numA==numG==numT==0:
       res=1
       print(0)

    number = []

    number.append(int((numA+abs(numA))/2))
    number.append(int((numC+abs(numC))/2))
    number.append(int((numT+abs(numT))/2))
    number.append(int((numG+abs(numG))/2))

    diff=sum(number)
    master=[[],[],[],[]]

    if res==0:
        for i in range(len(sentence)):
            if ((sentence[i]==charlist[0])and number[0]):
                master[0].append(i)
            if ((sentence[i]==charlist[1])and number[1]):
                master[1].append(i)
            if ((sentence[i]==charlist[2])and number[2]):
                master[2].append(i)
            if ((sentence[i]==charlist[3])and number[3]):
                master[3].append(i)


    end=[]
    x=[0,0,0,0]

    if res==0:
        for j in range(len(sentence)):
            if j:
                if (sentence[j-1]==charlist[0]):
                    x[0]+=1
                if (sentence[j-1]==charlist[1]):
                    x[1]+=1
                if (sentence[j-1]==charlist[2]):
                    x[2]+=1
                if (sentence[j-1]==charlist[3]):
                    x[3]+=1

            brk=0
            for i in range(4):

                if (number[i] and x[i]+number[i]>len(master[i])):

                    brk=1

            if brk:
                break
            mx=0
            for i in range(4):
                if number[i]:
                    mx=max(mx,master[i][x[i]+number[i]-1]-j+1)
            end.append(mx)

    if res==0:
        print(min(end))





if __name__ == '__main__':
    main()
