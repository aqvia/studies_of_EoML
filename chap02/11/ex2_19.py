d = {"a":1, "b":2,"c":3}

try:
    print(d["d"])
except KeyError as err:
    print("KeyError: {}".format(err))
