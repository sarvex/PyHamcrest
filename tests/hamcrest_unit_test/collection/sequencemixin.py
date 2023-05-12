class GeneratorForm(object):

    def _sequence(self, *objects):
        yield from objects


class SequenceForm(object):

    def _sequence(self, *objects):
        return list(objects)
