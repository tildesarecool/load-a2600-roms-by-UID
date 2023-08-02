def find_duplicates(log_file):
    hex_to_filenames = {}
    duplicate_hex_strings = []

    with open(log_file, "r") as infile:
        for line in infile:
            filename, hex_string = line.strip().split('\t')
            if hex_string in hex_to_filenames:
                duplicate_hex_strings.append(hex_string)
            else:
                hex_to_filenames[hex_string] = [filename]

    return duplicate_hex_strings, hex_to_filenames

if __name__ == "__main__":
    log_file = "conversion_log_all_250.txt"

    duplicate_hex_strings, hex_to_filenames = find_duplicates(log_file)

    if duplicate_hex_strings:
        print("Duplicates found:")
        for hex_string in duplicate_hex_strings:
            filenames = hex_to_filenames[hex_string]
            print(f"Hex string: {hex_string}")
            for filename in filenames:
                print(f"    {filename}")
    else:
        print("No duplicates found.")
