clc; clf 

% bA, bB grid %
bA=linspace(0,0.74,200);
bB=linspace(0,0.74,200);
[bbA,bbB]=meshgrid(bA,bB);

% eta bar %
eta0Bar = eta0-0.5*(bbA+bbB);

% coefficients of dispersive relations %
alpha = @(bA,bB,eta0) (bA-bB).^2/192./(eta0-bA)./(eta0-bB);
KdVCoeff = @(bA,bB,eta0) 1/3*(eta0-0.5*(bA+bB)).^2;

% Plot the coefficients %
p1 = surf(bbA,bbB,alpha(bbA,bbB,0.75)/2.0);
AxOne = get(p1,'Parent');
colormap(AxOne,'hot');
set(p1,'edgecolor','none')
freezeColors 

hold on
p2 = surf(bbA,bbB,KdVCoeff(bbA,bbB,0.75)/2.0);
AxTwo = get(p2,'Parent');
set(p2,'edgecolor','none')

% format the figure %
xlabel('bA','fontsize',20)
ylabel('bB','fontsize',20)
xlim([0,0.75])
ylim([0,0.75])

ax = gca;
ax.FontSize = 20;

ax.ZTick=[0,0.04,0.08,0.12,0.16,0.2];
ax.XTick=[0,0.2, 0.4, 0.6];
ax.YTick=[0,0.2, 0.4, 0.6];

%campos([-4.95  3.90    0.82])
campos([-5.5, -1.75, 0.7])

set(gcf, 'Position',  [2000, 100, 800, 800])
saveas(gcf,'dispCoeff.png')

% Compute the ratio of the coefficients for the situations of interest %
KdVCoeff(0,0.5,0.75)/alpha(0,0.5,0.75)
KdVCoeff(0,0.5,0.55)/alpha(0,0.5,0.55)

