def read_file(name):
    import xml.etree.ElementTree as ET
    parser = ET.XMLParser(encoding='utf-8')
    tree = ET.parse(name, parser)
    root = tree.getroot()
    news_list = root.findall('channel/item/description')
    text_news = []
    for news in news_list:
        result = news.text.lower()
        text_news.append(result)
    return text_news


def count_word(text_news):
    for one_news in text_news:
        to_list = one_news.split(' ')
        to_set = set()
        for i in to_list:
            if len(i) > 6:
                to_set.add(i)
    word_value = {}
    for i in to_set:
        count = 0
        for j in to_list:
            if i == j:
                count += 1
        word_value[i] = count
    return word_value


def sort_top(word_value):
    register = list()
    l_dict = str(len(word_value))
    for i in word_value.items():
        l_word = str(i[1])
        register.append((len(l_dict) - len(l_word)) * '0' + str(i[1]) + ' ' + i[
            0])
    register.sort(reverse=True)
    top_10 = {}
    count = 1
    for j in register:
        top_10[count] = j.split(' ')
        top_10[count][0] = int(top_10[count][0])
        if count == 10:
            break
        count += 1
    return top_10


def main():
    from pprint import pprint
    top_10 = sort_top(count_word(read_file('newsafr.xml')))
    pprint(top_10)


main()