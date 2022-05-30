import pandas as pd
import requests
import re
def get_fund_data():
    """ 获取天天基金，8千多基金排行（默认为近6个月收益率）"""
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36',
        'Referer': 'http://fund.eastmoney.com/data/fundranking.html',
        'Cookie': 'st_si=51694067779834; st_asi=delete; ASP.NET_SessionId=e1pno0koqkcp5es3xyzyrg1n; EMFUND1=null; EMFUND2=null; EMFUND3=null; EMFUND4=null; EMFUND5=null; EMFUND6=null; EMFUND7=null; EMFUND8=null; EMFUND0=null; _adsame_fullscreen_18503=1; EMFUND9=09-23 01:16:38@#$%u4E07%u5BB6%u65B0%u5229%u7075%u6D3B%u914D%u7F6E%u6DF7%u5408@%23%24519191; st_pvi=87492384111747; st_sp=2021-09-23%2000%3A05%3A17; st_inirUrl=http%3A%2F%2Ffund.eastmoney.com%2Fdata%2Ffundranking.html; st_sn=15; st_psi=20210923011636912-0-9218336114'
    }
    url2 = 'https://fund.eastmoney.com/data/rankhandler.aspx?op=dy&dt=kf&ft=lof&rs=&gs=0&sc=qjzf&st=desc&sd=2021-04-01&ed=2022-05-01&es=0&qdii=&pi=1&pn=4000&dx=0&v=0.6658618553246816'
    response = requests.get(url2, headers=header)
    text = response.text
    compile_data = "[" + re.findall("\\[(.*)\\]", str(text))[0] + "]"
    strip_data = str(compile_data).strip('[').strip(']').replace(" ", "")
    column_list = ["基金代码", "基金简称", "基金条码",  "涨幅", "期间分红", "分红次数", "起始日期", "单位净值", "累计净值", "终止日期", "单位净值", "累计净值", "成立日期", "无用1",  "手续费", "无用2", "也是手续费", "无用3", "无用4"]
    list_list = [i.strip('"').split(",") for i in strip_data.split('","')]
    df = pd.DataFrame(list_list, columns=column_list)

    print("Save the found ranking info to csv file, saving ...")
    df.to_csv('LOF 2021.csv', encoding='utf_8_sig')
    return df

if __name__ == '__main__':
    found_all = get_fund_data()
    # print(">>>>> The found all as:\n", found_all)
