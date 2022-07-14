import os


dict_type = "DictIntStr_t"
dict_name = "WdtTaskDict"
fw=open('dict.c','w');
fr=open('input.txt','r');


data = fr.readlines();

print(f"{dict_type} {dict_name} = {{",file = fw)

for sline in data:
    sep = ','
    stripped = sline.split(sep, 1)[0]
    new_s = stripped.strip()
    print(f"{{ {new_s}, \"{new_s}\" }},",file = fw)


print("};",file = fw)
