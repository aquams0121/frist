import streamlit as st
import random

# 1. 화면 전환을 위한 세션 상태(Session State) 초기화
if 'show_greeting' not in st.session_state:
    st.session_state.show_greeting = False

# 버튼 클릭 시 상태를 변경하는 함수
def go_to_greeting():
    st.session_state.show_greeting = True

def go_to_main():
    st.session_state.show_greeting = False

# 2. 벌들을 동적으로 생성하는 함수 (HTML + CSS)
def generate_bees(num_bees):
    bee_css = ""
    bee_html = ""
    
    for i in range(1, num_bees + 1):
        # 벌들의 위치, 날아가는 시간, 지연 시간을 랜덤하게 설정
        top = random.randint(5, 90)
        duration = random.uniform(8, 18)
        delay = random.uniform(0, 5)
        direction = random.choice(['fly-right', 'fly-left'])
        
        bee_css += f"""
        .bee{i} {{
            top: {top}%;
            animation: {direction} {duration:.1f}s linear infinite {delay:.1f}s;
        }}
        """
        bee_html += f'<div class="bee bee{i}">🐝</div>\n'
        
    return bee_css, bee_html

# 3. 화면 상태에 따라 벌의 마리 수 결정
# 메인 화면은 3마리, 인사 화면은 20마리
num_bees = 20 if st.session_state.show_greeting else 3
dynamic_bee_css, dynamic_bee_html = generate_bees(num_bees)

# 4. 공통 CSS 및 애니메이션 설정 (방향 수정 완료!)
st.markdown(f"""
    <style>
    /* 전체 배경색과 기본 글자색 설정 */
    .stApp {{
        background-color: #FFD700;
        color: #000000;
        overflow-x: hidden; 
    }}
    
    /* 텍스트 요소 색상 */
    h1, h2, h3, p, span, div, .stMarkdown {{
        color: #000000 !important;
    }}
    
    /* 버튼 스타일 */
    .stButton>button {{
        color: #000000;
        border-color: #000000;
        background-color: #FFFFFF;
        font-weight: bold;
    }}

    /* 🐝 날아다니는 꿀벌 기본 설정 */
    .bee {{
        position: fixed;
        font-size: 35px;
        z-index: 9999;
        pointer-events: none;
    }}
    
    /* 동적으로 생성된 벌들의 개별 설정 삽입 */
    {dynamic_bee_css}

    /* 벌 이모지(🐝)는 기본적으로 왼쪽을 봅니다.
       오른쪽으로 날아갈 때(fly-right): scaleX(-1)로 우측을 보게 뒤집음 
    */
    @keyframes fly-right {{
        0% {{ left: -10%; transform: translateY(0px) scaleX(-1); }}
        25% {{ transform: translateY(-20px) scaleX(-1); }}
        50% {{ transform: translateY(15px) scaleX(-1); }}
        75% {{ transform: translateY(-10px) scaleX(-1); }}
        100% {{ left: 110%; transform: translateY(0px) scaleX(-1); }}
    }}
    
    /* 왼쪽으로 날아갈 때(fly-left): 원래 모습인 scaleX(1) 유지 
    */
    @keyframes fly-left {{
        0% {{ left: 110%; transform: translateY(0px) scaleX(1); }} 
        25% {{ transform: translateY(20px) scaleX(1); }}
        50% {{ transform: translateY(-15px) scaleX(1); }}
        75% {{ transform: translateY(10px) scaleX(1); }}
        100% {{ left: -10%; transform: translateY(0px) scaleX(1); }}
    }}
    </style>
    
    {dynamic_bee_html}
    """, unsafe_allow_html=True)

# 5. 화면 렌더링 로직
if not st.session_state.show_greeting:
    # --- 메인 화면 ---
    st.markdown("<br><br><h2 style='text-align: center;'>🐝 안녕하세요 저는 Streamlit입니다 🐝</h2><br>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        st.button("나도 인사하기:", on_click=go_to_greeting, use_container_width=True)

else:
    # --- 인사 화면 (버튼 클릭 후) ---
    st.markdown("<br><br><h2 style='text-align: center;'>첫 웹페이지 제작을 축하해요! 🍯</h2><br>", unsafe_allow_html=True)
    st.balloons() # 폭죽 효과
    
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        st.button("돌아가기", on_click=go_to_main, use_container_width=True)
