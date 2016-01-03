import re


class Reindeer(object):
    def __init__(self, speed, fly_time, rest_time):
        self.speed = int(speed)
        self.fly_time = int(fly_time)
        self.rest_time = int(rest_time)
        self.is_flying = True
        self.fly_time_left = self.fly_time
        self.rest_time_left = 0
        self.total_dist = 0
        self.score = 0

    def reset(self):
        self.is_flying = True
        self.fly_time_left = self.fly_time
        self.rest_time_left = 0
        self.total_dist = 0
        self.score = 0

    def travel(self, time):
        while time > 0:
            if self.is_flying:
                elapsed = min(self.fly_time, time)
                self.total_dist += elapsed * self.speed
                self.fly_time_left -= elapsed

                if self.fly_time_left <= 0:
                    self.fly_time_left = 0
                    self.rest_time_left = self.rest_time
                    self.is_flying = False
            else:
                elapsed = min(self.rest_time, time)
                self.rest_time_left -= elapsed

                if self.rest_time_left <= 0:
                    self.rest_time_left = 0
                    self.fly_time_left = self.fly_time
                    self.is_flying = True

            time -= elapsed

        return self.total_dist


def main():
    with open('input.txt', 'r') as f:
        rows = f.read().strip().split('\n')
    total_time = 2503

    reindeer_regex = re.compile(r'.* (\d+) km/s for (\d+) .* (\d+) seconds.')
    reindeer = [Reindeer(*reindeer_regex.search(row).groups()) for row in rows]

    max_dist = max(r.travel(total_time) for r in reindeer)
    print('The winning reindeer travelled %d km.' % max_dist)

    # Reset for part two.
    for r in reindeer:
        r.reset()

    for i in range(total_time):
        max_dist = max(r.travel(1) for r in reindeer)
        for r in reindeer:
            if r.total_dist == max_dist:
                r.score += 1

    max_score = max(r.score for r in reindeer)
    print('The winning reindeer has %d points.' % max_score)

if __name__ == '__main__':
    main()
