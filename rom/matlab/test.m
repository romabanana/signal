vector = randn(2000 0,1);
m = var(vector)
aux = mean(vector)

v_a = set_new_var(vector, 4);
m = var(v_a)
aux = mean(v_a)

