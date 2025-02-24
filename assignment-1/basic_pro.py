x = input("Enter x: ")
y = input("Enter y: ")

x_bool = bool(x)
y_bool = bool(y)

print(f"x AND y: {x_bool and y_bool}")
print(f"x OR y: {x_bool or y_bool}")
print(f"NOT x: {not x_bool}")
print(f"x XOR y: {(x_bool and not y_bool) or (not x_bool and y_bool)}")
