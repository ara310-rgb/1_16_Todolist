import streamlit as st

# 1. 페이지 설정
st.set_page_config(page_title="수출역량진단 서비스", layout="wide")

# 2. 커스텀 CSS 적용
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    
    .header-container { text-align: center; margin-bottom: 30px; }

    /* --- [버튼 디자인] --- */
    /* stButton 내부 버튼들이 부모 컬럼 너비에 맞춰 꽉 차도록 설정 */
    div.stButton > button {
        background-color: #007bff; color: white; padding: 12px 0px;
        border-radius: 8px; font-weight: bold; border: none; transition: 0.3s; 
        width: 100%; /* 컬럼 너비에 맞춤 */
        display: block;
    }
    /* 모의 테스트 버튼은 흰색 배경에 파란 테두리로 구분감 주기 (선택 사항) */
    div.stButton > button[kind="secondary"] {
        background-color: white; color: #007bff; border: 2px solid #007bff;
    }
    
    div.stButton > button:hover { 
        background-color: #0056b3; color: white; border-color: #0056b3;
    }

    /* --- [후기 알림바 스타일] --- */
    .review-ticker-container {
        width: 100%; 
        margin: 40px auto; 
        height: 80px;
        overflow: hidden;
        background: white;
        border-radius: 12px;
        border: 1px solid #e0e0e0;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        display: flex;
        align-items: center;
        padding: 0 30px;
        position: relative;
    }

    .review-wrapper {
        display: flex;
        flex-direction: column;
        animation: ticker-slide 10s infinite;
    }

    .review-item {
        height: 80px;
        display: flex;
        align-items: center;
        gap: 15px;
        flex-shrink: 0;
    }

    .bell-icon { font-size: 22px; }
    .review-content { display: flex; flex-direction: column; }
    .review-header { font-size: 13px; color: #888; margin-bottom: 2px; }
    .review-text { font-size: 16px; font-weight: bold; color: #333; }

    @keyframes ticker-slide {
        0%, 15% { transform: translateY(0); }
        20%, 35% { transform: translateY(-80px); }
        40%, 55% { transform: translateY(-160px); }
        60%, 75% { transform: translateY(-240px); }
        80%, 95% { transform: translateY(-320px); }
        100% { transform: translateY(0); }
    }

    /* --- [카드 섹션 스타일] --- */
    .section2-title { text-align: center; margin-top: 50px; margin-bottom: 30px; }
    .card {
        background-color: white; padding: 30px 20px; border-radius: 12px;
        border: 1px solid #e0e0e0; box-shadow: 2px 2px 12px rgba(0,0,0,0.05);
        display: flex; flex-direction: column; justify-content: center;
        align-items: center; height: 280px; text-align: center; transition: 0.2s;
    }
    .card:hover { transform: translateY(-5px); border-color: #007bff; }
    .card .icon { font-size: 50px; margin: 15px 0; }

    .step-box {
        background-color: #ffffff; border: 2px solid #007bff; border-radius: 50px;
        padding: 10px 20px; text-align: center; font-weight: bold; color: #007bff;
    }
    .notice-box {
        background-color: #f1f1f1; padding: 20px; border-radius: 8px;
        font-size: 13px; color: #666; margin-top: 60px; line-height: 1.6;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 상단 타이틀 ---
st.markdown("""
    <div class='header-container'>
        <h1 style='font-size: 40px;'>수출역량진단 서비스</h1>
        <p style='font-size: 18px; color: #555;'>나에게 맞는 지원서비스를 활용하여 수출 역량을 Upgrade!</p>
    </div>
    """, unsafe_allow_html=True)

# --- 1번 섹션: 버튼 (수정된 부분) ---
# 좌우 여백을 주어 버튼 2개가 중앙에 모이도록 설정
col_l, col_btn1, col_btn2, col_r = st.columns([0.6, 1, 1, 0.6])

with col_btn1:
    # '모의 테스트 시작' 버튼
    if st.button("모의 테스트 시작", key="mock_test_btn", use_container_width=True):
        st.toast("모의 테스트 페이지로 이동합니다.")

with col_btn2:
    # '평가보고서 신청하기' 버튼
    if st.button("평가보고서 신청하기", key="top_btn", use_container_width=True):
        st.toast("신청 페이지로 이동합니다.")

st.markdown("<br><hr>", unsafe_allow_html=True)

# --- 2번 섹션: 서비스 소개 (카드 섹션) ---
st.markdown("<div class='section2-title'><h2>빅데이터 기반<br>수출역량 진단보고서 제공</h2></div>", unsafe_allow_html=True)

card_col1, card_col2, card_col3 = st.columns(3)
with card_col1:
    st.markdown('<div class="card"><h3>01</h3><div class="icon">📊</div><p><b>수출 / 경영 / 기술</b><br>파트별 역량진단</p></div>', unsafe_allow_html=True)
with card_col2:
    st.markdown('<div class="card"><h3>02</h3><div class="icon">📋</div><p>항목별 세분화된<br><b>분석 리포트</b> 제공</p></div>', unsafe_allow_html=True)
with card_col3:
    st.markdown('<div class="card"><h3>03</h3><div class="icon">💡</div><p>맞춤형<br><b>지원 서비스</b> 추천</p></div>', unsafe_allow_html=True)

# --- 3번 섹션: 후기 알림바 ---
st.markdown("""
    <div class="review-ticker-container">
        <div class="review-wrapper">
            <div class="review-item">
                <span class="bell-icon">🔔</span>
                <div class="review-content">
                    <span class="review-header">김*우 대표님 | 방금 전</span>
                    <span class="review-text">"우리 회사에 딱 맞는 지원사업을 바로 찾았어요! 📈"</span>
                </div>
            </div>
            <div class="review-item">
                <span class="bell-icon">🔔</span>
                <div class="review-content">
                    <span class="review-header">이*민 팀장님 | 2분 전</span>
                    <span class="review-text">"보고서 분석 내용이 생각보다 훨씬 정교해서 놀랐습니다. 👍"</span>
                </div>
            </div>
            <div class="review-item">
                <span class="bell-icon">🔔</span>
                <div class="review-content">
                    <span class="review-header">(주)테크솔루션 | 10분 전</span>
                    <span class="review-text">"수출 전략 짜는 데 이만한 서비스가 없네요. 강력 추천합니다! 🔥"</span>
                </div>
            </div>
            <div class="review-item">
                <span class="bell-icon">🔔</span>
                <div class="review-content">
                    <span class="review-header">박*지 담당자님 | 1시간 전</span>
                    <span class="review-text">"데이터 기반이라 내부 보고용으로도 아주 훌륭해요. 📊"</span>
                </div>
            </div>
            <div class="review-item">
                <span class="bell-icon">🔔</span>
                <div class="review-content">
                    <span class="review-header">정*훈 대표님 | 오늘 오전</span>
                    <span class="review-text">"진단부터 추천 서비스까지 한 번에 해결되니 너무 편하네요. ✅"</span>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# --- 4번 섹션: 서비스 이용 방법 ---
st.markdown("<br><br><h3 style='text-align:center;'>서비스 이용 방법</h3><br>", unsafe_allow_html=True)
step_cols = st.columns([1, 0.2, 1, 0.2, 1, 0.2, 1, 0.2, 1])
steps = ["로그인", "서비스 신청", "정성 평가 질문", "평가진행", "결과 확인"]
for i, step in enumerate(steps):
    with step_cols[i*2]: st.markdown(f'<div class="step-box">{step}</div>', unsafe_allow_html=True)
    if i < len(steps)-1:
        with step_cols[i*2+1]: st.markdown("<p style='text-align:center; padding-top:12px;'>➡</p>", unsafe_allow_html=True)

# --- 5번 섹션: 하단 주의사항 ---
st.markdown("""
    <div class="notice-box">
        <b>💡 서비스 이용 주의사항</b><br>
        본 수출역량 진단은 신용정보법 제15조 1항에 의거하여 기업의 신용정보를 수집하고 처리할 수 있습니다. 
        적법한 절차에 의해 수집된 정보를 활용하며, 제공되는 리포트는 참고용으로 공식적인 증빙 서류로의 활용은 제한될 수 있습니다.
    </div>
    """, unsafe_allow_html=True)



import streamlit as st

# 1. 페이지 설정
st.set_page_config(page_title="수출역량진단 서비스", layout="wide")

# 세션 상태 초기화 (페이지 전환용)
if 'page' not in st.session_state:
    st.session_state.page = "home"

# 2. 커스텀 CSS 적용 (기존 스타일 + 모의테스트 스타일 통합)
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    .header-container { text-align: center; margin-bottom: 30px; }

    /* --- [버튼 디자인] --- */
    div.stButton > button {
        background-color: #007bff; color: white; padding: 12px 0px;
        border-radius: 8px; font-weight: bold; border: none; transition: 0.3s; 
        width: 100%; display: block;
    }
    div.stButton > button:hover { 
        background-color: #0056b3; color: white; border-color: #0056b3;
    }

    /* --- [후기 알림바 스타일] --- */
    .review-ticker-container {
        width: 100%; margin: 40px auto; height: 80px; overflow: hidden;
        background: white; border-radius: 12px; border: 1px solid #e0e0e0;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05); display: flex; align-items: center;
        padding: 0 30px; position: relative;
    }
    .review-wrapper { display: flex; flex-direction: column; animation: ticker-slide 10s infinite; }
    .review-item { height: 80px; display: flex; align-items: center; gap: 15px; flex-shrink: 0; }
    .review-text { font-size: 16px; font-weight: bold; color: #333; }

    @keyframes ticker-slide {
        0%, 15% { transform: translateY(0); }
        20%, 35% { transform: translateY(-80px); }
        40%, 55% { transform: translateY(-160px); }
        60%, 75% { transform: translateY(-240px); }
        80%, 95% { transform: translateY(-320px); }
        100% { transform: translateY(0); }
    }

    /* --- [카드 및 스텝 섹션] --- */
    .card {
        background-color: white; padding: 30px 20px; border-radius: 12px;
        border: 1px solid #e0e0e0; box-shadow: 2px 2px 12px rgba(0,0,0,0.05);
        display: flex; flex-direction: column; justify-content: center;
        align-items: center; height: 280px; text-align: center;
    }
    .step-box {
        background-color: #ffffff; border: 2px solid #007bff; border-radius: 50px;
        padding: 10px 20px; text-align: center; font-weight: bold; color: #007bff;
    }

    /* --- [모의테스트 전용 스타일] --- */
    .q-card {
        background-color: #ffffff; padding: 15px 20px; border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05); border-left: 5px solid #007bff;
        margin-top: 20px; margin-bottom: 5px; text-align: left;
    }
    .q-text { font-size: 1rem; font-weight: bold; color: #1e293b; }
    div[role="radiogroup"] label { font-size: 0.85rem !important; white-space: nowrap !important; }
    
    .notice-box {
        background-color: #f1f1f1; padding: 20px; border-radius: 8px;
        font-size: 13px; color: #666; margin-top: 60px; line-height: 1.6;
    }
    </style>
    """, unsafe_allow_html=True)

# ------------------------------------------------------------------
# [화면 1: 메인 대시보드]
# ------------------------------------------------------------------
if st.session_state.page == "home":
    # --- 상단 타이틀 ---
    st.markdown("""
        <div class='header-container'>
            <h1 style='font-size: 40px;'>수출역량진단 서비스</h1>
            <p style='font-size: 18px; color: #555;'>나에게 맞는 지원서비스를 활용하여 수출 역량을 Upgrade!</p>
        </div>
        """, unsafe_allow_html=True)

    # --- 버튼 섹션 ---
    col_l, col_btn1, col_btn2, col_r = st.columns([0.6, 1, 1, 0.6])
    with col_btn1:
        if st.button("모의 테스트 시작", key="mock_test_btn"):
            st.session_state.page = "mock_test"
            st.rerun()

    with col_btn2:
        if st.button("평가보고서 신청하기", key="top_btn"):
            st.toast("신청 페이지로 이동합니다.")

    st.markdown("<br><hr>", unsafe_allow_html=True)

    # --- 서비스 소개 (카드 섹션) ---
    st.markdown("<h2 style='text-align:center;'>빅데이터 기반 수출역량 진단보고서 제공</h2>", unsafe_allow_html=True)
    card_col1, card_col2, card_col3 = st.columns(3)
    with card_col1:
        st.markdown('<div class="card"><h3>01</h3><div style="font-size:50px;">📊</div><p><b>수출 / 경영 / 기술</b><br>파트별 역량진단</p></div>', unsafe_allow_html=True)
    with card_col2:
        st.markdown('<div class="card"><h3>02</h3><div style="font-size:50px;">📋</div><p>항목별 세분화된<br><b>분석 리포트</b> 제공</p></div>', unsafe_allow_html=True)
    with card_col3:
        st.markdown('<div class="card"><h3>03</h3><div style="font-size:50px;">💡</div><p>맞춤형<br><b>지원 서비스</b> 추천</p></div>', unsafe_allow_html=True)

    # --- 후기 알림바 ---
    st.markdown("""
        <div class="review-ticker-container">
            <div class="review-wrapper">
                <div class="review-item"><span style="font-size:22px;">🔔</span><div style="display:flex; flex-direction:column;"><span style="font-size:13px; color:#888;">김*우 대표님 | 방금 전</span><span class="review-text">"우리 회사에 딱 맞는 지원사업을 바로 찾았어요! 📈"</span></div></div>
                <div class="review-item"><span style="font-size:22px;">🔔</span><div style="display:flex; flex-direction:column;"><span style="font-size:13px; color:#888;">이*민 팀장님 | 2분 전</span><span class="review-text">"보고서 분석 내용이 생각보다 훨씬 정교해서 놀랐습니다. 👍"</span></div></div>
                <div class="review-item"><span style="font-size:22px;">🔔</span><div style="display:flex; flex-direction:column;"><span style="font-size:13px; color:#888;">(주)테크솔루션 | 10분 전</span><span class="review-text">"수출 전략 짜는 데 이만한 서비스가 없네요. 강력 추천합니다! 🔥"</span></div></div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    # --- 서비스 이용 방법 ---
    st.markdown("<br><h3 style='text-align:center;'>서비스 이용 방법</h3><br>", unsafe_allow_html=True)
    step_cols = st.columns([1, 0.2, 1, 0.2, 1, 0.2, 1, 0.2, 1])
    steps = ["로그인", "서비스 신청", "정성 평가 질문", "평가진행", "결과 확인"]
    for i, step in enumerate(steps):
        with step_cols[i*2]: st.markdown(f'<div class="step-box">{step}</div>', unsafe_allow_html=True)
        if i < len(steps)-1:
            with step_cols[i*2+1]: st.markdown("<p style='text-align:center; padding-top:12px;'>➡</p>", unsafe_allow_html=True)

    # --- 하단 주의사항 ---
    st.markdown("""
        <div class="notice-box">
            <b>💡 서비스 이용 주의사항</b><br>
            본 수출역량 진단은 신용정보법 제15조 1항에 의거하여 기업의 신용정보를 수집하고 처리할 수 있습니다. 
            적법한 절차에 의해 수집된 정보를 활용하며, 제공되는 리포트는 참고용으로 공식적인 증빙 서류로의 활용은 제한될 수 있습니다.
        </div>
        """, unsafe_allow_html=True)

# ------------------------------------------------------------------
# [화면 2: 모의 테스트 페이지]
# ------------------------------------------------------------------
elif st.session_state.page == "mock_test":
    st.markdown("<h2 style='text-align: center;'>수출역량진단 모의테스트</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #666;'>현재 기업의 상황을 객관적으로 선택해 주세요.</p>", unsafe_allow_html=True)
    
    questions = [
        "1. 시장 조사 : 수출 희망 국가의 시장 트렌드 및 경쟁사 현황 파악",
        "2. 전담 인력 : 외국어 상담 및 무역 실무 수행 전담 인력 보유",
        "3. 홍보 인프라 : 영문 홈페이지/카탈로그 등 바이어용 홍보 수단",
        "4. 인증 및 지재권 : 수출국 요구 인증(CE, FDA 등) 및 상표권 보유",
        "5. 생산 능력 : 수출 주문 증가 시 감당 가능한 생산/공급망",
        "6. 네트워킹 : 해외 전시회 참여 경험 및 바이어 DB 보유",
        "7. 무역 실무 : 인코텀즈 및 대금 결제 방식 숙지",
        "8. 물류 체계 : 포워더 파트너십 등 물류 프로세스 구축",
        "9. 제품 경쟁력 : 현지 제품 대비 가격/품질 차별성",
        "10. 재무 여력 : 초기 마케팅 및 현지화 비용 여력"
    ]
    options_map = {1: "전혀아님", 2: "아님", 3: "보통", 4: "그럼", 5: "매우그럼"}

    with st.form("mock_diagnosis_form"):
        user_answers = []
        for i, q in enumerate(questions):
            st.markdown(f'<div class="q-card"><span class="q-text">{q}</span></div>', unsafe_allow_html=True)
            score = st.radio(f"q_{i}", options=[1, 2, 3, 4, 5], 
                             format_func=lambda x: f"{x}점 ({options_map[x]})",
                             index=2, horizontal=True, label_visibility="collapsed", key=f"r_{i}")
            user_answers.append(score)
        
        col_submit1, col_submit2 = st.columns(2)
        with col_submit1:
            submit_button = st.form_submit_button("진단 결과 확인하기")
        with col_submit2:
            if st.form_submit_button("홈으로 돌아가기"):
                st.session_state.page = "home"
                st.rerun()

    if submit_button:
        total_score = sum(user_answers)
        st.markdown("---")
        st.markdown(f"<h2 style='text-align: center;'>📊 진단 결과: 총점 {total_score}점</h2>", unsafe_allow_html=True)
        
        if total_score <= 20:
            st.error("### [1단계] 수출 내수기업\n💡 **전략:** 내수 비중이 높습니다. 기초적인 홍보물 구축이 시급합니다.")
        elif total_score <= 30:
            st.warning("### [2단계] 수출 유망기업\n💡 **전략:** 기초는 갖춰졌습니다. 타겟 시장 인증 획득에 집중하세요.")
        elif total_score <= 40:
            st.success("### [3단계] 수출 성장기업\n💡 **전략:** 즉시 수출 가능 역량입니다. 본격적인 현지 마케팅을 추진하세요.")
        else:
            st.balloons()
            st.success("### [4단계] 수출 강소기업\n💡 **전략:** 글로벌 경쟁력이 우수합니다. 브랜드 강화에 집중하세요.")
            
        if st.button("테스트 다시 하기"):
            st.rerun()