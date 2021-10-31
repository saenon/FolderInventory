import os
import csv

#Return files list
def getAllFiles(path):
	files_in_path = []
	for root, dirs, files in os.walk(path):
		for file in files:
			files_in_path.append(os.path.join(root, file))
	return files_in_path

#Write inventory of files
def writeAllFiles(file_to_write, files):
	with open(file_to_write, 'w', newline = '') as csv_file:
		writer = csv.writer(csv_file, delimiter = ',', quotechar = '|', quoting = csv.QUOTE_MINIMAL)
		writer.writerow(['ID' ,'File', 'Comments'])

		id = 0

		for file in files:
			writer.writerow([id, file])
			id += 1