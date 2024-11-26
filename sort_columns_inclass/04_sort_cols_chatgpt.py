def sort_file_by_columns(input_file, output_file, primary_index=0, secondary_index=0, delimiter=',', reverse=False):
    # Open the input file and read all the lines.
    with open(input_file, 'r') as f:
        lines = f.readlines()

    # Separate the first two lines (unsorted) and the rest (to be sorted)
    header = lines[0].strip().split(delimiter)
    spacer = lines [1]
    body = lines[2:]

    # Sort the body by primary and secondary columns (case-insensitive)
    sorted_body = sorted(
        body,
        key=lambda line:(
            line.split(delimiter) [primary_index].lower(), # Primary sort
            line.split(delimiter) [secondary_index].lower() # Secondary sort
        ),
        reverse=reverse # Apply reverse sorting if needed
    )

    # Format the header with aligned columns.
    header_str = f"{header[0]:<35} {header[1]:<21} {header[2]:<15}\n" # Adjust the width for each column.
    body_str = ''.join([f"{line.split(delimiter)[0]:<35} {line.split(delimiter)[1]:<21} {line.split(delimiter)[2]:<15}\n"
                        for line in sorted_body])

    # Combine the header and sorted body
    #sorted_lines = header + sorted_body

    # Write the result to the output file
    with open(output_file, 'w') as f:
        f.write(header_str) # Write the header
        f.write(spacer)
        f.writelines(body_str) # Write the sorted body

# Specify input and output file names
input_file = 'dinosaurs.csv'
output_file = '04_dino_output.txt'

# Sort by the first column, then by the second column
sort_file_by_columns(input_file, output_file, primary_index=0, secondary_index=1, delimiter=',', reverse=False)