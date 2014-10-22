import argparse
from os.path import basename, splitext
from os import system, remove
import platform

def convertOFFToSTL(inputOFF):
	basenameInputOFF = splitext(basename(inputOFF))[0] 
	cmd='./'+ platform.system()+ '/meshconv '+ inputOFF +' -c stl -o ' + basenameInputOFF
	system(cmd)
	return basenameInputOFF+'.stl'

def convertSTLToOFF(inputSTL):
	basenameInputSTL = splitext(basename(inputSTL))[0] 
	cmd='./' + platform.system() + '/meshconv '+ inputSTL +' -c off -o ' + basenameInputSTL
	system(cmd)
	return basenameInputSTL+'.off'

def applyBooleanOperation(input1OFF, input2OFF, typeOp, outputOFF):
	cmd = './../bin/cork -' + typeOp + ' ' + input1OFF + ' ' + input2OFF + ' ' + outputOFF 
	system(cmd)


parser = argparse.ArgumentParser()
parser.add_argument('-f1', '--file1')
parser.add_argument('-f2', '--file2')
parser.add_argument('-t', '--operationtype')
parser.add_argument('-o','--outputstl')

args = parser.parse_args()

print args

f1STL = args.file1
f2STL = args.file2
typeOp = args.operationtype
outputSTL = args.outputstl

## convert STL to .off
f1OFF = convertSTLToOFF(f1STL)
f2OFF = convertSTLToOFF(f2STL)

outputOFF = splitext(basename(outputSTL))[0]+'.off'

## apply boolean operation
applyBooleanOperation(f1OFF, f2OFF, typeOp, outputOFF)

## convert OFF to STL
convertOFFToSTL(outputOFF)

remove(f1OFF)
remove(f2OFF)
remove(outputOFF)