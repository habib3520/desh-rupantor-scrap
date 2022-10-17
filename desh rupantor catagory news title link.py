import bs4
import requests
import csv

all_unit_link = []
main_page_links = []

def get_sub_links(main_page_link):

    global all_unit_link
    #print(main_page_link)
    page = requests.get(main_page_link)
    #print(page)
    soup = bs4.BeautifulSoup(page.content, 'html.parser')
    # print(soup)
    divs = soup.find("div",{"class":"col-md-8 sidebar-left"})

    for i in divs.find_all("a"):
        #a_tag = newsArticle.find_all("a")
        #news_link = a_tag['href']
        #print(news_link)
        #complete_url = base_address + news_link[1:]
        j = i.get('href')
        print("https://www.deshrupantor.com/" + j[0:len(j)])
        all_unit_link.append(["https://www.deshrupantor.com/" + j[0:len(j)]])
        # print(all_unit_link)

    pass



def write_csv(list_to_be_inserted):
    with open('all_link_catagory_wise.csv', mode='w', newline='',encoding='utf-8') as unit_url_list:
        unit_url_writer = csv.writer(unit_url_list, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        for url in list_to_be_inserted:
            print(url)
            if url!="#recent-view":
               unit_url_writer.writerow(url)

    unit_url_list.close()

    pass


def final():
   with open('main_page_url.csv') as main_url_csv:
      readCSV = csv.reader(main_url_csv)

      for row in readCSV:
          main_page_links.append(row[0])

   print('+---------------------------------------------------------+')

   for main_link in main_page_links:
      get_sub_links(main_link)
      pass

   write_csv(all_unit_link)

   print(len(all_unit_link))

final()


