import ams_compiler as compiler
import re
from compilers.datapack_generator import datapack_build
from compilers.resourcepack_generator import resourcepack_build

def main(input_file, debug_mode=True):
    """
    The main function reads an input file, processes the syntax content, splits it into blocks, and then
    creates a file from each block using the create_file_from_syntax function.
    
    :param input_file: The input_file parameter is the path to the file that contains the syntax content
    to be processed
    :param debug_mode: The `debug_mode` parameter is a boolean flag that determines whether or not debug
    information should be included in the compiled data. If `debug_mode` is `True`, then debug
    information will be included. If `debug_mode` is `False`, then debug information will be excluded,
    defaults to True (optional)
    :return: The function `main` returns a list of compiled data.
    """
    syntax_content = open(input_file, "r+").read().replace("\n}","}").lstrip(" ")
    blocks = syntax_content.strip().split('\n\n')

    compiled_data = []
    for block in blocks:
        compiled_data.append(create_file_from_syntax(block, debug_mode))

    return compiled_data

def create_file_from_syntax(syntax, debug=False):
    lines = syntax.strip().split('\n')
    filename = lines[0].strip().rstrip(':')
    content = '\n'.join(lines[1:]).strip()

    return compile(content, filename, debug)

def compile(infile, outfile, debug=False):
    """
    The `compile` function takes an input file, processes its lines, builds a tree, and compiles the
    tree into an output file, with an option to include debug information.
    
    :param infile: The `infile` parameter is the input file that contains the code to be compiled. It
    should be a string representing the contents of the file
    :param outfile: The `outfile` parameter is the name of the output file that will be generated after
    compiling the input file
    :param debug: The `debug` parameter is a boolean flag that determines whether or not to include
    debug information in the output. If `debug` is set to `True`, the function will return a list
    containing two elements: the first element is the name of the output file, and the second element is
    the compiled, defaults to False (optional)
    :return: The function `compile` returns a list of tuples. Each tuple contains two elements: the
    `outfile` and the result of compiling the `tree_list`.
    """
    file_lines = [line for line in infile.split("\n") if line.strip() != '']
    tree_list = compiler.build_tree(file_lines)

    if debug:
        out_text = compiler.compile_tree_list(tree_list)
        return f"{outfile}-{out_text}".split("-")
    else:
        return [(outfile, compiler.compile_tree_list(tree_list))]
        

if __name__ == '__main__':
    # This code block is responsible for reading the content of the input file, making some
    # modifications to the content, compiling the modified content, and then generating a datapack and
    # resourcepack based on the compiled data.

    input_file = input("Enter .cmc file directory for compilation: ").strip(".cmc") + ".cmc" # Provide the input file path

    with open(input_file, "r+") as file:
        content = file.read()
        content = re.sub(r'run\s*{', 'run{', content)
        content = re.sub(r'\n\n*}', '\n\n}', content)
        file.seek(0)
        file.write(content)
        file.truncate()

    compiled_data = main(input_file, debug_mode=True)
    pack_id = input_file.replace(".cmc","").replace(" ","_").lower()
    #print(compiled_data)
    datapack_build(pack_id,compiled_data)
    resourcepack_build(pack_id,compiled_data)
    input("Compiled successfuly!")