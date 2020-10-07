import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', '..')))

from nfa import *


r0 = DisjRegex(CharRegex("a"), CharRegex("b"))
r1 = SeqRegex(StarRegex(r0), CharRegex("b"))

if NFA(r1).NFA_to_DFA().matches("aaa") == False:
    exit(0)
else:
    exit(1)
