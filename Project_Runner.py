from Lab8_Login import main_call as login
from Lab8_B import main_call as lab_b
from Lab8_C import main_call as lab_c
from Lab8_D import main_call as lab_d
from Lab8_AdminPage import main_call as admin


def admin_loop():
    while True:
        #   opens respective gui based on button pressed
        match admin():
            case 1:
                break
            case "info":
                lab_b()
            case "payroll":
                lab_c()
            case "account":
                lab_d()


def main():
    while True:
        #   opens login gui, then opens respective gui based on user account type
        match login()[4]:
            case "Quit":
                break
            case "HR":
                lab_b()
            case "Accounting":
                lab_c()
            case "Employee":
                lab_d()
            case "Admin":
                admin_loop()


if __name__ == "__main__":
    main()
