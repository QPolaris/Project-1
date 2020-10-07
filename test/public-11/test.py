import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', '..')))

from nfa import *

r = regex("(x|y|)(xxyy|xyy|xxy)*")

nfar = NFA(r)
mindfa = nfar.NFA_to_DFA().minimizeDFA()

if (nfar.isDFA() == False
        and mindfa.isDFA()
        and mindfa.matches("xxxx") == False
        and mindfa.matches("xxxy")
        and mindfa.matches("yxxyyxyy")):
    exit(0)
else:
    exit(1)
