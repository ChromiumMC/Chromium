from beet import DataPack,Function
import randomcharactergenerator

#///Function Compiler for Auto Branch Functions For Datapacks 

def process_syntax(input_syntax,data,pack_id,function_name,function_tags):
    # Replace '{' and '}' with '(' and ')' respectively
    replaced_syntax = input_syntax.replace('{', '(').replace('}', ')')

    # Remove content inside curly braces
    replaced_syntax = replaced_syntax[:replaced_syntax.find('(') + 1] + "Branched_Commands"+ replaced_syntax[replaced_syntax.rfind(')'):]

    

    # The code block you provided is a function called `process_syntax` that processes the input
    # syntax and generates functions for a datapack.
    # Extract content within the curly braces
    start_brace_index = input_syntax.find('{')
    end_brace_index = input_syntax.rfind('}')

    generated_function_name = randomcharactergenerator.rand_code()

    # This code block is checking if there are curly braces `{}` in the input syntax. If there are, it
    # extracts the content inside the curly braces and assigns it to the variable
    # `content_inside_braces`.
    if start_brace_index != -1 and end_brace_index != -1:
        content_inside_braces = input_syntax[start_brace_index + 1:end_brace_index].strip()

        data[f"{pack_id}:{function_name}"] = Function([replaced_syntax.replace("(Branched_Commands)",f" function demo:embed/function_{generated_function_name.lower()}")], tags=function_tags)
        data[f"{pack_id}:embed/function_{generated_function_name.lower()}"] = Function([f"{content_inside_braces}"])

    else:
        data[f"{pack_id}:{function_name}"] = Function([f"{input_syntax}"], tags=function_tags)

if __name__ == "__main__":
    None
