from steps import extract_order, parse_output, check_order,write_reply

messages = [
    "bhai kal 15 bori maida bhej dena, paisay hafte baad dunga",
    "20 bori bhej do",
    "assalam o alaikum, mill kab tak khula hai aaj?",
]


def run_pipeline(message):

    raw = extract_order(message)
    print("STEP 1 (raw):", raw)

    data = parse_output(raw)
    print("STEP 2 (dict):", data)

    ok, reason = check_order(data)
    print("STEP 3 (check):", ok, "|", reason)

    reply = write_reply(message, data, ok, reason)
    return(reply)


for message in messages:
    print("MESSAGE:", message)
    reply = run_pipeline(message)
    print("REPLY:", reply)
    print("-" * 40)