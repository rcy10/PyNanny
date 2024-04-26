import logging
from queue import Empty, Full, Queue
from threading import Event, Thread

import numpy as np
from cv2 import VideoCapture
from pydantic import BaseModel

from pynanny.settings import Settings

settings = Settings()

logger = logging.getLogger(__name__)
logger.setLevel(logging.getLevelName(settings.log_level))


class VideoManager(BaseModel):
    url: str

    _cap: VideoCapture | None = None
    _thread: Thread | None = None
    _queue: Queue | None = None
    _event: Event | None = None

    @property
    def queue(self) -> Queue:
        if self._queue is None:
            self._queue = Queue(5)
        return self._queue

    @property
    def event(self) -> Event:
        if self._event is None:
            self._event = Event()
        return self._event

    @property
    def thread(self) -> Thread:
        if self._thread is None:
            self._thread = Thread(target=self.run, args=(self.queue, self.event))
        return self._thread

    @property
    def cap(self) -> VideoCapture:
        if self._cap is None:
            logger.info(f"{self.__module__}: Connecting to {self.url}")
            self._cap = VideoCapture(self.url)
        return self._cap

    def start(self) -> None:
        self.thread.start()

    def stop(self) -> None:
        self.release()
        self.event.set()
        self.thread.join()

    def release(self) -> None:
        if self._cap is not None and self._cap.isOpened():
            logger.info(f"{self.__module__}: Releasing connection to {self.url}")
            self._cap.release()
        self._cap = None

    def _read_frame(self) -> np.ndarray:
        status, frame = self.cap.read()
        if not status:
            logger.error(
                f"{self.__module__}: Unable to read frame from {self.url}. Releasing connection."
            )
            self.release()
            return None
        return frame

    def read(self) -> np.ndarray:
        return self._read_frame()

    def run(self, queue: Queue, stop_event: Event) -> None:
        while not stop_event.is_set():
            frame = self.read()
            if frame is None:
                continue
            try:
                self.queue.put_nowait(frame)
            except Full:
                continue

    def get_image(self) -> np.ndarray | None:
        try:
            frame = self.queue.get_nowait()
        except Empty:
            frame = None

        return frame
