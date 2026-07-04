import streamlit as st

# 1. 배경색(노란색)과 글자색(검정색)을 변경하는 CSS 적용
st.markdown("""
    <style>
    /* 전체 배경색과 기본 글자색 설정 */
    .stApp {
        background-color: #FFD700; /* 밝은 노란색 */
        color: #000000;
    }
    /* 제목, 본문 등 모든 텍스트 요소를 검정색으로 강제 지정 */
    h1, h2, h3, p, span, div, .stMarkdown {
        color: #000000 !important;
    }
    /* 버튼 텍스트 색상도 검정색으로 설정 */
    .stButton>button {
        color: #000000;
        border-color: #000000;
    }
    </style>
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
    st.markdown("<h2 style='text-align: center;'>🎉 안녕하세요 저는 Streamlit입니다 🎉</h2>", unsafe_allow_html=True)
    
    # 버튼이 화면 중앙 즈음에 오도록 컬럼 사용 (선택 사항)
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        st.button("나도 인사하기:", on_click=go_to_greeting, use_container_width=True)

else:
    # --- 인사 화면 (버튼 클릭 후) ---
    st.markdown("<h2 style='text-align: center;'>첫 웹페이지 제작을 축하해요!</h2>", unsafe_allow_html=True)
    st.balloons() # 폭죽(풍선) 효과 터뜨리기
    
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        st.button("돌아가기", on_click=go_to_main, use_container_width=True)
