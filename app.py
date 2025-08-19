import streamlit as st
import requests
import datetime
import random
import os
from dotenv import load_dotenv

# ---------------------------
# Load API Key from .env
# ---------------------------
load_dotenv()
API_KEY = os.getenv("API_KEY")
API_URL = "https://api.api-ninjas.com/v1/horoscope"

# ---------------------------
# Zodiac helpers
# ---------------------------
ZODIAC_DATES = [
    ("capricorn", (12, 22), (1, 19)),
    ("aquarius", (1, 20), (2, 18)),
    ("pisces", (2, 19), (3, 20)),
    ("aries", (3, 21), (4, 19)),
    ("taurus", (4, 20), (5, 20)),
    ("gemini", (5, 21), (6, 20)),
    ("cancer", (6, 21), (7, 22)),
    ("leo", (7, 23), (8, 22)),
    ("virgo", (8, 23), (9, 22)),
    ("libra", (9, 23), (10, 22)),
    ("scorpio", (10, 23), (11, 21)),
    ("sagittarius", (11, 22), (12, 21)),
]

SIGN_EMOJI = {
    "aries": "♈", "taurus": "♉", "gemini": "♊", "cancer": "♋",
    "leo": "♌", "virgo": "♍", "libra": "♎", "scorpio": "♏",
    "sagittarius": "♐", "capricorn": "♑", "aquarius": "♒", "pisces": "♓",
}

SIGN_TRAITS = {
    "aries": {"trait": "Bold, energetic, takes initiative.", "mood": "Excited", "lucky_number": 5, "lucky_color": "Red"},
    "taurus": {"trait": "Grounded, patient, values comfort and stability.", "mood": "Calm", "lucky_number": 8, "lucky_color": "Green"},
    "gemini": {"trait": "Curious, communicative, adaptable.", "mood": "Inquisitive", "lucky_number": 3, "lucky_color": "Yellow"},
    "cancer": {"trait": "Caring, intuitive, protective of loved ones.", "mood": "Compassionate", "lucky_number": 2, "lucky_color": "Silver"},
    "leo": {"trait": "Confident, warm, creative; loves the spotlight.", "mood": "Joyful", "lucky_number": 1, "lucky_color": "Gold"},
    "virgo": {"trait": "Practical, detail-oriented, helpful.", "mood": "Focused", "lucky_number": 4, "lucky_color": "Brown"},
    "libra": {"trait": "Diplomatic, charming, seeks balance.", "mood": "Harmonious", "lucky_number": 6, "lucky_color": "Blue"},
    "scorpio": {"trait": "Intense, strategic, emotionally deep.", "mood": "Passionate", "lucky_number": 9, "lucky_color": "Black"},
    "sagittarius": {"trait": "Optimistic, adventurous, truth-seeking.", "mood": "Adventurous", "lucky_number": 7, "lucky_color": "Purple"},
    "capricorn": {"trait": "Ambitious, disciplined, long-term thinker.", "mood": "Determined", "lucky_number": 10, "lucky_color": "Brown"},
    "aquarius": {"trait": "Original, humanitarian, big-picture thinker.", "mood": "Innovative", "lucky_number": 11, "lucky_color": "Turquoise"},
    "pisces": {"trait": "Empathic, imaginative, intuitive.", "mood": "Dreamy", "lucky_number": 12, "lucky_color": "Sea Green"}
}

SEED_TEXT = {
    "career": [
        "Focus on one high-impact task and showcase it.",
        "Networking brings unexpected leads—follow up quickly.",
        "A mentor’s advice unlocks a stuck decision.",
        "Clarity beats speed; refine your plan before acting."
    ],
    "love": [
        "Small gestures deepen bonds today.",
        "Practice honest, gentle communication.",
        "Shared activities rekindle warmth and fun.",
        "Give space and trust—connections strengthen."
    ],
    "money": [
        "Track small expenses; they add up.",
        "A practical purchase outperforms a flashy one.",
        "Separate needs from wants; savings follow.",
        "Compare options—value hides in plain sight."
    ],
    "health": [
        "Hydration + light movement improves focus.",
        "Stretching relieves accumulated tension.",
        "Balance rest and action for steady energy.",
        "Mindful meals stabilize your mood."
    ],
    "general": [
        "A timely message nudges plans forward.",
        "Stay adaptable; a minor detour helps.",
        "Your patience attracts the right collaborator.",
        "Clear boundaries create calm momentum."
    ]
}

