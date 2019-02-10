from openpyxl import load_workbook
from pickle import load
import math

def get_data_from_excel(filename):
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

def get_data_from_file(filename):
    raw_data={}
    f=open(filename, 'rb')
    try:
        while True:
            data=load(f)
            raw_data.update(data)
    except EOFError:
        pass
    return raw_data


def get_average(scores):
    """
    average(scores)->integer
    scores는 점수 리스트입니다. 
    소수 1자리 평균값을 반환합니다.
    """
    s=0
    for score in scores:
        s+=score
    return round(s/len(scores), 1)

def get_variance(scores, avrg):
    s=0
    for score in scores:
        s+=(score-avrg)**2
    return round(s/len(scores), 1)

def get_std_dev(variance):
    return round(math.sqrt(variance),1)

def evaluate_class(avrg, total_avrg, std_dev, sd=20):
    """
    evaluate_class(avrg, total_avrg, std_dev, sd)->None
    avrg : 반 성적 평균
    total_avrg : 학년 전체 성적 평균
    std_dev : 반의 표준편차
    sd : 원하는 표준편차 기준
    """
    if avrg < 50 and std_dev > sd:
        print('성적이 너무 저조하고 학생들의 실력 차이가 너무 크다.')
    elif avrg > 50 and std_dev > sd:
        print('성적은 평균 이상이지만 학생들의 실력 차이가 크다. 주의 요망!')
    elif avrg < 50 and std_dev < sd:
        print('학생들의 실력 차이는 크지 않지만 성적이 너무 저조하다. 주의 요망!')
    elif avrg > 50 and std_dev < sd:
        print('성적도 평균 이상이고 학생들의 실력 차이도 크지 않다.')



