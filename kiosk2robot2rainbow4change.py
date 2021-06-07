from http.server import HTTPServer, BaseHTTPRequestHandler #http.server 모듈 사용
import json #json 모듈 불러오기
import ast
import socket # socket 모듈을 불러
import threading
import time
import pickle
from tkinter import * #tkinter 모듈 가져오기
import tkinter.font
from time import sleep

g=0
h=0
r=0


class Handler(BaseHTTPRequestHandler): #http.server 핸들러를 class로 지정


    def do_POST(self):


        length = int(self.headers.get('content-length')) #headers.get함수로 데이터 받기
        field_data = self.rfile.read(length) #read합수로 데이터 읽기
        v = field_data.decode('utf-8')
        t = ast.literal_eval(v)
        u = t['LISTS'][0]['LIST_H'][0]['BILL_NO']
        w = int(u)


        if w >= 1002:


            def qwe():
                global g
                g = g + 1

            qwe()

            if g%2:
                with open('./tmp/order_kiosk.json', 'w') as f: #C 드라이브에 order_kiosk.json 저장하기
                    json.dump(t, f)

                with open('./tmp/order_kiosk.json', 'r', encoding='UTF8') as f: #C 드라이브에 order_kiosk.json 불러오기
                    i = json.load(f)

                print(i)

                y = i['LISTS'][1]['LIST_D']

                if len(y) == 6:

                    da = i["date"] #주문날짜와 시간

                    CALL= i['LISTS'][0]['LIST_H'][0]['CALL_NO'] #주문번호

                    ITEM_1 = i['LISTS'][1]['LIST_D'][0]['ITEM_CD']  # 품목
                    ITEM_2 = i['LISTS'][1]['LIST_D'][1]['ITEM_CD']
                    ITEM_3 = i['LISTS'][1]['LIST_D'][2]['ITEM_CD']
                    ITEM_4 = i['LISTS'][1]['LIST_D'][3]['ITEM_CD']
                    ITEM_5 = i['LISTS'][1]['LIST_D'][4]['ITEM_CD']
                    ITEM_6 = i['LISTS'][1]['LIST_D'][5]['ITEM_CD']

                    QTY_1 = i['LISTS'][1]['LIST_D'][0]['QTY']  # 수량
                    QTY_2 = i['LISTS'][1]['LIST_D'][1]['QTY']
                    QTY_3 = i['LISTS'][1]['LIST_D'][2]['QTY']
                    QTY_4 = i['LISTS'][1]['LIST_D'][3]['QTY']
                    QTY_5 = i['LISTS'][1]['LIST_D'][4]['QTY']
                    QTY_6 = i['LISTS'][1]['LIST_D'][5]['QTY']

                    SEQ_1 = i['LISTS'][1]['LIST_D'][0]['SEQ']  # 품목순서
                    SEQ_2 = i['LISTS'][1]['LIST_D'][1]['SEQ']
                    SEQ_3 = i['LISTS'][1]['LIST_D'][2]['SEQ']
                    SEQ_4 = i['LISTS'][1]['LIST_D'][3]['SEQ']
                    SEQ_5 = i['LISTS'][1]['LIST_D'][4]['SEQ']
                    SEQ_6 = i['LISTS'][1]['LIST_D'][5]['SEQ']

                    print(CALL)
                    print(ITEM_1, ITEM_2, ITEM_3, ITEM_4, ITEM_5, ITEM_6)
                    print(QTY_1, QTY_2, QTY_3, QTY_4, QTY_5, QTY_6)
                    print(SEQ_1, SEQ_2, SEQ_3, SEQ_4, SEQ_5, SEQ_6)

                    k = {
                        CALL:
                            [
                                {
                                    SEQ_1:
                                        {
                                            "ITEM_CD": ITEM_1,
                                            "QTY": QTY_1

                                        }
                                },
                                {
                                    SEQ_2:
                                        {
                                            "ITEM_CD": ITEM_2,
                                            "QTY": QTY_2

                                        }
                                },
                                {
                                    SEQ_3:
                                        {
                                            "ITEM_CD": ITEM_3,
                                            "QTY": QTY_3

                                        }
                                },
                                {
                                    SEQ_4:
                                        {
                                            "ITEM_CD": ITEM_4,
                                            "QTY": QTY_4

                                        }
                                },
                                {
                                    SEQ_5:
                                        {
                                            "ITEM_CD": ITEM_5,
                                            "QTY": QTY_5

                                        }
                                },
                                {
                                    SEQ_6:
                                        {
                                            "ITEM_CD": ITEM_6,
                                            "QTY": QTY_6

                                        }
                                }
                            ]
                    }

                    m = json.dumps(k)
                    # 다시 json 형식으로 만들기

                    j_1 = int(CALL)

                    d_1 = int(ITEM_1)
                    d_2 = int(ITEM_2)
                    d_3 = int(ITEM_3)
                    d_4 = int(ITEM_4)
                    d_5 = int(ITEM_5)
                    d_6 = int(ITEM_6)

                    e_1 = int(QTY_1)
                    e_2 = int(QTY_2)
                    e_3 = int(QTY_3)
                    e_4 = int(QTY_4)
                    e_5 = int(QTY_5)
                    e_6 = int(QTY_6)

                    print(m)

                    if d_1 < 2000:
                        def x_1(count):
                            if count == 0:
                                return
                            add(d_1)
                            count -= 1
                            x_1(count)

                        x_1(e_1)

                        def dis1(cou):
                            if cou == 0:
                                return
                            dist.append(j_1)
                            cou -= 1
                            dis1(cou)

                        dis1(e_1)

                    elif d_1 >= 2000:
                        pass

                    if d_2 < 2000:
                        def x_2(count):
                            if count == 0:
                                return
                            add(d_2)
                            count -= 1
                            x_2(count)

                        x_2(e_2)

                        def dis1(cou):
                            if cou == 0:
                                return
                            dist.append(j_1)
                            cou -= 1
                            dis1(cou)

                        dis1(e_2)

                    elif d_2 >= 2000:
                        pass

                    if d_3 < 2000:
                        def x_3(count):
                            if count == 0:
                                return
                            add(d_3)
                            count -= 1
                            x_3(count)

                        x_3(e_3)

                        def dis1(cou):
                            if cou == 0:
                                return
                            dist.append(j_1)
                            cou -= 1
                            dis1(cou)

                        dis1(e_3)

                    elif d_3 >= 2000:
                        pass

                    if d_4 < 2000:
                        def x_4(count):
                            if count == 0:
                                return
                            add(d_4)
                            count -= 1
                            x_4(count)

                        x_4(e_4)

                        def dis1(cou):
                            if cou == 0:
                                return
                            dist.append(j_1)
                            cou -= 1
                            dis1(cou)

                        dis1(e_4)

                    elif d_4 >= 2000:
                        pass

                    if d_5 < 2000:
                        def x_5(count):
                            if count == 0:
                                return
                            add(d_5)
                            count -= 1
                            x_5(count)

                        x_5(e_5)

                        def dis1(cou):
                            if cou == 0:
                                return
                            dist.append(j_1)
                            cou -= 1
                            dis1(cou)

                        dis1(e_5)

                    elif d_5 >= 2000:
                        pass

                    if d_6 < 2000:
                        def x_6(count):
                            if count == 0:
                                return
                            add(d_6)
                            count -= 1
                            x_6(count)

                        x_6(e_6)

                        def dis1(cou):
                            if cou == 0:
                                return
                            dist.append(j_1)
                            cou -= 1
                            dis1(cou)

                        dis1(e_6)

                    elif d_6 >= 2000:
                        pass

                    print_q()
                    print(dist)

                    def save():
                        f = open("./kiosk_order/kioskorder.txt", 'a')
                        data = "\n-----------------------------------\n주문번호:%d \n\n품목:%d 수량:%d" \
                               "\n품목:%d 수량:%d\n품목:%d 수량:%d\n품목:%d 수량:%d\n품목:%d 수량:%d" \
                               "\n품목:%d 수량:%d\n\n주문시간:%s" % (
                            j_1, d_1, e_1, d_2, e_2, d_3, e_3, d_4, e_4, d_5, e_5, d_6, e_6, da)
                        f.write(data)
                        f.close()

                    save()
                    # C 드라이브 kioskorder.txt파일에 주문 데이터를 계속 저장

                    di2 = d_1 + d_2 + d_3 + d_4 + d_5 + d_6
                    if di2 > 7000:
                        dist2.append(j_1)
                        print(dist2)
                    elif di2 <= 7000:
                        pass






                elif len(y) == 5:

                    da = i["date"]

                    CALL = i['LISTS'][0]['LIST_H'][0]['CALL_NO']

                    ITEM_1 = i['LISTS'][1]['LIST_D'][0]['ITEM_CD']  # d
                    ITEM_2 = i['LISTS'][1]['LIST_D'][1]['ITEM_CD']
                    ITEM_3 = i['LISTS'][1]['LIST_D'][2]['ITEM_CD']
                    ITEM_4 = i['LISTS'][1]['LIST_D'][3]['ITEM_CD']
                    ITEM_5 = i['LISTS'][1]['LIST_D'][4]['ITEM_CD']

                    QTY_1 = i['LISTS'][1]['LIST_D'][0]['QTY']  # e
                    QTY_2 = i['LISTS'][1]['LIST_D'][1]['QTY']
                    QTY_3 = i['LISTS'][1]['LIST_D'][2]['QTY']
                    QTY_4 = i['LISTS'][1]['LIST_D'][3]['QTY']
                    QTY_5 = i['LISTS'][1]['LIST_D'][4]['QTY']

                    SEQ_1 = i['LISTS'][1]['LIST_D'][0]['SEQ']  # f
                    SEQ_2 = i['LISTS'][1]['LIST_D'][1]['SEQ']
                    SEQ_3 = i['LISTS'][1]['LIST_D'][2]['SEQ']
                    SEQ_4 = i['LISTS'][1]['LIST_D'][3]['SEQ']
                    SEQ_5 = i['LISTS'][1]['LIST_D'][4]['SEQ']

                    print(CALL)
                    print(ITEM_1, ITEM_2, ITEM_3, ITEM_4, ITEM_5)
                    print(QTY_1, QTY_2, QTY_3, QTY_4, QTY_5)
                    print(SEQ_1, SEQ_2, SEQ_3, SEQ_4, SEQ_5)

                    k = {
                        CALL:
                            [
                                {
                                    SEQ_1:
                                        {
                                            "ITEM_CD": ITEM_1,
                                            "QTY": QTY_1

                                        }
                                },
                                {
                                    SEQ_2:
                                        {
                                            "ITEM_CD": ITEM_2,
                                            "QTY": QTY_2

                                        }
                                },
                                {
                                    SEQ_3:
                                        {
                                            "ITEM_CD": ITEM_3,
                                            "QTY": QTY_3

                                        }
                                },
                                {
                                    SEQ_4:
                                        {
                                            "ITEM_CD": ITEM_4,
                                            "QTY": QTY_4

                                        }
                                },
                                {
                                    SEQ_5:
                                        {
                                            "ITEM_CD": ITEM_5,
                                            "QTY": QTY_5

                                        }
                                }

                            ]
                    }

                    m = json.dumps(k)

                    j_1 = int(CALL)

                    d_1 = int(ITEM_1)
                    d_2 = int(ITEM_2)
                    d_3 = int(ITEM_3)
                    d_4 = int(ITEM_4)
                    d_5 = int(ITEM_5)

                    e_1 = int(QTY_1)
                    e_2 = int(QTY_2)
                    e_3 = int(QTY_3)
                    e_4 = int(QTY_4)
                    e_5 = int(QTY_5)

                    print(m)

                    if d_1 < 2000:
                        def x_1(count):
                            if count == 0:
                                return
                            add(d_1)
                            count -= 1
                            x_1(count)

                        x_1(e_1)

                        def dis1(cou):
                            if cou == 0:
                                return
                            dist.append(j_1)
                            cou -= 1
                            dis1(cou)

                        dis1(e_1)

                    elif d_1 >= 2000:
                        pass

                    if d_2 < 2000:
                        def x_2(count):
                            if count == 0:
                                return
                            add(d_2)
                            count -= 1
                            x_2(count)

                        x_2(e_2)

                        def dis1(cou):
                            if cou == 0:
                                return
                            dist.append(j_1)
                            cou -= 1
                            dis1(cou)

                        dis1(e_2)

                    elif d_2 >= 2000:
                        pass

                    if d_3 < 2000:
                        def x_3(count):
                            if count == 0:
                                return
                            add(d_3)
                            count -= 1
                            x_3(count)

                        x_3(e_3)

                        def dis1(cou):
                            if cou == 0:
                                return
                            dist.append(j_1)
                            cou -= 1
                            dis1(cou)

                        dis1(e_3)

                    elif d_3 >= 2000:
                        pass

                    if d_4 < 2000:
                        def x_4(count):
                            if count == 0:
                                return
                            add(d_4)
                            count -= 1
                            x_4(count)

                        x_4(e_4)

                        def dis1(cou):
                            if cou == 0:
                                return
                            dist.append(j_1)
                            cou -= 1
                            dis1(cou)

                        dis1(e_4)

                    elif d_4 >= 2000:
                        pass

                    if d_5 < 2000:
                        def x_5(count):
                            if count == 0:
                                return
                            add(d_5)
                            count -= 1
                            x_5(count)

                        x_5(e_5)

                        def dis1(cou):
                            if cou == 0:
                                return
                            dist.append(j_1)
                            cou -= 1
                            dis1(cou)

                        dis1(e_5)

                    elif d_5 >= 2000:
                        pass

                    print_q()
                    print(dist)

                    def save():
                        f = open("./kiosk_order/kioskorder.txt", 'a')
                        data = "\n-----------------------------------\n\n주문번호:%d \n품목:%d 수량:%d\n품목:%d 수량:%d\n품목:%d 수량:%d\n품목:%d 수량:%d\n품목:%d 수량:%d\n\n주문시간:%s" % (
                            j_1, d_1, e_1, d_2, e_2, d_3, e_3, d_4, e_4, d_5, e_5, da)
                        f.write(data)
                        f.close()

                    save()

                    di2 = d_1 + d_2 + d_3 + d_4 + d_5
                    if di2 > 6000:
                        dist2.append(j_1)
                        print(dist2)
                    elif di2 <= 6000:
                        pass



                elif len(y) == 4:

                    da = i["date"]

                    CALL = i['LISTS'][0]['LIST_H'][0]['CALL_NO']

                    ITEM_1 = i['LISTS'][1]['LIST_D'][0]['ITEM_CD']  # d
                    ITEM_2 = i['LISTS'][1]['LIST_D'][1]['ITEM_CD']
                    ITEM_3 = i['LISTS'][1]['LIST_D'][2]['ITEM_CD']
                    ITEM_4 = i['LISTS'][1]['LIST_D'][3]['ITEM_CD']

                    QTY_1 = i['LISTS'][1]['LIST_D'][0]['QTY']  # e
                    QTY_2 = i['LISTS'][1]['LIST_D'][1]['QTY']
                    QTY_3 = i['LISTS'][1]['LIST_D'][2]['QTY']
                    QTY_4 = i['LISTS'][1]['LIST_D'][3]['QTY']

                    SEQ_1 = i['LISTS'][1]['LIST_D'][0]['SEQ']  # f
                    SEQ_2 = i['LISTS'][1]['LIST_D'][1]['SEQ']
                    SEQ_3 = i['LISTS'][1]['LIST_D'][2]['SEQ']
                    SEQ_4 = i['LISTS'][1]['LIST_D'][3]['SEQ']

                    print(CALL)
                    print(ITEM_1, ITEM_2, ITEM_3, ITEM_4)
                    print(QTY_1, QTY_2, QTY_3, QTY_4)
                    print(SEQ_1, SEQ_2, SEQ_3, SEQ_4)

                    k = {
                        CALL:
                            [
                                {
                                    SEQ_1:
                                        {
                                            "ITEM_CD": ITEM_1,
                                            "QTY": QTY_1

                                        }
                                },
                                {
                                    SEQ_2:
                                        {
                                            "ITEM_CD": ITEM_2,
                                            "QTY": QTY_2

                                        }
                                },
                                {
                                    SEQ_3:
                                        {
                                            "ITEM_CD": ITEM_3,
                                            "QTY": QTY_3

                                        }
                                },
                                {
                                    SEQ_4:
                                        {
                                            "ITEM_CD": ITEM_4,
                                            "QTY": QTY_4

                                        }
                                }

                            ]
                    }

                    m = json.dumps(k)

                    j_1 = int(CALL)

                    d_1 = int(ITEM_1)
                    d_2 = int(ITEM_2)
                    d_3 = int(ITEM_3)
                    d_4 = int(ITEM_4)

                    e_1 = int(QTY_1)
                    e_2 = int(QTY_2)
                    e_3 = int(QTY_3)
                    e_4 = int(QTY_4)

                    print(m)

                    if d_1 < 2000:
                        def x_1(count):
                            if count == 0:
                                return
                            add(d_1)
                            count -= 1
                            x_1(count)

                        x_1(e_1)

                        def dis1(cou):
                            if cou == 0:
                                return
                            dist.append(j_1)
                            cou -= 1
                            dis1(cou)

                        dis1(e_1)

                    elif d_1 >= 2000:
                        pass

                    if d_2 < 2000:
                        def x_2(count):
                            if count == 0:
                                return
                            add(d_2)
                            count -= 1
                            x_2(count)

                        x_2(e_2)

                        def dis1(cou):
                            if cou == 0:
                                return
                            dist.append(j_1)
                            cou -= 1
                            dis1(cou)

                        dis1(e_2)

                    elif d_2 >= 2000:
                        pass

                    if d_3 < 2000:
                        def x_3(count):
                            if count == 0:
                                return
                            add(d_3)
                            count -= 1
                            x_3(count)

                        x_3(e_3)

                        def dis1(cou):
                            if cou == 0:
                                return
                            dist.append(j_1)
                            cou -= 1
                            dis1(cou)

                        dis1(e_3)

                    elif d_3 >= 2000:
                        pass

                    if d_4 < 2000:
                        def x_4(count):
                            if count == 0:
                                return
                            add(d_4)
                            count -= 1
                            x_4(count)

                        x_4(e_4)

                        def dis1(cou):
                            if cou == 0:
                                return
                            dist.append(j_1)
                            cou -= 1
                            dis1(cou)

                        dis1(e_4)

                    elif d_4 >= 2000:
                        pass

                    print_q()
                    print(dist)

                    def save():
                        f = open("./kiosk_order/kioskorder.txt", 'a')
                        data = "\n-----------------------------------\n\n주문번호:%d \n품목:%d 수량:%d\n품목:%d 수량:%d\n품목:%d 수량:%d\n품목:%d 수량:%d\n\n주문시간:%s" % (
                            j_1, d_1, e_1, d_2, e_2, d_3, e_3, d_4, e_4, da)
                        f.write(data)
                        f.close()

                    save()

                    di2 = d_1 + d_2 + d_3 + d_4
                    if di2 > 5000:
                        dist2.append(j_1)
                        print(dist2)
                    elif di2 <= 5000:
                        pass


                elif len(y) == 3:

                    da = i["date"]

                    CALL = i['LISTS'][0]['LIST_H'][0]['CALL_NO']

                    ITEM_1 = i['LISTS'][1]['LIST_D'][0]['ITEM_CD']  # d
                    ITEM_2 = i['LISTS'][1]['LIST_D'][1]['ITEM_CD']
                    ITEM_3 = i['LISTS'][1]['LIST_D'][2]['ITEM_CD']

                    QTY_1 = i['LISTS'][1]['LIST_D'][0]['QTY']  # e
                    QTY_2 = i['LISTS'][1]['LIST_D'][1]['QTY']
                    QTY_3 = i['LISTS'][1]['LIST_D'][2]['QTY']

                    SEQ_1 = i['LISTS'][1]['LIST_D'][0]['SEQ']  # f
                    SEQ_2 = i['LISTS'][1]['LIST_D'][1]['SEQ']
                    SEQ_3 = i['LISTS'][1]['LIST_D'][2]['SEQ']

                    print(CALL)
                    print(ITEM_1, ITEM_2, ITEM_3)
                    print(QTY_1, QTY_2, QTY_3)
                    print(SEQ_1, SEQ_2, SEQ_3)

                    k = {
                        CALL:
                            [
                                {
                                    SEQ_1:
                                        {
                                            "ITEM_CD": ITEM_1,
                                            "QTY": QTY_1

                                        }
                                },
                                {
                                    SEQ_2:
                                        {
                                            "ITEM_CD": ITEM_2,
                                            "QTY": QTY_2

                                        }
                                },
                                {
                                    SEQ_3:
                                        {
                                            "ITEM_CD": ITEM_3,
                                            "QTY": QTY_3

                                        }
                                }

                            ]
                    }

                    m = json.dumps(k)

                    j_1 = int(CALL)

                    d_1 = int(ITEM_1)
                    d_2 = int(ITEM_2)
                    d_3 = int(ITEM_3)

                    e_1 = int(QTY_1)
                    e_2 = int(QTY_2)
                    e_3 = int(QTY_3)

                    print(m)

                    if d_1 < 2000:
                        def x_1(count):
                            if count == 0:
                                return
                            add(d_1)
                            count -= 1
                            x_1(count)

                        x_1(e_1)

                        def dis1(cou):
                            if cou == 0:
                                return
                            dist.append(j_1)
                            cou -= 1
                            dis1(cou)

                        dis1(e_1)
                    elif d_1 >= 2000:
                        pass

                    if d_2 < 2000:
                        def x_2(count):
                            if count == 0:
                                return
                            add(d_2)
                            count -= 1
                            x_2(count)

                        x_2(e_2)

                        def dis1(cou):
                            if cou == 0:
                                return
                            dist.append(j_1)
                            cou -= 1
                            dis1(cou)

                        dis1(e_2)

                    elif d_2 >= 2000:
                        pass

                    if d_3 < 2000:
                        def x_3(count):
                            if count == 0:
                                return
                            add(d_3)
                            count -= 1
                            x_3(count)

                        x_3(e_3)

                        def dis1(cou):
                            if cou == 0:
                                return
                            dist.append(j_1)
                            cou -= 1
                            dis1(cou)

                        dis1(e_3)

                    elif d_3 >= 2000:
                        pass

                    print_q()
                    print(dist)

                    def save():
                        f = open("./kiosk_order/kioskorder.txt", 'a')
                        data = "\n-----------------------------------\n\n주문번호:%d \n품목:%d 수량:%d\n품목:%d 수량:%d\n품목:%d 수량:%d\n\n주문시간:%s" % (
                            j_1, d_1, e_1, d_2, e_2, d_3, e_3, da)
                        f.write(data)
                        f.close()

                    save()

                    di2 = d_1 + d_2 + d_3
                    if di2 > 4000:
                        dist2.append(j_1)
                        print(dist2)
                    elif di2 <= 4000:
                        pass





                elif len(y) == 2:

                    da = i["date"]

                    CALL = i['LISTS'][0]['LIST_H'][0]['CALL_NO']

                    ITEM_1 = i['LISTS'][1]['LIST_D'][0]['ITEM_CD']  # d
                    ITEM_2 = i['LISTS'][1]['LIST_D'][1]['ITEM_CD']

                    QTY_1 = i['LISTS'][1]['LIST_D'][0]['QTY']  # e
                    QTY_2 = i['LISTS'][1]['LIST_D'][1]['QTY']

                    SEQ_1 = i['LISTS'][1]['LIST_D'][0]['SEQ']  # f
                    SEQ_2 = i['LISTS'][1]['LIST_D'][1]['SEQ']

                    print(CALL)
                    print(ITEM_1, ITEM_2)
                    print(QTY_1, QTY_2)
                    print(SEQ_1, SEQ_2)

                    k = {
                        CALL:
                            [
                                {
                                    SEQ_1:
                                        {
                                            "ITEM_CD": ITEM_1,
                                            "QTY": QTY_1

                                        }
                                },
                                {
                                    SEQ_2:
                                        {
                                            "ITEM_CD": ITEM_2,
                                            "QTY": QTY_2

                                        }
                                }

                            ]
                    }

                    m = json.dumps(k)

                    j_1 = int(CALL)

                    d_1 = int(ITEM_1)
                    d_2 = int(ITEM_2)

                    e_1 = int(QTY_1)
                    e_2 = int(QTY_2)

                    print(m)

                    if d_1 < 2000:
                        def x_1(count):
                            if count == 0:
                                return
                            add(d_1)
                            count -= 1
                            x_1(count)

                        x_1(e_1)

                        def dis1(cou):
                            if cou == 0:
                                return
                            dist.append(j_1)
                            cou -= 1
                            dis1(cou)

                        dis1(e_1)

                    elif d_1 >= 2000:
                        pass

                    if d_2 < 2000:
                        def x_2(count):
                            if count == 0:
                                return
                            add(d_2)
                            count -= 1
                            x_2(count)

                        x_2(e_2)

                        def dis1(cou):
                            if cou == 0:
                                return
                            dist.append(j_1)
                            cou -= 1
                            dis1(cou)

                        dis1(e_2)

                    elif d_2 >= 2000:
                        pass

                    print_q()
                    print(dist)

                    def save():
                        f = open("./kiosk_order/kioskorder.txt", 'a')
                        data = "\n-----------------------------------\n\n주문번호:%d \n품목:%d 수량:%d\n품목:%d 수량:%d\n\n주문시간:%s" % (
                        j_1, d_1, e_1, d_2, e_2, da)
                        f.write(data)
                        f.close()

                    save()

                    di2 = d_1 + d_2
                    if di2 > 3000:
                        dist2.append(j_1)
                        print(dist2)
                    elif di2 <= 3000:
                        pass





                elif len(y) == 1:

                    da = i["date"]

                    CALL = i['LISTS'][0]['LIST_H'][0]['CALL_NO']

                    ITEM_1 = i['LISTS'][1]['LIST_D'][0]['ITEM_CD']  # d

                    QTY_1 = i['LISTS'][1]['LIST_D'][0]['QTY']  # e

                    SEQ_1 = i['LISTS'][1]['LIST_D'][0]['SEQ']  # f

                    print(CALL)
                    print(ITEM_1)
                    print(QTY_1)
                    print(SEQ_1)

                    k = {
                        CALL:
                            [
                                {
                                    SEQ_1:
                                        {
                                            "ITEM_CD": ITEM_1,
                                            "QTY": QTY_1

                                        }
                                }

                            ]
                    }

                    m = json.dumps(k)

                    j_1 = int(CALL)

                    d_1 = int(ITEM_1)

                    e_1 = int(QTY_1)

                    print(m)

                    if d_1 < 2000:
                        def x_1(count):
                            if count == 0:
                                return
                            add(d_1)
                            count -= 1
                            x_1(count)

                        x_1(e_1)

                        def dis1(cou):
                            if cou == 0:
                                return
                            dist.append(j_1)
                            cou -= 1
                            dis1(cou)

                        dis1(e_1)


                    elif d_1 >= 2000:
                        pass

                    print_q()
                    print(dist)

                    def save():
                        f = open("./kiosk_order/kioskorder.txt", 'a')
                        data = "\n-----------------------------------\n\n주문번호:%d \n품목:%d 수량:%d\n\n주문시간:%s" % (
                        j_1, d_1, e_1, da)
                        f.write(data)
                        f.close()

                    save()

                    di2 = d_1
                    if di2 > 2000:
                        dist2.append(j_1)
                        print(dist2)
                    elif di2 <= 2000:
                        pass




        elif w==1001:

            def wer():
                global h
                h = h + 1

            wer()

            if h==1:
                def ert():
                    global r
                    r = r + 1

                ert()
                print(r)
                if r%2:
                    with open('./tmp/order_kiosk.json', 'w') as f:
                        json.dump(t, f)

                    with open('./tmp/order_kiosk.json', 'r', encoding='UTF8') as f:
                        i = json.load(f)

                    print(i)
                    y = i['LISTS'][1]['LIST_D']

                    if len(y) == 6:

                        da = i["date"]

                        CALL = i['LISTS'][0]['LIST_H'][0]['CALL_NO']

                        ITEM_1 = i['LISTS'][1]['LIST_D'][0]['ITEM_CD']  # d
                        ITEM_2 = i['LISTS'][1]['LIST_D'][1]['ITEM_CD']
                        ITEM_3 = i['LISTS'][1]['LIST_D'][2]['ITEM_CD']
                        ITEM_4 = i['LISTS'][1]['LIST_D'][3]['ITEM_CD']
                        ITEM_5 = i['LISTS'][1]['LIST_D'][4]['ITEM_CD']
                        ITEM_6 = i['LISTS'][1]['LIST_D'][5]['ITEM_CD']

                        QTY_1 = i['LISTS'][1]['LIST_D'][0]['QTY']  # e
                        QTY_2 = i['LISTS'][1]['LIST_D'][1]['QTY']
                        QTY_3 = i['LISTS'][1]['LIST_D'][2]['QTY']
                        QTY_4 = i['LISTS'][1]['LIST_D'][3]['QTY']
                        QTY_5 = i['LISTS'][1]['LIST_D'][4]['QTY']
                        QTY_6 = i['LISTS'][1]['LIST_D'][5]['QTY']

                        SEQ_1 = i['LISTS'][1]['LIST_D'][0]['SEQ']  # f
                        SEQ_2 = i['LISTS'][1]['LIST_D'][1]['SEQ']
                        SEQ_3 = i['LISTS'][1]['LIST_D'][2]['SEQ']
                        SEQ_4 = i['LISTS'][1]['LIST_D'][3]['SEQ']
                        SEQ_5 = i['LISTS'][1]['LIST_D'][4]['SEQ']
                        SEQ_6 = i['LISTS'][1]['LIST_D'][5]['SEQ']

                        print(CALL)
                        print(ITEM_1, ITEM_2, ITEM_3, ITEM_4, ITEM_5, ITEM_6)
                        print(QTY_1, QTY_2, QTY_3, QTY_4, QTY_5, QTY_6)
                        print(SEQ_1, SEQ_2, SEQ_3, SEQ_4, SEQ_5, SEQ_6)

                        k = {
                            CALL:
                                [
                                    {
                                        SEQ_1:
                                            {
                                                "ITEM_CD": ITEM_1,
                                                "QTY": QTY_1

                                            }
                                    },
                                    {
                                        SEQ_2:
                                            {
                                                "ITEM_CD": ITEM_2,
                                                "QTY": QTY_2

                                            }
                                    },
                                    {
                                        SEQ_3:
                                            {
                                                "ITEM_CD": ITEM_3,
                                                "QTY": QTY_3

                                            }
                                    },
                                    {
                                        SEQ_4:
                                            {
                                                "ITEM_CD": ITEM_4,
                                                "QTY": QTY_4

                                            }
                                    },
                                    {
                                        SEQ_5:
                                            {
                                                "ITEM_CD": ITEM_5,
                                                "QTY": QTY_5

                                            }
                                    },
                                    {
                                        SEQ_6:
                                            {
                                                "ITEM_CD": ITEM_6,
                                                "QTY": QTY_6

                                            }
                                    }
                                ]
                        }

                        m = json.dumps(k)

                        j_1 = int(CALL)

                        d_1 = int(ITEM_1)
                        d_2 = int(ITEM_2)
                        d_3 = int(ITEM_3)
                        d_4 = int(ITEM_4)
                        d_5 = int(ITEM_5)
                        d_6 = int(ITEM_6)

                        e_1 = int(QTY_1)
                        e_2 = int(QTY_2)
                        e_3 = int(QTY_3)
                        e_4 = int(QTY_4)
                        e_5 = int(QTY_5)
                        e_6 = int(QTY_6)

                        print(m)

                        if d_1 < 2000:
                            def x_1(count):
                                if count == 0:
                                    return
                                add(d_1)
                                count -= 1
                                x_1(count)

                            x_1(e_1)

                            def dis1(cou):
                                if cou == 0:
                                    return
                                dist.append(j_1)
                                cou -= 1
                                dis1(cou)

                            dis1(e_1)

                        elif d_1 >= 2000:
                            pass

                        if d_2 < 2000:
                            def x_2(count):
                                if count == 0:
                                    return
                                add(d_2)
                                count -= 1
                                x_2(count)

                            x_2(e_2)

                            def dis1(cou):
                                if cou == 0:
                                    return
                                dist.append(j_1)
                                cou -= 1
                                dis1(cou)

                            dis1(e_2)

                        elif d_2 >= 2000:
                            pass

                        if d_3 < 2000:
                            def x_3(count):
                                if count == 0:
                                    return
                                add(d_3)
                                count -= 1
                                x_3(count)

                            x_3(e_3)

                            def dis1(cou):
                                if cou == 0:
                                    return
                                dist.append(j_1)
                                cou -= 1
                                dis1(cou)

                            dis1(e_3)

                        elif d_3 >= 2000:
                            pass

                        if d_4 < 2000:
                            def x_4(count):
                                if count == 0:
                                    return
                                add(d_4)
                                count -= 1
                                x_4(count)

                            x_4(e_4)

                            def dis1(cou):
                                if cou == 0:
                                    return
                                dist.append(j_1)
                                cou -= 1
                                dis1(cou)

                            dis1(e_4)

                        elif d_4 >= 2000:
                            pass

                        if d_5 < 2000:
                            def x_5(count):
                                if count == 0:
                                    return
                                add(d_5)
                                count -= 1
                                x_5(count)

                            x_5(e_5)

                            def dis1(cou):
                                if cou == 0:
                                    return
                                dist.append(j_1)
                                cou -= 1
                                dis1(cou)

                            dis1(e_5)

                        elif d_5 >= 2000:
                            pass

                        if d_6 < 2000:
                            def x_6(count):
                                if count == 0:
                                    return
                                add(d_6)
                                count -= 1
                                x_6(count)

                            x_6(e_6)

                            def dis1(cou):
                                if cou == 0:
                                    return
                                dist.append(j_1)
                                cou -= 1
                                dis1(cou)

                            dis1(e_6)

                        elif d_6 >= 2000:
                            pass

                        print_q()
                        print(dist)

                        def save():
                            f = open("./kiosk_order/kioskorder.txt", 'a')
                            data = "\n-----------------------------------\n주문번호:%d \n\n품목:%d 수량:%d\n품목:%d 수량:%d\n품목:%d 수량:%d\n품목:%d 수량:%d\n품목:%d 수량:%d\n품목:%d 수량:%d\n\n주문시간:%s" % (
                                j_1, d_1, e_1, d_2, e_2, d_3, e_3, d_4, e_4, d_5, e_5, d_6, e_6, da)
                            f.write(data)
                            f.close()

                        save()

                        di2 = d_1 + d_2 + d_3 + d_4 + d_5 + d_6
                        if di2 > 7000:
                            dist2.append(j_1)
                            print(dist2)
                        elif di2 <= 7000:
                            pass






                    elif len(y) == 5:

                        da = i["date"]

                        CALL = i['LISTS'][0]['LIST_H'][0]['CALL_NO']

                        ITEM_1 = i['LISTS'][1]['LIST_D'][0]['ITEM_CD']  # d
                        ITEM_2 = i['LISTS'][1]['LIST_D'][1]['ITEM_CD']
                        ITEM_3 = i['LISTS'][1]['LIST_D'][2]['ITEM_CD']
                        ITEM_4 = i['LISTS'][1]['LIST_D'][3]['ITEM_CD']
                        ITEM_5 = i['LISTS'][1]['LIST_D'][4]['ITEM_CD']

                        QTY_1 = i['LISTS'][1]['LIST_D'][0]['QTY']  # e
                        QTY_2 = i['LISTS'][1]['LIST_D'][1]['QTY']
                        QTY_3 = i['LISTS'][1]['LIST_D'][2]['QTY']
                        QTY_4 = i['LISTS'][1]['LIST_D'][3]['QTY']
                        QTY_5 = i['LISTS'][1]['LIST_D'][4]['QTY']

                        SEQ_1 = i['LISTS'][1]['LIST_D'][0]['SEQ']  # f
                        SEQ_2 = i['LISTS'][1]['LIST_D'][1]['SEQ']
                        SEQ_3 = i['LISTS'][1]['LIST_D'][2]['SEQ']
                        SEQ_4 = i['LISTS'][1]['LIST_D'][3]['SEQ']
                        SEQ_5 = i['LISTS'][1]['LIST_D'][4]['SEQ']

                        print(CALL)
                        print(ITEM_1, ITEM_2, ITEM_3, ITEM_4, ITEM_5)
                        print(QTY_1, QTY_2, QTY_3, QTY_4, QTY_5)
                        print(SEQ_1, SEQ_2, SEQ_3, SEQ_4, SEQ_5)

                        k = {
                            CALL:
                                [
                                    {
                                        SEQ_1:
                                            {
                                                "ITEM_CD": ITEM_1,
                                                "QTY": QTY_1

                                            }
                                    },
                                    {
                                        SEQ_2:
                                            {
                                                "ITEM_CD": ITEM_2,
                                                "QTY": QTY_2

                                            }
                                    },
                                    {
                                        SEQ_3:
                                            {
                                                "ITEM_CD": ITEM_3,
                                                "QTY": QTY_3

                                            }
                                    },
                                    {
                                        SEQ_4:
                                            {
                                                "ITEM_CD": ITEM_4,
                                                "QTY": QTY_4

                                            }
                                    },
                                    {
                                        SEQ_5:
                                            {
                                                "ITEM_CD": ITEM_5,
                                                "QTY": QTY_5

                                            }
                                    }

                                ]
                        }

                        m = json.dumps(k)

                        j_1 = int(CALL)

                        d_1 = int(ITEM_1)
                        d_2 = int(ITEM_2)
                        d_3 = int(ITEM_3)
                        d_4 = int(ITEM_4)
                        d_5 = int(ITEM_5)

                        e_1 = int(QTY_1)
                        e_2 = int(QTY_2)
                        e_3 = int(QTY_3)
                        e_4 = int(QTY_4)
                        e_5 = int(QTY_5)

                        print(m)

                        if d_1 < 2000:
                            def x_1(count):
                                if count == 0:
                                    return
                                add(d_1)
                                count -= 1
                                x_1(count)

                            x_1(e_1)

                            def dis1(cou):
                                if cou == 0:
                                    return
                                dist.append(j_1)
                                cou -= 1
                                dis1(cou)

                            dis1(e_1)

                        elif d_1 >= 2000:
                            pass

                        if d_2 < 2000:
                            def x_2(count):
                                if count == 0:
                                    return
                                add(d_2)
                                count -= 1
                                x_2(count)

                            x_2(e_2)

                            def dis1(cou):
                                if cou == 0:
                                    return
                                dist.append(j_1)
                                cou -= 1
                                dis1(cou)

                            dis1(e_2)

                        elif d_2 >= 2000:
                            pass

                        if d_3 < 2000:
                            def x_3(count):
                                if count == 0:
                                    return
                                add(d_3)
                                count -= 1
                                x_3(count)

                            x_3(e_3)

                            def dis1(cou):
                                if cou == 0:
                                    return
                                dist.append(j_1)
                                cou -= 1
                                dis1(cou)

                            dis1(e_3)

                        elif d_3 >= 2000:
                            pass

                        if d_4 < 2000:
                            def x_4(count):
                                if count == 0:
                                    return
                                add(d_4)
                                count -= 1
                                x_4(count)

                            x_4(e_4)

                            def dis1(cou):
                                if cou == 0:
                                    return
                                dist.append(j_1)
                                cou -= 1
                                dis1(cou)

                            dis1(e_4)

                        elif d_4 >= 2000:
                            pass

                        if d_5 < 2000:
                            def x_5(count):
                                if count == 0:
                                    return
                                add(d_5)
                                count -= 1
                                x_5(count)

                            x_5(e_5)

                            def dis1(cou):
                                if cou == 0:
                                    return
                                dist.append(j_1)
                                cou -= 1
                                dis1(cou)

                            dis1(e_5)

                        elif d_5 >= 2000:
                            pass

                        print_q()
                        print(dist)

                        def save():
                            f = open("./kiosk_order/kioskorder.txt", 'a')
                            data = "\n-----------------------------------\n\n주문번호:%d \n품목:%d 수량:%d\n품목:%d 수량:%d\n품목:%d 수량:%d\n품목:%d 수량:%d\n품목:%d 수량:%d\n\n주문시간:%s" % (
                                j_1, d_1, e_1, d_2, e_2, d_3, e_3, d_4, e_4, d_5, e_5, da)
                            f.write(data)
                            f.close()

                        save()

                        di2 = d_1 + d_2 + d_3 + d_4 + d_5
                        if di2 > 6000:
                            dist2.append(j_1)
                            print(dist2)
                        elif di2 <= 6000:
                            pass



                    elif len(y) == 4:

                        da = i["date"]

                        CALL = i['LISTS'][0]['LIST_H'][0]['CALL_NO']

                        ITEM_1 = i['LISTS'][1]['LIST_D'][0]['ITEM_CD']  # d
                        ITEM_2 = i['LISTS'][1]['LIST_D'][1]['ITEM_CD']
                        ITEM_3 = i['LISTS'][1]['LIST_D'][2]['ITEM_CD']
                        ITEM_4 = i['LISTS'][1]['LIST_D'][3]['ITEM_CD']

                        QTY_1 = i['LISTS'][1]['LIST_D'][0]['QTY']  # e
                        QTY_2 = i['LISTS'][1]['LIST_D'][1]['QTY']
                        QTY_3 = i['LISTS'][1]['LIST_D'][2]['QTY']
                        QTY_4 = i['LISTS'][1]['LIST_D'][3]['QTY']

                        SEQ_1 = i['LISTS'][1]['LIST_D'][0]['SEQ']  # f
                        SEQ_2 = i['LISTS'][1]['LIST_D'][1]['SEQ']
                        SEQ_3 = i['LISTS'][1]['LIST_D'][2]['SEQ']
                        SEQ_4 = i['LISTS'][1]['LIST_D'][3]['SEQ']

                        print(CALL)
                        print(ITEM_1, ITEM_2, ITEM_3, ITEM_4)
                        print(QTY_1, QTY_2, QTY_3, QTY_4)
                        print(SEQ_1, SEQ_2, SEQ_3, SEQ_4)

                        k = {
                            CALL:
                                [
                                    {
                                        SEQ_1:
                                            {
                                                "ITEM_CD": ITEM_1,
                                                "QTY": QTY_1

                                            }
                                    },
                                    {
                                        SEQ_2:
                                            {
                                                "ITEM_CD": ITEM_2,
                                                "QTY": QTY_2

                                            }
                                    },
                                    {
                                        SEQ_3:
                                            {
                                                "ITEM_CD": ITEM_3,
                                                "QTY": QTY_3

                                            }
                                    },
                                    {
                                        SEQ_4:
                                            {
                                                "ITEM_CD": ITEM_4,
                                                "QTY": QTY_4

                                            }
                                    }

                                ]
                        }

                        m = json.dumps(k)

                        j_1 = int(CALL)

                        d_1 = int(ITEM_1)
                        d_2 = int(ITEM_2)
                        d_3 = int(ITEM_3)
                        d_4 = int(ITEM_4)

                        e_1 = int(QTY_1)
                        e_2 = int(QTY_2)
                        e_3 = int(QTY_3)
                        e_4 = int(QTY_4)

                        print(m)

                        if d_1 < 2000:
                            def x_1(count):
                                if count == 0:
                                    return
                                add(d_1)
                                count -= 1
                                x_1(count)

                            x_1(e_1)

                            def dis1(cou):
                                if cou == 0:
                                    return
                                dist.append(j_1)
                                cou -= 1
                                dis1(cou)

                            dis1(e_1)

                        elif d_1 >= 2000:
                            pass

                        if d_2 < 2000:
                            def x_2(count):
                                if count == 0:
                                    return
                                add(d_2)
                                count -= 1
                                x_2(count)

                            x_2(e_2)

                            def dis1(cou):
                                if cou == 0:
                                    return
                                dist.append(j_1)
                                cou -= 1
                                dis1(cou)

                            dis1(e_2)

                        elif d_2 >= 2000:
                            pass

                        if d_3 < 2000:
                            def x_3(count):
                                if count == 0:
                                    return
                                add(d_3)
                                count -= 1
                                x_3(count)

                            x_3(e_3)

                            def dis1(cou):
                                if cou == 0:
                                    return
                                dist.append(j_1)
                                cou -= 1
                                dis1(cou)

                            dis1(e_3)

                        elif d_3 >= 2000:
                            pass

                        if d_4 < 2000:
                            def x_4(count):
                                if count == 0:
                                    return
                                add(d_4)
                                count -= 1
                                x_4(count)

                            x_4(e_4)

                            def dis1(cou):
                                if cou == 0:
                                    return
                                dist.append(j_1)
                                cou -= 1
                                dis1(cou)

                            dis1(e_4)

                        elif d_4 >= 2000:
                            pass

                        print_q()
                        print(dist)

                        def save():
                            f = open("./kiosk_order/kioskorder.txt", 'a')
                            data = "\n-----------------------------------\n\n주문번호:%d \n품목:%d 수량:%d\n품목:%d 수량:%d\n품목:%d 수량:%d\n품목:%d 수량:%d\n\n주문시간:%s" % (
                                j_1, d_1, e_1, d_2, e_2, d_3, e_3, d_4, e_4, da)
                            f.write(data)
                            f.close()

                        save()

                        di2 = d_1 + d_2 + d_3 + d_4
                        if di2 > 5000:
                            dist2.append(j_1)
                            print(dist2)
                        elif di2 <= 5000:
                            pass


                    elif len(y) == 3:

                        da = i["date"]

                        CALL = i['LISTS'][0]['LIST_H'][0]['CALL_NO']

                        ITEM_1 = i['LISTS'][1]['LIST_D'][0]['ITEM_CD']  # d
                        ITEM_2 = i['LISTS'][1]['LIST_D'][1]['ITEM_CD']
                        ITEM_3 = i['LISTS'][1]['LIST_D'][2]['ITEM_CD']

                        QTY_1 = i['LISTS'][1]['LIST_D'][0]['QTY']  # e
                        QTY_2 = i['LISTS'][1]['LIST_D'][1]['QTY']
                        QTY_3 = i['LISTS'][1]['LIST_D'][2]['QTY']

                        SEQ_1 = i['LISTS'][1]['LIST_D'][0]['SEQ']  # f
                        SEQ_2 = i['LISTS'][1]['LIST_D'][1]['SEQ']
                        SEQ_3 = i['LISTS'][1]['LIST_D'][2]['SEQ']

                        print(CALL)
                        print(ITEM_1, ITEM_2, ITEM_3)
                        print(QTY_1, QTY_2, QTY_3)
                        print(SEQ_1, SEQ_2, SEQ_3)

                        k = {
                            CALL:
                                [
                                    {
                                        SEQ_1:
                                            {
                                                "ITEM_CD": ITEM_1,
                                                "QTY": QTY_1

                                            }
                                    },
                                    {
                                        SEQ_2:
                                            {
                                                "ITEM_CD": ITEM_2,
                                                "QTY": QTY_2

                                            }
                                    },
                                    {
                                        SEQ_3:
                                            {
                                                "ITEM_CD": ITEM_3,
                                                "QTY": QTY_3

                                            }
                                    }

                                ]
                        }

                        m = json.dumps(k)

                        j_1 = int(CALL)

                        d_1 = int(ITEM_1)
                        d_2 = int(ITEM_2)
                        d_3 = int(ITEM_3)

                        e_1 = int(QTY_1)
                        e_2 = int(QTY_2)
                        e_3 = int(QTY_3)

                        print(m)

                        if d_1 < 2000:
                            def x_1(count):
                                if count == 0:
                                    return
                                add(d_1)
                                count -= 1
                                x_1(count)

                            x_1(e_1)

                            def dis1(cou):
                                if cou == 0:
                                    return
                                dist.append(j_1)
                                cou -= 1
                                dis1(cou)

                            dis1(e_1)
                        elif d_1 >= 2000:
                            pass

                        if d_2 < 2000:
                            def x_2(count):
                                if count == 0:
                                    return
                                add(d_2)
                                count -= 1
                                x_2(count)

                            x_2(e_2)

                            def dis1(cou):
                                if cou == 0:
                                    return
                                dist.append(j_1)
                                cou -= 1
                                dis1(cou)

                            dis1(e_2)

                        elif d_2 >= 2000:
                            pass

                        if d_3 < 2000:
                            def x_3(count):
                                if count == 0:
                                    return
                                add(d_3)
                                count -= 1
                                x_3(count)

                            x_3(e_3)

                            def dis1(cou):
                                if cou == 0:
                                    return
                                dist.append(j_1)
                                cou -= 1
                                dis1(cou)

                            dis1(e_3)

                        elif d_3 >= 2000:
                            pass

                        print_q()
                        print(dist)

                        def save():
                            f = open("./kiosk_order/kioskorder.txt", 'a')
                            data = "\n-----------------------------------\n\n주문번호:%d \n품목:%d 수량:%d\n품목:%d 수량:%d\n품목:%d 수량:%d\n\n주문시간:%s" % (
                                j_1, d_1, e_1, d_2, e_2, d_3, e_3, da)
                            f.write(data)
                            f.close()

                        save()

                        di2 = d_1 + d_2 + d_3
                        if di2 > 4000:
                            dist2.append(j_1)
                            print(dist2)
                        elif di2 <= 4000:
                            pass





                    elif len(y) == 2:

                        da = i["date"]

                        CALL = i['LISTS'][0]['LIST_H'][0]['CALL_NO']

                        ITEM_1 = i['LISTS'][1]['LIST_D'][0]['ITEM_CD']  # d
                        ITEM_2 = i['LISTS'][1]['LIST_D'][1]['ITEM_CD']

                        QTY_1 = i['LISTS'][1]['LIST_D'][0]['QTY']  # e
                        QTY_2 = i['LISTS'][1]['LIST_D'][1]['QTY']

                        SEQ_1 = i['LISTS'][1]['LIST_D'][0]['SEQ']  # f
                        SEQ_2 = i['LISTS'][1]['LIST_D'][1]['SEQ']

                        print(CALL)
                        print(ITEM_1, ITEM_2)
                        print(QTY_1, QTY_2)
                        print(SEQ_1, SEQ_2)

                        k = {
                            CALL:
                                [
                                    {
                                        SEQ_1:
                                            {
                                                "ITEM_CD": ITEM_1,
                                                "QTY": QTY_1

                                            }
                                    },
                                    {
                                        SEQ_2:
                                            {
                                                "ITEM_CD": ITEM_2,
                                                "QTY": QTY_2

                                            }
                                    }

                                ]
                        }

                        m = json.dumps(k)

                        j_1 = int(CALL)

                        d_1 = int(ITEM_1)
                        d_2 = int(ITEM_2)

                        e_1 = int(QTY_1)
                        e_2 = int(QTY_2)

                        print(m)

                        if d_1 < 2000:
                            def x_1(count):
                                if count == 0:
                                    return
                                add(d_1)
                                count -= 1
                                x_1(count)

                            x_1(e_1)

                            def dis1(cou):
                                if cou == 0:
                                    return
                                dist.append(j_1)
                                cou -= 1
                                dis1(cou)

                            dis1(e_1)

                        elif d_1 >= 2000:
                            pass

                        if d_2 < 2000:
                            def x_2(count):
                                if count == 0:
                                    return
                                add(d_2)
                                count -= 1
                                x_2(count)

                            x_2(e_2)

                            def dis1(cou):
                                if cou == 0:
                                    return
                                dist.append(j_1)
                                cou -= 1
                                dis1(cou)

                            dis1(e_2)

                        elif d_2 >= 2000:
                            pass

                        print_q()
                        print(dist)

                        def save():
                            f = open("./kiosk_order/kioskorder.txt", 'a')
                            data = "\n-----------------------------------\n\n주문번호:%d \n품목:%d 수량:%d\n품목:%d 수량:%d\n\n주문시간:%s" % (
                            j_1, d_1, e_1, d_2, e_2, da)
                            f.write(data)
                            f.close()

                        save()

                        di2 = d_1 + d_2
                        if di2 > 3000:
                            dist2.append(j_1)
                            print(dist2)
                        elif di2 <= 3000:
                            pass





                    elif len(y) == 1:

                        da = i["date"]

                        CALL = i['LISTS'][0]['LIST_H'][0]['CALL_NO']

                        ITEM_1 = i['LISTS'][1]['LIST_D'][0]['ITEM_CD']  # d

                        QTY_1 = i['LISTS'][1]['LIST_D'][0]['QTY']  # e

                        SEQ_1 = i['LISTS'][1]['LIST_D'][0]['SEQ']  # f

                        print(CALL)
                        print(ITEM_1)
                        print(QTY_1)
                        print(SEQ_1)

                        k = {
                            CALL:
                                [
                                    {
                                        SEQ_1:
                                            {
                                                "ITEM_CD": ITEM_1,
                                                "QTY": QTY_1

                                            }
                                    }

                                ]
                        }

                        m = json.dumps(k)

                        j_1 = int(CALL)

                        d_1 = int(ITEM_1)

                        e_1 = int(QTY_1)

                        print(m)

                        if d_1 < 2000:
                            def x_1(count):
                                if count == 0:
                                    return
                                add(d_1)  # add라는 함수를 이용하여 큐 구조에 쌓습
                                count -= 1
                                x_1(count)

                            x_1(e_1)


                            def dis1(cou):
                                if cou == 0:
                                    return
                                dist.append(j_1) # append 함수를 이용하여 리스트 1에 추가
                                cou -= 1
                                dis1(cou)

                            dis1(e_1)


                        elif d_1 >= 2000:
                            pass

                        print_q()
                        print(dist)

                        def save():
                            f = open("./kiosk_order/kioskorder.txt", 'a')
                            data = "\n-----------------------------------\n\n주문번호:%d \n품목:%d 수량:%d\n\n주문시간:%s" % (
                            j_1, d_1, e_1, da)
                            f.write(data)
                            f.close()

                        save()

                        di2 = d_1
                        if di2 > 2000:
                            dist2.append(j_1) #append 함수를 이용하여 리스트 2에 추가
                            print(dist2)
                        elif di2 <= 2000:
                            pass

