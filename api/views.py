import os
from . import health_api
from config.settings import alg_queue,video_save_path,logger
from flask import request,jsonify

import uuid
import traceback

@health_api.app_errorhandler(500)
def internal_server_error(e):
    traceback.print_exc()
    logger.warning("flask runtime error:" + traceback.format_exc())
    return jsonify({"msg":"failed"})


@health_api.route('/medicine',methods=['post'])
def view_medicine():
    # recv args
    file_id = request.form.get("file_id")
    file = request.files.get("file")
    logger.info("request file_id is {}".format(file_id))

    # save file
    file_name = file_id + "_" +str(uuid.uuid1()) + ".mp4"
    file_path = video_save_path + "/" +file_name
    file.save(file_path)
    logger.info("file save is ok  file_id:{} - file_path:{}".format(file_id,file_path))

    # put alg work
    alg_args = (file_id,file_path)
    alg_queue.put(alg_args)
    logger.info("put {} is ok".format(alg_args))

    return jsonify({"msg":"success"})



