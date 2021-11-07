from dataclasses import dataclass
from typing import Optional


@dataclass
class Configuration:
    chrome_browser_language: Optional[str] = "--lang=en-US"
    chrome_window_size: Optional[str] = "--window-size=1920,1080"
    chrome_enable_logging: Optional[str] = "--enable-logging"
    headless_mode: Optional[bool] = False
