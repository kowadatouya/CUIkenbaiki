import keyboard
from human import Human
class Admin:
    def __init__(self):
        self.special = 1000
        self.special_pieces = 0
        self.special_sum = 0
        self.soi = 780
        self.soi_pieces = 0
        self.soi_sum = 0
        self.salt = 880
        self.salt_pieces = 0
        self.salt_sum = 0
        self.rice = 150
        self.rice_pieces = 0
        self.rice_sum = 0
    def get_key_input(self):
        while True:
            if keyboard.is_pressed('enter'):
                return 'enter'
            if keyboard.is_pressed('esc'):
                return 'esc'
    def menu(self):
        print('***********************')
        print('       管理画面')
        print('***********************')
        print('======= 商品一覧 =======')
        print('商品      単価  販売数  売上金額')
        print('=======================')
        print(f'1.特製ラーメン {self.special}円  {self.special_pieces}   {self.special_sum}')
        print(f'2.醤油ラーメン {self.soi}円   {self.soi_pieces}      {self.soi_sum}')
        print(f'3.しおラーメン {self.salt}円     {self.salt_pieces}     {self.salt_sum}')
        print(f'4.ごはん {self.rice}円      {self.rice_pieces}        {self.rice_sum} ')
        print('———')
        print('総売上金額 80,700円')
        print('=== 管理メニュー ====')
        print('1. 売上をリセットする')
        print('2. 商品の価格を変更する')
        print('※売上がリセットされていないと利用できません。')
        print('3. 管理画面を終了する')
        print('———')
        self.admin_user()
    def command1(self):
        print("管理コード入力:1")
        print("===")
        self.special_pieces = 0
        self.special_sum = 0
        self.soi_pieces = 0
        self.soi_sum = 0
        self.salt_pieces = 0
        self.salt_sum = 0
        self.rice_pieces = 0
        self.rice_sum = 0
        print("売上をリセットしました。")
        self.menu()
    def command2(self):
        print('管理コード入力:2')
        print('======= 商品一覧 =======')
        print('商品      単価  販売数  売上金額')
        print('=======================')
        print('1.特製ラーメン 1000円  0   0円')
        print('2.醤油ラーメン 780円   0     0円')
        print('3.しおラーメン 880円     0     0円')
        print('4.ごはん 150円      0     0円')
        print('———')
        input('価格を変更する商品の番号を入力してください。>')
        input('変更金額を入力してください。>')
        print('【2.醤油ラーメン 800円】に変更します。')
        print('よろしいですか(Y/N）>')
        print('変更しました。')
        self.menu()
    def command3(self):
        print('管理コード入力:3 （Enterキー押下でタイトル画面の表示に戻る）')
        key = self.get_key_input()
        if key == 'enter':
            title()
    def admin_user(self):
        admin = input()
        if admin == 1:
            self.command1()
        elif admin == 2:
            self.command2
        elif admin == 3:
            self.command3()
