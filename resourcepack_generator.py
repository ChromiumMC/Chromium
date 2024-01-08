from beet import ResourcePack, Texture, Model, Atlas, JsonFile, TextFile
import json

#CMD = Custom Model Data

def resourcepack_build(pack_name,resources_data):
   
 pack = ResourcePack(f"{pack_name} Resource_Pack")
 
 #check & split
 for rp_fetch in resources_data:

  if "@Resource_Pack" in rp_fetch[0]:
   #loads Models & Textures Inputs
   rp_input = rp_fetch[1].split(";")
   #print(rp_input)

   for rp_temp in rp_input:
   #input_values from list
    rp_data = rp_temp.strip("[").strip(" [").strip("] \n").split(',')
    #list of inputs
    if rp_data[0] == "":
     break
    model_name = rp_data[0].strip(" ")
    model_data = rp_data[1].strip(" ")
    texture_name = rp_data[2].strip(" ")
    texture_data = rp_data[3].strip(" ")
    #output compiler
    #models and textures
    pack[f"{pack_name}:{model_name}"] = Model(source_path=f"{model_data}")
    pack[f"{pack_name}:{texture_name}"] = Texture(source_path=f'{texture_data}')

  #pack[f"minecraft:blocks"] = Atlas(atlases_string)



  if "@Custom_Model_Data" in rp_fetch[0]:
   #loads CMD Inputs and Outputs it into json file(for items)
   cmd_data = rp_fetch[1].replace('"model": "',f'"model": "{pack_name}:').split(';')
   #CMD JSON LIST
   cmddata_list = []
   for item_input in cmd_data:
     #input_json = json.loads(item_input)
     cmddata_list.append(json.loads(item_input))
   
   #input_values
   item_resources = rp_fetch[0].strip("@Custom_Model_Data[").strip("]").split(",")
   item_data = item_resources[0].strip(" ")

   

  #CMD JSON 
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













