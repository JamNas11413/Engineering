# details are in withExe,txt
with open("withExe.txt","r") as f:       # the f is an alias for the stuff resulting from the statement, i.e, f and Sample.txt==same file
    data = f.read()
    print(data)

with open("withExe.txt","w") as f:       # the f is an alias for the stuff resulting from the statement, i.e, f and Sample.txt==same file
    data = f.read()
    print(data)         # not readable b\c it has no thing

{don't run'}
