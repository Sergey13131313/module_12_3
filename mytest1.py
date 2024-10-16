import unittest
import mymodule1


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Замороженный')
    def test_walk(self):
        obj = mymodule1.Runner('Ivan')
        for i in range(10):
            obj.walk()
        self.assertEqual(obj.distance, 50, 'test_walk')

    @unittest.skipIf(is_frozen, 'Замороженный')
    def test_run(self):
        obj = mymodule1.Runner('Petr')
        for i in range(10):
            obj.run()
        self.assertEqual(obj.distance, 100, 'test_run')

    @unittest.skipIf(is_frozen, 'Замороженный')
    def test_challenge(self):
        obj1 = mymodule1.Runner('Ivan')
        obj2 = mymodule1.Runner('Petr')
        for i in range(10):
            obj1.walk()
            obj2.run()
        self.assertNotEqual(obj1.distance, obj2.distance, 'test_challenge')


if __name__ == '__main__':
    unittest.main()
