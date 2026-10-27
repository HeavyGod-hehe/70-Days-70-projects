from lc_steps import extract_order, check_order,write_reply

messages = [
    "bhai kal 15 bori maida bhej dena, paisay hafte baad dunga",
    "20 bori bhej do",
    "assalam o alaikum, mill kab tak khula hai aaj?",
]

for message in messages:
    print("MESSAGE:", message)

    data = extract_order(message)
    print("STEP 1 (form):", data)

    ok, reason = check_order(data)
    print("STEP 2 (check):", ok, "|", reason)

    print("-" * 40)




reply = write_reply(message, data, ok, reason)
print("STEP 3 (reply):", reply)