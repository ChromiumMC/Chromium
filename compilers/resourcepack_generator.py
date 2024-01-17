from beet import ResourcePack, Texture, Model, Atlas, JsonFile, TextFile
import json

#CMD = Custom Model Data

def resourcepack_build(pack_name,resources_data):
   
 pack = ResourcePack(f"{pack_name} resource_pack")
 
 #check & split
 for rp_fetch in resources_data:

# The code block you provided is checking if the string "@Resource_Pack" is present in the first
# element of the `rp_fetch` list. If it is present, it splits the second element of `rp_fetch` by
# semicolon (;) and iterates over the resulting list (`rp_input`).
  if "@Resource_Pack" in rp_fetch[0]:
   #loads Models & Textures Inputs
   rp_input = rp_fetch[1].split(";")
   #print(rp_input)

   for rp_temp in rp_input:
   #input_values from list
    rp_data = rp_temp.strip("[").strip(" [").strip("]").strip("] \n").split(',')
    #list of inputs
    if rp_data[0] == "":
     break
    model_name = rp_data[0].strip("[").strip(" ")
    model_data = rp_data[1].strip(" ")
    texture_name = rp_data[2].strip("[").strip(" ")
    texture_data = rp_data[3].strip(" ")
    # The code `pack[f"{pack_name}:{model_name}"] = Model(source_path=f"{model_data}")` is adding a
    # model to the resource pack. It associates the model with a specific name in the format
    # "{pack_name}:{model_name}". The `source_path` parameter specifies the path to the model file.
    pack[f"{pack_name}:{model_name}"] = Model(source_path=f"{model_data}")
    pack[f"{pack_name}:{texture_name}"] = Texture(source_path=f'{texture_data}')

  #pack[f"minecraft:blocks"] = Atlas(atlases_string)



# The code block you provided is checking if the string "@Custom_Model_Data" is present in the first
# element of the `rp_fetch` list. If it is present, it performs the following steps:
  if "@Custom_Model_Data" in rp_fetch[0]:
   #loads CMD Inputs and Outputs it into json file(for items)
   # This code block is processing the input data for Custom Model Data (CMD).
   cmd_data = rp_fetch[1].replace('"model": "',f'"model": "{pack_name}:').split(';')
   #CMD JSON LIST
   cmddata_list = []
   for item_input in cmd_data:
     #input_json = json.loads(item_input)
  # The line `cmddata_list.append(json.loads(item_input))` is adding the parsed JSON object from
  # `item_input` to the `cmddata_list` list.
     cmddata_list.append(json.loads(item_input))
   
   #input_values
   item_resources = rp_fetch[0].strip("@Custom_Model_Data[").strip("]").split(",")
   item_data = item_resources[0].strip(" ")

   

  #CMD JSON 
# The code `pack.extra[f"assets\minecraft\models\{item_data}.json"] = JsonFile({...})` is creating
# a new JSON file in the resource pack. The file is located at
# "assets\minecraft\models\{item_data}.json".
 pack.extra[f"assets\\minecraft\\models\\{item_data}.json"] = JsonFile(
  {
  "parent": "item/generated",
  "textures": {
  "layer0": f"minecraft:{item_data}"
  },

  "overrides": 
  cmddata_list

  

 
  }
  )

























 pack.save(overwrite=True)













