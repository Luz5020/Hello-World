import time

import Coreload
import DIYMath

# LoadingscreenFX
Coreload.loadingeffectstart()
DIYMath.loadingscreen()
Coreload.loadingeffectend()
# End LoadingscreenFX
print("Select Operation:")
print("+++Basic Operations+++")
print("(1) Addition")
print("(2) Subtraction")
print("(3) Multiplication")
print("(4) Division")
print("+++Other Operations+++")
print("(5) IsEven")
X = input()
try:
    X = int(X)
except ValueError:
    time.sleep(0.1)
if X == 1:
    DIYMath.addition()
    input("Press Enter Key to Exit")
elif X == 2:
    DIYMath.subtraction()
    input("Press Enter Key to Exit")
elif X == 3:
    DIYMath.multiplication()
    input("Press Enter Key to Exit")
elif X == 4:
    DIYMath.division()
    input("Press Enter Key to Exit")
elif X == 5:
    DIYMath.iseven()
    input("Press Enter Key to Exit")
else:
    print("Invalid Input")
    input("Press Enter Key to Exit")
