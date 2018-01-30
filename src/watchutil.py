import urllib
import urllib2
import ssh
from processobj import JavaProcess
import time

def sendMsg(serverIp):
	data = {"account":"vip-xy168","pswd":"Tch12160","mobile":"18002584703,15012681079,13530893116","msg":serverIp + " was down","extno":""}
	dataUrlencode = urllib.urlencode(data)
	requrl = "http://222.73.117.156/msg/HttpBatchSendSM"
	req = urllib2.Request(url = requrl, data = dataUrlencode)
	res_data = urllib2.urlopen(req)
	res = res_data.read()
	print(res)
	return res
	
def remoteProcess(ip, user, pwd):
	myclient = ssh.SSHClient()
	myclient.set_missing_host_key_policy(ssh.AutoAddPolicy())
	myclient.connect(ip, port=22, username=user, password=pwd)
	stdin, stdout, stderr = myclient.exec_command("jps -v")
	returnLine = stdout.read()
	return returnLine

def connectServer(ip, user, pwd):
	myclient = ssh.SSHClient()
	myclient.set_missing_host_key_policy(ssh.AutoAddPolicy())
	myclient.connect(ip, port=22, username=user,password=pwd)
        return myclient

def checkJavaProcess(serversConfig, javaProcess):
	 noWorkServer = {}
	 for key in serversConfig:
                print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), "###########", key, "#############")
                sshClient = connectServer(key, serversConfig[key]["user"], serversConfig[key]["pwd"])
                stdin, stdout, stderr = sshClient.exec_command("jps -v")
                javaRets = stdout.readlines()
                if len(javaRets) > 0:
			noWorkModuleList = []
                        for module in javaProcess:
				isWork = False;
                                for javaRet in javaRets:
                                    pidAndName = javaRet.split(" ")
                                    if module == pidAndName[1].replace("\n",""):
                                        isWork = True
                                        break;
                                if isWork == False:
					noWorkModuleList.append(module)
                                        print(module + " not working")
                                       # sendRet = sendMsg(key+" "+module)
					#print(sendRet[1])
					#if sendRet[1] == 0:
				#		 sendTime = time()
			if len(noWorkModuleList) > 0:
				noWorkServer[key] = noWorkModuleList
                print( time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), "##############end################")
		return noWorkServer
