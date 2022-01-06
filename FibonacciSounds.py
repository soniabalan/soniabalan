# MUSIC WITH PYTHON
import numpy as np
from pprint import pprint
from scipy.io.wavfile import write

# Code adapted from: https://github.com/weeping-angel/Mathematics-of-Music
# Number to note assignment inspired by: https://www.youtube.com/watch?v=IGJeGOw8TzQ

samplerate = 44100

def get_wave(freq, duration=0.5):
    #IN: frequecy time_duration for a wave 
    #OUT "numpy array" of values at all points in time
    
    amplitude = 4096
    t = np.linspace(0, duration, int(samplerate * duration))
    wave = amplitude * np.sin(2 * np.pi * freq * t)
    
    return wave

def get_piano_notes():
    #Returns a dict object for all the piano note freqs.

    # WHITE keys
    # black(sharp) keys
    octave = ['C', 'c', 'D', 'd', 'E', 'F', 'f', 'G', 'g', 'A', 'a', 'B', 'H','h','I','i','J','K','k','L','l','M','m','N'] 
    # added notes H through k to have all the numbers as in video
    
    base_freq = 261.63 #Frequency of Note C4
    base_freq2 = 523.25
    
    note_freqs1 = {octave[i]: base_freq * pow(2,(i/12)) for i in range(12)} #C4-B4 octave
    note_freqs2 = {octave[i+12]: base_freq2 * pow(2,(i/12)) for i in range(12)} #C5-B5 octave
    
    note_freqs = {**note_freqs1, **note_freqs2} #2 octave piano 
    note_freqs[''] = 0.0 # silent note
    
    return note_freqs
  
  # To get the piano note's frequencies
note_freqs = get_piano_notes()

def get_song_data(music_notes):
    # Function to concatenate all the waves (notes)
    
    note_freqs = get_piano_notes() # Function that we made earlier
    song = [get_wave(note_freqs[note]) for note in music_notes.split('-')]
    song = np.concatenate(song)
    return song

def get_chord_data(chords):
    chords = chords.split('-')
    note_freqs = get_piano_notes()
    
    chord_data = []
    for chord in chords:
        data = sum([get_wave(note_freqs[note]) for note in list(chord)])
        chord_data.append(data)
    
    chord_data = np.concatenate(chord_data, axis=0)    
    return chord_data.astype(np.int16)

def main():

    music_notes ='d' # fibonacci sequence starts with 0
    fib_seq = '112358132134558914423337761098715972584418167651094617711286574636875025'
    for nr in fib_seq:
        if nr==str(0):
            music_notes+='-d'
        elif nr=='1':
            music_notes+='-E'
        elif nr=='2':
            music_notes+='-f'
        elif nr=='3':
            music_notes+='-g'
        elif nr=='4':
            music_notes+='-A'
        elif nr=='5':
            music_notes+='-B'
        elif nr=='6':
            music_notes+='-h'
        elif nr=='7':
            music_notes+='-i'
        elif nr=='8':
            music_notes+='-J'
        elif nr=='9':
            music_notes+='-k'

    # print(music_notes)
    data = get_song_data(music_notes)
    data = data * (16300/np.max(data)) # Adjusting the Amplitude (Optional)
    write('fibonacci_sounds.wav', samplerate, data.astype(np.int16))

    
if __name__=='__main__':
    main()
