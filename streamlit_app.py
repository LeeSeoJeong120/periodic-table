import streamlit as st

# Streamlit 상태 초기화
if "selected" not in st.session_state:
    st.session_state.selected = None

def convert_to_embed(url):
    if "watch?v=" in url:
        return url.replace("watch?v=", "embed/")
    elif "shorts/" in url:
        return url.replace("shorts/", "embed/")
    return url

# 원소 정보 (1~20번)
elements = {
    "H":  {"Z": 1,  "name": "수소",  "video": "https://youtube.com/shorts/enPX78U9nbg?si=b3crXHGSq4dLiXTG"},
    "He": {"Z": 2,  "name": "헬륨",    "video": "https://youtu.be/SKM3UG2iFOw"},
    "Li": {"Z": 3,  "name": "리튬",   "video": "https://youtu.be/1Zz8bRK8j1I"},
    "Be": {"Z": 4,  "name": "베릴륨", "video": "https://youtu.be/8e5kSt53PeU"},
    "B":  {"Z": 5,  "name": "붕소",     "video": "https://youtu.be/jghvuTLpZMo"},
    "C":  {"Z": 6,  "name": "탄소",    "video": "https://youtu.be/dkKaC5q9Rp0"},
    "N":  {"Z": 7,  "name": "질소",  "video": "https://youtu.be/ohGzREVa3G8"},
    "O":  {"Z": 8,  "name": "산소",    "video": "https://youtu.be/Sf80sYj1XRs"},
    "F":  {"Z": 9,  "name": "플루오린",  "video": "https://youtu.be/6_JT5Gk6jfw"},
    "Ne": {"Z": 10, "name": "네온",      "video": "https://youtu.be/dQYQJHQhuzU"},
    "Na": {"Z": 11, "name": "나트륨",    "video": "https://youtu.be/KK5jnxB5eCo"},
    "Mg": {"Z": 12, "name": "마그네슘", "video": "https://youtu.be/r89aIgldkPg"},
    "Al": {"Z": 13, "name": "알루미늄", "video": "https://youtu.be/Yy8PYJYfk6I"},
    "Si": {"Z": 14, "name": "규소",   "video": "https://youtu.be/bkzEHDZUbHg"},
    "P":  {"Z": 15, "name": "인","video": "https://youtu.be/U1e9kB_OxMQ"},
    "S":  {"Z": 16, "name": "황",    "video": "https://youtu.be/vlQm3Q8gKps"},
    "Cl": {"Z": 17, "name": "염소",  "video": "https://youtu.be/vI_Gh7jBA-M"},
    "Ar": {"Z": 18, "name": "아르곤",     "video": "https://youtu.be/J_lF8hbd-Qg"},
    "K":  {"Z": 19, "name": "칼륨", "video": "https://youtu.be/CeyuMs95NvA"},
    "Ca": {"Z": 20, "name": "칼슘",   "video": "https://youtu.be/jja6b1xOQDQ"},
}

st.title("🔬 주기율표 1~20번 원소")

# ▶︎ 각 행 구성 (None은 빈칸)
layout = [
    ["H", None, None, None, None, None, None, "He"],
    ["Li", "Be", "B", "C", "N", "O", "F", "Ne"],
    ["Na", "Mg", "Al", "Si", "P", "S", "Cl", "Ar"],
    ["K", "Ca", None, None, None, None, None, None]
]

# 버튼 배치
for row in layout:
    cols = st.columns(8)
    for i, symbol in enumerate(row):
        if symbol:
            if cols[i].button(symbol):
                st.session_state.selected = symbol
        else:
            cols[i].write(" ")

# ▶︎ 선택된 원소 정보 출력
if st.session_state.selected:
    el = elements[st.session_state.selected]
    st.markdown("---")
    st.subheader(f"원자번호 {el['Z']} - {el['name']} ({st.session_state.selected})")
    st.video(convert_to_embed(el["video"]))
