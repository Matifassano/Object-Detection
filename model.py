import cv2
from ultralytics import YOLO
from yt_dlp import YoutubeDL

def download_yt_video(url, output_path="downloaded_video.mp4"):
    try:
        ydl_opts = {
            'format': 'best',
            'outtmpl': output_path,
        }
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print(f"Video download: {output_path}")
        return output_path
    except Exception as e:
        print(f"An error occurred while downloading the video: {e}")
        return None

# Process video with YOLOv11
def process_video(video_path):

    model = YOLO(r".\yolo11n.pt")
    video_capture = cv2.VideoCapture(video_path)
    
    if not video_capture.isOpened():
        print("An error occurred while open the video.")
        return

    while video_capture.isOpened():
        ret, frame = video_capture.read()
        if not ret:
            break

        results = model(frame)  # Objects detection from video frame

        # Show detections
        for result in results:
            boxes = result.boxes.xyxy.cpu().numpy()
            confidences = result.boxes.conf.cpu().numpy()  # Percentages
            class_ids = result.boxes.cls.cpu().numpy().astype(int)

            for box, confidence, class_id in zip(boxes, confidences, class_ids):
                x1, y1, x2, y2 = map(int, box)
                label = f"{model.names[class_id]} {confidence:.2f}"
                color = (255, 0, 0)
                cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
                cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

        cv2.imshow("Autonomous car detections simulator", frame)

        # Quit with 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video_capture.release()
    cv2.destroyAllWindows()