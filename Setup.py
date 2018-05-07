from Get_Data import GetData
import datetime as dt
import matplotlib.pyplot as plt
import numpy as np

start_date = dt.datetime(2016,5,4) #Stock data start date
end_date = dt.datetime(2018,4,30) #Stock data end date
prediction_date = dt.datetime(2018,5,4) #Date of predicted stock price
stock_symbol = 'WIKI/TSLA'
df = GetData.get_price(stock_symbol, start_date, end_date)
close = df.values.flatten().tolist()
lastClose = close[0]
close.reverse()
date = df.index.to_pydatetime().tolist()
date.reverse()
data = np.matrix(close).T
dates = np.matrix([[1,(x-start_date).days/1000] for x in date])
theta = np.matrix([[0],[0]])
alphas = [0.001, 0.003, 0.01, 0.03, 0.1]
plt.plot(dates[:,1], data)
m = len(dates)
costs = []
thetas = []
for alpha in alphas: #Checks each learning rate to find best fit
    theta = np.matrix([[0],[0]])
    for i in range(1000):
        dJ = (dates.T * (dates*theta-data))
        theta = theta - (alpha/m)*dJ
    thetas.append(theta)
    costs.append((1/2*m)*np.sum(np.square(dates*theta-data)))
theta = thetas[costs.index(min(costs))] #Chooses learning rate that minimizes cost function
predicted_price = float(([1, (prediction_date-start_date).days/1000])*theta) #Calculates estimated price for prediction date
print('Last Closing Price: {:.2f}'.format(lastClose))
print('{}: ${:.2f}'.format(prediction_date.date(), predicted_price))
plt.plot(dates[:,1], dates*theta)
plt.show()
