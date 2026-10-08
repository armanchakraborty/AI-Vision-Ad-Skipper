import cv2
import numpy as np
import pyautogui
import time
import random
import ctypes

# Fix 1: Windows DPI Awareness fix to prevent mouse click coordinate offset on scaled displays (125%, 150%, etc.)
try:
    ctypes.windll.shcore.SetProcessDpiAwareness(2)
except Exception:
    pass

print("AI Ad-Skipper Agent initialized and scanning screen...")
print("Press Ctrl+C in terminal to stop.")

# Load the reference template in grayscale mode
skip_template = cv2.imread('skp_btn.png', 0)

if skip_template is None:
    # Fallback to check alternative filename
    skip_template = cv2.imread('skip_btn.png', 0)

if skip_template is None:
    print("ERROR: Reference image ('skp_btn.png' or 'skip_btn.png') not found in project folder!")
else:
    t_h, t_w = skip_template.shape[:2]
    print(f"Loaded reference template successfully. Base size: {t_w}x{t_h}")

try:
    while True:
        if skip_template is not None:
            # 1. Capture full screen
            screenshot = pyautogui.screenshot()
            frame = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
            gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            found = False

            # 2. Multi-scale search loop (handles resolution & zoom differences)
            for scale in np.linspace(0.6, 1.4, 9):
                scaled_w = int(t_w * scale)
                scaled_h = int(t_h * scale)

                # Fix 2: Bounds checking fix on width and height limits against screen dimensions
                if scaled_w <= 0 or scaled_h <= 0 or scaled_w > gray_frame.shape[1] or scaled_h > gray_frame.shape[0]:
                    continue

                resized_template = cv2.resize(skip_template, (scaled_w, scaled_h))

                # Match template
                res = cv2.matchTemplate(gray_frame, resized_template, cv2.TM_CCOEFF_NORMED)
                threshold = 0.65  # Detection threshold
                loc = np.where(res >= threshold)

                for pt in zip(*loc[::-1]):
                    # Calculate center coordinates of detected button
                    click_x = pt[0] + (scaled_w // 2)
                    click_y = pt[1] + (scaled_h // 2)

                    print(f"\n[{time.strftime('%H:%M:%S')}] Skip Button Detected (Scale {scale:.1f}x) at X:{click_x} Y:{click_y}")

                    # Humanized mouse movement sequence (prevents bot detection)
                    pyautogui.moveTo(click_x, click_y, duration=random.uniform(0.3, 0.5), tween=pyautogui.easeOutQuad)
                    time.sleep(random.uniform(0.15, 0.3))
                    pyautogui.click()

                    found = True
                    time.sleep(3.5)  # Pause to avoid repeated clicks
                    break

                if found:
                    break

            if not found:
                print(".", end="", flush=True)

        time.sleep(1.0)

except KeyboardInterrupt:
    print("\nAI Agent stopped safely.")