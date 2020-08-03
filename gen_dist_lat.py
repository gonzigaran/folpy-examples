#!/usr/bin/env python
# -*- coding: utf8 -*-

from folpy.semantics import Lattice
from folpy.syntax.types import AlgebraicType
from folpy.semantics.modelfunctions import Operation, Operation_decorator


def gen_chain(n):
    universe = list(range(n))

    @Operation_decorator(universe)
    def sup(x, y):
        return max(x, y)

    @Operation_decorator(universe)
    def inf(x, y):
        return min(x, y)

    return Lattice(universe,
                   sup,
                   inf,
                   name="Chain Lattice %s" % n)


def gen_full(n):
    chain2 = gen_chain(2)
    return (chain2 ** n).continous()[0]


def save_chains(n):
    for i in range(2,n):
        chain = gen_chain(i)
        file_name = 'examples/DistLattices/%schain.model' % i
        chain.to_file(file_name)


def save_fulls(n):
    for i in range(2,n):
        full = gen_full(i)
        file_name = 'examples/DistLattices/%sfull.model' % 2**i
        full.to_file(file_name)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    
    save_chains(11)
    save_fulls(5)
