# class Speed():
#     def __init__(self):
#         self.speed=10 #public variable(acceced by outside of world)
#         self.__speed_limit=20#privat variable(acceced only member function)
#     def get_speed(self):
#         return self.speed
#     def get_speed_limit(self):
#         return self.__speed_limit
#     def set_speed_limit(self, new_speed):
#         self.__speed_limit=new_speed
# s=Speed()
# s.speed=100
# s.__speed_limit=23 #no effect
# s.set_speed_limit(80)
# print(s.get_speed(),s.get_speed_limit())


# class BankAccount:
#     bank_name = "CCCC"
#     interest_Rate = 8.00
#     def __init__(self,acc_name,acc_num,balance):
#         self.__acc_num = acc_num
#         self.__acc_name = acc_name
#         self.__balance = balance
#     def get_acc_name(self):
#         return self.__acc_name
#     def set_name(self,new_name):
#        self.__acc_name = new_name
#     def get_acc_num(self):
#        return self.__acc_num
#     def get_balance(self):
#        return self.__balance
#     def set_balance(self,new_balance):
#        self.__balance = new_balance
#     def add_money(self,deposit_amt):
#        self.__balance += deposit_amt
#        print("The amount is deposited, your new balance is",self.__balance)
#     def withdraw_money(self,withdraw_amt):
#        if withdraw_amt <= self.__balance:
#            self.__balance -= withdraw_amt
#            print("The amount withdrawn, final balance is",self.__balance)
#        else:
#            print("Insufficient balance")

# millionaire = BankAccount("abs",1324,1000000000)
# # millionaire.__acc_name="nmm"
# # millionaire.set_name("qwe")
# # print(millionaire.get_acc_name())

# # millionaire.__acc_num=12345
# # print(millionaire.get_acc_num())

# millionaire.__balance=345678
# millionaire.set_balance(120000)
# millionaire.add_money(500)
# millionaire.withdraw_money(130000)
# millionaire.withdraw_money(2000)
# print(millionaire.get_balance())
