#! /usr/bin/env python
# -*- coding: utf-8 -*-
def aDecimal(numeroBin):
    numeroBin = str(numeroBin)
    decimal = 0
    exp = len (numeroBin) -1
    for i in numeroBin:
        decimal += (int(i) * 2**(exp))
        exp = exp - 1
    return decimal