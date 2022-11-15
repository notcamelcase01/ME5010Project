clc;
clear;

populationCountry = 1352642280;
t = linspace(0,128,129);
growthRate = 2309;% calculated from t0Cases and t1Cases

t0Cases = 585493;%01-07-2020
t1Cases = 742417;%08-07-2020

realData=xlsread('indiaWeeklyCoviddata.xlsx');%imports real data from excel sheet
realWeeks = realData(:,1);
realCases = realData(:,2);


%% Estimate using basic Logistic Equation

N = populationCountry./(1 + growthRate.*(0.788.^t));

figure(1);

for j = 1:18
    bar(t(j),N(j),'b'); hold on;%plot estimated data 
    drawnow;
    bar(realWeeks(j),realCases(j),'r'); hold on;%plot real data
    drawnow;
    pause(0.1);
end

legend('blue = estimated data','red = real data');
xlabel('time');
ylabel('cumulative cases');

hold off;



