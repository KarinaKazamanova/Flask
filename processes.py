import argparse
import multiprocessing
import time
import requests



tt_time = 0
def download(url):
    global tt_time
    p = requests.get(url) 
    text_context = p.text.split()
    for item in text_context:
        if 'https' in item:
            if 'svg' in item:
                
                image = item[item.find('https'):item.find('.svg')+ 4]
                try:
                    with open(str(item).split('/')[-1].replace('"','').replace('>','').replace("'",''),'bw') as file:
                        time_start = time.time()
                        file.write(requests.get(image).content)
                        tt_time += (time.time() -  time_start)
                        print(f"Изображение скачалось за {time.time() - time_start} секунд")
                except:
                    continue
               

            if 'png' in item :
                image = item[item.find('https'):item.find('.png')+ 4]
                try:
                    with open(str(item).split('/')[-1].replace('"','').replace('>','').replace("'",''),'bw') as file:
                        time_start = time.time()
                        file.write(requests.get(image).content)
                        tt_time += (time.time() -  time_start)
                        print(f"Изображение скачалось за {time.time() - time_start} секунд")
                except:
                    continue
                

            if 'jpeg' in item :
                image = item[item.find('https'):item.find('.jpeg')+ 5]
                try:
                    with open(str(item).split('/')[-1].replace('"','').replace('>','').replace("'",''),'bw') as file:
                        time_start = time.time()
                        file.write(requests.get(image).content)
                        tt_time += (time.time() -  time_start)
                        print(f"Изображение скачалось за {time.time() - time_start} секунд")
                except:
                    continue
    print(f'Все изображения скачались за {tt_time} секунд')
        
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--url-list', required=True)
    args_ = parser.parse_args()
    print(args_)        
    processes = []
    time_start = time.time()
    site_list = [str(i) for i in args_.url_list.split(',')]
    
    for url in site_list:
        p = multiprocessing.Process(target=download, args=([url]))
        processes.append(p)
        p.start()
        
    for p in processes:
        p.join()
        
    print('Готово')
    time_end = time.time()
    print(f'Программа завершила свою работу за {time_end - time_start} cекунд')