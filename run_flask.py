import sys
from alg.alg_entrance import alg_init_process
from config.core import create_app,cleanup_app

if __name__ == "__main__":
    assert( len(sys.argv) <= 2 )
    if len(sys.argv) == 1:
        port = 9000
    else:
        port = int(sys.argv[1])

    ip = "0.0.0.0"
    debug_model = False

    p = alg_init_process()
    app = create_app()

    try:
        app.run(host=ip,port=port,debug=debug_model,threaded=True)
    finally:
        p.terminate()
        p.join()


