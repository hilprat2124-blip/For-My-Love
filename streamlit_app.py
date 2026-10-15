import streamlit as st
import streamlit.components.v1 as components
import random
import base64
import os

# ================== KONFIG ==================
st.set_page_config(
    page_title="Untuk Kamu",
    page_icon="🌸",
    layout="centered"
)

# ================== LOAD FOTO ==================
FOTO_PATH = "assets/foto.jpg"

def load_foto_base64():
    if os.path.exists(FOTO_PATH):
        try:
            with open(FOTO_PATH, "rb") as f:
                return base64.b64encode(f.read()).decode()
        except Exception as e:
            print(f"Error load foto: {e}")
    return None

FOTO_B64 = load_foto_base64()

# ================== LOAD LAGU ==================
LAGU_PATH = "assets/lagu.mp3"

def load_lagu_base64():
    if os.path.exists(LAGU_PATH):
        try:
            with open(LAGU_PATH, "rb") as f:
                data = f.read()
            print(f"✅ Lagu loaded: {len(data)} bytes")
            return base64.b64encode(data).decode()
        except Exception as e:
            print(f"❌ Error load lagu: {e}")
    else:
        print(f"❌ File tidak ditemukan: {LAGU_PATH}")
    return None

LAGU_B64 = load_lagu_base64()

# Cek juga kalau lagu.mp3 di root (bukan di assets/)
if not LAGU_B64 and os.path.exists("lagu.mp3"):
    with open("lagu.mp3", "rb") as f:
        LAGU_B64 = base64.b64encode(f.read()).decode()
    print("✅ Lagu loaded dari root folder")

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

if "sfx" not in st.session_state:
    st.session_state.sfx = ""

