이미지/ 안에 buildingI 폴더 통째로 넣기

<!DOCTYPE html>
<html lang="ko">

<head>
    <meta charset="UTF-8">
    <title>회원 관리 및 문의 게시판</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
    <link rel="stylesheet" href="{{ url_for('static', filename='image_slider.css') }}">
    <style>
        /* style.css로 이동할 스타일 정의는 여기에서 제외 */
    </style>
</head>

<body>
    <div class="top-section">
        <div class="top-section-text">
            <h1>안녕하세요!</h1>
            <p>회원 관리 및 문의 게시판 웹사이트입니다.</p>
        </div>
        <div class="top-section-links">
            {% if current_user.is_authenticated %}
            <a href="{{ url_for('board') }}">문의 게시판</a>
            <a href="{{ url_for('logout') }}">로그아웃</a>
            {% else %}
            <a href="{{ url_for('register') }}">회원 가입</a>
            <a href="{{ url_for('login') }}">로그인</a>
            {% endif %}
        </div>
    </div>

    <div class="main-content-wrapper">
        <div class="left-space board-preview">
            <h2>최근 게시글</h2>
            <ul>
                {% for post in recent_posts %}
                <li><a href="{{ url_for('view', id=post.id) }}">{{ post.title }}</a></li>
                {% else %}
                <li>최근 게시글이 없습니다.</li>
                {% endfor %}
            </ul>
            <a href="{{ url_for('board') }}" class="view-all-board">게시판 전체 보기</a>
        </div>
        <div class="image-slider-container">
            <div class="image-slider">
                <img src="{{ url_for('static', filename='images/school.png') }}" alt="학교 이미지 1">
                <img src="{{ url_for('static', filename='images/map.png') }}" alt="학교 지도 실물물">
                <img src="{{ url_for('static', filename='images/lib_in.png') }}" alt="부산 도시 이미지">
            </div>
            <button class="prev-button">&lt;</button>
            <button class="next-button">&gt;</button>
        </div>
        <div class="right-space">
            <ul class="building-list">
                <li><a href="{{ url_for('building_page', id=1) }}">1호관 (건물명 1)</a></li>
                <li><a href="/building/2">2호관   (건물명 2)</a></li>
                <li><a href="/building/3">3호관   (건물명 3)</a></li>
                <li><a href="/building/4">4호관   (건물명 4)</a></li>
                <li><a href="/building/5">5호관   (건물명 5)</a></li>
                <li><a href="/building/6">6호관   (건물명 6)</a></li>
                <li><a href="/building/7">7호관   (건물명 7)</a></li>
                <li><a href="/building/8">8호관   (건물명 8)</a></li>
                <li><a href="/building/9">9호관   (건물명 9)</a></li>
                <li><a href="/building/10">10호관(건물명 10)</a></li>
                <li><a href="/building/11">11호관 (건물명 11)</a></li>
                <li><a href="/building/12">12호관 (건물명 12)</a></li>
                <li><a href="/building/13">13호관 (건물명 13)</a></li>
                <li><a href="/building/14">14호관 (건물명 14)</a></li>
                <li><a href="/building/15">15호관 (건물명 15)</a></li>
                <li><a href="/building/16">16호관 (건물명 16)</a></li>
                <li><a href="/building/17">17호관 (건물명 17)</a></li>
                <li><a href="/building/18">18호관 (건물명 18)</a></li>
                <li><a href="/building/19">19호관 (건물명 19)</a></li>
                <li><a href="/building/20">20호관 (건물명 20)</a></li>
                <li><a href="/building/21">21호관 (건물명 21)</a></li>
                <li><a href="/building/22">22호관 (건물명 22)</a></li>
                <li><a href="/building/23">23호관 (건물명 23)</a></li>
                <li><a href="/building/24">24호관 (건물명 24)</a></li>
                <li><a href="/building/25">25호관 (건물명 25)</a></li>
                <li><a href="/building/26">26호관 (멀티미디어 정보관)</a></li>
                <li><a href="/building/27">27호관 (중앙도서관)</a></li>
                <li><a href="/building/28">28호관 (건물명 28)</a></li>
                <li><a href="/building/29">29호관 (건물명 29)</a></li>
                <li><a href="/building/30">30호관 (건물명 30)</a></li>
            </ul>
        </div>
    </div>

    <div class="main-section" style="display:none;">
    </div>

    <script src="{{ url_for('static', filename='image_slider.js') }}"></script>
</body>

</html>
