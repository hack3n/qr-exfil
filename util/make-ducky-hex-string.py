with open("../qr-exfil.html", "rb") as file:
    binary_data = file.read()
    hex_string_lower = binary_data.hex().lower()

chunk_size = 10000
buffer_size = 10
delay = 400

num_chunks = (len(hex_string_lower) // chunk_size) + 1

for i in range(num_chunks):
    chunk = hex_string_lower[i * chunk_size: (i + 1) * chunk_size]
    filename = f"qr-exfil-hex{i + 1}.txt"
    num_buffers = (len(chunk) // buffer_size)
    output = ""
    
    for j in range(num_buffers):
        buff_chunk = chunk[j * buffer_size: (j + 1) * buffer_size]
        output += f"STRING {buff_chunk}\n"
        output += f"DELAY {delay}\n"
        
    with open(filename, 'w') as file:
        file.write(output)
