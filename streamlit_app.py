import streamlit as st
import streamlit.components.v1 as components
import random

# ================== KONFIG ==================
st.set_page_config(
    page_title="Untuk Kamu",
    page_icon="🌸",
    layout="centered"
)

# ================== KATA SEMANGAT NUGAS ==================
kata_nugas = [
    "Sayang... aku tahu kamu capek, tapi aku percaya kamu pasti bisa. Semangat ya, cintakuu.",
    "Aku tahu tugas kamu banyak, tapi aku juga tahu kamu sekuat itu. Aku bangga banget sama kamu.",
    "Capek boleh, istirahat dulu juga boleh. Kamu nggak harus selalu kuat setiap saat, yaa... Aku tetap bangga sama kamu, apa pun hasilnya.",
    "Coba nugas sambil bayangin aku lagi nemenin kamu, yaa. Anggap aja aku lagi duduk di samping kamu sambil elus kepala kamu pelan-pelan. 🤍",
    "Kalau udah selesai, aku traktir kamu es krim.",
    "Kalau tugas kamu udah selesai, sini cerita sama aku. Aku mau dengerin semua keluh kesah kamu, terus aku peluk yang lamaaa.",
]

# ================== PARAGRAF CINTA ==================
kalimat_penutup = (
    "Sayang... aku gak tau harus gimana ngejelasin ini semua ke kamu. "
    "Tiap hari rasanya aku makin sayang, makin cinta, makin pengen kamu bahagia terus. "
    "Kamu itu bukan cuma pacar. Kamu udah jadi tempat aku pulang, tempat aku cerita hal-hal random, "
    "Makasih ya udah bertahan, udah sabar, udah sayang sama aku yang menyebalkan ini. "
    "Kita tau hubungan tidak selalu mulus, tapi aku janji bakal terus ada buat kamu, "
    "di hari kamu senang, di hari kamu capek, di hari kamu ngerasa sendirian. "
    "Pokoknya, aku cinta banget banget banget sama kamu. "
    "I LOVE YOU SOOOOOOOOOO MMMMUUUUUUCCCHHHHH SAYANGGGG!!!!!!"
)

