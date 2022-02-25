"""
All values are considered "truthy" except for the following, which are "falsy":

None
False
Zeros, including:
0
0.0
0j
decimal.Decimal(0)
fraction.Fraction(0, 1)
Empty sequences and collections, including:
[] - an empty list
{} - an empty dict
() - an empty tuple
'' - an empty str
b'' - an empty bytes
set() - an empty set
an empty range, like range(0)
objects for which
obj.__bool__() returns False
obj.__len__() returns 0
"""
