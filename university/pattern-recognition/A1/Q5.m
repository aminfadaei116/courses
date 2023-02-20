%% Pattern Recognition HW1 Q5
clear;clc;close all
star=[1 3;2 3;0.5 2;1.5 2;2.5 2;1 1;2 1;0 0.5;1.5 0];
dote=[1.5 0.5;0.5 0.5;1.5 -0.5;0.5 -0.5;1 -1;-1 -1;-1.5 0;0.5 -0.5;-1.5 1;-2 -1;-0.5 0.5];

sz=100;
figure
scatter(star(:,1),star(:,2),sz,'*');
hold on
scatter(dote(:,1),dote(:,2),sz,'filled');
xlabel('x axis');
ylabel('y axis');
grid on
xlim([-3 3]);
ylim([-2 4]);
hold off
%%
starXmean=mean(star(:,1));
starYmean=mean(star(:,2));
starMean=[starXmean;starYmean];

doteXmean=mean(dote(:,1));
doteYmean=mean(dote(:,2));
doteMean=[doteXmean;doteYmean];


mat1=(star(:,1)-starXmean);
mat2=(star(:,2)-starYmean);

mat3=(dote(:,1)-doteXmean);
mat4=(dote(:,2)-doteYmean);

Sigmastar=[sum(mat1.*mat1),sum(mat1.*mat2);sum(mat2.*mat1),sum(mat2.*mat2)]/9;
Sigmadote=[sum(mat3.*mat3),sum(mat3.*mat4);sum(mat4.*mat3),sum(mat4.*mat4)]/9;

[X,Y]=meshgrid(-10:0.1:10);
Z1=meshconvr(X,Y,starMean,Sigmastar);
Z2=meshconvr(X,Y,doteMean,Sigmadote);
figure
mesh(X,Y,Z1);
hold on 
mesh(X,Y,Z2);
xlabel('x axis');
ylabel('y axis');
title('Probability');


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
title('Probability decision');
%%
L12=2;
L21=1;
Z1=Z1*L12;
Z2=Z2*L21;
XB1 = X(Z1>Z2);
YB1 = Y(Z1>Z2);
ZB1 = Z1(Z1>Z2);

XB2 = X(Z1<=Z2);
YB2 = Y(Z1<=Z2);
ZB2 = Z2(Z1<=Z2);

figure
mesh(X,Y,Z1);
hold on 
mesh(X,Y,Z2);
xlabel('x axis');
ylabel('y axis');
title('Risk');

figure
stem3(XB1, YB1, ZB1);
hold on
stem3(XB2, YB2, ZB2);
xlabel('x axis');
ylabel('y axis');
title('Risk decision');






function y=meshconvr(X,Y,Mean,Sigma)
y=zeros(length(X),length(Y));
    for i= 1:length(X)
        for j=1:length(Y)
           y(i,j)=Gaussian([X(i,j);Y(i,j)],Mean,Sigma);
        
        end
    end
end

function outp=Gaussian(x,mean,sigma)

outp=(1/(sqrt(2*pi)*sqrt(det(sigma)))*exp(-0.5*(x-mean)' * inv(sigma)*(x-mean)));

end