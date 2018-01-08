import argparse

SECTION_CHAR = "â€¢"
FIELD_CHAR = "o"
PROPERTY_CHAR = "ï‚§"
PROPERTY_CHAR_2 = "?"


def main(in_file, out_file):
    with open(in_file, "r") as in_file:
        lines = in_file.readlines()

    out_lines = []
    for line in lines:
        if line:
            if SECTION_CHAR in line:
                line = line.lstrip(SECTION_CHAR)
                line = line.lstrip()
            elif line[0] == FIELD_CHAR:
                line = line.lstrip(FIELD_CHAR)
                line = line.lstrip()
                line = "\t" + line
            elif PROPERTY_CHAR in line:
                line = line.lstrip(PROPERTY_CHAR)
                line = line.lstrip()
                line = "\t\t" + line
            elif line[0] == PROPERTY_CHAR_2:
                line = line.lstrip(PROPERTY_CHAR_2)
                line = line.lstrip()
                line = "\t\t" + line

        out_lines.append(line)

    with open(out_file, "w") as file:
        file.writelines(out_lines)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("doc_text_schema_file", help="A text file containing the copy-pasted contents of a Microsoft Word schema")
    parser.add_argument("txt_schema_file",
                        help="A text file containing the copy-pasted contents of a Microsoft Word schema")
    args = parser.parse_args()

    main(args.doc_text_schema_file, args.txt_schema_file)
