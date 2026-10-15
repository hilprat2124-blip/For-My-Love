import streamlit as st
import streamlit.components.v1 as components
import random

# ================== KONFIG ==================
st.set_page_config(
    page_title="buat kamu 💕",
    page_icon="🎀",
    layout="centered"
)

# ================== DATA KATA SEMANGAT NUGAS ==================
kata_nugas = [
    "dikit lagi selesai kok, jangan nyerah dulu ya 🥺",
    "skripsi/tugasnya bakal kangen kamu kalo gak dikerjain wkwk 📚",
    "capek itu wajar, tapi kamu lebih kuat dari capeknya 💪",
    "nugas sambil dengerin lagu favorit, dijamin lebih enak 🎧",
    "kalo udah selesai, aku traktir kamu es krim 🍦",
    "dunia butuh orang pinter, jadi jangan males nugas ya 😤",
    "istirahat boleh, nyerah jangan ya sayang 💗",
    "kamu tuh hebat, aku aja bangga liat kamu berjuang 🌟",
    "semangat! nanti aku elus-elus kepala kamu (bayangin aja dulu) 🤲",
    "dikit lagi, dikit lagi... janji deh setelah ini kita have fun 🎉",
    "aku percaya kamu bisa, jadi kamu harus percaya juga ✨",
    "jangan lupa makan & minum, jangan sampe tumbang 🍜",
    "nugasnya pelan-pelan aja, gak usah buru-buru 🐢",
    "kamu tuh pinter, cuma kadang lupa aja kalo kamu pinter 😆",
    "yang sabar ya, semua ini bakal worth it kok 🥰",
    "kalo bingung, tarik napas, terus mikir lagi. kamu bisa! 💭",
]

# ================== KALIMAT POP SURPRISE ==================
kalimat_penutup = (
    "jujur ya, aku tuh gak tau harus gimana ngejelasin ini semua ke kamu. "
    "tiap hari rasanya aku makin sayang, makin cinta, makin pengen kamu bahagia terus. "
    "kamu itu bukan cuma pacar, kamu udah jadi tempat aku pulang, tempat aku cerita hal-hal random, "
    "tempat aku jadi diri aku sendiri tanpa takut dihakimi. "
    "makasih ya udah bertahan, udah sabar, udah sayang sama aku yang kadang nyebelin ini. "
    "aku gak janji bisa jadi sempurna, tapi aku janji bakal terus ada buat kamu — "
    "di hari kamu seneng, di hari kamu capek, di hari kamu ngerasa sendirian. "
    "pokoknya, aku cinta banget sama kamu. banget. serius. gak boong. 💖"
)

