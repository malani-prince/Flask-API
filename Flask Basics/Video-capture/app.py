# pip install python 
# pip install opencv-python

from flask import Flask, request, render_template, url_for, redirect, Response
import cv2

app = Flask(__name__)

def gen_frames():
    # create the object which capture Frame from the camara
    # trigger the camera we pass 0 as an arguments.
    camera = cv2.VideoCapture(0)  
    
    # return the frames, continuously 
    while True:
        # add the window and generate the frame
        # success: a bool data type, return true or false
        # frame: a numpy array whih contain capture frame
        #read(): return bool. if frame is read correctly.
        success, frame = camera.read()  
        
        if not success:
            break
        else:
            # ret: return the value:
            # buffer: store Value of image
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == "__main__":
    app.run(debug=True)