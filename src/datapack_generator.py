from beet import DataPack,Function
import requests
from compilers.functions_compiler import process_syntax


def datapack_build(pack_id,function_info):

 data = DataPack(f"{pack_id} data_pack")

 #built-in Functions
# The code snippet is iterating over each `func_data` in the `function_info` list. It then checks the
# value of `func_data[0]` to determine what action to take.
 for func_data in function_info:    #-----Checking------
  if func_data[0] == "": 
   None
  elif "@Resource_Pack" in func_data[0]:
   None
  elif "Custom_Model_Data" in func_data[0]:
   None
  elif func_data[0] == "@Load":
   process_syntax(func_data[1].strip("\n"),data,pack_id,"load",["minecraft:load"])
  elif func_data[0] == "@Tick":
   process_syntax(func_data[1].strip("\n"),data,pack_id,"tick",["minecraft:tick"])
  elif func_data[0] == "@Import":
    with open("test_func.mcfunction","wb") as x:
     x.write(requests.get(f"{func_data[1]}").content)
  else:  
   process_syntax(func_data[1].strip("\n"),data,pack_id,func_data[0],None)
   #print("Done!") ---debug


  
 data.save(overwrite=True)
 









