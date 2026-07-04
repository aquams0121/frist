import streamlit as st

# 1. 배경색, 글자색 및 꿀벌 애니메이션 CSS 적용
st.markdown("""
    <style>
    /* 전체 배경색과 기본 글자색 설정 */
    .stApp {
        background-color: #FFD700; /* 밝은 노란색 */
        color: #000000;
        overflow-x: hidden; /* 벌이 화면 밖으로 나갈 때 가로 스크롤바 생김 방지 */
    }
    
    /* 모든 텍스트 요소를 검정색으로 강제 지정 */
    h1, h2, h3, p, span, div, .stMarkdown {
        color: #000000 !important;
    }
    
    /* 버튼 텍스트와 테두리 색상 */
    .stButton>button {
        color: #000000;
        border-color: #000000;
        background-color: #FFFFFF; /* 버튼이 조금 더 잘 보이도록 흰색 배경 추가 */
        font-weight: bold;
    }

    /* 🐝 날아다니는 꿀벌 애니메이션 설정 */
    .bee {
        position: fixed;
        font-size: 35px; /* 벌 크기 */
        z-index: 9999;
        pointer-events: none; /* 클릭을 방해하지 않도록 설정 */
    }
    
    /* 각 벌들의 시작 위치와 속도 다르게 설정 */
    .bee1 { top: 15%; animation: fly-right 12s linear infinite; }
    .bee2 { top: 45%; animation: fly-left 15s linear infinite 2s; left: -50px; }
    .bee3 { top: 75%; animation: fly-right 10s linear infinite 1s; }

    /* 왼쪽에서 오른쪽으로 둥둥 날아가는 애니메이션 (우측을 보도록 scaleX(-1) 적용) */
    @keyframes fly-right {
        0% { left: -10%; transform: translateY(0px) scaleX(-1); }
        25% { transform: translateY(-20px) scaleX(-1); }
        50% { transform: translateY(15px) scaleX(-1); }
        75% { transform: translateY(-10px) scaleX(-1); }
        100% { left: 110%; transform: translateY(0px) scaleX(-1); }
    }
    
    /* 오른쪽에서 왼쪽으로 둥둥 날아가는 애니메이션 (좌측을 보도록 scaleX(1) 적용) */
    @keyframes fly-left {
        0% { left: 110%; transform: translateY(0px) scaleX(1); } 
        25% { transform: translateY(20px) scaleX(1); }
        50% { transform: translateY(-15px) scaleX(1); }
        75% { transform: translateY(10px) scaleX(1); }
        100% { left: -10%; transform: translateY(0px) scaleX(1); }
    }
    </style>
    
    <div class="bee bee1">🐝</div>
    <div class="bee bee2">🐝</div>
    <div class="bee bee3">🐝</div>
    """, unsafe_allow_html=True)

# 2. 화면 전환을 위한 세션 상태(Session State) 초기화
if 'show_greeting' not in st.session_state:
    st.session_state.show_greeting = False

# 버튼 클릭 시 상태를 변경하는 함수
def go_to_greeting():
    st.session_state.show_greeting = True

def go_to_main():
    st.session_state.show_greeting = False

# 3. 메인 화면과 인사 화면 로직
if not st.session_state.show_greeting:
    # --- 메인 화면 ---
    st.markdown("<h2 style='text-align: center;'>🐝 안녕하세요 저는 Streamlit입니다 🐝</h2>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        st.button("나도 인사하기:", on_click=go_to_greeting, use_container_width=True)

else:
    # --- 인사 화면 (버튼 클릭 후) ---
    st.markdown("<h2 style='text-align: center;'>첫 웹페이지 제작을 축하해요! 🍯</h2>", unsafe_allow_html=True)
    st.balloons() # 폭죽(풍선) 효과
    
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        st.button("돌아가기", on_click=go_to_main, use_container_width=True)
