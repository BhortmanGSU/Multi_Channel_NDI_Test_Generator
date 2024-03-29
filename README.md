# Multi_Channel_NDI_Test_Generator
This is a simple multichannel signal generator I made using Python and the Gstreamer Framework. 
It features Smpte bars, bouncing ball, animated static, and white noise.

# Requirements 
NDI SDK 
https://ndi.video/download-ndi-sdk/

Gstreamer multimedia framework 
https://gstreamer.freedesktop.org/download/
Download and install both runtime and development installer 

This will also get you setup with the Gstreamer framework with NDI! <3 

(I did this on Windows, I'm unsure about other devices) 

# Notes 
If your machine is beefy, then you can add more channels. This is an 8 channel for use on my Samsung galaxy book ultra 3 laptop, but if you edit the python script in a text editor at: 
for i in range(1, 9):  to say (1,17) Then you will have 16 named channels 

*This currently only uses software encoding, so everything is on the CPU  
