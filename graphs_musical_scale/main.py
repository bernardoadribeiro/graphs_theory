from pprint import pformat
from musical_scales import MusicalScale
from musical_scales import Music


if __name__ == '__main__':
    music = Music()

    op = str(input(
        'Select a option: \n'
        '[C1] Show all scales graph \n'
        '[D2] Generate major, minor and pentatonic scales \n'
        '[D3] Compose and Play a random melody \n'
        '[Just Press Enter] Play Twinkle Twinkle Little Star and exit\n'
    )).upper()

    if op == 'C1':
        scale_asc = MusicalScale().view_complete_scales_graph('major', 'ascending')
        scale_desc = MusicalScale().view_complete_scales_graph('major', 'descending')
        print('Ascending: \n', pformat(scale_asc, indent=4))
        print('Descending: \n', pformat(scale_desc, indent=4))

    elif op == 'D2':
        print(
            f"Major: {MusicalScale().generate('major', 'C', 'ascending')} \n"
            f"Minor: {MusicalScale().generate('minor', 'C', 'descending')} \n"
            f"Pentatonica: {MusicalScale().generate('pentatonica', 'C', 'ascending')} \n"
        )

    elif op == 'D3':
        scale = str(input('Scale [major/minor]: '))
        tone = str(input('Tone: ')).upper()
        interval_type = str(input('Interval type [ascending/descending]: '))

        music.compose_music(scale, tone, interval_type)
        music.play_music()

    else:
        music.name = 'Twinkle Twinkle Little Star'
        music.tone = 'C'
        music.interval_type = 'ascending'
        music.music = ['C', 'C', 'G', 'G', 'A', 'A', 'G', 'F', 'F', 'E', 'E', 'D', 'D', 'C']
        music.play_music()
