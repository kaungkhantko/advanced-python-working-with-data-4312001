# Demonstrate the usage of Counter objects

from collections import Counter


# list of students in class 1
class1 = [
    "Bob",
    "James",
    "Chad",
    "Darcy",
    "Penny",
    "Hannah",
    "Kevin",
    "James",
    "Melanie",
    "Becky",
    "Steve",
    "Frank",
]

# list of students in class 2
class2 = [
    "Bill",
    "Barry",
    "Cindy",
    "Debbie",
    "Frank",
    "Gabby",
    "Kelly",
    "James",
    "Joe",
    "Sam",
    "Tara",
    "Ziggy",
]

# TODO: Create a Counter for class1 and class2
c1 = Counter(class1)
c2 = Counter(class2)

# TODO: How many students in class 1 named James?
print(c1["James"])

# TODO: How many students are in class 1?
print(f"{sum(c1.values())} students in class 1")

# TODO: Combine the two classes
print(f"{c1.values()} students in class 1")
c1.update(class2)
print(f"{c1.values()} students in class 1")
# TODO: What's the most common name in the two classes?
print("Most common names in class 1: ", c1.most_common(3))
print("Most common name in class 2: ", c2.most_common(3))
# TODO: Separate the classes again
c1.subtract(class2)
print("After separating: ", c1.most_common(3))

# TODO: What's common between the two classes?
print("Common names between the two classes: ", c1 & c2)
