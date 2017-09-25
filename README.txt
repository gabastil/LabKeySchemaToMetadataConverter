=====================================================================================================
Instructions for Converting Schema files to Metadata JSON files
=====================================================================================================

Refer to the FAQs section below if something is unclear or not working in the following instructions.
This manual assumes the user is using Windows.

-----
Input
-----

Navigate to the Schema_to_Metadata_Converter folder in the command prompt.
Use the following command:

	convert_schema_to_json.cmd [FILE]

where FILE is the schema file name. For example, if the schema file is named
biomarker_schema_4.txt in the folder C:\Documents\Schemas, then the command would be:

	convert_schema_to_json.cmd C:\Documents\Schemas\biomarker_schema_4.txt

------
Output
------

The script will produce a json file of the same name as the schema file in the same location.

So, in the example above, the script will create "biomarker_schema_4.json" and 
put it in C:\Documents\Schemas



=====================================================================================================
Next Steps
=====================================================================================================

The metadata file needs to have a quick processing step before being loaded into LabKey. 
The LabKey project manager should be able to handle this so there are no more steps necessary 
for the schema manager.

But if the schema manager is interested in doing this step themselves,
the metadata file needs to have carriage return characters stripped out of it. 

One way to accomplish this is to 
	1) Open the json file in Notepad++
	2) Press CTRL+H to bring up the Find/Replace screen
	3) In the "Search Mode" section of the radial buttons, make sure "Extended" is activated
	4) In "Find what", enter "\r"
	5) In "Replace with", make sure the field is empty
	6) Hit "Replace All"

One way to check for carriage return characters in the file
	1) Open the json file in Notepad++
	2) Go to View > Show Symbol > Show All Characters
	3) Carriage returns will appear as a box with the letters "CR"



=====================================================================================================
FAQs
=====================================================================================================
What is a command prompt?

	This is a program used to manage files and run other programs.
	To access this, 
		1) Press the Start button at the bottom left of your screen or the Windows key on your keyboard
		2) In the search bar, type "cmd"
		3) Select "cmd.exe"

	Tutorial: http://www.cs.princeton.edu/courses/archive/spr05/cos126/cmd-prompt.html


Got an error: "convert_schema_to_json.cmd is not recognized..."

	Make sure you navigate to the folder that convert_schema_to_json.cmd is in before you try running it.
	Navigation in the command prompt is included in the tutorial above.

