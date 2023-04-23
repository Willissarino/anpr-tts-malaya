from fastapi import FastAPI, Form
from fastapi.responses import FileResponse, StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
import malaya_speech
import soundfile as sf
import io

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8000",
    "*"
]

app.add_middleware(
     CORSMiddleware,
     allow_origins=origins,
     allow_credentials=True,
     allow_methods=["*"],
     allow_headers=["*"],
)

# Use malaya_speech to generate speech
yasmin = malaya_speech.tts.vits(model = 'mesolitica/VITS-yasmin')
#f_singlish = malaya_speech.tts.vits(model = 'mesolitica/VITS-female-singlish')


@app.post('/api/generate-speech')
async def generate_speech(text: str = Form(...)):
    
    # Predict
    r_yasmin = yasmin.predict(text, sid = 0)
    
    # Create a file-like buffer to hold the audio data
    #audio_data = io.BytesIO()
    #sf.write(audio_data, r_yasmin["y"], 22050, format="WAV", subtype="PCM_16")
    #audio_data.seek(0)
    
    # Return the file as streaming response
    #return StreamingResponse(audio_data, media_type="audio/wav")
    
    # Save the audio to a WAV file
    output_path = "output.wav"
    sf.write(output_path, r_yasmin["y"], 22050, "PCM_16")
    
    # Return the file
    return FileResponse("output.wav", media_type="audio/wav")

""" Citation """
""" @misc{Malaya, Speech-Toolkit library for bahasa Malaysia, powered by Deep Learning Tensorflow, """
"""   author = {Husein, Zolkepli},  """
"""   title = {Malaya-Speech}, """
"""   year = {2020}, """
"""   publisher = {GitHub}, """
"""   journal = {GitHub repository}, """
""" }  """

