%% Pattern Recognition HW1 Q3
clear;clc;close all
a1=[2;1];
a2=[3;5];
b1=1;
b2=1;
var=[1 0.5;0.5 1];
x=[1;0];
%%
[X,Y]=meshgrid(-10:0.1:10);
result1=meshconv(X,Y,a1,b1,var);
result2=meshconv(X,Y,a2,b2,var);
%%
Z1=result1;
Z2=result2;

%%
XB1 = X(Z1>Z2);
YB1 = Y(Z1>Z2);
ZB1 = Z1(Z1>Z2);

XB2 = X(Z1<=Z2);
YB2 = Y(Z1<=Z2);
ZB2 = Z2(Z1<=Z2);

figure
stem3(XB1, YB1, ZB1);
hold on
stem3(XB2, YB2, ZB2);
xlabel('x axis');
ylabel('y axis');

%%
figure
mesh(X,Y,result1);
hold on
mesh (X,Y,result2);
xlabel('x axis');
ylabel('y axis');


function y=meshconv(X,Y,a,b,var)
y=zeros(length(X),length(Y));
    for i= 1:length(X)
        for j=1:length(Y)
           y(i,j)=Neyman_Pearson([X(i,j);Y(i,j)],a,b,var);
        
        end
    end
end

function outp=Neyman_Pearson(x,a,b,var)


outp=(1/(pi*b)) / (1+((x-a)/b)' * inv(var) * (x-a)/b);


end