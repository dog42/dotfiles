import re

with open("bindings.lua", "r") as f:
    lines = f.readlines()

new_lines = []
current_block_comment = None

for line in lines:
    stripped = line.strip()
    
    if stripped.startswith("--") and not stripped.startswith("-- See") and "Example binds" not in stripped:
        if current_block_comment is None:
            current_block_comment = stripped[2:].strip()
        new_lines.append(stripped)
        continue

    if not stripped:
        current_block_comment = None
        new_lines.append(stripped)
        continue
        
    if "hl.bind(" in line:
        code_part = stripped
        inline_comment = None
        
        # carefully find inline comment that is NOT part of a string
        # A simpler hack: find " -- " (with spaces) to avoid matching "--menue" inside strings
        if " -- " in code_part:
            parts = code_part.rsplit(" -- ", 1)
            code_part = parts[0].strip()
            inline_comment = parts[1].strip()
            
        # Fix line 17 if it was truncated
        if 'waybar-tailscale.sh' in code_part and not code_part.endswith(')'):
            code_part = 'hl.bind("SUPER + T", hl.dsp.exec_cmd((os.getenv("HOME") or "") .. "/.config/waybar/waybar-tailscale/waybar-tailscale.sh --menue"))'
            inline_comment = 'tailscale-waybar-menue'
            
        desc = inline_comment if inline_comment else current_block_comment
        
        if desc:
            # We already have some descriptions inserted by previous script
            if '{ description =' in code_part or '{description =' in code_part:
                new_lines.append(code_part)
                continue
                
            if code_part.endswith(")"):
                inner = code_part[:-1].strip()
                if inner.endswith("}"):
                    inner = inner[:-1] + f', description = "{desc}" }}'
                else:
                    inner = inner + f', {{ description = "{desc}" }}'
                code_part = inner + ")"
                
        new_lines.append(code_part)
    else:
        new_lines.append(stripped)

# Remove duplicate empty lines
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
