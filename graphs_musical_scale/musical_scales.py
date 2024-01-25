import winsound
import random


class Music:
    """A class representing music composition and playback.

    Attributes:
        name (str): The name of the music composition.
        tone (str): The tone of the music composition.
        interval_type (str): The interval type of the music composition.
        notes (list): The list of notes in the music composition.
        music (list): The generated melody of the music composition.
    """

    def _make_melody(self, notes_to_use, size: int = 12):
        """Randomly select notes to create a melody.

        Args:
            notes_to_use (dict): A dictionary containing the available notes.
            size (int, optional): The size of the melody. Defaults to 12.

        Returns:
            list: The generated melody.
        """
        melody = []
        for _ in range(size):
            melody.append(
                random.choice(list(notes_to_use.keys()))
            )

        return melody

    def compose_music(self, scale: str, tone: str, interval_type: str):
        """Compose music based on the given scale, tone, and interval type.

        Args:
            scale (str): The musical scale to use.
            tone (str): The tone of the composition.
            interval_type (str): The interval type of the composition.

        Returns:
            list: The generated notes of the composition.
        """
        self.name = f'Sonata in {tone} {scale}'
        self.tone = tone
        self.interval_type = interval_type
        self.notes = MusicalScale().generate(scale, tone, interval_type)
        self.music = self._make_melody(self.notes)

        return self.notes

    def _get_frequency(self, note):
        """Return the frequency of a given note.

        Args:
            note (str): The note for which to retrieve the frequency.

        Returns:
            int: The frequency of the note.
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

    def play_music(self):
        """Play the composed music."""
        print(f'Playing {self.name} in {self.tone} tone, in {self.interval_type} scale.')
        for note in self.music:
            frequency = self._get_frequency(note)  # Gets note frequency
            duration = 500  # Note duration in milliseconds
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
        self.minor_scale_intervals = [0, 2, 1, 2, 2, 2, 1, ]

        # Starts in the 2nd degree, finish in 4th, tonic is 0
        self.pentatonica_scale_intervals = [0, 2, 2, 3, 2, ]

        self.cromatic_scale_ascending = ['C', 'C#', 'D',
                                         'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
        self.cromatic_scale_descending = ['B', 'Bb', 'Ab',
                                          'A', 'G', 'Gb', 'F', 'E', 'Eb', 'D', 'Db', 'C']

    def _generate_scale(self, tonic: str, intervals: list, chromatic_scale: list):
        """
        Generates a musical scale based on the given tonic, intervals, and chromatic scale.

        Args:
            tonic (str): The tonic note of the scale.
            intervals (list): The intervals between each degree of the scale.
            chromatic_scale (list): The chromatic scale used as the base.

        Returns:
            dict: A dictionary representing the generated scale, where the keys are the notes
            and the values are the intervals.
        """
        scale = {}  # if we want to add the tonic note, we can use this line: scale[tonic] = 0
        current_note = tonic
        for interval in intervals:
            for _ in range(interval):
                current_note = self._next_note(current_note, chromatic_scale)
            scale[current_note] = interval
        return scale

    def _next_note(self, current_note, chromatic_scale: list):
        """
        Returns the next note in the chromatic scale based on the current note.

        Args:
            current_note (str): The current note.
            chromatic_scale (list): The chromatic scale.

        Returns:
            str: The next note in the chromatic scale.
        """
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
        """
        Generates a musical scale based on the given parameters.

        Args:
            scale (str, optional): The type of scale to generate. Defaults to 'major'.
            tonic (str, optional): The tonic note of the scale. Defaults to 'C'.
            interval_type (str, optional): The type of interval to use. Defaults to 'ascending'.

        Returns:
            dict: A dictionary representing the generated scale, where the keys are the notes
            and the values are the intervals.

        Raises:
            ValueError: If the scale is not 'major' or 'minor'.
        """
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
        """
        Generates a graph of complete scales based on the given parameters.

        Args:
            scale (str, optional): The type of scale to generate. Defaults to 'major'.
            interval_type (str, optional): The type of interval to use. Defaults to 'ascending'.

        Returns:
            dict: A dictionary representing the complete scales graph, where the keys are the notes
            and the values are the scales.
        """
        graph = {}
        cromatic_scale = (self.cromatic_scale_ascending
                          if interval_type == 'ascending'
                          else self.cromatic_scale_descending
                          )
        for note in cromatic_scale:
            graph[note] = self.generate(scale, note, interval_type)

        return graph
