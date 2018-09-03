#!/usr/bin/env python3
# -*- coding: utf-8 -*-

t_doll_exp = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000,
              1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000,
              2100, 2200, 2300, 2400, 2500, 2600, 2800, 3100, 3400, 4200,
              4600, 5000, 5400, 5800, 6200, 6700, 7200, 7700, 8200, 8800,
              9300, 9900, 10500, 11100, 11800, 12500, 13100, 13900, 14600, 15400,
              16100, 16900, 17700, 18600, 19500, 20400, 21300, 22300, 23300, 24300,
              25300, 26300, 27400, 28500, 29600, 30800, 32000, 33200, 34400, 45100,
              46800, 48600, 50400, 52200, 54000, 55900, 57900, 59800, 61800, 63900,
              66000, 68100, 70300, 72600, 74800, 77100, 79500, 81900, 84300, 112600,
              116100, 119500, 123100, 126700, 130400, 134100, 137900, 141800, 145700,
              100000, 120000, 140000, 160000, 180000, 200000, 220000, 240000, 280000, 360000,
              480000, 640000, 900000, 1200000, 1600000, 2200000, 3000000, 4000000, 5000000, 6000000]

t_doll_exp_oath = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000,
                   1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000,
                   2100, 2200, 2300, 2400, 2500, 2600, 2800, 3100, 3400, 4200,
                   4600, 5000, 5400, 5800, 6200, 6700, 7200, 7700, 8200, 8800,
                   9300, 9900, 10500, 11100, 11800, 12500, 13100, 13900, 14600, 15400,
                   16100, 16900, 17700, 18600, 19500, 20400, 21300, 22300, 23300, 24300,
                   25300, 26300, 27400, 28500, 29600, 30800, 32000, 33200, 34400, 45100,
                   46800, 48600, 50400, 52200, 54000, 55900, 57900, 59800, 61800, 63900,
                   66000, 68100, 70300, 72600, 74800, 77100, 79500, 81900, 84300, 112600,
                   116100, 119500, 123100, 126700, 130400, 134100, 137900, 141800, 145700,
                   50000, 60000, 70000, 80000, 90000, 100000, 110000, 120000, 140000, 180000,
                   240000, 320000, 450000, 600000, 800000, 1100000, 1500000, 2000000, 2500000, 3000000]

fairy_exp = [300, 600, 900, 1200, 1500, 1800, 2100, 2400, 2700, 3000,
             3300, 3600, 3900, 4200, 4500, 4800, 5100, 5500, 6000, 6500,
             7100, 8000, 9000, 10000, 11000, 12200, 13400, 14700, 16000, 17500,
             18900, 20500, 22200, 23900, 25700, 27600, 29500, 31600, 33700, 35900,
             38200, 40500, 43000, 45500, 48200, 50900, 53700, 56600, 59600, 62700,
             65900, 69200, 72600, 76000, 79600, 83300, 87000, 90900, 94900, 99000,
             103100, 107400, 111800, 116300, 120900, 125600, 130400, 135300, 140400, 145500,
             150800, 156100, 161600, 167200, 172900, 178700, 184700, 190700, 196900, 203200,
             209600, 216100, 222800, 229600, 236500, 243500, 250600, 257900, 265300, 272800,
             280400, 288200, 296100, 304100, 312300, 320600, 329000, 337500, 357000]

squad_exp = [500, 900, 1300, 1800, 2200, 2700, 3200, 3600, 4000, 4500,
             5000, 5400, 5800, 6300, 6800, 7200, 7600, 8300, 9000, 9800,
             10600, 12000, 13500, 15000, 16500, 18300, 20100, 22000, 24000, 26300,
             28300, 30800, 33300, 35800, 38600, 41400, 44200, 47400, 50600, 53800,
             57300, 60800, 64500, 68200, 72300, 76400, 80500, 84900, 89400, 94100,
             98800, 103800, 108900, 114000, 119500, 124900, 130500, 136300, 142400, 148500,
             154600, 161100, 167700, 174500, 181500, 188500, 195500, 203000, 210600, 218200,
             226200, 234200, 242500, 250800, 259500, 268000, 277000, 286000, 295500, 304700,
             314500, 324000, 334500, 344000, 355000, 365000, 376000, 387000, 398000, 409000,
             421000, 432000, 444000, 456000, 469000, 481000, 493000, 506000, 537000]

