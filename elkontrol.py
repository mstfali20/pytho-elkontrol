import cv2
import mediapipe
import pyttsx3

camera= cv2.VideoCapture(0)#tek kamera oldugu icin 0.kameraya indexini atiyoruz
sesmotoru=pyttsx3.init()
sesmotoru.setProperty('language', 'tr')

mpHands=mediapipe.solutions.hands

hands=mpHands.Hands()

mpDraw=mediapipe.solutions.drawing_utils

hareket=False

while True:
    succces, img =  camera.read() # kameradan goruntu yakalar eger goruntu yakalnmazsa succes false olur img bos gelir ture ise img icine yakalanan fotoyu atar 
    imgRGB =cv2.cvtColor(img, cv2.COLOR_BGR2RGB)# gelen img rgb formatina cevirdik
    hlms=hands.process(imgRGB)
    height, width, channel = img.shape
    if hlms.multi_hand_landmarks:
        for handlandmarks in hlms.multi_hand_landmarks:

            for fingerNum, landmark in enumerate(handlandmarks.landmark):
                positionX, positionY = int(landmark.x * width), int(landmark.y * height)

                cv2.putText(img,str(fingerNum),(positionX,positionY),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,0),2)
              
            #   ------------------------- baş parmagı beyaz işaretleme finger numarasına göre
                # if fingerNum==4:  
                #     cv2.circle(img,(positionX,positionY),30,(255,255,255),cv2.FILLED)

               
                if handlandmarks.landmark[8].y>handlandmarks.landmark[6].y:
                    if handlandmarks.landmark[16].y>handlandmarks.landmark[14].y:
                        if handlandmarks.landmark[20].y>handlandmarks.landmark[18].y:            
                                if handlandmarks.landmark[12].y<handlandmarks.landmark[11].y:
                                    if handlandmarks.landmark[11].y<handlandmarks.landmark[10].y:
                                        if handlandmarks.landmark[10].y<handlandmarks.landmark[9].y:
                                            print("sana girsin")     
                                            # hareket = True
                elif handlandmarks.landmark[16].y>handlandmarks.landmark[14].y:
                    if handlandmarks.landmark[12].y>handlandmarks.landmark[11].y:
                        if handlandmarks.landmark[17].y>handlandmarks.landmark[18].y:
                            if handlandmarks.landmark[18].y>handlandmarks.landmark[19].y:
                                if handlandmarks.landmark[19].y>handlandmarks.landmark[20].y:
                                    if handlandmarks.landmark[5].y>handlandmarks.landmark[6].y:
                                        if handlandmarks.landmark[6].y>handlandmarks.landmark[7].y:
                                            if handlandmarks.landmark[7].y>handlandmarks.landmark[8].y:
                                                print("Bas koymusum Turkıyemın yoluna ")


                # if fingerNum == 10  and landmark.y < handlandmarks.landmark[2].y:  
                #     break

                # if fingerNum == 20 and landmark.y > handlandmarks.landmark[2].y:

                #    hareket = True
                     
                
                # if fingerNum > 4 and landmark.y < handlandmarks.landmark[2].y:
                #     break

                # if fingerNum == 20 and landmark.y > handlandmarks.landmark[].y:
                #     # hareket = True
                #     print("Başarılı")

            mpDraw.draw_landmarks(img, handlandmarks, mpHands.HAND_CONNECTIONS)
    cv2.imshow('Camera',img)
    if hareket:
        sesmotoru.say("lütfen ayıpppppp ")
        sesmotoru.runAndWait()
        break
    cv2.waitKey(15) # 1 ile 1mls boyunca yeniden donguye girip framler birlesince dongu olur  cv2.waitKey(0) donuk bi resim gelir biz tusa bakmasmadan yeni bir fream yakalamz 
    if cv2.waitKey(1)& 0xFF == ord('q'):
        break
