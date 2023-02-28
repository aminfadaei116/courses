import numpy as np
import matplotlib.pyplot as plt


def gaussian(x, mu, sig2):
    return 1./(np.sqrt(2.*np.pi*sig2))*np.exp(-((x-mu)*(x-mu)/(2*sig2)))


mu = [0.5, 1.2, 2.1, 3.4, 4.0]
sigma2 = [0.02, 0.09, 0.06, 0.04, 0.01]
kk = []
The_list = []
number_data = 2500
number_sample = 2
for i in range(5):
    kk.append(np.random.normal(mu[i], np.sqrt(sigma2[i]), 1000))
    The_list.extend(np.random.normal(mu[i], np.sqrt(sigma2[i]), 1000))


hist, bins = np.histogram(kk, bins=100)
width = 0.7 * (bins[1] - bins[0])
center = (bins[:-1] + bins[1:]) / 2
plt.bar(center, hist, align='center', width=width)
plt.show()
# This past is for showing the real Distribution
x_values = np.linspace(0, 4.5, 1000)

# Now here we start to estimate the gaussian
new_mu = [1.8, 3.5]
new_sig = [1, 1]
all_data = number_data*number_sample
class1 = np.zeros(all_data)
class2 = np.zeros(all_data)
#class3 = np.zeros(all_data)
# class4 = np.zeros(all_data)
#class5 = np.zeros(all_data)

prob1 = np.zeros(all_data)
prob2 = np.zeros(all_data)
#prob3 = np.zeros(all_data)
#prob4 = np.zeros(all_data)
#prob5 = np.zeros(all_data)


for i in range(50):
    for j in range(all_data):
        class1[j] = gaussian((The_list[j]), new_mu[0], new_sig[0])
        class2[j] = gaussian((The_list[j]), new_mu[1], new_sig[1])
        #class3[j] = gaussian((The_list[j]), new_mu[2], new_sig[2])
        #class4[j] = gaussian((The_list[j]), new_mu[3], new_sig[3])
        #class5[j] = gaussian((The_list[j]), new_mu[4], new_sig[4])
      #  print([j],The_list[j],class1[j],class2[j],class3[j],class4[j],class5[j])

    for j in range(all_data):
        finaly = class1[j] + class2[j]# + class3[j] + class4[j]# + class5[j]
        prob1[j] = class1[j]/finaly
        prob2[j] = class2[j]/finaly
        #prob3[j] = class3[j]/finaly
        #prob4[j] = class4[j]/finaly
        #prob5[j] = class5[j]/finaly
    new_mu[0] = sum(The_list[k] * prob1[k] for k in range(all_data))/sum(prob1)
    new_mu[1] = sum(The_list[k] * prob2[k] for k in range(all_data))/sum(prob2)
    #new_mu[2] = sum(The_list[k] * prob3[k] for k in range(all_data))/sum(prob3)
    #new_mu[3] = sum(The_list[k] * prob4[k] for k in range(all_data))/sum(prob4)
    #new_mu[4] = sum(The_list[k] * prob5[k] for k in range(all_data))/sum(prob5)

    new_sig[0] = sum(prob1[k]*(The_list[k]-new_mu[0])*(The_list[k]-new_mu[0]) for k in range(all_data))/sum(prob1)
    new_sig[1] = sum(prob2[k]*(The_list[k]-new_mu[1])*(The_list[k]-new_mu[1]) for k in range(all_data))/sum(prob2)
    #new_sig[2] = sum(prob3[k]*(The_list[k]-new_mu[2])*(The_list[k]-new_mu[2]) for k in range(all_data))/sum(prob3)
    #new_sig[3] = sum(prob4[k]*(The_list[k]-new_mu[3])*(The_list[k]-new_mu[3]) for k in range(all_data))/sum(prob4)
    #new_sig[4] = sum(prob5[k]*(The_list[k]-new_mu[4])*(The_list[k]-new_mu[4]) for k in range(all_data))/sum(prob5)

for k in range(number_sample):
    F2 = 1/5 * gaussian(x_values, new_mu[k], new_sig[k])
    plt.plot(x_values, F2)
plt.show()

for j in range(5):
    F1 = 1/5 * gaussian(x_values, mu[j], sigma2[j])
    plt.plot(x_values, F1)
plt.show()
print(new_mu)
print(new_sig)