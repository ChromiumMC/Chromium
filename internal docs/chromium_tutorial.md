## Chromium Language

### Example Code
```

@Resource_Pack:
 [Model Name, Model Directory, Texture Name, Directory];
 


@Custom_Model_Data[Item Input]:
 {"predicate": {"custom_model_data": 1000 }, "model": "item/tablet_model" }



@Tick:
 #Tick Function - Runs Per Tick

@Load:
 #Load Function - Runs when game loads

directory/function_name:
 #custom function - Function in directory
```

### Built-In Arguments
```
@Tick: Tick Function
@Load: Load Function
@Resource_Pack: Adds Resource Pack
@Custom_Model_Data: Adds Custom Model Arguments for Resource Pack

```

### Functions & Directories
To Create a Function:
```
Function_Name:
 Function Contents

```
To Create a Function Within a Directory:
```
directory_name/function_name:
 function Contents

```





