# 라이프로그 데이터를 이용한 사용자의 활동수준 예측모델
## 0. 연구목적
본 연구는 웨어러블 디바이스를 착용한 환자들의 데이터를 바탕으로 환자의 라이프로그를 예측하는 머신러닝 모델을 개발하는데 그 목적을 가지고 있음

## 1. 데이터
* 100명의 환자들의 라이프로그 데이터를 수집
* 100명의 환자들의 라이프로그 데이터 중 82건의 데이터를 학습에 사용하고, 나머지 18건을 테스트에 사용

구분 | 라이프로그 데이터(건)
:-: | -:
Total | 100
Train | 82
Test | 18

## 2. 사용자의 활동수준 예측모델
* 스마트워치를 통해 수집한 라이프로그 데이터를 바탕으로 사용자의 활동 수준을 5단계로 구분

Status | 활동 상태 | 설명
:-: | :-: | :-: | 
0 | Not Worn | 미착용 상태
1 | Sedentary | 활동량이 거의 없는 상태
2 | Lightly Active | 가벼운 활동량
3 | Fairly / Moderately Active | 적당한 활동량
4 | Very Active | 매우 활발한 활동량

## 3. 연구결과
### 3.1. Macro 평균
모델 | 파라미터 | 정확도<br>(Accuracy) | 정밀도<br>(Precision) | 재현율<br>(Recall) | F1 점수<br>(F1-score)
:-: | :-: | :-: | :-: | :-: | :-: |
SVM | C: 100, <br> Gamma: 10 | 0.943024 | 0.943119 | 0.943024 | 0.940818
K-Neighbors | N neighbers: 25, <br> Leaf size: 100, <br> Weights: distance | 0.937563 | 0.938129 | 0.937563 | 0.936102
Naïve Bayes | - | 0.936823 | 0.875738 | 0.857192 | 0.862402
Random Forest | Max depth: 120, <br> Min samples leaf: 60, <br> Min samples split: 6 | 0.943572 | 0.897313 | 0.846786 | 0.869652
Random Forest | Max depth: 80, <br> Min samples leaf: 6, <br> Min samples split: 80 | 0.943413 | 0.892486 | 0.848268 | 0.941702
Random Forest | Max depth: 8, <br> Min samples leaf: 6, <br> Min samples split: 80 | 0.943360 | 0.900447 | 0.842849 | 0.868469
Hard Voting | - | 0.943667 | 0.899020 | 0.844964 | 0.869265
Soft Voting | - | 0.943254 | 0.899170 | 0.847136 | 0.870639
GBM | Learning rate: 0.1, <br> Max depth: 2, <br> N estimators: 250 | 0.943731 | 0.893708 | 0.851856 | 0.871046
XGBoost | Learning rate: , <br> Max depth: , <br> N estimators:  | 0.943434 | 0.892980 | 0.849545 | 0.869396

### 3.2. Micro 평균
모델 | 파라미터 | 정확도<br>(Accuracy) | 정밀도<br>(Precision) | 재현율<br>(Recall) | F1 점수<br>(F1-score)
:-: | :-: | :-: | :-: | :-: | :-: |
SVM | C: 100, <br> Gamma: 10 | 0.943024 | 0.943119 | 0.943024 | 0.940818
K-Neighbors | N neighbers: 25, <br> Leaf size: 100, <br> Weights: distance | 0.937563 | 0.938129 | 0.937563 | 0.936102
Naïve Bayes | - | 0.936823 | 0.936823 | 0.936823 | 0.936823
Random Forest | Max depth: 120, <br> Min samples leaf: 60, <br> Min samples split: 6 | 0.943572 | 0.943572 | 0.943572 | 0.943572
Random Forest | Max depth: 80, <br> Min samples leaf: 6, <br> Min samples split: 80 | 0.943413 | 0.943413 | 0.943413 | 0.943413
Random Forest | Max depth: 8, <br> Min samples leaf: 6, <br> Min samples split: 80 | 0.943360 | 0.943360 | 0.943360 | 0.943360
Hard Voting | - | 0.943667 | 0.943667 | 0.943667 | 0.943667
Soft Voting | - | 0.943254 | 0.943254 | 0.943254 | 0.943254
GBM | Learning rate: 0.1, <br> Max depth: 2, <br> N estimators: 250 | 0.943731 | 0.943731 | 0.943731 | 0.943731
XGBoost | Learning rate: , <br> Max depth: , <br> N estimators:  | 0.943434 | 0.943434 | 0.943434 | 0.943434

### 3.3. Weighted 평균
모델 | 파라미터 | 정확도<br>(Accuracy) | 정밀도<br>(Precision) | 재현율<br>(Recall) | F1 점수<br>(F1-score)
:-: | :-: | :-: | :-: | :-: | :-: |
SVM | C: 100, <br> Gamma: 10 | 0.943024 | 0.943119 | 0.943024 | 0.940818
K-Neighbors | N neighbers: 25, <br> Leaf size: 100, <br> Weights: distance | 0.937563 | 0.938129 | 0.937563 | 0.936102
Random Forest | Max depth: 80, <br> Min samples leaf: 30, <br> Min samples split: 6 | 0.943404 | 0.943997 | 0.943404 | 0.94185
Random Forest | Max depth: 40, <br> Min samples leaf: 6, <br> Min samples split: 80 | 0.943248 | 0.943844 | 0.943242 | 0.941702
Random Forest | Max depth: 8, <br> Min samples leaf: 60, <br> Min samples split: 40 | 0.943106 | 0.944033 | 0.943106 | 0.941639
Naïve Bayes | - | 0.936823 | 0.938346 | 0.936823 | 0.937217
Random Forest | Max depth: 120, <br> Min samples leaf: 60, <br> Min samples split: 6 | 0.943572 | 0.942523 | 0.943572 | 0.942801
Random Forest | Max depth: 80, <br> Min samples leaf: 6, <br> Min samples split: 80 | 0.943413 | 0.942307 | 0.943413 | 0.942612
Random Forest | Max depth: 8, <br> Min samples leaf: 6, <br> Min samples split: 80 | 0.943360 | 0.942449 | 0.943360 | 0.942626
Hard Voting | - | 0.943667 | 0.942592 | 0.943667 | 0.942857
Soft Voting | - | 0.943254 | 0.942276 | 0.943254 | 0.942537
GBM | Learning rate: 0.1, <br> Max depth: 2, <br> N estimators: 250 | 0.943731 | 0.942787 | 0.943731 | 0.943056
XGBoost | - | 0.943434 | 0.942384 | 0.943434 | 0.942909

** 본 연구는 2022년도 산업통상자원부 및 산업기술평가관리원(KEIT) 연구비 지원에 의한 연구임을 밝힙니다. (20002781)