import json


diff_list = ['services', 'staff', 'datetime']

def compare_jsons(json_1, json_2):
    result = {}
    for key, value in json_1.items():
        if type(value) == dict:
            result.update(compare_jsons(json_1[key], json_2[key]))
        if key not in diff_list:
            continue
        if value != json_2[key]:
            result[key] = json_2[key]
    return result

with open('31tema/json_old.json', 'r', encoding="UTF-8") as f:
    json_old = json.load(f)

with open('31tema/json_new.json', 'r', encoding="UTF-8") as f:
    json_new = json.load(f)

answer = compare_jsons(json_old, json_new)
print(answer)

with open('31tema/json_diffs.json', 'w', encoding="UTF-8") as f:
    json.dump(answer, f, indent=4, ensure_ascii=False)
