---
title: "非平衡現象論"
collection: courses
type: "理学研究科宇宙地球科学専攻大学院科目"
permalink: /courses/2025-spring-noneq
venue: "大阪大学, 理学部"
date: 2025-03-28
location: "Osaka, Japan"
---

大学院科目、木曜日2限、理B307教室  
[CLE授業支援システム](https://www.cle.osaka-u.ac.jp/ultra/courses/_218473_1/outline)  

[このページ](https://stsykw.github.io/courses/2025-spring-noneq)

スケジュール
----------
**4月10日**  
平衡近傍でのゆらぎ: Boltzmann-Einsteinの原理。孤立系、開放系での表現  

**4月17日**  
(休講)

**4月24日**  
ゆらぎの動力学: 現象論的方程式、Onsagerの相反関係、Onsager係数の決定  

**5月8日**  
ゆらぎの動力学: Langevin方程式とFokker-Planck方程式、例:Brown運動、例:ポテンシャルのある場合  

**5月15日**  
線形応答理論: 静的な場合、動的な場合、揺動散逸定理  

**5月22日**  
ゆらぎの定理: Jarzynski等式、ゆらぎの定理  

**5月29日**  
ゆらぎの定理: ゆらぎの定理の証明、線形応答との対応  

**6月5日**  
情報と熱力学: Maxwellデーモン、Szilardエンジン、Landauer原理、フィードバック系のゆらぎの定理  


Quiz
----
**Quiz 1(4月10日出題)**  
マクロ量 \\( \\{ a_i \\} \\)の平衡値 \\( \\{ \overline{a_i} \\} \\)からのずれは
エントロピーで支配され
\\[
P(\\{a_i\\}) = (2\pi)^{-n/2} \left[ \det \left(
-\dfrac{1}{k_\mathrm{B}} \dfrac{\partial^2 S}{\partial a_i \partial a_j }
 \right)
 \right]^{1/2}
\exp \left(
\dfrac{1}{2 k_\mathrm{B}}
\sum_{ij} \dfrac{\partial^2 S}{\partial a_i \partial a_j} (a_i - \overline{a_i}) (a_j - \overline{a_j})
\right)
\\]
と書ける。この多次元Gauss積分を実行し、規格化定数がこれで良いことを確認せよ。


**Quiz 2(4月10日出題)**  
マクロ量 \\( \\{ X_i \\} \\)の分布
\\[
P(\\{X_i\\}) \propto
\exp \left(
-\dfrac{1}{2}
\sum_{ij} \beta_{ij} X_i X_j
\right)
\\]
に対し、期待値 \\( \left\langle X_i X_j \right\rangle = (\beta^{-1})\_{ij} \\) となることを示せ。
また
\\(x_i = \sum_j \beta_{ij} X_j\\)と置いたとき、
\\( \left\langle x_i X_j \right\rangle = \delta_{ij} \\)、
\\( \left\langle x_i x_j \right\rangle = \beta_{ij} \\)となることを示せ。

**Quiz 3(4月10日出題)**  
熱浴および圧力浴と接している系に対してエントロピーゆらぎの二乗の期待値および圧力ゆらぎの二乗の期待値が
\\[
  \left \langle (\Delta S)^2 \right\rangle = k_\mathrm{B} C_p \, , \, \, 
  \left \langle (\Delta p)^2 \right\rangle = \dfrac{k_\mathrm{B} T}{V \chi_S}
\\]
となることを示せ。ここで\\( C_p , \chi_S \\)はそれぞれ等圧熱容量、断熱圧縮率である。

**Quiz 4(4月24日出題)**  
オンサーガー係数やノイズの計算で
\\[
I=\int_{0}^{t}  ds_{1}\int_{0}^{t}  ds_{2} \, f(s_{1}-s_{2})
\\]
の形の積分がでてきた。
\\( f \\) が偶関数のとき
\\[
  I = \int_{0}^{t}  dx\, 2 (t -x ) f(x) 
\\]
とできることを示せ。

**Quiz ５(5月8日出題)**  
ブラウン運動のLangevin表現、
\\[
  \dfrac{dp_i}{dt} = - \dfrac{f}{T_R M} p_i + \xi_i(t)
\\]
ただし\\(  \langle \xi_i(t) \rangle_{eq} = 0 \enspace , \quad \langle \xi_i(t) \xi_j (t') \rangle_{eq} = 2 k_\mathrm{B} f \delta_{ij} \delta (t-t') \\)に対して、
初期条件\\( p_i(0) = p_i^0 \\) のもと、\\( p_i(t) \\)の解を求めよ。
これを使い、
\\[
\langle p_i (t+\tau) p_j (t) \rangle_{p_i(0)=p_i^0, p_j(0)=p_j^0}
\\]
を計算せよ。また、初期値 \\( p_i^0, p_j^0 \\)を熱平衡にとり十分に時間が経った後の、
\\[
\langle p_i (t+\tau) p_j (t) \rangle_{eq} - \langle p_i (t+\tau) \rangle_{eq} \langle p_j (t) \rangle_{eq}
\\]
を計算せよ。

**Quiz 6(5月8日出題)**  
Quiz5の
\\[
\langle p_i (t+\tau) p_j (t) \rangle_{eq} - \langle p_i (t+\tau) \rangle_{eq} \langle p_j (t) \rangle_{eq}
\\]
を、対応するFokker-Planck方程式をつかって計算せよ。


**Quiz 7(5月15日出題)**  
講義ではハミルトニアンが無摂動状態\\( H_0\\)から外場\\(E\\)のもと\\( H_0- M E \\)と変化する時の物理量\\(A \\)の応答を見た。
摂動を、逆温度をつかって\\( E = 1- \beta' / \beta \\)と与えたとき、\\(A=M=H_0 \\)として熱容量を求めよ。

**Quiz 8(5月15日出題)**  
\\(L \times L \times L \\)の立方体中に\\( N \\)個の古典的な自由粒子が
逆温度\\( \beta \\)の熱平衡状態として存在している。
この自由粒子の重心位置\\( \dfrac{1}{N} \langle \sum_i q_i^z \rangle \\)の
重力に対する応答を、重力が小さいとした線形応答の範囲で調べよ。
また、重力は立方体のある辺と平行なz軸負の向きにかかるとする。
この系では厳密な重心位置も評価できるので、線形応答の結果と比較せよ。

**Quiz 9(5月15日出題)**  
複素アドミッタンス
\\[
\chi_{AM}(\omega) = \lim_{\epsilon \downarrow 0}\int_{0}^{\infty} ds \phi_{AM}(s)  e^{i\omega s} e^{-\epsilon s}
\\]
に対し、Kramers-Kronig関係式
\\[
\Re \chi_{AM}(\omega)  = \pv\int_{-\infty}^{\infty} \dfrac{d\omega'}{\pi} \Im \dfrac{\chi_{AM}(\omega')}{\omega'-\omega}
\\]
\\[
\Im \chi_{AM}(\omega)  = - \pv\int_{-\infty}^{\infty} \dfrac{d\omega'}{\pi} \Re \dfrac{\chi_{AM}(\omega')}{\omega'-\omega}
\\]
が成立することを示せ。

**Quiz 10(5月22日出題)**  
運動量と座標の組\\(\{ p_i, q_i \} \\)がハミルトニアン\\( H \\)に従って
時間変化するとする。
\\[
  \dot{q_i} = \dfrac{\partial H}{\partial p_i}
\\]
\\[
  \dot{p_i} = - \dfrac{\partial H}{\partial q_i}
\\]
このとき
位相空間中のある領域\\( \mathcal{D}(t) \\)の体積
\\[
  V(\Gamma(t)) =
  \int_{\mathcal{D}(t)} d\Gamma(t) 
\\] 
がLagrange的な時間変化に対して不変である事を示せ。


**Quiz 11(5月22日出題)**  
運動量\\( p\\)、座標\\( q\\)に対し
\\[
  \dfrac{dp}{dt} = 0 \enspace, \quad \dfrac{dq}{dt}= p
\\]
という運動を考える。
* この運動方程式が可逆であることを示せ。
* ある初期状態から時間\\( t\\)だけ時間発展させ、状態を時間反転し、おなじ時間\\( t \\)だけ時間発展し、時間反転するともとの初期状態に戻ることを示せ。

また
\\[
  \dfrac{dp}{dt} = -p \enspace, \quad \dfrac{dq}{dt}= p
\\]
という運動に対し、
* この運動方程式が可逆でないことを示せ。
* ある初期状態から時間\\( t\\)だけ時間発展させ、状態を時間反転し、おなじ時間\\( t \\)だけ時間発展し、時間反転してももとの初期状態に戻らないことを示せ。

**Quiz 12(5月22日出題)**  
与えられたハミルトニアンに対し
拡張された運動方程式
\\[
\dot{q_{i}} = \dfrac{\partial \mathcal{H}}{\partial p_i}
\\]
\\[
\dot{p_{i}} = - \dfrac{\partial \mathcal{H}}{\partial q_{i}} - \zeta p_{i}
\\]
\\[
   \dot{\zeta}  = \dfrac{1}{\tau^{2}} \left(   \beta \sum_{i} \dfrac{p_{i}^{2}}{m}  -  dN \right)
\\]
を考える。(\\(d\\)は空間次元である。)この時間発展にしたがうダイナミクスを能勢-Hooverダイナミクスと呼ぶ。能勢-Hooverダイナミクスでは運動方程式にしたがって時間発展すると、カノニカル分布が定常状態として得られることが知られている。
* ハミルトニアンの時間微分が
\\[
\dfrac{d\mathcal{H}}{dt} = - \zeta \sum_{i} \dfrac{p_{i}^{2}}{m}
\\]
となることを示せ。
* この時間発展で、分布関数\\( f(p_i,q_i,\zeta) \propto \exp ( -\beta H - \tau^2 \zeta^2 / 2 ) \\)が定常、すなわち時間微分が0であることを示せ。

**Quiz 13(5月29日出題)**  
体積\\( V \\)の三次元領域のなかに閉じこめられた古典的な粒子系が以下のハミルトニアンを持つとする。
\\[
  H = \sum_i \dfrac{\boldsymbol{p}\_i^2}{2m} + \dfrac{1}{2}\sum_{i,j (i\ne j)} \phi( \left\lvert \boldsymbol{q}\_i - \boldsymbol{q}\_j \right\rvert)
\\]
このとき
\\[
  \sigma_{\alpha\beta} = \dfrac{1}{V}\left( 
    \sum_i \dfrac{p_i^\alpha p_i^\beta}{m} + \dfrac{1}{2}\sum_{i,j (i \ne j)} (q_i^\alpha-q_j^\alpha)
    (f_{ij}^\beta)
  \right)
\\]
が応力テンソルの\\( \alpha\beta \\)成分となることを示せ。\\(p_i^\alpha \\)は\\( i\\)番目の粒子の運動量の\\(\alpha\\)成分、\\( f_{ij}^\beta \\)は\\( j \\)番目の粒子が\\( i\\)番目の粒子におよぼす力の\\(\beta \\)成分である。

**Quiz 14(6月5日出題)**  
同時情報量
\\[
S(X,Y) = -\sum_{x,y} P_{X\otimes Y}(x,y) \log P_{X\otimes Y}(x,y)
\\]
を、情報量
\\[
  S(X) = - \sum_{x} P_{X}(x) \log P_{X}(x)
\\]
と、条件付き情報量
\\[
S(X|Y)=  - \sum_{y} P_{Y}(y) \sum_{x} P_{X}(x|y) \log P_{X}(x|y)  
\\]
をつかって
\\[
  S(X,Y) = S(Y) + S(X|Y)
\\]
と表すことができることを示せ。

**Quiz 15(6月5日出題)**  
相互情報量
\\[
  I(X,Y) =  \sum_{x,y} P_{X\otimes Y} (x,y) \log \dfrac{P_{X\otimes Y}(x,y)}{P_{X}(x) P_{Y}(y)}
\\]
を、
\\[
 I(X,Y) =  S(X) + S(Y)  - S(X, Y)
\\]
と表すことができることを示せ。

評価
---
期末レポート、およびQuizの解答状況(数問選んで、最後に提出)をみて総合的に判断する。
詳細はシラバスを参照してください。


参考書、参考文献
-------------
一般的なこと
* S. R. de Groot and P. Mazur "Non-equilibrium Thermodynamics", Dover Publications
* 一柳正和「不可逆過程の物理」日本評論社
* 川崎恭治「非平衡と相転移-メソスケールの統計力学-」朝倉書店
* 早川尚男「非平衡統計力学」サイエンス社
* 北原和夫「非平衡系の統計力学」岩波書店
* 鈴木増雄「統計力学、岩波講座現代の物理学」岩波書店
* 戸田盛和、久保亮五、斎藤信彦、橋爪夏樹「統計物理学、現代物理学の基礎第二版」岩波書店
* 関本謙「ゆらぎのエネルギー論」岩波書店
* 沙川貴大「非平衡統計力学」共立出版
* 齊藤圭司「ゆらぐ系の熱力学」サイエンス社
* D. N. Zubarev "Nonequilibrium Statistical Thermodynamics", Consultants Bureau
* R. Zwanzig "Nonequilibrium Statistical Mechanics", Oxford
* M. Ichiyanagi, ["Conceptual developments of non-equilibrium statistical mechanics in the early days of Japan", Phys. Rep. **262** (1995) 227.](http://www.sciencedirect.com/science?_ob=MImg&_imagekey=B6TVP-3YF4GW9-6-2&_cdi=5540&_user=5735665&_orig=browse&_coverDate=11%2F30%2F1995&_sk=997379994&view=c&wchp=dGLzVlz-zSkWA&md5=eb16ad3f3147413c76cc65ec10af35e6&ie=/sdarticle.pdf)
* R. Kubo, M. Toda, and N. Hashitsume, "Statistical Physics II, Nonequilibirum Statistical Mechanics" Spinger-Verlag
* J. A. McLennan, "Introduction to Non-equilibrium Statistical Mechanics" Prentice-Hall
* 佐々真一「非平衡現象論」講義ノート

Einsteinのゆらぎの理論
* L. Landau, E. Lifshitz 「統計物理学 (下)」岩波書店, L. Landau, E. Lifshitz, "Statistical Physics (course of theoretical physics volume 5) Butterworth-Heinemann"
* A. Einstein, "Theorie der Opaleszenz von homogenen Flüssigkeiten und Flüssigkeitsgemischen in der Nähe des Kritischen Zustandes", Ann. der Phys. **33** (1910), pp. 1275-1298. 邦訳 アインシュタイン選集1、監修 湯川秀樹 翻訳 井上健、谷川安孝、中村誠太郎 共立出版(1971)

確率過程
* N. G. van Kampen, "Stochastic Processes in Physics and Chemistry", Elsevier

ブラウン運動
* A. Einstein "Investigations on the theory of the Brownian movement", Dover

Onsagerの相反定理、Onsager-Machlup過程
* L. Onsager, ["Reciprocal Relations in Irreversible Processes I", Phys. Rev. **37** (1931) 405.](http://prola.aps.org/abstract/PR/v37/i4/p405_1)
* L. Onsager, ["Reciprocal Relations in Irreversible Processes II", Phys. Rev. **38** (1931) 2265.](http://prola.aps.org/abstract/PR/v38/i12/p2265_1)
* 上記二つの論文の翻訳が[物性研究](https://doi.org/10.14989/178097)にある。
* 橋爪夏樹、["A Statistical Theory of Linear Dissipative Systems", Prog. Theor. Phys. **8** (1952) 461.](https://doi.org/10.1143/PTP/8.4.461)s
* L. Onsager and S. Machlup, ["Fluctuations and Irreversible Processes", Phys. Rev. **91**, 1505, (1953).](http://prola.aps.org/abstract/PR/v91/i6/p1505_1)
* M. Ichiyanagi ["Variational principles of irreversible processes", Phys. Rep. **243**, 125,(1994)](http://www.sciencedirect.com/science/article/pii/0370157394900523)

線形応答
* 戸田盛和、久保亮五、斎藤信彦、橋爪夏樹「統計物理学、現代物理学の基礎第二版」岩波書店
* R. Kubo, M. Toda, and N. Hashitsume, "Statistical Physics II, Nonequilibirum Statistical Mechanics" Spinger-Verlag

ゆらぎの定理、Jarzynski等式
* D. J. Evans and  D. J. Searles, ["The Fluctuation Theorem"</a>, Adv. Phys. **51** (2002) 1529.](http://taylorandfrancis.metapress.com/index/GY5R6P9XX8RYVXGR.pdf)
* G. E. Crooks, ["Entropy production fluctuation theorem and
    the non equilibrium work relation for free energy
  differences", Phys. Rev. E **60**, 2721, (1999).]()
* C. Jarzynski, ["Nonequilibrium Equality for Free Energy
  Differences", Phys. Rev. Lett. **78**, 2690 (1997).]()
* C. Jarzynski, ["Nonequilibrium  work theorem for a system strongly coupled to a thermal environment", J. Stat. Mech.: Theor. Exp. **P09005**, (2004).]()

情報と熱力学
* H. Leff and A. F. Rex ed. "Maxwell's Demon 2 Entropy, Classical and Quantum Information, Computing", Institute of Physics Publishing


大偏差性
* 大野克嗣、["Large Deviation and Statistical Physics", Prog. Theor. Phys. Suppl. **99** (1989) 165.](https://doi.org/10.1143/PTPS.99.165)
* 大野克嗣、["Onsager's Principle from Large Deviation Point of View", Prog. Theor. Phys. **89** (1993) 973.](https://doi.org/10.1143/PTP.89.973)
* H. Touchette, ["The large deviation approach to statistical mechanics", arXiv:0804.0327](http://arxiv.org/abs/0804.0327)
