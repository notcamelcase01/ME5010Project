r=0.564;
k=72036179;
t=0:1:45;
h=@(t,y)[r.*y(1).*(1-(y(1)/k))]
[t za]=ode45(h,t,[1959000])
plot(t,za(:,1),'o')
xlabel('time')
ylabel('subscriber')
legend('logistics')