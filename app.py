
from flask import Flask,render_template,request,redirect,url_for,jsonify
import json
import speech_recognition as sr
import io
from pathlib import Path
from flask_cors import CORS

def SpeechToText(path):
   
    r = sr.Recognizer()
    s=''
    hellow=sr.AudioFile(path)
    with hellow as source:
        audio = r.record(source)
        try:
            s = r.recognize_google(audio)
            print("Text: "+s)
        except Exception as e:
            print("Exception: "+str(e))
    return s

app=Flask(__name__)

CORS(app)

@app.route('/', methods=['GET', 'POST'])
def result():
    # path=str(Path(__file__).resolve().parent)+'\\audio.wav'

    if request.method == 'POST':
        
        # print(request.files)
        file = request.files['audio_data']
        file_obj = io.BytesIO()  # create file-object
        file_obj.write(file.read()) # write in file-object
        file_obj.seek(0) # move to beginning so it will read from beginning
        
        text=SpeechToText(file_obj)
        print(text)
        return (text)
    else:
        return ("bad request")

if __name__=='__main__':
    # from waitress import serve
    # serve(app, host="0.0.0.0", port=8080)
    app.run(debug=True,threaded=True)



