# Minja - a minimal templating replacement engine

Given a dictionary of "from" -> "to" replacements, and a folder full of files:

- replaces all occurrences in the body of all files
- also within filenames
- also within folder names

Attempts to:

- leave binary files alone
- preserve the line ending of text files (Unix, DOS)
- preserve the permissions (executable bit should say set even after modification/renaming)

Kind of like Cookiecutter or Jinja but without half the feature and 90% less code!
Also barely tested.

Don't blame me if this accidentally destroys the files in the folder you provide, but it probably won't.

## Usage

```
./minja.py /path/to/template/folder
```

## FAQ

Q: Do you realize how terrible the name is?
A: Yeah. Naming is hard.
