import re

in_file = "DOE_BreastRecurrence_ANNOTATION_LABKEY_SCHEMA_8_2017-09-13.txt"
out_file = "doe_breast_recurrence_schema_8.txt"

TEXT = "Text"
DATE = "Date"
OC = "OC"
CC = "CC"
PROPERTIES = [TEXT, DATE, OC, CC]
PROPERTY_PATTERN = "|".join(PROPERTIES)
END_OF_LINE = "\r|\n|\r\n"

PATTERN = r"\t\t\*?("+PROPERTY_PATTERN+r")("+END_OF_LINE+r")"


def main():
    with open(in_file, "r") as file:
        lines = file.readlines()

    out_lines = []
    for line in lines:
        line = re.sub(PATTERN, r"\t\t*\1*\2", line, flags=re.I)
        out_lines.append(line)

    with open(out_file, "w") as file:
        file.writelines(out_lines)


if __name__ == '__main__':
    main()
