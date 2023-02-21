%绘制正态分布曲线
% 定义 x 的取值范围
x = 1:0.01:6;

% 计算正态分布曲线的概率密度函数
mu = 4.4985;    % 均值
sigma = sqrt(0.24729);  % 标准差
y = normpdf(x, mu, sigma);

% 计算 x = 1, 2, 3, 4, 5, 6 处的概率密度值
pdf_at_x = normpdf([1, 2, 3, 4, 5, 6], mu, sigma);

% 输出概率密度值
disp(pdf_at_x)

% 绘制正态分布曲线
plot(x, y)
xlabel('x')
ylabel('num')
title('Normal distribution ')
