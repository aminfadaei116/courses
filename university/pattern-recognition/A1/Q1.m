%% Pattern Recognition HW1 Q2
clear;clc;close all
a1=3;
a2=5;
b=1;
%%
x=-15:0.01:15;

P1=(1/(pi*b) * 1./(1+((x-a1)/b).^2));
P2=(1/(pi*b) * 1./(1+((x-a2)/b).^2));
figure('Name','Distribution');
plot(x,P1,x,P2)
legend('w1','w2')
grid on

%%
L12=1;
L21=2;
R1=P1*L21;
R2=P2*L12;
figure('Name','Rick');
plot(x,R1,x,R2)
legend('w1','w2')
grid on

