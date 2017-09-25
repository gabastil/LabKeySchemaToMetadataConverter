JSON_EXTENSION = ".json"

SCHEMA = "SCHEMA"
METADATA = "METADATA"

info_file = "Converter_Files\\"
json_header_file = info_file + "json_header.txt"
json_footer_file = info_file + "json_footer.txt"

TABLE_SPACING = "      "
FIELD_LIST_SPACING = "        "
FIELD_SPACING = "          "
PROPERTY_SPACING = "            "
DROPDOWN_SPACING = "              "

# Table level
TABLE_LINE_START = TABLE_SPACING + "{\"table\":\""
TABLE_LINE_END = "\",\n"
FINAL_TABLE_END_LINE = TABLE_SPACING + "}\n"
CONTINUING_TABLE_END_LINE = TABLE_SPACING + "},\n"

# Field level
FIELD_LIST_LINE = FIELD_LIST_SPACING + "\"fields\":[\n"
FIELD_LIST_END_LINE = FIELD_LIST_SPACING + "]\n"
FIELD_LINE_START = FIELD_SPACING + "{\"field\":\""
FIELD_LINE_END = "\",\n"
FINAL_FIELD_END_LINE = FIELD_SPACING + "}\n"
CONTINUING_FIELD_END_LINE = FIELD_SPACING + "},\n"

# Property level
TEXT = "text"
DATE = "date"
OC = "oc"
CC = "cc"

DATATYPES = [OC, CC, DATE]

property_conversion_table = {
    TEXT: "string",
    DATE: "date",
    OC: "False",
    CC: "True"
}

DATATYPE_LINE_START = PROPERTY_SPACING + "\"datatype\":\""
DATATYPE_LINE_END = "\",\n"
CLASS_LINE_START = PROPERTY_SPACING + "\"closedClass\":\""
CLASS_LINE_END = "\",\n"
DISEASE_PROPERTIES_LINE = PROPERTY_SPACING + "\"diseaseProperties\":\n"
DISEASE_PROPERTIES_END_LINE = PROPERTY_SPACING + "]\n"
DISEASE_PROPERTIES_START_BRACKET_LINE = PROPERTY_SPACING + "[\n"
DISEASE_PROPERTIES_END_BRACKET_LINE = PROPERTY_SPACING + "]\n"

# Dropdown level
DISEASE_GROUP_LINE = DROPDOWN_SPACING + "{\"diseaseGroup\":[\"*\"],\n"
DROPDOWN_OPTIONS_LINE_START = DROPDOWN_SPACING + "\"values\":[\""
DROPDOWN_OPTIONS_LINE_END = "\"]\n"
DISEASE_GROUP_END_LINE = DROPDOWN_SPACING + "}\n"


# Schema file components
class Field:
    def __init__(self, name="NO NAME FIELD"):
        self.name = name
        self.datatype = TEXT
        self.class_type = OC
        self.dropdown = []


class Section:
    def __init__(self, name="NO NAME SECTION"):
        self.name = name
        self.fields = []


TAB = '\t'
TAB_EQUIVALENT = '    '
TAB_EQUIVALENT_COUNT = len(TAB_EQUIVALENT)

SECTION_TABS = 0
FIELD_TABS = 1
PROPERTY_TABS = 2

SECTION = "SECTION"
FIELD = "FIELD"
PROPERTY = "PROPERTY"
ERROR = "BAD"

DATATYPE = "DATATYPE"
CLASS = "CLASS"
DROPDOWN = "DROPDOWN"

ASCII_REPLACEMENT_DICT = {
    "–": "-"
}
