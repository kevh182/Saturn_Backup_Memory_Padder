import sys

def expand_save(input_file, output_file):
    # Expand a 32KB raw save file to a 64KB 'byte-expanded' format
    try:
        with open(input_file, "rb") as f_in, open(output_file, "wb") as f_out:
            data = f_in.read()
            for byte in data:
                # Write the alternating padding byte (0xFF) followed by the actual data byte
                f_out.write(b'\xFF')
                f_out.write(bytes([byte]))
        print(f"Expanded save written to: {output_file}")
    except Exception as e:
        print(f"Error: {e}")

def contract_save(input_file, output_file):
    # Contract a 64KB byte-expanded save to a 32KB raw format
    try:
        with open(input_file, "rb") as f_in, open(output_file, "wb") as f_out:
            data = f_in.read()
            for i in range(0, len(data), 2):
                if data[i] == 0xFF:
                    f_out.write(bytes([data[i + 1]]))
                else:
                    print("Warning: Unrecognized padding byte encountered.")
                    break
        print(f"Contracted save written to: {output_file}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Saturn_Backup_Memory_Padder.py")
        print("## Expand 32kb and contract 64kb Sega Saturn Memory image files ##")
        print("")
        print("Usage")
        print("Expand 32kb to 64kb:")
        print("python Saturn_Backup_Memory_Padder.py --expand <input_file> <output_file>")
        print("")
        print("Contract 64kb to 32kb:")
        print("python Saturn_Backup_Memory_Padder.py --contract <input_file> <output_file>")
        sys.exit(1)

    operation = sys.argv[1]
    input_file = sys.argv[2]
    output_file = sys.argv[3]

    if operation == "--expand":
        expand_save(input_file, output_file)
    elif operation == "--contract":
        contract_save(input_file, output_file)
    else:
        print("Invalid operation. Use 'expand' or 'contract'.")
        sys.exit(1)
