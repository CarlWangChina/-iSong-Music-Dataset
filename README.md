# àiSong datasets
[download datasets](http://aige.midilib.com/%C3%A0imusic-datasets/%C3%A0imusic-datasets.zip)  
[view datasets](http://aige.midilib.com/%C3%A0imusic-datasets/datas/data-tone/)  
## Data Source and Processing
``` python
1 Data Source
To enrich the music styles of our dataset, we built the àiSong Dataset from scratch. We first collected 6,000 guitar scores, where we selected 650 oriental songs that meet our requirements. Furthermore, several music professionals are invited to manually standardize the naming rules and formats of our experimental data. We also split each song into mutually-different sections to reduce data repetition. Segments with different tonalities in the same song will also be listed separately. After 4 months of collection and processing, àiSong Dataset is finally completed, containing 2323 musical pieces.
Our àiSong Dataset is mainly based on the Chinese national pentatonic, which is composed of five positive tones, namely, "Gong(Do), Shang(Re), Jue(Mi), Zhi(Sol) and Yu(La)" and various partial tones. To better train the SongDriver on our original àiSong Dataset, we transpose the national pentatonic into a natural major with Gong as the tonic. 

2 Data Processing 
The àiSong Dataset is further standardized following the steps below. 
2.1 Rhythm Screening. We only reserve the music pieces in 4/4 and 2/4 time for subsequent sampling. To maintain a stable sampling granularity, pieces containing chords shorter than one beat are also deleted. 
2.2 Octave Transposition. For each piece of music, we calculate the current octave of the melody and accompaniment according to the note distribution. Then by adding to or subtracting several interval differences, we transpose the melody to the 6𝑡h row of the MIDI standard pitch table and the accompaniment to the 4𝑡h row. 
2.3 Mode Unification. Based on the music mode information in the dataset, we convert all major mode music to C major and all minor mode music to A minor. The distinguishment between major mode and minor mode is important because the extraction of our proposed four features is influenced by the mode of current music.

```
## Dataset Format Description
``` python
We use three different parts of information to represent a song in our dataset, including 1) musical tonality and mode, 2)melody sequence, 3)chord sequence of the accompaniment. A brief example is as follows:

#Tonality of the file
C:KeyMode.MAJOR 
# melody sequence,every 4 notes correspond to a chord
[74,74,74,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,72,72,76,76,76,76,74,74,74,74,74,74,74,74,74,71,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,60,65,65,65,65,65,65,67,67,67,64,64,64,64,64,64,64,64,64,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62] 
# chord sequence
[[38,41,45],[41,45,48],[41,45,48],[43,47,50],[43,47,50],[45,48,52],[45,48,52],[45,48,52],[45,48,52],[45,48,52],[45,48,52],[45,48,52],[45,48,52],[36,40,43],[36,40,43],[45,48,52],[45,48,52],[41,45,48],[41,45,48],[36,40,43],[36,40,43],[43,47,50],[43,47,50],[43,47,50],[43,47,50],[43,47,50],[43,47,50],[43,47,50],[43,47,50],[38,42,45]]

Musical tonality and mode 
are stored at the beginning of a piece of music data. For example, C:KeyMode.MAJOR means the music is in C major.

The melody sequence 
is a one-dimensional time series array, and the elements in the array are the MIDI pitch of the melody at the corresponding time. The melody sequence is sampled in units of sixteenth notes, that is, the time value of each element in the array is one quarter of a beat.

The chord sequence of accompaniment 
is also a one-dimensional timing array. The elements in the array are the chords at the corresponding time, which are expressed in the form of constituent tones. The chord sequence is sampled by quarter notes, that is, the time value of each element in the array is one beat.

```
## Parse File
``` python
    file = open("./datas/data-tone/1.txt") # open file
    arr = file.read().split("\n") # read file
    tone = arr[0] # get Tonality
    print(tone)
    melody = arr[1].strip("[]").split(",") # get melody
    print(melody)
    chord = arr[2].lstrip("[").rstrip("]").split("],[") # get chord
    print(chord)
```
