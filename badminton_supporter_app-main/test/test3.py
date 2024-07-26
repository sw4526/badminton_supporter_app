import cv2
import time
from collections import deque
from tkinter import Tk, messagebox
from datetime import datetime
import flask
from flask import request
from flask import Response
from flask import stream_with_context

frame_rate = 30
slow_motion_factor = 0.5
buffer_seconds = 10

buffer_size = frame_rate * buffer_seconds
frame_buffer = deque(maxlen=buffer_size)

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("웹캠을 열 수 없습니다.")
    exit()

out = None
file_counter = 0

def ask_to_save():
    root = Tk()
    root.withdraw()
    result = messagebox.askyesno("저장", "이 영상을 저장하겠습니까?")
    root.destroy()
    return result

def get_filename(counter):
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    return f'slow_motion_video_{timestamp}_{counter}.avi'

while True:
    ret, frame = cap.read()
    if not ret:
        print("프레임을 읽을 수 없습니다.")
        break

    frame_buffer.append(frame)
    cv2.imshow('Webcam', frame)

    key = cv2.waitKey(1) & 0xFF

    if key == ord('r'):
        print("슬로우모션 재생 시작...")
        for f in list(frame_buffer):
            cv2.putText(f, 'replay', (f.shape[1] - 100, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
            cv2.imshow('Webcam', f)
            if out is not None:
                out.write(f)
            if cv2.waitKey(int(1000 / (frame_rate * slow_motion_factor))) & 0xFF == ord('q'):
                break

        print("슬로우모션 재생이 완료되었습니다.")
        # 슬로우모션 재생이 완료된 후 저장 여부 묻기
        if ask_to_save():
            file_counter += 1
            output_file = get_filename(file_counter)
            if out is not None:
                out.release()
            fourcc = cv2.VideoWriter_fourcc(*'XVID')
            out = cv2.VideoWriter(output_file, fourcc, frame_rate * slow_motion_factor, (int(cap.get(3)), int(cap.get(4))))
            print("비디오 저장 중...")
            for f in list(frame_buffer):
                out.write(f)
            print(f"비디오 저장 완료: {output_file}")
        else:
            print("비디오 저장 취소.")

    if key == ord('s'):
        # 's' 키를 눌렀을 때 저장 여부 묻기
        print("슬로우모션 재생 중 저장 여부를 묻습니다.")
        if ask_to_save():
            file_counter += 1
            output_file = get_filename(file_counter)
            if out is not None:
                out.release()
            fourcc = cv2.VideoWriter_fourcc(*'XVID')
            out = cv2.VideoWriter(output_file, fourcc, frame_rate * slow_motion_factor, (int(cap.get(3)), int(cap.get(4))))
            print("비디오 저장 중...")
            for f in list(frame_buffer):
                out.write(f)
            print(f"비디오 저장 완료: {output_file}")
        else:
            print("비디오 저장 취소.")

    if key == ord('q'):
        break

cap.release()
if out is not None:
    out.release()
cv2.destroyAllWindows()

if __name__ == '__main__' :
    
    print('------------------------------------------------')
    print('Wandlab CV - version ' + version )
    print('------------------------------------------------')
    
    app.run(host='0.0.0.0', port=5000 )