import csv
import random

class MidiMauler:
    def __init__(self, csv_filename):
        with open(csv_filename, 'r') as csv_file:
            reader = csv.reader(csv_file)
            self.events = list(reader)

    def mutate(self, filename="new.csv", severity=1):
        new = []

        likelihood = severity/100
        noise = severity

        #event is a list of midi events
        for event in self.events:
            if event[2].strip() in ("Note_on_c", "Control_c"):
                if random.random() < likelihood:
                    event[4] = min(max(int(event[4]) + random.randint(-noise, noise), 1), 127)

            # this is a bad hack to remove some annoying drum beats
            if int(event[0]) != 4:
                new.append(event)

        self.write(new, filename)

    @staticmethod
    def write(events, filename):
        with open(filename, 'w') as csv_file:
            writer = csv.writer(csv_file)
            for event in events:
                writer.writerow(event)

if __name__ == '__main__':
    mm = MidiMauler("shortened_ptmd.csv")

    # 50 slides, 49 transitions... 1 outro track?
    for n in range(50):
        mm.mutate(filename="output/{}.csv".format(n), severity=n)
