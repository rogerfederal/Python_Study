import requests

header = {
    "User-Agent1": "23A45BIDp9BgvqW6ok4TUFE1JCHa94/4al2f+wYLk3z7OO1awJblLSJ+5T8m2wIxWUB3KByMbeyQd2HiuT3H6JYbl8U7CTnYCPczYB6AmhggzWmIx/dzd2v4+Qc4r87tBGpre+CS11kdSqbDRQfxZtc/FDJD/0fJvB2ymfw8BPl4orBT8WERMbQdW1DDnB0W2DxDlztd68CsnD1+t9sXp8rjWqmiP2cq99vzyMP/OK8OBFERmcUphYhCYQA7Q1ooHsCCRUIxsZcWQ0mJ4lH/ECsuOZ2UoSFDf1DQCbm/D/HNj9cJIROuiRJXxw+KHoZM6XASZYyO5F96R3jSQ/DBcT2A95+rln0UlPskFoH30g45sOi7gmjW+xvy9FhmFAPLkhe8U4zOMt8JMS+yKfFTYFQQEGUlXRxvGk9YSExBoAUJ/z2NfkEE0S2zlwYAIllf37VqG/Vvkgrs0Lq6iHHnyEL9Kmz7vXjsiOxv0lQlxgoqW0AScD+YXkixzfvfrVmUELK/emxgfjUV4VTmHl7NkBGD4ifnuYjyf"
}

cook = {
    "Cookie": "UserAgentMd5Key=3B317A1D95C76FCC727EA2D0B2B13765"
}

url = "http://vitamin.wallpaper.313515.com/search/catepiclist?p=2Y5p+T+73LxkQF0Y9GW2sRA2apQ30ES+KGNO1tSWmhMujhkxJ7tgv4p8YRteJx7Q8ahppGgSBG4Obk/CMoI41wg=="

response = requests.get(url,headers=header,cookies=cook)
print(response.text)