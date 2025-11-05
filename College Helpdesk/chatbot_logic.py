# chatbot_logic.py

import re
import sqlite3

def search_faq_db(user_input):
    conn = sqlite3.connect('chatbot.db')
    c = conn.cursor()
    c.execute("SELECT answer FROM faqs")
    faqs = c.fetchall()
    conn.close()

    user_input = user_input.lower()

    for faq in faqs:
        if any(word in user_input for word in faq[0].lower().split()):
            return faq[0]
    return None


def get_response(user_input):
    user_input = user_input.lower().strip()

    # 1️⃣ Search in database
    conn = sqlite3.connect('chatbot.db')
    c = conn.cursor()
    c.execute("SELECT answer FROM faqs WHERE LOWER(question) LIKE ?", ('%' + user_input + '%',))
    res = c.fetchone()
    conn.close()

    if res:
        return res[0]

    # 2️⃣ Else use rule-based logic
    if re.search(r'\b(hi|hello|hey)\b', user_input):
        return "Hello! 👋 I'm your college helpdesk bot. How can I assist you?"

    elif "admission" in user_input or "apply" in user_input:
        return "You can apply for admission online through our official college website."

    elif "exam" in user_input or "test" in user_input:
        return "Semester exams are conducted twice a year — December and May."

    elif "faculty" in user_input:
        return "You can check faculty details on the college website."
    
    elif "hostel" in user_input:
        return "Yes, hostels are available for both boys and girls with mess facilities."
    
    elif "placement" in user_input or "companies" in user_input:
        return "Our top recruiters include TCS, Infosys, Wipro, and Tech Mahindra."

    elif "contact" in user_input or "phone" in user_input or "email" in user_input:
        return "You can reach us at helpdesk@college.edu or call 98765-43210."

    elif "scholarship" in user_input:
        return "Yes, scholarships are available for meritorious and economically weaker students."

    elif "attendance" in user_input:
        return "A minimum of 75% attendance is required to appear for final exams."

    elif "events" in user_input or "fest" in user_input:
        return "The college hosts annual cultural and technical fests every year."

    elif "canteen" in user_input:
        return "The canteen is open from 8:00 AM to 6:00 PM and offers a variety of meals and snacks."
    
    elif "bus" in user_input or "transport" in user_input:
        return "Yes, college buses are available from various routes across the city."

    elif "fees" in user_input or "fee" in user_input:
        return "Fee details vary by course. Please visit the official college website for more information."

    elif "sports" in user_input:
        return "Yes, we have facilities for football, cricket, badminton, and indoor games."

    elif "wifi" in user_input:
        return "Wi-Fi is available throughout the campus for students and staff."

    elif "result" in user_input or "marks" in user_input:
        return "Semester results are published on the college website under the Examination section."

    elif "principal" in user_input:
        return "Our Principal is Dr. S. D. Chede"

    else:
        return "Sorry, I couldn't find that info."
