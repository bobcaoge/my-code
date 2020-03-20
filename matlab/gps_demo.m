P_s = 8;

%D = %��������
W_IF = 150e6;%�ز�Ƶ��
fs = 3*W_IF/2*pi;
N = 4096;
C = round(rand(1, N));%C/A��
dt = 1/fs;
t =  (0:N-1)*dt;%ʱ����
theta = 1/3*pi;%����
noise = rand(1, N);

S =  sqrt(2*P_s)*C  .* cos(W_IF*t+theta);
S_IF = S + noise;
%C/A�벨��ͼ
 figure(1);plot(t, C)
 title('C/A�벨��ͼ')
 axis([0 60*dt 0 2])
%�ź���˲���ͼ
%subplot(3,2,1);% 
figure(2);plot(t,S)
title('�ź���˲���ͼ')
%��������ͼ
%subplot(3,3,1);
figure(3);plot(t,noise);
title('��������ͼ')




