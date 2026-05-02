# senoidal - rampa - cuadrada - rand
tini = 0;
tfin = 1;
fm   = 100;
fs   = 10;
fase = 0;
r    = 1;


[t, senoidal]  = gen_sen(tini, tfin, fm , fs, fase);
[_, cuadrada]  = gen_cuad(tini, tfin, fm , fs, fase);
[_, aleatoria] = gen_aleatoria_fix(tini, tfin, fm, r);
rampa          = lineal(t);

##hold on;
##grid on;
##plot(senoidal);
##plot(cuadrada);
##plot(aleatoria);
##plot(rampa);

# defino [senoidal rampa cuadrada aleatroria]

signals = [senoidal; rampa; cuadrada; aleatoria];

# vector de valores

valores = zeros(8, 4);

n = rows(signals);
for i = 1:n
  valores(1, i) = media(signals(i,:));          % valor medio
  valores(2, i) = max(signals(i,:));            % max
  valores(3, i) = min(signals(i,:));            % min
  valores(4, i) = max(abs(signals(i,:)));       % Amplitud
  valores(5, i) = normp(signals(i,:),2).^2;     % Energy
  valores(6, i) = normp(signals(i,:),1);        % action
  valores(7, i) = potencia(signals(i,:));       % potencia media
  valores(8, i) = sqrt(potencia(signals(i,:))); % RMS
endfor

valores
