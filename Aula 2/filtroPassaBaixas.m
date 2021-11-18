
clear 
close all
clc

n =0:24;
N = 25;

fs = 8e3;
fc = 1e3;

ws = 2*pi*fs;
wc = 2*pi*fc;
Omegac = wc*1/fs;
alpha = (N-1)/2;

h = sin(Omegac*(n-alpha))./(pi*(n-alpha));
h(alpha+1) = Omegac/pi;

stem(h);

grid on;

