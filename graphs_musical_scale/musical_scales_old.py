class MusicalScales():
    """
        Musical Scale class to generate scales and the graph of cromatic scale
        (ascending and descending).
        TODO: Implement generation for minor scale.
    """

    def __init__(self) -> None:

        self.major_scale_intervals = [
            # distance (intervals) between each degree,
            # Starts in the 2nd degree, Tonic is 0
            0,  # Tonic
            2,  # 2nd degree
            2,  # 3rd
            1,  # 4th
            2,  # 5th
            2,  # 6th
            2,  # 7th
            # 1,  # 8th - restart from tonic
        ]
        self.minor_scale_degree_tones = [2, 1, 2, 2, 2, 1, 2]  # Starts in the 2nd degree, Tonic = 0

        self.cromatic_scale_ascending = [
            'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']  # len: 12

        self.cromatic_scale_descending = [
            'B', 'Bb', 'A', 'Ab', 'G', 'Gb', 'F', 'E', 'Eb', 'D', 'Db', 'C']  # len: 12

    def generate_cromatic_graph(self, scale: str, tonic_note: str):
        """ Generates a Graph that represents
        """
        cromatic_graph = self.generate_scale(self, tonic_note, scale)
        if scale == 'major':
            for note in self.cromatic_scale_ascending:
                # create a dict of dict for each note in ascending scale.
                cromatic_graph[note] = self._generate_scale()

        else:  # 'minor'
            for note in self.cromatic_scale_descending:
                # create a dict of dict for each note in ascending scale.
                cromatic_graph[note] = {}

        return cromatic_graph

    def generate_scale(self, tonic_note: str = 'C#', scale: str = 'major'):
        """ Generates a scale for a given tonic note.
        """
        base_index = self.cromatic_scale_ascending.index(tonic_note)

        # Generate the scale from Tonic note.
        major_scale = {
            tonic_note: 0,  # Set the tonic note and it interval value as the first.
        }
        current_index = base_index

        # For each interval in the major scale intervals list
        for interval in self.major_scale_intervals:

            # Select the next note in cromatic scale, by the index in current position in
            # `cromatic_scale_ascending` list.
            # We setted the `current_index` as the base_index that is the tonic note,
            # Then, we select the next note in cromatic scale by sum of actual_note + interval
            # that is in `major_scale_intervals` list.
            # `% len` is to garantee that the next index is a valid index inside
            # `cromatic_scale_ascending` and returns to the begin of the list, if the index was
            # the last in the list.
            current_index = (current_index + interval) % len(self.cromatic_scale_ascending)

            # Select the note in ascending cromatic scale, by it's index
            note = self.cromatic_scale_ascending[current_index]

            # Add to Dict, the note and it's interval value
            major_scale[note] = interval
            print(major_scale)

        return major_scale


class MajorCromaticScale():
    scale = {
        'C': {
            'C': 0.,  # Tonic
            'D': 1.,
            'E': 2.,
            'F': 2.5,
            'G': 3.5,
            'A': 4.5,
            'B': 5.5,
            # 'C': 6.  # Octave
        },
        'C#': {
            'C#': 0.,  # Tonic
            'D#': 1.,
            'E': 2.,
            'F': 2.5,
            'G': 3.5,
            'A': 4.5,
            'B': 5.5,
            # 'C#': 6.,  # Octave
        },
        'D': {},
        'D#': {},
        'E': {},
        'F': {},
        'F#': {},
        'G': {},
        'G#': {},
        'A': {},
        'A#': {},
        'B': {},
        'B#': {}
    }
