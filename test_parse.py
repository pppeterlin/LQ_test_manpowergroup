##################################################
## Project: {Crawler Parser LQ assessment}
## Author: {Chun}
## Version: {2100906}
## Status: 
##################################################

import requests
import json
import random
import pandas as pd
from datetime import datetime
import time

# XHR_invite: Get token & uid for submit 
def invite(token):
    url = "https://insights.manpowergroupassessments.com/api/v1/invite"

    headers = {"User-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15",
                "Host": "insights.manpowergroupassessments.com",
                "Referer": "https://insights.manpowergroupassessments.com/",
                # "X-TOKEN":"eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJpYXQiOjE2MzEwODQwMjUsImV4cCI6MTYzMTE3MDQyNSwiZW1haWwiOiJhbm9uXzYxMDM1MDEzMUBtYXJrZXRpbmcuY29tIiwiaWQiOjIzNjk5NSwidHlwZSI6InRva2VuIiwiYWNjb3VudCI6Im1hcmtldGluZyIsImtleSI6IjRhODFlZDFkOGE5MWZiNWNmZWQ1YmIyMDAyMDc0MGJjMzUwNmI3NzgiLCJzZXNzaW9uX2tleSI6ImE0YTNkZmViMzE2YTg0NWRlMzhjMzUxOWZkOTMxMDJiZDkwODZkMDAifQ.c4QSmiOeoIjpwNgJADtIHulqv81rtIawo2gZE461ndJNbWfHVC8VsD3Q6y-Vn-HJmHNJ6K_TVJtlIY_BFZmWCRFsvCLe-PQA7RMjiUkICxwxVq9ciDrX7bOKo0IKDTEs6AAhkXTDAKoH8H6xYKb1LaN334iQmaXjqcBSXYoqWQrHZyUR9Yu4CEwG9Yl_X7YpBXp0W9EAyw52P2-vsOyXd8QwVMOw_gShPOBaPf-qTf0crgoqIrEpboKZVMs7p7zeS8dd-oWqgP1d0glVrteConJGeJHasQc-WKjJ4xatcdT79kkcdvnU9KKx6FmJELQo2UjZ2D2stgFIg-MXaK504Yf2aex_6M_ExbzWbI0dn8HQFgl6RwIxVkXdaADcYq0nKe91DvCNVGM3c9jsnAaEreIWL-CAnnfHSbf9hc1b2Dogy7UrOCzZBrFJqEdKMNH8P-oelf8E4wWWqatMD00pGpkQxJd8rt8ZAC7TMDmjIsaamVbURtnwyhCdsRNldSvGAjq3KgeUxCpJAMVNidIoZfmRDFvKIEWM32xgulGsq5T00wkveQ57lGJz8P2TRfLOxvc_g3OgydOjq66eylYfpnunvTOPsY0SyvBM4wddmmEBb-AM7XOSuQVblXiGAKOcDVOSIMJoWULN6Of0EXfxiy34Qel9M96KfR7T3lb5ka8"
                "X-TOKEN": token
    }
    data = {"token": "0a6e553c90590ad754be7e7c40c9fc23"}
    s = requests.session()
    html = s.post(url, headers=headers, data=data)
    if(html.status_code==200):
        print('Invite Successfully')
        html = json.loads(html.text)
        return({'token': html['tokens']['token_key'],
                'qtoken': html['tokens']['quizToken']['token'],
                'uid':html['tokens']['user']['id'],
                'vid':html['userassessment']['vendor_id']})
    else:
        print("Invite Fail.")
        return(0)


