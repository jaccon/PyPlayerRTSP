import cv2
import imutils.video as vid
import json
import os
import time

os.environ["OPENCV_FFMPEG_CAPTURE_OPTIONS"] = "rtsp_transport;0"

def open_rtsp_player(rtsp_url, legend_text, instructions_text):
    stream = vid.VideoStream(rtsp_url).start()

    window_name = f"PyPlayerRTSP: {rtsp_url}"

    cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
    is_fullscreen = False

    capture_message = ""
    capture_start_time = 0

    while True:
        frame = stream.read()

        if frame is None:
            print(f"Error: Failed to read frame from {rtsp_url}.")
            break

        # Adiciona legenda no canto inferior direito
        legend = f"{legend_text} | Type: C to Capture | Q to Quit | F to Toggle Fullscreen"
        legend_size = cv2.getTextSize(legend, cv2.FONT_HERSHEY_SIMPLEX, 1, 2)[0]
        frame[frame.shape[0] - legend_size[1] - 10:frame.shape[0] - 10,
              frame.shape[1] - legend_size[0] - 10:frame.shape[1] - 10] = (0, 0, 0)
        cv2.putText(frame, legend, (frame.shape[1] - legend_size[0] - 5, frame.shape[0] - 5),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)

        # Adiciona instruções na parte inferior esquerda
        instructions_size = cv2.getTextSize(instructions_text, cv2.FONT_HERSHEY_SIMPLEX, 0.8, 1)[0]
        frame[frame.shape[0] - instructions_size[1] - 10:frame.shape[0] - 10,
              10:instructions_size[0] + 10] = (0, 0, 0)
        cv2.putText(frame, instructions_text, (10, frame.shape[0] - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 1, cv2.LINE_AA)

        # Exibir mensagem "Captured" com fade apenas por 5 segundos
        if capture_message and time.time() - capture_start_time < 5:
            alpha = max(0, 1 - (time.time() - capture_start_time) / 2)  # Tempo de fade: 2 segundos
            frame = cv2.addWeighted(frame, alpha, create_text_overlay(frame, capture_message), 1 - alpha, 0)

        cv2.imshow(window_name, frame)

        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break
        elif key == ord('c'):
            save_screenshot(frame, rtsp_url)
            capture_message = "Captured"
            capture_start_time = time.time()
        elif key == ord('f'):
            if is_fullscreen:
                cv2.setWindowProperty(window_name, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_NORMAL)
            else:
                cv2.setWindowProperty(window_name, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
            is_fullscreen = not is_fullscreen

    stream.stop()
    cv2.destroyAllWindows()

def save_screenshot(frame, rtsp_url):
    if not os.path.exists("captures"):
        os.makedirs("captures")

    timestamp = cv2.getTickCount()
    filename = f"captures/screenshot_{timestamp}.png"
    cv2.imwrite(filename, frame)
    print(f"Screenshot saved: {filename}")

def create_text_overlay(frame, text):
    overlay = frame.copy()
    cv2.putText(overlay, text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
    return overlay

if __name__ == "__main__":
    with open('config.json', 'r') as file:
        config = json.load(file)

    for camera_config in config['cameras']:
        camera_url = camera_config['url']
        legend_text = camera_config.get('legend', 'xxx')  # Texto da legenda, vazio se não especificado
        instructions_text = 'PyPlayerRTSP'  # Texto de instruções, vazio se não especificado
        open_rtsp_player(camera_url, legend_text, instructions_text)
