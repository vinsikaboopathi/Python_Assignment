marks = [78, 35, 92, 40, 61]

marks_tuple = tuple(marks)

print("List:", marks)
print("List type:", type(marks))

print("Tuple:", marks_tuple)
print("Tuple type:", type(marks_tuple))

print("Highest mark:", max(marks))
print("Lowest mark:", min(marks))

count_40_or_above = (
    (marks[0] >= 40)
    + (marks[1] >= 40)
    + (marks[2] >= 40)
    + (marks[3] >= 40)
    + (marks[4] >= 40)
)

print("Students scoring at least 40:", count_40_or_above)

valid_marks = (
    0 <= marks[0] <= 100
    and 0 <= marks[1] <= 100
    and 0 <= marks[2] <= 100
    and 0 <= marks[3] <= 100
    and 0 <= marks[4] <= 100
)

print("All marks are valid:", valid_marks)

marks[0] = 100
print("Modified list:", marks)

# List can be changed, but tuple cannot be changed.
# marks_tuple[0] = 100 would give a TypeError.