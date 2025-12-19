import streamlit as st
import base64

# 1. Page Configuration
st.set_page_config(page_title="Best of Amravati | Assistant", page_icon="💬", layout="centered")

# --- IMAGE PROCESSING SECTION ---
def get_base64_of_bin_file(bin_file):
    try:
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()
    except Exception:
        return None

# Load your local logo from the 'jpg' folder
img_base64 = get_base64_of_bin_file("jpg/logobestofamravati.jpg")


# 2. Modern UI Styling (Vibrant Pink & Blue Gradient)
st.markdown(f"""
    <style>
    [data-testid="stAppViewContainer"] {{ background-color: #FDF4F7 !important; }}
    [data-testid="stHeader"], [data-testid="stBottom"] {{ background: transparent !important; }}

    /* Branded Gradient Header */
    .chat-header {{
        background: linear-gradient(135deg, #FF0080 0%, #7928CA 50%, #2D7FF9 100%);
        padding: 22px;
        border-radius: 20px 20px 0 0;
        color: white;
        display: flex;
        align-items: center;
        margin-bottom: 10px;
        box-shadow: 0 4px 15px rgba(255, 0, 128, 0.2);
    }}
    
    .header-text h2 {{ font-size: 19px !important; margin: 0 !important; color: white !important; font-weight: 700 !important; }}
    .status-text {{ font-size: 12px; opacity: 0.9; letter-spacing: 0.5px; }}

    /* Chat Bubbles */
    .chat-row {{ display: flex; margin: 10px 0; width: 100%; }}
    .row-user {{ justify-content: flex-end; }}
    .row-assistant {{ justify-content: flex-start; }}

    .bubble {{
        padding: 14px 18px;
        max-width: 80%;
        font-size: 15px;
        font-family: 'Inter', sans-serif;
        line-height: 1.5;
    }}
    .assistant-bubble {{
        background-color: #FFFFFF;
        color: #1A1A1A;
        border-radius: 20px 20px 20px 5px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.05);
        border: 1px solid #F0E0E5;
    }}
    .user-bubble {{
        background: linear-gradient(135deg, #2D7FF9 0%, #FF0080 100%);
        color: white;
        border-radius: 20px 20px 5px 20px;
        font-weight: 500;
    }}

    /* Gradient Quick Reply Buttons */
    .stButton > button {{
        border-radius: 25px !important;
        border: 1px solid #FF0080 !important;
        background: white !important;
        color: #FF0080 !important;
        padding: 8px 20px !important;
        font-size: 14px !important;
        font-weight: 600 !important;
        width: 100%;
        transition: all 0.4s ease;
    }}
    .stButton > button:hover {{
        background: linear-gradient(135deg, #FF0080 0%, #2D7FF9 100%) !important;
        color: white !important;
        border: none !important;
        transform: translateY(-2px);
    }}

   
    </style>
    
    <a href="https://wa.me/918956727311" class="wa-float" target="_blank">
        <img src="https://upload.wikimedia.org/wikipedia/commons/6/6b/WhatsApp.svg" width="30">
    </a>
    """, unsafe_allow_html=True)

# 3. Knowledge Base (Sourced from provided documentation)
QA_DATA = {
    "what is best of amravati?": "Best of Amravati is a digital platform that promotes trusted local businesses in Amravati.",
    "Is this an advertisement?": "Yes, it is a digital promotional service for your business.",
    "what service do you provide?": "Media, Digital News, Business Magazine ,Branding ,Collaboration.   We create and promote professional reels to give your business high digital visibility.",
    "how will you promote my business?": "We promote your business using creative reels across Instagram, Facebook, and YouTube Shorts.",
    "what is a promotional reel?": "A promotional reel is a short creative video showcasing your business, offers, and services.",
    "how long is the reel?": "The reel duration is between 30 to 60 seconds. ",
    "will you shoot video at my shop?": "Yes, we shoot professional videos at your business location.",
    "where will my reel be posted?": "Your reel will be posted on Best of Amravati's Instagram, Facebook, and YouTube Shorts. ",
    "how many views will i get?": "We guarantee a minimum combined reach of 1,00,000+ views.",
    "is the reach guaranteed?": "Yes, the minimum reach is guaranteed across all platforms.",
    "how does this help my business?": "It increases brand visibility, customer trust, and local footfall.",
    "is this only for amravati businesses?": "Yes, this service is specially designed for Amravati-based businesses.",
    "can i promote offers or discounts?": "Yes, your offers, discounts, and special deals can be highlighted.",
    "will my business name be tagged?": "Yes, your business will be tagged and featured in the post. ",
    "do i get the reel file?": "Yes, you will receive the final reel file.",

    "can i post the reel on my own page?": "Yes, you can freely post the reel on your social media accounts. ",
    "how much does it cost?": "Pricing depends on the promotion plan; please contact us for details.",
    "are there any extra charges?": "No, there are no hidden or extra charges.",
    "how can i book this service?": "You can book by contacting our team directly.",
    "how long does delivery take?": "The reel is usually delivered within a few working days.",
    "how can i contact your team?": "You can contact us via WhatsApp, call, or Instagram DM.",
    "payment issue": "This is my ..bestofamravati@gmail.com.. we will contact you within 24hrs regarding your payment concern."
}

def get_response(user_input):
    user_input = user_input.lower().strip()
    for question, answer in QA_DATA.items():
        if question in user_input:
            return answer
    return "I'm sorry, I didn't quite catch that. Would you like to know about our reels, reach, or pricing?"

# 4. Interface Structure
def main():
    st.markdown("""
        <div class="chat-header">
            <div class="avatar-circle"></div>
            <div class="header-text">
                <h2>BEST of AMRAVATI</h2>
                <div class="status-text">● How I Can Help You!</div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "assistant", "content": "Welcome! Ready to transform your business with viral reels? 🎬"
        "         Ask Me Any Question...    I am Here to Give You Solution"}]

       
    for msg in st.session_state.messages:
        div_class = "row-assistant" if msg["role"] == "assistant" else "row-user"
        bub_class = "assistant-bubble" if msg["role"] == "assistant" else "user-bubble"
        st.markdown(f'<div class="chat-row {div_class}"><div class="bubble {bub_class}">{msg["content"]}</div></div>', unsafe_allow_html=True)

    # Quick Replies Section
    st.write("---")
    st.markdown("##### Quick Actions")
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("Our Services"): process_message("what service do you provide?")
    with col2:
        if st.button("How to Book?"): process_message("How can I book this service?")
    with col3:
        if st.button("Payment Issue"): process_message("payment issue")
    
    if prompt := st.chat_input("Ask me anything..."):
        process_message(prompt)

def process_message(text):
    st.session_state.messages.append({"role": "user", "content": text})
    response = get_response(text)
    st.session_state.messages.append({"role": "assistant", "content": response})
    st.rerun()

if __name__ == "__main__":
    main()