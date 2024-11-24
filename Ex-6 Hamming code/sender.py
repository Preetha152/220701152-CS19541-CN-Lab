def text_to_binary(text):
    return ''.join(format(ord(char), '08b') for char in text)

def calculate_redundant_bits(m):
    for r in range(m):
        if (2**r >= m + r + 1):
            return r

def position_redundant_bits(data, r):
    j = 0
    k = 1
    m = len(data)
    res = ''
    for i in range(1, m + r + 1):
        if i == 2**j:
            res += '0'
            j += 1
        else:
            res += data[-1 * k]
            k += 1
    return res[::-1]

def calculate_parity_bits(data, r):
    n = len(data)
    data = list(data)
    for i in range(r):
        val = 0
        for j in range(1, n + 1):
            if j & (2**i) == (2**i):
                val = val ^ int(data[-1 * j])
        data[-1 * (2**i)] = str(val)
    return ''.join(data)

def apply_hamming_code(data):
    m = len(data)
    r = calculate_redundant_bits(m)
    data = position_redundant_bits(data, r)
    data = calculate_parity_bits(data, r)
    return data

def save_to_file(filename, data):
    with open(filename, 'w') as file:
        file.write(data)

def main():
    text = input("Enter the text to be transmitted: ")
    binary_data = text_to_binary(text)
    print(f"Binary Representation: {binary_data}")

    hamming_code_data = apply_hamming_code(binary_data)
    print(f"Hamming Code Data: {hamming_code_data}")

    save_to_file("channel.txt", hamming_code_data)
    print("Data saved to 'channel.txt'.")

if __name__ == "__main__":
    main()
