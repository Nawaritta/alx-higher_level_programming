#!/usr/bin/python3
def multiple_returns(sentence):
    tup = ()
    tup += (len(sentence),)
    if len(sentence) > 0:
        tup += (sentence[0],)
    else:
        tup += (None,)
    return tup
