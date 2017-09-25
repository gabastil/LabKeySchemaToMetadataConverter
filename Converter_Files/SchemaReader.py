import re
import string

from Globals import *


def get_schema_contents(schema_lines):
    # Read file lines, create schema object
    found_text, schema_is_valid, expected_element, schema, section, field = process_schema_lines(schema_lines)

    if not found_text:
        print("Schema file is empty.")
    elif expected_element != DROPDOWN and schema_is_valid:
        schema_is_valid = False
        index = len(schema_lines)
        if expected_element == FIELD:
            print("Error: every section requires a field. Section on line " + str(index) + " missing fields.")
        if expected_element == DATATYPE:
            print("Error: in the last section's last field, missing a " + expected_element.lower() + ". Line " + str(index))
    else:
        # Add final field and final section at end of file
        index = len(schema_lines) + 1
        schema_is_valid = check_field(field, index, schema_is_valid)
        section.fields.append(field)
        schema.append(section)

    return schema, schema_is_valid


def check_line_characters(line, line_index):
    is_blank = True
    replaced_line = ""
    for char in line:
        # check for non-ascii
        char = check_for_extended_ascii(char, line_index)
        replaced_line += char

        # check for non-whitespace
        if char not in string.whitespace:
            is_blank = False
    return is_blank, replaced_line


def check_for_extended_ascii(char, line_index):
    try:
        char.encode('ascii')
    except UnicodeEncodeError:
        # replace extended ascii with ascii or blank
        char = replace_extended_ascii(char, line_index)
    return char


def replace_extended_ascii(char, line_index):
    if char in ASCII_REPLACEMENT_DICT:
        ascii_char = ASCII_REPLACEMENT_DICT[char]
        print("Replaced extended ASCII character found in line " + str(line_index) + ": \"" + char + "\" -> \"" + ascii_char + "\"")
    else:
        print("Warning: Extended ASCII character found in line " + str(line_index) + ". Replacing it and continuing")
        ascii_char = ''
    return ascii_char


def read_schema_line(line, line_index):
    text_index = 0
    tab_count = 0

    line, schema_is_valid = check_spacing(line, line_index)

    # Count tabs
    for index, char in enumerate(line):
        if char == TAB:
            tab_count += 1
        else:
            text_index = index
            break

    # Derive level
    level = get_level(tab_count)
    if level == ERROR:
        schema_is_valid = False
        print("Error: too many tabs in line " + str(line_index) + ": \"" + line + "\"")

    # Get value
    value = line[text_index:]
    value = value.rstrip("\r\n")
    value = re.sub(r"\"", "'", value)

    return value, level, schema_is_valid


def check_spacing(line, line_index):
    schema_is_valid = True

    # Get leading whitespace
    index = 0
    space_count = 0
    whitespace = ""
    for index, char in enumerate(line):
        if char in string.whitespace:
            whitespace += char

            if char == " ":
                space_count += 1
        else:
            break

    # Check if spaces are equivalent to tabs
    if space_count % TAB_EQUIVALENT_COUNT != 0:
        schema_is_valid = False
        print("Error: line not properly spaced in line " + str(line_index) + ": " + line)

    # Substitute spaces
    whitespace = re.sub(TAB_EQUIVALENT, TAB, whitespace)
    line = whitespace + line[index:]

    return line, schema_is_valid


def get_level(tab_count):
    level = ERROR
    if tab_count == SECTION_TABS:
        level = SECTION
    elif tab_count == FIELD_TABS:
        level = FIELD
    elif tab_count == PROPERTY_TABS:
        level = PROPERTY
    return level


def process_schema_lines(schema_lines):
    schema_is_valid = False
    found_text = False
    schema = []  # List of Section objects
    section = Section()
    field = Field()

    expected_element = SECTION

    for line_index, line in enumerate(schema_lines):
        line_index += 1
        is_blank, line = check_line_characters(line, line_index)

        if not is_blank:
            found_text = True
            value, level, schema_is_valid = read_schema_line(line, line_index)

            if schema_is_valid:
                # Add information from line to schema object
                schema, section, field, expected_element, schema_is_valid = process_schema_line(value, level, field, section, schema, schema_is_valid, line_index, expected_element)

            if not schema_is_valid:
                break

    return found_text, schema_is_valid, expected_element, schema, section, field


