from processobj import JavaProcess
from watchutil import checkJavaProcess
from watchutil import sendMsg
import time

def checkXyb2bRun():
  process = JavaProcess()
  xyb2bProcess = process.xyb2bProcesses().module
  process.helperProcess(xyb2bProcess)
  serversConfig= {"10.25.211.163":{"user":"root", "pwd":"k#2IQ9sj"}, "127.0.0.1":{"user":"root", "pwd":"5&vk&M*Y"}}
  lastSendTime = 0 
  while True:
	duration = 0         
	if lastSendTime > 0:
		duration = time.time() - lastSendTime

	noWorkServer = checkJavaProcess(serversConfig, xyb2bProcess)
	if len(noWorkServer) > 0 and duration > 3600:
		for key,v in noWorkServer.items():
			sendRet = sendMsg(key + " " +"".join(v))
			print("#"+sendRet.split(",")[0] + "#" + sendRet.split(",")[1])
			if sendRet.split(",")[1] == "0":
				print(sendRet.split(",")[0] + " send successful" + key + " " + "".join(v))			
				lastSendTime = time.time()
        time.sleep(10)

checkXyb2bRun()
