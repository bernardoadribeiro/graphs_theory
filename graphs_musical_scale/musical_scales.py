import winsound
import random


class Music:

    def _make_melody(self, notes_to_use, size: int = 12):
        """ Randomly select notes to create a melody.
        """
        melody = []
        for _ in range(size):
            melody.append(
                random.choice(list(notes_to_use.keys()))
            )

        return melody

    def compose_music(self, scale: str, tone: str, interval_type: str):
        self.name = f'Sonata in {tone} {scale}'
        self.tone = tone
        self.interval_type = interval_type
        self.notes = MusicalScale().generate(scale, tone, interval_type)
        self.music = self._make_melody(self.notes)

        # print(self.__dict__)
        return self.notes

    def _get_frequency(self, note):
        """ Return the frequency of a given note.
        """
        note_frequencies = {
            'C': 261,
            'C#': 277,
            'Db': 277,
            'D': 293,
            'D#': 311,
            'Eb': 311,
            'E': 329,
            'F': 349,
            'F#': 369,
            'Gb': 369,
            'G': 392,
            'G#': 415,
            'Ab': 415,
            'A': 440,
            'A#': 466,
            'Bb': 466,
            'B': 493
        }
        return note_frequencies[note]

    def play_music(self,):
        print(f'Playing {self.name} in {self.tone} tone, in {self.interval_type} scale.')
        for note in self.music:
            # print(note, end=' ')
            frequency = self._get_frequency(note)  # Gets note frequency
            duration = 500  # Note duration in miliseconds
            winsound.Beep(frequency, duration)  # play the sound


class MusicalScale:
    """
        Musical Scale class to generate scales and the graph of cromatic scale: minor and major,
        ascending and descending.
    """

    def __init__(self) -> None:
        # distance (intervals) between each degree,
        # Starts in the 2nd degree, finish in 7th, tonic is 0
        self.major_scale_intervals = [0, 2, 2, 1, 2, 2, 2, ]
        # Starts in the 2nd degree, finish in 7th, tonic is 0
        self.minor_scale_intervals = [0, 2, 1, 2, 2, 2, 1, ]
        # Starts in the 2nd degree, finish in 4th, tonic is 0
        self.pentatonica_scale_intervals = [0, 2, 2, 3, 2, ]

        self.cromatic_scale_ascending = ['C', 'C#', 'D',
                                         'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
        self.cromatic_scale_descending = ['B', 'Bb', 'Ab',
                                          'A', 'G', 'Gb', 'F', 'E', 'Eb', 'D', 'Db', 'C']

    def _generate_scale(self, tonic: str, intervals: list, chromatic_scale: list):
        scale = {}  # if we want to add the tonic note, we can use this line: scale[tonic] = 0
        current_note = tonic
        for interval in intervals:
            for _ in range(interval):
                current_note = self._next_note(current_note, chromatic_scale)
            scale[current_note] = interval
        return scale

    def _next_note(self, current_note, chromatic_scale: list):
        notes = chromatic_scale
        current_index = notes.index(current_note)
        next_index = (current_index + 1) % len(notes)
        return notes[next_index]

    def generate(
        self,
        scale: str = 'major',
        tonic: str = 'C',
        interval_type: str = 'ascending'
    ):
        cromatic_scale = (self.cromatic_scale_ascending
                          if interval_type == 'ascending'
                          else self.cromatic_scale_descending)

        if scale == 'major':
            return self._generate_scale(tonic, self.major_scale_intervals, cromatic_scale)

        elif scale == 'minor':
            return self._generate_scale(tonic, self.minor_scale_intervals, cromatic_scale)

        elif scale == 'pentatonica':
            return self._generate_scale(tonic, self.pentatonica_scale_intervals, cromatic_scale)

        else:
            raise ValueError('Scale must be major or minor.')

    def view_complete_scales_graph(
        self,
        scale: str = 'major',
        interval_type: str = 'ascending'
    ):
        graph = {}
        cromatic_scale = (self.cromatic_scale_ascending
                          if interval_type == 'ascending'
                          else self.cromatic_scale_descending
                          )
        for note in cromatic_scale:
            graph[note] = self.generate(scale, note, interval_type)

        return graph


class MusicPlayer():
    def _get_frequency(self, note):
        # Mapeia as notas para as frequências correspondentes
        note_frequencies = {
            'C': 261,
            'Db': 277,
            'D': 293,
            'Eb': 311,
            'E': 329,
            'F': 349,
            'Gb': 369,
            'G': 392,
            'Ab': 415,
            'A': 440,
            'Bb': 466,
            'B': 493
        }
        return note_frequencies[note]

    def play_music(self, music: Music):
        print(f'Playing "{music.name}" in {music.tone} scale.')
        for note in music.music:
            frequency = self._get_frequency(note)  # Obtenha a frequência da nota
            duration = 1000  # Duração da nota em milissegundos
            winsound.Beep(frequency, duration)  # Reproduz o som
            print(note, end=' ')
