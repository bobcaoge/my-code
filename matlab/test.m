% 单周期PRN自相关函数
clc
clear
close all
 
chiprate       = 1.023e6;            %码速率/码频率
IF             = 9.548e6;            %载波频率
samplingFreq   = 16.368e6;           %采样频率
codeLength     = 1023;               %码长
PRN            = 9;                 %卫星号

%每个CA码周期的采样数，整数倍不好38192
samplesPerCode = round(samplingFreq /(chiprate/codeLength));  

CAcode = cacode(PRN);
samplecacodes =  makeCaTable(PRN,codeLength,chiprate,samplingFreq);
length = length(samplecacodes);
PRNcode = samplecacodes;
middle = ceil(length/2);
temp = [PRNcode PRNcode];
start = temp(middle:(middle+length-1));
start_to_circle = [start start];
corr = zeros(1,length);
step = ceil(length/1023);
% 先计算采样前的C/A码的码形估计
j = 0;
for i = 1:length
%     index = step*j;
%     j = j+1;
    buffer = start_to_circle(i:(i-1+length));
   corr(i) = sum(PRNcode.* buffer);  
end

plot(corr,'*:')
axis([7900 8500 -2000 18000])
% axis([8550 8880 -1500 2000])
xlabel('相位')
ylabel('相关值')

% 
% 
% %单周期PRN自相关函数
% % clc
% % clear
% % close all
% % PRNcode3 = cacode(3);
% % 
% % PRNcode9 = cacode(9);
% % 
% % temp = [PRNcode3 PRNcode3];
% % start = temp(500:(500+1022));
% % start_to_circle = [start start];
% % corr = zeros(1,1023);
% % % 先计算采样前的C/A码的码形估计
% % for i = 1:1023
% %     buffer = start_to_circle(i:(i+1022));
% %    corr(i) = sum(PRNcode9.* buffer);  
% % end
% % corr=[corr corr corr corr corr];
% % 
% % 
% % plot(corr)
% % % title('PRN3和PRN9 C/A的自相关函数')
% % axis([0 1200 -200 1200])
% % xlabel('相位/码片')
% % ylabel('相关值')
% % %  
% % 
% % % PRN码频谱
% % clc
% % clear
% % chiprate       = 1.023e6;            %码速率/码频率
% % IF             = 9.548e6;            %载波频率
% % samplingFreq   = 16.3676e6;           %采样频率
% % codeLength     = 1023;               %码长
% % PRN            = 18;                 %卫星号
% % 
% % 
% % %??????????????????????????????????????
% % %每个CA码周期的采样数，整数倍不好38192
% % samplesPerCode = round(samplingFreq /(chiprate/codeLength));  
% % 
% % % 产生伪随机码,看cacode.m
% % w_code=cacode(PRN);
% % 
% % %对CA码进行采样
% % samplecacodes = makeCaTable(PRN,codeLength,chiprate,samplingFreq);
% % 
% % % 扩频，应该点乘离散的数据码
% % spread_code=samplecacodes;
% % y = fftshift(abs(fft(spread_code)));
% % freq = (0:length(y)-1)*samplingFreq/length(y);
% % 
% % plot(freq,20*log10(y))
% % figure(2)
% % plot(freq,y)
% % 
% % clc
% % clear
% % close all
% % 
% % T =0.001;
% % w= 0:0.03:2500;
% % p1 = T*sinc(w*T/2).*sinc(w*T/2)*1000;
% % 
% % T =0.002;
% %  
% % p2 = T*sinc(w*T/2).*sinc(w*T/2)*1000;
% % 
% % T =0.005;
% %  
% % p3 = T*sinc(w*T/2).*sinc(w*T/2)*1000;
% % 
% % T =0.02;
% %  
% % p4 = sinc(w*T/2).*sinc(w*T/2)*1000;
% % 
% % x = w;
% %  
% % plot(x, p1,x, p2,x, p3,x, p4)
% % 
% % % plot(w,p1,w,p2,'r:',w,p3,'--')
% % grid on;
% % ylim([0, 6])
% % legend('T=1ms','T=2ms','T=5ms')
% % xlabel('相位')
% % ylabel('归一化相关峰')
% 
% 
% 
% % clc
% % clear
% % close all
% % 
% % T =0.001;
% % w = -2000:0.03:2000;
% % p1 = T*sinc(w*T/2).*sinc(w*T/2)*1000;
% % 
% % T =0.002;
% %  
% % p2 = T*sinc(w*T/2).*sinc(w*T/2)*1000;
% % 
% % T =0.005;
% %  
% % p3 = T*sinc(w*T/2).*sinc(w*T/2)*1000;
% % 
% % T =0.02;
% %  
% % p4 = sinc(w*T/2).*sinc(w*T/2)*1000;
% 
% 
% 
% clc
% clear
% close all
% 
% T =0.001;
% w= 0:0.03:2500;
% p1 = sinc(w*T/2).*sinc(w*T/2);
% 
% T =0.002;
%  
% p2 = sinc(w*T/2).*sinc(w*T/2);
% 
% T =0.005;
%  
% p3 = sinc(w*T/2).*sinc(w*T/2);
% T =0.02;
%  
% p4 = sinc(w*T/2).*sinc(w*T/2);
% 
% 
% 
% plot(w,p1,'*',w,p2,'r:',w,p3,'--',w,p4)
% grid on;
% ylim([0, 1])
% legend('T=1ms','T=2ms','T=5ms','T=20ms')
% xlabel('相位')
% ylabel('归一化相关峰')
% 
% 
%  