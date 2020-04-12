## Sequoia选股系统
### 简介
本程序使用[TuShare Pro接口](https://tushare.pro/)，获取数据,此接口需要注册Token才能生效;


数据保存在data中，使用sqlite存储在db中，数据分析使用DataFrame格式。

### 海龟交易法则
本程序实现了海龟交易法则，使用20日突破线作为选股条件，具体代码：strategy/turtle

## 安装依赖:
 ### 使用Python3.5以上以及pip3
 ### Python 依赖:
 ```
 pip install -r requirements.txt 
 ```
 
## 运行
### 本地运行

#### 获取数据，并更新数据
```
$ fetch_stock_main.py
```

####运行策略
```
$ strategy_main.py
```



