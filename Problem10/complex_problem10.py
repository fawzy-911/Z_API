import pandas as pd

s1 = pd.Series([3,4,5,8,6])
s2 = pd.Series([1,2,3,4,5])

add = s1 + s2
print("Addition = "+str(add))
sub = s1 - s2
print("Subtraction = "+str(sub))
div = s1 / s2
print("Division = "+str(div))
mul = s1 * s2
print("Multiplication = "+str(mul))