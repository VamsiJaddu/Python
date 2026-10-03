## compile(pattern) ---- if you want to use the same pattern in multiple example ,makesure of compile the pattern and use it.

import re

## Now i have to use this pattern in multiple example so i will compile the pattern and use it.


pattern = r"\d{10}"
pattern_compiled = re.compile(pattern)


if __name__ == "__main__":
    
    name = "Alice-9876543212, Bob-9876543213, Charlie-9876543214, David-9876543215"

    print(re.search(pattern,name))
    print(re.findall(pattern,name))
    print(re.finditer(pattern,name))

    print(re.search(pattern_compiled,name))

    print(pattern_compiled.search(name))
    print(pattern_compiled.findall(name))       
