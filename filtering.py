PATH = '/home/sofia/Desktop/url/Infocom/news_links.txt'
FILT= '/home/sofia/Desktop/url/Infocom/filtered_links.txt'
with open(PATH, "r") as txt_file:
   text = txt_file.read()
   urls_list = text.split()
   unique_elements_set = set (urls_list)
   result = list(unique_elements_set)
with open(FILT, 'w') as f:
      f.write('\n'.join(result) )
