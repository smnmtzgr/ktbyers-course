def mult(x, y, z = 1):
    return x*y*z

print mult(5, 10, 15)
print mult(x=5, y=10, z=15)
print mult(5, y=10, z=15)
print mult(5, 10)
