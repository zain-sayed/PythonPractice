#one.py

def func():
 print("FUNC IN ONE.PY")
 print(__name__)

print("TOP LEVEL ONE.PY")

if __name__ == "__main__":
   print("ONE.PY HAS BEEN RUN DIRECTLY")
   #Here we will want to write all the stuff
else:
   print("ONE.PY HAS BEEN IMPORTED")
