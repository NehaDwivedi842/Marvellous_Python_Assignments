def remove_blank_lines(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            if line.strip(): 
                outfile.write(line)

remove_blank_lines("marks.txt", "cleaned_marks.txt")