fairy_info = [['勇士妖精', '04:30:00', '战斗', '25 %', '80 %', '40 %', '10 %', '0 %', '0'],
              ['暴怒妖精', '04:35:00', '战斗', '15 %', '0 %', '40 %', '10 %', '40 %', '0'],
              ['盾甲妖精', '03:00:00', '战斗', '22 %', '0 %', '0 %', '25 %', '22 %', '0'],
              ['护盾妖精', '03:05:00', '战斗', '20 %', '60 %', '80 %', '0 %', '0 %', '0'],
              ['防御妖精', '04:10:00', '策略', '22 %', '0 %', '80 %', '20 %', '0 %', '1'],
              ['嘲讽妖精', '03:10:00', '战斗', '18 %', '58 %', '28 %', '8 %', '25 %', '0'],
              ['狙击妖精', '03:30:00', '战斗', '0 %', '88 %', '28 %', '15 %', '36 %', '0'],
              ['炮击妖精', '03:35:00', '战斗', '55 %', '0 %', '56 %', '6 %', '0 %', '0'],
              ['空袭妖精', '03:40:00', '战斗', '30 %', '50 %', '40 %', '10 %', '0 %', '0'],
              ['增援妖精', '04:00:00', '策略', '12 %', '0 %', '88 %', '12 %', '15 %', '1'],
              ['空降妖精', '04:05:00', '策略', '36 %', '0 %', '32 %', '8 %', '40 %', '5'],
              ['布雷妖精', '05:30:00', '策略', '25 %', '44 %', '85 %', '0 %', '0 %', '3'],
              ['火箭妖精', '05:35:00', '策略', '0 %', '44 %', '0 %', '22 %', '35 %', '3'],
              ['工事妖精', '05:40:00', '策略', '15 %', '50 %', '40 %', '10 %', '20 %', '3'],
              ['指挥妖精', '05:00:00', '策略', '36 %', '0 %', '32 %', '8 %', '36 %', '1'],
              ['搜救妖精', '05:05:00', '策略', '32 %', '80 %', '64 %', '0 %', '0 %', '1'],
              ['照明妖精', '05:10:00', '策略', '0 %', '90 %', '32 %', '8 %', '38 %', '5'],
              ['黄金妖精', '深层映射排位奖励', '战斗', '20 %', '62 %', '50 %', '12 %', '25 %', '0'],
              ['八重樱妖精', '独法师联动奖励', '战斗', '26 %', '0 %', '24 %', '6 %', '32 %', '0'],
              ['耀夜姬妖精', '独法师联动奖励', '策略', '0 %', '70 %', '24 %', '15 %', '32 %', '3'],
              ['柯萝伊妖精', '独法师联动奖励', '战斗', '18 %', '55 %', '64 %', '6 %', '0 %', '0'],
              ['炊事妖精', '塌缩点排位奖励', '战斗', '10 %', '20 %', '80 %', '20 %', '10 %', '0'],
              ['希依妖精', '荣耀日联动奖励', '策略', '0 %', '0 %', '70 %', '18 %', '30 %', '0'],
              ['世拉妮娜妖精', '荣耀日联动奖励', '战斗', '15 %', '40 %', '50 %', '0 %', '20 %', '0'],
              ['普蕾娅卡米莉娅妖精', '荣耀日联动奖励', '战斗', '22 %', '50 %', '10 %', '10 %', '22 %', '0']]

