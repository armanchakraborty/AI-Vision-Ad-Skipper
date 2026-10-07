# AI Vision Ad-Skipper 🤖👁️

**Built for the MLH Hacktoberfest Hack Day Noida (Delhi NCR) x NIAT-NIU**  
**Category:** Best Open-Source AI Project

## 📌 Overview
AI Vision Ad-Skipper is a system-wide AI computer vision agent powered by open-source vision tools (YOLOv8 & OpenCV) and PyAutoGUI. 

Instead of relying on static browser extensions or rigid web DOM selectors that video platforms frequently block or break, our agent visually scans desktop media streams in real-time. It dynamically detects interactive UI ad-skip elements across different display scales and executes humanized mouse interactions to keep focus and workflow uninterrupted.

## ✨ Key Features
* **Pure Visual Recognition:** Operates entirely on pixel data using OpenCV multi-scale template matching, bypassing browser-level extension blockers completely.
* **Multi-Scale Detection:** Automatically interpolates the reference UI element across 9 different scale factors (60% to 140%) to work seamlessly on standard screens, zoomed browsers, and high-DPI Windows displays.
* **Anti-Bot Telemetry Bypass:** Implements randomized Bezier-curve mouse movements (`easeOutQuad`) and variable micro-delays to simulate human hover states, preventing platform rate-limiting algorithms from flagging the session.
* **Standalone Executable:** Packaged into a single, double-clickable `.exe` file so non-technical users can run the AI agent without installing Python or dependencies.

## 🚀 How to Use (For Regular Users)
1. Download the latest `AI-Ad-Skipper.exe` and the `skp_btn.png` reference image from the **Releases** tab on this repository.
2. Place both files in the same folder on your Windows PC.
3. Double-click `AI-Ad-Skipper.exe` to start the agent. 
4. A terminal window will open showing the scanning logs. To stop the agent, simply close the window!

## 💻 How to Run & Contribute (For Developers)

### Prerequisites
* Python 3.x installed
* Git

### Installation
1. Clone the repository:
   ```bash
   git clone [https://github.com/armanchakraborty/AI-Vision-Ad-Skipper.git](https://github.com/armanchakraborty/AI-Vision-Ad-Skipper.git)
