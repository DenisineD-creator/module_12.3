import unittest


class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.r1 = Runner('Усэйн', 10)
        self.r2 = Runner('Андрей', 9)
        self.r3 = Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for res in cls.all_results:
            print(res)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_run1(self):
        t1 = Tournament(90, self.r1, self.r3)
        self.all_results = t1.start()
        self.assertTrue(sorted(self.all_results.items())[-1][1] == self.r3.name)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_run2(self):
        t2 = Tournament(90, self.r2, self.r3)
        self.all_results = t2.start()
        self.assertTrue(sorted(self.all_results.items())[-1][1] == self.r3.name)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_run3(self):
        t3 = Tournament(90, self.r1, self.r2, self.r3)
        self.all_results = t3.start()
        self.assertTrue(sorted(self.all_results.items())[-1][1] == self.r3.name)

class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_walk(self):
        r1 = Runner('r1')
        for _ in range(10):
            r1.walk()
        self.assertEqual(r1.distance, 50)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_run(self):
        r2 = Runner('r2')
        for _ in range(10):
            r2.run()
        self.assertEqual(r2.distance, 100)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_challenge(self):
        r3 = Runner('r3')
        r4 = Runner('r4')
        for _ in range(10):
            r3.run()
            r4.walk()
        self.assertNotEqual(r3.distance, r4.distance)


if __name__ == '__main__':
    unittest.main()