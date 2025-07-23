import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# 페이지 전체 레이아웃 설정
st.set_page_config(layout="wide")
st.title("🔬 주기율표 1~20번 원소 - 원자 모형 시각화")

# 상태 초기화
if "selected" not in st.session_state:
    st.session_state.selected = None

# ▶ 원자 모형 그리기 함수
def draw_simple_atom_model_with_boundary(atomic_number):
    fig, ax = plt.subplots(figsize=(3, 3))  # 크기 축소
    ax.set_aspect('equal')
    ax.axis('off')

    # 원자 경계선 (검은 실선)
    atom_radius = 2.5
    atom_boundary = plt.Circle((0, 0), atom_radius, color='black', fill=False, linestyle='solid', linewidth=1)
    ax.add_artist(atom_boundary)

    # 원자핵 (빨간 원 + +숫자 표시, 글자 검정)
    nucleus = plt.Circle((0, 0), 0.2, color='red', zorder=3)
    ax.add_artist(nucleus)
    ax.text(0, 0, f'+{atomic_number}', fontsize=10, ha='center', va='center', color='black')

    # 전자: 무작위 위치에 파란 원 + '-' 텍스트
    radii = np.random.uniform(0.4, atom_radius - 0.2, atomic_number)
    angles = np.random.uniform(0, 2 * np.pi, atomic_number)
    for r, theta in zip(radii, angles):
        x = r * np.cos(theta)
        y = r * np.sin(theta)
        electron = plt.Circle((x, y), 0.07, color='blue', zorder=2)
        ax.add_artist(electron)
        ax.text(x, y, '-', fontsize=8, ha='center', va='center', color='white', zorder=4)

    ax.set_xlim(-3, 3)
    ax.set_ylim(-3, 3)
    return fig

# ▶ 원소 정보 (1~20)
elements = {
    "H": 1, "He": 2, "Li": 3, "Be": 4, "B": 5,
    "C": 6, "N": 7, "O": 8, "F": 9, "Ne": 10,
    "Na": 11, "Mg": 12, "Al": 13, "Si": 14, "P": 15,
    "S": 16, "Cl": 17, "Ar": 18, "K": 19, "Ca": 20
}

# ▶ 역방향 매핑 (원자번호 → 기호)
atomic_number_to_symbol = {v: k for k, v in elements.items()}

# ▶ 상단 주기율표 버튼 배치
layout = [
    ["H", None, None, None, None, None, None, "He"],
    ["Li", "Be", "B", "C", "N", "O", "F", "Ne"],
    ["Na", "Mg", "Al", "Si", "P", "S", "Cl", "Ar"],
    ["K", "Ca", None, None, None, None, None, None]
]

st.markdown("### 🧷 주기율표 버튼")

for row in layout:
    cols = st.columns([0.8, 1, 1, 1, 1, 1, 1, 1, 0.8])  # 좌우 여백 포함
    for i, symbol in enumerate(row):
        if symbol:
            if cols[i + 1].button(symbol):
                st.session_state.selected = elements[symbol]

# ▶ 출력 영역
if st.session_state.selected:
    Z = int(st.session_state.selected)  
    symbol = atomic_number_to_symbol.get(Z, "?")
    st.markdown("---")
    st.subheader(f"🔍 원자번호 {Z} - {symbol}")
    fig = draw_simple_atom_model_with_boundary(Z)
    st.pyplot(fig)