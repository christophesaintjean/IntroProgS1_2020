def f():
    a = 2
    def local_f():
        nonlocal a
        a = 4
        print(f"local_f: {a}")

    print(f"f: {a}")
    local_f()
    print(f"f: {a}")

f()