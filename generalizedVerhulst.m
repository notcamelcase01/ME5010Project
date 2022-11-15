clc;
clear;

syms n(t);
r = 3;%growth rate
ninf = 10000;%maximum carrying capacity
p = 1;
q = linspace(1,20,10);%(q)>1 shifts the simple logistic growth right


tspan = [0 50];
Y0 = [1];%%only one initital condition as 1st order equation
figure(1);

%effect of change in q
for i = 1:length(q)
    eqn = diff(n,1)== r* n^p *(1- (n/ninf)^q(i))/q(i);
    [V] = odeToVectorField(eqn);
    M = matlabFunction(V,'vars',{'t','Y'});
    [time,Y] = ode45(M, tspan, Y0);
    
    plot(time,Y,'DisplayName',num2str(q(i))); hold on
    drawnow;
end

xlabel('time');
ylabel('cumulative cases');
legend;
title('effect of parameter q');
hold off;

%effect of change in p
p = linspace(1,0,10);
q = 1;
figure(2);
tspan = [0 100];
for i = 1:length(p)
    eqn = diff(n,1)== r* n^p(i) *(1- (n/ninf)^q)/q;
    [V] = odeToVectorField(eqn);
    M = matlabFunction(V,'vars',{'t','Y'});
    [time,Y] = ode45(M, tspan, Y0);
    
    plot(time,Y,'DisplayName',num2str(p(i))); hold on
    drawnow;
end

xlabel('time');
ylabel('cumulative cases');
legend;
title('effect of parameter p');
hold off;
