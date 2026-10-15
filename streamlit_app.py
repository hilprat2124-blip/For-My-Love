import streamlit as st
import random
import time

# ================== KONFIGURASI HALAMAN ==================
st.set_page_config(
    page_title="Untuk Kamu 💖",
    page_icon="💕",
    layout="centered"
)

# ================== KATA-KATA SEMANGAT ==================
kata_semangat = [
    "Semangat ya sayangku! Kamu pasti bisa melewati hari ini! 💪💖",
    "Jangan lupa makan ya cantik, aku gak mau kamu sakit 🥺🍜",
    "Kamu itu kuat, hebat, dan luar biasa! Aku bangga sama kamu 🌟",
    "Kalau capek, istirahat ya. Aku selalu ada buat kamu 💕",
    "Hari ini boleh sedih, besok harus senyum lagi ya sayang 😊",
    "Kamu tuh kayak kopi, bikin hari-hariku jadi lebih hidup ☕💗",
    "Semangat kerjanya! Nanti aku traktir kamu ya 🍰",
    "Kamu adalah alasan aku senyum sendiri kayak orang gila 😆💘",
    "Aku sayang kamu lebih dari kemarin, tapi kurang dari besok 💌",
    "Jangan overthinking ya, aku cuma cinta sama kamu kok 🥰",
    "Kamu cantik, pinter, dan menggemaskan. Paket lengkap! 🎀",
    "Kalau dunia jahat sama kamu, aku lawan! 😤💗",
    "Semangat terus ya, aku selalu support kamu dari sini 📣💖",
    "Kamu itu bunga, dan aku lebahnya. Eh, gombal ya? Hehe 🐝🌸",
    "Aku gak butuh kopi, aku butuh kamu tiap pagi ☕💕",
    "Kamu itu sekuat baja, tapi selembut kapas. Aku suka! 🩷",
    "Jangan lupa minum air putih ya, biar makin glowing ✨",
    "Aku bangga punya kamu. Serius deh, gak boong 🥺💗",
]

# ================== ALASAN SAYANG ==================
alasan_sayang = [
    "Aku sayang kamu karena senyum kamu bikin dunia aku terang ✨",
    "Aku sayang kamu karena kamu selalu dengerin cerita aku 🎧💗",
    "Aku sayang kamu karena kamu sabar banget sama aku 😌💖",
    "Aku sayang kamu karena kamu wangi dan bikin aku nyaman 🌸",
    "Aku sayang kamu karena kamu pinter masak (walau kadang gosong) 🍳😆",
    "Aku sayang kamu karena kamu tuh home aku 🏡💕",
    "Aku sayang kamu karena kamu gak pernah bosen sama aku 🥺",
    "Aku sayang kamu karena kamu ganteng/cantik banget 😍",
    "Aku sayang kamu karena kamu selalu bikin aku ketawa 🤣💗",
    "Aku sayang kamu karena kamu tuh paket lengkap, gak ada obat 💊💕",
]

# ================== CSS CUSTOM PINK GIRLY ==================
st.markdown("""
<style>
    /* Background utama pink gradasi */
    .stApp {
        background: linear-gradient(135deg, #ffd1dc 0%, #ffb6c1 50%, #ffc0cb 100%);
    }

    /* Container utama */
    .main-container {
        background: rgba(255, 255, 255, 0.85);
        border-radius: 30px;
        padding: 40px 30px;
        box-shadow: 0 20px 50px rgba(255, 105, 180, 0.4);
        text-align: center;
        border: 3px dashed #ff8fab;
        margin-top: 20px;
        animation: float 3s ease-in-out infinite;
    }

    @keyframes float {
        0%, 100% { transform: translateY(0); }
        50% { transform: translateY(-8px); }
    }

    /* Judul */
    h1 {
        font-family: 'Pacifico', cursive;
        color: #ff4d88 !important;
        text-align: center;
        font-size: 2.5em !important;
        text-shadow: 2px 2px 4px rgba(255, 182, 193, 0.6);
    }

    /* Card pesan */
    .card {
        background: linear-gradient(135deg, #fff0f5, #ffe4ec);
        border-radius: 20px;
        padding: 25px 20px;
        margin: 20px 0;
        border: 2px solid #ffb6c1;
        box-shadow: inset 0 0 15px rgba(255, 182, 193, 0.3);
    }

    .card-title {
        font-family: 'Pacifico', cursive;
        color: #ff69b4;
        font-size: 1.3em;
        margin-bottom: 12px;
        text-align: center;
    }

    .card-text {
        color: #c71585;
        font-size: 1.2em;
        line-height: 1.6;
        font-weight: 600;
        text-align: center;
    }

    /* Tombol */
    .stButton > button {
        background: linear-gradient(135deg, #ff69b4, #ff1493) !important;
        color: white !important;
        border: none !important;
        padding: 15px 35px !important;
        border-radius: 50px !important;
        font-size: 1.1em !important;
        font-weight: 700 !important;
        box-shadow: 0 8px 20px rgba(255, 105, 180, 0.5) !important;
        transition: all 0.3s !important;
        width: 100% !important;
    }

    .stButton > button:hover {
        transform: translateY(-3px) scale(1.03);
        box-shadow: 0 12px 25px rgba(255, 105, 180, 0.7) !important;
    }

    /* Footer */
    .footer {
        text-align: center;
        color: #ff69b4;
        font-size: 0.95em;
        font-style: italic;
        margin-top: 25px;
    }

    /* Sembunyikan menu streamlit */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# ================== KONTEN ==================
st.markdown('<h1>💖 Hai Sayang! 💖</h1>', unsafe_allow_html=True)
st.markdown(
    '<p style="text-align:center; color:#ff69b4; font-weight:600; font-size:1.1em;">'
    'Website ini dibuat khusus buat kamu 💌</p>',
    unsafe_allow_html=True
)

# Inisialisasi session state biar pesan gak berubah tiap refresh
if "pesan" not in st.session_state:
    st.session_state.pesan = random.choice(kata_semangat)
if "alasan" not in st.session_state:
    st.session_state.alasan = random.choice(alasan_sayang)

# Card pesan semangat
st.markdown(f"""
<div class="card">
    <div class="card-title">✨ Semangat Hari Ini ✨</div>
    <p class="card-text">{st.session_state.pesan}</p>
</div>
""", unsafe_allow_html=True)

# Card alasan sayang
st.markdown(f"""
<div class="card">
    <div class="card-title">💕 Alasan Aku Sayang Kamu 💕</div>
    <p class="card-text">{st.session_state.alasan}</p>
</div>
""", unsafe_allow_html=True)

# Tombol ganti pesan
if st.button("🎀 Kasih Aku Pesan Baru 🎀"):
    st.session_state.pesan = random.choice(kata_semangat)
    st.session_state.alasan = random.choice(alasan_sayang)
    st.balloons()  # 🎈 efek balon
    st.rerun()

# Footer
st.markdown(
    '<p class="footer">Made with 💗 by pacar kamu yang paling ganteng</p>',
    unsafe_allow_html=True
)
