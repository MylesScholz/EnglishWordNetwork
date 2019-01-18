#Run Script
#Myles Scholz

import data_parser as dp
import Network as nw

dp.make_data()
tr_d, te_d, va_d = dp.load_data()
print(len(tr_d))
net = nw.Network([28,25,25,28])
net.SGD(tr_d,30,10,1.0,test_data=te_d)