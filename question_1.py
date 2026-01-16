import streamlit as st
import time

# 1. 페이지 설정 및 디자인
st.set_page_config(page_title="무역 수출역량진단", page_icon="🌐", layout="centered")

st.markdown("""
    <style>
    /* 배경색 및 폰트 설정 */
    .stApp { background-color: #f8fafc; }
    .header-container { text-align: center; padding: 30px 0 40px 0; }
    .main-title { font-size: 2.2rem; font-weight: 800; color: #1e293b; margin-bottom: 12px; }
    .sub-title { font-size: 1.05rem; color: #64748b; font-weight: 400; }
    
    /* ✨ 마우스 오버 애니메이션 (연한 회색 테마) ✨ */
    .info-card {
        background-color: #ffffff;
        padding: 22px 25px;
        border-radius: 12px;
        box-shadow: 0 2px 10px rgba(0, 0, 0, 0.03);
        margin-bottom: 12px;
        border: 1px solid #e2e8f0; 
        width: 100%;
        transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1);
    }
    
    .info-card:hover {
        transform: translateY(-4px); 
        border-color: #cbd5e1;      /* 마우스 오버 시 연한 회색 */
        box-shadow: 0 10px 20px rgba(0, 0, 0, 0.06); 
    }

    .question-title { font-size: 1.05rem; font-weight: 700; color: #334155; }
    .result-text { font-size: 1.2rem; font-weight: 700; color: #475569; line-height: 1.6; }
    
    /* 결과 피드백 카드 - 왼쪽 선 디자인 제거 및 중앙 정렬 유지 */
    .feedback-card { 
        text-align: center; 
        margin-top: 15px; 
        margin-bottom: 20px; 
        border-left: none !important; /* 파란색/회색 선 제거 */
    }

    /* 진단 버튼 디자인 */
    div[data-testid="stForm"] button {
        background-color: #334155 !important;
        color: white !important;
        border-radius: 8px !important;
        height: 3.5rem !important;
    }
    
    .stButton > button { font-weight: bold !important; }
    </style>
    """, unsafe_allow_html=True)

def typing_effect(text):
    """텍스트 타이핑 효과"""
    empty_space = st.empty()
    displayed_text = ""
    for char in text:
        displayed_text += char
        # 피드백 카드에서도 동일한 info-card 스타일 적용 (왼쪽 선 없음)
        empty_space.markdown(f'<div class="info-card feedback-card"><span class="result-text">{displayed_text}</span></div>', unsafe_allow_html=True)
        time.sleep(0.03)

def main():
    if 'submitted' not in st.session_state:
        st.session_state.submitted = False

    st.markdown("""
        <div class="header-container">
            <div class="main-title">🌐 무역 수출역량진단 모의 테스트</div>
            <div class="sub-title">우리 기업의 글로벌 진출 준비도를 차분하게 분석해 드립니다.</div>
        </div>
    """, unsafe_allow_html=True)

    questions = [
        "수출 전담 인력이나 조직이 구성되어 있습니까?",
        "외국어 카탈로그, 홈페이지 등 홍보물이 준비되어 있습니까?",
        "최근 1년 내 해외 전시회 참여나 바이어 미팅 경험이 있습니까?",
        "주력 제품의 해외 인증(CE, FDA 등)을 보유 중입니까?",
        "해외 시장조사를 통해 타겟 국가를 선정한 상태입니까?",
        "영어 또는 타겟 국가 언어로 계약서 작성이 가능합니까?",
        "수출 대금 결제 방식(L/C, T/T 등)에 대해 이해하고 있습니까?",
        "물류 파트너사(포워딩 업체)를 확보하고 있습니까?",
        "자사 제품의 HS Code를 정확히 알고 있습니까?",
        "경영진의 수출 의지가 확고하고 예산이 편성되어 있습니까?"
    ]

    options = ["1점 (전혀 아님)", "2점 (미흡)", "3점 (보통)", "4점 (양호)", "5점 (매우 우수)"]
    score_map = {opt: i+1 for i, opt in enumerate(options)}

    with st.form("diagnostic_form"):
        total_score = 0
        for i, q in enumerate(questions):
            st.markdown(f'<div class="info-card"><div class="question-title">{i+1}. {q}</div></div>', unsafe_allow_html=True)
            answer = st.radio(f"radio_{i}", options=options, index=2, horizontal=True, label_visibility="collapsed")
            total_score += score_map[answer]
        
        st.write("")
        _, col_btn, _ = st.columns([1.5, 2, 1.5])
        with col_btn:
            submit_button = st.form_submit_button(label="종합 진단 결과 확인", use_container_width=True)

    if submit_button or st.session_state.submitted:
        st.session_state.submitted = True
        if submit_button:
            st.session_state.current_score = total_score
            with st.spinner('데이터를 분석 중입니다...'):
                time.sleep(0.8)
        
        status, color, desc = get_result_data(st.session_state.current_score)
        
        st.markdown(f"""
            <div style="text-align: center; margin-top: 40px;">
                <h2 style="color: {color}; margin-bottom: 5px; font-size: 2rem;">{status}</h2>
                <div style="margin: 10px 0;">
                    <span style="font-size: 3.5rem; font-weight: 800; color: #1e293b;">{st.session_state.current_score}</span>
                    <span style="font-size: 1.5rem; color: #cbd5e1;"> / 50</span>
                </div>
            </div>
        """, unsafe_allow_html=True)
        
        if submit_button:
            typing_effect(desc)
        else:
            st.markdown(f'<div class="info-card feedback-card"><span class="result-text">{desc}</span></div>', unsafe_allow_html=True)

        _, col_home, _ = st.columns([1.5, 2, 1.5])
        with col_home:
            if st.button("메인 페이지로", use_container_width=True):
                st.session_state.submitted = False
                st.rerun()

def get_result_data(score):
    if score <= 20:
        return "수출 초보 단계", "#94a3b8", "기초 무역 실무 교육과 내부 인력 양성이 시급한 단계입니다."
    elif score <= 35:
        return "수출 유망 단계", "#64748b", "본격적인 마케팅을 위한 인프라 보완이 필요한 단계입니다."
    elif score <= 45:
        return "수출 성장 단계", "#475569", "글로벌 시장 확대 및 실질적인 계약 성사가 기대되는 단계입니다."
    else:
        return "수출 강소 단계", "#1e293b", "최상위 역량입니다. 신시장 개척과 브랜드 강화에 집중해 보세요."

if __name__ == "__main__":
    main()