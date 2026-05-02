function x = numero(input, C1, C2, C3, R1, R2, R3, R4)

  # Numpad

  numpad = ["1" "2" "3"; "4" "5" "6"; "7" "8" "9"; "*" "0" "#"];

  # Cols

  c1      = max(C1 * input);
  c2      = max(C2 * input);
  c3      = max(C3 * input);
  [_,col] = max([c1, c2, c3]); #max retorna posicion;

  # Rows

  r1      = max(R1 * input);
  r2      = max(R2 * input);
  r3      = max(R3 * input);
  r4      = max(R4 * input);
  [_,row] = max([r1, r2, r3, r4]);

  # return
  x = numpad(row, col);

endfunction


