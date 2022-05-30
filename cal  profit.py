import  numpy as np
import matplotlib.pyplot as plt
import pandas as pd

number = 100000# 模拟的次数
random_p = np.empty((number, 9))#空数组保存随机权重和标准差
np.random.seed(5)
#profitpercent={'股票型':0.05158,'混合型':0.0448,'债券型':0.041245,'指数型':0.045578,'QDII':0.091802,'ETF':0.05067,'LOF':'0.036288','FOF':'0.046022','货币型':'0.039148'}
volper=[0.1057,0.0971,0.0503,0.098549,0.104169,0.0979,0.100662]
profitper=np.array([5.158,4.48,4.1245,4.5578,9.1802,5.067,3.6288])
profitpercent=np.array([[7.054,4.828,3.591],[4.124, 5.448,3.868],[0.686,2.908,5.341],[6.197,3.823,3.658],[13.43,7.598, 6.512],[6.989,4.458,3.754],[5.392,2.999,2.495]])
volp=np.cov(profitpercent)
for i in range(number):

    random7 = np.random.random(7)
    randomweight = random7 / np.sum(random7)
    vol = np.sqrt(np.dot(randomweight.T, np.dot(volp, randomweight)))
    profit = np.dot(profitper, randomweight)
    random_p[i][:7] = randomweight
    random_p[i][7] = profit
    random_p[i][8] = vol

RandomPortfolios = pd.DataFrame(random_p)# 将Numpy数组转化为DataF数据框
foundlist=['股票型','混合型','债券型','指数型','QDII','ETF','LOF']
RandomPortfolios.columns = [_ + '_weight' for _ in foundlist] + ['Profit', 'Vol']
#RandomPortfolios.plot('Vol', 'Profit', kind='scatter', alpha=0.3)
RandomPortfolios.plot.scatter(x='Vol', y='Profit', marker='o', s=10, alpha=0.3, grid=False, figsize=[10,10])

plt.savefig( 'text1.png')
# plt.show()
# max_profit = RandomPortfolios.iloc[RandomPortfolios['Profit'].idxmax()]
# print(max_profit+'/n')
min_vol = RandomPortfolios.iloc[RandomPortfolios['Vol'].idxmin()]
print(min_vol)

# GMV_weights = np.array(RandomPortfolios.iloc[min_index, 0:numstocks])
#
# # StockReturns['Portfolio_GMV'] = stock_return.mul(GMV_weights, axis=1).sum(axis=1)
# # #输出风险最小投资组合的权重
# print(GMV_weights)
