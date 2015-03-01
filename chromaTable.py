import os
import sys
import numpy as np


smf2txt = './smf2txt'


class Track():
    def __init__(self):
        self.notesNum = []
        self.name = []
        self.info = np.empty([0, 4])

    
def chromaTable(midifile):
    txttemp = 'temp.txt'
    order = smf2txt + ' -q 1024 ' + midifile + ' > ' + txttemp
    try: os.system(order)
    except:
        print 'ERROR on ' + order
        sys.exit(1)
        
    f = open(txttemp,'r')
    midi_lines = f.readlines()
    f.close()
    
    
    tracklist = []
    cont = -1
    for midi_line in range(len(midi_lines)):
        midi_lines[midi_line] = midi_lines[midi_line][:-1]
        if midi_lines[midi_line].find('#') != -1 or midi_lines[midi_line].find('@') != -1 :
            if midi_lines[midi_line].find('track') != -1: ##pensar a posar excepcions
                cont += 1
                tracklist.append(Track())
                tp = midi_lines[midi_line].split(' ')
                tracklist[cont].name = tp[2]
                notes = 0
        else:
            tracklist[cont].info = np.vstack([tracklist[cont].info, np.array(midi_lines[midi_line].split(' '))])
            notes += 1

    return tracklist