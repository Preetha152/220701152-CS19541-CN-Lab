def read_from_file(filename):
    with open(filename, 'r') as file:
        return file.read()

def calculate_redundant_bits(m):
    for r in range(m):
        if (2**r >= m + r + 1):
            return r

def detect_error(data, r):
    n = len(data)
    data = list(data)
    error_position = 0
    for i in range(r):
        val = 0
        for j in range(1, n + 1):
            if j & (2**i) == (2**i):
                val = val ^ int(data[-1 * j])
        error_position += val * (2 ** i)  
    return error_position

def correct_error(data, error_position):
    data = list(data)
    if error_position > 0:
        data[-1 * error_position] = '1' if data[-1 * error_position] == '0' else '0'
    return ''.join(data)

def remove_redundant_bits(data, r):
    j = 0
    res = ''
    for i in range(1, len(data) + 1):
        if i != 2 ** j:
            res = res + data[-1 * i]
        else:
            j += 1
    return res[::-1]

def binary_to_text(binary_data):
    
    text = ''.join(chr(int(binary_data[i:i + 8], 2)) for i in range(0, len(binary_data), 8))
    return text

def main():
    hamming_code_data = read_from_file("channel.txt")
    print(f"Received Hamming Code Data: {hamming_code_data}")

    m = len(hamming_code_data)
    r = calculate_redundant_bits(m)
    error_position = detect_error(hamming_code_data, r)

    if error_position == 0:
        print("No error detected.")
    else:
        print(f"Error detected at position: {error_position}")
        hamming_code_data = correct_error(hamming_code_data, error_position)
        print(f"Corrected Hamming Code Data: {hamming_code_data}")

    binary_data = remove_redundant_bits(hamming_code_data, r)
    text = binary_to_text(binary_data)
    print(f"Decoded Text: {text}")

if __name__ == "__main__":
    main()
