import os
import sys
import unittest
import coverage


tests_path = os.path.dirname(os.path.realpath(__file__)) + '/tests'
sys.path.insert(0, tests_path)

cov = coverage.Coverage()
cov.start()


loader = unittest.TestLoader()
suite = loader.discover(tests_path)

runner = unittest.TextTestRunner()
runner.run(suite)

cov.stop()

cov.report()

cov.xml_report(outfile='coverage.xml')