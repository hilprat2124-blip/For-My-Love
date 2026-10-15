import streamlit as st
import streamlit.components.v1 as components
import random
import base64
import os
import json

# ================== KONFIG ==================
st.set_page_config(
    page_title="Untuk Kamu",
    page_icon="🌸",
    layout="centered"
)

# ================== LOAD SEMUA FOTO ==================
def load_foto_list():
    """Load semua foto di assets/ dengan nama foto.jpg, foto2.jpg, dst."""
    fotos = []
    # Cek foto.jpg
    if os.path.exists("assets/foto.jpg"):
        with open("assets/foto.jpg", "rb") as f:
            fotos.append(base64.b64encode(f.read()).decode())
    # Cek foto2.jpg sampai foto9.jpg
    for i in range(2, 10):
        path = f"assets/foto{i}.jpg"
        if os.path.exists(path):
            with open(path, "rb") as f:
                fotos.append(base64.b64encode(f.read()).decode())
    return fotos

FOTOS = load_foto_list()
print(f"📸 Loaded {len(FOTOS)} foto")

# ================== LOAD LAGU ==================
def find_lagu():
    candidates = ["assets/lagu.mp3", "lagu.mp3", "assets/lagu.MP3", "assets/Lagu.mp3"]
    for path in candidates:
        if os.path.exists(path):
            try:
                with open(path, "rb") as f:
                    data = f.read()
                print(f"✅ Lagu loaded: {path} ({len(data)} bytes)")
                return base64.b64encode(data).decode()
            except Exception as e:
                print(f"❌ Error load {path}: {e}")
    print("❌ lagu.mp3 tidak ditemukan")
    return None

LAGU_B64 = find_lagu()

