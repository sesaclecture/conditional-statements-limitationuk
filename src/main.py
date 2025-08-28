"""
Implement User Management System
"""
# 초기 사용자 목록
users = {
    "uid1": {
        "name": "한정욱",
        "birth": "1998-07-15",
        "id": "user1",
        "password": "@pass1",
        "role": "viewer"
    },
    "uid2": {
        "name": "개발자",
        "birth": "1995-03-12",
        "id": "user2",
        "password": "@pass2",
        "role": "editor"
    },
    "uid3": {
        "name": "관리자",
        "birth": "1990-01-01",
        "id": "user3",
        "password": "@pass3",
        "role": "admin"
    }
}

# 실행 시 전체 사용자 목록 출력
print("[전체 사용자 목록]")
for uid, info in users.items():
    print(f"ID: {info['id']}, 이름: {info['name']}, 생년월일: {info['birth']}, 역할: {info['role']}")

print("\n[기능 선택]")
print("1) 회원가입")
print("2) 로그인")
choice = input("번호 입력: ")

# 2. 회원가입
if choice == "1":
    new_id = input("새 아이디: ")

    # 중복된 아이디 검사
    if new_id in users:
        print("이미 존재하는 아이디입니다.")
    else:
        name = input("이름: ")
        birth = input("생년월일(YYYY-MM-DD): ")

        # 유효한 생년월일 검사 (간단히 길이와 - 위치만 확인)
        if len(birth) == 10 and birth[4] == "-" and birth[7] == "-":
            password = input("비밀번호: ")

            # 비밀번호 조건: 10자 이상 + 특수문자 포함
            special = any(ch in "!@#$%^&*()" for ch in password) #password의 각 문자를 ch변수에 할당, ch가 특수문자열에 있으면 True 
            #any()함수는 하나라도 True를 지니면 True 반환

            if len(password) >= 10 and special:     #password의 글자수와 특수문자포함 여부 검사
                role = input("역할(viewer/editor/admin): ")

                if role in ["viewer", "editor", "admin"]: #역할을 제대로 입력했는지 검사
                    #새로운 유저 정보 등록
                    users[new_id] = {                   
                        "name": name,
                        "birth": birth,
                        "id": new_id,
                        "password": password,
                        "role": role
                    }
                    print("회원가입 성공!")

                    # 전체 목록 출력
                    print("\n[전체 사용자 목록]")
                    for uid, info in users.items():
                        print(f"ID: {uid}, 이름: {info['name']}, 생년월일: {info['birth']}, 역할: {info['role']}")
                else:
                    print("역할 입력이 잘못되었습니다.")
            else:
                print("비밀번호 조건 불만족 (10자 이상 + 특수문자 포함 필요)")
        else:
            print("생년월일 형식이 올바르지 않습니다.")

# 3. 로그인
elif choice == "2":
    login_id = input("아이디: ")
    login_pw = input("비밀번호: ")
    
    # 딕셔너리 내부의 "id" 값으로 로그인 검사
    logged_in_uid = None
    for uid, info in users.items():
        if info["id"] == login_id and info["password"] == login_pw:
            logged_in_uid = uid
            break
    
    if logged_in_uid:
        role = users[logged_in_uid]["role"]
        print(f"로그인 성공! 역할: {role}")

        #사용자 역할에 따른 기능 제공
        match role:
            case "viewer":
                action = input("1) 내 정보 수정  2) 내 계정 삭제 : ")
                if action == "1":
                    new_name = input("새 이름: ")
                    users[logged_in_uid]["name"] = new_name
                elif action == "2":
                    del users[logged_in_uid]
                    print("계정 삭제 완료!")

            case "editor":
                action = input("1) 사용자 정보 수정  2) 내 계정 삭제 : ")
                if action == "1":
                    target_id = input("수정할 사용자 아이디: ")
                    # target_id로 실제 uid 찾기
                    target_uid = None
                    for uid, info in users.items():
                        if info["id"] == target_id:
                            target_uid = uid
                            break
                    
                    if target_uid:
                        new_name = input("새 이름: ")
                        users[target_uid]["name"] = new_name
                    else:
                        print("해당 사용자를 찾을 수 없습니다.")
                        
                elif action == "2":
                    del users[logged_in_uid]
                    print("계정 삭제 완료!")



            case "admin":
                action = input("1) 사용자 정보 수정  2) 사용자 삭제 : ")
                if action == "1":
                    target_id = input("수정할 사용자 아이디: ")
                    
                    target_uid = None
                    for uid, info in users.items():
                        if info["id"] == target_id:
                            target_uid = uid
                            break
                    if target_uid:
                        new_name = input("새 이름: ")
                        users[target_uid]["name"] = new_name
                    else:
                        print("해당 사용자를 찾을 수 없습니다.")

                elif action == "2":
                    target_id = input("삭제할 사용자 아이디: ")

                    target_uid = None
                    for uid, info in users.items():
                        if info["id"] == target_id:
                            target_uid = uid
                            break
                    if target_uid:
                        del users[target_uid]
                        print("계정 삭제 완료!")

        # 변경 후 목록 출력
        print("\n[전체 사용자 목록]")
        for uid, info in users.items():
            print(f"ID: {uid}, 이름: {info['name']}, 생년월일: {info['birth']}, 역할: {info['role']}")

    else:
        print("로그인 실패 (아이디 또는 비밀번호 오류)")

else:
    print("잘못된 선택입니다.")
