import logging
from typing import List

from pydantic import BaseModel
from torch import nn

from pynanny.settings import Settings
from pynanny.video import VideoManager

settings = Settings()

logger = logging.getLogger(__name__)
logger.setLevel(logging.getLevelName(settings.log_level))


class Nanny(BaseModel):
    streams: List[VideoManager]
    model: nn.Module
    monitor_label: str = "person"

    def shutdown(self) -> None:
        for stream in self.streams:
            stream.stop()

    def start(self) -> None:
        for stream in self.streams:
            stream.start()

    def step(self):
        # TODO
        pass

    def run(self) -> None:
        self.start()
        while True:
            try:
                self.step()
            except KeyboardInterrupt:
                logger.warning("Keyboard interrupt received. Shutting down nicely")
                break

        self.shutdown()
