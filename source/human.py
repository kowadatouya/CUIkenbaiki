# import keyboard
import os
import sys
import time
class Human:
    def __init__(self):
        self.current_state = "human"
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
        self.items_in_cart = {}
        self.price_initialized = False
        
        # if not self.price_initialized:
        #     self.special, self.soi, self.salt, self.rice = self.vi.update_price()
        #     self.price_initialized = True
        
        

    def title(self):
        print("***********************")
        print("券売機シミュレータ")
        print("***********************")
        print("Please Enter (Enterキー押下で画面がクリアされて処理が進む）")
        print("（ESCと入力で管理画面に処理が進む）")
        print("（qキー押下でシミュレータ終了）\n")
        key_pressed = input()
        if key_pressed == "esc" or key_pressed == "ESC":
            self.menu()
        elif key_pressed == "":
            time.sleep(1)
            os.system('cls')
            self.shop()
        elif key_pressed == "q":
            print("qキーが押されました。qキー押下でシミュレータ終了")
            sys.exit()
    def shop(self):
        print("商品      金額")
        print("=======================")
        for key, item in self.items.items():
            print(f"{key}.{item['name']} {item['price']}円")
        print("———")
        while True:
            human_select = input("購入する商品番号(支払いに進む場合はc)>")
            if human_select in self.items:
                if human_select in self.items_in_cart:
                    self.items_in_cart[human_select] += 1
                else:
                    self.items_in_cart[human_select] = 1
            elif human_select == "c":
                self.show_cart()
                self.pay()
                break

    def show_cart(self):
        print("———")
        print("商品        数量")
        for item_id, quantity in self.items_in_cart.items():
            item_name = self.items[item_id]["name"]
            print(f"{item_id}.{item_name}   {quantity}")
        total = self.total()
        print("===")
        print(f"合計{total}円")

    def total(self):
        total = 0
        for item_id, quantity in self.items_in_cart.items():
            total += self.items[item_id]["price"] * quantity
        return total

    def pay(self):
        total = self.total()
        while True:
            try:
                print("———")
                payment = int(input("現金を投入してください>"))
                if payment < 0:
                    print("———")
                    print("金額は正の数で入力してください。")
                    break
                elif payment < total:
                    print("———")
                    print("金額が不足しています。")
                    break
                else:
                    change = payment - total
                    print("———")
                    print(f"ご購入ありがとうございます。おつり{change}円です。")
                    self.update_admin()
                    break
            except ValueError:
                print("整数で金額を入力してください。")
        print("（Enterキー押下でタイトル画面の表示に戻る）")
        print("（qキー押下でシミュレータ終了）")
        key_pressed = input()
        if key_pressed == "":
            time.sleep(1)
            self.items_in_cart = {}
            self.title()
        elif key_pressed == "q":
            print("qキーが押されました。qキー押下でシミュレータ終了")
            
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
        self.sum = self.update_total_sum()
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
        for item in self.items.values():
            item["pieces"] = 0
            item["sum"] = 0
        self.update_total_sum()
        print("売上をリセットしました。")
        if skip_menu == False:
            self.menu()
    def all_sales_reset(self):
        for item in self.items.values():
            if item["pieces"] != 0 or item["sum"] != 0:
                return False
        return True
    def command2(self, skip_menu=False):
        if not self.all_sales_reset():
            print('販売数と売上がリセットされていないため、価格を変更できません。')
            self.menu()
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
        if select.lower() == 'y':
            self.items[pieces]["price"] = int(change)
            if pieces == '1':
                self.special = int(change)
            if pieces == '2':
                self.soi = int(change)
            if pieces == '3':
                self.salt = int(change)
            if pieces == '4':
                self.rice = int(change)
            print('変更しました。')
        elif select.lower() == 'n':
            print('キャンセルしました')
        if not skip_menu:
            self.menu()
    def command3(self):
        print('（Enterキー押下でタイトル画面の表示に戻る）')
        key = input()
        if key == '':
            time.sleep(1)
            self.title()
    def admin_user(self):
        admin = int(input('管理コード入力:'))
        if admin == 1:
            self.command1()
        elif admin == 2:
            self.command2()
        elif admin == 3:
            self.command3()
    def update_total_sum(self):
        special_sum = self.items["1"]["sum"]
        soi_sum = self.items["2"]["sum"]
        salt_sum = self.items["3"]["sum"]
        rice_sum = self.items["4"]["sum"]
        self.sum = special_sum + soi_sum + salt_sum + rice_sum
        return self.sum
        
    def update_admin(self):
        for item_id, quantity in self.items_in_cart.items():
            item_name = item_id
            item_price = self.items[item_id]["price"]
            self.update_sales(item_name, quantity, item_price)
        self.items_in_cart.clear()
    def update_sales(self, item_name, quantity, price):
        if item_name in self.items:
            self.items[item_name]["pieces"] += quantity
            self.items[item_name]["sum"] += quantity * price
    def update_price(self, item_name, item_price):
        if item_name == "特製ラーメン":
            self.special_price = item_price
            self.items["1"]["price"] = self.special_price
        if item_name == "醤油ラーメン":
            self.soi_price = item_price
            self.items["2"]["price"] = self.soi_price
        if item_name == "しおラーメン":
            self.salt_price = item_price
            self.items["3"]["price"] = self.salt_price
        if item_name == "ごはん":
            self.rice_price = item_price
            self.items["4"]["price"] = self.rice_price
if __name__ == '__main__':
   self = Human()
   self.title()