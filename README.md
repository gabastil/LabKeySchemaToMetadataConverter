# SchemaToMetadataConverter
Converts text file annotation schemas into metadata JSON files useable by LabKey Software

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
Spacing indicates the element:
* 0 tabs = Section
* 1 tab =  Field
* 2 tabs = Datatype or Dropdown List Option

The schema file will be processed by script to convert it to a format readable by LabKey software, called a metadata file.
In order for this to work, the file must follow the format shown in this document.

The schema cannot contain double quote characters ["]. Any found in the file will be automatically converted to single quotes ['].

However, the script has functionality to make things easier:
1. The script will check for schema validity
2. Capitalization for anything and asterisks for datatypes are not necessary
3. An additional script is available to automatically add asterisks to datatypes in an otherwise completed schema, if desired