d = {"a":1, "b":2,"c":3}

try:
    print(d["d"])
except Exception as err:
    print(type(err))
    print(err)
