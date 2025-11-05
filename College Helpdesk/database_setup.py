# database_setup.py

import sqlite3

conn = sqlite3.connect('chatbot.db')
c = conn.cursor()

# Table for FAQs
c.execute('''CREATE TABLE IF NOT EXISTS faqs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                question TEXT,
                answer TEXT
            )''')

# Table for Chat History
c.execute('''CREATE TABLE IF NOT EXISTS chat_history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_msg TEXT,
                bot_reply TEXT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            )''')

# Insert some FAQs
faqs = [
    ("college timing", "Our college timing is from 9:00 AM to 4:00 PM, Monday to Friday."),
    ("library timing", "The library is open from 8:30 AM to 5:30 PM on working days."),
    ("courses offered", "We offer courses in Computer Science, Electronics, Mechanical, Civil, and IT."),
    ("hostel facility", "Yes, hostels are available for both boys and girls with mess facilities."),
    ("placement companies", "Our top recruiters include TCS, Infosys, Wipro, and Tech Mahindra."),
    ("contact details", "You can reach us at helpdesk@college.edu or call 98765-43210."),
    ("admission process", "Admissions are based on entrance exam scores followed by counseling."),
    ("scholarship", "Scholarships are available for meritorious and economically weaker students."),
    ("attendance rules", "A minimum of 75% attendance is required to appear for final exams."),
    ("exam schedule", "Exams are conducted at the end of each semester as per the academic calendar."),
    ("principal name", "Our Principal is Dr. S.D. Chede"),
    ("events", "The college hosts annual fests, tech competitions, and cultural events every year."),
    ("canteen timing", "The canteen is open from 8:00 AM to 6:00 PM."),
    ("transport facility", "Yes, college buses are available from various city routes."),
    ("fees structure", "Fee details vary by course. You can check the official website for updates."),
    ("wifi facility", "Wi-Fi is available across the campus for students and staff."),
    ("computer lab", "Computer labs are equipped with high-speed internet and modern systems."),
    ("sports facility", "Yes, the college provides facilities for football, cricket, badminton, and indoor games."),
    ("library membership", "Students can apply for library membership through the library counter."),
    ("faculty details", "Our faculty members are highly qualified and experienced in their respective fields."),
    ("results", "Semester results are published on the college website under the Examination section."),
    ("college location", "The college is located at ABC Road, XYZ City, near the central bus station."),
    ("anti ragging", "Our college has a strict anti-ragging policy to ensure student safety."),
    ("alumni network", "We have an active alumni association that helps with placements and mentorship."),
    ("grievance cell", "Students can submit complaints or feedback through the Grievance Cell portal.")
]

# Add data only if table is empty
c.execute("SELECT COUNT(*) FROM faqs")
if c.fetchone()[0] == 0:
    c.executemany("INSERT INTO faqs (question, answer) VALUES (?, ?)", faqs)
    conn.commit()

print("✅ Database setup completed.")
conn.close()