if "sfx_id" not in st.session_state:
    st.session_state.sfx_id = 0


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
# AUDIO PLAYER — pakai pendekatan PALING SEDERHANA
# Audio element ada di iframe yang SAMA, gak perlu cari di parent
# =====================================================================
def render_music_player():
    """Audio player yang sticky & persist. Pakai iframe sendiri."""

    if LAGU_B64:
        lagu_embed = f'data:audio/mp3;base64,{LAGU_B64}'
        pakai_mp3 = True
    else:
        lagu_embed = ""
        pakai_mp3 = False

    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
    <style>
        * {{ margin:0; padding:0; box-sizing:border-box; }}
        body {{
            background: transparent;
            font-family: 'Nunito', sans-serif;
            overflow: hidden;
        }}
        #musicUI {{
            position: fixed;
            top: 12px;
            right: 12px;
            z-index: 99999;
            display: flex;
            align-items: center;
            gap: 8px;
        }}
        #musicBtn {{
            background: rgba(255,255,255,0.95);
            border: 2px solid #ffb3cc;
            color: #d6336c;
            border-radius: 999px;
            padding: 8px 16px;
            font-size: 13px;
            font-weight: 700;
            cursor: pointer;
            box-shadow: 0 4px 14px rgba(214,51,108,0.3);
            font-family: 'Nunito', sans-serif;
            transition: transform 0.2s;
        }}
        #musicBtn:hover {{ transform: scale(1.06); background:#fff; }}

        #unlockOverlay {{
            position: fixed;
            inset: 0;
            background: rgba(255, 200, 220, 0.85);
            backdrop-filter: blur(8px);
            z-index: 99998;
            display: flex;
            align-items: center;
            justify-content: center;
            flex-direction: column;
            gap: 18px;
            cursor: pointer;
            animation: fadeIn 0.4s ease-out;
        }}
        @keyframes fadeIn {{
            from {{ opacity: 0; }}
            to {{ opacity: 1; }}
        }}
        #unlockOverlay .emoji {{
            font-size: 80px;
            animation: heartbeat 1.5s ease-in-out infinite;
        }}
        @keyframes heartbeat {{
            0%, 100% {{ transform: scale(1); }}
            50% {{ transform: scale(1.15); }}
        }}
        #unlockOverlay .text {{
            color: #d6336c;
            font-size: 16px;
            font-weight: 700;
            text-align: center;
            padding: 0 20px;
            line-height: 1.5;
        }}
        #unlockOverlay .sub {{
            color: #e0709a;
            font-size: 13px;
            font-style: italic;
        }}
        #unlockOverlay.hidden {{
            display: none;
        }}
    </style>
    </head>
    <body>

    <audio id="musicEl" loop preload="auto"></audio>

    <div id="musicUI">
        <button id="musicBtn">🔊 Musik</button>
    </div>

    <div id="unlockOverlay">
        <div class="emoji">🎵</div>
        <div class="text">
            Tap di mana saja untuk memulai musik & pengalaman 💕
        </div>
        <div class="sub">(browser butuh 1x sentuhan untuk memutar musik)</div>
    </div>

    <script>
        (function() {{
            const PAKAI_MP3 = {str(pakai_mp3).lower()};
            const LAGU_DATA = "{lagu_embed}";

            const audioEl = document.getElementById('musicEl');
            const btn = document.getElementById('musicBtn');
            const overlay = document.getElementById('unlockOverlay');

            let musicEnabled = true;
            let musicStarted = false;
            let audioCtx = null;
            let lastSfxId = null;

            // ============ SET SUMBER LAGU ============
            if (PAKAI_MP3 && LAGU_DATA) {{
                audioEl.src = LAGU_DATA;
                console.log('[love] MP3 source set, length:', LAGU_DATA.length);
            }} else {{
                console.log('[love] No MP3, using synth fallback.');
            }}

            // ============ AUDIO CONTEXT (untuk SFX & synth) ============
            function getCtx() {{
                if (!audioCtx) {{
                    audioCtx = new (window.AudioContext || window.webkitAudioContext)();
                }}
                if (audioCtx.state === 'suspended') {{
                    audioCtx.resume().catch(()=>{{}});
                }}
                return audioCtx;
            }}

            // ============ REVERB ============
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

            let masterGain = null;
            let reverbNode = null;

            function initReverb() {{
                if (masterGain) return;
                const ctx = getCtx();
                const reverbIR = makeReverbIR(ctx, 4.5, 2.5);
                reverbNode = ctx.createConvolver();
                reverbNode.buffer = reverbIR;
                const reverbGain = ctx.createGain();
                reverbGain.gain.value = 0.45;
                masterGain = ctx.createGain();
                masterGain.gain.value = 0.7;
                reverbNode.connect(reverbGain);
                reverbGain.connect(masterGain);
                masterGain.connect(ctx.destination);
            }}

            // ============ PIANO SYNTH (untuk SFX & fallback musik) ============
            const SFX_VOLUME = 0.7;
            const MUSIC_VOLUME = 0.55;

            function playPiano(freq, startTime, duration, volume) {{
                const ctx = getCtx();
                initReverb();

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

                    const dryGain = ctx.createGain();
                    dryGain.gain.value = 0.55;
                    g.connect(dryGain);
                    dryGain.connect(masterGain);

                    const wetGain = ctx.createGain();
                    wetGain.gain.value = 0.55;
                    g.connect(wetGain);
                    wetGain.connect(reverbNode);

                    o.start(startTime);
                    o.stop(startTime + duration + 0.1);
                }});
            }}

            // ============ FALLBACK: SYNTH MUSIC ============
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
                const vol = MUSIC_VOLUME;
                const barIdx = synthStep % 4;
                const baseTime = atTime;

                playPiano(bassLine[barIdx], baseTime, 4.2, 0.30 * vol);
                const arp = arpChords[barIdx];
                for (let i = 0; i < arp.length; i++) {{
                    playPiano(arp[i], baseTime + i * 0.85, 2.0, 0.14 * vol);
                }}
                const phrase = melodyPhrases[barIdx];
                for (let i = 0; i < 4; i++) {{
                    const note = phrase[i];
                    playPiano(note, baseTime + i * 0.85 + 0.1, 2.2, 0.20 * vol);
                    playPiano(note * 2, baseTime + i * 0.85 + 0.15, 1.4, 0.045 * vol);
                }}
                synthStep++;
            }}

            function startSynth() {{
                if (synthRunning) return;
                synthRunning = true;
                function loop() {{
                    if (!synthRunning || !musicEnabled) return;
                    const ctx = getCtx();
                    playMeasure(ctx.currentTime + 0.05);
                    synthTimer = setTimeout(loop, 3400);
                }}
                loop();
            }}

            function stopSynth() {{
                synthRunning = false;
                if (synthTimer) {{ clearTimeout(synthTimer); synthTimer = null; }}
            }}

            // ============ SFX ============
            function sfxPop() {{
                const now = getCtx().currentTime;
                playPiano(880, now, 1.0, 0.45 * SFX_VOLUME);
                playPiano(1318.51, now + 0.08, 1.1, 0.35 * SFX_VOLUME);
            }}
            function sfxDing() {{
                const now = getCtx().currentTime;
                [1174.66, 1479.98, 1760.00].forEach((f, i) => {{
                    playPiano(f, now + i * 0.07, 1.4, 0.30 * SFX_VOLUME);
                }});
            }}
            function sfxChime() {{
                const now = getCtx().currentTime;
                [587.33, 739.99, 880.00, 1174.66, 1479.98, 1760.00].forEach((f, i) => {{
                    playPiano(f, now + i * 0.12, 2.0, 0.28 * SFX_VOLUME);
                }});
            }}
            function sfxReset() {{
                const now = getCtx().currentTime;
                [880, 659.25, 440].forEach((f, i) => {{
                    playPiano(f, now + i * 0.1, 1.0, 0.30 * SFX_VOLUME);
                }});
            }}

            // ============ PLAY MUSIC ============
            function tryPlayMusic() {{
                if (!musicEnabled) return;

                if (PAKAI_MP3 && audioEl.src) {{
                    audioEl.volume = 0.4;
                    const p = audioEl.play();
                    if (p && p.then) {{
                        p.then(() => {{
                            musicStarted = true;
                            console.log('[love] ✅ MP3 playing');
                            hideOverlay();
                        }}).catch(err => {{
                            console.warn('[love] MP3 blocked:', err.name);
                            // Overlay tetap tampil, tunggu tap
                        }});
                    }}
                }} else {{
                    // Fallback synth
                    getCtx();
                    startSynth();
                    musicStarted = true;
                    hideOverlay();
                    console.log('[love] ✅ Synth playing (no MP3)');
                }}
            }}

            function stopMusic() {{
                if (audioEl) {{
                    try {{ audioEl.pause(); }} catch(e) {{}}
                }}
                stopSynth();
                musicStarted = false;
            }}

            // ============ OVERLAY ============
            function hideOverlay() {{
                if (overlay) {{
                    overlay.classList.add('hidden');
                }}
            }}

            // ============ UNLOCK AUDIO ============
            function unlockAndPlay() {{
                getCtx();
                tryPlayMusic();
            }}

            // Overlay: tap untuk unlock
            if (overlay) {{
                overlay.addEventListener('click', (e) => {{
                    e.stopPropagation();
                    unlockAndPlay();
                }});
                overlay.addEventListener('touchstart', (e) => {{
                    e.stopPropagation();
                    unlockAndPlay();
                }});
            }}

            // Fallback: coba autoplay langsung
            setTimeout(() => {{
                tryPlayMusic();
            }}, 500);

            // ============ TOMBOL MUSIK TOGGLE ============
            btn.addEventListener('click', (e) => {{
                e.stopPropagation();
                musicEnabled = !musicEnabled;
                if (musicEnabled) {{
                    btn.textContent = '🔊 Musik';
                    unlockAndPlay();
                }} else {{
                    btn.textContent = '🔇 Musik';
                    stopMusic();
                }}
            }});

            // ============ TERIMA TRIGGER DARI STREAMLIT ============
            // Karena audio element & ctx ada di iframe yang SAMA,
            // kita pakai postMessage listener untuk terima perintah
            window.addEventListener('message', (e) => {{
                const data = e.data;
                if (!data) return;

                if (data.__loveSfx) {{
                    if (data.__loveSfxId !== undefined && data.__loveSfxId === lastSfxId) return;
                    lastSfxId = data.__loveSfxId;

                    getCtx();
                    const name = data.__loveSfx;
                    if (name === 'pop') sfxPop();
                    else if (name === 'ding') sfxDing();
                    else if (name === 'chime') sfxChime();
                    else if (name === 'reset') sfxReset();
                }}

                if (data.__loveToggleMusic !== undefined) {{
                    musicEnabled = data.__loveToggleMusic;
                    if (musicEnabled) unlockAndPlay();
                    else stopMusic();
                }}

                if (data.__loveQuery === true) {{
                    // kirim status balik
                    try {{
                        window.parent.postMessage({{
                            __loveStatus: true,
                            musicEnabled: musicEnabled,
                            musicStarted: musicStarted,
                            pakaiMp3: PAKAI_MP3
                        }}, '*');
                    }} catch(e) {{}}
                }}
            }});

            // Sinyal siap
            try {{
                window.parent.postMessage({{ __loveReady: true, pakaiMp3: PAKAI_MP3 }}, '*');
            }} catch(e) {{}}

            console.log('[love] Player ready. PAKAI_MP3 =', PAKAI_MP3);
        }})();
    </script>
    </body>
    </html>
    """

    # Pakai st.components.v1.html dengan tinggi kecil (buat tombol musik saja)
    components.html(html, height=70, scrolling=False)


# =====================================================================
# TRIGGER SFX — pakai IFRAME TERPISAH
# =====================================================================
def trigger_sfx(sfx_name: str, sfx_id: int):
    if not sfx_name:
        return
    html = f"""
    <!DOCTYPE html><html><head><style>body{{margin:0;background:transparent;}}</style></head>
    <body>
    <script>
        (function() {{
            const msg = {{ __loveSfx: '{sfx_name}', __loveSfxId: {sfx_id} }};
            // Kirim ke SEMUA iframe (biar audio player yang dapet)
            window.parent.postMessage(msg, '*');

            // Juga ke window parent sendiri (kalau player ada di parent)
            try {{
                if (window.parent.__lovePlaySfx) {{
                    window.parent.__lovePlaySfx('{sfx_name}', {sfx_id});
                }}
            }} catch(e) {{}}
        }})();
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
            try {
                window.parent.postMessage({ __loveFireworks: true }, '*');
            } catch(e) {}
        })();
    </script>
    </body></html>
    """
    components.html(html, height=0)


# =====================================================================
# EFEK GLOBAL: Fireworks + Petal + Sparkle
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
            container.style.cssText = 'position:fixed;top:0;left:0;width:100vw;height:100vh;pointer-events:none;z-index:9999;overflow:hidden;';
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
                if (existing
