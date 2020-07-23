# 此文档为补充文档 需结合 crawler frontera 文档观看

# frontera 部署 单机 伪代码（无法直接使用）
  git clone crawler [拉取cralwer代码]

# 目录结构
-  crawler-arch (启动脚本代码所在地)
   -  bin (启动脚本逻辑)
   -  conf (配置)
   -  single-crawler (scrapy 项目具体地址)
-  env (python 环境地址)
-  lib (无头浏览器，等三方库 暂无使用)
-  make (哥伦布编译脚本)

-  具体可以参考执行脚本

# 单机部署
-  1.在project代码外层创建env.sh 并添加instance_id=xxx(注：xxx可以为任何英文参数，)
-  2 在project目录层 mkider logs
   -  在logs下查看各个组件日志
-  3.进入opinion项目后, config修改配置(配置参数不明确 可参考frontera官方文档)
-  4.启动脚本
   -  sh opinion_control start sw 【调度 strategy/sw.py】
   -  sh opinion_control start db_consume 【启动存储，取值, 队列,和kafka-habse做交互】
   -  sh opinion_control start db_batch_gen 【启动分发, 主要分发url给spider】
   -  sh opinion_control start spider 【抓去spider】

# 哥伦布部署
-  哥伦布一键部署 无需任何操作
-  部署顺序优先级
   -  spider
   -  consume
   -  sw

# batch模块
-  batch模块由start_batch模块启动
-  crontab管理

#  手动添加第一批种子
-  run_add_seeds.sh 【无法运行，线上无法手动添加种子】
-  修改
   -  1.strategy/sw.py/read_seeds【方法】
   -  2.把if self._mxxxxx 放入
   -  3.修改condif/dbw.py/ 把if后等参数放入
   -  4.urls --> list
   -  5.把参数传入self.sche.seeds()

# 重要 重要 重要【hbase】
-  habse利用thrift和python模块happybase做连接
-  连接本地hbase时需要把COMPACT改为False
-  地址为python的site-packages下的frontear/setting
-  本项目为修改后frontera
