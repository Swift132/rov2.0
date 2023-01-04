import picamera
import gst-rtsp-server

# Crie uma instância da câmera
camera = picamera.PiCamera()

# Configure a resolução e a taxa de quadros da câmera
camera.resolution = (640, 480)
camera.framerate = 30

# Crie um pipeline de vídeo usando o gst-rtsp-server
pipeline = (
    "rtspsrc location=rtsp://0.0.0.0:8554/stream latency=0 ! "
    "rtph264depay ! h264parse ! avdec_h264 ! videoconvert ! "
    "x264enc tune=zerolatency ! rtph264pay name=pay0 pt=96"
)

# Inicie a câmera e o pipeline
camera.start_recording(pipeline, format="h264")
server = gst-rtsp-server.Server()
server.attach(pipeline)
server.set_service("8554")

# Execute o loop infinito para transmitir o vídeo
while True:
    pass