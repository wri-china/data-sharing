# 中国省级财政数据2023-2024

本数据集为中国省级2023年财政预算执行情况和2024年财政预算计划的数据，涵盖9个省（市），包括北京市、广东省、河北省、江苏省、山东省、上海市、四川省、天津市和浙江省。数据内容主要包括各省的国有资本经营收入和支出、社会保险基金收入和支出、一般公共收入和支出、政府性基金收入和支出。这些数据由各省政府或财政厅发布，并通过校正后整理为结构化的Excel表格格式。

## 数据整理流程

1. 从官网下载公开官方报告
2. 将PDF报告转为Doc或PNG的形式
3. 利用文字识别AI工具，分离表格数据
4. 修改自动识别中不准确的数据和文字，如小数点识别为逗号、数字或文字遗漏，表格识别错行等特殊情况
5. 若有特殊格式的报告，如2023年和2024年的数据不在一张表格中，则需要手动对齐表格/增删科目类别
6. 使用Excel自带功能，核验各类账目是否配平，确保数据和PDF报告中一致
7. 进行表格的分级，方便后续代码读取使用，按照报告原分级，将财政数据类别分解为一级、二级、三级和四级类目
8. 合并整理表格，共计10列，包括：
    - 省份
    - 表名称：国有资本经营收入、国有资本经营支出、社会保险基金收入、社会保险基金支出、一般公共收入、一般公共支出、政府性基金收入、政府性基金支出
    - 项目一级
    - 项目二级
    - 项目三级
    - 项目四级
    - 2023年执行数
    - 2024年计划数
    - 计划数为执行数百分比
    - Index


## 数据来源

#### 北京市 - [北京市人民政府](https://www.beijing.gov.cn/)
- [北京市 2023 年预算执行情况和2024 年预算](https://www.beijing.gov.cn/gongkai/caizheng/czbg/ysbg/202402/W020240220729348087558.pdf)
- [关于北京市 2023年预算执行情况和2024年预算的报告](https://www.beijing.gov.cn/gongkai/caizheng/czbg/ysbg/202402/W020240202423465960076.pdf)

#### 广东省 - [广东省人民政府](https://www.gd.gov.cn/)
- [广东省 2023年预算执行情况和2024年预算草案的报告](https://www.gd.gov.cn/attachment/0/542/542789/4361282.pdf)
- [广东省 2023年预算执行情况和 2024年预算草案附件二表格附件](https://www.gd.gov.cn/attachment/0/542/542791/4361282.pdf)
- [广东省 2023年预算执行情况和2024年预算草案的报告网页](https://www.gd.gov.cn/zwgk/czxx/sjczyjs/ys/content/post_4361282.html)

#### 河北省 - [河北省人民政府](https://www.hebei.gov.cn/)
- [关于河北省 2023年预算执行情况和2024年预算草案的报告（书面）](https://www.hebei.gov.cn/attachments/1/202401/28/%E9%A2%84%E7%AE%97%E6%8A%A5%E5%91%8A-%E9%99%84%E8%A1%A8.pdf20240128183610173.pdf?sid=da5fc236-ee17-4f7e-be36-ffcd5f23c87b)
- [河北省 2023年全省及省本级预算完成情况表](https://www.hebei.gov.cn/attachments/1/202401/28/%E9%A2%84%E7%AE%97%E6%8A%A5%E5%91%8A-%E9%99%84%E8%A1%A8.pdf20240128183610173.pdf?sid=da5fc236-ee17-4f7e-be36-ffcd5f23c87b)
- [河北省2023年预算执行情况和2024年预算草案的报告网页](https://www.hebei.gov.cn/columns/faa0e062-09f9-4519-b152-616a9ef8c6de/202401/28/ab5664b3-e5e4-452a-ba93-99ee3f1bd9df.html)

#### 江苏省 - [江苏省财政厅](https://czt.jiangsu.gov.cn/)
- [江苏省 2023年预算执行情况 与 2024年预算（草案）](https://czt.jiangsu.gov.cn/attach/-1/2402151557302341324.pdf)
- [关于江苏省 2023年预算执行情况 与2024年预算草案的报告](https://czt.jiangsu.gov.cn/attach/-1/2402151516061604378.pdf)

#### 山东省 - [山东省财政厅](http://czt.shandong.gov.cn/)
- [关于山东省 2023年预算执行情况和 2024年预算草案的报告](http://czt.shandong.gov.cn/module/download/downfile.jsp?classid=0&filename=49ca088112224d33b2df8eeeb8521119.pdf)
- [山东省 2023年预算执行情况和 2024年预算草案](http://czt.shandong.gov.cn/module/download/downfile.jsp?classid=0&filename=14b5035df3314b60ac43dcc1a7b971d4.pdf)

#### 上海市 - [上海市财政局](https://czj.sh.gov.cn/)
- [关于上海市2023年预算执行情况和2024年预算草案的报告](https://czj.sh.gov.cn/zys_8908/czsj_9054/zfyjs/yjsbg_9056/20240130/ed3e7f3402e24a37ababd897481cb458.html)
- [上海市全市及市本级2024年预算和2023年预算执行情况](https://czj.sh.gov.cn/zys_8908/czsj_9054/zfyjs/yjsbg_9056/20240131/0d1a71ed237a4ef483e9d5a1b813b347.html)

#### 四川省 - [四川省财政厅](https://czt.sc.gov.cn/scczt/index.shtml) - [四川省人民政府](https://www.sc.gov.cn/10462/index.shtml)
- [关于四川省2023年预算执行情况和2024年预算草案的报告](https://www.sc.gov.cn/10462/10464/10699/10702/2024/2/19/256c549788f14ae280d0503a1524cb02.shtml)
- [四川省2023年预算执行情况和2024年预算草案的报告及相关表格](https://czt.sc.gov.cn/scczt/c102371/2024/2/5/51dff1f4f4e943cea7a38744dde5d357.shtml)

#### 天津市 - [天津市人民政府](https://www.tj.gov.cn/) - [天津市财政局](https://cz.tj.gov.cn/)
- [关于天津市2023年预算执行情况和2024年预算草案的报告](https://cz.tj.gov.cn/zwgk_53713/yjsgktypt/ysgk/2024nzfys/202402/W020240209506245077061.pdf)
- [天津市2023年预算执行情况和2024年预算](https://www.tj.gov.cn/zwgk/zfxxgkzl/fdzdgknr/czyjs/sbj/202403/W020240318417161634640.pdf)

#### 浙江省 - [浙江省财政厅](https://czt.zj.gov.cn/)
- [关于2023年全省和省级预算执行情况及2024年全省和省级预算草案的报告](https://zjjcmspublic.oss-cn-hangzhou-zwynet-d01-a.internet.cloud.zj.gov.cn/jcms_files/jcms1/web1791/site/attach/0/ade3dd24d9064333bfe4f86e2153533f.pdf)
- [浙江省2023年全省和省级一般公共预算执行情况及2024年全省和省级一般公共预算](https://zjjcmspublic.oss-cn-hangzhou-zwynet-d01-a.internet.cloud.zj.gov.cn/jcms_files/jcms1/web1791/site/attach/0/ac30500bb0bd4bea9bc7b06169bd653f.pdf)
