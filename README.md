# Smart Meat Monitoring System During Transportation

This system provides real-time environmental monitoring for meat in transit using an ESP32 and multiple sensors. 
Designed for refrigerated trucks, it collects data on temperature, humidity, light exposure, and motion. 
The captured data is sent wirelessly to a backend server and displayed on a secure web interface while also being
stored in a MySQL database for tracking and analysis.

---

# Technologies Used
- **Microcontroller**: ESP32 WeMos D1 R32
- **Sensors**: DS18B20 (External Temp), DHT22 (Humidity & Temp), LDR (Light), IR Sensor (Presence Detection)
- **Programming Languages**: C++ for Arduino, Python with Flask framework
- **Database**: MySQL
- **Frontend Technologies**: HTML, CSS, JavaScript using JSON format
- **Development Tools**: Arduino IDE, Wokwi for simulation

---

## System Features
- Continuous capture and monitoring of sensor data
- Wireless communication via ESP32 (Wi-Fi capable)
- User-friendly dashboard with login functionality
- Data stored with timestamps for tracking and reporting
- Administrative view with dynamic tables and live graphs
- Detects changes in environment including motion and lighting
- Basic hardware setup using breadboard and clear wiring layout

---

## Project Architecture
- Sensors feed data to the ESP32 microcontroller
- ESP32 sends data via Wi-Fi to the Flask server
- Server processes and inserts data into MySQL database
- Web app fetches and displays this information live to users

---

## 📸 Example Pages
- `login.html`: User and admin login interface
- `dashboard.html`: Live updates on temperature, humidity, and other conditions
- `admin.html`: Advanced panel with graphs and control features
- `graph.html`: Historical sensor data visualization

---

## Limitations
- Lacks mobile application and off-site cloud backup
- Motion detection is basic (no real-time alerting)
- No built-in power redundancy (relies on vehicle power)
- Sensors used are affordable and limited in precision

---

## Future Enhancements
- Integrate text or email alert notifications
- Replace with higher accuracy sensor hardware
- Add mobile access or sync with cloud services like Firebase
- Include solar/battery-based backup power
- Expand dashboard for route tracking and refrigeration control

---

## Skills & Experience Gained
This project allowed me to practice embedded system design, real-time communication, full-stack web development, and sensor integration. It strengthened my problem-solving ability, especially in building, testing, and troubleshooting an IoT solution from the ground up.

---

## Deployment Guide
1. Flash the Arduino `.ino` code to your ESP32 board using Arduino IDE
2. Set up the MySQL database using the SQL schema provided
3. Run the Flask app (`app.py`) on your server or local machine
4. Access the dashboard by opening your browser to `http://localhost:5000`

---

**Author**: Sibundeni Sandile Ernest  
**Project Classification**: Final Year Project – Engineering Programming 3 (EIENP3A)  
**Institution**: Vaal University of Technology  
**Team Members**: Mazibuko T., Nkgodi N.N., Malatji M.P., Mpata M.C  
**Supervisor**: Mr. Dipo Ojo Seriki
