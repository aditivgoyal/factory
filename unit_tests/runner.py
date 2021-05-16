import unittest

import TestInventory
import TestRecipes
import TestBuilder

loader = unittest.TestLoader()
suite = unittest.TestSuite()

suite.addTests(loader.loadTestsFromModule(TestInventory))
suite.addTests(loader.loadTestsFromModule(TestRecipes))
suite.addTests(loader.loadTestsFromModule(TestBuilder))

runner = unittest.TextTestRunner(verbosity=3)
result = runner.run(suite)