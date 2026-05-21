#a) se ve 23hz por aliasing
fm = 50;
##t  = 0:1/fm:1-(1/fm);
##k  = 2 * pi * 27;
##x  = 2 * sin(k .* t);
##
##figure(1);
##hold on;
##plot(t, x);
##stem(t, x);
##
##X  = fft(x);
##figure(2);
##stem(1:fm, abs(X));
##
##figure(3);
##stemft(abs(X), t, fm);

## b)
## 23  = abs(27 - 50)
## f_a = abs(fs - fm)

## 55 = abs(105 - 50)

##for fm=1:60
##  t  = 0:1/fm:1-(1/fm);
##  k  = 2 * pi * 27;
##  x  = 2 * sin(k .* t);
##
##  X  = fft(x);
##
##  figure(1);
##  stem(1:fm, abs(X));
##  pause(1)
##endfor

fs_b = 105;
t  = 0:1/fm:1-(1/fm);
k  = 2 * pi * fs_b;
x  = 2 * sin(k .* t);

##figure(1);
##hold on;
##plot(t, x);
##stem(t, x);
##
##X  = fft(x);
##figure(2);
##stem(1:fm, abs(X));
##
##figure(3);
##stemft(abs(X), t, fm);

#5hz

#3) h = A*n/2
n = 15;
for i=1:n
  X1  = fft(i/2 * x);
##  stem(1:fm, abs(X1));

##  rel(i) = max(abs(X1));
##  rel(i) = max(abs(X1)) / i;
endfor

plot(1:n, rel);




