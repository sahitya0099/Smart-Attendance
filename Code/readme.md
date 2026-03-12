Face Recognition Attendance System

A Smart Attendance System that uses Face Recognition with OpenCV and Python to automatically mark attendance. The system captures facial images, trains a recognition model, and records attendance in real time using a webcam.

This project helps automate traditional attendance systems by using computer vision and machine learning techniques to identify individuals and store their attendance records efficiently. 


Features:-

Capture face images of students using webcam
Train a face recognition model using LBPH algorithm
Detect and recognize faces in real-time
Automatically mark attendance with date and time
Store attendance data in CSV files
Send attendance reports via email automatically
Simple command-line menu interface

Technologies Used:-

Python
OpenCV
NumPy
Pandas
Yagmail (for sending emails)
Haar Cascade Classifier

The project uses a Haar Cascade model to detect faces and the LBPH Face Recognizer to train and recognize individuals from stored images. 


Project Workflow

1.Check Camera
Verify webcam functionality before capturing images.

2.Capture Faces
Capture multiple images of each user and store them in the dataset. 

3.Train Images
Train the face recognition model using the collected images.

4.Recognize Faces & Mark Attendance
Detect faces through webcam and automatically record attendance in CSV format.

5.Send Attendance Report
Email the generated attendance file automatically.

The system is controlled through a simple menu-based interface that allows users to perform all operations easily. 

Output

Real-time face detection

Attendance stored as: Attendance/Attendance_YYYY-MM-DD_HH-MM-SS.csv

Attendance records contain:- ID,Name,Date,Time


Use Cases:-

College attendance systems
School attendance monitoring
Office employee attendance
Contactless attendance tracking

Future Improvements:-

GUI interface using Tkinter or Streamlit
Cloud database integration
Deep learning models for better accuracy
Mobile application integration
