import re


if __name__ == '__main__':
    quote = ("There's only one thing I hate more than lying: skim milk. Which is water"
            "that's lying about being milk. - Ron Swanson")

    result = re.search("milk", quote).group()
    print(result)

    result = re.findall("milk", quote)
    print(result)
 
    result = re.split("milk", quote)
    print(result)