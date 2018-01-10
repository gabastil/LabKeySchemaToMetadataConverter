@ECHO OFF
SET path=Converter_Files
SET py=%path%\python.exe
SET script=%path%\convert_schema_to_json.py
%py% %script% %1