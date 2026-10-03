REGULAR EXPESSION
## use re module
## re.search(regex pattern,string)
## returns match object when match found else returns None
## if there special char or symbols in regex pattern is called as metacharacters.
## re.match(regex pattern,string) -- checks at the begining else it give None.
## findall(regex pattern,string) --- returns all matches -- list
## finditer(regex pattern,string) ---- returns match object for all matches
## sub(pattern,replacement,string,count,flags=re.IGNORECASE) --- Replaces matched string
## compile(pattern) ---- if you want to use the same pattern in multiple example ,makesure of compile the pattern and use it.

METACHAR IN REGEX
## metachar [0-9]
## metachar [.] only consider dot.
## metachar . ---- dot matches any character except new line character (\n). 
## r --- raw string r"old\new" (here \n is consider as new only.) 
## without r --- it old , new line ew. 
## metachar [A-Z][a-z]
## metachar \d -- consider 1 digit character like [0-9].
## metachar \D --- matches to any non-digit character.
## metavhar \s -- matches to any spaces and it matches \t and \n(new line).
## metavhar \S -- matches to any character and except spaces, \t and \n(new line).
## metavhar \w -- matches [a-z],[A-Z],[0-9], _ .
## metachar \W -- matches spaces,\n,-,$ etc.. except [a-z][A-Z][0-9]

QUANTIFIERS IN REGEX

## {n} -- n times  
## * -- matches zero or more
## ? -- matches zero or one
## + -- matches one or more
## ^ - caret --- starting of the line
## $ - dollar --- end of te line
## [] - charter set
## () - group
##  | - or
