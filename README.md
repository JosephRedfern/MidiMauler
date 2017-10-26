MidiMutator
===========

Takes in an input midi file + severity parameter, and randomly changes notes in said midi file (with varying frequency/likelihood accoring to severity). Because reasons.

Very hacked together. Relies on [CSVMidi](http://www.fourmilab.ch/webtools/midicsv/) to convert midi->csv and vis-versa, [Timidity](http://timidity.sourceforge.net/) for Midi Synthesis, any Python for maulin' up the midis.

`MidiMauler` requires the path to a prepared MIDI CSV file (passed through csvmidi using `csvmidi filename.mid > filename.csv`). It can then be used to mutate midi files like so:

```
mm = MidiMauler("midifile.csv")
mm.mutate(severity=20, filename="mauled.csv")
```

This will write out a mauled midi csv file to `mauled.csv`, which can be midifiedusing `midicsv mauled.csv > mauled.mid`. Timidity can then be used for playback of midi file, and pair with ffmpeg to get an mp3 of the track. See `run.sh` for an example.
