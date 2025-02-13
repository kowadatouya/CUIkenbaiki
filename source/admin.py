import keyboard
import time
class Admin:
    def __init__(self):
        self.current_state = "admin"
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
        self.items = {
            "1": {"name": '特製ラーメン',"price":self.special,"pieces":self.special_pieces,"sum":self.special_sum},
            "2": {"name": '醤油ラーメン',"price":self.soi,"pieces":self.soi_pieces,"sum":self.soi_sum},
            "3": {"name": 'しおラーメン',"price":self.salt,"pieces":self.salt_pieces,"sum":self.salt_sum},
            "4": {"name": 'ごはん',"price":self.rice,"pieces":self.rice_pieces,"sum":self.rice_sum}
        }
        self.sum = self.special_sum + self.soi_sum + self.salt_sum + self.rice_sum
        self.items_in_cart = {}
    def menu(self):
        print('***********************')
        print('       管理画面')
        print('***********************')
        print('======= 商品一覧 =======')
        print('商品      単価  販売数  売上金額')
        print('=======================')
        for key, item in self.items.items():
            print(f"{key}.{item["name"]} {item["price"]}円 {item["pieces"]} {item["sum"]}円")
        print('———')
        print(f'総売上金額 {self.sum}円')
        print('=== 管理メニュー ====')
        print('1. 売上をリセットする')
        print('2. 商品の価格を変更する')
        print('※売上がリセットされていないと利用できません。')
        print('3. 管理画面を終了する')
        print('———')
        self.admin_user()
    def command1(self, skip_menu=False):
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
        if skip_menu == False:
            self.menu()
    def command2(self, skip_menu=False):
        print('======= 商品一覧 =======')
        print('商品      単価  販売数  売上金額')
        print('=======================')
        print(f'1.特製ラーメン {self.special}円  {self.special_pieces}   {self.special_sum}円')
        print(f'2.醤油ラーメン {self.soi}円   {self.soi_pieces}   {self.soi_sum}円')
        print(f'3.しおラーメン {self.salt}円   {self.salt_pieces}   {self.salt_sum}円')
        print(f'4.ごはん {self.rice}円      {self.rice_pieces}   {self.rice_sum}円')
        print('———')
        pieces = input('価格を変更する商品の番号を入力してください。>')
        change = input('変更金額を入力してください。>')
        print(f'【{pieces}. {self.items[pieces]["name"]} {change}円に変更します。')
        select = input('よろしいですか(Y/N）>')
        id = pieces
        if select == 'Y' or 'y':
            self.items[id]["price"] = change
            print('変更しました。')
        elif select == 'N' or 'n':
            print('キャンセルしました')
        if skip_menu == False:
            self.menu()
    
    def command3(self):
        def key_input(self):
            while True:
                if keyboard.is_pressed('enter'):
                    return 'enter'
        key = key_input()
        print('（Enterキー押下でタイトル画面の表示に戻る）')
        if key == 'enter':
            time.sleep(1)
            from human import Human
            self = self
            branch1 = self.items["1"]["price"]
            branch2 = self.items["2"]["price"]
            branch3 = self.items["3"]["price"]
            branch4 = self.items["4"]["price"]
            vi = Human(self)
            vi.title()
    def admin_user(self):
        admin = int(input('管理コード入力:'))
        if admin == 1:
            self.command1()
        elif admin == 2:
            self.command2()
        elif admin == 3:
            self.command3()
    def update_sales(self, item_name, quantity, price):
        if item_name in self.items:
            self.items[item_name]["pieces"] += quantity
            self.items[item_name]["sum"] += quantity * price