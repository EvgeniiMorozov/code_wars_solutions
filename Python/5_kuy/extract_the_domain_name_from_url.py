def domain_name(url: str) -> str:
    for el in ["http://", "www.", "https://"]:
        if el in url:
            url = url.split(el)[1]
    return url.split(".")[0]


if __name__ == "__main__":
    print(domain_name("http://google.com"))
    print(domain_name("http://google.co.jp"))
    print(domain_name("www.xakep.ru"))
    print(domain_name("https://youtube.com"))
