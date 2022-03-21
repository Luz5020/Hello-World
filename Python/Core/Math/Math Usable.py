import time

import Coreload
import Math

# LoadingscreenFX
Coreload.loadingeffectstart()
Math.loadingscreen()
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
    Math.addition()
    input("Press Enter Key to Exit")
elif X == 2:
    Math.subtraction()
    input("Press Enter Key to Exit")
elif X == 3:
    Math.multiplication()
    input("Press Enter Key to Exit")
elif X == 4:
    Math.division()
    input("Press Enter Key to Exit")
elif X == 5:
    Math.iseven()
    input("Press Enter Key to Exit")
else:
    print("Invalid Input")
    input("Press Enter Key to Exit")
