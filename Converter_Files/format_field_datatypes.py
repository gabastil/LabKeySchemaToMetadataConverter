import re
import argparse

DATE = "Date"
OC = "OC"
CC = "CC"
PROPERTIES = [DATE, OC, CC]
PROPERTY_PATTERN = "|".join(PROPERTIES)
END_OF_LINE = "\r|\n|\r\n"
TABS = r"\t\t"
SPACES = r"        "
PROPERTY_SPACING = "|".join([TABS, SPACES])

PATTERN = PROPERTY_SPACING + r"\*?(" + PROPERTY_PATTERN + r")(" + END_OF_LINE + r")"


def main(file):
    with open(file, "r") as in_file:
        lines = in_file.readlines()

    out_lines = []
    last_line_was_field = False
    for line_index, line in enumerate(lines):
        if last_line_was_field:
            line = check_for_and_convert_datatype_line(line, line_index, last_line_was_field)
            last_line_was_field = False
        else:
            last_line_was_field = check_for_field_line(line)

        out_lines.append(line)

    with open(file, "w") as out_file:
        out_file.writelines(out_lines)


def check_for_field_line(line):
    last_line_was_field = False
    is_field = re.match(r"\t\S.*", line)
    if is_field:
        last_line_was_field = True
    else:
        is_field = re.match(r"    \S.*", line)
        if is_field:
            last_line_was_field = True
    return last_line_was_field


def check_for_and_convert_datatype_line(line, line_index, last_line_was_field):
    if last_line_was_field:
        has_datatype = re.match(PATTERN, line, flags=re.I)
        if has_datatype:
            line = re.sub("("+PROPERTY_PATTERN+")", r"*\1*", line, flags=re.I)
            line = line.upper()
        else:
            print("Error: expected datatype on line " + str(line_index) + " but didn't find known datatype.")
            print("Known type: " + str(PROPERTIES))
            print("Line " + str(line_index) + ": " + line)
    return line


if __name__ == '__main__':
    # Arguments:    schema_file
    parser = argparse.ArgumentParser()
    parser.add_argument("schema_file", help="the input file name")
    args = parser.parse_args()

    main(args.schema_file)
