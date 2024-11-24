import re

def is_valid_phone(phone):
    return re.match(r'^010-\d{4}-\d{4}$', phone) is not None


def is_valid_email(email):
    return re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email) is not None


def modify_logic(contact):
    while True:
        try:
            choice = int(input("어떤 것을 수정하시겠습니까? 1. 이름 2. 전화번호 3. 이메일 : "))
        except ValueError:
            print("1~3번 중에서 입력해주세요!")
            continue

        if choice == 1:
            new_name = input("변경할 이름을 입력해주세요! : ")
            contact["name"] = new_name
            return contact
        if choice == 2:
            new_phone = input("변경할 전화번호를 입력해주세요! : ")
            contact["p_num"] = new_phone
            return contact
        if choice == 3:
            new_email = input("변경할 이메일을 입력해주세요! : ")
            contact["email"] = new_email
            return contact


def search_contact(contact_datas):
    target = input("검색할 이름 또는 전화번호를 입력하세요 : ")
    found = False
    for contact in contact_datas:
        if target == contact["p_num"] or target == contact["name"]:
            print(f"이름: {contact['name']} 전화번호: {contact['p_num']} 이메일: {contact['email']}")
            found = True
    if not found:
        print("결과가 없습니다.")
    print()


def modify_contact(contact_datas):
    print("=== 연락처 수정 ===")
    target = input("검색할 이름 또는 전화번호를 입력하세요 : ")
    found = False
    for i, contact in enumerate(contact_datas):
        if target == contact["p_num"] or target == contact["name"]:
            print(f"이름: {contact['name']} 전화번호: {contact['p_num']} 이메일: {contact['email']}")
            found = True
            contact_datas[i] = modify_logic(contact)
    if not found:
        print("결과가 없습니다.")
    print()
    return contact_datas


def add_contact(contact_datas):
    print("=== 연락처 추가 ===")
    while True:
        new_contact = {}
        name = input("이름 : ")
        if name == "":
            print("잘못된 이름입니다! 다시 입력해주세요!")
            continue
        else:
            new_contact["name"] = name

        while True:
            p_num = input("전화번호 : ")
            if any(contact['p_num'] == p_num for contact in contact_datas):
                print("이미 존재하는 전화번호입니다!")
                continue
            if is_valid_phone(p_num):
                new_contact["p_num"] = p_num
                break
            else:
                print("전화번호 형식이 올바르지 않습니다!")
                continue

        while True:
            email = input("이메일(선택) : ")
            if is_valid_email(email):
                new_contact["email"] = email
                break
                          
            elif email == "":
                new_contact["email"] = email
                break
            else:
                print("이메일 형식이 올바르지 않습니다!")
                continue 
        break

    print("연락처가 추가되었습니다!")
    print()
    return new_contact


def delete_contact(contact_datas):
    print("=== 연락처 검색 ===")
    target = input("검색할 이름 또는 전화번호를 입력하세요 : ")
    found = False
    for contact in contact_datas:
        if target == contact["p_num"] or target == contact["name"]:
            print(f"이름: {contact['name']} 전화번호: {contact['p_num']} 이메일: {contact['email']}")
            found = True
            contact_datas.remove(contact)
    if not found:
        print("결과가 없습니다.")
    print()
    return contact_datas


def print_contact(contact_datas):
    print("=== 연락처 전체 출력 ===")
    if contact_datas:
        for i, contact in enumerate(contact_datas):
            email = contact["email"] if contact["email"] else "입력하지 않음"
            print(f"[{i+1}] 이름 : {contact['name']} 전화번호 : {contact['p_num']} 이메일 : {email}")
    else:
        print("현재 연락처가 비어있습니다!")