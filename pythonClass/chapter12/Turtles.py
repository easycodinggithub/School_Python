# pip install tensorflow
# pip install pillow
# pip install numpy
# pip install opencv-python
import tensorflow.keras
from PIL import Image, ImageOps
import numpy as np
import cv2
import time

import turtle as t

################# 터틀 방향키 #########################
t1=t.Turtle()
t1.pensize(10)

def t_up():
     t1.seth(90)
     t1.forward(10)
def t_down():
     t1.seth(270)
     t1.forward(10)
def t_right():
     t1.seth(0)
     t1.forward(10)
def t_left():
     t1.seth(180)
     t1.forward(10)
def t_stop():
     t1.seth(0)
     

################# 터틀 방향키 #########################


#클래스 이름 가져오기
labels=[]
f=open("labels.txt", "r")
for x in f:
     labels.append(x.rstrip('\n'))
label_count = len(labels)
f.close()

#생성된 모델 불러오기
# e-04,e+10과 같은  과학적 표기법을 제거하고 싶을 때 사용하는 옵션
np.set_printoptions(suppress=True)

# Teachable Machine에서 학습시킨 모델 파일을 컴파일을 다시 하지 않고, model 변수에 넣음
model = tensorflow.keras.models.load_model('keras_model.h5', compile=False)

# numpy를 이용해 이미지를 1차원, 높이 224pixel, 폭 224pixel, 색상 3채널(RGB)로 변환해서 data 변수를 만듬.  형식은 float32,
# 여기서는 data 변수를 만드는 의미로 쓰임(4차원의 배열이 만들어짐)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

# OpenCV를 이용해 캠으로 들어오는 영상을 cap 변수에 넣음, '0'은 컴퓨터가 인식한 첫번째 카메라를 의미함
cap = cv2.VideoCapture(0)

print('Press "q", if you want to quit')
# while문 안의 내용을 계속 반복시켜 모델 계속 평가하기
while(True):
     # 웹캠에서 이미지 가져와 이미지 사이즈를 변경해 생성된 모델로 평가하기
     #time.sleep(1)
    # cap 변수에 비디오 프레임이 들어올 때마다 읽어서 frame 변수에 넣음,
    # 제대로 프레임이 읽어지면 ret값이 True, 실패하면 False가 나타남
    # ret는 True, frame.shape는 (480, 640, 3)의 배열로 생성됨.
     ret, frame = cap.read()
     # 들어온 이미지 플립, 이미지 좌우반전(1은 좌우반전, 0은 상하반전)
     flip_frame = cv2.flip(frame, 1)
     # 이미지 높이, 폭 추출  
     h = flip_frame.shape[0] #480 행의수
     w = flip_frame.shape[1] #640 열의수

     # 바이큐빅보간법(cv2.INTER_CUBIC, 이미지를 확대할 때 주로 사용)을 이용해
    # frame변수에 들어온 비디오 프레임의 사이즈를 224, 224로 다운사이징하여 image 변수에 넣음
    # 480,480 이미지를 224, 224이미지로 리사이즈 시킴
     crop_image = flip_frame[0:h, int((w-h)/2):int(w-((w-h)/2))]
     image = cv2.resize(crop_image, dsize=(224, 224), interpolation=cv2.INTER_CUBIC)

     # asarray메소드를 이용해 image에 들어있는 크기가 변형된 이미지를
    # numpy가 처리할 수 있는 배열로 만들어서 image_array 변수에 넣음
    # 리스트 배열을 np배열로 변환
    # np.array는 참조본을 반환하고 np.asarray는 복사본을 반환한다.
     image_array = np.asarray(image)
    # image_array에 들어있는 image의 변형된 배열을 정규화(normalized)하기 위해 수식을 적용함
    # 배열값을 -1~1사이값으로 변경
     normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1

     # 정규화된 배열을 data[0]에 넣음
     data[0] = normalized_image_array

     # 정규화된 배열값으로 정돈된 data를 Teachable Machine으로 학습시켜서 얻은 모델을 이용해 추론하고,
    # 그 결과를 prediction 변수에 넣음
    # [[0.01828334 0.8726836  0.10874491 0.00028817]]
     prediction = model.predict(data)
     
     #콘솔창에 결과 표시
     print(labels)
     print(prediction)

     # 글씨 넣기 준비
     font = cv2.FONT_HERSHEY_TRIPLEX
     fontScale = 1
     fontColor = (0,255,0)
     lineThickness = 1
     
     # 표기 문구 초기화
     scoreLabel = 0
     score = 0
     result = ''
     #예측값 모니터링
     for x in range(0, label_count):
          #예측값 반올림하여 화면에 표시
          line=('%s=%0.0f' % (labels[x], int(round(prediction[0][x]*100)))) + "%"
          cv2.putText(crop_image, line, (10,(x+1)*35), font, fontScale, fontColor, lineThickness)

          # 가장 높은 예측 찾기
          if score < prediction[0][x]:
               scoreLabel = labels[x]
               score = prediction[0][x]
               result = str(scoreLabel) + " : " + str(score)
     print(result)
          
     # 최고 결과치 보여주기
     crop_image = cv2.putText(crop_image, result, (10, int(label_count+1)*35), font, 1, (0, 0, 255), 1, cv2.LINE_AA)
     cv2.imshow('crop_image',crop_image)



##############################결과값에 터틀 코딩 코딩하기######################################

     #예측값에 따라 동작하기(클래스에 갯수에 맞게 생성)
     if prediction[0, 0] > 0.7 :
          t_up()
     elif prediction[0, 1] > 0.7 :
          t_down()
     elif prediction[0, 2] > 0.7 :
          t_left()
     elif prediction[0, 3] > 0.7 :
          t_right()
     else :
          t_stop()
          

#################################################################################################          
     print()

     # 키 입력을 기다림
     key = cv2.waitKey(1) & 0xFF

     # q 키를 눌렀다면 반복실행에서 종료함
     if key == ord("q"):
          print('Quit')
          break

# 동작이 종료되면 비디오 프레임 캡쳐를 중단함
cap.release()
# 모든 창을 닫음
cv2.destroyAllWindows()
