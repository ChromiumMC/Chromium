execute as @a[tag=demo] at @s run say TICK! 
execute as @a[tag=demo] at @s run summon sheep{nbt} 
execute as @a[tag=demo] at @s run summon cow 
execute as @a[tag=player] at @s run function demo:mech/test 

