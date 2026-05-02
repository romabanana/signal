A  = gen_mat_sen(1);
fm = 11025;
t  = 0:1/fm:4000/fm - 1/fm;
hold on;
plot(t, A(1,:));

plot(t, A(4,:));
