# Smart Meat Monitoring System While in Transit

This project is a real-time IoT-based monitoring system developed to ensure safe and efficient meat transportation. It uses an ESP32 microcontroller connected to multiple sensors to track temperature, humidity, motion, and light conditions inside a delivery truck. Data is transmitted via Wi-Fi to a Flask server, stored in a MySQL database, and accessed through a secure web dashboard for both real-time and historical analysis.

---

## Technologies Used
- **Microcontroller**: ESP32 WeMos D1 R32  
- **Sensors**: DS18B20 (External Temp), DHT22 (Internal Temp & Humidity), Infrared Sensor (Motion), LDR (Light)  
- **Programming Languages**: C++ (Arduino), Python (Flask)  
- **Database**: MySQL  
- **Frontend**: HTML, CSS, JavaScript (JSON)  
- **Tools**: Arduino IDE, Wokwi Simulator, Visual Studio Code  

---

## System Features
- Live monitoring of environmental conditions inside meat transport vehicles  
- Wireless data transfer using ESP32 with Wi-Fi  
- Secure login system with different views for users and admins  
- Real-time display and graph-based data visualization  
- Timestamped logging of sensor readings in a structured database  
- Organized HTML pages for each sensor and system function  
- Simple hardware wiring and test-friendly enclosure design  

---

## Project Architecture
- Sensors collect environmental data and send it to the ESP32  
- ESP32 transmits data over Wi-Fi to the Flask server  
- Flask processes data and stores it in MySQL  
- HTML pages render data dynamically for the end-user in a web browser  

---

## 📸 Web Pages
- `index.html`: Welcome page  
- `login.html`: Login form  
- `signup.html`: New user registration  
- `admin.html`: Admin-only dashboard with graphs  
- `display.html`: All current sensor values in one place  
- `temperature.html`: Internal temperature  
- `temperature_out.html`: External temperature  
- `humidity.html`: Humidity monitoring  

**Backend File**: `TH.py` – handles routing, database connection, sessions

---

## Limitations

Although this system performs well under standard conditions, there are certain limitations that should be considered. The monitoring relies on continuous Wi-Fi connectivity; in remote or signal-poor areas, data transmission may be interrupted. Since the system uses basic, low-cost sensors, the readings—while reliable for prototyping—may not meet strict industry calibration standards. Additionally, there is currently no battery backup, meaning that power outages or vehicle shutdowns will interrupt data collection. Lastly, the system does not yet support real-time alerts via SMS or mobile notifications, which limits proactive responses to emergencies.

---

## Future Improvements
- Add GSM module for SMS alerts when thresholds are exceeded in remote areas  
- Integrate GPS to track location alongside sensor data  
- Develop a mobile app for remote live monitoring  
- Include battery or solar backup to support the system during power failure  
- Upgrade sensors to high-precision, food-industry standards  

---

## What I Learned

This project helped me gain real-world experience in embedded system development, Internet of Things (IoT) integration, server-side programming with Flask, and user interface design. It deepened my understanding of how to design, connect, and troubleshoot full-stack systems for data monitoring, while emphasizing the importance of data accuracy, usability, and real-time feedback.

---

## How to Run the System

1. Flash the Arduino code (.ino) to the ESP32 board using Arduino IDE  
2. Start your MySQL server and create the `trailor_system` database  
3. Run the Flask backend by executing `python TH.py`  
4. Open your browser and navigate to `http://localhost:5000`  

---

**Author**: Sibundeni Sandile Ernest  
**Project Type**: Final Year Practical Project – Engineering Programming 3 (EIENP3A)  
**Institution**: Vaal University of Technology  
**Team Members**: Mazibuko T., Nkgodi N.N., Malatji M.P., Mpata M.C  
**Supervisor**: Mr. Dipo Ojo Seriki