# XRH_submmit: Submmit answers
def submmit(x_token, quiz_token, ans):
    url = "https://insights.quiz.manpowergroupassessments.com/api/v1/quiz/submit"
    headers = {"User-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15",
                # "X-TOKEN":"eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJpYXQiOjE2MzEyNTkwNjQsImV4cCI6MTYzMTM0NTQ2NCwiZW1haWwiOiJhbm9uXzE5NzIxNjgzNThAbWFya2V0aW5nLmNvbSIsImlkIjoyMzc3NTIsInR5cGUiOiJ0b2tlbiIsImFjY291bnQiOiJtYXJrZXRpbmciLCJrZXkiOiIxZTQ1YjE3ZWY5MWFlZjllNGE5MjMxMzJiZWMyNTU1OGYwMjA3Njk1Iiwic2Vzc2lvbl9rZXkiOiIwZGY3ZTdkZmU0ZjU2MTZkMzA4OGM5YTY0NWYxODBiMTE5MzcyMDg0In0.SDUnao8T0va5pQnhuEnZH_nURNhg3WquY7vBAKcAWhe3W-Mrh9AYkiCIiSw5J-iMZYguPoFKsQa-rrpr5hZ3wQT1C-ndIDcmFgKFTvrgEVCzT29fQuY_VXQ2rCIi653CQR3P3IY0gY1-LSny_Kz-BzlSuAQ-TB0wMYpo-Qyt6FHLt_B4PMNpTRFvYQb20V_LEgh1j_Ou6B5L8ppsYUfUQY8IJrh_BV43ljS_LXskOcA05GqidySoBDqo2g830CtUSe6e9oX5Oi7nZmgLAoOWtzFEeKEVsX4B2Gj0EI98WE3O3APaQO-SWCSxQ8tdEP6GzWJ1kiEX9RiKctSp2MAPwIMtddrpROnjofKdFRJodiNGbuZhvvhryz2eggkUGBgLSll26xHzFAzKQ6DlMDvjcQZ_32tMmjzu68tlA5f-7fBZChAy9QnvOhLFzId6znbiRVzJadxRoH8BZo4O5yePkdsgxu1R0D2oRzQV6rTtUGTYJfhDCVsXrPDFMEFo1AMktOtie4QYHx-M9x4O1rfOAnMg9IrpblwXC6Ml7z31YqH--_13iB8QVOEGFv26TY5q3wwyGN56I0lPLCfHBfrm7Jbj4kVsTIC3WwHUAtSz4-w57VWEtxvA6cMbHvV81fX8MPIOfDGtWWWRBjPg4COY5uSZIhpr6hkQWN52bAR4gaQ",
                # "QuizToken":"a7113132cc32392d94d45a8d5bce6e56b50413b2a0d10b852eaee8e034d3b85ce8cadd8b",
                "X-TOKEN": x_token,
                "QuizToken": quiz_token
                }    
    # ans = {"hidden_fields":{"uid":uid},
    #                         "quiz_key":"3iN5mfN4JR",
    #                         "result_key":"negzLpTZmS",
    #                         "result":{"vjUS31K3CaFJ":{"value":"0","text":"False"},
    #                                     "PqCwhIKJzhsp":{"value":"1","text":"False"},
    #                                     "9d1ovlHB72es":{"value":"1","text":"True"},
    #                                     "SwuGNe2gTjze":{"value":"0","text":"True"},
    #                                     "e73OMCMftDhd":{"value":"1","text":"False"},
    #                                     "g4PsMghgAAiq":{"value":"1","text":"True"},
    #                                     "ZX1PBvCZpKu8":{"value":"1","text":"True"},
    #                                     "NnlQ7lw1tdHA":{"value":"0","text":"True"},
    #                                     "YXnG1ykzkyYA":{"value":"1","text":"False"},
    #                                     "qFd479yUeFoH":{"value":"1","text":"True"},
    #                                     "IdrXuJz3E7dl":{"value":"0","text":"False"},
    #                                     "lX6Dlmr4IUMT":{"value":"0","text":"True"},
    #                                     "5hKNGRznPqBh":{"value":"0","text":"False"},
    #                                     "YE53DdN9Jg6L":{"value":"0","text":"False"},
    #                                     "goYJGaXbEBSg":{"value":"1","text":"True"},
    #                                     "36suqmeVQJbK":{"value":"0","text":"True"},
    #                                     "Tju11YYlgsPh":{"value":"0","text":"False"},
    #                                     "QWxymtatxcGX":{"value":"0","text":"True"},
    #                                     "GjFwlEBz7WVy":{"value":"0","text":"False"},
    #                                     "8d48e7p6xqo7":{"value":"1","text":"True"},
    #                                     "ucPoMFaQOMKZ":{"value":"1","text":"True"},
    #                                     "Dnr8dpYhvw1p":{"value":"0","text":"True"},
    #                                     "ntqLIhrdeq4k":{"value":"1","text":"False"},
    #                                     "Mub5LBXqsdUS":{"value":"1","text":"False"},
    #                                     "WLKB71aqLoyP":{"value":"3","text":''},
    #                                     "ZWrTMFLE3Jpi":{"value":"2","text":"SATISFIED - I am unaware of my opportunities for growth, but I am happy for now"}},
    #                                     "locale":"en"}
    ans = json.dumps(ans)
    s = requests.session()
    html = s.post(url, headers=headers, data=ans)
    if(html.status_code==200):
        print('Submmit successfully!')
        return(1)
    else:
        print('Submmit Failed!')
        return(0)


