# deque objects are like double-ended queues

import collections
import string


# TODO: initialize a deque with lowercase letters
d = collections.deque(string.ascii_lowercase)

# TODO: deques support the len() function
print(f"Length of the deque: {len(d)}")
# TODO: deques can be iterated over
for iter in d:
    print(iter.upper())
# TODO: manipulate items from either end
print(d)
d.pop()
d.popleft()
d.appendleft(1)
d.append(2)
print(d)
# TODO: use an index to get a particular item
print(d[2])
d.rotate(2)
print(d)
