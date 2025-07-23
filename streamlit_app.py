import streamlit as st

# 페이지 전체 wide 설정
st.set_page_config(layout="wide")

# ▶ 유튜브 링크 변환 함수
def convert_to_embed(url):
    if "watch?v=" in url:
        return url.replace("watch?v=", "embed/")
    elif "shorts/" in url:
        return url.replace("shorts/", "embed/")
    return url

# ▶ 원소 정보 일부 예시
elements = {
    "H": {"Z": 1, "name": "Hydrogen", "image": "https://images-of-elements.com/hydrogen.jpg", "video": "https://youtube.com/shorts/enPX78U9nbg?si=yZ25IlbAC1zmJHS4"},
    "He": {"Z": 2, "name": "Helium", "image": "https://images-of-elements.com/helium.jpg", "video": "https://www.youtube.com/watch?v=SKM3UG2iFOw"},
    "Li": {"Z": 3, "name": "Lithium", "image": "https://images-of-elements.com/lithium.jpg", "video": ""},
    "Be": {"Z": 4, "name": "Beryllium", "image": "https://images-of-elements.com/beryllium.jpg", "video": ""},
    "B": {"Z": 5, "name": "Boron", "image": "https://images-of-elements.com/boron.jpg", "video": ""},
    "C": {"Z": 6, "name": "Carbon", "image": "https://images-of-elements.com/carbon.jpg", "video": ""},
    "N": {"Z": 7, "name": "Nitrogen", "image": "https://images-of-elements.com/nitrogen.jpg", "video": ""},
    "O": {"Z": 8, "name": "Oxygen", "image": "https://images-of-elements.com/oxygen.jpg", "video": ""},
    "F": {"Z": 9, "name": "Fluorine", "image": "https://images-of-elements.com/fluorine.jpg", "video": ""},
    "Ne": {"Z": 10, "name": "Neon", "image": "https://images-of-elements.com/neon.jpg", "video": ""},
    "Na": {"Z": 11, "name": "Sodium", "image": "https://images-of-elements.com/sodium.jpg", "video": ""},
    "Mg": {"Z": 12, "name": "Magnesium", "image": "https://images-of-elements.com/magnesium.jpg", "video": ""},
    "Al": {"Z": 13, "name": "Aluminium", "image": "https://images-of-elements.com/aluminium.jpg", "video": ""},
    "Si": {"Z": 14, "name": "Silicon", "image": "https://images-of-elements.com/silicon.jpg", "video": ""},
    "P": {"Z": 15, "name": "Phosphorus", "image": "https://images-of-elements.com/phosphorus.jpg", "video": ""},
    "S": {"Z": 16, "name": "Sulfur", "image": "https://images-of-elements.com/sulfur.jpg", "video": ""},
    "Cl": {"Z": 17, "name": "Chlorine", "image": "https://images-of-elements.com/chlorine.jpg", "video": ""},
    "Ar": {"Z": 18, "name": "Argon", "image": "https://images-of-elements.com/argon.jpg", "video": ""},
    "K": {"Z": 19, "name": "Potassium", "image": "https://images-of-elements.com/potassium.jpg", "video": ""},
    "Ca": {"Z": 20, "name": "Calcium", "image": "https://images-of-elements.com/calcium.jpg", "video": ""}
}

# 상태 초기화
if "selected" not in st.session_state:
    st.session_state.selected = None

st.title("🔬 주기율표 1~20번 원소")

# ────────────────
# 🔼 상단: 버튼 구역 (좌우 여백 넓게)
# ────────────────
with st.container():
    st.markdown("### 🧷 주기율표 버튼")

    layout = [
        ["H", None, None, None, None, None, None, "He"],
        ["Li", "Be", "B", "C", "N", "O", "F", "Ne"],
        ["Na", "Mg", "Al", "Si", "P", "S", "Cl", "Ar"],
        ["K", "Ca", None, None, None, None, None, None]
    ]

    for row in layout:
        cols = st.columns([0.8, 1, 1, 1, 1, 1, 1, 1, 1, 0.8])  # 좌우 여백 넓게
        for i, symbol in enumerate(row):
            if symbol:
                if cols[i + 1].button(symbol):  # 실제 버튼은 가운데 1~8열
                    st.session_state.selected = symbol

# ────────────────
# 🔽 하단: 선택된 원소 정보
# ────────────────
if st.session_state.selected:
    el = elements[st.session_state.selected]
    st.markdown("---")
    st.markdown(f"### 🔍 원자번호 {el['Z']} - {el['name']} ({st.session_state.selected})")

    with st.container():
        col_img, col_vid = st.columns([1, 2])

        with col_img:
            st.image(el["image"], caption=f"{el['name']} (사진)", use_container_width=True)

        with col_vid:
            if el["video"]:
                st.video(convert_to_embed(el["video"]))
            else:
                st.info("등록된 영상이 없습니다.")
