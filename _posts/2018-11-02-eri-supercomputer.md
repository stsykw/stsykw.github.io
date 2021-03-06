---
title: '地震研でLIGGGHTS'
date: 2018-11-02
permalink: /posts/2018/11/liggghts/
tags:
  - computer
  - liggghts
---


地震研でLIGGGHTS
===============

**注意: 実際の動作を保証するものではありません。特定の人物に向けて書いています。**

ファイルの用意
-----------
手元のコンピュータでインプットファイル、ジョブ実行スクリプト(下で説明)を準備する。
たとえばin.packing、job.sh。これを地震研に転送。下記の操作で地震研の計算機のホームディレクトリにコピーできる。
```
scp ./in.packing username@eic.eri.u-tokyo.ac.jp:~/
scp ./job.sh username@eic.eri.u-tokyo.ac.jp:~/
```

もちろん地震研の計算機でインプットファイル、ジョブ実行スクリプトを編集して用意しても良い。

ログイン
------
地震研計算機にログイン
```
ssh username@eic.eri.u-tokyo.ac.jp
```

実行
---
用意したジョブ実行スクリプトを計算キューに投入する。
計算は、スクリプトを投入したディレクトリで実行される。
```
qsub job.sh
```

計算の様子を確認するには
```
qstat  
```
この出力から自分のユーザー名、投入したジョブクラスを探す。


ジョブ実行スクリプトの内容
----------------------
```sh

#!/bin/bash  
#$ -jc B  
#$ -ac n=8  
#$ -ac P=8  
#$ -cwd  

LD_LIBRARY_PATH=/home/yuk/local/lib/:$LD_LIBRARY_PATH mpiexec_mpt -np 8 dplace -s1 /home/yuk/local/bin/liggghts_mpi < in.packing
```
#から始まる行はコメントで一行目はスクリプトを実行するプログラム名を指定している。
変更する必要なし。  
二行目から四行目はジョブクラスと並列度を指定する。上の例は、Bクラス、8並列を指定している。
[指定できる内容はここにある。](http://wwweic.eri.u-tokyo.ac.jp/computer/manual/eic2015/index.php?%E3%83%90%E3%83%83%E3%83%81%E3%82%B8%E3%83%A7%E3%83%96%EF%BC%88%E9%AB%98%E9%80%9F%E8%A8%88%E7%AE%97%E3%82%B5%E3%83%BC%E3%83%90%EF%BC%89) 当面はBクラスの8並列で大丈夫だと思うが、計算時間が足りなければ別のクラスの利用も考える。  
五行目はスクリプトを投入したディレクトリで実行するための指定。

LD...からはじまる行が実際の計算を実行している部分。
変更する必要があるのは、mpiexec_mptのあとにある-npの後ろの数字。これをジョブクラスの並列数をあわせる必要がある。またインプットファイルも変更する必要あり。

計算結果を手元に
--------
計算結果のファイルを手元に得るにはファイルを送り込んだscpの逆をすれば良いが、ファイル数が多いので先にまとめた方が簡単。  
ファイルをまとめる
```
tar cvfz test.tar.gz test test1 test3
```
test test1 test3 のファイルやディレクトリがtest.tar.gzという名前でまとめられる。まとめたファイルをscpで転送。
まとめたファイルをバラバラにするには
```
tar xvf test.tar.gz
```
