# conv_ops.py
#
# Usage: python3 conv_ops.py c_in h_in w_in n_filt h_filt w_filt s p
#  Converts input shape and operation count of convolution layer into output.
# Parameters:
#  c_in: input channel count
#  h_in: input height count
#  w_in: input width count
#  n_filt: number of filters in the convolution layer
#  h_filt: filter height count
#  w_filt: filter width count
#  s: stride of convolution filters
#  p: amount of padding on each of the four input map sides
# Output:
#  Output shape and operation count of convolution layer.
#
# Written by Matthew Moore
# Other contributors: None
#
# Optional license statement, e.g., See the LICENSE file for the license.

# import Python modules
# e.g., import math # math module
import sys # argv

# "constants"
# e.g., R_E_KM = 6378.137

# helper functions

## function description
# def calc_something(param1, param2):
#   pass

# initialize script arguments
c_out = float('nan')
h_out = float('nan')
w_out = float('nan')
adds = 0.0
muls = 0.0
divs = 0.0

# parse script arguments
if len(sys.argv)==9:
    c_in = float(sys.argv[1])
    h_in = float(sys.argv[2])
    w_in = float(sys.argv[3])
    n_filt = float(sys.argv[4])
    h_filt = float(sys.argv[5])
    w_filt = float(sys.argv[6])
    s = float(sys.argv[7])
    p = float(sys.argv[8])
else:
    print('Usage: python3 conv_ops.py c_in h_in w_in n_filt h_filt w_filt s p')
    exit()

# write script below this line
c_out = n_filt
h_out = (h_in + 2 * p - h_filt) / s + 1
w_out = (w_in + 2 * p - w_filt) / s + 1
muls = n_filt * h_out * w_out * c_in * h_filt * w_filt
adds = n_filt * h_out * w_out * c_in * h_filt * w_filt


# script output
print(int(c_out))
print(int(h_out))
print(int(w_out))
print(int(adds))
print(int(muls))
print(int(divs))
