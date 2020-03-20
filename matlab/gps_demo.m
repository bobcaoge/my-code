P_s = 8;

%D = %导航电文
W_IF = 150e6;%载波频率
fs = 3*W_IF/2*pi;
N = 4096;
C = round(rand(1, N));%C/A码
dt = 1/fs;
t =  (0:N-1)*dt;%时间轴
theta = 1/3*pi;%初相
noise = rand(1, N);

S =  sqrt(2*P_s)*C  .* cos(W_IF*t+theta);
S_IF = S + noise;
%C/A码波形图
 figure(1);plot(t, C)
 title('C/A码波形图')
 axis([0 60*dt 0 2])
%信号射端波形图
%subplot(3,2,1);% 
figure(2);plot(t,S)
title('信号射端波形图')
%噪声波形图
%subplot(3,3,1);
figure(3);plot(t,noise);
title('噪声波形图')




