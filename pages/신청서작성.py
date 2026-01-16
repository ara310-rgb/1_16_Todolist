import streamlit as st
from datetime import datetime

# 1. 페이지 설정
st.set_page_config(page_title="프리미엄 상세 평가보고서 신청", page_icon="⚖️", layout="centered")

# 2. 커스텀 CSS (고급스러운 디자인 적용)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@300;400;700;900&display=swap');

    /* 전체 폰트 및 배경 */
    html, body, [data-testid="stAppViewContainer"] {
        font-family: 'Noto Sans KR', sans-serif;
        background-color: #F4F7F9;
    }

    /* 폼 컨테이너 카드 디자인 */
    [data-testid="stForm"] {
        background-color: #ffffff;
        padding: 40px !important;
        border-radius: 20px !important;
        border: 1px solid #E2E8F0 !important;
        box-shadow: 0 10px 25px rgba(0, 0, 0, 0.05) !important;
    }

    /* 타이틀 스타일 */
    .main-title {
        font-size: 2.2rem;
        font-weight: 900;
        color: #1A365D;
        text-align: center;
        margin-bottom: 0.5rem;
    }
    .sub-title {
        font-size: 1.1rem;
        color: #718096;
        text-align: center;
        margin-bottom: 2rem;
    }

    /* 입력창 라벨 스타일 */
    div[data-testid="stWidgetLabel"] p {
        font-weight: 700 !important;
        color: #2D3748 !important;
        font-size: 0.95rem !important;
        margin-bottom: 8px !important;
    }

    /* 입력창 디자인 (포커스 시 골드 포인트) */
    input, div[data-baseweb="select"], textarea {
        border-radius: 10px !important;
        border: 1.5px solid #E2E8F0 !important;
        transition: all 0.3s ease !important;
    }
    
    div[data-baseweb="input"]:focus-within, div[data-baseweb="select"]:focus-within {
        border-color: #D4AF37 !important;
        box-shadow: 0 0 0 3px rgba(212, 175, 55, 0.2) !important;
    }

    /* 제출 버튼 디자인 (럭셔리 골드 그라데이션) */
    div.stButton > button {
        width: 100% !important;
        height: 3.8rem !important;
        margin-top: 20px !important;
        border-radius: 12px !important;
        background: linear-gradient(135deg, #1A365D 0%, #2A4365 100%) !important;
        color: #D4AF37 !important; /* 골드 텍스트 */
        font-weight: 700 !important;
        font-size: 1.2rem !important;
        border: 1px solid #D4AF37 !important;
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275) !important;
        letter-spacing: 1px;
    }

    /* 버튼 마우스 오버 효과 */
    div.stButton > button:hover {
        background: #D4AF37 !important;
        color: #ffffff !important;
        transform: translateY(-3px) !important;
        box-shadow: 0 12px 20px rgba(212, 175, 55, 0.3) !important;
    }

    /* 구분선 스타일 */
    hr {
        margin: 2rem 0 !important;
        border-bottom: 1px solid #E2E8F0 !important;
    }
    
    /* 성공 메시지 박스 */
    div[data-testid="stNotification"] {
        border-radius: 15px !important;
    }
    </style>
    """, unsafe_allow_html=True)

def main():
    # 상단 헤더 영역
    st.markdown('<p class="main-title">Request a customized in-depth analysis report tailored by our experts!</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-title">전문가의 상세한 분석을 경험해보세요!</p>', unsafe_allow_html=True)

    # 폼 생성
    with st.form("evaluation_form"):
        st.markdown("#### 👤 신청자 기본 정보")
        col1, col2 = st.columns(2)
        with col1:
            name = st.text_input("성함", placeholder="성함을 입력하세요")
        with col2:
            contact = st.text_input("연락처", placeholder="010-0000-0000")
        
        organization = st.text_input("🏢 소속 기관 / 기업명", placeholder="소속을 정확히 입력해 주세요.")
        
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("#### 🔍 평가 요청 상세")
        
        category = st.selectbox(
            "평가 대상 분야",
            ["IT 솔루션 및 아키텍처", "경영 전략 컨설팅", "제조 공정 최적화", "서비스 품질 평가", "기타 전문 분야"],
            index=None,
            placeholder="상세 분야를 선택하세요"
        )

        desired_date = st.date_input("📅 보고서 수령 희망일", min_value=datetime.today())
        notes = st.text_area("✍️ 추가 요청 및 문의사항", placeholder="분석에 참고할 상세 내용을 기재해 주세요.", height=150)

        # 제출 버튼
        submitted = st.form_submit_button("상세 평가보고서 신청하기")

        if submitted:
            if not (name and contact and organization and category):
                st.error("🚨 모든 필수 정보를 입력해 주셔야 신청이 완료됩니다.")
            else:
                st.balloons()
                st.success(f"**{name}** 님의 신청이 성공적으로 접수되었습니다. 담당 전문가가 빠른 시일 내에 연락드리겠습니다.")

if __name__ == "__main__":
    main()