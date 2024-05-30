from bs4 import BeautifulSoup
import requests
import urllib.request
import time
import random
import urllib3

black_list_name = []
black_list_img = []
white_list_name = []
white_list_img = []


def update_white_lst(movie_id, filename):
    '''更新白名单'''
    with open('./white_black_file/' + filename, 'a+') as fb:
        fb.write(movie_id + '\n')


def update_black_lst(movie_id, filename):
    with open('./white_black_file/' + filename, 'a+') as fb:
        fb.write(movie_id + '\n')


def get_url(filename):
    url_dict = {}
    with open(filename, encoding='utf-8') as fb:
        fb.readline()
        for line in fb:
            if line.strip() == '':
                continue
            # print(line.strip().split(','))
            movie_id = line.strip().split(',')[0]
            # print(movie_id)
            movie_url = line.strip().split(',')[-1]
            # print(movie_url)
            url_dict[movie_id] = movie_url
    return url_dict


def save_poster(id, url):
    # 获取表头
    session = requests.session()
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
        'Connection': 'close'}
    # # imdb网页搜索电影名的网页url
    # url = "https://www.imdb.com/title/tt0020697/?ref_=nv_sr_srsg_0"
    # 模仿浏览器请求网页申请
    requests.adapters.DEFAULT_RETRIES = 5
    # 读取ip池
    f = open("./useful_ip.txt", "r")
    file = f.readlines()
    # 遍历并分别存入列表，方便随机选取IP
    items = []
    for a in file:
        items.append('HTTP://' + a)
    ip = random.choice(items)  # 随机选取一个IP
    proxies = {}
    proxies['HTTP'] = ip[:-1]
    proxies['HTTPS'] = 'HTTPS://' + ip[7:-1]
    f.close()
    print(proxies)
    urllib3.disable_warnings()
    try:
        r = session.get(url, headers=headers, proxies=proxies, verify=False)
        print(r.status_code)  # 输出状态码 200，表示访问成功
    except:
        r = session.get(url, headers=headers, proxies=proxies, verify=False)
    time.sleep(1)
    requests.adapters.DEFAULT_RETRIES = 5
    # 获取html源码并转为utf-8格式
    html = r.content.decode('utf-8', 'ignore')
    # 使用BeautifulSoup对html以lxml格式保存，方便检索
    my_page = BeautifulSoup(html, 'lxml')
    # imdb首页url
    url_header = 'https://www.imdb.com'
    # 获取html源码中所有的'main'，class='ipc-page-wrapper ipc-page-wrapper--base'部分的源码
    print('--------------------' + str(id) + '-----------------------')
    for tag in my_page.find_all('main', class_='ipc-page-wrapper ipc-page-wrapper--base'):
        # 获取电影名部分的源码
        try:
            name_h1 = tag.find('h1', class_='sc-b73cd867-0 eKrKux')
            # 获取包含的文本，即电影名
            name = name_h1.text
            print('name:' + name)
            white_list_name.append(id)
            update_white_lst(id, 'white_list_name.txt')
        except AttributeError as e:
            black_list_name.append(id)
            update_black_lst(id, 'black_list_name.txt')
        try:
            # 获取电影海报部分的源码
            img = tag.find('a', class_='ipc-lockup-overlay ipc-focusable')
            # 获取该部分中'href'的内容：即海报的url
            img_url_tail = img.get('href')
            # 获得完整的海报url
            img_url = url_header + img_url_tail
            print('img_url:' + img_url)
            white_list_img.append(id)
            update_white_lst(id, 'white_list_img.txt')
        except AttributeError as e:
            black_list_img.append(id)
            update_black_lst(id, 'black_list_img.txt')
        # if id in black_list_img:
        #     continue
        print('再次获取海报url网页')
        # 再次获取海报url网页的请求
        session2 = requests.session()
        requests.adapters.DEFAULT_RETRIES = 5
        try:
            r2 = session2.get(img_url, headers=headers, proxies=proxies, verify=False)
            print('r2 status_code:' + r2.status_code)  # 输出状态码 200，表示访问成功
        except:
            r2 = session2.get(img_url, headers=headers, proxies=proxies, verify=False)

        html2 = r2.content.decode('utf-8', 'ignore')
        img_page = BeautifulSoup(html2, 'lxml')
        print('获取海报图片的源码')
        print('$$$$$$$$$$$')
        # print(img_page.find_all('main' , class_='ipc-page-wrapper ipc-page-wrapper--baseAlt'))
        # 获取海报图片的源码
        for tag2 in img_page.find_all('main', class_='ipc-page-wrapper ipc-page-wrapper--baseAlt'):
            try:
                img2 = tag2.find('img')
                # print('img2:'+img2)
                # time.sleep(1)
                # 获取图片的可下载url
                img2_url = img2.get('src')
                print('img2_url:' + img2_url)
                # 将海报图片下载到filename中
                urllib.request.urlretrieve(img2_url, filename=r"./image/" + id + ".jpg")
                # 清除缓存
                urllib.request.urlcleanup()
            except AttributeError as e:
                print(' in black_list_img.txt')
                black_list_img.append(id)
                update_black_lst(id, 'black_list_img.txt')


def run(filename=r'./miss_movies.csv'):
    url_dict = get_url(filename)
    for movie_id, movie_url in url_dict.items():
        if int(movie_id) != 3935:
            continue
        print("!!!!!!!!!!" + str(movie_id) + "!!!!!!!!")
        save_poster(movie_id, movie_url)


if __name__ == '__main__':
    run()
