# scopes1.py
# Local versus Global
# we define a function, called local
def local():
    m = 7
    print(m)
m = 5
print(m)
# we call, or `execute` the function local
local()

def local():
 # m doesn't belong to the scope defined by the local function
 # so Python will keep looking into the next enclosing scope.
 # m is finally found in the global scope
    print(m, 'printing from the local scope')
m = 5
print(m, 'printing from the global scope')
local()
print("Hello")
print("Hello World")
