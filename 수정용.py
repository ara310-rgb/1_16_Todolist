import streamlit as st

# 1. 페이지 설정
st.set_page_config(page_title="수출역량진단 서비스", layout="wide")

# 세션 상태 초기화
if 'page' not in st.session_state:
    st.session_state.page = "home"

# 2. 커스텀 CSS 적용 (기존 스타일 유지)
st.markdown("""
    <style>
    .main { background-color: #ffffff; }
    .header-container { text-align: center; margin-bottom: 30px; }

    /* 버튼 디자인 */
    div.stButton > button {
        background-color: #007bff; color: white; padding: 10px 0px;
        border-radius: 8px; font-weight: bold; border: none; transition: 0.3s; 
        display: block;
    }
    div.stButton > button:hover { background-color: #0056b3; color: white; }

    /* 레이아웃 컨테이너 */
    .fixed-layout-container { max-width: 800px; margin: 0 auto; padding: 20px; }

    /* 섹션 4: 그리드 컨테이너 */
    .grid-container {
        max-width: 900px; margin: 0 auto; display: grid;
        grid-template-columns: 1fr 1fr; gap: 25px; padding: 20px 0;
    }
    .feature-box {
        background-color: #ffffff; padding: 40px 30px; border-radius: 20px;
        border: 1px solid #f0f0f0; text-align: center;
        box-shadow: 0 10px 20px rgba(0, 0, 0, 0.08); 
        transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1);
        min-height: 240px; display: flex; flex-direction: column; justify-content: center;
    }
    .feature-box:hover { transform: translateY(-10px); box-shadow: 0 15px 30px rgba(0, 123, 255, 0.2); }
    .feature-icon { font-size: 50px; margin-bottom: 15px; } 
    .feature-title { font-size: 22px; font-weight: 800; color: #1a202c; margin-bottom: 12px; }
    .feature-desc { font-size: 16px; color: #4a5568; line-height: 1.6; }

    /* 섹션 5: 이용 방법 */
    .step-wrapper { display: flex; justify-content: space-between; align-items: center; gap: 10px; margin-top: 10px; }
    .step-card {
        flex: 1; background: white; border: 1.5px solid #e2e8f0;
        border-radius: 15px; padding: 20px 10px; text-align: center;
        box-shadow: 0 4px 6px rgba(0,0,0,0.03); transition: all 0.2s ease;
    }
    .step-num { font-size: 13px; color: #007bff; font-weight: 800; margin-bottom: 5px; display: block; }
    .step-txt { font-size: 15px; font-weight: 700; color: #334155; }
    .step-arrow { color: #cbd5e1; font-size: 18px; font-weight: bold; }

    /* 섹션 6: 안내 사항 */
    .notice-box {
        background-color: #ffffff; border-left: 5px solid #e2e8f0;
        padding: 22px 28px; border-radius: 12px; margin-top: 25px;
        box-shadow: 4px 4px 15px rgba(0, 0, 0, 0.04), -1px -1px 10px rgba(0, 0, 0, 0.02);
    }
    .notice-title { font-size: 16px; font-weight: 700; color: #94a3b8; margin-bottom: 10px; display: flex; align-items: center; gap: 6px; }
    .notice-content { font-size: 14px; color: #64748b; line-height: 1.7; }

    /* 카드 및 티커 */
    .card {
        background-color: white; padding: 30px 20px; border-radius: 12px;
        border: 1px solid #e0e0e0; box-shadow: 2px 2px 12px rgba(0,0,0,0.05);
        display: flex; flex-direction: column; justify-content: center;
        align-items: center; height: 280px; text-align: center;
    }
    .review-ticker-container {
        width: 100%; margin: 40px auto; height: 85px; overflow: hidden;
        background: linear-gradient(135deg, #ffffff 0%, #f0f7ff 100%); 
        border-radius: 15px; border: 1.5px solid rgba(0, 123, 255, 0.2); 
        box-shadow: 0 10px 25px rgba(0, 123, 255, 0.1); padding: 0 30px; 
        display: flex; align-items: center;
    }
    .review-wrapper { display: flex; flex-direction: column; animation: ticker-slide 10s infinite; }
    .review-item { height: 85px; display: flex; align-items: center; gap: 15px; }
    .review-user-info { font-size: 12px; color: #007bff; font-weight: 500; }
    .review-text { font-size: 15px; font-weight: 700; color: #1e293b; }

    @keyframes ticker-slide {
        0%, 15% { transform: translateY(0); }
        20%, 35% { transform: translateY(-85px); }
        40%, 55% { transform: translateY(-170px); }
        60%, 75% { transform: translateY(-255px); }
        80%, 95% { transform: translateY(-340px); }
        100% { transform: translateY(0); }
    }
    </style>
    """, unsafe_allow_html=True)

