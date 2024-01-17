> [!CAUTION]
> ### 🚧Under Construction🚧
# Getting Started
### Start First by creating File with `.cmc` file extension 
## Example Template
```

@Resource_Pack:
 [Model_Name, Model_Directory_Input, Texture_Name, Texture_Directory_Input];
 


@Custom_Model_Data[Item Input]:
 {"predicate": {"custom_model_data": (Value) }, "model": "Model_Name" }



@Tick:
 #Tick Function - Runs Per Tick

@Load:
 #Load Function - Runs when game loads

directory/function_name:
 #custom function - Function in directory
```
> [!NOTE]
> **`@Resource_Pack` values: `Model_Name` & `Texture_Name` can be added into directory inside Resource pack. 
   Example: `Directory_Name/Model_Name`**

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
#function_name.mcfunction

execute if entity @s run say Test
execute if entity @s run summon cow
execute if entity @s run setblock ~ ~-1 ~ white_wool

```
> [!NOTE]
> **Stacked Functions(unlike Branched Functions) can be used with other commands other than `execute subcommands`**
>
> Example:
> ```
> tag @s add
> +First
> +Second
> +Third
> ```
> Output `mcfunction`:
> ```
> tag @s add First 
> tag @s add Second 
> tag @s add Third
> ```





















