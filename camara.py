import cv2
from flask import Flask, render_template, Response

app = Flask(__name__)

@app.route('/html')

def index():
    return render_template('index.html')

@app.route('/')

def gen():
    # Obtém a referência da câmera
    camera = cv2.VideoCapture(0)

    # Define o codec do vídeo
    fourcc = cv2.VideoWriter_fourcc(*'H264')

    # Cria um objeto VideoWriter
    out = cv2.VideoWriter('output.mp4', fourcc, 20.0, (640, 480))

    while True:
        # Captura o próximo frame da câmera
        success, frame = camera.read()

        # Verifica se o frame foi capturado corretamente
        if not success:
            break

        # Ajusta o tamanho do frame para 640x480
        frame = cv2.resize(frame, (640, 480))

        # Adiciona o frame ao arquivo de saída
        out.write(frame)

        # Converte o frame para o formato JPEG
        ret, jpeg = cv2.imencode('.jpg', frame)

        # Envia o frame para o cliente
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + jpeg.tobytes() + b'\r\n\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
