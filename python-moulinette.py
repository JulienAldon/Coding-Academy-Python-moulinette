#!/usr/bin/env python3

import subprocess
import sys
import difflib
import shutil

def exec_exercice(exo, args):
	cmd = ['python'] + [exo] + args
	try:
		output = subprocess.check_output(cmd, stderr=subprocess.STDOUT)
	except subprocess.CalledProcessError as exc:
		return('Status : FAIL ' + str(exc.returncode) + ' ' + str(exc.output))
	else:
		return('{}'.format(output.decode('utf-8')))


def genDiff(a, b):
	print('reference (mouli) : {} => testing (you) : {}'.format(a,b))  
	okornotok = 0
	for i,s in enumerate(difflib.ndiff(a, b)):
		if s[0] == ' ': continue
		elif s[0] == '-':
			print(u'Delete "{}" from position {}'.format(s[-1],i))
			okornotok += 1
		elif s[0] == '+':
			print(u'Add "{}" to position {}'.format(s[-1],i))
			okornotok += 1
	print()
	return (okornotok)

path_corrige = 'corrige/'

basics_exercice_list = ['01_basics_01/script.py', '01_basics_02/test.py', '01_basics_03/test.py', '01_basics_04/test.py', '01_basics_05/test.py']
basics_args_list = [['Hello World', '@_@', 'Geckos'], [''], [''], [''], ['a string object']]

iterator_exercice_list = ['02_iterators_01/test.py', '02_iterators_02/test.py', '02_iterators_03/test.py', '02_iterators_04/test.py']
iterator_args_list = [['5'], [''], [''], ['']]

comprehension_exercice_list = ['03_list_comprehension_01/test.py', '03_list_comprehension_02/test.py', '03_list_comprehension_03/test.py']
comprehension_args_list = [[], [], []]

advanced_tests = ['04_reduce_01/sum_sub.py', '05_regexp_01/regexp.py']
advanced_args = [['0', '3', '1', '3', '4', '5'], ['']]

#TODO: check argv exist with os (open it)
if sys.argv[1] is not None:
	path_test = sys.argv[1]

gen_test = ['01_basics_02/test.py', '01_basics_03/test.py', '01_basics_04/test.py', '01_basics_05/test.py', 
			'02_iterators_01/test.py', '02_iterators_02/test.py', '02_iterators_03/test.py', '02_iterators_04/test.py',
			'03_list_comprehension_01/test.py', '03_list_comprehension_02/test.py', '03_list_comprehension_03/test.py']

for a in gen_test:
	shutil.copyfile(path_corrige+a, path_test+a)

for i, n in zip(basics_exercice_list, basics_args_list):
	print('\nExercice '+ i[:i.index('/')])
	ref_ret = exec_exercice(path_corrige+i, n)
	try:
		test_ret = exec_exercice(path_test+i, n)
	except:
		print('exercice not found [KO]')
	res = genDiff(ref_ret, test_ret)
	if res != 0:
		print('output differ [KO]')
	else:
		print('test passed [OK]')

for i, n in zip(iterator_exercice_list, iterator_args_list):
	print('\nExercice '+ i[:i.index('/')])
	ref_ret = exec_exercice(path_corrige+i, n)
	try:
		test_ret = exec_exercice(path_test+i, n)
	except:
		print('exercice not found [KO]')
	res = genDiff(ref_ret, test_ret)
	if res != 0:
		print('output differ [KO]')
	else:
		print('test passed [OK]')

for i, n in zip(comprehension_exercice_list, comprehension_args_list):
	print('\nExercice '+ i[:i.index('/')])
	ref_ret = exec_exercice(path_corrige+i, n)
	try:
		test_ret = exec_exercice(path_test+i, n)
	except:
		print('exercice not found [KO]')
	res = genDiff(ref_ret, test_ret)
	if res != 0:
		print('output differ [KO]')
	else:
		print('test passed [OK]')

for i, n in zip(advanced_tests, advanced_args):
	print('\nExercice '+ i[:i.index('/')])
	ref_ret = exec_exercice(path_corrige+i, n)
	try:
		test_ret = exec_exercice(path_test+i, n)
	except:
		print('exercice not found [KO]')
	res = genDiff(ref_ret, test_ret)
	if res != 0:
		print('output differ [KO]')
	else:
		print('test passed [OK]')