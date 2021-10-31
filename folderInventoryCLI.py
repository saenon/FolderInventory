from argparse import ArgumentParser
from logic.files import getAllFiles
from logic.files import writeAllFiles


#args
parser = ArgumentParser()
parser.add_argument("-p", "--path", help = "Specify the path to be analyzed.", required = True)
parser.add_argument("-o", "--output", help = "Specify the output file name.", default = "files_inventory.csv")

args = parser.parse_args()

#Get all files
files = getAllFiles(args.path)

#check csv extension
if(not args.output.endswith('.csv')):
	args.output = args.output + '.csv'

#write files
writeAllFiles(args.output, files)