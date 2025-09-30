import cv2
import mss
import numpy as np
import time
import threading
import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class ScreenRecorder:
    def __init__(self, output_file="test_flow.mp4", monitor_index=1, fps=20):
        self.output_file = output_file
        self.monitor_index = monitor_index
        self.fps = fps
        self.recording = False
        self.thread = None

    def _record(self):
        with mss.mss() as sct:
            monitor = sct.monitors[self.monitor_index]
            width, height = monitor["width"], monitor["height"]
            fourcc = cv2.VideoWriter_fourcc(*"mp4v")
            out = cv2.VideoWriter(self.output_file, fourcc, self.fps, (width, height))

            while self.recording:
                img = np.array(sct.grab(monitor))
                frame = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)
                out.write(frame)
                time.sleep(1 / self.fps)

            out.release()

    def start(self):
        self.recording = True
        self.thread = threading.Thread(target=self._record, daemon=True)
        self.thread.start()

    def stop(self):
        self.recording = False
        if self.thread:
            self.thread.join()


def start_browser_with_network_logging():
    options = Options()
    options.set_capability("goog:loggingPrefs", {"performance": "ALL"})
    driver = webdriver.Chrome(options=options)
    return driver


def get_network_logs(driver, output_file="network_logs.json"):
    logs_raw = driver.get_log("performance")
    events = []

    for entry in logs_raw:
        message = json.loads(entry["message"])
        msg = message["message"]
        if msg["method"].startswith("Network."):
            events.append(msg)

    with open(output_file, "w") as f:
        json.dump(events, f, indent=2)

    print(f"Network logs saved to {output_file}")
    return events


def run_test_flow():
    # 1. Start browser
    driver = start_browser_with_network_logging()

    # 2. Start recording
    recorder = ScreenRecorder("test_flow.mp4", monitor_index=1, fps=15)
    recorder.start()
    print("Screen recording started...")

    try:
        # 3. Do test actions
        driver.get("https://parabank.parasoft.com/parabank/index.htm")
        time.sleep(20)

    finally:
        # 4. Collect logs + stop browser
        logs = get_network_logs(driver, "network_logs.json")
        driver.quit()

        # 5. Stop recording
        recorder.stop()
        print("Screen recording stopped.")

        print("Test flow completed: video + logs captured")
        return "test_flow.mp4", "network_logs.json"
