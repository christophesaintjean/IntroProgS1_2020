def f():
    a = "f"

    def local_f():
        nonlocal a
        a = "local_f"
        print(f"local_f: {a}")

    print(f"f: {a}")
    local_f()
    print(f"f: {a}")

f()