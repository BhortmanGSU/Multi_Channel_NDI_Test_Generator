import subprocess
import signal

processes = []

for i in range(1, 9):
    source_name = f"Source{i}"
    pipeline = f'''gst-launch-1.0 \
        videotestsrc pattern=ball is-live=true ! video/x-raw,format=UYVY,width=1280,height=720,framerate=60000/1001 ! mixer.sink_0 \
        videotestsrc pattern=smpte is-live=true ! video/x-raw,format=UYVY,width=1280,height=720,framerate=60000/1001 ! mixer.sink_1 \
        compositor name=mixer sink_1::alpha=0.5 ! textoverlay text="{source_name}" valignment=center halignment=center font-desc="Sans, 36" ! textoverlay text="GSPN Engineering" valignment=bottom halignment=left font-desc="Sans, 24" ! ndisinkcombiner name=combiner ! ndisink ndi-name="SMPTE TEST ({source_name})" \
        audiotestsrc wave=white-noise is-live=true ! combiner.audio'''

    p = subprocess.Popen(pipeline, shell=True)
    processes.append(p)

# Run until interrupted
try:
    while True:
        pass
except KeyboardInterrupt:
    # Terminate all the processes on Ctrl+C
    for p in processes:
        p.send_signal(signal.CTRL_C_EVENT)