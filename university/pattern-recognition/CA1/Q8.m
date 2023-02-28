%% Pattern Recognition HW1 Q5
clear;clc;close all
x=-5:0.01:5;
g1=(1/sqrt(2*pi))*exp(-(x-1).^2 /2) *0.5;
g2=(1/sqrt(2*pi))*exp(-(x+1).^2 /2) *0.5;

g3=(1-0.25)*(g1+g2);

plot(x,g1,x,g2,x,g3);
title('discriminant function');
xlabel('x axis');
ylabel('y axis');
legend('g1','g2','g3');


