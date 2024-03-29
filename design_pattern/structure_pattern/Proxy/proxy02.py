"""
Proxyパターン
代理を表している。処理が複雑、危険な処理がありチェックしたい場合に使う

・Subject: RealSubjectとProxyを同一視して利用するためのIF
・RealSubject: Subjectを継承して処理記述
・Proxy: RealSubjectの代わりにクライアントからの処理を返す。自分で処理できなかった場合にRealSubjectを呼ぶ
"""

from abc import ABC, abstractmethod
import time

class APICaller(ABC):
    
    @abstractmethod
    def request(self):
        pass
    

class RealAPICaller(APICaller):
    
    def __init__(self, url):
        self.__url = url
        time.sleep(5)
    
    def request(self):
        print('APIを呼び出す')
        return

class RealAPICallerProxy(APICaller):
    def __init__(self, url):
        self.__url = url
        
    def __check_access(self):
        print('アクセスに成功しました')
        return True
    
    def __write_log(self):
        print('ログを出力しました')

    def request(self):
        if self.__check_access():
            real_api_caller = RealAPICaller(self.__url)
            real_api_caller.request()
            self.__write_log()
            return

# caller = RealAPICaller('http://api.com')
# caller.request()

proxy = RealAPICallerProxy('http://api.com')
proxy.request()