def process_schema_line(value, level, field, section, schema, schema_is_valid, line_index, expected_element):

    if expected_element == SECTION:
        section, expected_element, schema_is_valid = process_schema_section(value, level, schema_is_valid, line_index)
    elif expected_element == FIELD:
        field, expected_element, schema_is_valid = process_schema_field(value, level, field, schema_is_valid, line_index)
    elif expected_element == DATATYPE:
        field, expected_element, schema_is_valid = process_schema_field_datatype(value, level, field, schema_is_valid, line_index)
    elif expected_element == DROPDOWN:
        schema, section, field, expected_element, schema_is_valid = process_schema_field_dropdown(value, level, field, section, schema, schema_is_valid, line_index)

    return schema, section, field, expected_element, schema_is_valid


def process_schema_section(line_value, line_level, schema_is_valid, line_index):
    if line_level != SECTION:
        schema_is_valid = False
        print("Error: expected section, but line " + str(line_index) + " not in section format: \"" + line_value + "\"")

    section = Section(line_value)
    expected_element = FIELD

    return section, expected_element, schema_is_valid


def process_schema_field(line_value, line_level, field, schema_is_valid, line_index):
    if line_level != FIELD:
        schema_is_valid = False
        print("Error: Sections must have at least 1 field. Expected field, but line " + str(line_index) + " not in field format: \"" + line_value + "\"")
        expected_element = ERROR
    else:
        field = Field(line_value)
        expected_element = DATATYPE

    return field, expected_element, schema_is_valid


def process_schema_field_datatype(line_value, line_level, field, schema_is_valid, line_index):
    if line_level != PROPERTY:
        schema_is_valid = False
        print("Error: Fields must have a datatype. Expected datatype, but line " + str(line_index) + " not in datatype format: \"" + line_value + "\"")
        expected_element = ERROR
    else:
        line_datatype = line_value.lower()
        line_datatype = re.sub("\*", "", line_datatype)

        if line_datatype not in DATATYPES:
            schema_is_valid = False
            print("Error: Fields must have a datatype specified. Valid datatypes: " + str(DATATYPES) + ". Line " + str(line_index) + ": \"" + line_value + "\"")
            expected_element = ERROR
        else:
            field = set_datatype_and_class_type(field, line_datatype)
            expected_element = DROPDOWN

    return field, expected_element, schema_is_valid


def set_datatype_and_class_type(field: Field, line_datatype):
    if line_datatype == DATE:
        field.datatype = DATE
        field.class_type = OC
    else:
        field.datatype = TEXT
        field.class_type = line_datatype
    return field


def process_schema_field_dropdown(line_value, line_level, field, section, schema, schema_is_valid, line_index):
    if line_level == PROPERTY:
        field.dropdown.append(line_value)
        expected_element = DROPDOWN

    elif line_level == FIELD:
        # Add last field to section
        schema_is_valid = check_field(field, line_index, schema_is_valid)
        section.fields.append(field)
        field = Field(line_value)

        # Move on to datatype of new field
        expected_element = DATATYPE

    elif line_level == SECTION:
        # Add last field to previous section
        schema_is_valid = check_field(field, line_index, schema_is_valid)
        section.fields.append(field)
        field = Field(line_value)

        # Add last section to schema
        schema.append(section)
        section = Section(line_value)

        # Move on to first field of new section
        expected_element = FIELD

    else:
        schema_is_valid = False
        print("Error: Unexpected format in line" + str(line_index) + ": \"" + line_value + "\"")
        expected_element = ERROR

    return schema, section, field, expected_element, schema_is_valid


def check_field(field: Field, line_index, schema_is_valid):
    line_index -= 1

    if field.datatype == TEXT:
        if field.class_type == CC:
            if not field.dropdown:
                schema_is_valid = False
                print("Error: field is Closed Class but has no options in the dropdown. Line: " + str(line_index))
    elif field.datatype == DATE:
        if field.dropdown:
            print("Warning: field set as Date but has items given for dropdown. Line: " + str(line_index))

    return schema_is_valid