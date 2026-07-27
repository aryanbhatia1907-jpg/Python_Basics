ep={121:45 , 122:57 , 123:556}
ep2={224:78 , 225:82}

ep.update(ep2)
print(ep)

ep2.clear()
print(ep2," ~clear")     # Dict ko clearkarne ke liye

emp={}
print(emp," ~empty")     # Empty dict banane ke liye

ep.pop(121)              # Remove any Key-Value from dictionary
print(ep,"~pop")

ep.popitem()             # Remove last one only , No need to mention otherwise error occurs
print(ep,"~popitem")

del ep[122]              # Also used to delete
print(ep,"~del")

print(max(ep.values()))  # To find maximum value