import unittest
import mytest1 as my1
import mytest2 as my2

myTS = unittest.TestSuite()
myTS.addTest(unittest.TestLoader().loadTestsFromTestCase(my1.RunnerTest))
myTS.addTest(unittest.TestLoader().loadTestsFromTestCase(my2.TournamentTest))
runner = unittest.TextTestRunner(verbosity=2)
runner.run(myTS)