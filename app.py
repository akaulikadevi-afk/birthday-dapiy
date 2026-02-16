import streamlit as st
from datetime import date

st.set_page_config(page_title="Birthday Card", page_icon="🎂", layout="centered")

# --- Simple clean CSS ---
st.markdown(
    """
    <style>
    .card {
        border: 1px solid rgba(0,0,0,0.10);
        border-radius: 18px;
        padding: 18px 18px 8px 18px;
        background: rgba(255,255,255,0.7);
        backdrop-filter: blur(6px);
    }
    .muted {opacity: 0.75;}
    .big {font-size: 1.2rem; line-height: 1.6;}
    .quote {
        border-left: 4px solid rgba(0,0,0,0.15);
        padding-left: 12px;
        margin: 12px 0;
        opacity: 0.9;
    }
    .tiny {font-size: 0.9rem; opacity: 0.8;}
    </style>
    """,
    unsafe_allow_html=True,
)

# --- Session state ---
if "unlocked" not in st.session_state:
    st.session_state.unlocked = False
if "revealed" not in st.session_state:
    st.session_state.revealed = {"wish": False, "storyline": False, "note": False}

# --- Content (your text) ---
TITLE_LINE = "HAPPY BIRTHDAY DAPIII 🎂🤍"
STORYLINE_LINE = "my mantan kandung but still a part of my storyline 😌"
LETTER = """wish u all the best ya tahun ini. semoga makin gg, makin mantap, makin naik level pelan pelan tapi pasti. semoga makin sehat, makin kuat, makin banyak rezeki dari arah yg ga disangka sangka. semoga apa yg km kejar sekarang satu satu mulai keliatan hasilnya.

i hope this year lebih baik dr yg kemarin. semoga capek km kebayar, doa doa km dikabulin, dan km ketemu banyak hal yg bikin km ngerasa hidup tuh worth it. jgn lupa jaga diri, jgn kebanyakan overwork, makan yg bener, istirahat yg cukup.

makasih ya pernah jadi bagian cerita ak. walaupun sekarang udh beda jalan, ak tetep bersyukur pernah kenal km. ada hal hal yg ak pelajarin, dan itu ga ak lupain.
stay kind, stay real, stay you. jangan lupa jaga diri, jaga kesehatan, jangan overwork, dan jangan lupa bahagia.
pokoknya semoga km bahagia dgn versi hidup km yg skrg. happy birthday once again sayang 🤍 take care always."""
# --- UI ---
st.title("🎂 A Small Birthday Page")

with st.sidebar:
    st.subheader("Navigation")
    page = st.radio("Go to", ["Home", "Open the Card", "Mini Quiz", "Credits"], label_visibility="collapsed")
    st.divider()
    st.caption("Built with Streamlit • hosted via GitHub")

if page == "Home":
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("### Hi 👋")
    st.markdown(
        "<p class='big'>Ini kartu ulang tahun versi web. Ada tombol-tombol buat buka isinya pelan-pelan.</p>",
        unsafe_allow_html=True,
    )
    st.markdown("<p class='muted'>Tip: buka tab “Open the Card”.</p>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

elif page == "Open the Card":
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("### 📨 Tap to open")
    col1, col2 = st.columns([1, 1])

    with col1:
        pin = st.text_input("PIN (optional)", type="password", placeholder="boleh dikosongin")
        st.caption("Kalau mau, kamu bisa set PIN kecil biar feel-nya kayak ‘unlock’.")

    with col2:
        if st.button("Open", use_container_width=True):
            # If PIN filled, require "dapi" or "dap i" style? keep gentle
            if pin and pin.strip().lower() not in {"dapi", "dap i", "dap"}:
                st.warning("PIN-nya salah. Coba lagi (atau kosongin aja).")
            else:
                st.session_state.unlocked = True
                st.balloons()

    if not st.session_state.unlocked:
        st.info("Klik **Open** untuk buka kartunya.")
        st.markdown("</div>", unsafe_allow_html=True)
        st.stop()

    st.success("Unlocked.")
    st.markdown(f"## {TITLE_LINE}")
    st.markdown(f"<p class='muted'>{STORYLINE_LINE}</p>", unsafe_allow_html=True)

    st.divider()

    c1, c2, c3 = st.columns(3)
    with c1:
        if st.button("Reveal wishes", use_container_width=True):
            st.session_state.revealed["wish"] = True
    with c2:
        if st.button("Reveal storyline", use_container_width=True):
            st.session_state.revealed["storyline"] = True
    with c3:
        if st.button("One more note", use_container_width=True):
            st.session_state.revealed["note"] = True

    if st.session_state.revealed["wish"]:
        st.markdown('<div class="quote">', unsafe_allow_html=True)
        st.markdown(LETTER.replace("\n", "\n\n"))
        st.markdown("</div>", unsafe_allow_html=True)

    if st.session_state.revealed["storyline"]:
        st.markdown("#### a small reminder")
        st.write("Some people leave the scene, but not the meaning.")

    if st.session_state.revealed["note"]:
        st.markdown("#### for today")
        mood = st.slider("Your mood today", 0, 10, 7)
        if mood >= 8:
            st.write("Nice. Keep it light, keep it steady.")
        elif mood >= 5:
            st.write("Semoga harimu tenang dan lancar.")
        else:
            st.write("Pelan-pelan aja. Istirahat juga progress.")
        if st.button("Snow effect (optional)"):
            st.snow()

    st.markdown("<p class='tiny'>PS: halaman ini sengaja minimalis.</p>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

elif page == "Mini Quiz":
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("### Quick mini-quiz (buat iseng, tapi sopan)")
    a = st.radio("One thing that matters most this year:", ["Health", "Growth", "Peace", "All of the above"], index=3)
    b = st.selectbox("Pick a pace:", ["Pelan tapi pasti", "Gas tipis-tipis", "Yang penting konsisten"])
    if st.button("Show result"):
        st.success("✅ Valid. Semoga tahun ini rapi, sehat, dan naik level tanpa maksa.")
        st.write(f"Pilihan kamu: **{a}** • **{b}**")
    st.markdown("</div>", unsafe_allow_html=True)

else:  # Credits
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("### Credits")
    st.write("Made with Streamlit.")
    st.write("Hosted from GitHub.")
    st.caption(f"Date generated: {date.today().isoformat()}")
    st.markdown("</div>", unsafe_allow_html=True)
