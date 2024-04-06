import numpy as np
import pandas as pd
import math
import matplotlib.pyplot as plt
import webbrowser


weights = np.array([0.2, 0.3])
points = np.array([
    [1,-6],
    [-3,2],
    [0.3,-1],
    [2.1,-1.4],
    [-9,2]
])

bias = 1.2
lambda_val = 0.5

result1 = pd.DataFrame(data = np.around(np.sum(weights*points, axis=1),decimals=2), columns=['val1_no_bias'])
result2 = pd.DataFrame(data = np.around(np.sum(weights*points + bias, axis=1),decimals=2), columns=['val1_bias'])
final_r = pd.concat([result2,result1], axis=1)

final_r.loc[:, 'unipolar_bias'] = final_r.apply(lambda x: 1 if x.val1_bias >=0 else 0, axis=1)
final_r.loc[:, 'unipolar_no_bias'] = final_r.apply(lambda x: 1 if x.val1_no_bias >=0 else 0, axis=1)

final_r.loc[:, 'bipolar_bias'] = final_r.apply(lambda x: 1 if x.val1_bias >=0 else -1, axis=1)
final_r.loc[:, 'bipolar_no_bias'] = final_r.apply(lambda x: 1 if x.val1_no_bias >=0 else -1, axis=1)

final_r.loc[:, 'unipolar_bias_no_discrete'] = final_r.apply(lambda x: 1 / (1 + math.exp(-lambda_val * x.val1_bias))
                                                            , axis=1)
final_r.loc[:, 'unipolar_no_bias_no_discrete'] = final_r.apply(lambda x: 1 / (1 + math.exp(-lambda_val * x.val1_no_bias))
                                                            , axis=1)
final_r.loc[:, 'bipolar_bias_no_discrete'] = final_r.apply(lambda x: 2 / (1 + math.exp(-lambda_val * x.val1_bias))
                                                            , axis=1)
final_r.loc[:, 'bipolar_no_bias_no_discrete'] = final_r.apply(lambda x: 2 / (1 + math.exp(-lambda_val * x.val1_no_bias))
                                                            , axis=1)
final_r.iloc[:,[0,1]].to_html("frame.html")
url = "http://localhost:8888/files/notebook/frame.html"
webbrowser.open(url,new=2)

x_axis_r = np.arange(-10,10).reshape(20,1)
y_no_bias_calc = np.apply_along_axis(lambda x: (-weights[0]*x[0]) / weights[1], 1, x_axis_r)
y_bias_calc = np.apply_along_axis(lambda x: (-weights[0]*x[0] - bias) / weights[1], 1, x_axis_r)

fig, axs = plt.subplots(1,2)
axs[0].plot(x_axis_r, y_no_bias_calc)
axs[0].set_title('no bias')
axs[1].plot(x_axis_r, y_bias_calc)
axs[1].set_title('bias')

axs[0].scatter([point[0] for point in points]
               ,[point[1] for point in points]
               , marker = '*'
               , c='red')
axs[1].scatter([point[0] for point in points]
               ,[point[1] for point in points]
               , marker = '*'
               , c='red')
plt.show()

"""
przykłady punktów aktywujących neuron
-- no bias
    [5,-2], [10,4], [0,6]
-- bias
    [5,-2], [10,4], [0,2]
"""







