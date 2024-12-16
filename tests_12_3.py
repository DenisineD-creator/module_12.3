import unittest
import module_12_3

ts = unittest.TestSuite()

ts.addTest(unittest.TestLoader().loadTestsFromTestCase(module_12_3.TournamentTest))
ts.addTest(unittest.TestLoader().loadTestsFromTestCase(module_12_3.RunnerTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(ts)