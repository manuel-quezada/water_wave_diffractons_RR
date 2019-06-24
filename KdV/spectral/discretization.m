function Du = ps_discretization(u,k)

global g mwl

uhat=fft(squeeze(u(1,:)));
eta=u(1,:);

dudx=real(ifft(1i*k.*uhat));
du3dx3=real(ifft(-1i*k.^3.*uhat));

Du(1,:)=-sqrt(g*mwl)*(dudx+3/2/mwl*(eta-mwl).*dudx+1/6*mwl^2*du3dx3);
