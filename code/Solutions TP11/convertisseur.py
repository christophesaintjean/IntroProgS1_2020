print(f'convertisseur: {__name__}')

def deCversF(tc):
    tf = tc * 9 / 5 + 32
    return tf

def deFversC(tf):
    tc = (tf - 32) * 5 / 9
    return tc

if __name__ == "__main__":
    tc_str = input("Temperature en Celsius ? ")
    tc = float(tc_str)
    tf = deCversF(tc)
    print(f"Temperature en Farenheit: {tf} °F")