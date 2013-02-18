#!/usr/bin/env python3
# --coding:utf-8
#
# @brief  为CRF++分词服务。输入样例和对应的输出样例见下面。
#         使用SBME标注。
#           S: 单字词
#           B：词的开始
#           M: 词的中间
#           E: 词的结尾
#
# 输入样例：
#       迈向
#       充满
#       希望
#       的
#       新世纪
#
# 对应的输出样例:
#       迈 B
#       向 E
#       
#       充 B
#       慢 E
#       
#       希 B
#       望 E
#
#       的 S
#       
#       新 B
#       世 M
#       纪 E
#
# @author Huanxing Yang
# @date   2013-02-18
#

import fileinput

crlf = "\n"

for line in fileinput.input():
    if (line.startswith("#")):
        continue
    word = line.strip()
    output = ""
    if len(word) == 0:
        continue
    elif len(word) == 1:
        output = word + " S"
    else:
        output = word[0] + " B"
        output += crlf
        for i in range(len(word) - 2):
            output += word[1 + i] + " M"
            output += crlf
        output += word[-1] + " E"
    print(output)
    print("")
