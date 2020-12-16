import cv2
import face_recognition


face_locations = []
face_encodings = []
face_names = []
frame_number = 0

# Bước 1: Lấy video
video = cv2.VideoCapture(r"test.mp4")
print("1")
length = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
print("2")

# Bước 2: tạo biến mảng
image = face_recognition.load_image_file(r"Capture.PNG")
print("3")
face_image = face_recognition.face_locations(image)
print("4")
face_encodings  = face_recognition.face_encodings(image,face_image)

print("5")
know_faces = [
    face_encodings,
]

while(True):
    #tạo khung hình từ video
    ret, frame = video.read()
    print("6")
    frame_number += 1
    
    if not ret:
        print("6.5")
        break
    
    #chuyển đổi từ hình ảnh sang màu sắc theo dạng BGR để nhận diện khuôn mặt
    rgb_frame = frame[:, :, ::-1]
    
    #tìm tất cả khuôn mặt trong video
    face_locations = face_recognition.face_locations(rgb_frame, model='cnn')
try:
    face_encoding = face_recognition.face_encodings(rgb_frame, face_locations)
    print("7")
except IndexError as e:
    print(e)
    sys.exit(1)

    face_names = []
    
    for face_encoding in face_encodings:
        match = face_recognition.compare_faces(know_faces,face_encodings, tolerance=0.50)
        
        name = None
        if(match[0]):
            name = "DUng dep trai"
            print("8")
            
        face_names.append(name)
        
    
    for top, right, bottom, left, name in zip(face_location, face_names):
        if not name:
            continue
        
        cv2.rectangle(frame, (left, top), (right, bottom), (0,0 , 255), 2)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(frame,name, (left + 6, bottom -6), font, 0.5, (255,255,255),1)
    
        print("writing frame {} / {}".format()(frame_number, length))
    output_movie.write(frame)
    print("9")
        
        
    cv2.imshow('frame', frame)
if cv2.waitKey(1) & 0xFF == ord('q'):
    sys.exit()    
    
output_movie.release()
cv2.destroyAllWindows()


# face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
# image = cv2.imread(r"user.jpg")

# # Bước 2: Tạo một bức ảnh xám
# grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# # Bước 3: Tìm khuôn mặt
# faces = face_cascade.detectMultiScale(
#     grayImage,
#     scaleFactor  = 1.1,
#     minNeighbors = 3,
# )

# # Bước 4: Vẽ các khuôn mặt đã nhận diện được lên tấm ảnh gốc
# for (x, y, w, h) in faces:
#     cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

# # Bước 5: Vẽ lên màn hình
# cv2.imshow("Faces found", image)