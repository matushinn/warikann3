def warikan(amount, number_of_people):
    quotient = amount / number_of_people
    remainder = amount % number_of_people

    return f"1人あたり: {quotient}円, 端数: {remainder}円"

# 1500円を3人で割り勘 -> 1人あたり: 500円, 端数: 0円
check_result = warikan(1500, 3) == "1人あたり: 500円, 端数: 0円"

print(check_result) # False <-- 何か間違いがあったぞ！