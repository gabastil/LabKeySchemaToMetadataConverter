@ECHO OFF
SET path=Converter_Files
SET py=%path%\python.exe
SET cleaner_script=%path%\format_docx_contents_in_text_file.py
SET converter_script=%path%\convert_schema_to_json.py
%py% %cleaner_script% %1
%py% %converter_script% %1