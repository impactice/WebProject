app.py 수정

@app.route('/building/<int:id>')
def building_page(id):
    # id가 1~99 사이일 때만 처리 (필요시 예외 처리 가능)
    if not (1 <= id <= 99):
        return "존재하지 않는 건물입니다.", 404
    template_name = f'building/B{id:02d}.html'  # building/B01.html, B02.html ...
    return render_template(template_name)

를 추가

==============================

index.html 수정

<li><a href="{{ url_for('building_page', id=1) }}">1호관 (건물명 1)</a></li>

li 테그 url 수정

================================

building 폴더는 templates폴더 안에 넣기

buildingC 폴더는 staric 안에 넣기

