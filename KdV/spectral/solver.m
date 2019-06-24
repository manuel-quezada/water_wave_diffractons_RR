function []=solver()
clc; clear all; clf

%To pass parameters to Au
global g mwl

%User parameters
save_solution = 1; %flag to save solution
name_solution='deep'; %OPTIONS: 'shallow', 'mean', 'deep'
mwl=0.75;  %OPTIONS: 0.25, 0.5, 0.75

%%
dt=0.0001;    %time step
tf=30;      %final time
td=0.5;     %time interval to display 

% physical domain
x_lower=0; x_upper=200;

mx=2^10; %Number of Fourier modes
Lx=x_upper-x_lower;
kx = (2*pi/Lx)*[0:(mx/2-1) (-mx/2):-1]; % Wavenumber vector in x

%discretized domain
dx = (x_upper-x_lower)/mx;
x = (0:(mx-1))*dx;

nit=floor(tf/dt); %number of iterations

% initial condition and parameters
x0=(x_upper-x_lower)/2;
g=9.8;

% Profile
A=0.025;
sig2=2.0;  
eta=mwl+A*exp(-(x-x0).^2/(2*sig2)); 

u(1,:)=eta;
plot(x-Lx/2,eta)
xlim([0,Lx/2])
pause(2)

U(1,:)=eta;
index=1;
for i=1:nit
    disp('*********************************')
    disp('*********************************')
    disp(['Time step ' num2str(i) '. Time t=' num2str(i*dt)])
    % Four stages Runge-Kutta
    D1u=dt.*discretization(u,kx);    
    D2u=dt.*discretization(u+0.5*D1u,kx);
    D3u=dt.*discretization(u+0.5*D2u,kx);
    D4u=dt.*discretization(u+D3u,kx);
    u = u + (D1u+2*D2u+2*D3u+D4u)/6;
    if((i*dt-index*td)>=0)
        eta=squeeze(u(1,:));
        plot(x-Lx/2,eta)
        xlim([0,Lx/2])
        title(['t=' num2str(dt*i)]);
        U(index+1,:)=eta;
        index=index+1;
        pause(0.1)        
    end
end
if save_solution == 1
    save([name_solution,'.mat'])
    csvwrite(['uKdV_',name_solution,'.csv'],U)
    csvwrite(['xKdV_',name_solution,'.csv'],x-Lx/2)
end