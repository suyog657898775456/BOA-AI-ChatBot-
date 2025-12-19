import streamlit as st

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="Best of Amravati Assistant",
    page_icon="🎬",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# --- SESSION STATE ---
if "lang" not in st.session_state:
    st.session_state.lang = "English"
if "messages" not in st.session_state:
    st.session_state.messages = []

# --- TRANSLATIONS & QA DATA ---
STRINGS = {
    "English": {
        "title": "BEST of AMRAVATI",
        "subtitle": "● Your City ● Your Guide ● Your Amravati",
        "welcome": "Welcome to Best Of Amravati! 🎬 How can I help you?",
        "quick_actions": "Quick Actions",
        "ask_placeholder": "Type your message...",
        "not_found": "I'm sorry, I didn't quite catch that.",
        "btn_services": "Our Services",
        "btn_booking": "How to Book?",
        "btn_payment": "Payment Issue",
        "sidebar_label": "SELECT LANGUAGE",
    },
    "मराठी": {
        "title": "BEST of AMRAVATI",
        "subtitle": "● तुमचे शहर ● तुमचा मार्गदर्शक ● तुमचा अमरावती",
        "welcome": "अमरावतीमध्ये आपले स्वागत आहे! 🎬 मी तुम्हाला कशी मदत करू शकतो?",
        "quick_actions": "त्वरीत कृती",
        "ask_placeholder": "तुमचा संदेश टाइप करा...",
        "not_found": "क्षमस्व, मला ते समजले नाही.",
        "btn_services": "आमच्या सेवा",
        "btn_booking": "बुकिंग कसे करावे?",
        "btn_payment": "पेमेंट समस्या",
        "sidebar_label": "भाषा निवडा",
    }
}

QA_DATA = {
    "service": {
        "English": "We provide Media, Digital News, Business Magazine, Branding, and Collaboration services.",
        "मराठी": "आम्ही मीडिया, डिजिटल न्यूज, बिझनेस मॅगझिन, ब्रँडिंग आणि कोलॅबरेशन सेवा प्रदान करतो."
    },
    "book": {
        "English": "To book a service, please visit our 'Contact' page or click the WhatsApp icon.",
        "मराठी": "सेवा बुक करण्यासाठी, कृपया आमच्या 'संपर्क' पृष्ठास भेट द्या किंवा व्हॉट्सअॅप चिन्हावर क्लिक करा."
    },
    "payment": {
        "English": "If you are facing payment issues, please share your transaction ID with us.",
        "मराठी": "तुम्हाला पेमेंट समस्या येत असल्यास, कृपया तुमचा व्यवहार आयडी आमच्याशी शेअर करा."
    }
}

# --- STYLING ---
st.markdown(f"""
    <style>
    /* Dark Theme Background */
    .stApp {{
        background-color: #0e1117;
    }}

    /* Main Header Gradient */
    .chat-header {{
        background: linear-gradient(135deg, #FF0080 0%, #7928CA 50%, #2D7FF9 100%);
        padding: 40px 20px;
        border-radius: 20px;
        color: white;
        text-align: center;
        margin-bottom: 25px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.3);
    }}

    /* Professional Bubble Styling */
    .bubble {{
        padding: 12px 18px;
        border-radius: 20px;
        margin: 8px 0;
        max-width: 80%;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        line-height: 1.5;
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    }}
    .assistant-bubble {{
        background-color: #ffffff;
        color: #1a1a1a;
        align-self: flex-start;
        border-bottom-left-radius: 4px;
    }}
    .user-bubble {{
        background: linear-gradient(135deg, #FF0080 0%, #2D7FF9 100%);
        color: white;
        margin-left: auto;
        border-bottom-right-radius: 4px;
        text-align: right;
    }}

    /* Button Styling */
    .stButton > button {{
        background-color: #1e2129 !important;
        color: white !important;
        border: 1px solid #3d414b !important;
        border-radius: 12px !important;
        transition: 0.3s;
    }}
    .stButton > button:hover {{
        border-color: #FF0080 !important;
        color: #FF0080 !important;
    }}

    /* Sidebar Label */
    [data-testid="stSidebar"] label {{
        color: #000000 !important;
        font-weight: bold;
    }}
    </style>
""", unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    st.markdown(f"### {STRINGS[st.session_state.lang]['sidebar_label']}")
    choice = st.radio("Select", ["English", "मराठी"], label_visibility="collapsed")
    if choice != st.session_state.lang:
        st.session_state.lang = choice
        st.rerun()

# --- CHAT LOGIC ---
def process_input(text):
    st.session_state.messages.append({"role": "user", "content": text})
    query = text.lower()
    
    response = STRINGS[st.session_state.lang]["not_found"]
    if "service" in query or "सेवा" in query:
        response = QA_DATA["service"][st.session_state.lang]
    elif "book" in query or "बुकिंग" in query:
        response = QA_DATA["book"][st.session_state.lang]
    elif "payment" in query or "पेमेंट" in query:
        response = QA_DATA["payment"][st.session_state.lang]
        
    st.session_state.messages.append({"role": "assistant", "content": response})

# --- UI RENDER ---
lang_set = STRINGS[st.session_state.lang]

# Header
st.markdown(f"""
    <div class="chat-header">
        <h1 style='margin:0; font-size: 2.5rem;'>{lang_set['title']}</h1>
        <p style='margin:0; opacity:0.9; font-size: 1.1rem;'>{lang_set['subtitle']}</p>
    </div>
""", unsafe_allow_html=True)

# Initial Welcome
if not st.session_state.messages:
    st.session_state.messages.append({"role": "assistant", "content": lang_set["welcome"]})

# Display Chat History
for msg in st.session_state.messages:
    div_class = "user-bubble" if msg["role"] == "user" else "assistant-bubble"
    st.markdown(f'<div class="bubble {div_class}">{msg["content"]}</div>', unsafe_allow_html=True)

# Quick Actions
st.write(f"**{lang_set['quick_actions']}**")
c1, c2, c3 = st.columns(3)
with c1:
    if st.button(lang_set["btn_services"], use_container_width=True):
        process_input(lang_set["btn_services"])
        st.rerun()
with c2:
    if st.button(lang_set["btn_booking"], use_container_width=True):
        process_input(lang_set["btn_booking"])
        st.rerun()
with c3:
    if st.button(lang_set["btn_payment"], use_container_width=True):
        process_input(lang_set["btn_payment"])
        st.rerun()

# Chat Input
if prompt := st.chat_input(lang_set["ask_placeholder"]):
    process_input(prompt)
    st.rerun()