script_moe = ["指挥官，我好饿啊 ...",
              "指挥官，用过餐点了吗",
              "指挥官，你要买东西吗？要就给你便宜点也不是不行哦 ~",
              "指挥官，所谓的奇迹啊，就要靠我纯真的魔法，和一点点钞票啦",
              "指挥官，今天又要买什么？都算你便宜哟！",
              "嘻嘻嘻，又有好多小钱钱 ... 咦！指挥官你在啊！",
              "最近物资挤压啊 ... 啊，指挥官！来得正好，现在特别算你便宜哦！",
              "哼哼哼 ... 啊，指挥官，今天心情不错，都算你便宜点哦 ~",
              "指挥官，在这样出手阔绰，我可要着迷了呢 ... 虽然是对钞票啦 ~",
              "指挥官，你这么大方，人家 ... 也不会给你便宜哦！",
              "其实 ... 也没有多喜欢钱啦，但是，也没出现更喜欢的东西呢",
              "指挥官，不要忙得太过火哦，必要时请花点钱省心吧",
              "除了这些、那些，和那边那些，基本都是进货价呢，并没有骗您哦",
              "想更了解我 ... 吗，人家要不要把私密权限也卖给您呢，可惜没有那种东西啦",
              "美好的一天呢，是不是该花点钱，让它更美好一点呢？",
              "诶？没钱了？真是没办法今天就特别给你打点折好了",
              "随便聊聊也是可以的哦，看在您是老主顾的份上，破例免费一次吧",
              "指挥官，要来点点心吗？",
              "东西快堆不下了 ... 指挥官，快拿走一些吧，成本价卖你了",
              "虽然有句名言“不要被金钱支配，要去支配金钱”，但我是不会支配您的，指挥官大人！",
              "稍稍做个游戏吧，您赢了，就打赏人家一点，输了的话，就买些东西，如何呢？",
              "指挥官！再多买一些就给你特别的惊喜哦！",
              "我为您破例打了那么多折扣，而我对您的爱慕之心，可从来没有打折过哦",
              "别忘了我们的特殊契约哦，金钱只是付出的一部分呢"]

ban_word = ["日", "操", "艹", "草", "舔", "RBQ", "rbq", "Rbq", "奸", "中出",
            "社保", "射", "啪", "嫖", "菊", "胸", "肛", "曰", "RI", "Ri",
            "ri", "肏", "腚", "后入", "里面", "尾交", "交尾", "干", "变性",
            "奶子", "插入", "马眼", "玩坏", "生意", "公交", "援交", "小电影",
            "床", "穴", "玩弄", "乳", "asshole", "黄瓜", "香肠"]

