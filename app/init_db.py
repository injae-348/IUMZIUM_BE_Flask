from app import db
from app.models import Menu

def insert_initial_data():
    db.create_all()  # 테이블 생성

    # 기본 데이터 삽입
    if not Menu.query.first():  # 테이블이 비어있다면 데이터 삽입
        initial_data = [
            {'name': '아메리카노', 'price': 4000, 'category': '커피', 'image_name': 'americano.png'},
            {'name': '카페라떼', 'price': 4500, 'category': '커피', 'image_name': 'caffelatte.png'},
            {'name': '연유라떼', 'price': 5000, 'category': '커피', 'image_name': 'condensedmilk_latte.png'},
            {'name': '바닐라라떼', 'price': 4800, 'category': '커피', 'image_name': 'vanilla_latte.png'},
            {'name': '카푸치노', 'price': 4500, 'category': '커피', 'image_name': 'cappuccino.png'},
            {'name': '카라멜마끼야또', 'price': 5000, 'category': '커피', 'image_name': 'caramel_macchiato.png'},
            {'name': '카페모카', 'price': 4700, 'category': '커피', 'image_name': 'caffe_mocha.png'},
            {'name': '아인슈페너', 'price': 5500, 'category': '커피', 'image_name': 'eiskaffee.png'},
            {'name': '복숭아티', 'price': 3500, 'category': '차', 'image_name': 'peach_tea.png'},
            {'name': '리치캐모마일', 'price': 4000, 'category': '차', 'image_name': 'lychee_camomile.png'},
            {'name': '청귤얼그레이', 'price': 3800, 'category': '차', 'image_name': 'green_citrus_earlgrey.png'},
            {'name': '트리플민트', 'price': 3600, 'category': '차', 'image_name': 'triple_mint.png'},
            {'name': '애플히비스커스', 'price': 3700, 'category': '차', 'image_name': 'apple_hibiscus.png'},
            {'name': '허나유자티', 'price': 3900, 'category': '차', 'image_name': 'honey_yuja_tea.png'},
            {'name': '허니자몽티', 'price': 4000, 'category': '차', 'image_name': 'honey_persimmon_tea.png'},
            {'name': '허니레몬티', 'price': 3800, 'category': '차', 'image_name': 'honey_lemon_tea.png'},
            {'name': '레몬에이드', 'price': 4000, 'category': '에이드', 'image_name': 'lemonade.png'},
            {'name': '하비스커스에이드', 'price': 4200, 'category': '에이드', 'image_name': 'hibiscus_aid.png'},
            {'name': '블루베리에이드', 'price': 4500, 'category': '에이드', 'image_name': 'blueberry_aid.png'},
            {'name': '자몽에이드', 'price': 4300, 'category': '에이드', 'image_name': 'grapefruit_aid.png'}
        ]       

        for item in initial_data:
            menu_item = Menu(name=item['name'], price=item['price'], category=item['category'], image_name=item['image_name'])
            db.session.add(menu_item)
        db.session.commit()
