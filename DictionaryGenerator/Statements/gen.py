
import sys
import os
import argparse

utf8_mask = 0x7F
line_feed = '0x0a'

ap = argparse.ArgumentParser()

#Input file has to be encoded as Windows-1250
ap.add_argument("-i","--input",required=True,help =
                "Input file - lines formatted as 'enum;string'. File have to be encoded as Windows-1250")
ap.add_argument("-a","--array",required=False,default = "statements_u8_pl",help = "Hex array name")
ap.add_argument("-c","--class",required=False,default = "ScreenStatementsPL",help = "Statements class name")

v_args = vars(ap.parse_args());
hex_array_name = v_args["array"];
class_name = v_args["class"]
dir_name = "generated"

if not os.path.exists(dir_name):
    os.mkdir(dir_name)

fr=open(v_args['input'],'r');
fw_hex=open('generated/statements_utf8.c','w');
fw_map=open('generated/map.cpp','w');
fw_enum=open('generated/enum.cpp','w');

data = fr.readlines();

#Print comment note in hex file
hex_file_note = """/* IMPORTANT: DO NOT EDIT THIS FILE
*
* It have to be generated by Utilities\Statements\gen.py script.
* Usage quick quide:
* - update input CSV file by providing enum name and statement (input.csv)
* - ensure that input file is ANSI-encoded
* - generate file by running: python gen.py -i input.csv
* 
*/ """
print(hex_file_note,file = fw_hex)
print(f"const char* const {hex_array_name}[] = {{",file = fw_hex)

#Print comment note in map file
map_file_note = """/*IMPORTANT:
* This map should be generated by Utilities\Statements\gen.py script.
* Look to statements_***.c file for details.
*/ """
print(map_file_note,file = fw_map)

print("enum EScreenStatement {",file = fw_enum)

print(f"const ScreenStatementsMap {class_name}::statements{{",file = fw_map)

for sline in data:

    #Split statement string and statement name
    sline = sline.split(';')
    #Get statement name
    statement_name = sline[0]
    #Get statement name without class name
    statement_name_clean = statement_name.split('::')[1]
    #Get statement string
    statement = sline[1][0:(len(sline[1]) - 1)]

    b = bytearray(statement.encode())
    b.append(0)
    hex_list = []
    special_char = False
    for x in b:
        if special_char == True:
            if(chr(x) == "n"):
                hex_list.append(line_feed)
                special_char = False
        elif (chr(x) == "\\"):
            special_char = True
        elif (x>0) and (x<utf8_mask):
            hex_list.append(f"\'{chr(x)}\'")
        else:
            hex_list.append("0x{:02x} ".format(x))
    hex_str = ','.join(hex_list)

    #Write statement to hex file
    print(f'//{statement}',file = fw_hex)
    print(f'(const char[]){{{hex_str}}},',file = fw_hex)
    #Write statement to map file
    print(f'//{statement}',file = fw_map)
    print(f' {{ {statement_name},{hex_array_name}[{statement_name}] }},',file=fw_map)
    #Write statement name to enum file
    print(f'{statement_name_clean},',file=fw_enum)

print("};",file = fw_hex)
print("};",file = fw_map)
print("};",file = fw_enum)
    