t_doll_name_list = [["1", "柯尔特左轮", "HG"],
                    ["2", "M1911", "HG"],
                    ["3", "M9", "HG"],
                    ["5", "纳甘左轮", "HG"],
                    ["6", "托卡列夫", "HG"],
                    ["7", "斯捷奇金", "HG"],
                    ["8", "马卡洛夫", "HG"],
                    ["9", "P38", "HG"],
                    ["10", "PPK", "HG"],
                    ["11", "P08", "HG"],
                    ["12", "C96", "HG"],
                    ["13", "92式", "HG"],
                    ["14", "阿斯特拉左轮", "HG"],
                    ["15", "格洛克17", "HG"],
                    ["16", "汤姆森", "SMG"],
                    ["17", "M3", "SMG"],
                    ["18", "MAC-10", "SMG"],
                    ["19", "FMG-9", "SMG"],
                    ["20", "Vector", "SMG"],
                    ["21", "PPSh-41", "SMG"],
                    ["22", "PPS-43", "SMG"],
                    ["23", "PP-90", "SMG"],
                    ["24", "PP-2000", "SMG"],
                    ["25", "MP40", "SMG"],
                    ["26", "MP5", "SMG"],
                    ["27", "蝎式", "SMG"],
                    ["28", "MP7", "SMG"],
                    ["29", "司登MkⅡ", "SMG"],
                    ["31", "伯莱塔38型", "SMG"],
                    ["32", "微型乌兹", "SMG"],
                    ["33", "m45", "SMG"],
                    ["34", "M1加兰德", "RF"],
                    ["35", "M1A1", "RF"],
                    ["36", "春田", "RF"],
                    ["37", "M14", "RF"],
                    ["38", "M21", "RF"],
                    ["39", "莫辛-纳甘", "RF"],
                    ["40", "SVT-38", "RF"],
                    ["41", "西蒙诺夫", "RF"],
                    ["42", "PTRD", "RF"],
                    ["43", "SVD", "RF"],
                    ["44", "SV-98", "RF"],
                    ["46", "Kar98k", "RF"],
                    ["47", "G43", "RF"],
                    ["48", "WA2000", "RF"],
                    ["49", "56式半", "RF"],
                    ["50", "李-恩菲尔德", "RF"],
                    ["51", "FN-49", "RF"],
                    ["52", "BM59", "RF"],
                    ["53", "NTW-20", "RF"],
                    ["54", "M16A1", "AR"],
                    ["55", "M4A1", "AR"],
                    ["56", "M4 SOPMODII", "AR"],
                    ["57", "ST AR-15", "AR"],
                    ["58", "AK-47", "AR"],
                    ["60", "AS Val", "AR"],
                    ["61", "StG44", "AR"],
                    ["62", "G41", "AR"],
                    ["63", "G3", "AR"],
                    ["64", "G36", "AR"],
                    ["65", "HK416", "AR"],
                    ["66", "56-1式", "AR"],
                    ["68", "L85A1", "AR"],
                    ["69", "FAMAS", "AR"],
                    ["70", "FNC", "AR"],
                    ["71", "加利尔", "AR"],
                    ["72", "TAR-21", "AR"],
                    ["74", "SIG-510", "AR"],
                    ["75", "M1918", "MG"],
                    ["77", "M2HB ", "MG"],
                    ["78", "M60", "MG"],
                    ["79", "M249 SAW", "MG"],
                    ["80", "M1919A4", "MG"],
                    ["81", "LWMMG", "MG"],
                    ["82", "DP28", "MG"],
                    ["84", "RPD", "MG"],
                    ["85", "PK", "MG"],
                    ["86", "MG42", "MG"],
                    ["87", "MG34", "MG"],
                    ["88", "MG3", "MG"],
                    ["89", "布伦", "MG"],
                    ["90", "FNP-9", "HG"],
                    ["91", "MP-446", "HG"],
                    ["92", "Spectre M4", "SMG"],
                    ["93", "IDW", "SMG"],
                    ["94", "64式", "SMG"],
                    ["95", "汉阳造88式", "RF"],
                    ["96", "灰熊MkⅤ", "HG"],
                    ["97", "M950A", "HG"],
                    ["98", "SPP-1", "HG"],
                    ["99", "Mk23", "HG"],
                    ["100", "P7", "HG"],
                    ["101", "UMP9", "SMG"],
                    ["102", "UMP40", "SMG"],
                    ["103", "UMP45", "SMG"],
                    ["104", "G36C", "SMG"],
                    ["105", "OTs-12", "AR"],
                    ["106", "FAL", "AR"],
                    ["107", "F2000", "AR"],
                    ["108", "CZ-805", "AR"],
                    ["109", "MG5", "MG"],
                    ["110", "FG42", "MG"],
                    ["111", "AAT-52", "MG"],
                    ["112", "内格夫", "MG"],
                    ["113", "谢尔久科夫", "HG"],
                    ["114", "维尔德MkⅡ", "HG"],
                    ["115", "索米", "SMG"],
                    ["116", "Z-62", "SMG"],
                    ["117", "PSG-1", "RF"],
                    ["118", "9A-91", "AR"],
                    ["119", "OTs-14", "AR"],
                    ["120", "ARX-160", "AR"],
                    ["121", "Mk48", "MG"],
                    ["122", "G11", "AR"],
                    ["123", "P99", "HG"],
                    ["124", "Super SASS", "RF"],
                    ["125", "MG4", "MG"],
                    ["126", "NZ75", "HG"],
                    ["127", "79式", "SMG"],
                    ["128", "M99", "RF"],
                    ["129", "95式", "AR"],
                    ["130", "97式", "AR"],
                    ["131", "EVO 3", "SMG"],
                    ["132", "59式", "HG"],
                    ["133", "63式", "AR"],
                    ["134", "AR70", "AR"],
                    ["135", "SR-3MP", "SMG"],
                    ["136", "PP-19", "SMG"],
                    ["137", "PP-19-01", "SMG"],
                    ["138", "6P62", "AR"],
                    ["139", "Bren Ten", "HG"],
                    ["140", "PSM", "HG"],
                    ["141", "USP Compact", "HG"],
                    ["142", "Five-seveN", "HG"],
                    ["143", "RO635", "SMG"],
                    ["144", "MT-9", "SMG"],
                    ["145", "OTs-44", "RF"],
                    ["146", "G28", "RF"],
                    ["147", "SSG 69", "RF"],
                    ["148", "IWS 2000", "RF"],
                    ["149", "AEK-999", "MG"],
                    ["150", "希普卡", "SMG"],
                    ["151", "M1887", "SG"],
                    ["152", "M1897", "SG"],
                    ["153", "M37", "SG"],
                    ["154", "M500", "SG"],
                    ["155", "M590", "SG"],
                    ["156", "Super-Shorty", "SG"],
                    ["157", "KSG", "SG"],
                    ["158", "KS-23", "SG"],
                    ["159", "RMB-93", "SG"],
                    ["160", "Saiga-12", "SG"],
                    ["161", "97式霰", "SG"],
                    ["162", "SPAS-12", "SG"],
                    ["166", "CZ75", "HG"],
                    ["167", "HK45", "HG"],
                    ["168", "Spitfire", "HG"],
                    ["169", "SCW", "SMG"],
                    ["170", "ASh-12.7", "AR"],
                    ["171", "利贝罗勒", "AR"],
                    ["172", "RFB", "AR"],
                    ["173", "PKP", "MG"],
                    ["174", "八一式马", "RF"],
                    ["175", "ART556", "AR"],
                    ["176", "TMP", "SMG"],
                    ["177", "KLIN", "SMG"],
                    ["178", "F1", "SMG"],
                    ["179", "DSR-50", "RF"],
                    ["180", "PzB39", "RF"],
                    ["181", "T91", "AR"],
                    ["182", "wz.29", "RF"],
                    ["183", "竞争者", "HG"],
                    ["184", "T-5000", "RF"],
                    ["185", "阿梅利", "MG"],
                    ["186", "P226", "HG"],
                    ["187", "Ak 5", "AR"],
                    ["188", "S.A.T.8", "SG"],
                    ["189", "USAS-12", "SG"],
                    ["190", "NS2000", "SG"],
                    ["191", "M12", "SMG"],
                    ["192", "JS05", "RF"],
                    ["193", "T65", "AR"],
                    ["194", "K2", "AR"],
                    ["195", "HK23", "MG"],
                    ["196", "Zas M21", "AR"],
                    ["197", "卡尔卡诺M1891", "RF"],
                    ["198", "卡尔卡诺M91/38", "RF"],
                    ["199", "80式", "MG"],
                    ["200", "XM3", "RF"],
                    ["201", "猎豹M1", "RF"],
                    ["202", "雷电", "HG"],
                    ["203", "蜜獾", "SMG"],
                    ["204", "芭莉斯塔", "RF"],
                    ["205", "AN-94", "AR"],
                    ["206", "AK-12", "AR"],
                    ["207", "CZ2000", "AR"],
                    ["208", "HK21", "MG"],
                    ["209", "OTs-39", "SMG"],
                    ["210", "CZ52", "HG"],
                    ["211", "SRS", "RF"],
                    ["212", "K5", "HG"],
                    ["213", "C-MS", "SMG"],
                    ["215", "MDR", "AR"],
                    ["216", "XM8", "AR"],
                    ["217", "SM-1", "RF"],
                    ["1001", "诺爱尔", "HG"],
                    ["1002", "艾尔菲尔特", "SG"],
                    ["1003", "琪亚娜", "HG"],
                    ["1004", "雷电芽衣", "RF"],
                    ["1005", "布洛妮娅", "RF"],
                    ["1006", "德丽莎", "HG"],
                    ["1007", "无量塔姬子", "AR"],
                    ["1008", "希儿", "SG"],
                    ["1009", "克莉尔", "HG"],
                    ["1010", "菲尔", "HG"]]
