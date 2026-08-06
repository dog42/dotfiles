#!/usr/bin/env python3
import sys

def convert(input_file, output_file=None):
    with open(input_file, 'r') as f:
        lines = f.readlines()

    out_lines = []
    
    for line in lines:
        stripped = line.strip()
        if not stripped:
            out_lines.append("")
            continue
            
        if stripped.startswith("#"):
            out_lines.append(stripped.replace("#", "--", 1))
            continue
            
        if stripped.startswith("monitor="):
            args_str = stripped.split("=", 1)[1]
            parts = args_str.split(",")
            if len(parts) >= 4:
                output = parts[0]
                mode = parts[1]
                position = parts[2]
                scale = parts[3]
                
                out_lines.append("hl.monitor({")
                out_lines.append(f'    output = "{output}",')
                out_lines.append(f'    mode = "{mode}",')
                out_lines.append(f'    position = "{position}",')
                
                # Parse additional arguments like transform, vrr, bitdepth
                i = 4
                extra_args = []
                while i < len(parts):
                    key = parts[i].strip()
                    if i + 1 < len(parts) and (parts[i+1].strip().isdigit() or (parts[i+1].strip().startswith('-') and parts[i+1].strip()[1:].isdigit())):
                        val = parts[i+1].strip()
                        extra_args.append((key, val))
                        i += 2
                    else:
                        extra_args.append((key, 'true'))
                        i += 1
                
                if extra_args:
                    out_lines.append(f'    scale = "{scale}",')
                    for idx, (k, v) in enumerate(extra_args):
                        comma = "," if idx < len(extra_args) - 1 else ""
                        out_lines.append(f'    {k} = {v}{comma}')
                else:
                    out_lines.append(f'    scale = "{scale}"')
                        
                out_lines.append("})")
                out_lines.append("")
                continue
                
        out_lines.append(line.rstrip('\n'))

    result = "\n".join(out_lines) + "\n"
    
    if output_file:
        with open(output_file, 'w') as f:
            f.write(result)
        print(f"Konvertierung abgeschlossen. Gespeichert in: {output_file}")
    else:
        print(result, end='')

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Verwendung: python3 convert_monitors.py <eingabe_datei.conf> [ausgabe_datei.lua]")
        sys.exit(1)
        
    in_file = sys.argv[1]
    out_file = sys.argv[2] if len(sys.argv) > 2 else None
    convert(in_file, out_file)
