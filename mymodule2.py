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
            leader = self.participants[0]
            for participant in self.participants:
                participant.run()
                leader = participant if participant.distance > leader.distance else leader
            if leader.distance >= self.full_distance:
                finishers[place] = leader
                place += 1
                self.participants.remove(leader)

        return finishers


if __name__ == '__main__':
    runner1 = Runner('Усэйн', 40)
    runner2 = Runner('Андрей', 20)
    runner3 = Runner('Ник', 30)

    obj = Tournament(10, runner1, runner2, runner3)

    dict = obj.start()

    for i in dict.keys():
        print(f'{i}: {dict[i]}')

    a = 1

    dict = {1: 'Усэйн', 2: 'Андрей', 3: 'Ник'}
    print(len(dict))
    for key, value in dict.items():
        print(f'{key}: {value}')
