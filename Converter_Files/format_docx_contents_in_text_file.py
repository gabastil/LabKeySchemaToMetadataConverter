import argparse

SECTION_BULLET = "â€¢"
SECTION_BULLET_2 = "aEURC/"
SECTION_BULLET_3 = "•"
SECTION_BULLETS = {SECTION_BULLET, SECTION_BULLET_2, SECTION_BULLET_3}
BOM = u"\ufeff"
BOM_SECTION_BULLET = "ï»¿â€¢"
BOM_SECTION_BULLET_2 = BOM + "aEURC/"
BOM_SECTION_BULLET_3 = BOM + "•"
BOM_SECTION_BULLET_4 = BOM + "â€¢"
BOM_SECTION_BULLETS = {BOM_SECTION_BULLET, BOM_SECTION_BULLET_2, BOM_SECTION_BULLET_3}
FIELD_BULLET = "o"
PROPERTY_BULLET = "ï‚§"
PROPERTY_BULLET_2 = "?"
PROPERTY_BULLET_3 = ""
PROPERTY_BULLETS = {PROPERTY_BULLET, PROPERTY_BULLET_2, PROPERTY_BULLET_3}


def main(in_file):
    print("Cleaning Schema...")
    with open(in_file, "r") as file:
        lines = file.readlines()

    has_bad_format = False
    out_lines = []
    for line in lines:
        if line and line != "\n":
            chunks = line.split()
            if len(chunks) > 1:

                line, has_bad_format = process_line(chunks, line, has_bad_format)

                if not has_bad_format:
                    out_lines.append(line)
                else:
                    break
            else:
                has_bad_format = True
                print("Error: expected bullet and text separated by whitespace. Line: \"" + line.rstrip() + "\"")
                break

    if not has_bad_format:
        with open(in_file, "w") as file:
            file.writelines(out_lines)
        print("Finished cleaning schema")


def process_line(chunks, line, has_bad_format):
    bullet = chunks[0]
    content = " ".join(chunks[1:]) + "\n"

    if bullet in SECTION_BULLETS:
        line = content
    elif bullet == FIELD_BULLET:
        line = "\t" + content
    elif bullet in PROPERTY_BULLETS:
        line = "\t\t" + content
    elif bullet in BOM_SECTION_BULLETS:
        line = content
    else:
        has_bad_format = True
        print("Didn't find any known type of bullet at the beginning of line: \"" + line.rstrip() + "\"")

    return line, has_bad_format


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("doc_text_schema_file", help="A text file containing the copy-pasted contents of a Microsoft Word schema")
    args = parser.parse_args()

    main(args.doc_text_schema_file)
