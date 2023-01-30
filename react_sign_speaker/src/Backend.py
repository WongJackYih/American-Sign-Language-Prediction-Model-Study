from flask import Flask,Response
import cv2
import os
import pickle
import numpy as np

# If mediapipe library is not installed on your device, open terminal and run command "pip install mediapipe"
# If you face Access is denied error [WinError 5] or other errors try to run this command "pip3 install --upgrade mediapipe --user"
# Once installed, a restart of visual studio code is required
import mediapipe as mp
import tensorflow # same process as above

app = Flask(__name__)
cap = cv2.VideoCapture(1)

def visualize_Prediction_Output(res, wordList, input_frame):
    output_frame = input_frame.copy()
    for num, prob in enumerate(res):
        cv2.rectangle(output_frame, (0,60+num*40), (int(prob*100), 90+num*40), -1)
        cv2.putText(output_frame, wordList[num], (0, 85+num*40), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2, cv2.LINE_AA)
        
    return output_frame

def load_label():
    label_path = os.path.join(path)
    with open(path, 'rb') as label_path:
        loaded_dict = pickle.load(label_path)
        return loaded_dict

def mediapipe_HolisticModel_Detection(image, model):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image.flags.writeable = False                 
    res = model.process(image)                
    image.flags.writeable = True                   
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    return image, res

def get_Landmark_Values(res):
    leftHand = np.array([[res.x, res.y, res.z] for res in res.left_hand_landmarks.landmark]).flatten() if res.left_hand_landmarks else np.zeros(21*3)
    rightHand = np.array([[res.x, res.y, res.z] for res in res.right_hand_landmarks.landmark]).flatten() if res.right_hand_landmarks else np.zeros(21*3)
    return np.concatenate([leftHand, rightHand])

def generate_frames():
    modelName = 'Vocabulary LSTM Model'
    outside = outside = os.path.normpath(cwd + os.sep + os.pardir)
    path = os.path.join(outside, 'LSTM Model', modelName, 'ASL_Word_Model.h5')
    model = tensorflow.keras.models.load_model(path)
    frameCap = 15
    sequence = []

    wordList = list(load_label().keys())
    with mediapipe_HolisticModel_Model.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5) as HolisticModel:
        while True:
                
            ## read the camera frame
            success,frame=cap.read()
            if not success:
                break
            else:
                image, results = mediapipe_HolisticModel_Detection(frame, HolisticModel)
                
                # 2. Prediction logic
                keypoints = get_Landmark_Values(results)
                sequence.append(keypoints)
                sequence = sequence[-frameCap:]
                        
                if len(sequence) == frameCap:
                    res = model.predict(np.expand_dims(sequence, axis=0))[0]
                    
                    # Viz probabilities
                    image = visualize_Prediction_Output(res, wordList, image)
                    ret,buffer=cv2.imencode('.jpg',image)
                    frame=buffer.tobytes()

                    yield(b'--frame\r\n'
                            b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


# API Route
@app.route('/video')
def video():
    return Response(generate_frames(),mimetype='multipart/x-mixed-replace; boundary=frame')
    
if __name__ == '__main__':
    modelName = 'Vocabulary LSTM Model'
    cwd = os.getcwd()
    outside = outside = os.path.normpath(cwd + os.sep + os.pardir)
    path = os.path.join(outside, 'LSTM Model', modelName, 'Labels.pkl')

    mediapipe_HolisticModel_Model = mp.solutions.holistic # HolisticModel model
    mediapipe_Draw_Landmarks = mp.solutions.drawing_utils # Drawing utilities
    app.run(debug=True)