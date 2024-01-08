from beet import DataPack,Function
import requests


def datapack_build(pack_id,function_info):

 data = DataPack(f"{pack_id} Data_Pack")

 #built-in Functions
 for func_data in function_info:    #-----Checking------
  if func_data[0] == "": 
   None
  elif "@Resource_Pack" in func_data[0]:
    None
  elif "Custom_Model_Data" in func_data[0]:
   None
  elif func_data[0] == "@Load":
   data[f"{pack_id}:load"] = Function([f"{func_data[1]}"], tags=["minecraft:load"])
  elif func_data[0] == "@Tick":
    data[f"{pack_id}:tick"] = Function([f"{func_data[1]}"], tags=["minecraft:tick"])
  elif func_data[0] == "@Import":
    with open("test_func.mcfunction","wb") as x:
     x.write(requests.get(f"{func_data[1]}").content)
  else:  
   data[f"{pack_id}:{func_data[0]}"] = Function([f"{func_data[1]}"])
   #print("Done!") ---debug


  
 data.save(overwrite=True)
 









