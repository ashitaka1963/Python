def zero_padding(input, digits):
    # 右寄せゼロ埋め: zfill
    return str(input).zfill(digits)

input = 33
digits = 3

output = zero_padding(input, digits)
print(output) # 033