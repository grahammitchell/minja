#!/usr/bin/python3

# 2020-04-01 - Graham Mitchell

import json, logging, os, re, shutil, sys
from os.path import join

def main():
	logging.getLogger().setLevel(logging.WARNING)

	if len(sys.argv) < 2:
		print(f"Usage: {sys.argv[0]} [folder]")
		sys.exit(1)
	filename = sys.argv[1]

	with open('replacements.json') as f:
		replacements = json.load(f)

	prefilter = re.compile(r'(\A|\W)__\w+__(\W|\Z)')
	minja(filename, replacements, prefilter)


def minja(input_folder, replacements, prefilter=None):
	"""replaces all occurrences of replacements in all files, filename and folder names"""
	for root, dirs, files in os.walk(input_folder, topdown=False):
		for name in files:
			change_file_in_place(join(root, name), replacements, prefilter)
			rename_if_matching(root, name, replacements)
		for name in dirs:
			rename_if_matching(root, name, replacements)


def rename_if_matching(root, name, replacements):
	new_name, is_different = replace_in_string(name, replacements)
	if is_different:
		src = os.path.join(root, name)
		dest = os.path.join(root, new_name)
		logging.info("Renaming '%s' => '%s'", src, dest)
		os.rename(src, dest)


def change_file_in_place(filename, replacements, prefilter=None):
	"""replaces all occurrences of replacements in the given file"""
	if is_binary_file(filename):
		logging.info(f"Skipping binary file '%s'.", filename)
		return

	logging.info(f"Examining '{filename}'")

	with open(filename, 'r') as f:
		file_contents = f.read()
		original_newline = f.newlines
		logging.debug("Newlines: [%s]", repr(original_newline))

	file_contents, modified = replace_in_string(file_contents, replacements, prefilter)

	if modified:
		modified_filename = f"{filename}" 
		with open(modified_filename, 'w', newline=original_newline) as f:
			f.write(file_contents)
		logging.info(f"'{modified_filename}' written.")


def replace_in_string(s, replacements, prefilter=None):
	"""returns a new string after replacing all occurrences of replacements in the given string"""
	if prefilter and not prefilter.search(s):
		logging.debug("Prefilter indicates no match.")
		return s, False

	modified = False
	for original, substitution in replacements.items():
		if re.search(original, s):
			modified = True
			s = re.sub(original, substitution, s, count=0)

	return s, modified


def is_binary_file(filename):
	with open(filename, 'rb') as f:
		chunk = f.read(1024)	
	return is_binary_string(chunk)


def is_binary_string(s):
	# https://stackoverflow.com/questions/898669/how-can-i-detect-if-a-file-is-binary-non-text-in-python
	textchars = bytearray({7,8,9,10,12,13,27} | set(range(0x20, 0x100)) - {0x7f})
	return bool(s.translate(None, textchars))


if __name__ == "__main__":
	main()
