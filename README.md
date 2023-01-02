# What is DuplicateChecker?
A script to search for files of **specified extension** with duplicate content in the **specified folder**.
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
There are **2 positional arguments** you should specify to run the script:
- `path` - path to the folder you need to check for files with duplicate content in (*example:* `"C:/Users/My_folder"`)
- `extension` - extension (*without a dot*) of files to be checked (*example:* `txt`, but not `.txt`)

## Example of usage:
```bash
python main.py "C:/Users/My_folder" txt
```



