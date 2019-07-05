import io
from lib.reflect import reflect
import exampleClass

print(reflect("exampleClass").Instance("testClass").Call("testCall","test reflect example"))