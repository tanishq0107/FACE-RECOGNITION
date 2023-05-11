import face_recognition
import os
import cv2
from pathlib import Path

#importing base64 module
# import base64
 
# #open file with base64 string data
# file = open(r"D:\Ausweg projects\source code\images\unknown\detect.txt", 'rb')
# encoded_data = file.read()
# file.close()

# #decode base64 string data
# decoded_data=base64.b64decode((encoded_data))

# #write the decoded data back to original format in  file
# img_file = open('image.jpeg', 'wb')
# img_file.write(decoded_data)
# img_file.close()

while(1):
    
    def read_img(path):
        img = cv2.imread(path)
        (h, w) = img.shape[:2]
        width = 500
        ratio = width/float(w)
        height = int(h*ratio)
        return cv2. resize(img, (width, height))

    known_encodings = []
    known_names = []
    known_dir = 'D:\Ausweg projects\source code\images\known'

    for file in os.listdir(known_dir):
        img = read_img(known_dir + '/' + file)
        try:
            img_enc = face_recognition.face_encodings(img)[0]
        except IndexError as e:
            print(e)
        known_encodings.append(img_enc)
        known_names.append(file.split('.')[0])

        # print(known_encodings)

    unknown_dir = r'D:\Ausweg projects\source code\images\unknown'
    path = Path(unknown_dir)

    # if os.path.isfile(r"D:\Ausweg projects\source code\images\unknown\1.jpg"):
    if not os.listdir(unknown_dir):
        print("Directory is empty.")
    elif os.listdir(unknown_dir):
    
            for file in os.listdir(unknown_dir):
                print("processing", file)
                img = read_img(unknown_dir + '/' + file)
                img_enc = face_recognition.face_encodings(img)[0]

                results = face_recognition.compare_faces(known_encodings, img_enc)
                        
                for i in range(len(results)):
                    if results[i]:
                        
                        print("match found: ", known_names[i])
                    else:
                        x = False
                # if x == False:
                #     print("No match found")
                        

            