# XHR_score: Get result
def score(x_token, uid):
    # url = 'https://insights.manpowergroupassessments.com/api/v1/results/3iN5mfN4JR/236495/score' 
    url = ('/').join(['https://insights.manpowergroupassessments.com/api/v1/results/3iN5mfN4JR', str(uid), 'score'])
    headers = {"User-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36",
                "Referer": "https://insights.manpowergroupassessments.com/",
                # "X-TOKEN":"eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJpYXQiOjE2MzEwMDM2MTMsImV4cCI6MTYzMTA5MDAxMywiZW1haWwiOiJhbm9uXzcyNDk3OTgyNkBtYXJrZXRpbmcuY29tIiwiaWQiOjIzNjUxNCwidHlwZSI6InRva2VuIiwiYWNjb3VudCI6Im1hcmtldGluZyIsImtleSI6IjA5YTZiMWIwOTQ4YmRlYTg3YzRhNWI5YTM2MWFmNzkxNDcxMTExZjgiLCJzZXNzaW9uX2tleSI6IjA0ODA4MTRiZGYwZDRhYzljNjQ2MTdkMTUwMTM0YzYyMTI0ZjY0ODIifQ.DqKf4BYO4iA0YzXjQwfEdwENs_e-lt32rDuv-pVE7DhlcK1SWTgbIOxpFpKDbPqh-2vdGzidjg4OZPHrLZpEeNcuYX5OPwJfhzVus71N8AaHfDhan8RiNeKUrK-9Vpnz48gxJSIHto_KC5JW23AcHFohpcvCfUtqLB4WhGhUEsOwDvlhv4Tt2KwVHNO7fTvnP2ZF0RCpP42DVxMcjSjZlw3F3vcrwDuWMb-1pNTl4lf86OyH4Hc7dFDuhiKka1mfvhHg6gGgJt1UV8On8BzeSKWRKFsTGWwqH1djTkk-wOQd3h8G7zEP7auubwbQzKFjH73-di55lPjn2AditglhrYgKfCIbnKqFqKsn3LNzML034pzUHyXDhBNDL52UcTMByyXax9pqqpMgsI6HXhvqNpoGbSt_ZuRbfX_tvTcdNGumRmJftOSFPhHD33XU51KZICnVeAM3PAWxSdqbZ-eaSRr0YxNQXPCGnn_1ccCcxTbX6RCK60tiaxc9GuWl5bKDiYlnNbuPd2q4dzhB-vgfmShUwCRujdDSzF9jDNb3-M5sPzc8UA5Pj0orTMMUXD615_UwGolc42Nu0aG1N_DhJMiHWu1fJEhl8mDIJW4JFqx0Sd_JPwL27HNRrTq_VJ1kkvjzjVXc45WnyMhWOeU4j6nxrR6jFMkzL7vkE6tOeWM"
                "X-TOKEN": x_token
                }
    s = requests.session()
    html = s.get(url, headers = headers)
    if(html.status_code==200):
        html = json.loads(html.text)
        return(html['score']['scores']['normalized_summary'])
    else:
        print('Score Response Error!')
        return(0)

