import requests
from bs4 import BeautifulSoup
import json
import time

def main():
    headers = {
        'Host':'www.lagou.com',
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
        'Referer':'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=',
        'X-Anit-Forge-Code': '0',
        'X-Anit-Forge-Token': 'None',
        'X-Requested-With': 'XMLHttpRequest'
    }


    positions = []
    for x in range(1,2):
        form_data = {
            'first': 'true',
            'pn': x,
            'kd': 'python'
        }
        result = requests.post('https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false',
                               headers=headers, data=form_data)
        res = result.json()
        print(res)
        page_positions = res['content']['positionResult']['result']
        for postion in page_positions:
            position_dict = {
                'position_name':postion['positionName'],
                'workYear':postion['workYear'],
                'salary':postion['salary'],
                'companyFullName':postion['companyFullName']
            }
            position_Id = postion['positionId']
            print(position_Id)
            postion_detail = crawlDetail(position_Id)
            position_dict['postion_detail'] = postion_detail
            positions.append(position_dict)
            time.sleep(5)

        time.sleep(3)

    line = json.dumps(positions, ensure_ascii=False)
    with open('lagou.json', 'wb+') as fp:
        fp.write(line.encode('utf-8'))




def crawlDetail(position_id):
    url = 'https://www.lagou.com/jobs/%s.html' % position_id
    headers = {
        'Host': 'www.lagou.com',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'
    }

    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.content, 'html.parser')
    job_bt = soup.find('dd', attrs={'class':'job_bt'})
    print(job_bt)
    return job_bt.text


if __name__ == '__main__':
    main()
    # crawlDetail('2475715')