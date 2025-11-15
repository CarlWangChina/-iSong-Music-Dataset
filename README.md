# àiSong datasets
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
[download datasets](http://aige.midilib.com/%C3%A0imusic-datasets/%C3%A0imusic-datasets.zip)  
[view datasets](http://aige.midilib.com/%C3%A0imusic-datasets/datas/data-tone/)  
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

## Citation
If you use this work in your research, please cite our paper:
```
@inproceedings{10.1145/3503161.3548368,
author = {Wang, Zihao and Zhang, Kejun and Wang, Yuxing and Zhang, Chen and Liang, Qihao and Yu, Pengfei and Feng, Yongsheng and Liu, Wenbo and Wang, Yikai and Bao, Yuntao and Yang, Yiheng},
title = {SongDriver: Real-time Music Accompaniment Generation without Logical Latency nor Exposure Bias},
year = {2022},
isbn = {9781450392037},
publisher = {Association for Computing Machinery},
address = {New York, NY, USA},
url = {https://doi.org/10.1145/3503161.3548368},
doi = {10.1145/3503161.3548368},
abstract = {Real-time music accompaniment generation has a wide range of applications in the music industry, such as music education and live performances. However, automatic real-time music accompaniment generation is still understudied and often faces a trade-off between logical latency and exposure bias. In this paper, we propose SongDriver, a real-time music accompaniment generation system without logical latency nor exposure bias. Specifically, SongDriver divides one accompaniment generation task into two phases: 1) The arrangement phase, where a Transformer model first arranges chords for input melodies in real-time, and caches the chords for the next phase instead of playing them out. 2) The prediction phase, where a CRF model generates playable multi-track accompaniments for the coming melodies based on previously cached chords. With this two-phase strategy, SongDriver directly generates the accompaniment for the upcoming melody, achieving zero logical latency. Furthermore, when predicting chords for a timestep, SongDriver refers to the cached chords from the first phase rather than its previous predictions, which avoids the exposure bias problem. Since the input length is often constrained under real-time conditions, another potential problem is the loss of long-term sequential information. To make up for this disadvantage, we extract four musical features from a long-term music piece before the current time step as global information. In the experiment, we train SongDriver on some open-source datasets and an original \`{a}iMusic Dataset built from Chinese-style modern pop music sheets. The results show that SongDriver outperforms existing SOTA (state-of-the-art) models on both objective and subjective metrics, meanwhile significantly reducing the physical latency.},
booktitle = {Proceedings of the 30th ACM International Conference on Multimedia},
pages = {1057–1067},
numpages = {11},
keywords = {automatic improvisation, music accompaniment generation},
location = {Lisboa, Portugal},
series = {MM '22}
}
