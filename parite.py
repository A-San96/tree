#! /usr/bin/env python3
# coding: utf-8
import argparse
import analysis.csv as c_an
import analysis.xml as x_an

def parse_arguments():
	parser = argparse.ArgumentParser()
	parser.add_argument("-e","--extension",help="""Type of file to analyse. Is it a CSV or an XML?""")
	parser.add_argument("-d","--datafile",help="""CSV file containing pieces of information about the members of parliament""")
	return parser.parse_args()

def main():
	args = parse_arguments()
	datafile=args.datafile
	if args.extension == 'xml':
		x_an.launch_analysis('SyceronBrut.xml')
	elif args.extension == 'csv':
		c_an.launch_analysis('current_mps.csv')

if __name__ == '__main__':
#	main()
	