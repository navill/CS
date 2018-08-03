from functions import *

#학년 전체 평균 : 50점

raw_data=get_data_from_excel('class_1.xlsx')
scores=list(raw_data.values())

avrg=get_average(scores)
variance=get_variance(scores, avrg)
std_dev=get_std_dev(variance)

print('평균:{}, 분산:{}, 표준편차:{}'.format(avrg, variance, std_dev))

evaluate_class(avrg, 50, std_dev, 20)
