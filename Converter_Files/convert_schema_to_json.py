import argparse
import os
from typing import List
from SchemaReader import *


def main(schema_file):
    print("Checking schema...")

    json_file = get_file_path_and_names(schema_file)

    try:
        with open(schema_file, "rU", encoding="utf-8") as in_file:
            schema_lines = in_file.readlines()
        convert_file(json_file, schema_lines)

    except IOError:
        print("Error: could not locate " + schema_file)


def convert_file(json_file, schema_lines):
    json_file_content = []

    schema_contents, schema_is_valid = get_schema_contents(schema_lines)

    if schema_is_valid:
        print("Schema is valid. Converting to JSON...")
        # Get header
        json_file_content, schema_is_valid = get_header_or_footer(json_file_content, json_header_file, schema_is_valid)
        # Convert schema lines to json
        json_file_content = convert_schema_lines_to_json(schema_contents, json_file_content)
        # Get footer
        json_file_content, schema_is_valid = get_header_or_footer(json_file_content, json_footer_file, schema_is_valid)

        if schema_is_valid:
            write_json_file(json_file_content, json_file)


def get_header_or_footer(json_file_content, file, schema_is_valid):
    try:
        with open(file, "rU", encoding="utf8") as in_file:
            lines = in_file.readlines()

        json_file_content.extend(lines)
    except IOError:
        schema_is_valid = False
        print("Error: can't find supporting file " + file + " from current directory " + os.getcwd())
    return json_file_content, schema_is_valid


def convert_schema_lines_to_json(schema: List[Section], json_file_content: List):
    for section_index, section in enumerate(schema):
        section_line = TABLE_LINE_START + section.name + TABLE_LINE_END
        json_file_content.append(section_line)
        json_file_content.append(FIELD_LIST_LINE)

        for field_index, field in enumerate(section.fields):
            # Field name line
            field_line = FIELD_LINE_START + field.name + FIELD_LINE_END
            json_file_content.append(field_line)

            # Datatype line
            datatype = property_conversion_table[field.datatype]
            datatype_line = DATATYPE_LINE_START + datatype + DATATYPE_LINE_END
            json_file_content.append(datatype_line)

            # Class type line
            class_type = property_conversion_table[field.class_type]
            class_type_line = CLASS_LINE_START + class_type + CLASS_LINE_END
            json_file_content.append(class_type_line)

            # Dropdown options lines
            json_file_content = add_dropdown_lines(json_file_content, field.dropdown)

            # Field ending line
            if field_index == len(section.fields) - 1:
                json_file_content.append(FINAL_FIELD_END_LINE)
            else:
                json_file_content.append(CONTINUING_FIELD_END_LINE)

        # Section ending lines
        json_file_content.append(FIELD_LIST_END_LINE)

        if section_index == len(schema) - 1:
            json_file_content.append(FINAL_TABLE_END_LINE)
        else:
            json_file_content.append(CONTINUING_TABLE_END_LINE)

    return json_file_content


def add_dropdown_lines(json_file_content, dropdown_list):
    json_file_content.append(DISEASE_PROPERTIES_LINE)
    json_file_content.append(DISEASE_PROPERTIES_START_BRACKET_LINE)
    json_file_content.append(DISEASE_GROUP_LINE)

    dropdown_options = "\", \"".join(dropdown_list)
    dropdown_line = DROPDOWN_OPTIONS_LINE_START + dropdown_options + DROPDOWN_OPTIONS_LINE_END
    json_file_content.append(dropdown_line)

    json_file_content.append(DISEASE_GROUP_END_LINE)
    json_file_content.append(DISEASE_PROPERTIES_END_BRACKET_LINE)

    return json_file_content


def write_json_file(json_file_content, json_filename):
    try:
        with open(json_filename, "w", encoding="ascii") as out_file:
            out_file.writelines(json_file_content)
        print("Done")
    except IOError:
        print("Error: could not locate destination for " + json_filename)
    except UnicodeEncodeError:
        print("Error: character encoding error. ")
        with open(json_filename, "w", encoding="ascii") as out_file:
            out_file.write("Schema Conversion Failed - character encoding issue")


def get_file_path_and_names(schema_file):
    # Get path and schema file name
    path_chunks = schema_file.split("\\")
    schema_filename = path_chunks[-1]
    path = "\\\\".join(path_chunks[0:-1])

    # Create json file name and path from schema file
    json_filename = get_metadata_filename(schema_filename)
    json_filename = re.sub(SCHEMA, METADATA, json_filename, flags=re.I)

    if path:
        json_file = path + "\\\\" + json_filename
    else:
        json_file = json_filename

    return json_file


def get_metadata_filename(schema_filename):
    # remove extension (anything after final dot) and replace with new extension
    name = ".".join(schema_filename.split(".")[0:-1])
    return name + JSON_EXTENSION


if __name__ == '__main__':
    # Arguments:    schema_file
    parser = argparse.ArgumentParser()
    parser.add_argument("schema_file", help="the input file name")
    args = parser.parse_args()

    main(args.schema_file)