# Get New X-TOKEN from XHR_invite
# from selenium import webdriver
# # init webdriver
# executable_path = os.path.join(os.getcwd(), '../', 'chromedriver')
# if platform.system() == 'Windows':
#     executable_path += '.exe'
# driver = webdriver.Chrome(executable_path = executable_path)


def tokenCheck(xtoken, log_path='../log'):
    result = invite(xtoken)
    try:
        log = open(log_path, 'a')
    except:
        log = open(log_path, 'w')

    
    time_check = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    log.write('[Log Time]: ' + time_check + '\n')
    log.write('[X-TOKEN]='+xtoken+'\n')

    if result:
        # print('X-TOKEN is valid.')
        log.write('[Token Status]: Valid. \n')
    else:
        # print('X-TOKNE is invalid.')
        log.write('[Token Status]: Invalid. \n')
    
    log.write('\n')
    log.close()
    return result

def ansTrans(value, uid, result_key):
    # value = list(value)
    ans = {"hidden_fields":{"uid":uid},
                    "quiz_key":"3iN5mfN4JR",
                    "result_key":result_key,
                    "result":{"vjUS31K3CaFJ":{"value":"1","text":"True"},
                                "PqCwhIKJzhsp":{"value":"0","text":"True"},
                                "9d1ovlHB72es":{"value":"1","text":"True"},
                                "SwuGNe2gTjze":{"value":"0","text":"True"},
                                "e73OMCMftDhd":{"value":"0","text":"True"},
                                "g4PsMghgAAiq":{"value":"1","text":"True"},
                                "ZX1PBvCZpKu8":{"value":"1","text":"True"},
                                "NnlQ7lw1tdHA":{"value":"0","text":"True"},
                                "YXnG1ykzkyYA":{"value":"0","text":"True"},
                                "qFd479yUeFoH":{"value":"1","text":"True"},
                                "IdrXuJz3E7dl":{"value":"1","text":"True"},
                                "lX6Dlmr4IUMT":{"value":"0","text":"True"},
                                "5hKNGRznPqBh":{"value":"1","text":"True"},
                                "YE53DdN9Jg6L":{"value":"1","text":"True"},
                                "goYJGaXbEBSg":{"value":"1","text":"True"},
                                "36suqmeVQJbK":{"value":"0","text":"True"},
                                "Tju11YYlgsPh":{"value":"1","text":"True"},
                                "QWxymtatxcGX":{"value":"0","text":"True"},
                                "GjFwlEBz7WVy":{"value":"1","text":"True"},
                                "8d48e7p6xqo7":{"value":"1","text":"True"},
                                "ucPoMFaQOMKZ":{"value":"1","text":"True"},
                                "Dnr8dpYhvw1p":{"value":"0","text":"True"},
                                "ntqLIhrdeq4k":{"value":"0","text":"True"},
                                "Mub5LBXqsdUS":{"value":"0","text":"True"},
                                "WLKB71aqLoyP":{"value":"3","text":''},
                                "ZWrTMFLE3Jpi":{"value":"2","text":"SATISFIED - I am unaware of my opportunities for growth, but I am happy for now"}},
                                "locale":"en"}    
    key = [k for k in ans['result'].keys()]
    for i in range(len(value)):
        ans['result'][key[i]]['value'] = str(value[i])
    # v_True = [1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0]
    # diff = [i-j for i, j in zip(v_True, list(value))]
    # for i in range(len(diff)):   
    #     if(diff[i]):
    #         ans['result'][key[i]]['text'] = 'False'
        
    return(ans)


