# ----------------------------------------
#              创建姓名：十元

#              创建时间：2021/2/15 下午6:45

# 功能实现：post 和get请求 session 待验证
# ---------------------------------------
import requests
from tools.Log_Tools import mylog
class RequestsTool:
    def requests(self, request_mode, url, headers=None, json=None, data=None):
        mylog.info('请求加载进来了'+'request_mode:<'+request_mode+
                   '>  url:<'+str(url)+
                   '>  headers:<'+str(headers)+
                   '>  json:<'+str(json) +
                   '>  data:<'+str(data)
                   )
        if request_mode in ('get', 'Get', 'GET'):  # get请求
            respons = requests.get(url=url, headers=headers, json=json, params=data)
        elif request_mode in ('post', 'Post', 'POST'):  # post请求
            respons = requests.post(url=url, headers=headers, json=json, data=data)
        else:
            # 打印日志
            mylog.error('请求模式非法')
            print('请求非法')
            pass
        mylog.info("请求结束了,响应信息：<" +str(respons.json())+'>')
        return respons.json()


requests.session()


class SessionTools:
    def __init__(self):
        self.session = requests.session()

    def Session_re(self, request_mode, url, headers=None, json=None, data=None):
        if request_mode in ('get', 'GET', 'Get'):
            response = self.session.get(url=url, headers=headers, json=json, farams=data)
        elif request_mode in ('post', 'POST', 'Post'):
            response = self.session.post(url=url, headers=headers, json=json, data=data)
        else:
            # 日志打印
            mylog.error('请求模式非法')
            print('请求非法')
            pass
        return response.json()

    def Session_close(self):
        self.session.close()


# get测试
# if __name__ == '__main__':
#     request_mode ='get'
#     url ='http://47.100.92.21:8080/colatest/colamember/registMember.do'
#     data ={
#         "accountName" : "shi" ,
#         "accountPWD" : "123456" ,
#         "phoneNumber" : "13838381441" ,
#         "accountType" : "1" ,
#         "accountId" : "1111111111111113"
#     }
#
#     respons =RequestsTool().requests(request_mode,url,data)
#     print(respons)

# post测试
if __name__ == '__main__':
    request_mode = 'post'
    url = 'http://47.100.92.21:8080/colatest/colamember/login.do'
    # url='http://www.youdao.com/'
    data = {
        "accountPWD": "222222",
        "phoneNumber": "13333333333"
    }
    response = RequestsTool().requests(request_mode=request_mode, url=url, json=data)


    print(response)
