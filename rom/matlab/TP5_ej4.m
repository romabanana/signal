Hs = @(s) (12500.*s)./(44.*(s.^2)+(60625.*s)+6250000);

Hz1 = @(z,T) Hs((1-z.^-1)/T); #euler
Hz2 = @(z,T) Hs((2/T).*((1-z.^-1)./(1 + z.^-1))); #bilineal

w = 0:50:10000;
f_analog = w / (2*pi);
H = abs(Hs(w*1i));

[m, maxp] = max(H)
target =  m * 10^(-3/10)
% Busqueda
H_size   = length(H);
f0  = 0;
idx = -1;
for i=maxp:H_size
    if(H(i)<target)
        f0  = w(i)/(2*pi)
        [_, idx] = min(abs(2*w(i)-w));
      break;
    endif
endfor

subplot(3,1,1);
plot(f_analog(1:idx),H(1:idx));
#plot(f_analog,H);
title('H(s)');


fT = f0*4;
N  = 1000;
wz = linspace(0, pi, N);
f_hz = (wz ./ pi) * (fT / 2);

K1 = abs(Hz1(exp(wz.*1i),1/fT)); #...
subplot(3,1,2);
plot(f_hz,K1);
title('H1(z) euler');
K2 = abs(Hz2(exp(wz.*1i),1/fT)); #...
subplot(3,1,3);
plot(f_hz,K2);
title('H2(z) bilineal');

##figure(2);
##error_euler    = abs(H(1:idx) - K1);
##plot(wz, error_euler)
##error_bilineal = abs(H(1:idx) - K2);

