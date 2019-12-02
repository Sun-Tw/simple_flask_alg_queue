import os
import time
from multiprocessing import Process
from config.settings import alg_queue,logger


def call_back_request_dmz(result):# 异步requests,推送结果
    # eg requests.get("http://www.flag.com/?flag=True&file_id=111")
    pass

def alg(file_id,file_path):
    time.sleep(5)
    return True,file_id
    
def alg_loop(alg_queue):
    while True:

        file_id,file_path = alg_queue.get()
        logger.info("get ({}, {}) alg is start".format(file_id,file_path))

        result = alg(file_id,file_path)
        call_back_request_dmz(result)
        logger.info("finshed-> file_id: {} ,result: {}".format(file_id,result))

        os.remove(file_path)
        logger.info("del file:{}".format(file_path))


def alg_init_process():
    p = Process(target=alg_loop,args=(alg_queue,))
    p.start()
    return p