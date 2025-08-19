import json 


def save_json(file_path: str, data: list[dict[str]]) -> None:
    with open(file_path, 'a', encoding='utf-8') as file: 
        json.dump(
            data,
            file,
            indent=2,
            ensure_ascii=False
            )