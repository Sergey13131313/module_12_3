import unittest
import mymodule2 as my


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    @classmethod
    def setResult(cls, obj):
        cls.all_results = obj

    def setUp(self):
        runner1 = my.Runner('Усэйн', 10)
        runner2 = my.Runner('Андрей', 9)
        runner3 = my.Runner('Ник', 3)
        return [runner1, runner2, runner3]

    @unittest.skipIf(is_frozen, 'Замороженный')
    def test_tournament1(self):
        list_runner = self.setUp()
        obj_t = my.Tournament(90, list_runner[0], list_runner[2])
        aaa = obj_t.start()
        self.setResult(aaa)
        self.assertEqual(self.all_results[len(self.all_results)], 'Ник')

    @unittest.skipIf(is_frozen, 'Замороженный')
    def test_tournament2(self):
        list_runner = self.setUp()
        obj_t = my.Tournament(90, list_runner[1], list_runner[2])
        aaa = obj_t.start()
        self.setResult(aaa)
        self.assertEqual(self.all_results[len(self.all_results)], 'Ник')

    @unittest.skipIf(is_frozen, 'Замороженный')
    def test_tournament3(self):
        list_runner = self.setUp()
        obj_t = my.Tournament(90, list_runner[0], list_runner[1], list_runner[2])
        aaa = obj_t.start()
        self.setResult(aaa)
        self.assertEqual(self.all_results[len(self.all_results)], 'Ник')

    @classmethod
    def tearDownClass(cls):
        for key, value in cls.all_results.items():
            print(f'{key}: {value.name}')


if __name__ == '__main__':
    unittest.main()
