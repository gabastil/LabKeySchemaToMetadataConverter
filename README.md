# SchemaToMetadataConverter
Converts text file annotation schemas into metadata JSON files useable by LabKey Software

## Instructions for Converting Files
This manual assumes the user is using Windows.

**Input**

Navigate to the Schema_to_Metadata_Converter folder in the command prompt.
Use the following command:

```convert_schema_to_json.cmd [FILE]```

where FILE is the schema file name. For example, if the schema file is named
biomarker_schema_4.txt in the folder C:\Documents\Schemas, then the command would be:

```convert_schema_to_json.cmd C:\Documents\Schemas\biomarker_SCHEMA_v4.txt```


**Output**

The script will produce a json file of the same name as the schema file, except for swapping "schema" for "METADATA", in the same location.

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

The schema cannot contain double quote characters ["]. Any found in the file will be converted to single quotes ['].

The conversion script has functionality to make things easier:
1. The script will check for schema validity
2. Capitalization for anything and asterisks for datatypes are not necessary
3. An additional script is available to automatically add asterisks to datatypes in an otherwise completed schema, if desired