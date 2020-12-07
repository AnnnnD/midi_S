#!/opt/anaconda3/envs/music/bin/python3
"""
Print a description of the available devices.
"""
import midi.sequencer as sequencer

s = sequencer.SequencerHardware()

print s
