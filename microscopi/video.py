import cv2


class VideoSource:
    def __init__(self, device: int, width: int, height: int):
        self.device = device
        self.width = width
        self.height = height

        self.cap = cv2.VideoCapture(device, cv2.CAP_V4L2)
        if not self.cap.isOpened():
            raise RuntimeError(f"Cannot open video device {device}")

        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

    def read(self):
        ret, frame = self.cap.read()
        if not ret or frame is None:
            raise RuntimeError("Cannot read from video device")
        return frame

    def release(self):
        if self.cap:
            self.cap.release()
