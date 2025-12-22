%% ============================================================
%  TONG HOP BO DIEU KHIEN BEN VUNG H-INFINITY (CASCADE)
%  Su dung Pade de xu ly tre thoi gian
% ============================================================

clear; clc; close all;

s = tf('s');

thamso

%% 1. Tham so nhan dang

% Van dieu khien
K_v   = 1;
T_v   = 1.984;
tau_v = 0.88;

% Bo qua nhiet
K_bqn   = 9;
T_bqn   = 18.315;
tau_bqn = 11.68;

%% 2. Mo hinh doi tuong (KHONG tre)

Gv_nom   = K_v/(T_v*s + 1)^2;
Gbqn_nom = K_bqn/(T_bqn*s + 1)^2;

%% 3. Xap xi tre bang Pade

% Van: Pade bac 1
[numDv, denDv] = pade(tau_v,1);
Delay_v = tf(numDv, denDv);

% Bo qua nhiet: Pade bac 2
[numDb, denDb] = pade(tau_bqn,2);
Delay_bqn = tf(numDb, denDb);

Gv   = Gv_nom*Delay_v;
Gbqn = Gbqn_nom*Delay_bqn;

%% 4. Dong vong trong (PI cho van)

Kp_inner = Kp1;
Ti_inner = Ti1;

R_inner = Kp_inner*(1 + 1/(Ti_inner*s));

W1 = feedback(R_inner*Gv,1);

%% 5. Doi tuong tuong duong vong ngoai
G_outer = W1*Gbqn;

%% 6. Ham trong so H-infinity

% Trong so sai so
Ms = 2;
wb = 0.01;
As = 0.001;

Wp = (s/Ms + wb)/(s + wb*As);

% Trong so tin hieu dieu khien
Mu = 2;
wu = 1;
eps_u = 0.01;

Wu = (s + wu/Mu)/(eps_u*(s + wu));

% Trong so nhay cam
Mt = 2;
wt = 10;
eps_t = 0.1;

Wt = eps_t*(s + wt/Mt)/(s + wt);

%% 7. He tong quat (Generalized Plant)

systemnames = 'G_outer Wp Wu Wt';
inputvar    = '[r; u]';
outputvar   = '[Wp; Wu; Wt; r - G_outer]';

input_to_G_outer = '[u]';
input_to_Wp      = '[r - G_outer]';
input_to_Wu      = '[u]';
input_to_Wt      = '[G_outer]';

P = sysic;

%% 8. Tong hop H-infinity

nmeas = 1;
ncont = 1;

[K_hinf, CL, gamma] = hinfsyn(P,nmeas,ncont);

disp('--------------------------------')
disp('Chi so ben vung gamma = ')
disp(gamma)
disp('--------------------------------')

%% 9. Dap ung buoc

CL_sys = feedback(G_outer*K_hinf,1);

figure;
step(CL_sys,500)
grid on
title('Dap ung buoc he cascade voi bo dieu khien H_\infty')