---
title: "電磁気学詳論II"
collection: courses
type: "全学共通教育科目"
permalink: /courses/2025-spring-elemag2
venue: "大阪大学, 全学共通教育機構"
date: 2025-03-28
location: "Osaka, Japan"
---

専門基礎教育科目(基礎工学部(システム、情報)、理学部(数学))、火曜日1限、共A302  
[CLE授業支援システム](https://www.cle.osaka-u.ac.jp/ultra/courses/_215612_1/outline)

[このページ](https://stsykw.github.io/courses/2025-spring-elemag2)

試験通知
-------
8月5日(火曜日、1限)に期末試験を実施します。詳細はCLEに掲示します。

スケジュール
----------
**4月15日**  
(休講)

**4月22日**  
電磁気学詳論Iの復習  
真空中の電磁波: 波動方程式の導出とその解  

**5月7日(火曜日の振替日)**  
真空中の電磁波: 電磁波としての性質、エネルギーと運動量  

**5月13日**  
真空中の電磁波: 偏光  
電気伝導と導体の性質: 導体、電荷の保存則、電気伝導  

**5月20日**  
誘電体: 分極、電束密度、誘電率、境界条件  

**5月27日**  
誘電体: エネルギー、具体例  

**6月3日**  
誘電体: 具体例  
磁性体: 磁化、磁化電流、透磁率  

**6月10日**  
磁性体: 境界条件、エネルギー、具体例  

**6月17日**  
磁性体: 具体例、強磁性体の例  
超伝導体と磁場: 超伝導  

**6月24日**  
物質中の電磁波: 物質中のマクスウェル方程式、屈折率  

**7月1日**  
物質中の電磁波: 反射、屈折、内部全反射、エバネッセント光、反射波の位相  

**7月8日**  
物質中の電磁波: 導体と電磁波  
回路: 起電力、定常電流回路の基礎方程式、キルヒホッフの法則  

**7月15日**  
回路: 準定常回路、LC回路、RC回路、RL回路  

**7月22日**  
回路: RLC回路、交流回路、実効値、複素数を使った表現  

**7月29日**  
回路: 合成インピーダンス、共鳴、フィルター回路  

**8月5日**  
期末試験  


Quiz
----

解答はCLE経由で提出すること。手書き文書のスキャン、Word文書、Tex文書など形式は問わないが、最終的に提出時には一つのpdfファイルにまとめて提出すること。
基本的に提出締め切りは、出題日の一週間後の正午とします。

**Quiz 1(4月22日出題)**  
ベクトル微分演算子\\( \nabla \\)およびベクトル値関数\\( \boldsymbol{A} \\)に対し
\\[
  \nabla \times ( \nabla \times \boldsymbol{A}) = \nabla (\nabla \cdot \boldsymbol{A} ) - \nabla^2 \boldsymbol{A}
\\]
となることを示せ。

**Quiz 2(5月7日出題)**  
真空中の電磁場のエネルギー密度は
\\[
  u = \dfrac{\epsilon_0}{2} \left\lvert \boldsymbol{E}\right\rvert^2
  +\dfrac{1}{2\mu_0} \left\lvert \boldsymbol{B}\right\rvert^2
\\]
である。このエネルギー密度のある領域\\( \mathcal{D} \\)での体積積分\\( \mathcal{E} \\)の時間変化は
\\[
  \dfrac{d\mathcal{E}}{dt} = \int_\mathcal{D} \left(
    \epsilon_0 \boldsymbol{E} \cdot \dfrac{\partial \boldsymbol{E}}{\partial t} 
    + \dfrac{1}{\mu_0} \boldsymbol{B} \cdot \dfrac{\partial \boldsymbol{B}}{\partial t} 
  \right)
\\]
である。右辺の電場および磁束密度の時間変化を、電荷密度および電流密度が存在しない場合のMaxwell方程式をつかって
\\[
    \dfrac{d\mathcal{E}}{dt} = \dfrac{1}{\mu_0} \int_\mathcal{D}\nabla \cdot \left(
     \boldsymbol{B} \times \boldsymbol{E} 
  \right)  
\\]
まで変形せよ。この積分の表現にGaussの定理を使ってPoyntingベクトル\\( \boldsymbol{S} \\)を求めよ。

**Quiz 3(5月13日出題)**  
導体中の自由電子の運動を、1次元の古典的な力学にしたがうとするDrudeモデル
\\[
  m \dfrac{d^2 x}{dt^2} = - eE - \dfrac{m}{\tau} \dfrac{dx}{dt}
\\]
で取り扱う。
* この運動方程式にしたがう自由電子の定常状態(加速度が0となる状態)での速度\\( \bar{v}\\)を求めよ。
* 自由電子の数密度を\\( n\\)として定常状態での電流密度の大きさ\\( i \\)を求めよ。
* 速度に比例した抵抗力(右辺第二項)に速度\\( \bar{v} \\)と自由電子の数密度\\( n \\)をかけると、単位体積当たりのエネルギー散逸に関する仕事率になる。これを電流密度\\( i \\) と電場の大きさ\\( E\\)をつかって表すと、\\( i E \\)となることを示せ。これは単位体積当たりのJoule熱である。


**Quiz 4(5月27日出題)**  
極板面積\\( S \\)、極板間隔\\( d \\)の平行平板コンデンサーがあり、極板間を誘電率\\( \epsilon \\)の誘電体で満たしている。それぞれの極板に一様な面密度\\( \sigma (>0), - \sigma \\)で電荷を与えた。
コンデンサー内部の電場は一様であると仮定する。
* 極板間の電束密度の大きさ\\( D \\)および電場の大きさ\\( E \\)を求めよ。
* 極板間の電気分極の大きさ\\( P \\)を求めよ。
* 誘電体の極板と接する表面には電場に誘導され分極電荷が発生している。面密度\\( \sigma \\)で電荷が蓄えられている極板側で発生している分極電荷密度を面密度として求めよ。
* コンデンサーに蓄えられているエネルギーを求めよ。

**Quiz 5(6月3日出題)**  
原点にある磁気双極子モーメント\\( \boldsymbol{m} \\)が点\\( \boldsymbol{r} \\)につくるベクトルポテンシャルは
\\[
  \boldsymbol{A}(\boldsymbol{r}) = \dfrac{\mu_0}{4\pi} \dfrac{ \boldsymbol{m} \times \boldsymbol{r}}{\lvert \boldsymbol{r} \rvert^3}
\\]
である。このベクトルポテンシャルが表す磁束密度\\( \boldsymbol{B} \\)を計算し、結果が磁気双極子モーメントが\\( \boldsymbol{r} \ne 0\\)に作る磁束密度
\\[
  \boldsymbol{B} = \dfrac{\mu_0}{4\pi} 
  \left\[3 \dfrac{(\boldsymbol{m}\cdot \boldsymbol{r} ) \boldsymbol{r} }{r^{5}} - \dfrac{\boldsymbol{m}}{r^{3}}\right\]
\\]
と同じことを確認せよ。

**Quiz 6(6月10日出題)**  
講義で、半径\\( a\\)の無限に長い円柱型常磁性体(透磁率\\( \mu \\))に一様に電流 \\( I \\)が流れているときの、磁場\\( \boldsymbol{H} \\)と磁束密度\\( \boldsymbol{B} \\)を取り扱った。復習も兼ねて以下の問いに解答せよ。
* 磁場を、半径が\\( r >a \\)と\\( r < a \\)の場合に分けて導出せよ。
* 同様に磁束密度を求めよ。
* 同様に磁化を求めよ。
* 磁化と等価な磁化電流密度\\( \boldsymbol{i}_M \\)を\\( r< a\\)で求めよ。( \\( \nabla \cdot \boldsymbol{i}_M = 0\\)より、\\( r=a \\)では、この磁化電流をうち消すだけの逆向きの電流が流れていることになる。)


**Quiz 7(6月17日出題)**  
渦度\\( \boldsymbol{\omega} \\)を
\\[
  \boldsymbol{\omega} = \nabla \times \boldsymbol{v} + \dfrac{q}{m} \boldsymbol{B}
\\]
と定義する。
速度場の時間発展が
\\[
  \dfrac{\partial \boldsymbol{v}}{\partial t} + (\boldsymbol{v}\cdot \nabla ) \boldsymbol{v} = 
  \dfrac{q}{m} ( \boldsymbol{E} + \boldsymbol{v}\times \boldsymbol{B})
\\]
を満たすとき、
渦度の時間発展が
\\[
  \dfrac{\partial \boldsymbol{\omega}}{\partial t} = \nabla \times (\boldsymbol{v} \times \boldsymbol{\omega})
\\]
となることを示せ。
(ヒント: (8)式から出発する。まず両辺の回転を取る。\\( \nabla \times \boldsymbol{E} = - \dfrac{\partial \boldsymbol{B}}{\partial t} \\) をつかって、電場の回転を磁場の時間変化に置き換える。時間微分に関する項をすべて左辺に集める。\\( (\boldsymbol{v}\cdot \nabla) \boldsymbol{v}  \\)を\\( \boldsymbol{v} \times (\nabla \times \boldsymbol{v}) \\)をつかって置き換える。)

**Quiz 8(7月1日出題)**  
実電荷も実電流も存在しない物質(誘電率\\( \epsilon \\)、透磁率\\( \mu \\))中を電磁波が伝わるとき、
その電磁波のエネルギー流束はPoyntingベクトル\\( \boldsymbol{S} = \boldsymbol{E} \times \boldsymbol{H} \\)で表される。
このPoyntingベクトルベクトルを平面波
$$
\begin{align}
\boldsymbol{E} & = \boldsymbol{E_0} \cos ( \boldsymbol{k} \cdot \boldsymbol{r} - \omega t) \\
\boldsymbol{B} & = \dfrac{\boldsymbol{k} \times \boldsymbol{E_0}}{\omega} \cos ( \boldsymbol{k} \cdot \boldsymbol{r} - \omega t) 
\end{align}
$$
のもと計算し、時間的に一周期にわたり平均をとると
\\[
  \boldsymbol{S} = \dfrac{1}{2}\sqrt{\dfrac{\epsilon}{\mu}} \left\lvert \boldsymbol{E_0}\right\rvert^2 \dfrac{\boldsymbol{k}}{ \left\lvert \boldsymbol{k}\right\rvert}
\\]
となることを示せ。

**Quiz 9(7月8日出題)**  
\\( N \\)個の抵抗値\\( R_i \enspace i=1,2,\dots,N \\)をもつ抵抗を並列につなぐ。
この並列につないだときの合成抵抗をキルヒホッフの法則にもとづき導出せよ。

**Quiz 10(7月15日出題)**  
抵抗値\\( R \\)の抵抗と電気容量\\( C \\)のキャパシタが直列につながれており、この二つの素子のみで閉回路が構成されているとする。
時刻\\( t=0 \\)で、キャパシタに電荷が\\( q(0) = q_0 \\)蓄えられていたとする。
* 時刻\\( t \ge 0 \\)で、キャパシタに蓄えられている電荷の大きさを求めよ。
* 抵抗で発生するジュール熱の総和
\\[
  \int_0^\infty R I(t)^2 dt
\\]
が元のキャパシタに蓄えられていたエネルギーと等しいことを示せ。


**Quiz 11(7月22日出題)**  
講義で黒板にいくつか書き間違いがあったので、復習をかねてRLC回路に交流起電力をつないだ場合を考える。
抵抗値\\( R \\)の抵抗と、電気容量\\( C \\)のキャパシタ、自己インダクタンス\\( L\\)のコイル、および交流起電力が直列につながれ閉回路を作っている。
このとき交流起電力の形が\\( \mathcal{E} = \mathcal{E}_0 e^{i \omega t} \\)として、回路のインピーダンス、電流の振幅、および位相を求めよ。


-----
期末試験(60%)、及びQuiz等(平常点 40%)で判断する。シラバスに従う。


文献
-----
電磁気学詳論Iでつかった教科書や資料は参考になります。
それ以外の参考書、演習書などをあげおきます。
参考書は、詳しい内容や教科書以外の記述を見たくなった場合に利用してください。
すべて大学図書館にあると思います。
* 参考書: 前野昌弘「よくわかる電磁気学」東京図書
* 参考書: 太田浩一「電磁気学の基礎I」東京大学出版会
* 参考書: 太田浩一「電磁気学の基礎II」東京大学出版会
* 参考書: J. D. ジャクソン(著)、西田稔(訳)「電磁気学(上)」吉岡書店
* 演習書: 後藤憲一、山崎修一郎(編)「詳解電磁気学演習」共立出版