if __name__ == '__main__':
    rawdt = pd.read_csv('../answers.csv', index_col=0)

    for k in range(7):
        ind_start = 2**(17+k)
        save_path = '../parse_result_'+str(ind_start)+'.csv'

        dt = rawdt.iloc[ind_start:(ind_start+1000),:]
        # rawdt = pd.read_excel('/Users/peterlin/Desktop/lqdata.xlsx', engine='openpyxl')
        xtoken="eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJpYXQiOjE2MzE3Nzk2NTIsImV4cCI6MTYzMTg2NjA1MiwiZW1haWwiOiJhbm9uXzIxMDE5NjUxNUBtYXJrZXRpbmcuY29tIiwiaWQiOjIzOTgwNCwidHlwZSI6InRva2VuIiwiYWNjb3VudCI6Im1hcmtldGluZyIsImtleSI6IjEyZTg3ZmZhNjljZGIyNTUzYjIxZjhkNTgwOGNlY2ZiODIwMjAyZjYiLCJzZXNzaW9uX2tleSI6IjM5MGE1NjdlMDk4MjgzNzVjM2YwMjJkNWUwMDU2ZTcwYTA4YjcyOGYifQ.arxhyxSyyLdoJpMMZqnPhL8UFAtUX_GaWTsmtt-cFs-16vxVeT4QS409H6AWPR0zpkl_DOfYRxzH8N09fTVrz5U5nXem07mIlshE0YI3eRpb4IJ11cuydgbN83r_xeG-BAEj4FcIU7JKZsoQqv2CkYIETi7nTauuUpJpI9xCthLk4YX6ImsExuaY2GV7lIpvK8IWTOMV9a5OsOEeFuzvdiQ0piFJZ7w063ENtoTshwVqdHSVzQtqOMg5ZLaw8XU7mKRNvpz4y5K6Ustx8xcaOrL42SzcawPNn72YLblXeCqtF532o7pXMu6itdRxfIw6e1fk26VH9XeEI1Bng6JYnF7uA8sjkUmwPJJG7Opb1VOJvDVk9rK4_cJrxyXGwafnKP7m3MEz9t0Fabij4aaSS8RNR71PDs5FTPKcibxeYfbG1BhcVkSX5v6kgNEjpkhUzPBLl0Ux31ZVwjk3JrjnBWU8t9pCCVA2QPYFL7iAqvLPQ8MEKbvc82DOin8ED37d4gdrN5JmCb-8aOiZFojPNj_FZWtITS4irg5i79obVkXVJ4bMS_2SWjL8gDUJu_WD1a_4sK3zWpXCJuD4nMfWAQgvOxzxAgUGBBPpNq69hWDutnI91zfXeMUwgzqV7QNYNJz8PS2NsJ1pYK1Q3W8f5cg9WB-VuglcP0bHPatMEUE"
        result = tokenCheck(xtoken)
        # for i in range(dt_ans):
        n = 0
        for i in range(1000):
            if (i%50==0 & (i!=0)):
                result = tokenCheck(xtoken)
                dt.head(i).to_csv(save_path)
            
            if((i%100==0) & (i!=0)):
                print('Sleeping...')
                time.sleep(100)
            
            if result:
                try:
                    print('Progress: '+str(i)+'/'+str(len(dt)))
                    token = result['token']
                    uid = result['uid']
                    qtoken = result['qtoken']
                    result_key = result['vid']
                    v = dt.iloc[i,:24]
                    ans = ansTrans(v, uid, result_key)                                        
                    submmit(token, qtoken, ans, uid)
                    s = score(token, uid)
                    dt.iloc[i, 24] = s[2]
                    dt.iloc[i, 25] = s[0]
                    dt.iloc[i, 26] = s[1]

                    # v = rawdt.iloc[i,1:25]
                    # ans = ansTrans(v, uid, result_key)                                        
                    # submmit(token, qtoken, ans, uid)
                    # s = score(token, uid)
                    # rawdt.iloc[i, 25] = s[2]
                    # rawdt.iloc[i, 26] = s[0]
                    # rawdt.iloc[i, 27] = s[1]
                    print('')
                    n=i
                except:
                    print('token failed')
                    
        dt.to_csv(save_path)
        print('Done')
            
        


    # Sampling
    ind_change = []
    for i in range(24):
        ind_change.append(dt[str(i)].eq(0).idxmax())
    ind_change

    for i in range(7):
        print(2**(17+i))

