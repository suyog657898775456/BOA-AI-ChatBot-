import streamlit as st

# --- 1. PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Best of Amravati | Assistant",
    page_icon="🎬",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# --- 2. INITIALIZE SESSION STATE ---
if "lang" not in st.session_state:
    st.session_state.lang = "English"
if "messages" not in st.session_state:
    st.session_state.messages = []

# --- 3. TRANSLATIONS & DATA ---
STRINGS = {
    "English": {
        "title": "BEST of AMRAVATI",
        "subtitle": " Your City  Your Guide  Your Amravati",
        "welcome": "Welcome to Best Of Amravati! 🎬 How can I help you grow your business?",
        "quick_actions": "Explore Our Business Model",
        "ask_placeholder": "Type your question here...",
        "not_found": "I'm sorry, I didn't quite catch that. You can ask about our pricing, reach, or services!",
        "btn_services": "Our Services",
        "btn_pricing": "Pricing Plans",
        "btn_reach": "Growth & Reach",
        "btn_reels": "Creative Reels",
        "btn_booking": "How to Book?",
        "btn_payment": "Payment Issue",
        "sidebar_label": "SELECT LANGUAGE",
    },
    "मराठी": {
        "title": "BEST of AMRAVATI",
        "subtitle": " तुमचे शहर  तुमचा मार्गदर्शक  तुमचा अमरावती",
        "welcome": "अमरावतीमध्ये आपले स्वागत आहे! 🎬 मी तुम्हाला तुमचा व्यवसाय वाढवण्यास कशी मदत करू शकतो?",
        "quick_actions": "आमचे बिझनेस मॉडेल एक्सप्लोर करा",
        "ask_placeholder": "तुमचा प्रश्न येथे विचारा...",
        "not_found": "क्षमस्व, मला ते समजले नाही. तुम्ही आमच्या किमती, पोहोच किंवा सेवांबद्दल विचारू शकता!",
        "btn_services": "आमच्या सेवा",
        "btn_pricing": "दर पत्रक",
        "btn_reach": "रिच आणि ग्रोथ",
        "btn_reels": "क्रिएटीव्ह रील्स",
        "btn_booking": "बुकिंग कसे करावे?",
        "btn_payment": "पेमेंट समस्या",
        "sidebar_label": "भाषा निवडा",
    }
}

QA_DATA = {
    "service": {
        "English": "We offer a complete ecosystem: Media coverage, Digital News features, Business Magazine spots, Branding, and Strategic Collaborations.",
        "मराठी": "आम्ही एक संपूर्ण इकोसिस्टम ऑफर करतो: मीडिया कव्हरेज, डिजिटल न्यूज वैशिष्ट्ये, बिझनेस मॅगझिन स्पॉट्स, ब्रँडिंग आणि स्ट्रॅटेजिक कोलॅबरेशन."
    },
    "pricing": {
        "English": "Our most popular 'Creative Reel Package' starts at just ₹3,500. This includes scripting, professional shooting, high-end editing, and distribution across our network.",
        "मराठी": "आमचे सर्वात लोकप्रिय 'क्रिएटीव्ह रील पॅकेज' फक्त ₹३,५०० पासून सुरू होते. यामध्ये स्क्रिप्टिंग, प्रोफेशनल शूटिंग, हाय-एंड एडिटिंग आणि आमच्या नेटवर्कवर वितरण समाविष्ट आहे."
    },
    "reach": {
        "English": "We guarantee a minimum local reach. Our campaigns typically achieve 1,00,000+ views among the Amravati audience, ensuring high visibility for your brand.",
        "मराठी": "आम्ही किमान स्थानिक पोहोचची (reach) हमी देतो. आमच्या मोहिमांना सहसा अमरावतीमधील प्रेक्षकांमध्ये १,००,०००+ व्ह्यूज मिळतात, ज्यामुळे तुमच्या ब्रँडची ओळख वाढते."
    },
    "reels": {
        "English": "We specialize in 30-60 second high-impact reels. Our team visits your location, handles the direction, and uses trending hooks to make your business go viral.",
        "मराठी": "आम्ही ३०-६० सेकंदांच्या हाय-इम्पॅक्ट रील्समध्ये तज्ञ आहोत. आमची टीम तुमच्या लोकेशनला भेट देते, डायरेक्शन सांभाळते आणि तुमचा व्यवसाय व्हायरल करण्यासाठी ट्रेंडिंग हुक्स वापरते."
    },
    "book": {
        "English": "Ready to start? You can book by clicking 'Start Now' on our website, messaging us on WhatsApp (+91 89567 27311), or filling out the inquiry form.",
        "मराठी": "सुरू करण्यास तयार आहात? तुम्ही आमच्या वेबसाइटवर 'Start Now' वर क्लिक करून, आम्हाला व्हॉट्सअॅपवर (+91 89567 27311) मेसेज करून किंवा चौकशी फॉर्म भरून बुकिंग करू शकता."
    },
    "payment": {
        "English": "For payment issues or billing inquiries, please email bestofamravati@gmail.com with your transaction details. We resolve all issues within 24 hours.",
        "मराठी": "पेमेंट समस्या किंवा बिलिंग चौकशीसाठी, कृपया तुमच्या व्यवहाराच्या तपशीलांसह bestofamravati@gmail.com वर ईमेल करा. आम्ही २४ तासांच्या आत सर्व समस्यांचे निराकरण करतो."
    }
}

