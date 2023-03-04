import requests
import json
import time
b='47093004950016'#初始化消息id（填需要发送频道的最后一条消息链接的最后一串数字,必须设置）
okkey=0
lp='40e8a03ab7363267748ae59ae8af09fd1bf15551a96d3bd995b1ad0167f7f5b038'#令牌
pd_id=39650900596224#频道id
while True:
    time.sleep(1)
    url='https://a1.fanbook.mobi/api/bot/'+lp+'/message/getList'#注意令牌
    headers = {'content-type':"application/json;charset=utf-8"}
    jsonfile=json.dumps({'channel_id':str(pd_id),'message_id':b,'behavior':'after'})#channel_id填频道id
    postreturn=requests.post(url,data=jsonfile,headers=headers)
    a=str(postreturn.text)
    okkey+=1
    if len(a)>150:
                desc_data = json.loads(postreturn.text)["data"]
                print(desc_data)
                me=int(json.loads(desc_data[0]['message_id']))
                desc_data = json.loads(desc_data[0]['content'])
                desc_data = desc_data['text']
                print(desc_data)
                if '去哪里闲聊？' in desc_data:
                    url='https://a1.fanbook.mobi/api/bot/'+lp+'/sendMessage'#注意令牌
                    headers = {'content-type':"application/json;charset=utf-8"}
                    jsonfile=json.dumps({"chat_id":pd_id,"text":'闲聊可以去${#395848619799871489}'})
                    postreturn=requests.post(url,data=jsonfile,headers=headers)
                    c=postreturn.text
                    b=c[34:52]
                elif '去哪里签到？' in desc_data:
                    url='https://a1.fanbook.mobi/api/bot/'+lp+'/sendMessage'#注意令牌
                    headers = {'content-type':"application/json;charset=utf-8"}
                    jsonfile=json.dumps({"chat_id":pd_id,"text":'签到可以去${#395853531971596288}'})
                    postreturn=requests.post(url,data=jsonfile,headers=headers)
                    c=postreturn.text
                    b=c[34:52]
                elif '求皮肤' in desc_data:
                    url='https://a1.fanbook.mobi/api/bot/'+lp+'/sendMessage'#注意令牌
                    headers = {'content-type':"application/json;charset=utf-8"}
                    jsonfile=json.dumps({"chat_id":pd_id,"text":'禁止ssd'})
                    postreturn=requests.post(url,data=jsonfile,headers=headers)
                    c=postreturn.text
                    b=c[34:52]
                    url='https://a1.fanbook.mobi/api/bot/'+lp+'/deleteMessage'#注意令牌
                    headers = {'content-type':"application/json;charset=utf-8"}
                    jsonfile=json.dumps({"chat_id":pd_id,"message_id":me})
                    postreturn=requests.post(url,data=jsonfile,headers=headers)
                    print(postreturn.text)
                elif '求送皮肤' in desc_data:
                    url='https://a1.fanbook.mobi/api/bot/'+lp+'/sendMessage'#注意令牌
                    headers = {'content-type':"application/json;charset=utf-8"}
                    jsonfile=json.dumps({"chat_id":pd_id,"text":'禁止ssd'})
                    postreturn=requests.post(url,data=jsonfile,headers=headers)
                    c=postreturn.text
                    b=c[34:52]
                    url='https://a1.fanbook.mobi/api/bot/'+lp+'/deleteMessage'#注意令牌
                    headers = {'content-type':"application/json;charset=utf-8"}
                    jsonfile=json.dumps({"chat_id":pd_id,"message_id":me})
                    postreturn=requests.post(url,data=jsonfile,headers=headers)
                    print(postreturn.text)
                else:
                    url='https://a1.fanbook.mobi/api/bot/'+lp+'/sendMessage'#注意令牌
                    headers = {'content-type':"application/json;charset=utf-8"}
                    jsonfile=json.dumps({"chat_id":pd_id,"text":'你的问题有点复杂，请等待人工回答'})
                    postreturn=requests.post(url,data=jsonfile,headers=headers)
                    c=postreturn.text
                    b=c[34:52]
