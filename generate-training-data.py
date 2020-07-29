import os
import cv2
cap = cv2.VideoCapture(0)
path = 'path_to_save_images'
start = False
count = 0
while True:
    ret, frame = cap.read()
    if not ret:
        continue
    if count == 300:
        break

    cv2.rectangle(frame, (100, 100), (508, 580), (0, 0, 255), 2)

    if start:
        roi = frame[100:500, 100:500]
        save_path = os.path.join(path, '{}.jpg'.format(count + 1))
        cv2.imwrite(save_path, roi)
        count += 1
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame, "Collecting {}".format(count),
            (5, 50), font, 0.7, (0, 0, 255), 2, cv2.LINE_AA)
    cv2.imshow("Collecting images", frame)
    k = cv2.waitKey(10)
    if k == ord('a'):
        start = not start
    if k == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
image = input('image')
