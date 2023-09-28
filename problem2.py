def floating_model(f):
    if f == 0.0:
        return "0" * 14
    elif f == float("inf") or f == float("-inf"):
        return "0" + "1" * 5 + "0" * 8

    sign_bit = "0"
    if f < 0:
        sign_bit = "1"
        f = abs(f)

    exponent = 0
    while f >= 2.0:
        f /= 2.0
        exponent += 1
    while f < 1.0:
        f *= 2.0
        exponent -= 1
    exponent_bits = format(exponent + 15, "05b")

    mantissa_bits = ""
    for _ in range(8):
        f *= 2.0
        bit = "1" if f >= 1.0 else "0"
        mantissa_bits += bit
        if f >= 1.0:
            f -= 1.0

    return sign_bit + exponent_bits + mantissa_bits


try:
    float_num = float(input("Enter a floating-point number: "))
    binary_representation = floating_model(float_num)
    print("14-bit binary representation:", binary_representation)
except ValueError:
    print("Invalid input. Please enter a valid floating-point number.")