# ------------------------------------------------------------------
# [화면 1: 메인 대시보드]
# ------------------------------------------------------------------
if st.session_state.page == "home":
    st.markdown("<div class='header-container'><h1 style='font-size: 40px;'>수출역량진단 서비스</h1><p style='font-size: 18px; color: #555;'>나에게 맞는 지원서비스를 활용하여 수출 역량을 Upgrade!</p></div>", unsafe_allow_html=True)

    col_l, col_btn1, col_btn2, col_r = st.columns([0.6, 1, 1, 0.6])
    with col_btn1:
        if st.button("모의 테스트 시작", key="mock_test_btn", use_container_width=True):
            st.session_state.page = "mock_test"; st.rerun()
    with col_btn2:
        if st.button("평가보고서 신청하기", key="top_btn", use_container_width=True):
            st.session_state.page = "apply_report"; st.rerun()

    st.markdown("<br><hr>", unsafe_allow_html=True)

    # ------------------------------------------------------------------
    # [변경 섹션 1: 왜 수출역량진단이 필요한가요?] (기존 섹션 4)
    # ------------------------------------------------------------------
    st.markdown("<h3 style='text-align:center;'>왜 수출역량진단이 필요한가요?</h3>", unsafe_allow_html=True)
    st.markdown('''
    <div class="grid-container">
        <div class="feature-box"><div class="feature-icon">🎯</div><div class="feature-title">정밀 타겟팅</div><div class="feature-desc">기업의 강점과 약점을 데이터로 객관화하여<br>최적의 진출 시장을 제시합니다.</div></div>
        <div class="feature-box"><div class="feature-icon">⚡</div><div class="feature-title">실시간 매칭</div><div class="feature-desc">정부와 지자체에서 제공하는 최신<br>수출 지원사업을 즉시 추천합니다.</div></div>
        <div class="feature-box"><div class="feature-icon">📈</div><div class="feature-title">성장 가이드</div><div class="feature-desc">단기적 성과를 넘어 장기적인 글로벌<br>성장 로드맵을 체계적으로 수립합니다.</div></div>
        <div class="feature-box"><div class="feature-icon">🤝</div><div class="feature-title">전문가 네트워킹</div><div class="feature-desc">검증된 분야별 무역 전문가 및 컨설턴트와의<br>다이렉트 매칭 기회를 제공합니다.</div></div>
    </div>
    ''', unsafe_allow_html=True)

    # 리뷰 티커 (중간 전환점)
    st.markdown('''
    <div class="review-ticker-container"><div class="review-wrapper">
        <div class="review-item"><span>🔔</span><div><span class="review-user-info">김*우 대표님 | 방금 전</span><br><span class="review-text">"우리 회사에 딱 맞는 지원사업을 바로 찾았어요! 📈"</span></div></div>
        <div class="review-item"><span>🔔</span><div><span class="review-user-info">이*민 팀장님 | 2분 전</span><br><span class="review-text">"보고서 분석 내용이 훨씬 정교해서 놀랐습니다. 👍"</span></div></div>
        <div class="review-item"><span>🔔</span><div><span class="review-user-info">박*현 본부장님 | 10분 전</span><br><span class="review-text">"수출 전략 수립에 실질적인 지표가 되어주네요. 대만족입니다. 🌏"</span></div></div>
    </div></div>
    ''', unsafe_allow_html=True)

    # ------------------------------------------------------------------
    # [변경 섹션 2: 빅데이터 기반 수출역량 진단보고서 제공]
    # ------------------------------------------------------------------
    st.markdown("<h2 style='text-align:center;'>빅데이터 기반 수출역량 진단보고서 제공</h2>", unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    with c1: st.markdown('<div class="card"><h3>01</h3><div style="font-size:50px;">📊</div><p><b>수출 / 경영 / 기술</b><br>파트별 역량진단</p></div>', unsafe_allow_html=True)
    with c2: st.markdown('<div class="card"><h3>02</h3><div style="font-size:50px;">📋</div><p>항목별 세분화된<br><b>분석 리포트</b> 제공</p></div>', unsafe_allow_html=True)
    with c3: st.markdown('<div class="card"><h3>03</h3><div style="font-size:50px;">💡</div><p>맞춤형<br><b>지원 서비스</b> 추천</p></div>', unsafe_allow_html=True)

    # [섹션 5: 서비스 이용 방법]
    st.markdown("""
    <div class="fixed-layout-container">
        <h3 style="text-align:center; margin-top: 40px; margin-bottom: 20px;">서비스 이용 방법</h3>
        <div class="step-wrapper">
            <div class="step-card"><span class="step-num">STEP 01</span><span class="step-txt">로그인</span></div>
            <div class="step-arrow">➡</div>
            <div class="step-card"><span class="step-num">STEP 02</span><span class="step-txt">서비스 신청</span></div>
            <div class="step-arrow">➡</div>
            <div class="step-card"><span class="step-num">STEP 03</span><span class="step-txt">정성 평가</span></div>
            <div class="step-arrow">➡</div>
            <div class="step-card"><span class="step-num">STEP 04</span><span class="step-txt">평가 진행</span></div>
            <div class="step-arrow">➡</div>
            <div class="step-card"><span class="step-num">STEP 05</span><span class="step-txt">결과 확인</span></div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # [섹션 6: 안내 사항]
    st.markdown("""
    <div class="fixed-layout-container">
        <div class="notice-box">
            <div class="notice-title">💡 안내드립니다</div>
            <div class="notice-content">
                입력하신 정보는 관련 법령에 따라 소중하게 관리됩니다. 본 서비스는 "신용정보법"에 의거하여 
                보다 정확한 진단 결과 제공을 위해 기업 정보를 적법하게 활용하고 있습니다. 
                전문적인 분석을 통해 최적의 수출 전략을 제안해 드리고 있으니 안심하고 이용해 주세요.
            </div>
        </div>
    </div>
    <br><br>
    """, unsafe_allow_html=True)

# [페이지 로직 생략]
elif st.session_state.page == "mock_test":
    st.markdown('<div class="fixed-layout-container">', unsafe_allow_html=True)
    st.write("모의 테스트 페이지 내용...")
    if st.button("← 홈으로 돌아가기"):
        st.session_state.page = "home"; st.rerun()

elif st.session_state.page == "apply_report":
    st.markdown('<div class="fixed-layout-container">', unsafe_allow_html=True)
    st.write("보고서 신청 페이지 내용...")
    if st.button("← 홈으로 돌아가기"):
        st.session_state.page = "home"; st.rerun()