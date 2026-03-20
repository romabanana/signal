function [x,y] = sinc(ti,tf,fm,fs,phs)
  tm = 1/fm;
  t = ti:tm:tf-tm;
  x=2*pi*fs*t+phs;

  y = (x==0) .* 1 + (x!=0) .* sin(x) ./ x;
endfunction
