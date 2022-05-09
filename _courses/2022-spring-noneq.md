---
title: "非平衡現象論"
collection: courses
type: "理学研究科宇宙地球科学専攻大学院科目"
permalink: /courses/2022-spring-noneq
venue: "大阪大学, 理学部"
date: 2022-03-03
location: "Osaka, Japan"
---

大学院科目、月曜日2限、理F202教室



 
スケジュール
----------
**4月11日**  
平衡近傍でのゆらぎ: Boltzmann-Einsteinの原理。孤立系、開放系での表現  

**4月18日**  
ゆらぎの動力学: 現象論的方程式、Onsagerの相反関係、Onsager係数の決定  

**4月25日**  
ゆらぎの動力学: Langevin方程式とFokker-Planck方程式、例:Brown運動、例:ポテンシャルのある場合、例:不均一系

**5月2日**  
いちょう祭のため休講

**5月9日**  
線形応答理論: 静的な場合、動的な場合、揺動散逸定理  

**5月16日**  
ゆらぎの定理: Jarzynski等式、ゆらぎの定理、線形応答との対応  


**5月23日**  

**5月30日**  

**6月6日**  




Quiz
----
**Quiz 1(4月11日出題)**  
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

**Quiz 2(4月11日出題)**  
マクロ量 \\( \\{ x_i \\} \\)の分布
\\[
P(\\{x_i\\}) \propto
\exp \left(
-\dfrac{1}{2}
\sum_{ij} \beta_{ij} x_i x_j
\right)
\\]
に対し、期待値 \\( \left\langle x_i x_j \right\rangle = \beta_{ij}^{-1}\\)となることを示せ。また
\\(X_i = \sum_j \beta_{ij} x_j\\)と置いたとき、
\\( \left\langle X_i x_j \right\rangle = \delta_{ij} \\)、
\\( \left\langle X_i X_j \right\rangle = \beta_{ij} \\)となることを示せ。


**Quiz 3(4月18日出題)**  
Hall効果をDrudeモデルにより考察する。
電荷\\(q\\)をもつ質量\\(m\\)の荷電粒子が運動方程式
\\[
  m \dfrac{d\mathbf{v}}{dt} = q \mathbf{E} + q \mathbf{v} \times
  \mathbf{B}- \gamma \mathbf{v}
\\]
に従うとする。ここで\\(\mathbf{E}, \mathbf{B}\\)はそれぞれ電場、磁場、\\(\gamma\\)は散逸を表す。
電場、磁場が\\(\mathbf{E} = (E_x, E_y, 0) , \mathbf{B} = (0,0,B)\\)のとき、
定常速度\\( (v_x, v_y) \\)を求め、電気伝導率テンソル\\( \sigma_{xx}, \sigma_{xy},\sigma_{yx},\sigma_{yy} \\)を
\\[
v_x  = \sigma_{xx} E_x + \sigma_{xy} E_y 
\\]
\\[
v_y  = \sigma_{yx} E_x + \sigma_{yy} E_y
\\]
で定義したとき、電気伝導率テンソル\\( \sigma_{xy} , \sigma_{yx} \\)に関してOnsagerの相反定理が成立していることを確認せよ。

**Quiz 4(4月18日出題)**  
講義ではマクロ物理量 \\( \\{ a_i \\} \\)の時間発展を条件付き確率 \\( W_{\Delta t} (a_i+\Delta a_i | a_i) \\)で表した。この条件付き確率が詳細つりあい
\\[
  W_{\Delta t} (a_i+\Delta a_i | a_i) P_{eq}(a_i) = 
    W_{\Delta t} (a_i | a_i+\Delta a_i) P_{eq}(a_i+\Delta a_i)
\\]
を満たすことを示せ。

**Quiz ５(4月25日出題)**  
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

**Quiz 6(4月25日出題)**  
Quiz5の
\\[
\langle p_i (t+\tau) p_j (t) \rangle_{eq} - \langle p_i (t+\tau) \rangle_{eq} \langle p_j (t) \rangle_{eq}
\\]
を、対応するFokker-Planck方程式をつかって計算せよ。


**Quiz 7(5月9日出題)**  
講義ではハミルトニアンが無摂動状態\\( H_0\\)から外場\\(E\\)のもと\\( H_0- M E \\)と変化する時の物理量\\(A \\)の応答を見た。
摂動を逆温度をつかって\\( E = 1- \beta' / \beta \\)と与えたとき、\\(A=M=H_0 \\)として熱容量を求めよ。


**Quiz 8(5月9日出題)**  
\\(L \times L \times L \\)の立方体中に\\( N \\)個の古典的な自由粒子が
逆温度\\( \beta \\)の熱平衡状態として存在している。
この自由粒子の重心位置\\( \dfrac{1}{N} \langle \sum_i q_i^z \rangle \\)の
重力に対する応答を線形応答の範囲で調べよ。
また、重力は立方体のある辺と平行なz軸負の向きにかかるとする。
この系では厳密な重心位置も評価できるので、線形応答の結果と比較せよ。


**Quiz 9(5月9日出題)**  
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
