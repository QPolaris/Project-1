import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', '..')))

from nfa import *

r0 = DisjRegex(EpsilonRegex(), SeqRegex(SeqRegex(CharRegex("a"),CharRegex("b")),SeqRegex(CharRegex("b"),CharRegex("a"))))
r = regex("(abba|)") # You can insert an epsilon by closing a paren after a |, or using parens with nothing between them: ()


if (NFA(r).NFA_to_DFA().isDFA()
        and NFA(r).NFA_to_DFA().matches("abba")
        and NFA(r).NFA_to_DFA().matches("")
        and NFA(r).NFA_to_DFA().matches("a") == False):
    exit(0)
else:
    exit(1)
