import mylib
import mylib_cython

# Pure Python function
def get_result(val):
    return 'Python says: ' + val

print(get_result('Hi'))
print(mylib.get_result('Hi'))
print(mylib_cython.get_result('Hi'))
