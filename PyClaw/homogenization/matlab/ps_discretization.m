function Du = ps_discretization(u,k)

global g eta0Bar alpha beta omega2 
% Note: here I call the 1st and 2nd solutions u and v

coeff1 = g*eta0Bar;
coeff2 = g*eta0Bar*alpha*omega2;
coeff3 = g*eta0Bar*beta*omega2;

uhat=fft(squeeze(u(1,:)));
vhat=fft(squeeze(u(2,:)));

dudx=real(ifft(1i*k.*uhat));
du3dx3=real(ifft(-1i*k.^3.*uhat));
du5dx5=real(ifft(1i*k.^5.*uhat));
dvdx=real(ifft(1i*k.*vhat));

Du(1,:) = -dvdx;
Du(2,:) = -coeff1*dudx + coeff2*du3dx3; % + coeff3*du5dx5;