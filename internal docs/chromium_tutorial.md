> [!CAUTION]
> ### 🚧 Under Contruction🚧
# Chromium Language

## Example Template
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

## Built-In Arguments
```
@Tick: Tick Function
@Load: Load Function
@Resource_Pack: Adds Resource Pack
@Custom_Model_Data: Adds Custom Model Arguments for Resource Pack

```

## Functions & Directories
To Create a Function:
```
function_name:
 function contents

```
To Create a Function Within a Directory:
```
directory_name/function_name:
 function Contents

```

## Branched Functions

To Create a Branched Function:
```
function_name:
execute as @a at @s run{
say Test
summon cow
setblock ~ ~-1 ~ white_wool
}

```
Output:
```
#function_name.mcfunction

execute as @a at @s run filename:embed/generated_function

```
Also:
  ```
#embed/generated_function

say Test
summon cow
setblock ~ ~-1 ~ white_wool

```

## Stacked Functions

To Create a Stacked Function:
```
function_name:
execute if entity @s run
+say Test
+summon cow
+setblock ~ ~-1 ~ white_wool


```
Output:
```
execute if entity @s run say Test
execute if entity @s run summon cow
execute if entity @s run setblock ~ ~-1 ~ white_wool

```
> [!NOTE]
> **Stacked Functions(unlike Branched Functions) can be used with other commands other than `execute subcommands`**




















