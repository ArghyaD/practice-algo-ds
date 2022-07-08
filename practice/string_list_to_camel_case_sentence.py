from typing import List


def string_list_to_camel_case_sentence(input: List[str]):
    string_list: List[str] = []
    for i in input:
        string_list.extend(i.split(" "))
    i = 0
    while i < len(string_list):
        camel_case_word_buffer: str = string_list[i]
        camel_case_word_buffer = camel_case_word_buffer[0].upper() + camel_case_word_buffer[1:].lower()
        string_list[i] = camel_case_word_buffer
        i += 1
    return " ".join(string_list)


if __name__ == '__main__':
    input: List[str] = ['I', 'GOT', 'iNtErN', 'at geekSfoRgeekS']
    print(string_list_to_camel_case_sentence(input))

    input = ['AnNiruddHA Routh', 'LOVES', 'to', 'COdE everyDAY']
    print(string_list_to_camel_case_sentence(input))