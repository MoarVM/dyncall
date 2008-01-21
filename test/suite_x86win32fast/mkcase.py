#!/usr/bin/python
import sys

# parameters

nargs  = 3

types  = ["DCbool","DCint","DClonglong","DCdouble","DCpointer","DCfloat"]

# generator

ntypes = len(types)

sys.stderr.write("/* auto generated by mkcase (on stderr) */\n");
sys.stderr.write("".join(["#define NARGS  ",str(nargs),"\n"]))
sys.stderr.write("".join(["#define NTYPES ",str(ntypes),"\n"]))

def powerfact(x, n):
  if n==0:
    return 0
  else:
    return x**n+powerfact(x,n-1)

x     = 0
end   = powerfact(ntypes,nargs)+1

sys.stdout.write("/* auto generated by mkcase.py (on stdout) */\n");

while x < end:
  args = [str(x)]
  sig  = ["f_"]
  pos  = 0
  y    = x
  while y > 0:
    s     = (y-1) % ntypes
    y     = (y-1) / ntypes
    args += [ types[s] ]
    sig  += [ types[s][2] ]
    pos  += 1
  sig   = "".join(sig)
  args += [ sig ]
  args  = ",".join(args)
  sys.stdout.write( "".join(["VF",str(pos),"(",args,")\n"]) )
  x += 1
