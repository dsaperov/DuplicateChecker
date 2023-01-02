# What is DuplicateChecker?
A script to search for files with duplicate content in the **specified folder**. Can be configured to check only files 
of **specified extension**. 
Outputs a list of filenames having fully identical content. Each group of filenames with identical content is separated 
from another via dashed line (`----------------------`). So the output is like the following:
```
file_with_content_A_1.txt
file_with_content_A_2.txt
file_with_content_A_3.txt
----------------------
file_with_content_B_1.txt
file_with_content_B_2.txt
```

# Usage
The script accepts the following arguments:
- `path` (**positional**) - path to the folder you need to check for files with duplicate content in. Should be 
  enclosed in double quotes (*example:* `"C:/Users/My_folder"`).
- `-e, --extension` (**optional**) - extension (*without a dot*) of files to be checked (*example:* `txt`, but not 
  `.txt`). If not specified, files with all extensions will be checked.

## Examples of usage:
- `python main.py "C:/Users/My_folder"` to check files with all extensions.
- `python main.py "C:/Users/My_folder" -e txt` to check only files with `.txt` extension.



