clear all
clc

x=linspace(0,1,100);
% f=r*x.*(1-x);
plot(x,f(x),'-b')
hold on
plot(x,x,'-r')
hold on

  plot([x(5),x(5)],[0,f(x(5))]) %draws th vert1cal line from(x1) from '0' to f(x(i))
   plot([x(5),f(x(5))],[f(x(5)),f(x(5))]) %draws horizontal line
 
 
 for i=1:100
    x(i+5)=f(x(i+4));
    plot([x(i+5),x(i+5)],[x(i+5),f(x(i+5))]) %draws th vert1cal line from(x1) from '0' to f(x(i))
 plot([x(i+5),f(x(i+5))],[f(x(i+5)),f(x(i+5))])% draws horizontal line
  pause(0.2)
 end
xlabel("x_n value");
ylabel("x_n+1 values");
legend('r=2.56', 'location' , 'northwest');
set (gca, 'color' , [0 0 0])

function x_n=f(x)
x_n=2.56*x.*(1-x);
end
