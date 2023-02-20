import numpy as np

begin1 = [0.4, 0.6]
A1 = [0.45, 0.5]
B1 = [0.55, 0.5]
change1 = [[0.6, 0.4], [0.0, 1]]


begin2 = [0.7, 0.3]
A2 = [0.2, 0.6]
B2 = [0.8, 0.4]
change2 = [[0.2, 0.8], [0.0, 1]]

present1 = begin1
present1 = np.multiply(present1, A1)
present1 = np.matmul(present1, change1)
present1 = np.multiply(present1, B1)
present1 = np.matmul(present1, change1)
present1 = np.multiply(present1, A1)
print(present1)

present2 = begin2
present2 = np.multiply(present2, A2)
present2 = np.matmul(present2, change2)
present2 = np.multiply(present2, B2)
present2 = np.matmul(present2, change2)
present2 = np.multiply(present2, A2)
print(present2)

print(sum(present1), sum(present2))
