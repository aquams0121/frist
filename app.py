import streamlit as st
import random

# --- 1. 페이지 설정 및 상태 관리 ---
st.set_page_config(page_title="Streamlit Bee World", layout="centered")

if 'page' not in st.session_state:
    st.session_state.page = 'main'

def change_page(target):
    st.session_state.page = target

# --- 2. 동적 꿀벌 스타일 생성 함수 ---
def get_bee_styles(num_bees):
    bee_css = ""
    bee_html = ""
    for i in range(num_bees):
        top = random.randint(5, 85)
        duration = random.uniform(10, 20)
        delay = random.uniform(0, 5)
        # fly-right(오른쪽행), fly-left(왼쪽행) 랜덤 결정
        direction = random.choice(['fly-right', 'fly-left'])
        
        bee_css += f"""
        .bee-{i} {{
            top: {top}%;
            animation: {direction} {duration:.1f}s linear infinite {delay:.1f}s;
        }}
        """
        bee_html += f'<div class="bee bee-{i}">🐝</div>'
    return bee_css, bee_html

# 현재 페이지에 따라 벌 마리 수 결정 (메인 3마리, 환영 25마리)
num = 25 if st.session_state.page == 'greeting' else 3
dynamic_css, dynamic_html = get_bee_styles(num)

# --- 3. CSS 주입 (디자인 및 애니메이션) ---
# st.markdown의 unsafe_allow_html=True를 사용하여 스타일을 강제 주입합니다.
st.markdown(f"""
    <style>
    /* 배경 및 기본 폰트 설정 */
    .stApp {{
        background-color: #FFD700 !important;
        color: #000000 !important;
        overflow: hidden;
    }}

    /* 텍스트 스타일링 */
    .main-title {{
        font-size: 50px;
        font-weight: 800;
        text-align: center;
        margin-top: 100px;
        color: #000000;
    }}
    
    .sub-title {{
        font-size: 24px;
        text-align: center;
        color: #333333;
        margin-bottom: 50px;
    }}

    /* 버튼 중앙 정렬 스타일 */
    .stButton > button {{
        display: block;
        margin: 0 auto;
        background-color: #000000 !important;
        color: #FFD700 !important;
        border-radius: 10px;
        padding: 10px 25px;
        font-weight: bold;
        border: none;
    }}

    /* 🐝 꿀벌 애니메이션 핵심 */
    .bee {{
        position: fixed;
        font-size: 40px;
        z-index: 1000;
        pointer-events: none;
        user-select: none;
    }}

    /* 오른쪽으로 갈 때: 🐝(기본 왼쪽)를 뒤집어서 오른쪽을 보게 함 */
    @keyframes fly-right {{
        0%   {{ left: -10%; transform: scaleX(-1); }}
        100% {{ left: 110%; transform: scaleX(-1); }}
    }}

    /* 왼쪽으로 갈 때: 🐝 기본 상태 유지 */
    @keyframes fly-left {{
        0%   {{ left: 110%; transform: scaleX(1); }}
        100% {{ left: -10%; transform: scaleX(1); }}
    }}

    /* 동적 벌 위치 스타일 삽입 */
    {dynamic_css}
    </style>
    
    <div class="bee-container">
        {dynamic_html}
    </div>
    """, unsafe_allow_html=True)

# --- 4. 화면 콘텐츠 렌더링 ---

if st.session_state.page == 'main':
    # 메인 화면
    st.markdown('<p class="main-title">🐝 안녕하세요 저는 Streamlit입니다 🐝</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-title">꿀벌들이 평화롭게 날아다니고 있어요.</p>', unsafe_allow_html=True)
    
    if st.button("나도 인사하기:"):
        change_page('greeting')
        st.rerun()

else:
    # 인사 및 축하 화면
    st.balloons() # 폭죽 효과
    st.markdown('<p class="main-title">첫 웹페이지 제작을 축하해요! 🍯</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-title">벌 떼가 축하하러 몰려왔습니다!</p>', unsafe_allow_html=True)
    
    if st.button("돌아가기"):
        change_page('main')
        st.rerun()
