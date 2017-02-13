import base64
import sys


def decode(seg):
  padding_factor = (4 - len(seg) % 4)
  seg += '=' * (padding_factor + 1)
  return base64.decodestring(seg)

if len(sys.argv) < 2:
  print "no string to be decoded"
else:
  inp = sys.argv[1]
  segments = inp.split('.');
  print '===================Header===================' 
  print decode(segments[0])
  print '===================Claims==================='  
  print decode(segments[1])
  print '============================================'
