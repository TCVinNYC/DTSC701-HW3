from mrjob.job import MRJob

class MRWordFrequencyCount(MRJob):

    def mapper(self, _, line):
        words = line.split()
        for word in words:
            yield (word, 1)

    def reducer(self, key, values):
        yield (key, sum(values))

if __name__ == '__main__':
    MRWordFrequencyCount.run()

# python word_count.py bios.txt > bios_output.txt
