# Minja - a minimal templating replacement engine

Kind of like Cookiecutter or Jinja but with 70% fewer features and 90% less code!
Also barely tested.

Pure Python 3, no external dependencies.

Given a dictionary of "from" -> "to" replacements, and a folder full of files:

- replaces all occurrences in the body of all files
- also within filenames
- also within folder names

Attempts to:

- leave binary files alone
- preserve the line ending of text files (Unix, DOS)
- preserve the permissions (executable bit should say set even after modification/renaming)

Don't blame me if this accidentally destroys the files in the folder you provide, but it probably won't.

## Usage

```
./minja.py /path/to/template/folder
```

## FAQ

Q: Do you realize how terrible the name is?  
A: Yeah. Naming is hard.
