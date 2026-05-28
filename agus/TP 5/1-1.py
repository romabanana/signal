#1. y[n] - 1/2 y[n-1] + 1/4 y[n-2] = x[n]
#
#   Y(z) - 1/2 Y(z) z^(-1) + 1/5 Y(z) z^(-2) = X(z)
#   H(z) = Y(z) / X(z) = 1 / [1 - 1/2 z^(-1) + 1/5 z^(-2)]

#2. y[n] = y[n-1] + y[n-2] + x[n-1]
#
#   Y(z) - Y(z) z^(-1) - Y(z) z^(-2) = X(z) z^(-1)
#   H(z) = Y(z) / X(z) = z^(-1) / [1 - z^(-1) - z^(-2)]

#3. y[n] = 7 x[n] + 2 y[n-1] - 6 y[n-2]
#
#   Y(z) - 2 Y(z) z^(-1) + 6 Y(z) z^(-2) = 7 X(z)
#   H(z) = Y(z) / X(z) = 7 / [1 - 2 z^(-1) + 6 z^(-2)]

#4. y[n] = sum(k=0... 7) (2^(-k) x[n-k])
#
#   Y(z) = sum(k=0... 7) [2^(-k) X(z) z^(-k)] -> X(z) no depende de k, puedo sacarlo
#   H(z) = Y(z) / X(z) = sum(k=0... 7) [2^(-k) z^(-k)]