# ================== KATA SEMANGAT NUGAS ==================
kata_nugas = [
    "Sayang... aku tau kamu capek, tapi aku percaya kamu pasti bisa. Semangat ya, cintakuu.",
    "Aku tau tugas kamu banyak, tapi aku juga tau kamu sekuat itu. Aku bangga banget sama kamu.",
    "Capek boleh, istirahat dulu juga boleh. Kamu nggak harus selalu kuat setiap saat, yaa... Aku tetap bangga sama kamu, apa pun hasilnya.",
    "Coba nugas sambil bayangin aku lagi nemenin kamu, yaa. Anggap aja aku lagi duduk di samping kamu sambil elus kepala kamu. 🤍",
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
    "I LOVE YOU SOOOOOOOOOO MMMMUUUUUUCCCHHHHH SAYANGGG!!!!!!"
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

if "sfx_pending" not in st.session_state:
    st.session_state.sfx_pending = ""

if "sfx_counter" not in st.session_state:
    st.session_state.sfx_counter = 0


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


# =====================================================================
# AUDIO ENGINE
# =====================================================================
def inject_audio_engine():
    if LAGU_B64:
        lagu_src = f"data:audio/mpeg;base64,{LAGU_B64}"
        pakai_mp3 = True
    else:
        lagu_src = ""
        pakai_mp3 = False

    lagu_json = json.dumps(lagu_src)

    html = f"""
    <!DOCTYPE html><html><head><style>body{{margin:0;background:transparent;overflow:hidden;}}</style></head>
    <body>
    <script>
    (function() {{
        const P = window.parent;
        if (P.__loveEngine) return;
        P.__loveEngine = true;
        console.log('[love] Installing audio engine...');

        const PAKAI_MP3 = {str(pakai_mp3).lower()};
        const LAGU_DATA = {lagu_json};

        const AudioCtx = P.AudioContext || P.webkitAudioContext;
        P.__loveCtx = new AudioCtx();
        P.__lastSfxId = null;
        P.__musicStarted = false;
        P.__loveMusicEnabled = true;

        function makeReverbIR(ctx, duration, decay) {{
            const rate = ctx.sampleRate;
            const length = rate * duration;
            const impulse = ctx.createBuffer(2, length, rate);
            for (let ch = 0; ch < 2; ch++) {{
                const data = impulse.getChannelData(ch);
                for (let i = 0; i < length; i++) {{
                    data[i] = (Math.random() * 2 - 1) * Math.pow(1 - i / length, decay);
                }}
            }}
            return impulse;
        }}

        const reverbIR = makeReverbIR(P.__loveCtx, 4.5, 2.5);
        const reverb = P.__loveCtx.createConvolver();
        reverb.buffer = reverbIR;

        const reverbGain = P.__loveCtx.createGain();
        reverbGain.gain.value = 0.45;

        const masterGain = P.__loveCtx.createGain();
        masterGain.gain.value = 0.7;

        reverb.connect(reverbGain);
        reverbGain.connect(masterGain);
        masterGain.connect(P.__loveCtx.destination);

        P.__loveMaster = masterGain;
        P.__loveReverb = reverb;

        let audioEl = P.document.getElementById('loveGlobalAudio');
        if (!audioEl) {{
            audioEl = P.document.createElement('audio');
            audioEl.id = 'loveGlobalAudio';
            audioEl.loop = true;
            audioEl.preload = 'auto';
            audioEl.style.display = 'none';
            P.document.body.appendChild(audioEl);
        }}
        P.__loveAudioEl = audioEl;

        if (PAKAI_MP3 && LAGU_DATA && !audioEl.src) {{
            audioEl.src = LAGU_DATA;
            console.log('[love] MP3 src set');
        }}

        P.__sfxVolume = 0.85;
        P.__musicVolume = 0.6;

        function playPiano(freq, startTime, duration, volume) {{
            const ctx = P.__loveCtx;
            if (ctx.state === 'suspended') ctx.resume().catch(()=>{{}});

            const harmonics = [
                {{ mult: 1, gain: 1.0,  type: 'sine' }},
                {{ mult: 2, gain: 0.42, type: 'sine' }},
                {{ mult: 3, gain: 0.18, type: 'sine' }},
                {{ mult: 4, gain: 0.08, type: 'sine' }},
            ];

            harmonics.forEach(h => {{
                const o = ctx.createOscillator();
                const g = ctx.createGain();
                o.type = h.type;
                o.frequency.value = freq * h.mult;

                const amp = volume * h.gain;
                g.gain.setValueAtTime(0.0001, startTime);
                g.gain.exponentialRampToValueAtTime(amp, startTime + 0.02);
                g.gain.exponentialRampToValueAtTime(amp * 0.7, startTime + 0.2);
                g.gain.exponentialRampToValueAtTime(amp * 0.3, startTime + duration * 0.5);
                g.gain.exponentialRampToValueAtTime(0.0001, startTime + duration);

                o.connect(g);
                const dry = ctx.createGain();
                dry.gain.value = 0.55;
                g.connect(dry);
                dry.connect(masterGain);
                const wet = ctx.createGain();
                wet.gain.value = 0.55;
                g.connect(wet);
                wet.connect(reverb);

                o.start(startTime);
                o.stop(startTime + duration + 0.1);
            }});
        }}

        const bassLine = [130.81, 164.81, 174.61, 196.00];
        const arpChords = [
            [261.63, 329.63, 392.00, 493.88],
            [329.63, 392.00, 493.88, 587.33],
            [349.23, 440.00, 523.25, 659.25],
            [392.00, 523.25, 587.33, 698.46],
        ];
        const melodyPhrases = [
            [523.25, 659.25, 783.99, 659.25],
            [587.33, 659.25, 783.99, 987.77],
            [880.00, 783.99, 698.46, 659.25],
            [587.33, 659.25, 587.33, 523.25],
        ];
        let synthStep = 0;
        let synthRunning = false;
        let synthTimer = null;

        function playMeasure(atTime) {{
            const vol = P.__musicVolume;
            const barIdx = synthStep % 4;
            playPiano(bassLine[barIdx], atTime, 4.2, 0.30 * vol);
            const arp = arpChords[barIdx];
            for (let i = 0; i < arp.length; i++) {{
                playPiano(arp[i], atTime + i * 0.85, 2.0, 0.14 * vol);
            }}
            const phrase = melodyPhrases[barIdx];
            for (let i = 0; i < 4; i++) {{
                const note = phrase[i];
                playPiano(note, atTime + i * 0.85 + 0.1, 2.2, 0.20 * vol);
                playPiano(note * 2, atTime + i * 0.85 + 0.15, 1.4, 0.045 * vol);
            }}
            synthStep++;
        }}

        function startSynth() {{
            if (synthRunning) return;
            synthRunning = true;
            function loop() {{
                if (!synthRunning || !P.__loveMusicEnabled) return;
                playMeasure(P.__loveCtx.currentTime + 0.05);
                synthTimer = setTimeout(loop, 3400);
            }}
            loop();
        }}

        function stopSynth() {{
            synthRunning = false;
            if (synthTimer) {{ clearTimeout(synthTimer); synthTimer = null; }}
        }}

        function sfxPop() {{
            const now = P.__loveCtx.currentTime;
            playPiano(880, now, 1.0, 0.55 * P.__sfxVolume);
            playPiano(1318.51, now + 0.08, 1.1, 0.45 * P.__sfxVolume);
        }}
        function sfxDing() {{
            const now = P.__loveCtx.currentTime;
            [1174.66, 1479.98, 1760.00].forEach((f, i) => {{
                playPiano(f, now + i * 0.07, 1.4, 0.38 * P.__sfxVolume);
            }});
        }}
        function sfxChime() {{
            const now = P.__loveCtx.currentTime;
            [587.33, 739.99, 880.00, 1174.66, 1479.98, 1760.00].forEach((f, i) => {{
                playPiano(f, now + i * 0.12, 2.0, 0.35 * P.__sfxVolume);
            }});
        }}
        function sfxReset() {{
            const now = P.__loveCtx.currentTime;
            [880, 659.25, 440].forEach((f, i) => {{
                playPiano(f, now + i * 0.1, 1.0, 0.38 * P.__sfxVolume);
            }});
        }}

        P.__lovePlaySfx = function(name, id) {{
            console.log('[love] __lovePlaySfx:', name, 'id:', id);
            if (id !== undefined && id !== null && id === P.__lastSfxId) return;
            P.__lastSfxId = id;
            if (P.__loveCtx.state === 'suspended') P.__loveCtx.resume().catch(()=>{{}});
            try {{
                if (name === 'pop') sfxPop();
                else if (name === 'ding') sfxDing();
                else if (name === 'chime') sfxChime();
                else if (name === 'reset') sfxReset();
            }} catch(e) {{ console.error('[love] SFX error:', e); }}
        }};

        P.__loveStartMusic = function() {{
            if (P.__musicStarted) return;
            if (!P.__loveMusicEnabled) return;
            if (P.__loveCtx.state === 'suspended') P.__loveCtx.resume().catch(()=>{{}});

            if (PAKAI_MP3 && audioEl && audioEl.src) {{
                audioEl.volume = 0.5;
                const p = audioEl.play();
                if (p && p.then) {{
                    p.then(() => {{
                        P.__musicStarted = true;
                        console.log('[love] ✅ MP3 playing');
                    }}).catch(err => console.warn('[love] MP3 blocked:', err.name));
                }}
            }} else {{
                startSynth();
                P.__musicStarted = true;
                console.log('[love] ✅ Synth playing');
            }}
        }};

        P.__loveToggleMusic = function() {{
            if (P.__loveMusicEnabled) {{
                P.__loveMusicEnabled = false;
                if (audioEl) try {{ audioEl.pause(); }} catch(e) {{}}
                stopSynth();
                P.__musicStarted = false;
            }} else {{
                P.__loveMusicEnabled = true;
                P.__loveStartMusic();
            }}
            return P.__loveMusicEnabled;
        }};

        P.__loveStartMusic();

        ['click','keydown','touchstart','mousedown','pointerdown','scroll'].forEach(ev => {{
            P.document.addEventListener(ev, function() {{
                if (P.__loveCtx.state === 'suspended') P.__loveCtx.resume().catch(()=>{{}});
                if (!P.__musicStarted) P.__loveStartMusic();
            }}, {{ capture: true, passive: true }});
        }});

        let retry = 0;
        const iv = setInterval(() => {{
            retry++;
            if (P.__musicStarted) {{ clearInterval(iv); return; }}
            if (retry > 30) {{ clearInterval(iv); return; }}
            if (P.__loveCtx.state === 'running') P.__loveStartMusic();
            else P.__loveCtx.resume().catch(()=>{{}});
        }}, 1000);

        console.log('[love] Audio engine installed.');
    }})();
    </script>
    </body></html>
    """
    components.html(html, height=0)


# =====================================================================
# TRIGGER SFX
# =====================================================================
def trigger_sfx(sfx_name: str, sfx_id: int):
    if not sfx_name:
        return
    html = f"""
    <!DOCTYPE html><html><head><style>body{{margin:0;background:transparent;}}</style></head>
    <body>
    <script>
    (function() {{
        const name = '{sfx_name}';
        const id = {sfx_id};
        const P = window.parent;

        function fire() {{
            if (P && typeof P.__lovePlaySfx === 'function') {{
                P.__lovePlaySfx(name, id);
                return true;
            }}
            return false;
        }}

        let tries = 0;
        if (!fire()) {{
            const iv = setInterval(() => {{
                tries++;
                if (fire() || tries >= 30) clearInterval(iv);
            }}, 50);
        }}
    }})();
    </script>
    </body></html>
    """
    components.html(html, height=0)


# =====================================================================
# MUSIC PLAYER UI
# =====================================================================
def render_music_ui():
    html = """
    <!DOCTYPE html><html><head>
    <style>
        body { margin:0; padding:0; background:transparent; overflow:hidden; }
        #musicBtn {
            position: fixed;
            top: 12px; right: 12px;
            background: rgba(255,255,255,0.95);
            border: 2px solid #ffb3cc;
            color: #d6336c;
            border-radius: 999px;
            padding: 8px 16px;
            font-size: 13px;
            font-weight: 700;
            cursor: pointer;
            box-shadow: 0 4px 14px rgba(214,51,108,0.3);
            z-index: 999999;
            font-family: 'Nunito', sans-serif;
            transition: transform 0.2s;
        }
        #musicBtn:hover { transform: scale(1.06); background:#fff; }
    </style>
    </head>
    <body>
    <button id="musicBtn">🔊 Musik</button>
    <script>
        const btn = document.getElementById('musicBtn');
        const P = window.parent;
        function refresh() {
            if (typeof P.__loveMusicEnabled !== 'undefined') {
                btn.textContent = P.__loveMusicEnabled ? '🔊 Musik' : '🔇 Musik';
            }
        }
        btn.addEventListener('click', (e) => {
            e.stopPropagation();
            if (typeof P.__loveToggleMusic === 'function') {
                P.__loveToggleMusic();
                setTimeout(refresh, 150);
            }
        });
        setInterval(refresh, 1000);
        refresh();
    </script>
    </body></html>
    """
    components.html(html, height=0)


# =====================================================================
# EFEK GLOBAL
# =====================================================================
def inject_global_effects():
    html = """
    <!DOCTYPE html><html><head><style>body{margin:0;background:transparent;overflow:hidden;}</style></head>
    <body>
    <script>
    (function() {
        const P = window.parent;
        if (P.__loveGlobalEffects) return;
        P.__loveGlobalEffects = true;

        const container = P.document.createElement('div');
        container.id = 'love-effects-layer';
        container.style.cssText = 'position:fixed;top:0;left:0;width:100vw;height:100vh;pointer-events:none;z-index:9990;overflow:hidden;';
        P.document.body.appendChild(container);

        const style = P.document.createElement('style');
        style.textContent = `
            @keyframes lovePetalFall {
                0%   { transform: translateY(-10vh) translateX(0) rotate(0deg); opacity: 0; }
                10%  { opacity: 0.85; }
                50%  { transform: translateY(45vh) translateX(30px) rotate(180deg); opacity: 0.9; }
                90%  { opacity: 0.7; }
                100% { transform: translateY(110vh) translateX(-30px) rotate(360deg); opacity: 0; }
            }
            @keyframes loveTwinkle {
                0%, 100% { transform: scale(0.6) rotate(0deg); opacity: 0.3; }
                50%      { transform: scale(1.15) rotate(20deg); opacity: 1; }
            }
            @keyframes loveFloat {
                0%, 100% { transform: translateY(0) translateX(0); opacity: 0.6; }
                50%      { transform: translateY(-25px) translateX(15px); opacity: 0.9; }
            }
            .love-petal, .love-twinkle, .love-float {
                position: absolute;
                pointer-events: none;
                user-select: none;
                will-change: transform, opacity;
            }
            .love-petal { font-size: 20px; animation: lovePetalFall linear infinite; }
            .love-twinkle { font-size: 14px; animation: loveTwinkle ease-in-out infinite; }
            .love-float { font-size: 22px; animation: loveFloat ease-in-out infinite; }
        `;
        P.document.head.appendChild(style);

        const petalEmojis = ['🌸','🌷','💗','✨','🩷','💖','🌺','💕'];
        function createPetal() {
            const el = P.document.createElement('div');
            el.className = 'love-petal';
            el.textContent = petalEmojis[Math.floor(Math.random() * petalEmojis.length)];
            el.style.left = Math.random() * 100 + 'vw';
            el.style.fontSize = (Math.random() * 10 + 14) + 'px';
            const dur = Math.random() * 8 + 9;
            el.style.animationDuration = dur + 's';
            el.style.animationDelay = (Math.random() * 5) + 's';
            container.appendChild(el);
        }
        for (let i = 0; i < 18; i++) createPetal();

        const twinkleEmojis = ['✨','⭐','💫','✦'];
        function createTwinkle() {
            const el = P.document.createElement('div');
            el.className = 'love-twinkle';
            el.textContent = twinkleEmojis[Math.floor(Math.random() * twinkleEmojis.length)];
            el.style.left = Math.random() * 100 + 'vw';
            el.style.top = Math.random() * 100 + 'vh';
            el.style.fontSize = (Math.random() * 8 + 10) + 'px';
            el.style.animationDuration = (Math.random() * 2 + 1.5) + 's';
            el.style.animationDelay = (Math.random() * 3) + 's';
            container.appendChild(el);
        }
        for (let i = 0; i < 14; i++) createTwinkle();

        const floatEmojis = ['💕','💗','🩷','💖','🌸'];
        function createFloat() {
            const el = P.document.createElement('div');
            el.className = 'love-float';
            el.textContent = floatEmojis[Math.floor(Math.random() * floatEmojis.length)];
            el.style.left = Math.random() * 100 + 'vw';
            el.style.top = Math.random() * 100 + 'vh';
            el.style.fontSize = (Math.random() * 12 + 18) + 'px';
            el.style.animationDuration = (Math.random() * 3 + 3) + 's';
            el.style.animationDelay = (Math.random() * 2) + 's';
            el.style.opacity = (Math.random() * 0.3 + 0.4);
            container.appendChild(el);
        }
        for (let i = 0; i < 8; i++) createFloat();

        setInterval(() => {
            const oldTwinkles = container.querySelectorAll('.love-twinkle');
            oldTwinkles.forEach((el, i) => { if (i % 2 === 0) el.remove(); });
            for (let i = 0; i < 7; i++) createTwinkle();
        }, 8000);

        P.__loveFireworksFullScreen = function() {
            const existing = P.document.getElementById('love-fw-canvas');
            if (existing) existing.remove();

            const fw = P.document.createElement('canvas');
            fw.id = 'love-fw-canvas';
            fw.style.cssText = 'position:fixed;top:0;left:0;width:100vw;height:100vh;pointer-events:none;z-index:9989;';
            fw.width = P.innerWidth;
            fw.height = P.innerHeight;
            P.document.body.appendChild(fw);

            const ctx = fw.getContext('2d');
            const particles = [];
            const colors = ['#ff7fae','#d6336c','#ffb3cc','#ffd9a0','#ffe8b0','#ffffff','#f9a8c9','#e8879f'];

            function createFirework(x, y) {
                const count = 60 + Math.floor(Math.random() * 30);
                const baseHue = colors[Math.floor(Math.random() * colors.length)];
                for (let i = 0; i < count; i++) {
                    const angle = (Math.PI * 2 * i) / count + Math.random() * 0.2;
                    const speed = Math.random() * 6 + 2;
                    particles.push({
                        x, y,
                        vx: Math.cos(angle) * speed,
                        vy: Math.sin(angle) * speed,
                        life: 1,
                        decay: 0.010 + Math.random() * 0.008,
                        color: Math.random() < 0.7 ? baseHue : colors[Math.floor(Math.random()*colors.length)],
                        size: Math.random() * 2.8 + 1.8
                    });
                }
            }

            let active = true;
            function animate() {
                ctx.fillStyle = 'rgba(255, 233, 240, 0.14)';
                ctx.fillRect(0, 0, fw.width, fw.height);
                for (let i = particles.length - 1; i >= 0; i--) {
                    const p = particles[i];
                    p.x += p.vx; p.y += p.vy;
                    p.vy += 0.045;
                    p.vx *= 0.985; p.vy *= 0.985;
                    p.life -= p.decay;
                    if (p.life <= 0) { particles.splice(i, 1); continue; }
                    ctx.globalAlpha = Math.max(p.life, 0);
                    ctx.fillStyle = p.color;
                    ctx.beginPath();
                    ctx.arc(p.x, p.y, p.size * p.life, 0, Math.PI * 2);
                    ctx.fill();
                }
                ctx.globalAlpha = 1;
                if (active || particles.length > 0) {
                    requestAnimationFrame(animate);
                } else {
                    fw.remove();
                }
            }
            animate();

            const start = Date.now();
            const interval = setInterval(() => {
                if (Date.now() - start > 12000) {
                    clearInterval(interval);
                    active = false;
                    return;
                }
                createFirework(
                    Math.random() * fw.width,
                    Math.random() * fw.height * 0.7 + 50
                );
            }, 400);

            setTimeout(() => createFirework(fw.width * 0.5, fw.height * 0.3), 200);
            setTimeout(() => createFirework(fw.width * 0.25, fw.height * 0.45), 500);
            setTimeout(() => createFirework(fw.width * 0.75, fw.height * 0.4), 800);
        };

        P.addEventListener('message', function(ev) {
            if (ev.data && ev.data.__loveFireworks) {
                P.__loveFireworksFullScreen();
            }
        });
    })();
    </script>
    </body></html>
    """
    components.html(html, height=0)


def trigger_fireworks():
    html = """
    <!DOCTYPE html><html><head><style>body{margin:0;background:transparent;}</style></head>
    <body>
    <script>
    (function() {
        const P = window.parent;
        if (typeof P.__loveFireworksFullScreen === 'function') {
            P.__loveFireworksFullScreen();
        }
    })();
    </script>
    </body></html>
    """
    components.html(html, height=0)


# ================== PASANG SEMUA ==================
inject_audio_engine()
inject_global_effects()
render_music_ui()

if st.session_state.sfx_pending:
    trigger_sfx(st.session_state.sfx_pending, st.session_state.sfx_counter)
    st.session_state.sfx_pending = ""


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
        st.session_state.step = 1
        ambil_pesan_baru()
        st.session_state.sfx_pending = "pop"
        st.session_state.sfx_counter += 1
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
            ambil_pesan_baru()
            st.session_state.sfx_pending = "ding"
            st.session_state.sfx_counter += 1
            st.rerun()
    else:
        st.markdown(
            '<div class="counter">kotaknya sudah habis... '
            'tapi masih ada satu hal lagi untukmu</div>',
            unsafe_allow_html=True
        )
        if st.button("Buka yang terakhir ✨"):
            st.session_state.step = 99
            st.session_state.sfx_pending = "chime"
            st.session_state.sfx_counter += 1
            st.rerun()

    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("🔄 Ulang dari awal"):
        reset_semua()
        st.session_state.sfx_pending = "reset"
        st.session_state.sfx_counter += 1
        st.rerun()


# ================== HALAMAN 99: SURPRISE ==================
elif st.session_state.step == 99:

    trigger_fireworks()

    # ================================================================
    # FOTO HTML — pakai FRAME PORTRAIT biar sesuai foto photobooth 2:3
    # ================================================================
    if FOTOS:
        # Kalau ada banyak foto, tampilkan dalam grid/scroll
        foto_items = []
        for i, f_b64 in enumerate(FOTOS):
            rotate = -2.5 if i % 2 == 0 else 2.0  # selang-seling rotasi
            foto_items.append(f'''
                <div class="foto-frame" style="transform: rotate({rotate}deg);">
                    <div class="foto-inner">
                        <img src="data:image/jpeg;base64,{f_b64}" alt="Kita berdua" />
                    </div>
                    <div class="foto-caption">momen kita #{i+1} 💕</div>
                </div>
            ''')

        # Kalau cuma 1 foto, gedein
        if len(FOTOS) == 1:
            foto_html = f'''
            <div class="foto-frame foto-single">
                <div class="foto-inner">
                    <img src="data:image/jpeg;base64,{FOTOS[0]}" alt="Kita berdua" />
                </div>
                <div class="foto-caption">kita, dan semua momen kecil ini 💕</div>
            </div>
            '''
        else:
            # Multiple foto — grid
            foto_html = '<div class="foto-grid">' + ''.join(foto_items) + '</div>'
    else:
        foto_html = '''
        <div class="foto-frame foto-placeholder">
            <div class="foto-inner">
                <div style="display:flex;align-items:center;justify-content:center;
                            height:100%;color:#d6336c;font-size:0.9em;
                            text-align:center;padding:20px;">
                    (taruh foto kalian di<br>assets/foto.jpg ya 💕)
                </div>
            </div>
        </div>
        '''

    html_surprise = f"""
    <!DOCTYPE html>
    <html>
    <head>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Caveat:wght@600&family=Nunito:wght@400;600;700&display=swap');
        html, body {{ margin:0; padding:0; background:transparent; font-family:'Nunito',sans-serif; overflow:hidden; }}

        .konten {{
            position:relative; z-index:3;
            background:rgba(255,255,255,0.96);
            border-radius:26px;
            padding:36px 24px 30px 24px;
            margin:16px auto;
            max-width:680px;
            box-shadow:0 22px 55px rgba(214,51,108,0.28),
                       0 0 0 3px rgba(255,179,204,0.55);
            text-align:center;
            animation:popIn 1.1s cubic-bezier(0.22,1,0.36,1);
        }}
        @keyframes popIn {{
            0% {{ opacity:0; transform:scale(0.82) translateY(20px); filter:blur(6px); }}
            60% {{ filter:blur(0); }}
            100% {{ opacity:1; transform:scale(1) translateY(0); }}
        }}

        /* ============ FOTO FRAME — PORTRAIT (sesuai photobooth 2:3) ============ */
        .foto-grid {{
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
            gap: 20px 18px;
            margin: 20px 0 24px 0;
        }}

        .foto-frame {{
            display: inline-block;
            background: #fff;
            padding: 12px 12px 44px 12px;
            border-radius: 3px;
            box-shadow:
                0 14px 38px rgba(214, 51, 108, 0.32),
                0 4px 10px rgba(0,0,0,0.08),
                inset 0 0 0 1px rgba(255, 179, 204, 0.5);
            margin: 0;
            position: relative;
            transition: transform 0.4s ease;
            animation: fotoIn 1.1s cubic-bezier(0.22, 1, 0.36, 1) both;
        }}
        .foto-frame:hover {{ transform: rotate(0deg) scale(1.03) !important; }}

        @keyframes fotoIn {{
            0% {{ opacity:0; transform: rotate(-8deg) scale(0.7) translateY(30px); }}
            100% {{ opacity:1; }}
        }}

        /* Washi tape di atas frame */
        .foto-frame::before {{
            content: "";
            position: absolute;
            top: -11px; left: 50%;
            transform: translateX(-50%) rotate(-3deg);
            width: 80px; height: 22px;
            background: linear-gradient(135deg, rgba(255,179,204,0.85), rgba(255,143,187,0.85));
            border-radius: 2px;
            box-shadow: 0 2px 6px rgba(214,51,108,0.25);
            opacity: 0.92;
        }}

        /* Kotak foto — PORTRAIT 2:3 */
        .foto-inner {{
            width: 240px;        /* lebar tetap */
            height: 360px;       /* tinggi = 1.5× lebar (rasio 2:3) */
            overflow: hidden;
            background: linear-gradient(135deg, #ffe9f0, #ffd9e6);
            border-radius: 2px;
            position: relative;
        }}
        .foto-inner img {{
            width: 100%;
            height: 100%;
            object-fit: cover;         /* Penuhi frame tanpa distorsi */
            object-position: center;   /* Center crop */
            display: block;
            filter: saturate(1.05) contrast(1.02) brightness(1.03);
        }}

        /* Single foto — lebih besar */
        .foto-frame.foto-single .foto-inner {{
            width: 320px;
            height: 480px;
        }}

        .foto-caption {{
            position: absolute;
            bottom: 10px; left: 0; right: 0;
            text-align: center;
            font-family: 'Caveat', cursive;
            font-size: 1.15em;
            color: #d6336c;
            letter-spacing: 0.3px;
        }}

        .foto-frame::after {{
            content: "💕";
            position: absolute;
            bottom: 12px; right: 14px;
            font-size: 16px;
            opacity: 0.85;
            animation: heartbeat 2s ease-in-out infinite;
        }}

        @keyframes heartbeat {{
            0%, 100% {{ transform: scale(1); }}
            50% {{ transform: scale(1.18); }}
        }}

        /* HP — responsive */
        @media (max-width: 500px) {{
            .foto-inner {{
                width: 200px;
                height: 300px;
            }}
            .foto-frame.foto-single .foto-inner {{
                width: 260px;
                height: 390px;
            }}
            .foto-grid {{
                gap: 14px 10px;
            }}
        }}

        /* ============ JUDUL & PARAGRAF ============ */
        .judul-surprise {{
            font-family:'Caveat', cursive;
            font-size:2.4em;
            color:#d6336c;
            margin-bottom:6px;
            letter-spacing:0.5px;
            animation:heartbeat 2.4s ease-in-out infinite;
        }}

        .garis {{
            width:60px; height:3px;
            background:linear-gradient(90deg, transparent, #ff7fae, transparent);
            margin:14px auto 22px auto;
            border-radius:3px;
            animation:fadeIn 1.6s ease-out;
        }}
        @keyframes fadeIn {{ from {{ opacity:0; width:0; }} to {{ opacity:1; width:60px; }} }}

        .paragraf {{
            color:#a1255a;
            font-size:1.04em;
            line-height:1.9;
            text-align:left;
            font-weight:500;
            opacity:0;
            animation:fadeUp 1.4s ease-out 1.2s forwards;
        }}
        @keyframes fadeUp {{
            from {{ opacity:0; transform:translateY(14px); }}
            to {{ opacity:1; transform:translateY(0); }}
        }}
        .ttd {{
            margin-top:24px;
            color:#d6336c;
            font-family:'Caveat', cursive;
            font-size:1.5em;
            text-align:right;
            opacity:0;
            animation:fadeUp 1.4s ease-out 2.2s forwards;
        }}
    </style>
    </head>
    <body>
    <div class="konten">
        <div class="judul-surprise">Untuk kamu 🌸</div>
        <div class="garis"></div>
        {foto_html}
        <div class="paragraf">{kalimat_penutup}</div>
        <div class="ttd">— dari aku, yang sayang banget sama kamu</div>
    </div>
    </body>
    </html>
    """

    components.html(html_surprise, height=1400, scrolling=False)

    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("🔄 Ulang dari awal ya"):
        reset_semua()
        st.session_state.sfx_pending = "reset"
        st.session_state.sfx_counter += 1
        st.rerun()


# ================== FOOTER ==================
st.markdown(
    '<div class="footer">dibuat sambil mikirin kamu terus</div>',
    unsafe_allow_html=True
)