dist=[] #리스트1
dist2=[] #리스트2

class Node:
    def __init__(self,item,n):
        self.item=item
        self.next=n

def add(item):
    global size
    global front
    global rear

    new_node = Node(item, None)
    if size == 0:
        front = new_node
    else:
        rear.next = new_node
    rear = new_node
    size +=1

def remove():
    global size
    global front
    global rear
    if size != 0:
        fitem = front.item
        front = front.next
        size -=1
        if size == 0:
            rear = None
        return fitem

def print_q():
    p = front
    print('front: ', end='')
    while p:
        if p.next !=None:
            print(p.item, '-> ', end='')
        else:
            print(p.item, end = '')
        p = p.next
    print(' :rear')

front = None
rear = None
size = 0




def main():
    PORT = 80 #서버 포트 지정
    server = HTTPServer(('192.168.0.10', PORT), Handler) #서버 IP조소 지정
    print('Server running on port %s' % PORT)
    server.serve_forever() #서버 연결 유지

thread = threading.Thread(target=main)
thread.start()



# socket 모듈을 불러와 IP와 PORT를 지정하여 socket sever를 생성
class TCP_server:
    def TCP():
        while True:
            server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            server_socket.bind(('192.168.0.10', 60000))

            server_socket.listen()

            client_socket, addr = server_socket.accept()

            print('Connected by', addr)
            # 로봇이 보낸 데이터를 디코드
            def recv_data():
                while True:
                    data = client_socket.recv(4096)
                    o = data.decode()

                    print(o)
                    if o == "start":
                        tyu = remove()
                        print(tyu)
                        print_q()
                        del dist[0]

                        if tyu == 1001:
                            print('1')
                            data = "\"ame1\""
                            client_socket.send(data.encode("utf-8"))

                        elif tyu == 1002:
                            print('2')
                            data = "\"iceame1\""
                            client_socket.send(data.encode("utf-8"))

                        elif tyu == 1003:
                            print('3')
                            data = "\"esp1\""
                            client_socket.send(data.encode("utf-8"))

                        elif tyu == 1004:
                            print('4')
                            data = "\"lat1\""
                            client_socket.send(data.encode("utf-8"))

                        elif tyu == 1005:
                            print('5')
                            data = "\"cap1\""
                            client_socket.send(data.encode("utf-8"))

                        elif tyu == 1006:
                            print('6')
                            data = "\"moc1\""
                            client_socket.send(data.encode("utf-8"))

                        elif tyu == None:
                            print('a')

                client_socket.close()

            recv_data = threading.Thread(target=recv_data)
            recv_data.start()

    TCP = threading.Thread(target=TCP)
    TCP.start()

