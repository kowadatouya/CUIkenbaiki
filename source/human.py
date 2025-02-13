import keyboard
from .admin import Admin

class Human:
    def __init__(self):
        self.items = {
            "1": {"name": "特製ラーメン", "price": 1000},
            "2": {"name": "醤油ラーメン", "price": 780},
            "3": {"name": "しおラーメン", "price": 880},
            "4": {"name": "ごはん", "price": 150}
        }
        self.items_in_cart = {}

    def title(self):
        print("***********************")
        print("券売機シミュレータ")
        print("***********************")
        print("Please Enter (Enterキー押下で画面がクリアされて処理が進む）")
        print("（ESCキー押下で管理画面に処理が進む）")
        print("（qキー押下でシミュレータ終了）\n")

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
                    self.title()
                    self.shop()
                    return
                elif payment < total:
                    print("———")
                    print("金額が不足しています。")
                    self.title()
                    self.shop()
                    return
                else:
                    change = payment - total
                    print("———")
                    print(f"ご購入ありがとうございます。おつり{change}円です。")
                    break
            except ValueError:
                print("整数で金額を入力してください。")

vm = Human()
vm.title()
vi= Admin()
def get_key_input():
    while True:
        if keyboard.is_pressed("esc"):
            return "esc"
        if keyboard.is_pressed("enter"):
            return "enter"
        if keyboard.is_pressed("q"):
            return "q"
key_pressed = get_key_input()
if key_pressed == "esc":
    vi.menu()
elif key_pressed == "enter":
    vm.shop()
elif key_pressed == "q":
    print("qキーが押されました。qキー押下でシミュレータ終了")