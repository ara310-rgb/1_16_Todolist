import streamlit as st

# 1. 페이지 설정
st.set_page_config(page_title="수출역량진단 서비스", layout="wide")

# 세션 상태 초기화
if 'page' not in st.session_state:
    st.session_state.page = "home"

# 2. 커스텀 CSS 적용
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@300;400;500;700;800&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Noto+Sans+KR', sans-serif;
    }

    .main { background-color: #ffffff; }
    .header-container { text-align: center; margin-bottom: 30px; }

    /* 프리미엄 무역 이모지 티커 디자인 */
    .premium-emoji-container {
        width: 100%; overflow: hidden; background: transparent; 
        padding: 40px 0; margin-bottom: 50px; position: relative;
    }
    .emoji-track {
        display: flex; width: calc(180px * 20); 
        animation: scroll-premium 25s linear infinite;
    }
    .premium-emoji-card {
        width: 130px; height: 130px; margin: 0 25px;
        background: rgba(255, 255, 255, 0.4);
        backdrop-filter: blur(8px);
        border-radius: 30% 70% 70% 30% / 30% 30% 70% 70%;
        border: 1px solid rgba(0, 123, 255, 0.1);
        display: flex; align-items: center; justify-content: center;
        box-shadow: 0 15px 35px rgba(0, 0, 0, 0.05), 
                    inset 0 0 15px rgba(255, 255, 255, 0.5);
        animation: organic-morph 6s ease-in-out infinite;
        transition: transform 0.3s ease;
    }
    .premium-emoji-card:hover {
        transform: scale(1.15) rotate(5deg);
        background: rgba(255, 255, 255, 0.7);
        border: 1px solid rgba(0, 123, 255, 0.3);
    }
    .emoji-icon { font-size: 60px; filter: drop-shadow(5px 10px 15px rgba(0,0,0,0.15)); }

    @keyframes scroll-premium {
        0% { transform: translateX(0); }
        100% { transform: translateX(calc(-180px * 10)); }
    }
    @keyframes organic-morph {
        0%, 100% { border-radius: 30% 70% 70% 30% / 30% 30% 70% 70%; transform: translateY(0); }
        50% { border-radius: 50% 50% 30% 70% / 50% 60% 40% 50%; transform: translateY(-20px); }
    }

    /* 버튼 디자인 */
    div.stButton > button {
        background-color: #007bff; color: white; padding: 10px 0px;
        border-radius: 8px; font-weight: bold; border: none; transition: 0.3s; 
        display: block;
    }
    div.stButton > button:hover { background-color: #0056b3; color: white; }

    /* 섹션 공통 제목 */
    .section-title-custom {
        text-align: center; font-size: 26px; font-weight: 800; 
        color: #1e293b; margin-bottom: 30px; margin-top: 20px;
    }

    /* 왜 수출역량진단이 필요한가요? 그리드 */
    .grid-container {
        max-width: 900px; margin: 0 auto; display: grid;
        grid-template-columns: 1fr 1fr; gap: 25px; padding: 20px 0;
    }
    .feature-box {
        background-color: #ffffff; padding: 40px 30px; border-radius: 20px;
        border: 1px solid #f0f0f0; text-align: center;
        box-shadow: 0 10px 20px rgba(0, 0, 0, 0.05); 
        transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1);
        min-height: 240px; display: flex; flex-direction: column; justify-content: center;
    }
    .feature-box:hover { transform: translateY(-10px); box-shadow: 0 15px 30px rgba(0, 123, 255, 0.15); }
    .feature-icon { font-size: 50px; margin-bottom: 15px; } 
    .feature-title { font-size: 22px; font-weight: 800; color: #1a202c; margin-bottom: 12px; }
    .feature-desc { font-size: 16px; color: #4a5568; line-height: 1.6; }

    /* 진단보고서 카드 (음영 및 호버 애니메이션) */
    .report-card {
        background-color: white; padding: 35px 20px; border-radius: 20px;
        border: 1px solid rgba(0, 123, 255, 0.05);
        box-shadow: 0 10px 30px rgba(0, 123, 255, 0.07); 
        display: flex; flex-direction: column; justify-content: center;
        align-items: center; height: 300px; text-align: center;
        transition: all 0.4s cubic-bezier(0.165, 0.84, 0.44, 1);
    }
    .report-card:hover {
        transform: translateY(-12px);
        box-shadow: 0 20px 45px rgba(0, 123, 255, 0.12);
        border: 1px solid rgba(0, 123, 255, 0.2);
    }
    .report-card h4 { color: #007bff; font-size: 22px; margin-bottom: 10px; font-weight: 800; }

    /* 이용 방법 (은은한 음영 추가) */
    .step-wrapper { display: flex; justify-content: space-between; align-items: center; gap: 12px; margin-top: 20px; }
    .step-card {
        flex: 1; background: white; border: 1px solid #f1f5f9;
        border-radius: 18px; padding: 25px 10px; text-align: center;
        box-shadow: 0 8px 20px rgba(148, 163, 184, 0.12); 
        transition: all 0.3s ease;
    }
    .step-card:hover { transform: translateY(-5px); box-shadow: 0 12px 25px rgba(148, 163, 184, 0.2); }
    .step-num { font-size: 11px; color: #3b82f6; font-weight: 800; margin-bottom: 8px; display: block; }
    .step-txt { font-size: 15px; font-weight: 700; color: #334155; }
    .step-arrow { color: #cbd5e1; font-size: 22px; }

    /* 리뷰 티커 */
    .review-ticker-container {
        width: 100%; margin: 40px auto; height: 85px; overflow: hidden;
        background: linear-gradient(135deg, #ffffff 0%, #f0f7ff 100%); 
        border-radius: 15px; border: 1.5px solid rgba(0, 123, 255, 0.2); 
        box-shadow: 0 10px 25px rgba(0, 123, 255, 0.1); padding: 0 30px; 
        display: flex; align-items: center;
    }
    .review-wrapper { display: flex; flex-direction: column; animation: ticker-slide 10s infinite; }
    .review-item { height: 85px; display: flex; align-items: center; gap: 15px; }

    @keyframes ticker-slide {
        0%, 15% { transform: translateY(0); }
        20%, 35% { transform: translateY(-85px); }
        40%, 55% { transform: translateY(-170px); }
        60%, 75% { transform: translateY(-255px); }
        80%, 95% { transform: translateY(-340px); }
        100% { transform: translateY(0); }
    }
    
    .section-spacer { height: 80px; }
    .fixed-layout-container { max-width: 900px; margin: 0 auto; padding: 20px; }

    /* [고급화] 섹션 5: 안내 사항 디자인 업데이트 (정적 디자인) */
    .notice-container {
        background-color: #f8fafc; 
        border: 1px solid #e2e8f0;
        border-radius: 16px; 
        padding: 30px 35px; 
        margin-top: 40px;
        position: relative;
    }
    .notice-header { 
        display: flex; 
        align-items: center; 
        gap: 10px; 
        margin-bottom: 16px;
        color: #1e293b;
    }
    .notice-icon { font-size: 20px; }
    .notice-title-text { 
        font-size: 18px; 
        font-weight: 700; 
        letter-spacing: -0.5px;
    }
    .notice-body { 
        font-size: 15px; 
        color: #475569; 
        line-height: 1.8; 
        word-break: keep-all;
        font-weight: 400;
    }
    .notice-highlight {
        color: #007bff;
        font-weight: 600;
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

    # 이모지 배너
    st.markdown('''
    <div class="premium-emoji-container">
        <div class="emoji-track">
            <div class="premium-emoji-card"><span class="emoji-icon">🚢</span></div>
            <div class="premium-emoji-card"><span class="emoji-icon">✈️</span></div>
            <div class="premium-emoji-card"><span class="emoji-icon">🌐</span></div>
            <div class="premium-emoji-card"><span class="emoji-icon">📦</span></div>
            <div class="premium-emoji-card"><span class="emoji-icon">🛳️</span></div>
            <div class="premium-emoji-card"><span class="emoji-icon">🗺️</span></div>
            <div class="premium-emoji-card"><span class="emoji-icon">🌍</span></div>
            <div class="premium-emoji-card"><span class="emoji-icon">🏗️</span></div>
            <div class="premium-emoji-card"><span class="emoji-icon">📄</span></div>
            <div class="premium-emoji-card"><span class="emoji-icon">⚓</span></div>
            <div class="premium-emoji-card"><span class="emoji-icon">🚢</span></div>
            <div class="premium-emoji-card"><span class="emoji-icon">✈️</span></div>
            <div class="premium-emoji-card"><span class="emoji-icon">🌐</span></div>
            <div class="premium-emoji-card"><span class="emoji-icon">📦</span></div>
            <div class="premium-emoji-card"><span class="emoji-icon">🛳️</span></div>
            <div class="premium-emoji-card"><span class="emoji-icon">🗺️</span></div>
            <div class="premium-emoji-card"><span class="emoji-icon">🌍</span></div>
            <div class="premium-emoji-card"><span class="emoji-icon">🏗️</span></div>
            <div class="premium-emoji-card"><span class="emoji-icon">📄</span></div>
            <div class="premium-emoji-card"><span class="emoji-icon">⚓</span></div>
        </div>
    </div>
    ''', unsafe_allow_html=True)

    # [섹션 1: 왜 수출역량진단이 필요한가요?]
    st.markdown("<div class='section-title-custom'>왜 수출역량진단이 필요한가요?</div>", unsafe_allow_html=True)
    st.markdown('''
    <div class="grid-container">
        <div class="feature-box">
            <div class="feature-icon">🎯</div>
            <div class="feature-title">정밀 타겟팅</div>
            <div class="feature-desc">기업의 강점과 약점을 데이터로 객관화하여<br>최적의 진출 시장을 제시합니다.</div>
        </div>
        <div class="feature-box">
            <div class="feature-icon">⚡</div>
            <div class="feature-title">실시간 매칭</div>
            <div class="feature-desc">정부와 지자체에서 제공하는 최신<br>수출 지원사업을 즉시 추천합니다.</div>
        </div>
        <div class="feature-box">
            <div class="feature-icon">📈</div>
            <div class="feature-title">성장 가이드</div>
            <div class="feature-desc">단기적 성과를 넘어 장기적인 글로벌<br>성장 로드맵을 체계적으로 수립합니다.</div>
        </div>
        <div class="feature-box">
            <div class="feature-icon">🤝</div>
            <div class="feature-title">전문가 네트워킹</div>
            <div class="feature-desc">검증된 분야별 무역 전문가 및 컨설턴트와의<br>다이렉트 매칭 기회를 제공합니다.</div>
        </div>
    </div>
    ''', unsafe_allow_html=True)
    
    st.markdown('<div class="section-spacer"></div>', unsafe_allow_html=True)

    # [섹션 2: 리뷰 티커]
    st.markdown('''
    <div class="review-ticker-container"><div class="review-wrapper">
        <div class="review-item"><span>🔔</span><div><span style="font-size:12px; color:#007bff;">김*우 대표님 | 방금 전</span><br><span style="font-weight:700;">"우리 회사에 딱 맞는 지원사업을 바로 찾았어요! 📈"</span></div></div>
        <div class="review-item"><span>🔔</span><div><span style="font-size:12px; color:#007bff;">이*민 팀장님 | 2분 전</span><br><span style="font-weight:700;">"보고서 분석 내용이 훨씬 정교해서 놀랐습니다. 👍"</span></div></div>
        <div class="review-item"><span>🔔</span><div><span style="font-size:12px; color:#007bff;">박*현 본부장님 | 10분 전</span><br><span style="font-weight:700;">"수출 전략 수립에 실질적인 지표가 되어주네요. 대만족입니다. 🌏"</span></div></div>
    </div></div>
    ''', unsafe_allow_html=True)

    st.markdown('<div class="section-spacer"></div>', unsafe_allow_html=True)

    # [섹션 3: 진단보고서]
    st.markdown("<div class='section-title-custom'>빅데이터 기반 수출역량 진단보고서 제공</div>", unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    with c1: st.markdown('<div class="report-card"><h4>01</h4><div style="font-size:60px; margin-bottom:15px;">📊</div><p><b>수출 / 경영 / 기술</b><br>파트별 역량진단</p></div>', unsafe_allow_html=True)
    with c2: st.markdown('<div class="report-card"><h4>02</h4><div style="font-size:60px; margin-bottom:15px;">📋</div><p>항목별 세분화된<br><b>분석 리포트</b> 제공</p></div>', unsafe_allow_html=True)
    with c3: st.markdown('<div class="report-card"><h4>03</h4><div style="font-size:60px; margin-bottom:15px;">💡</div><p>맞춤형<br><b>지원 서비스</b> 추천</p></div>', unsafe_allow_html=True)

    st.markdown('<div class="section-spacer"></div>', unsafe_allow_html=True)

    # [섹션 4: 서비스 이용 방법]
    st.markdown("""
    <div class="fixed-layout-container">
        <div class='section-title-custom' style='margin-bottom:20px;'>서비스 이용 방법</div>
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

    st.markdown('<div class="section-spacer"></div>', unsafe_allow_html=True)

    # [섹션 5: 안내 사항 - 가독성 강화 디자인]
    st.markdown("""
    <div class="fixed-layout-container">
        <div class="notice-container">
            <div class="notice-header">
                <span class="notice-icon">💡</span>
                <span class="notice-title-text">서비스 이용 안내</span>
            </div>
            <div class="notice-body">
                본 서비스는 기업의 수출 역량을 객관적으로 진단하기 위해 <span class="notice-highlight">"신용정보의 이용 및 보호에 관한 법률"</span>을 준수합니다. <br>
                입력하신 모든 정보는 암호화되어 안전하게 관리되며, 보다 정밀한 진단 리포트 생성을 위해 적법한 절차에 따라 활용됩니다. <br>
                분석된 결과는 귀사의 <b>글로벌 시장 진출 전략 수립</b> 및 <b>정부 지원사업 매칭</b>을 위한 참고 자료로만 사용되오니 안심하고 이용하시기 바랍니다.
            </div>
        </div>
    </div>
    <br><br>
    """, unsafe_allow_html=True)

elif st.session_state.page == "mock_test":
    st.write("모의 테스트 페이지")
    if st.button("홈으로"): st.session_state.page = "home"; st.rerun()
elif st.session_state.page == "apply_report":
    st.write("보고서 신청 페이지")
    if st.button("홈으로"): st.session_state.page = "home"; st.rerun()