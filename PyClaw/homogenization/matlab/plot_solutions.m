%clc; clear all 

% load solution on shallow bathymetry
load('solution.mat')
U_hom1 = U;

% read FV solution
X_FV=csvread('X_FV.csv');
x_FV=X_FV(1,:);
eta1_FV=csvread('eta1_FV.csv');
eta2_FV=csvread('eta2_FV.csv');

[xx_FV,tt_FV]=meshgrid(x_FV,linspace(0,200,201));
[xx,tt]=meshgrid(x,linspace(0,200,401));

% For some shifts
DXLeft=25;
DXRight=15;

%%%%%%%%%%%%%
% plot t=20 %
%%%%%%%%%%%%%
t=20;
[m,argmax] = max(U_hom1(2*t+1,:));
xmax = x(argmax);
shift=-100;
%clf; hold on
clf; subplot(131); hold on
plot(x+shift,U_hom1(2*t+1,:),'-k','linewidth',4)
plot(x_FV,eta1_FV(t+1,:),'--b','linewidth',4)
plot(x_FV,eta2_FV(t+1,:),'-r','linewidth',3)
ylim([0.75-0.0002, 0.7506])
xlim([xmax+shift-DXLeft,xmax+shift+DXRight])
ax = gca;
ax.FontSize=20; 
title(['Lin. homogenized system at t=' num2str(t)],'fontsize',40);
leg=legend({'Homogenized lin. system', 'Shallow water eqns at y=0.25', 'Shallow water eqns at y=0.75'},'location','northwest');
leg.FontSize = 35;
xlabel('x','FontSize',30)
ylabel('\eta','Fontsize',30,'rotation',0)
% saveas(gcf,'homog_t20_corr1.png')
% save data to export for python plots
hom_data_for_python = [x' U_hom1(2*t+1,:)'];
FV_data_for_python  = [x_FV' eta1_FV(t+1,:)' eta2_FV(t+1,:)'];

%%%%%%%%%%%%%%
% plot t=120 %
%%%%%%%%%%%%%%
t=120;
[m,argmax] = max(U_hom1(2*t+1,:));
xmax = x(argmax);
shift=100;
shift_FV=200;
%clf; hold on
subplot(132); hold on
plot(x+shift,U_hom1(2*t+1,:),'-k','linewidth',4)
plot(x_FV+shift_FV,eta1_FV(t+1,:),'--b','linewidth',4)
plot(x_FV+shift_FV,eta2_FV(t+1,:),'-r','linewidth',3)
ylim([0.75-0.0002, 0.7506])
xlim([xmax+shift-DXLeft,xmax+shift+DXRight])
ax = gca;
ax.FontSize=20;
set(gca,'ytick',[])
title(['Lin. homogenized system at t=' num2str(t)],'fontsize',40);
leg=legend({'Homogenized lin. system', 'Shallow water eqns at y=0.25', 'Shallow water eqns at y=0.75'},'location','northwest');
leg.FontSize = 35;
xlabel('x','FontSize',30)
ylabel('\eta','Fontsize',30,'rotation',0)
% saveas(gcf,'homog_t120_corr1.png')
% save data to export for python plots
hom_data_for_python = [hom_data_for_python U_hom1(2*t+1,:)'];
FV_data_for_python  = [FV_data_for_python eta1_FV(t+1,:)' eta2_FV(t+1,:)'];

%%%%%%%%%%%%%%
% plot t=200 %
%%%%%%%%%%%%%%
t=200;
[m,argmax] = max(U_hom1(2*t+1,:));
xmax = x(argmax);
shift=300;
shift_FV=400;
%clf; hold on
subplot(133); hold on
plot(x+shift,U_hom1(2*t+1,:),'-k','linewidth',4)
plot(x_FV+shift_FV,eta1_FV(t+1,:),'--b','linewidth',4)
plot(x_FV+shift_FV,eta2_FV(t+1,:),'.r','linewidth',3)
ylim([0.75-0.0002, 0.7506])
xlim([xmax+shift-DXLeft,xmax+shift+DXRight])
ax = gca;
ax.FontSize=20;
set(gca,'ytick',[])
title(['Lin. homogenized system at t=' num2str(t)],'fontsize',40);
leg=legend({'Homogenized lin. system', 'Shallow water eqns at y=0.25', 'Shallow water eqns at y=0.75'},'location','northwest');
leg.FontSize = 35;
xlabel('x','FontSize',30)
ylabel('\eta','Fontsize',30,'rotation',0)
% saveas(gcf,'homog_t200_corr1.png')
% save data to export for python plots
hom_data_for_python = [hom_data_for_python U_hom1(2*t+1,:)'];
FV_data_for_python  = [FV_data_for_python eta1_FV(t+1,:)' (eta2_FV(t+1,:))'];

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% save data for python plots %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
dlmwrite('hom_data_for_python.csv',hom_data_for_python,'precision',12)
dlmwrite('FV_data_for_python.csv',FV_data_for_python,'precision',12)
