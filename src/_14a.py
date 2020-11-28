from file_importer import FileImporter

class Reindeer:
    def __init__(self, name, speed, duration, rest_time):
        self.name = name
        self.speed = speed
        self.duration = duration
        self.rest_time = rest_time

        self.seconds_left = self.duration
        self.rest_time_remaining = self.rest_time
        self.distance_traveled = 0

        self.points = 0

    def tick(self):
        ''' run once per second '''

        if self.seconds_left > 0:
            self.seconds_left -= 1
            self.distance_traveled += self.speed

        else:
            self.rest_time_remaining -= 1

            if self.rest_time_remaining == 0:
                self.rest_time_remaining = self.rest_time
                self.seconds_left = self.duration

reindeer = FileImporter.get_input("/../input/14.txt").split('\n')
reindeers = []
for r in reindeer:
    r = r.split(' ')
    reindeers.append(Reindeer(r[0], int(r[3]), int(r[6]), int(r[13])))

for s in range(2503):
    for r in reindeers:
        r.tick()
    max_dist = max(reindeers, key = lambda r: r.distance_traveled).distance_traveled
    reindeers_to_give_points = [i for i in reindeers if i.distance_traveled == max_dist]

    for r in reindeers_to_give_points:
        r.points += 1

print(max(reindeers, key = lambda r: r.points).points)
