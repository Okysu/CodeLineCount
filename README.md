# CodeLineCount

## Description

This is a small tool for counting lines of code, which can count the lines of code in a specified directory and support counting for specified programming languages. It automatically filters files based on the .gitignore file.

## Usage

First, you need to modify your code working directory,

```python
code_file_list = build_file_list('your path')
```

Then, modify the file types you want to count,

```python
patterns = ['*.py', '*.js', '*.html', '*.css', '*.go', "*.ts", "*.java"]
```

Finally, run the tool,

```shell
$ python3 main.py
```