# ================== CSS GIRLY LUCU ==================
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(135deg, #ffe0ec 0%, #ffc9dd 100%);
    }

    #MainMenu, footer, header {visibility: hidden;}

    .judul {
        text-align: center;
        font-family: 'Comic Sans MS', cursive;
        color: #ff4d88;
        font-size: 2em;
        margin-bottom: 5px;
    }

    .subjudul {
        text-align: center;
        color: #ff69b4;
        font-size: 1em;
        margin-bottom: 25px;
        font-style: italic;
    }

    /* Kotak misteri */
    .box {
        background: linear-gradient(135deg, #ff9ec7, #ff69b4);
        border-radius: 20px;
        padding: 40px 20px;
        text-align: center;
        color: white;
        font-size: 3em;
        cursor: pointer;
        box-shadow: 0 10px 25px rgba(255, 105, 180, 0.5);
        transition: transform 0.2s;
        border: 4px dashed #fff;
        margin: 10px 0;
    }

    .box:hover {
        transform: scale(1.05) rotate(-2deg);
    }

    /* Card pesan */
    .pesan-card {
        background: rgba(255, 255, 255, 0.95);
        border-radius: 20px;
        padding: 30px 25px;
        margin: 20px 0;
        border: 3px dotted #ff69b4;
        text-align: center;
        color: #d63384;
        font-size: 1.15em;
        font-weight: 600;
        line-height: 1.6;
        box-shadow: 0 8px 20px rgba(255, 182, 193, 0.4);
    }

    .counter {
        text-align: center;
        color: #ff69b4;
        font-size: 0.9em;
        font-style: italic;
        margin-top: 10px;
    }

    /* Tombol */
    .stButton > button {
        background: linear-gradient(135deg, #ff69b4, #ff1493) !important;
        color: white !important;
        border: none !important;
        padding: 14px 30px !important;
        border-radius: 50px !important;
        font-size: 1.05em !important;
        font-weight: 700 !important;
        box-shadow: 0 6px 18px rgba(255, 105, 180, 0.5) !important;
        transition: all 0.3s !important;
        width: 100% !important;
    }

    .stButton > button:hover {
        transform: translateY(-2px) scale(1.02);
        box-shadow: 0 10px 22px rgba(255, 105, 180, 0.7) !important;
    }

    .footer {
        text-align: center;
        color: #ff69b4;
        font-size: 0.85em;
        margin-top: 30px;
        opacity: 0.8;
    }
</style>
""", unsafe_allow_html=True)


# ================== SESSION STATE ==================
if "step" not in st.session_state:
    st.session_state.step = 0  # 0 = belum mulai, 1 = lagi buka kotak, 99 = surprise

if "pesan_sekarang" not in st.session_state:
    st.session_state.pesan_sekarang = ""

if "riwayat" not in st.session_state:
    st.session_state.riwayat = []

if "sisa_pesan" not in st.session_state:
    # acak urutan kata semangat biar gak repetitif
    pool = kata_nugas.copy()
    random.shuffle(pool)
    st.session_state.sisa_pesan = pool


# ================== FUNGSI ==================
def ambil_pesan_baru():
    if not st.session_state.sisa_pesan:
        # kalau udah habis, trigger surprise
        st.session_state.step = 99
        return
    pesan = st.session_state.sisa_pesan.pop()
    st.session_state.pesan_sekarang = pesan
    st.session_state.riwayat.append(pesan)


def reset_semua():
    st.session_state.step = 0
    st.session_state.pesan_sekarang = ""
    st.session_state.riwayat = []
    pool = kata_nugas.copy()
    random.shuffle(pool)
    st.session_state.sisa_pesan = pool


# ================== HALAMAN: AWAL ==================
if st.session_state.step == 0:
    st.markdown('<div class="judul">🎀 hai kamu 🎀</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="subjudul">aku titipin sesuatu di kotak-kotak ini... '
        'buka satu-satu ya, jangan nyolong buka semua 😤💕</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="box">🎁</div>',
        unsafe_allow_html=True
    )

    if st.button("buka kotaknya 💌"):
        st.session_state.step = 1
        ambil_pesan_baru()
        st.rerun()


# ================== HALAMAN: BUKA KOTAK ==================
elif st.session_state.step == 1:
    st.markdown('<div class="judul">💌 pesan buat kamu 💌</div>', unsafe_allow_html=True)

    st.markdown(
        f'<div class="pesan-card">{st.session_state.pesan_sekarang}</div>',
        unsafe_allow_html=True
    )

    sisa = len(st.session_state.sisa_pesan)
    total = len(kata_nugas)
    sudah = total - sisa

    st.markdown(
        f'<div class="counter">kotak yang udah kamu buka: {sudah} / {total} 🎁</div>',
        unsafe_allow_html=True
    )

    if sisa > 0:
        if st.button("lanjut buka kotak lagi 🎀"):
            ambil_pesan_baru()
            st.rerun()
    else:
        st.markdown(
            '<div class="counter">kotaknya udah abis nih... '
            'tapi ada satu hal lagi buat kamu 👀</div>',
            unsafe_allow_html=True
        )
        if st.button("buka yang terakhir ✨"):
            st.session_state.step = 99
            st.rerun()

    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("🔄 ulang dari awal"):
        reset_semua()
        st.rerun()


# ================== HALAMAN: SURPRISE ==================
elif st.session_state.step == 99:

    # ---- HTML + CSS + JS untuk sparkle love + fireworks ----
    html_surprise = f"""
    <!DOCTYPE html>
    <html>
    <head>
    <style>
        body {{
            margin: 0;
            padding: 0;
            background: transparent;
            font-family: 'Comic Sans MS', cursive;
            overflow: hidden;
        }}

        #fireworks {{
            position: fixed;
            top: 0; left: 0;
            width: 100%;
            height: 100%;
            z-index: 0;
            pointer-events: none;
        }}

        .love-sparkle {{
            position: fixed;
            font-size: 24px;
            animation: sparkleFloat 3s ease-in-out infinite;
            z-index: 2;
            pointer-events: none;
        }}

        @keyframes sparkleFloat {{
            0% {{ transform: translateY(0) scale(1); opacity: 1; }}
            50% {{ transform: translateY(-15px) scale(1.3); opacity: 0.7; }}
            100% {{ transform: translateY(0) scale(1); opacity: 1; }}
        }}

        .konten {{
            position: relative;
            z-index: 3;
            background: rgba(255, 255, 255, 0.94);
            border-radius: 25px;
            padding: 35px 30px;
            margin: 20px auto;
            max-width: 650px;
            border: 4px dashed #ff69b4;
            box-shadow: 0 15px 40px rgba(255, 105, 180, 0.5);
            text-align: center;
            animation: popIn 0.8s ease-out;
        }}

        @keyframes popIn {{
            0% {{ transform: scale(0.5); opacity: 0; }}
            70% {{ transform: scale(1.05); }}
            100% {{ transform: scale(1); opacity: 1; }}
        }}

        .judul-surprise {{
            font-size: 1.8em;
            color: #ff1493;
            margin-bottom: 15px;
            animation: heartbeat 1.5s infinite;
        }}

        @keyframes heartbeat {{
            0%, 100% {{ transform: scale(1); }}
            25% {{ transform: scale(1.1); }}
            50% {{ transform: scale(1); }}
        }}

        .paragraf {{
            color: #c71585;
            font-size: 1.05em;
            line-height: 1.8;
            text-align: left;
            padding: 10px 5px;
            font-weight: 600;
        }}

        .ttd {{
            margin-top: 25px;
            color: #ff69b4;
            font-size: 1.1em;
            font-style: italic;
            text-align: right;
        }}
    </style>
    </head>
    <body>

    <canvas id="fireworks"></canvas>

    <div class="konten">
        <div class="judul-surprise">💖 surprise 💖</div>
        <div class="paragraf">{kalimat_penutup}</div>
        <div class="ttd">— dari aku, yang sayang banget sama kamu 💗</div>
    </div>

    <script>
        // ===== SPARKLE LOVE BERJATUHAN =====
        const loveEmojis = ['💖','💕','✨','💗','🩷','💞','🌸','⭐'];
        function spawnLove() {{
            const el = document.createElement('div');
            el.className = 'love-sparkle';
            el.textContent = loveEmojis[Math.floor(Math.random() * loveEmojis.length)];
            el.style.left = Math.random() * 100 + 'vw';
            el.style.top = Math.random() * 100 + 'vh';
            el.style.fontSize = (Math.random() * 20 + 16) + 'px';
            el.style.animationDuration = (Math.random() * 2 + 2) + 's';
            document.body.appendChild(el);
            setTimeout(() => el.remove(), 3500);
        }}
        setInterval(spawnLove, 200);

        // ===== FIREWORKS =====
        const canvas = document.getElementById('fireworks');
        const ctx = canvas.getContext('2d');
        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;

        window.addEventListener('resize', () => {{
            canvas.width = window.innerWidth;
            canvas.height = window.innerHeight;
        }});

        const particles = [];
        const colors = ['#ff69b4','#ff1493','#ffb6c1','#ff85c1','#fff0f5','#ff4d88'];

        function createFirework(x, y) {{
            const count = 40 + Math.floor(Math.random() * 30);
            for (let i = 0; i < count; i++) {{
                const angle = (Math.PI * 2 * i) / count;
                const speed = Math.random() * 5 + 2;
                particles.push({{
                    x: x,
                    y: y,
                    vx: Math.cos(angle) * speed,
                    vy: Math.sin(angle) * speed,
                    life: 1,
                    color: colors[Math.floor(Math.random() * colors.length)],
                    size: Math.random() * 3 + 2
                }});
            }}
        }}

        function animate() {{
            ctx.fillStyle = 'rgba(255, 224, 236, 0.15)';
            ctx.fillRect(0, 0, canvas.width, canvas.height);

            for (let i = particles.length - 1; i >= 0; i--) {{
                const p = particles[i];
                p.x += p.vx;
                p.y += p.vy;
                p.vy += 0.06;
                p.vx *= 0.98;
                p.vy *= 0.98;
                p.life -= 0.015;

                if (p.life <= 0) {{
                    particles.splice(i, 1);
                    continue;
                }}

                ctx.globalAlpha = p.life;
                ctx.fillStyle = p.color;
                ctx.beginPath();
                ctx.arc(p.x, p.y, p.size, 0, Math.PI * 2);
                ctx.fill();
            }}
            ctx.globalAlpha = 1;
            requestAnimationFrame(animate);
        }}

        animate();

        // trigger fireworks berkala
        setInterval(() => {{
            createFirework(
                Math.random() * canvas.width,
                Math.random() * canvas.height * 0.6
            );
        }}, 700);

        // ledakan awal pas halaman muncul
        setTimeout(() => createFirework(canvas.width/2, canvas.height/3), 300);
        setTimeout(() => createFirework(canvas.width*0.3, canvas.height*0.5), 700);
        setTimeout(() => createFirework(canvas.width*0.7, canvas.height*0.4), 1100);
    </script>

    </body>
    </html>
    """

    components.html(html_surprise, height=800, scrolling=False)

    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("🔄 ulang dari awal ya"):
        reset_semua()
        st.rerun()


# ================== FOOTER ==================
st.markdown(
    '<div class="footer">dibuat sambil mikirin kamu terus 🩷</div>',
    unsafe_allow_html=True
)
