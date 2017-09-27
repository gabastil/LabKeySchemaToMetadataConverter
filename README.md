# LabKeySchemaToMetadataConverter
Converts text file annotation schemas into metadata JSON files useable by LabKey Software

## Instructions for Converting Files
This manual assumes the user is using Windows and is familiar with the command prompt.
Here is a [command prompt tutorial](http://www.cs.princeton.edu/courses/archive/spr05/cos126/cmd-prompt.html "Princeton Commant Prompt Tutorial") for reference.

### Setup

1. Click the green "Clone or download" button and click "Download ZIP". 
2. Find downloaded folder, right click it to bring up a menu, and proceed with "Extract All"
3. Open the LabKeySchemaToMetadataConverter folder

### Input

Navigate to the Schema_to_Metadata_Converter folder in the command prompt.
Use the following command:

```convert_schema_to_json.cmd SCHEMA_FILE```

where FILE is the schema file name. For example, if the schema file is named
biomarker_schema_4.txt in the folder C:\Documents\Schemas, then the command would be:

```convert_schema_to_json.cmd C:\Documents\Schemas\biomarker_SCHEMA_v4.txt```


### Output

The script will produce a json file of the same name as the schema file, except for swapping "schema" for "METADATA", and put it in the same location.

So, in the example above, the script will create "biomarker_METADATA_v4.json" and
put it in C:\Documents\Schemas


## Annotation Schema Format
LabKey annotation schemas consist of fields which are divided into sections.

Each field must specify:
* Its data type, one of [OC, CC, Date]
    * Open Class (OC) indicates a value may either be manually entered into the field, or selected from the dropdown list
	* Closed Class (CC) indicates a value can only be selected from the dropdown list
	* Date indicates a value to be selected from a calendar
* Possible values to be listed in its dropdown list (if applicable)


**Template:**

```
Section Name 1
	Field Name 1
		*Field data type*
		Dropdown Option 1
		Dropdown Option 2
		...
	Field Name 2
		*Field data type*
		Dropdown Option 1
		Dropdown Option 2
		...
	...
Section Name 2
	Field Name 1
		*Field data type*
		Dropdown Option 1
		Dropdown Option 2
		...
	Field Name 2
		*Field data type*
		Dropdown Option 1
		Dropdown Option 2
		...
	...
...
```

**Example:**

```
Loco-Regional Recurrence
	Local Recurrence - Breast
		*CC*
		Positive
		Negative
		Not evaluated
	Resection and/or Dissection
		*CC*
		Mastectomy
		Radical Mastectomy
		Axillary Dissection
		Sentinel Lymph Node Excision
Distant Recurrence
	Procedure type
		*OC*
	Specimen report date
		*Date*
	Distant Metastasis Site
		*OC*
		Liver
		Lung (incl. Malignant Pleural Effusion)
		Bone
		Brain
		Distant Lymph Nodes
```

## Notes for Schema Creators
Spacing indicates whether something is a section, field, or field property:
* 0 tabs = Section
* 1 tab =  Field
* 2 tabs = Datatype or Dropdown List Option

The schema cannot contain:
* Double quote characters ["]. Any found in the file will be converted to single quotes ['].
* Non-ASCII/Extended-ASCII characters (i.e. less common special characters, characters from non-English languages). Any found will be replaced or removed.

The conversion script has functionality to make schema development easier:
1. The script will check for schema validity
2. Capitalization for anything and asterisks for datatypes are not necessary
3. An additional script is available to automatically [add asterisks to datatypes](Converter_Files/format_field_datatypes.py) in an otherwise completed schema, if desired.

## Notes for Metadata Managers

After conversion, the metadata file needs to have a quick processing step before being loaded into LabKey.
This entails having carriage return characters stripped out of it.

One way to accomplish this is to
1. Open the json file in Notepad++
2. Press CTRL+H to bring up the Find/Replace screen
3. In the "Search Mode" section of the radial buttons, make sure "Extended" is activated
4. In "Find what", enter "\r"
5. In "Replace with", make sure the field is empty
6. Hit "Replace All"

One way to check for carriage return characters in the file
1. Open the json file in Notepad++
2. Go to View > Show Symbol > Show All Characters
3. Carriage returns will appear as a box with the letters "CR"
