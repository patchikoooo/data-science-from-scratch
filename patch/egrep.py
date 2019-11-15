# stdin and stdout

# If you run your Python scripts at the command line, you can pipe data through
#       them using sys.stdin and sys.stdout.

# egrep.py
import sys, re

# sys.argv is the list of command-line arguments
# sys.argv[0] is the name of the program itself
# sys.argv[1] will be the regex specified at the command line.
regex = sys.argv[1]
#print(regex)


for line in sys.stdin:
    # if it matches the regex, write it to stdout
    if re.search(regex, line):
        sys.stdout.write(line)


## type SomeFile.txt | python egrep.py "[0-9]" | python line_count.py

## The | is the pipe character, which means “use the output of the 
## 		left command as the input of the right command.” You 
## 		can build pretty elaborate data-processing pipelines this way.


## UNIX SYSTEM
#whereas in a Unix system you’d use:
# cat SomeFile.txt | python egrep.py "[0-9]" | python line_count.py

# If you are using Windows, you can probably leave out the python
#		part of this command:
# type SomeFile.txt | egrep.py "[0-9]" | line_count.py