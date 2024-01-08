import ams_compiler as compiler
from datapack_generator import datapack_build
from resourcepack_generator import resourcepack_build

def main(input_file, debug_mode=True):
    syntax_content = open(input_file, "r+").read()
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
    file_lines = infile.split("\n")
    tree_list = compiler.build_tree(file_lines)

    if debug:
        out_text = compiler.compile_tree_list(tree_list)
        return f"{outfile}-{out_text}".split("-")
    else:
        return [outfile, compiler.compile_tree_list(tree_list)]

if __name__ == '__main__':
    input_file = "demo.cmc"  # Provide the input file path
    compiled_data = main(input_file, debug_mode=True)
    pack_id = input_file.replace(".cmc","").replace(" ","_").lower()
    datapack_build(pack_id,compiled_data)
    resourcepack_build(pack_id,compiled_data)


