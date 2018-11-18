from app import warikan

def check_warikan():
    #ここに何か書く
    result = warikan(1500,3) == "1人あたり: 500円, 端数: 0円"

    if result :
        print("OK")
    else:
        print("NG")

check_warikan()