class GoodRoot(Tk):

    def __init__(self):
        super().__init__()
        self.title("srs 카페 주문번호")
        self.geometry("1780x800+50+10")
        font = tkinter.font.Font(family="맑은 고딕", size=80)
        font2 = tkinter.font.Font(family="맑은 고딕", size=30)
        # Display의 틀을 tkinter 모듈을 불러와 클래스로 만들어 줍니다.



        self.label_0_0 = Label(self, text="*", font=font)
        self.label_0_0.grid(row=0, column =0)
        self.label_1_0 = Label(self, text="*", font = font)
        self.label_1_0.grid(row=1, column =0)
        self.label_2_0 = Label(self, text="*", font=font)
        self.label_2_0.grid(row=2, column=0)
        self.label_3_0 = Label(self, text="대기2", font=font)
        self.label_3_0.grid(row=3, column=0)
        self.label_0_1 = Label(self, text="*", font=font)
        self.label_0_1.grid(row=0, column=1)
        self.label_1_1 = Label(self, text="커피", font=font)
        self.label_1_1.grid(row=1, column=1)
        self.label_2_1 = Label(self, text="대기1", font=font, fg ="red")
        self.label_2_1.grid(row=2, column=1)
        self.label_3_1 = Label(self, text="대기3", font=font)
        self.label_3_1.grid(row=3, column=1)
        self.label_0_2 = Label(self, text="*", font=font)
        self.label_0_2.grid(row=0, column=2)
        self.label_1_2 = Label(self, text="*", font=font)
        self.label_1_2.grid(row=1, column=2)
        self.label_2_2 = Label(self, text="*", font=font)
        self.label_2_2.grid(row=2, column=2)
        self.label_3_2 = Label(self, text="대기4", font=font)
        self.label_3_2.grid(row=3, column=2)
        self.label_0_3 = Label(self, text="*", font=font)
        self.label_0_3.grid(row=0, column=3)
        self.label_1_3 = Label(self, text="*", font=font)
        self.label_1_3.grid(row=1, column=3)
        self.label_2_3 = Label(self, text="*", font=font)
        self.label_2_3.grid(row=2, column=3)
        self.label_3_3 = Label(self, text="*", font=font)
        self.label_3_3.grid(row=3, column=3)
        self.label_0_4 = Label(self, text="*", font=font)
        self.label_0_4.grid(row=0, column=4)
        self.label_1_4 = Label(self, text="*", font=font)
        self.label_1_4.grid(row=1, column=4)
        self.label_2_4 = Label(self, text="*", font=font)
        self.label_2_4.grid(row=2, column=4)
        self.label_3_4 = Label(self, text="대기2", font=font)
        self.label_3_4.grid(row=3, column=4)
        self.label_0_5 = Label(self, text="*", font=font)
        self.label_0_5.grid(row=0, column=5)
        self.label_1_5 = Label(self, text="케이크", font=font)
        self.label_1_5.grid(row=1, column=5)
        self.label_2_5 = Label(self, text="대기1", font=font, fg ="red")
        self.label_2_5.grid(row=2, column=5)
        self.label_3_5 = Label(self, text="대기3", font=font)
        self.label_3_5.grid(row=3, column=5)
        self.label_0_6 = Label(self, text="*", font=font)
        self.label_0_6.grid(row=0, column=6)
        self.label_1_6 = Label(self, text="*", font=font)
        self.label_1_6.grid(row=1, column=6)
        self.label_2_6 = Label(self, text="*", font=font)
        self.label_2_6.grid(row=2, column=6)
        self.label_3_6 = Label(self, text="대기4", font=font)
        self.label_3_6.grid(row=3, column=6)

        def update():
            if not dist2:
                print("None")
                pass
            elif dist2[0]>0:
                del dist2[0]

        self.button = tkinter.Button(self, overrelief="solid", width=10, font=font2, text="다음 주문", command=update, bg='yellow', height=1, repeatdelay=1000,
                                repeatinterval=100)
        self.button.grid(row=4,column=5)


        while True:
            if not dist and not dist2:

                self.label_2_1.configure(text="대기1")
                self.label_3_0.configure(text="대기2")
                self.label_3_1.configure(text="대기3")
                self.label_3_2.configure(text="대기4")

                self.label_2_5.configure(text="대기1")
                self.label_3_4.configure(text="대기2")
                self.label_3_5.configure(text="대기3")
                self.label_3_6.configure(text="대기4")

                self.update()

            elif not dist and len(dist2) == 1 :

                self.label_2_1.configure(text="대기1")
                self.label_3_0.configure(text="대기2")
                self.label_3_1.configure(text="대기3")
                self.label_3_2.configure(text="대기4")

                self.label_2_5.configure(text=dist2[0])
                self.label_3_4.configure(text="대기2")
                self.label_3_5.configure(text="대기3")
                self.label_3_6.configure(text="대기4")

                self.update()

            elif not dist and len(dist2) == 2:

                self.label_2_1.configure(text="대기1")
                self.label_3_0.configure(text="대기2")
                self.label_3_1.configure(text="대기3")
                self.label_3_2.configure(text="대기4")

                self.label_2_5.configure(text=dist2[0])
                self.label_3_4.configure(text=dist2[1])
                self.label_3_5.configure(text="대기3")
                self.label_3_6.configure(text="대기4")

                self.update()

            elif not dist and len(dist2) == 3:

                self.label_2_1.configure(text="대기1")
                self.label_3_0.configure(text="대기2")
                self.label_3_1.configure(text="대기3")
                self.label_3_2.configure(text="대기4")

                self.label_2_5.configure(text=dist2[0])
                self.label_3_4.configure(text=dist2[1])
                self.label_3_5.configure(text=dist2[2])
                self.label_3_6.configure(text="대기4")

                self.update()


            elif not dist and len(dist2) >= 4:

                self.label_2_1.configure(text="대기1")
                self.label_3_0.configure(text="대기2")
                self.label_3_1.configure(text="대기3")
                self.label_3_2.configure(text="대기4")

                self.label_2_5.configure(text=dist2[0])
                self.label_3_4.configure(text=dist2[1])
                self.label_3_5.configure(text=dist2[2])
                self.label_3_6.configure(text=dist2[3])

                self.update()

            elif len(dist)==1 and not dist2:

                self.label_2_1.configure(text=dist[0])
                self.label_3_0.configure(text="대기2")
                self.label_3_1.configure(text="대기3")
                self.label_3_2.configure(text="대기4")

                self.label_2_5.configure(text="대기1")
                self.label_3_4.configure(text="대기2")
                self.label_3_5.configure(text="대기3")
                self.label_3_6.configure(text="대기4")

                self.update()

            elif len(dist) == 1 and len(dist2) == 1:

                self.label_2_1.configure(text=dist[0])
                self.label_3_0.configure(text="대기2")
                self.label_3_1.configure(text="대기3")
                self.label_3_2.configure(text="대기4")

                self.label_2_5.configure(text=dist2[0])
                self.label_3_4.configure(text="대기2")
                self.label_3_5.configure(text="대기3")
                self.label_3_6.configure(text="대기4")

                self.update()

            elif len(dist) == 1 and len(dist2) == 2:

                self.label_2_1.configure(text=dist[0])
                self.label_3_0.configure(text="대기2")
                self.label_3_1.configure(text="대기3")
                self.label_3_2.configure(text="대기4")

                self.label_2_5.configure(text=dist2[0])
                self.label_3_4.configure(text=dist2[1])
                self.label_3_5.configure(text="대기3")
                self.label_3_6.configure(text="대기4")

                self.update()

            elif len(dist) == 1 and len(dist2) == 3:

                self.label_2_1.configure(text=dist[0])
                self.label_3_0.configure(text="대기2")
                self.label_3_1.configure(text="대기3")
                self.label_3_2.configure(text="대기4")

                self.label_2_5.configure(text=dist2[0])
                self.label_3_4.configure(text=dist2[1])
                self.label_3_5.configure(text=dist2[2])
                self.label_3_6.configure(text="대기4")

                self.update()

            elif len(dist) == 1 and len(dist2) >= 4:

                self.label_2_1.configure(text=dist[0])
                self.label_3_0.configure(text="대기2")
                self.label_3_1.configure(text="대기3")
                self.label_3_2.configure(text="대기4")

                self.label_2_5.configure(text=dist2[0])
                self.label_3_4.configure(text=dist2[1])
                self.label_3_5.configure(text=dist2[2])
                self.label_3_6.configure(text=dist2[3])

                self.update()

            elif len(dist) == 2 and not dist2:

                self.label_2_1.configure(text=dist[0])
                self.label_3_0.configure(text=dist[1])
                self.label_3_1.configure(text="대기3")
                self.label_3_2.configure(text="대기4")

                self.label_2_5.configure(text="대기1")
                self.label_3_4.configure(text="대기2")
                self.label_3_5.configure(text="대기3")
                self.label_3_6.configure(text="대기4")

                self.update()

            elif len(dist) == 2 and len(dist2) == 1:

                self.label_2_1.configure(text=dist[0])
                self.label_3_0.configure(text=dist[1])
                self.label_3_1.configure(text="대기3")
                self.label_3_2.configure(text="대기4")

                self.label_2_5.configure(text=dist2[0])
                self.label_3_4.configure(text="대기2")
                self.label_3_5.configure(text="대기3")
                self.label_3_6.configure(text="대기4")

                self.update()

            elif len(dist) == 2 and len(dist2) == 2:

                self.label_2_1.configure(text=dist[0])
                self.label_3_0.configure(text=dist[1])
                self.label_3_1.configure(text="대기3")
                self.label_3_2.configure(text="대기4")

                self.label_2_5.configure(text=dist2[0])
                self.label_3_4.configure(text=dist2[1])
                self.label_3_5.configure(text="대기3")
                self.label_3_6.configure(text="대기4")

                self.update()

            elif len(dist) == 2 and len(dist2) == 3:

                self.label_2_1.configure(text=dist[0])
                self.label_3_0.configure(text=dist[1])
                self.label_3_1.configure(text="대기3")
                self.label_3_2.configure(text="대기4")

                self.label_2_5.configure(text=dist2[0])
                self.label_3_4.configure(text=dist2[1])
                self.label_3_5.configure(text=dist2[2])
                self.label_3_6.configure(text="대기4")

                self.update()

            elif len(dist) == 2 and len(dist2) >= 4:

                self.label_2_1.configure(text=dist[0])
                self.label_3_0.configure(text=dist[1])
                self.label_3_1.configure(text="대기3")
                self.label_3_2.configure(text="대기4")

                self.label_2_5.configure(text=dist2[0])
                self.label_3_4.configure(text=dist2[1])
                self.label_3_5.configure(text=dist2[2])
                self.label_3_6.configure(text=dist2[3])

                self.update()

            elif len(dist) == 3 and not dist2:

                self.label_2_1.configure(text=dist[0])
                self.label_3_0.configure(text=dist[1])
                self.label_3_1.configure(text=dist[2])
                self.label_3_2.configure(text="대기4")

                self.label_2_5.configure(text="대기1")
                self.label_3_4.configure(text="대기2")
                self.label_3_5.configure(text="대기3")
                self.label_3_6.configure(text="대기4")

                self.update()

            elif len(dist) == 3 and len(dist2) == 1:

                self.label_2_1.configure(text=dist[0])
                self.label_3_0.configure(text=dist[1])
                self.label_3_1.configure(text=dist[2])
                self.label_3_2.configure(text="대기4")

                self.label_2_5.configure(text=dist2[0])
                self.label_3_4.configure(text="대기2")
                self.label_3_5.configure(text="대기3")
                self.label_3_6.configure(text="대기4")

                self.update()

            elif len(dist) == 3 and len(dist2) == 2:

                self.label_2_1.configure(text=dist[0])
                self.label_3_0.configure(text=dist[1])
                self.label_3_1.configure(text=dist[2])
                self.label_3_2.configure(text="대기4")

                self.label_2_5.configure(text=dist2[0])
                self.label_3_4.configure(text=dist2[1])
                self.label_3_5.configure(text="대기3")
                self.label_3_6.configure(text="대기4")

                self.update()

            elif len(dist) == 3 and len(dist2) == 3:

                self.label_2_1.configure(text=dist[0])
                self.label_3_0.configure(text=dist[1])
                self.label_3_1.configure(text=dist[2])
                self.label_3_2.configure(text="대기4")

                self.label_2_5.configure(text=dist2[0])
                self.label_3_4.configure(text=dist2[1])
                self.label_3_5.configure(text=dist2[2])
                self.label_3_6.configure(text="대기4")

                self.update()

            elif len(dist) == 3 and len(dist2) >= 4:

                self.label_2_1.configure(text=dist[0])
                self.label_3_0.configure(text=dist[1])
                self.label_3_1.configure(text=dist[2])
                self.label_3_2.configure(text="대기4")

                self.label_2_5.configure(text=dist2[0])
                self.label_3_4.configure(text=dist2[1])
                self.label_3_5.configure(text=dist2[2])
                self.label_3_6.configure(text=dist2[3])

                self.update()

            elif len(dist) >= 4 and not dist2:

                self.label_2_1.configure(text=dist[0])
                self.label_3_0.configure(text=dist[1])
                self.label_3_1.configure(text=dist[2])
                self.label_3_2.configure(text=dist[3])


                self.label_2_5.configure(text="대기1")
                self.label_3_4.configure(text="대기2")
                self.label_3_5.configure(text="대기3")
                self.label_3_6.configure(text="대기4")

                self.update()

            elif len(dist) >= 4 and len(dist2) == 1:

                self.label_2_1.configure(text=dist[0])
                self.label_3_0.configure(text=dist[1])
                self.label_3_1.configure(text=dist[2])
                self.label_3_2.configure(text=dist[3])

                self.label_2_5.configure(text=dist2[0])
                self.label_3_4.configure(text="대기2")
                self.label_3_5.configure(text="대기3")
                self.label_3_6.configure(text="대기4")

                self.update()

            elif len(dist) >= 4 and len(dist2) == 2:

                self.label_2_1.configure(text=dist[0])
                self.label_3_0.configure(text=dist[1])
                self.label_3_1.configure(text=dist[2])
                self.label_3_2.configure(text=dist[3])

                self.label_2_5.configure(text=dist2[0])
                self.label_3_4.configure(text=dist2[1])
                self.label_3_5.configure(text="대기3")
                self.label_3_6.configure(text="대기4")

                self.update()

            elif len(dist) >= 4 and len(dist2) == 3:

                self.label_2_1.configure(text=dist[0])
                self.label_3_0.configure(text=dist[1])
                self.label_3_1.configure(text=dist[2])
                self.label_3_2.configure(text=dist[3])

                self.label_2_5.configure(text=dist2[0])
                self.label_3_4.configure(text=dist2[1])
                self.label_3_5.configure(text=dist2[2])
                self.label_3_6.configure(text="대기4")

                self.update()

                # Display를 while문과 if문을 이용해 리스트에 추가되고 삭제되는 것에 따라 Display의label을update하기
            elif len(dist) >= 4 and len(dist2) >= 4:

                self.label_2_1.configure(text=dist[0])
                self.label_3_0.configure(text=dist[1])
                self.label_3_1.configure(text=dist[2])
                self.label_3_2.configure(text=dist[3])

                self.label_2_5.configure(text=dist2[0])
                self.label_3_4.configure(text=dist2[1])
                self.label_3_5.configure(text=dist2[2])
                self.label_3_6.configure(text=dist2[3])

                self.update()


if __name__ == '__main__':

        GoodRoot()

while True:
    pass