import cv2
import numpy as np
import streamlit as st
# from pygame import mixer
from tensorflow.keras.models import load_model

# Load the trained model
model = load_model('Model.h5')

# Load the cascade classifiers
face_cascade = cv2.CascadeClassifier('haarcascade/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade/haarcascade_eye.xml')

# Initialize audio mixer
# mixer.init()
# sound = mixer.Sound('alarm.mp3')

# Set up video capture
cap = cv2.VideoCapture(0)

# Initialize variables
Score = 0
eyes_closed = False
alert_displayed = False

# Streamlit app
st.title('Drowsiness Detection App')

# Placeholder for the final frame
output_frame = st.empty()

# Create two columns for buttons
col1, col2 = st.columns(2)

# Button to start the Drowsiness Detection
start_button = col1.button('Start')

# Button to stop the Drowsiness Detection
stop_button = col2.button('Stop')

if start_button:
    while True:
        ret, frame = cap.read()
        height, width = frame.shape[0:2]
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5)
        eyes = eye_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=1)
        
        cv2.rectangle(frame, (0, height-50), (200, height), (0, 0, 0), thickness=cv2.FILLED)
        
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, pt1=(x, y), pt2=(x+w, y+h), color=(255, 0, 0), thickness=3)
            
        for (ex, ey, ew, eh) in eyes:
            eye = frame[ey:ey+eh, ex:ex+ew]
            eye = cv2.resize(eye, (80, 80))
            eye = eye / 255
            eye = eye.reshape(80, 80, 3)
            eye = np.expand_dims(eye, axis=0)
            
            prediction = model.predict(eye)
            
            if prediction[0][0] > 0.30:  # Closed eyes
                cv2.putText(frame, 'closed', (10, height-20), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=1, color=(255, 255, 255),
                            thickness=1, lineType=cv2.LINE_AA)
                cv2.putText(frame, 'Score: ' + str(Score), (100, height-20), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=1, color=(255, 255, 255),
                            thickness=1, lineType=cv2.LINE_AA)
                Score += 1
                if Score > 15 and not alert_displayed:
                    try:
                        # sound.play()
                        st.warning("Eyes are closed!")
                        alert_displayed = True
                    except:
                        pass
                
            elif prediction[0][1] > 0.90:  # Open eyes
                cv2.putText(frame, 'open', (10, height-20), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=1, color=(255, 255, 255),
                            thickness=1, lineType=cv2.LINE_AA)      
                cv2.putText(frame, 'Score: ' + str(Score), (100, height-20), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=1, color=(255, 255, 255),
                            thickness=1, lineType=cv2.LINE_AA)
                Score -= 1
                if Score < 0:
                    Score = 0
                if alert_displayed:
                    st.warning("")
                    alert_displayed = False
        
        # Update the output frame with the processed frame
        output_frame.image(frame, channels='BGR')
        
        if stop_button:
            break
            
    cap.release()
    cv2.destroyAllWindows()
