from statistics import Stat
from openpyxl import load_workbook

class DataHandler:
    evaluator=Stat()
    @classmethod
    def get_data_from_excel(cls, filename):
        """
        get_data_from_excel(filename)->{'name1' : 'score1', 'name2' : 'score2', ...}
        엑셀파일에서 데이터를 가져옵니다.
        반환값은 key가 학생 이름이고 value가 점수인 딕셔너리입니다.
        """
        raw_data={}
        wb=load_workbook(filename)
        ws=wb.active
        g=ws.rows
        for name_cell, score_cell in g:
            raw_data[name_cell.value]=score_cell.value
        
        return raw_data

    def __init__(self, filename):
        self.rawdata=DataHandler.get_data_from_excel(filename)
        self.year_class=filename.split('_')[1].split('.')[0]
        self.cache={}

    def get_scores(self):
        if 'scores' not in self.cache:
            self.cache['scores']=list(self.rawdata.values())
        return self.cache.get('scores')

    def get_average(self):
        if 'average' not in self.cache:
            self.cache['average']=self.evaluator.get_average(self.get_scores())
        return self.cache.get('average')

    def get_variance(self):
        if 'variance' not in self.cache:
            self.cache['variance']=self.evaluator.get_variance(self.get_scores(), self.get_average())
        return self.cache.get('variance')

    def get_standard_deviation(self):
        if 'standard_deviation' not in self.cache:
            self.cache['standard_deviation']=self.evaluator.get_std_dev(self.get_variance())
        return self.cache.get('standard_deviation')

    def evaluate_class(self, total_avrg, sd):
        """
        evaluate_class(total_avrg, sd)->None
        total_avrg : 학년 전체 성적 평균
        sd : 원하는 표준편차 기준
        """
        avrg=self.get_average()
        std_dev=self.get_standard_deviation()

        if avrg < 50 and std_dev > 20:
            print('성적이 너무 저조하고 학생들의 실력 차이가 너무 크다.')
        elif avrg > 50 and std_dev > 20:
            print('성적은 평균 이상이지만 학생들의 실력 차이가 크다. 주의 요망!')
        elif avrg < 50 and std_dev < 20:
            print('학생들의 실력 차이는 크지 않지만 성적이 너무 저조하다. 주의 요망!')
        elif avrg > 50 and std_dev < 20:
            print('성적도 평균 이상이고 학생들의 실력 차이도 크지 않다.')

    def get_evaluation(self, total_avrg, sd=20):
        print('*'*50)
        print('{} 반 성적 분석 결과'.format(self.year_class))
        print('{} 반의 평균은 {}점이고 분산은 {}이며 표준편차는 {}이다.'.format(
            self.year_class,
            self.get_average(),
            self.get_variance(),
            self.get_standard_deviation()
        ))
        print('*'*50)
        print('{}반 종합 평가'.format(self.year_class))
        print('*'*50)
        self.evaluate_class(total_avrg, sd)