# ================== CSS ==================
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Caveat:wght@600&family=Nunito:wght@400;600;700&display=swap');

    .stApp {
        background: linear-gradient(160deg, #ffe9f0 0%, #ffd9e6 55%, #ffc7db 100%);
        font-family: 'Nunito', sans-serif;
    }

    #MainMenu, footer, header {visibility: hidden;}

    .judul {
        text-align: center;
        font-family: 'Caveat', cursive;
        color: #d6336c;
        font-size: 2.6em;
        margin-bottom: 0;
        letter-spacing: 0.5px;
        animation: fadeDown 0.9s ease-out;
    }

    .subjudul {
        text-align: center;
        color: #e0709a;
        font-size: 0.98em;
        margin-top: 0;
        margin-bottom: 28px;
        font-style: italic;
        animation: fadeDown 1.2s ease-out;
    }

    @keyframes fadeDown {
        from { opacity: 0; transform: translateY(-12px); }
        to { opacity: 1; transform: translateY(0); }
    }

    .box-wrap {
        display: flex;
        justify-content: center;
        margin: 20px 0 30px 0;
        animation: floatY 3.2s ease-in-out infinite;
    }

    @keyframes floatY {
        0%, 100% { transform: translateY(0); }
        50% { transform: translateY(-10px); }
    }

    .box {
        width: 170px;
        height: 170px;
        background: linear-gradient(145deg, #ffb3cc, #ff7fae);
        border-radius: 28px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 4em;
        box-shadow: 0 18px 40px rgba(214, 51, 108, 0.35),
                    inset 0 -6px 12px rgba(255, 255, 255, 0.4);
        border: 3px solid rgba(255, 255, 255, 0.7);
        position: relative;
        animation: shake 2.6s ease-in-out infinite;
    }

    @keyframes shake {
        0%, 100% { transform: rotate(0deg); }
        15% { transform: rotate(-4deg); }
        30% { transform: rotate(4deg); }
        45% { transform: rotate(-3deg); }
        60% { transform: rotate(0deg); }
    }

    .pesan-card {
        background: rgba(255, 255, 255, 0.96);
        border-radius: 22px;
        padding: 34px 28px;
        margin: 18px auto;
        max-width: 560px;
        text-align: center;
        color: #b02a5b;
        font-size: 1.18em;
        font-weight: 600;
        line-height: 1.75;
        box-shadow: 0 12px 32px rgba(214, 51, 108, 0.15),
                    0 0 0 3px rgba(255, 179, 204, 0.6);
        position: relative;
        animation: cardIn 0.7s cubic-bezier(0.22, 1, 0.36, 1);
    }

    .pesan-card::before {
        content: "❝";
        position: absolute;
        top: 6px;
        left: 18px;
        font-size: 2.2em;
        color: #ffb3cc;
        font-family: Georgia, serif;
        line-height: 1;
    }

    @keyframes cardIn {
        0% { opacity: 0; transform: translateY(18px) scale(0.94); filter: blur(4px); }
        60% { filter: blur(0); }
        100% { opacity: 1; transform: translateY(0) scale(1); }
    }

    .counter {
        text-align: center;
        color: #d6336c;
        font-size: 0.88em;
        font-style: italic;
        margin-top: 12px;
        opacity: 0.85;
        animation: fadeDown 0.9s ease-out;
    }

    .stButton > button {
        background: linear-gradient(135deg, #ff7fae, #d6336c) !important;
        color: #fff !important;
        border: none !important;
        padding: 14px 26px !important;
        border-radius: 999px !important;
        font-size: 1.02em !important;
        font-weight: 700 !important;
        letter-spacing: 0.3px !important;
        box-shadow: 0 8px 22px rgba(214, 51, 108, 0.35) !important;
        transition: all 0.28s cubic-bezier(0.22, 1, 0.36, 1) !important;
        width: 100% !important;
        font-family: 'Nunito', sans-serif !important;
    }

    .stButton > button:hover {
        transform: translateY(-3px) scale(1.015);
        box-shadow: 0 14px 30px rgba(214, 51, 108, 0.5) !important;
        background: linear-gradient(135deg, #ff8fbb, #e03d7a) !important;
    }

    .stButton > button:active {
        transform: translateY(-1px) scale(0.99);
    }

    .footer {
        text-align: center;
        color: #d6336c;
        font-size: 0.85em;
        margin-top: 32px;
        opacity: 0.7;
        font-style: italic;
    }
</style>
""", unsafe_allow_html=True)


# ================== SESSION STATE ==================
if "step" not in st.session_state:
    st.session_state.step = 0

if "pesan_sekarang" not in st.session_state:
    st.session_state.pesan_sekarang = ""

if "sisa_pesan" not in st.session_state:
    pool = kata_nugas.copy()
    random.shuffle(pool)
    st.session_state.sisa_pesan = pool

if "key_pesan" not in st.session_state:
    st.session_state.key_pesan = 0


def ambil_pesan_baru():
    if not st.session_state.sisa_pesan:
        st.session_state.step = 99
        return
    st.session_state.pesan_sekarang = st.session_state.sisa_pesan.pop()
    st.session_state.key_pesan += 1


def reset_semua():
    st.session_state.step = 0
    st.session_state.pesan_sekarang = ""
    st.session_state.key_pesan = 0
    pool = kata_nugas.copy()
    random.shuffle(pool)
    st.session_state.sisa_pesan = pool


# ================== AUDIO ENGINE (SFX + Background Music) ==================
def inject_audio_engine():
    """注入 Web Audio API：背景钢琴曲 + 所有操作的音效"""
    html = """
    <!DOCTYPE html>
    <html><head><style>body{margin:0;background:transparent;overflow:hidden;}</style></head>
    <body>
    <script>
        // ========== 全局 AudioContext ==========
        let audioCtx = null;
        let musicStarted = false;
        let musicTimer = null;

        function getCtx() {
            if (!audioCtx) {
                audioCtx = new (window.AudioContext || window.webkitAudioContext)();
            }
            if (audioCtx.state === 'suspended') {
                audioCtx.resume();
            }
            return audioCtx;
        }

        // ========== 柔和钢琴和弦生成器 ==========
        // 使用正弦波合成柔和、延绵的钢琴感音色
        function playSoftNote(freq, startTime, duration, volume) {
            const ctx = getCtx();
            const o = ctx.createOscillator();
            const g = ctx.createGain();

            o.type = 'sine';
            o.frequency.value = freq;

            // 柔和的 attack + 长 release
            g.gain.setValueAtTime(0.0001, startTime);
            g.gain.exponentialRampToValueAtTime(volume, startTime + 0.08);
            g.gain.exponentialRampToValueAtTime(0.0001, startTime + duration);

            o.connect(g);
            g.connect(ctx.destination);
            o.start(startTime);
            o.stop(startTime + duration + 0.1);
        }

        // 弹奏一个柔和的钢琴和弦（C大调 9 和弦 - 温暖浪漫）
        function playRomanticChord(rootFreq) {
            const ctx = getCtx();
            const now = ctx.currentTime;
            const dur = 3.5;
            // C9 和弦音程：根音、三度、五度、七度、九度
            const intervals = [1, 1.25, 1.5, 1.8, 2.25];
            intervals.forEach((ratio, i) => {
                // 音量略微错开，低音稍响
                const vol = i === 0 ? 0.06 : 0.04 - i * 0.004;
                playSoftNote(rootFreq * ratio, now + i * 0.15, dur, vol);
            });
        }

        // ========== 背景音乐循环 ==========
        // 使用几个柔和的根音循环：C4, A3, F3, G3
        const roots = [261.63, 220.00, 174.61, 196.00];
        let rootIndex = 0;

        function startMusic() {
            if (musicStarted) return;
            musicStarted = true;

            function playLoop() {
                if (!musicStarted) return;
                playRomanticChord(roots[rootIndex]);
                rootIndex = (rootIndex + 1) % roots.length;
                // 每 4 秒换一个和弦
                musicTimer = setTimeout(playLoop, 4000);
            }
            playLoop();
        }

        function stopMusic() {
            musicStarted = false;
            if (musicTimer) {
                clearTimeout(musicTimer);
                musicTimer = null;
            }
        }

        // ========== 音效函数 ==========
        // 1. 开箱"叮"声 - 柔和的高音点击感
        function playBoxOpen() {
            const ctx = getCtx();
            const now = ctx.currentTime;
            const o = ctx.createOscillator();
            const g = ctx.createGain();
            o.type = 'sine';
            o.frequency.setValueAtTime(880, now);
            o.frequency.exponentialRampToValueAtTime(1320, now + 0.1);
            g.gain.setValueAtTime(0.0001, now);
            g.gain.exponentialRampToValueAtTime(0.12, now + 0.02);
            g.gain.exponentialRampToValueAtTime(0.0001, now + 0.4);
            o.connect(g); g.connect(ctx.destination);
            o.start(now); o.stop(now + 0.45);
        }

        // 2. 翻页/新消息"叮咚" - 两个音符
        function playDing() {
            const ctx = getCtx();
            const now = ctx.currentTime;
            [660, 990].forEach((f, i) => {
                const o = ctx.createOscillator();
                const g = ctx.createGain();
                o.type = 'sine';
                o.frequency.value = f;
                const t = now + i * 0.08;
                g.gain.setValueAtTime(0.0001, t);
                g.gain.exponentialRampToValueAtTime(0.1, t + 0.02);
                g.gain.exponentialRampToValueAtTime(0.0001, t + 0.6);
                o.connect(g); g.connect(ctx.destination);
                o.start(t); o.stop(t + 0.65);
            });
        }

        // 3. 惊喜/烟花"叮铃铃" - 上升琶音
        function playSurprise() {
            const ctx = getCtx();
            const now = ctx.currentTime;
            [523.25, 659.25, 783.99, 1046.5].forEach((f, i) => {
                const o = ctx.createOscillator();
                const g = ctx.createGain();
                o.type = 'sine';
                o.frequency.value = f;
                const t = now + i * 0.12;
                g.gain.setValueAtTime(0.0001, t);
                g.gain.exponentialRampToValueAtTime(0.09, t + 0.03);
                g.gain.exponentialRampToValueAtTime(0.0001, t + 1.0);
                o.connect(g); g.connect(ctx.destination);
                o.start(t); o.stop(t + 1.05);
            });
        }

        // 4. 重置"滴" - 简单轻柔
        function playReset() {
            const ctx = getCtx();
            const now = ctx.currentTime;
            const o = ctx.createOscillator();
            const g = ctx.createGain();
            o.type = 'sine';
            o.frequency.value = 440;
            g.gain.setValueAtTime(0.0001, now);
            g.gain.exponentialRampToValueAtTime(0.08, now + 0.02);
            g.gain.exponentialRampToValueAtTime(0.0001, now + 0.3);
            o.connect(g); g.connect(ctx.destination);
            o.start(now); o.stop(now + 0.35);
        }

        // ========== 首次交互时启动所有音频 ==========
        function unlockAudio() {
            getCtx();
            startMusic();
            document.removeEventListener('click', unlockAudio);
            document.removeEventListener('touchstart', unlockAudio);
            document.removeEventListener('keydown', unlockAudio);
        }
        document.addEventListener('click', unlockAudio);
        document.addEventListener('touchstart', unlockAudio);
        document.addEventListener('keydown', unlockAudio);

        // 暴露给 Streamlit 调用
        window.__playBoxOpen = playBoxOpen;
        window.__playDing = playDing;
        window.__playSurprise = playSurprise;
        window.__playReset = playReset;
        window.__startMusic = startMusic;
        window.__stopMusic = stopMusic;
    </script>
    </body></html>
    """
    components.html(html, height=0)


# 在每次 rerun 时注入音频引擎（确保持久存在）
inject_audio_engine()


# ================== 音效触发辅助函数 ==================
def trigger_sfx(sfx_name: str):
    """通过 components 执行 JS 来播放指定音效"""
    js = f"""
    <script>
        (function() {{
            const fn = window.parent['__{sfx_name}'];
            if (typeof fn === 'function') fn();
        }})();
    </script>
    """
    components.html(js, height=0)


# ================== HALAMAN 0: AWAL ==================
if st.session_state.step == 0:
    st.markdown('<div class="judul">Hai, kamu 🌸</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="subjudul">aku nitipin sesuatu di kotak ini. '
        'buka pelan-pelan ya, jangan sekaligus.</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="box-wrap"><div class="box">🎁</div></div>',
        unsafe_allow_html=True
    )

    if st.button("Buka kotaknya 💌"):
        trigger_sfx("playBoxOpen")
        st.session_state.step = 1
        ambil_pesan_baru()
        st.rerun()


# ================== HALAMAN 1: BUKA KOTAK ==================
elif st.session_state.step == 1:
    st.markdown('<div class="judul">Sebuah pesan untukmu</div>', unsafe_allow_html=True)

    st.markdown(
        f'<div class="pesan-card" key="p{st.session_state.key_pesan}">'
        f'{st.session_state.pesan_sekarang}</div>',
        unsafe_allow_html=True
    )

    sisa = len(st.session_state.sisa_pesan)
    total = len(kata_nugas)
    sudah = total - sisa

    st.markdown(
        f'<div class="counter">kotak yang sudah kamu buka — {sudah} dari {total} 🌸</div>',
        unsafe_allow_html=True
    )

    st.markdown("<br>", unsafe_allow_html=True)

    if sisa > 0:
        if st.button("Lanjut, buka kotak berikutnya 🌷"):
            trigger_sfx("playDing")
            ambil_pesan_baru()
            st.rerun()
    else:
        st.markdown(
            '<div class="counter">kotaknya sudah habis... '
            'tapi masih ada satu hal lagi untukmu</div>',
            unsafe_allow_html=True
        )
        if st.button("Buka yang terakhir ✨"):
            trigger_sfx("playSurprise")
            st.session_state.step = 99
            st.rerun()

    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("🔄 Ulang dari awal"):
        trigger_sfx("playReset")
        reset_semua()
        st.rerun()


# ================== HALAMAN 99: SURPRISE ==================
elif st.session_state.step == 99:

    html_surprise = f"""
    <!DOCTYPE html>
    <html>
    <head>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Caveat:wght@600&family=Nunito:wght@400;600;700&display=swap');

        html, body {{
            margin: 0;
            padding: 0;
            background: transparent;
            font-family: 'Nunito', sans-serif;
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

        .petal {{
            position: fixed;
            top: -30px;
            font-size: 18px;
            opacity: 0;
            animation: petalFall linear forwards;
            z-index: 1;
            pointer-events: none;
        }}

        @keyframes petalFall {{
            0% {{ opacity: 0; transform: translateY(-20px) rotate(0deg); }}
            10% {{ opacity: 0.9; }}
            90% {{ opacity: 0.9; }}
            100% {{ opacity: 0; transform: translateY(105vh) rotate(360deg); }}
        }}

        .konten {{
            position: relative;
            z-index: 3;
            background: rgba(255, 255, 255, 0.96);
            border-radius: 26px;
            padding: 40px 34px;
            margin: 24px auto;
            max-width: 640px;
            box-shadow: 0 22px 55px rgba(214, 51, 108, 0.28),
                        0 0 0 3px rgba(255, 179, 204, 0.55);
            text-align: center;
            animation: popIn 1.1s cubic-bezier(0.22, 1, 0.36, 1);
        }}

        @keyframes popIn {{
            0% {{ opacity: 0; transform: scale(0.82) translateY(20px); filter: blur(6px); }}
            60% {{ filter: blur(0); }}
            100% {{ opacity: 1; transform: scale(1) translateY(0); }}
        }}

        .judul-surprise {{
            font-family: 'Caveat', cursive;
            font-size: 2.4em;
            color: #d6336c;
            margin-bottom: 6px;
            letter-spacing: 0.5px;
            animation: heartbeat 2.4s ease-in-out infinite;
        }}

        @keyframes heartbeat {{
            0%, 100% {{ transform: scale(1); }}
            20% {{ transform: scale(1.06); }}
            40% {{ transform: scale(1); }}
            60% {{ transform: scale(1.04); }}
        }}

        .garis {{
            width: 60px;
            height: 3px;
            background: linear-gradient(90deg, transparent, #ff7fae, transparent);
            margin: 14px auto 22px auto;
            border-radius: 3px;
            animation: fadeIn 1.6s ease-out;
        }}

        @keyframes fadeIn {{
            from {{ opacity: 0; width: 0; }}
            to {{ opacity: 1; width: 60px; }}
        }}

        .paragraf {{
            color: #a1255a;
            font-size: 1.06em;
            line-height: 1.95;
            text-align: left;
            font-weight: 500;
            opacity: 0;
            animation: fadeUp 1.4s ease-out 0.6s forwards;
        }}

        @keyframes fadeUp {{
            from {{ opacity: 0; transform: translateY(14px); }}
            to {{ opacity: 1; transform: translateY(0); }}
        }}

        .ttd {{
            margin-top: 28px;
            color: #d6336c;
            font-family: 'Caveat', cursive;
            font-size: 1.5em;
            text-align: right;
            opacity: 0;
            animation: fadeUp 1.4s ease-out 1.6s forwards;
        }}
    </style>
    </head>
    <body>

    <canvas id="fireworks"></canvas>

    <div class="konten">
        <div class="judul-surprise">Untuk kamu 🌸</div>
        <div class="garis"></div>
        <div class="paragraf">{kalimat_penutup}</div>
        <div class="ttd">— dari aku, yang sayang banget sama kamu</div>
    </div>

    <script>
        // ===== PETAL JATUH =====
        const petals = ['🌸','🌷','💗','✨','🩷'];
        function spawnPetal() {{
            const el = document.createElement('div');
            el.className = 'petal';
            el.textContent = petals[Math.floor(Math.random() * petals.length)];
            el.style.left = Math.random() * 100 + 'vw';
            el.style.fontSize = (Math.random() * 8 + 14) + 'px';
            const dur = Math.random() * 5 + 7;
            el.style.animationDuration = dur + 's';
            document.body.appendChild(el);
            setTimeout(() => el.remove(), dur * 1000 + 500);
        }}
        setInterval(spawnPetal, 700);

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
        const colors = [
            '#ff7fae', '#d6336c', '#ffb3cc',
            '#ffd9a0', '#ffe8b0', '#ffffff',
            '#f9a8c9', '#e8879f'
        ];

        function createFirework(x, y) {{
            const count = 45 + Math.floor(Math.random() * 25);
            const baseHue = colors[Math.floor(Math.random() * colors.length)];
            for (let i = 0; i < count; i++) {{
                const angle = (Math.PI * 2 * i) / count + Math.random() * 0.15;
                const speed = Math.random() * 4.5 + 1.8;
                particles.push({{
                    x: x, y: y,
                    vx: Math.cos(angle) * speed,
                    vy: Math.sin(angle) * speed,
                    life: 1,
                    decay: 0.012 + Math.random() * 0.008,
                    color: Math.random() < 0.7 ? baseHue : colors[Math.floor(Math.random()*colors.length)],
                    size: Math.random() * 2.2 + 1.4
                }});
            }}
        }}

        function animate() {{
            ctx.fillStyle = 'rgba(255, 233, 240, 0.18)';
            ctx.fillRect(0, 0, canvas.width, canvas.height);

            for (let i = particles.length - 1; i >= 0; i--) {{
                const p = particles[i];
                p.x += p.vx; p.y += p.vy;
                p.vy += 0.05;
                p.vx *= 0.985; p.vy *= 0.985;
                p.life -= p.decay;

                if (p.life <= 0) {{ particles.splice(i, 1); continue; }}

                ctx.globalAlpha = Math.max(p.life, 0);
                ctx.fillStyle = p.color;
                ctx.beginPath();
                ctx.arc(p.x, p.y, p.size * p.life, 0, Math.PI * 2);
                ctx.fill();
            }}
            ctx.globalAlpha = 1;
            requestAnimationFrame(animate);
        }}
        animate();

        setInterval(() => {{
            createFirework(
                Math.random() * canvas.width,
                Math.random() * canvas.height * 0.6 + 40
            );
        }}, 1400);

        setTimeout(() => createFirework(canvas.width * 0.5, canvas.height * 0.28), 400);
        setTimeout(() => createFirework(canvas.width * 0.28, canvas.height * 0.45), 900);
        setTimeout(() => createFirework(canvas.width * 0.72, canvas.height * 0.38), 1400);
    </script>

    </body>
    </html>
    """

    components.html(html_surprise, height=780, scrolling=False)

    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("🔄 Ulang dari awal ya"):
        trigger_sfx("playReset")
        reset_semua()
        st.rerun()


# ================== FOOTER ==================
st.markdown(
    '<div class="footer">dibuat sambil mikirin kamu terus</div>',
    unsafe_allow_html=True
)
