import re

with open("bindings.lua", "r") as f:
    lines = f.readlines()

new_lines = []
in_loop = False

for i in range(len(lines)):
    line = lines[i].strip()
    
    # Handle empty lines
    if not line:
        # Keep empty line only if the NEXT non-empty line is a block comment (starts with -- but not a line we want to attach closely to)
        # Actually, let's just look ahead
        next_line = ""
        for j in range(i+1, len(lines)):
            if lines[j].strip():
                next_line = lines[j].strip()
                break
        if next_line.startswith("--") and next_line != "-- Screenshot":
            new_lines.append("")
        elif next_line == "-- Screenshot":
            new_lines.append("")
        # Also keep empty line at the very top (line 2)
        if i == 1 or i == 2:
            new_lines.append("")
        continue
        
    # Indentation
    if line.startswith("for "):
        in_loop = True
        new_lines.append(line)
        continue
    if line == "end":
        in_loop = False
        new_lines.append(line)
        continue
        
    prefix = "    " if in_loop else ""
    
    # Restore some internal spacing inside the loop for alignment if it's the specific lines
    if in_loop and line.startswith('hl.bind("SUPER + " .. key,'):
        line = line.replace('hl.bind("SUPER + " .. key,', 'hl.bind("SUPER + " .. key,            ')
    if in_loop and line.startswith('hl.bind("SUPER + SHIFT + " .. key,'):
        line = line.replace('hl.bind("SUPER + SHIFT + " .. key,', 'hl.bind("SUPER + SHIFT + " .. key,    ')
        
    new_lines.append(prefix + line)

# Clean up duplicate empty lines just in case
clean_lines = []
prev_empty = False
for l in new_lines:
    if not l:
        if not prev_empty:
            clean_lines.append("")
            prev_empty = True
    else:
        clean_lines.append(l)
        prev_empty = False

with open("bindings.lua", "w") as f:
    f.write("\n".join(clean_lines) + "\n")