# --- 4. ADVANCED STYLING ---
st.markdown(f"""
    <style>
    .stApp {{ background-color: #0e1117; }}
    [data-testid="stSidebar"] {{ background-color: #161b22 !important; border-right: 1px solid rgba(255, 255, 255, 0.1); }}
    .sidebar-title {{ color: #ffffff !important; font-weight: 800 !important; font-size: 1.2rem; text-transform: uppercase; padding-top: 20px; }}
    .lang-box {{ border-radius: 12px; border: 1px solid rgba(255, 0, 128, 0.4); padding: 15px; background-color: #0d1117; margin-top: 10px; }}
    .chat-header {{ background: linear-gradient(135deg, #FF0080 0%, #2D7FF9 100%); padding: 18px 10px; border-radius: 16px; text-align: center; margin-bottom: 22px; }}
    .header-title {{ font-size: 1.4rem !important; font-weight: 800 !important; color: white !important; }}
    .bubble {{ padding: 12px 18px; border-radius: 20px; margin: 8px 0; max-width: 85%; font-size: 14px; line-height: 1.5; }}
    .assistant-bubble {{ background: rgba(255, 255, 255, 0.95); color: #1a1a1a; align-self: flex-start; border-bottom-left-radius: 4px; }}
    .user-bubble {{ background: linear-gradient(135deg, #FF0080 0%, #2D7FF9 100%); color: white; margin-left: auto; border-bottom-right-radius: 4px; }}
    .wa-float {{ position: fixed; bottom: 100px; right: 25px; background-color: #25d366; border-radius: 50px; z-index: 1000; width: 55px; height: 55px; display: flex; align-items: center; justify-content: center; }}
    </style>
    <a href="https://wa.me/918956727311" class="wa-float" target="_blank">
        <img src="https://upload.wikimedia.org/wikipedia/commons/6/6b/WhatsApp.svg" width="30">
    </a>
""", unsafe_allow_html=True)

# --- 5. SIDEBAR ---
with st.sidebar:
    st.markdown(f'<div class="sidebar-title">{STRINGS[st.session_state.lang]["sidebar_label"]}</div>', unsafe_allow_html=True)
    choice = st.radio("Language", ["English", "मराठी"], index=0 if st.session_state.lang == "English" else 1, label_visibility="collapsed")
    if choice != st.session_state.lang:
        st.session_state.lang = choice
        st.rerun()

# --- 6. LOGIC ---
def process_input(text):
    st.session_state.messages.append({"role": "user", "content": text})
    query = text.lower()
    response = STRINGS[st.session_state.lang]["not_found"]
    
    # Matching keywords for expanded Q&A
    if any(k in query for k in ["service", "सेवा"]):
        response = QA_DATA["service"][st.session_state.lang]
    elif any(k in query for k in ["price", "pricing", "cost", "किती", "दर"]):
        response = QA_DATA["pricing"][st.session_state.lang]
    elif any(k in query for k in ["reach", "views", "growth", "व्ह्यूज"]):
        response = QA_DATA["reach"][st.session_state.lang]
    elif any(k in query for k in ["reel", "video", "शूटिंग"]):
        response = QA_DATA["reels"][st.session_state.lang]
    elif any(k in query for k in ["book", "बुकिंग", "सुरू"]):
        response = QA_DATA["book"][st.session_state.lang]
    elif any(k in query for k in ["payment", "पेमेंट"]):
        response = QA_DATA["payment"][st.session_state.lang]
        
    st.session_state.messages.append({"role": "assistant", "content": response})

# --- 7. UI RENDER ---
lang_set = STRINGS[st.session_state.lang]

st.markdown(f'<div class="chat-header"><div class="header-title">{lang_set["title"]}</div><div style="color:white; font-size:0.8rem;">{lang_set["subtitle"]}</div></div>', unsafe_allow_html=True)

if not st.session_state.messages:
    st.session_state.messages.append({"role": "assistant", "content": lang_set["welcome"]})

for msg in st.session_state.messages:
    div_class = "user-bubble" if msg["role"] == "user" else "assistant-bubble"
    st.markdown(f'<div class="bubble {div_class}">{msg["content"]}</div>', unsafe_allow_html=True)

# Expanded Quick Actions (2 rows for better mobile view)
st.markdown(f"<div style='color: #888; font-size: 0.85rem; font-weight: bold; margin: 20px 0 10px 0;'>{lang_set['quick_actions']}</div>", unsafe_allow_html=True)

row1_c1, row1_c2, row1_c3 = st.columns(3)
with row1_c1:
    if st.button(lang_set["btn_services"], use_container_width=True):
        process_input(lang_set["btn_services"]); st.rerun()
with row1_c2:
    if st.button(lang_set["btn_pricing"], use_container_width=True):
        process_input(lang_set["btn_pricing"]); st.rerun()
with row1_c3:
    if st.button(lang_set["btn_reach"], use_container_width=True):
        process_input(lang_set["btn_reach"]); st.rerun()

row2_c1, row2_c2, row2_c3 = st.columns(3)
with row2_c1:
    if st.button(lang_set["btn_reels"], use_container_width=True):
        process_input(lang_set["btn_reels"]); st.rerun()
with row2_c2:
    if st.button(lang_set["btn_booking"], use_container_width=True):
        process_input(lang_set["btn_booking"]); st.rerun()
with row2_c3:
    if st.button(lang_set["btn_payment"], use_container_width=True):
        process_input(lang_set["btn_payment"]); st.rerun()

if prompt := st.chat_input(lang_set["ask_placeholder"]):
    process_input(prompt)
    st.rerun()