# Lower Triangular
def print_lower_triangular(n):
    for i in range(n):
        for j in range(i + 1):
            print("*", end=" ")
        print()

# Upper Triangular
def print_upper_triangular(n):
    for i in range(n):
        for j in range(n - i):
            print("*", end=" ")
        print()

# Pyramid
def print_pyramid(n):
    for i in range(n):
        for j in range(n - i - 1):
            print(" ", end=" ")
        for j in range(2 * i + 1):
            print("*", end=" ")
        print()

# Example usage
n = 5
print("Lower Triangular:")
print_lower_triangular(n)
print("\nUpper Triangular:")
print_upper_triangular(n)
print("\nPyramid:")
print_pyramid(n)