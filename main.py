import os
import fnmatch
import codecs
from pathspec import PathSpec
from pathspec.patterns import GitWildMatchPattern


def build_file_list(start_dir, patterns=None):
    if patterns is None:
        patterns = ['*.py', '*.js', '*.html', '*.css', '*.go', "*.ts", "*.java"]
    file_list = []

    def process_directory(dirpath, parent_ignore_spec=None):
        ignore_patterns = []
        if '.gitignore' in os.listdir(dirpath):
            with open(os.path.join(dirpath, '.gitignore'), 'r') as f:
                ignore_patterns += f.read().splitlines()
        ignore_spec = PathSpec.from_lines(GitWildMatchPattern, ignore_patterns)
        if parent_ignore_spec is not None:
            ignore_spec = parent_ignore_spec + ignore_spec

        for filename in os.listdir(dirpath):
            filepath = os.path.join(dirpath, filename)
            if ignore_spec.match_file(filepath):
                continue
            if os.path.isdir(filepath):
                process_directory(filepath, ignore_spec)
            else:
                for pattern in patterns:
                    if fnmatch.fnmatch(filename, pattern):
                        file_list.append(filepath)
                        break

    process_directory(start_dir)
    return file_list


def count_lines_and_words(file_list):
    total_lines = 0
    total_words = 0
    for i, filepath in enumerate(file_list, 1):
        with codecs.open(filepath, 'r', 'utf-8', 'ignore') as f:
            lines = f.readlines()
            total_lines += len(lines)
            words = 0
            for line in lines:
                words += len(line)
            total_words += words
            print(f'Reading file {i}/{len(file_list)}:\t{filepath}\t({len(lines)} lines, {words} words)')
    return total_lines, total_words


code_file_list = build_file_list('/Users/okysu/Code')
print(code_file_list)
code_total_lines, code_total_words = count_lines_and_words(code_file_list)
print('Total lines:\t', code_total_lines)
print('Total words:\t', code_total_words)
