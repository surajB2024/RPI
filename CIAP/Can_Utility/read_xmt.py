def parse_xmt_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    data = []


    for line in lines:
        # Skip comments and empty lines
        if line.startswith(';') or not line.strip():
            continue
        
        # Split the line into components
        parts = line.split()
        if len(parts) < 6:  # Ensure there's enough data
            continue
        
        message_id = parts[0]
        cycle_time = parts[1]
        data_length = parts[2]
        frame_type = parts[3]
        message_data = ' '.join(parts[4:-1])  # Join message data excluding the comment
        comment = parts[-1] if len(parts) > 5 else ""

        # Store the parsed data
        data.append({
            'Message ID': message_id,
            'Cycle Time (ms)': cycle_time,
            'Data Length': data_length,
            'Frame Type': frame_type,
            'Message Data': message_data,
            'Comment': comment
        })

    return data

# Path to your XMT file
file_path = "/home/Sharukh/CIAP/Can_Utility/TCU_DFT_181021.xmt"

# Parse the file and print the results
parsed_data = parse_xmt_file(file_path)

for entry in parsed_data:
    print(entry)
