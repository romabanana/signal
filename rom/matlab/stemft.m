## Copyright (C) 2026
##
## This program is free software: you can redistribute it and/or modify
## it under the terms of the GNU General Public License as published by
## the Free Software Foundation, either version 3 of the License, or
## (at your option) any later version.
##
## This program is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.
##
## You should have received a copy of the GNU General Public License
## along with this program.  If not, see <https://www.gnu.org/licenses/>.

## -*- texinfo -*-
## @deftypefn {} {@var{retval} =} stemft (@var{input1}, @var{input2})
##
## @seealso{}
## @end deftypefn

## Author:  <romy@khan>
## Created: 2026-05-17

# S = abs(fft(...))
# stem desde -fm/2 hasta fm/2 - df (fm muestras)

function stemft (S, t, fm)
  df    = fm / length(t);
  k     = -fm/2: df: (fm/2 - df);
  mitad = ceil((length(S)/2));
##  length(k)
##  length([S(mitad+1:end), S(1:mitad)])
##  length(S)
  stem(k, [S(mitad+1:end), S(1:mitad)] );


endfunction
