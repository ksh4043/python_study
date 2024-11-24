import contact_data as cd
import contact_logic as cl
import menu
import os

path = "E:\\python_study\\file_data"
file = "contacts.txt"
fullfile = os.path.join(path, file)

if __name__ == "__main__":
    if not os.path.isdir(path):
        os.mkdir(path)

# 연락처 불러오기
    contact_datas = cd.read_contacts(fullfile)

# 메인 메서드
    while True:
        menu.show_menu()
        try:
            choice = int(input("메뉴를 입력하세요 : "))
            if choice > 6 or choice < 1:
                print("잘못된 입력입니다! 다시 입력해주세요!")
                continue
        except:
            print("1~6번을 입력해주세요!")
            continue

        if choice == 1:
            contact_datas.append(cl.add_contact(contact_datas))
        elif choice == 2:
            cl.search_contact(contact_datas)
        elif choice == 3:
            contact_datas = cl.modify_contact(contact_datas)
        elif choice == 4:
            contact_datas = cl.delete_contact(contact_datas)
        elif choice == 5:
            cl.print_contact(contact_datas)
        else:
            print("프로그램을 종료합니다!")
            break

# 연락처 저장
    cd.write_contacts(contact_datas, fullfile)