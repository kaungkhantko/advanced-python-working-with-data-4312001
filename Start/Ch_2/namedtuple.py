# Demonstrate the usage of namdtuple objects

import collections


# TODO: create a Point namedtuple

Point = collections.namedtuple("Point", "x y")
p1 = Point(10, 20)
p2 = Point(30, 40)
print(p1, p2)

p1 = p1._replace(x=100)
# TODO: use _replace to create a new instance
