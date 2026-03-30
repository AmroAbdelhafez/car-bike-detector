# 🚗 Car & Bike Object Detection Web App

A lightweight, Dockerized web application that uses a custom-trained YOLO model (exported to ONNX) to automatically detect and draw bounding boxes around cars and bikes in user-uploaded images. 

**🔴 Live Demo:** [https://car-bike-detector.onrender.com/](https://car-bike-detector.onrender.com/)

---

## 🛠️ Tech Stack
* **Frontend:** HTML5, CSS3 (Jinja2 Templates)
* **Backend:** Python, Flask, Gunicorn
* **Machine Learning:** Ultralytics YOLO, ONNX Runtime, OpenCV (Headless)
* **Deployment & DevOps:** Docker, Render

---

## 🚀 Features
1. **Simple Web Interface:** Easy-to-use UI for uploading images.
2. **Fast Inference:** Utilizes the ONNX runtime for optimized, CPU-friendly object detection.
3. **Containerized:** Fully packaged with Docker for guaranteed reproducibility across any environment.
4. **Cloud Deployed:** Hosted live on Render with automated continuous deployment via GitHub.

---

## 💻 How to Run Locally

If you want to run this project on your own machine, you can easily do so using Docker.

### Prerequisites
* [Docker Desktop](https://www.docker.com/products/docker-desktop/) installed and running.

### Installation Steps

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/YOUR_USERNAME/car-bike-detector.git](https://github.com/YOUR_USERNAME/car-bike-detector.git)
   cd car-bike-detector
