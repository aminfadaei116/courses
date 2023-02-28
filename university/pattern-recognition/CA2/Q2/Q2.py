import numpy as np

begin = [0.6, 0.4]
sleep = [0.1, 0.6]
poop = [0.4, 0.3]
eat = [0.5, 0.1]
input1 = "PESESEPEPSP"
input2 = "SESPSEPSPSE"


change = [[0.7, 0.3], [0.4, 0.6]]


def func(input1, begin):
    present = begin
    for i in range(len(input1)):
        if input1[i] == 'P':
            present = np.multiply(present, poop)
        elif input1[i] == 'E':
            present = np.multiply(present, eat)
        elif input1[i] == 'S':
            present = np.multiply(present, sleep)
        else:
            print("error")
        if i != (len(input1)-1):
            present = np.matmul(present, change)
    return present

out1 = func(input1, begin)
out2 = func(input2, begin)
print(out1)
print(out2)