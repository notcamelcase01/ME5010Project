r=.564;
k=72036179;
t=0:1:9;
h= @(t,x)[r.*x(1)]
[t ya]=ode45(h,t,[1959000])
figure
plot(t,ya(:,1),'r')
hold on
h=@(t,y)[r.*y(1).*(1-(y(1)/k))]
[t za]=ode45(h,t,[1959000])
plot(t,za(:,1),'o')
hold on 
subscriber=[1959000 1959000 6500000 11350000 15201000 15201000 32810000 32810000 51795000 51795000];
plot(t,subscriber,'*')
xlabel('time')
ylabel('subcriber')
legend('exponential','logistic','data')
for i=1:10
    error1=abs((subscriber(i)-ya(i))/ya(i))*100;
    error2=abs((subscriber(i)-za(i))/za(i))*100;
end