import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', '..')))

from nfa import *


r0 = DisjRegex(CharRegex("a"), CharRegex("b"))
r1 = SeqRegex(CharRegex("c"), StarRegex(CharRegex("a")))
r2 = DisjRegex(StarRegex(StarRegex(StarRegex(r0))), r1)

if NFA(r2).NFA_to_DFA().matches("") == True:
    exit(0)
else:
    exit(1)
