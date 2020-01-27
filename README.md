# conductify
Project for ConUHacks
The idea of this project was to create an application that would let users control the volume elements of music files much like a conductor in an orchestra.

We do this by:

1. Taking a music file, feeding it through a pre-trained machine learning model "Spleeter" to split it into it's substituent parts.

Conductify can currently split music files into these Elements: 
* Vocals
* Bass
* Drums
* Piano
* Other

2. After splitting the music files, the users can use an arduino with a {SENSOR_NAME} sensor and control the volume of individual elements LIVE as the song plays.

3. The PyQt5 GUI visualizes Element selection, and Volume control for the user. 

4. The app also allows the user to fetch new music files from the web using an API provided by OG.

Next Steps:


