list_1 = [
    {"id": "1", "name": "Shrey", "age": 25},
    {"id": "3", "age": 10, "name": "Hello"},
    {"id": "2", "name": "World", "age": 24},
]

list_2 = [
    {"id": "1", "marks": 100},
    {
        "id": "3",
        "marks": 90,
        "roll_no": 11,
        "extra_info": {
            "hello": "world",
        },
    },
]


def merge_lists(list_1, list_2) -> list:
    merged_dict = {}

    for val in list_1:
        id_val = val["id"]
        
        if id_val not in merged_dict:
            merged_dict[id_val] = {}

        merged_dict[id_val].update(val)
    
    for val in list_2:
        id_val = val["id"]

        if id_val not in merged_dict:
            merged_dict[id_val] = {}

        merged_dict[id_val].update(val)

    return list(merged_dict.values())


list_3 = merge_lists(list_1, list_2)
