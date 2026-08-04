import re

with open("bindings.lua", "r") as f:
    lines = f.readlines()

new_lines = []
current_block_comment = None

for line in lines:
    stripped = line.strip()
    
    # Check for block comment
    if stripped.startswith("--") and not stripped.startswith("-- See") and "Example binds" not in stripped:
        current_block_comment = stripped[2:].strip()
        new_lines.append(line)
        continue
        
    # Clear on empty line
    if not stripped:
        current_block_comment = None
        new_lines.append(line)
        continue
        
    if "hl.bind(" in line:
        if current_block_comment and 'description =' not in line:
            # We need to insert the description
            # We must preserve the original indentation
            m = re.match(r'^(\s*)(.*)$', line)
            indent = m.group(1)
            code = m.group(2)
            
            if code.endswith(")"):
                inner = code[:-1].strip()
                if inner.endswith("}"):
                    inner = inner[:-1] + f', description = "{current_block_comment}" }}'
                else:
                    inner = inner + f', {{ description = "{current_block_comment}" }}'
                code = inner + ")"
                
            new_lines.append(indent + code + "\n")
        else:
            new_lines.append(line)
    else:
        new_lines.append(line)

with open("bindings.lua", "w") as f:
    f.writelines(new_lines)
