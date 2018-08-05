import math

class Stat:
    def get_average(self, scores):
        """
        average(scores)->integer
        scores는 점수 리스트입니다. 
        소수 1자리 평균값을 반환합니다.
        """
        s=0
        for score in scores:
            s+=score
        return round(s/len(scores), 1)

    def get_variance(self, scores, avrg):
        s=0
        for score in scores:
            s+=(score-avrg)**2
        return round(s/len(scores), 1)

    def get_std_dev(self, variance):
        return round(math.sqrt(variance),1)
    