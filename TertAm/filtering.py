PATH = '/home/sofia/Desktop/url/TertAM/article_links.txt'
FILT= '/home/sofia/Desktop/url/TertAM/filtered_links.txt'


def main():

    with open(PATH, 'r') as txt_file:
        text = txt_file.read()
        urls_list = text.split()
        unique_elements_set = set (urls_list)
        result = list(unique_elements_set)

    with open(FILT, 'w') as f:
        f.write('\n'.join(result) )
main()