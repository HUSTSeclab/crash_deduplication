#!/usr/bin/env python

"""
A simple python script template.
"""

from __future__ import print_function
import os
import sys
import argparse
import openpyxl

def main(input_file):
    wb = openpyxl.load_workbook(input_file)
    ws = wb['Reproducible cases']

    reasons = {"Different Inputs":[], "Thread Interleaving":[], "Memory Dynamics":[], "Kernel Versions and Branches":[], "Sanitizers":[], "Inline":[]}
    patches = {}

    for row_cells in ws.iter_rows():
        if not row_cells[0].value:
            continue
        if row_cells[0].value == "Patch":
            continue
        if row_cells[0].value in patches:
            if row_cells[3].value:
                patches[row_cells[0].value].append(row_cells[3].value)
        else:
            patches[row_cells[0].value] = [row_cells[3].value]
    # loop the dict
    #for p in patches:
    #    print(p, patches[p])

    for p in patches:
        for reason in patches[p]:
            if reason in reasons.keys():
                reasons[reason].append(p)
    for r in reasons:
        print(r, len(reasons[r]), reasons[r])

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--in_file', help='provide the path of input data file', type=str)
    args = parser.parse_args()
    if not args.in_file:
        parser.error("Please provide argument for input data file")
    main(args.in_file)
    sys.exit()
