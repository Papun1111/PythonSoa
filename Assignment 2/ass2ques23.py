notes_100_count = 10
notes_50_count = 20
notes_20_count = 30
notes_10_count = 50

total_atm_cash = (100 * notes_100_count) + (50 * notes_50_count) + (20 * notes_20_count) + (10 * notes_10_count)

amount = int(input("Enter the amount you want to withdraw: "))

if amount % 10 != 0:
    print("Amount must be a multiple of 10.")
elif amount > total_atm_cash:
    print("Insufficient funds in the ATM.")
else:
    notes_100 = notes_50 = notes_20 = notes_10 = 0

    if amount >= 100 and notes_100_count > 0:
        notes_100 = min(amount // 100, notes_100_count)
        amount -= notes_100 * 100

    if amount >= 50 and notes_50_count > 0:
        notes_50 = min(amount // 50, notes_50_count)
        amount -= notes_50 * 50

    if amount >= 20 and notes_20_count > 0:
        notes_20 = min(amount // 20, notes_20_count)
        amount -= notes_20 * 20

    if amount >= 10 and notes_10_count > 0:
        notes_10 = min(amount // 10, notes_10_count)
        amount -= notes_10 * 10

    print("Withdrawal successful. Please collect your cash:")
    print(f"100 notes: {notes_100}")
    print(f"50 notes: {notes_50}")
    print(f"20 notes: {notes_20}")
    print(f"10 notes: {notes_10}")
