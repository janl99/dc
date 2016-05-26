from django_cron import CronJobBase,Schedule
import urllib2
import uuid
import json

class HttpNotifyAdapter(object):

    def __init__(self,url,auth_name,auth_password,post_data):
        self.url = url
        self.auth_username = auth_name
        self.auth_password = auth_password
        self.post_data = post_data

    def post_notify(self):
        try:
            #from base64 import encodestring
            req = urllib2.Request(self.url)
            print self.url 
            #if self.auth_username != '':
                #b64str= encodestring('%s:%s' % (self.auth_username,self.auth_passwold))[:-1]
                #req.add_header("Authorization","Basic %s" % b64str)
            f = urllib2.urlopen(req,self.post_data) 
            print f.readline()
        except:
            print 'notify except faild.'


class DataChangedNotifyer(object):
    Max_notify_retry_count = 3

    def __init__(self):
        self.notify_user_list = self.notify_users()

    def notify_users(self):
        users_dic = {}
        a = {"username":"abc","password":"123456","url":"http://192.168.2.182:8077/DataExchangeByjson.ashx","last_notify_data_id":1,"last_notify_time":"2016-05-21 00:00:00","last_notify_failed_count":0}
        users_dic["abc"] = a 
        b = {"username":"def","password":"123456","url":"http://192.168.2.182:8077/DataExchangeByXML.ashx","last_notify_data_id":1,"last_notify_time":"2016-05-21 00:00:00","last_notify_failed_count":0}
        users_dic["def"] = b 

        return users_dic




class DataChangedNotifcationJob(CronJobBase):
    RUN_EVERY_MINS = 1 

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'cronjob.data_changed_notifcation_job'

    def do(self):
        print '--------------this is cronjob.data_changed_notifcation_job doing.----------------------------'

        tmp_data = {}
        #tmp_data["ID"] = uuid.uuid1() 
        tmp_data["Source"] = "datacenter"
        tmp_data["Destination"] = "sqjz"
        tmp_data["CreateTime"] = "2016-05-26 14:35:35"
        tmp_data["Content"] = "test"
        tmp_data["ProtocolType"] = "PT-1"
        tmp_data_str = json.dumps(tmp_data)
        #print tmp_data_str

        users = DataChangedNotifyer().notify_users()
        for k in users:
            #print users[k]["username"]
            #print users[k]["password"]
            #print users[k]["url"]
            #print users[k]["last_notify_data_id"]
            #print users[k]["last_notify_time"]
            #print users[k]["last_notify_failed_count"]
            hna = HttpNotifyAdapter(users[k]["url"],"","",tmp_data_str)
            hna.post_notify()
        print '============================================================================================='




