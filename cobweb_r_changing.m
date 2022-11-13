clear all
clc

x=linspace(0,1,100);
% f=r*x.*(1-x);
hold on
plot(x,x,'-r')

p(1)=plot(0,0);
hold on

a = [];
b = [];


for r=1:0.1:4
    
 delete(p(1));  
 delete(a);
 delete(b);
p(1)=plot(x,f(x,r),'-b')
 drawnow;
 l=x(5);
 for i=1:100
     x_m=f(l,r);
    a(i) = plot([l,l],[l,x_m]);%draws th vert1cal line
    drawnow; 
    b(i) = plot([l,x_m],[x_m, x_m]); %draws horizontal line
  drawnow;
  l=x_m;
  
 end
 
end 
set(gca,'color',[0 0 0]);
%



function x_n=f(x,r)
x_n=r.*x.*(1-x);
end
