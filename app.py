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
        "English": "To book a service, please visit our 'Contact' page or message us directly on WhatsApp.",
        "मराठी": "सेवा बुक करण्यासाठी, कृपया आमच्या 'संपर्क' पृष्ठास भेट द्या किंवा थेट व्हॉट्सअॅपवर मेसेज करा."
    },
    "payment": {
        "English": "If you are facing payment issues, please share your transaction ID with us.",
        "मराठी": "तुम्हाला पेमेंट समस्या येत असल्यास, कृपया तुमचा व्यवहार आयडी आमच्याशी शेअर करा."
    }
}

# --- 4. ADVANCED STYLING (DARK SIDEBAR & GLASSMORPHISM) ---
st.markdown(f"""
    <style>
    /* Dark Background */
    .stApp {{
        background-color: #0e1117;
    }}

    /* --- SIDEBAR DARK THEME --- */
    [data-testid="stSidebar"] {{
        background-color: #161b22 !important; 
        border-right: 1px solid rgba(255, 255, 255, 0.1);
    }}
    
    .sidebar-title {{
        color: #ffffff !important;
        font-weight: 800 !important;
        font-size: 1.2rem;
        letter-spacing: 1px;
        text-transform: uppercase;
        margin-bottom: 15px !important;
        padding-top: 20px;
    }}

    [data-testid="stSidebar"] label, [data-testid="stSidebar"] .st-at {{
        color: #e6edf3 !important;
        font-weight: 500 !important;
        font-size: 15px !important;
    }}

    .lang-box {{
        border-radius: 12px;
        border: 1px solid rgba(255, 0, 128, 0.4);
        padding: 15px;
        background-color: #0d1117;
        margin-top: 10px;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.5);
    }}

    /* --- HEADER & BUBBLES (GLASSMORPHISM) --- */
    .chat-header {{
        background: linear-gradient(135deg, #FF0080 0%, #2D7FF9 100%);
        padding: 18px 10px;
        border-radius: 16px;
        text-align: center;
        margin-bottom: 22px;
        box-shadow: 0 8px 32px 0 rgba(255, 0, 128, 0.2), 0 4px 10px rgba(0, 0, 0, 0.4);
        border: 1px solid rgba(255, 255, 255, 0.18);
        backdrop-filter: blur(4px);
    }}
    
    .header-title {{
        margin: 0 !important;
        font-size: 1.4rem !important;
        font-weight: 800 !important;
        letter-spacing: 1.2px;
        text-transform: uppercase;
        color: white !important;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }}
    
    .header-subtitle {{
        margin: 6px 0 0 0 !important;
        font-size: 0.75rem !important;
        font-weight: 500 !important;
        color: rgba(255, 255, 255, 0.9) !important;
        letter-spacing: 0.5px;
        border-top: 1px solid rgba(255, 255, 255, 0.2);
        display: inline-block;
        padding-top: 4px;
    }}

    .bubble {{
        padding: 12px 18px;
        border-radius: 20px;
        margin: 8px 0;
        max-width: 85%;
        font-size: 14px;
        line-height: 1.5;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
    }}
    .assistant-bubble {{
        background: rgba(255, 255, 255, 0.95);
        color: #1a1a1a;
        align-self: flex-start;
        border-bottom-left-radius: 4px;
    }}
    .user-bubble {{
        background: linear-gradient(135deg, #FF0080 0%, #2D7FF9 100%);
        color: white;
        margin-left: auto;
        border-bottom-right-radius: 4px;
        text-align: left;
    }}

    /* WhatsApp Float */
    .wa-float {{
        position: fixed; bottom: 100px; right: 25px;
        background-color: #25d366; border-radius: 50px;
        z-index: 1000; width: 55px; height: 55px;
        display: flex; align-items: center; justify-content: center;
        box-shadow: 0 4px 10px rgba(0,0,0,0.3);
    }}
    </style>
    
    <a href="https://wa.me/918956727311" class="wa-float" target="_blank">
        <img src="https://upload.wikimedia.org/wikipedia/commons/6/6b/WhatsApp.svg" width="30">
    </a>
""", unsafe_allow_html=True)

# --- 5. SIDEBAR (DARK MENU) ---
with st.sidebar:
    st.markdown(f'<div class="sidebar-title">{STRINGS[st.session_state.lang]["sidebar_label"]}</div>', unsafe_allow_html=True)
    st.markdown('<div class="lang-box">', unsafe_allow_html=True)
    choice = st.radio(
        "Language", ["English", "मराठी"],
        index=0 if st.session_state.lang == "English" else 1,
        label_visibility="collapsed"
    )
    st.markdown('</div>', unsafe_allow_html=True)
    
    if choice != st.session_state.lang:
        st.session_state.lang = choice
        st.rerun()

# --- 6. LOGIC ---
def process_input(text):
    st.session_state.messages.append({"role": "user", "content": text})
    query = text.lower()
    response = STRINGS[st.session_state.lang]["not_found"]
    
    if any(k in query for k in ["service", "सेवा"]):
        response = QA_DATA["service"][st.session_state.lang]
    elif any(k in query for k in ["book", "बुकिंग"]):
        response = QA_DATA["book"][st.session_state.lang]
    elif any(k in query for k in ["payment", "पेमेंट"]):
        response = QA_DATA["payment"][st.session_state.lang]
        
    st.session_state.messages.append({"role": "assistant", "content": response})

# --- 7. UI RENDER ---
lang_set = STRINGS[st.session_state.lang]

st.markdown(f"""
    <div class="chat-header">
        <div class="header-title">{lang_set['title']}</div>
        <div class="header-subtitle">{lang_set['subtitle']}</div>
    </div>
""", unsafe_allow_html=True)

if not st.session_state.messages:
    st.session_state.messages.append({"role": "assistant", "content": lang_set["welcome"]})

for msg in st.session_state.messages:
    div_class = "user-bubble" if msg["role"] == "user" else "assistant-bubble"
    st.markdown(f'<div class="bubble {div_class}">{msg["content"]}</div>', unsafe_allow_html=True)

# Quick Actions
st.markdown(f"<div style='color: #888; font-size: 0.85rem; font-weight: bold; margin: 20px 0 10px 0;'>{lang_set['quick_actions']}</div>", unsafe_allow_html=True)
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

if prompt := st.chat_input(lang_set["ask_placeholder"]):
    process_input(prompt)
    st.rerun()