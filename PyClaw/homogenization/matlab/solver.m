function []=solver()
clc; clear all; clf

global g eta0Bar alpha beta omega2
%To pass parameters to Au

% parameters
g=9.8;
omega2=1.0;
bA=0.0;
bB=0.5;
eta0=0.75;
alpha = -(bA-bB)^2/192/(eta0-bA)/(eta0-bB);
beta  =  (bA-bB)^4/92160/(eta0-bA)^2/(eta0-bB)^2;
eta0Bar = eta0 - 0.5*(bA + bB);

dt=0.0001;    %time step
tf=200;      %final time
td=0.5;     %time interval to display 

save_solution = 1; %flag to save solution
name_solution='solution.mat';

% physical domain
x_lower=0; x_upper=200;

mx=2^9; %Number of Fourier modes
Lx=x_upper-x_lower;
kx = (2*pi/Lx)*[0:(mx/2-1) (-mx/2):-1]; % Wavenumber vector in x

%discretized domain
dx = (x_upper-x_lower)/mx;
x = (0:(mx-1))*dx;

nit=floor(tf/dt); %number of iterations

%initial conditions
A=0.001;
x0=(x_upper-x_lower)/2;
sig2=2;
eta=eta0+A*exp(-(x-x0).^2/(2*sig2)); %IC hom in y

u(1,:)=eta; %u
u(2,:)=x*0;   %sig

plot(x,eta)
pause(2)

U(1,:)=eta;
index=1;
for i=1:nit
    if(i*dt>=10 && i*dt<=11)
        u(1,1:end/2)=eta0;
        u(2,1:end/2)=0.;
    end
    disp('*********************************')
    disp('*********************************')
    disp(['Time step ' num2str(i) '. Time t=' num2str(i*dt)])
    % Four stages Runge-Kutta
    D1u=dt.*ps_discretization(u,kx);    
    D2u=dt.*ps_discretization(u+0.5*D1u,kx);
    D3u=dt.*ps_discretization(u+0.5*D2u,kx);
    D4u=dt.*ps_discretization(u+D3u,kx);
    u = u + (D1u+2*D2u+2*D3u+D4u)/6;
    if((i*dt-index*td)>=0)
        eta=squeeze(u(1,:));
        plot(x,eta)
        title(['t=' num2str(dt*i)]);
        U(index+1,:)=eta;
        index=index+1;
        pause(0.1)        
    end
end
if save_solution == 1
    save(name_solution)
end