# ---------------------------
# Functions
# ---------------------------
def get_zodiac_sign(dob: datetime.date) -> str:
    m, day = dob.month, dob.day
    for sign, (sm, sd), (em, ed) in ZODIAC_DATES:
        if (m == sm and day >= sd) or (m == em and day <= ed) or (sm < m < em) or (sm > em and (m > sm or m < em)):
            return sign
    return "aries"

def fetch_today_horoscope(sign: str):
    headers = {"X-Api-Key": API_KEY}
    params = {"zodiac": sign.lower(), "day": "today"}
    try:
        r = requests.get(API_URL, headers=headers, params=params, timeout=10)
        if r.status_code == 200:
            return r.json()
        else:
            return {"error": f"API Error {r.status_code}: {r.text}"}
    except Exception as e:
        return {"error": str(e)}

# ---------------------------
# Streamlit UI
# ---------------------------
st.set_page_config(page_title="AI Astrologer", page_icon="🔮", layout="centered")
st.title("🔮 AI Astrologer")
st.write("Enter your birth details to get your **today's horoscope**.")

name = st.text_input("Name")
dob = st.date_input("Date of Birth", datetime.date(2000, 1, 1))
time_of_birth = st.time_input("Time of Birth", datetime.time(12, 0))
place = st.text_input("Place of Birth")

if name and dob:
    zodiac = get_zodiac_sign(dob)
    trait_info = SIGN_TRAITS[zodiac]

    # ---------------------------
    # Display Zodiac Card (simple gray background)
    # ---------------------------
    st.markdown(
        f"""
        <div style="
            background: #d3d3d3; 
            padding:20px; 
            border-radius:10px; 
            color:#000;
        ">
        <h2>{zodiac.title()} {SIGN_EMOJI.get(zodiac, '')}</h2>
        <p><strong>Trait:</strong> {trait_info['trait']}</p>
        <p><strong>❤️ Mood:</strong> {trait_info['mood']}  |  <strong>🍀 Lucky Number:</strong> {trait_info['lucky_number']}  |  <strong>🎨 Lucky Color:</strong> {trait_info['lucky_color']}</p>
        </div>
        """, unsafe_allow_html=True
    )

    # ---------------------------
    # Get Today's Horoscope
    # ---------------------------
    if st.button("Get Today's Horoscope"):
        result = fetch_today_horoscope(zodiac)
        if "error" in result:
            st.error(result["error"])
        else:
            st.markdown(f"✨ **Horoscope for {zodiac.title()} (Today)** ✨")
            st.write(result.get("horoscope", "No description available"))

    # ---------------------------
    # Ask the Stars
    # ---------------------------
    st.markdown("---")
    st.subheader("🔍 Ask the Stars")
    question_category = st.selectbox(
        "Choose a category to get advice",
        ["General", "Career", "Love", "Health", "Money"]
    )
    if st.button("Get Advice"):
        category_map = {
            "General": "general",
            "Career": "career",
            "Love": "love",
            "Health": "health",
            "Money": "money"
        }
        key = category_map.get(question_category, "general")
        tip = random.choice(SEED_TEXT.get(key, SEED_TEXT["general"]))
        st.markdown(
            f"""
            <div style="
                background: #d3d3d3; 
                padding:15px;
                border-radius:8px;
                color:#000;
            ">
            <p><strong>As a {zodiac.title()}:</strong> {trait_info['trait']}</p>
            <p><strong>Tip:</strong> {tip}</p>
            <p>🍀 <strong>Lucky Number:</strong> {trait_info['lucky_number']}  ❤️ <strong>Mood:</strong> {trait_info['mood']}  🎨 <strong>Lucky Color:</strong> {trait_info['lucky_color']}</p>
            </div>
            """, unsafe_allow_html=True
        )
