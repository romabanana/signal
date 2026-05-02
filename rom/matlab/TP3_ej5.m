# Cargo la señal.--
S    = load('te.txt');
fm_S = 11025; %hz
##plot(S);

# Panel
# -----1209--1336--1477
# 697---1-----2-----3--
# 770---4-----5-----6--
# 852---7-----8-----9--
# 941---*-----0-----#--

fs_c1 = 1209;
fs_c2 = 1336;
fs_c3 = 1477;

fs_r1 = 697;
fs_r2 = 770;
fs_r3 = 852;
fs_r4 = 941;

# Extracción de inputs

m = 2999; % numero de muestras - 1

# 7 inputs

begin_1 = 17000;
input_1 = S(begin_1:begin_1 + m);

begin_2 = 30000;
input_2 = S(begin_2:begin_2 + m);

begin_3 = 39500;
input_3 = S(begin_3:begin_3 + m);

begin_4 = 48500;
input_4 = S(begin_4:begin_4 + m);

begin_5 = 59000;
input_5 = S(begin_5:begin_5 + m);

begin_6 = 69500;
input_6 = S(begin_6:begin_6 + m);

begin_7 = 81000;
input_7 = S(begin_7:begin_7 + m);

# Panel
# -----1209--1336--1477
# 697---1-----2-----3--
# 770---4-----5-----6--
# 852---7-----8-----9--
# 941---*-----0-----#--
# |
# | Defino una matriz que contiene senoidales (en varias fases)
# | con las frecuencia de la columna/fila
# |
# v
# -----C1----C2----C3--
# R1----1-----2-----3--
# R2----4-----5-----6--
# R3----7-----8-----9--
# R4----*-----0-----#--


C1 = gen_mat_sen(fs_c1);
C2 = gen_mat_sen(fs_c2);
C3 = gen_mat_sen(fs_c3);

R1 = gen_mat_sen(fs_r1);
R2 = gen_mat_sen(fs_r2);
R3 = gen_mat_sen(fs_r3);
R4 = gen_mat_sen(fs_r4);

# Calculo los numeros..
##inputs = [
##  input_1';
##  input_2';
##  input_3;
##  input_4;
##  input_5;
##  input_6;
##  input_7;
##];
##f = @(n) numero(n, C1, C2, C3, R1, R2, R3, R4);

numero_marcado = [
  numero(input_1, C1, C2, C3, R1, R2, R3, R4),
  numero(input_2, C1, C2, C3, R1, R2, R3, R4),
  numero(input_3, C1, C2, C3, R1, R2, R3, R4),
  numero(input_4, C1, C2, C3, R1, R2, R3, R4),
  numero(input_5, C1, C2, C3, R1, R2, R3, R4),
  numero(input_6, C1, C2, C3, R1, R2, R3, R4),
  numero(input_7, C1, C2, C3, R1, R2, R3, R4)
]

