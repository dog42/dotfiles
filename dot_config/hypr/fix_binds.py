import re

with open("bindings.lua", "r") as f:
    lines = f.readlines()

new_lines = []
current_block_comment = None

for line in lines:
    stripped = line.strip()
    
    # Catch block comments that aren't empty and don't start with "See "
    if stripped.startswith("--") and not stripped.startswith("-- See") and "Example binds" not in stripped:
        if current_block_comment is None:
            current_block_comment = stripped[2:].strip()
        new_lines.append(line)
        continue

    # If it's an empty line, clear the current block comment
    if not stripped:
        current_block_comment = None
        new_lines.append(line)
        continue
        
    # Check if line is a bind
    if "hl.bind(" in line:
        # Check for inline comment
        inline_comment = None
        code_part = line
        
        m_inline = re.match(r'^(.*?)--\s*(.+)$', line)
        if m_inline and "hl.bind" in m_inline.group(1):
            code_part = m_inline.group(1).rstrip()
            inline_comment = m_inline.group(2).strip()
            
        desc = inline_comment if inline_comment else current_block_comment
        
        if desc:
            # Need to insert description into the bind
            # Example code_part: hl.bind("SUPER + left", hl.dsp.focus({ direction = "l" }))
            # Or with options: hl.bind("...", ..., { repeating = true })
            
            # Find the last closing parenthesis of hl.bind
            # We'll just rsplit on ")" to insert before it
            if code_part.endswith(")"):
                inner = code_part[:-1]
                if inner.endswith("}"):
                    # Has an options table at the end
                    inner = inner[:-1] + f', description = "{desc}" }}'
                else:
                    # No options table
                    inner = inner + f', {{ description = "{desc}" }}'
                code_part = inner + ")"
                
            new_lines.append(code_part + "\n")
        else:
            new_lines.append(line)
    else:
        new_lines.append(line)

with open("bindings.lua", "w") as f:
    f.writelines(new_lines)
