import cv2
import asyncio
from aiohttp import web
from threading import Thread

from writers.writer import Writer


class VideoServer(Writer):
    def __init__(self, port, pipes, using_pipes):
        self.port = port
        self.frame = None
        self.using_pipes = using_pipes
        self.pipes = pipes
        self.running = True

    def __enter__(self):
        self.frame = None
        Thread(target=self.run_thread).start()
        return self

    def __exit__(self, exit_type, value, traceback):
        self.loop.stop()
        self.running = False

    def write(self, data):
        self.frame = data

    def run_thread(self):
        self.loop = asyncio.new_event_loop()
        asyncio.set_event_loop(self.loop)
        app = web.Application(loop=self.loop)
        app.router.add_get("/", self.index_handler)
        app.router.add_get("/video", self.video_handler)
        app.router.add_get("/change", self.change_handler)
        app.router.add_get("/get_filters", self.filters_handler)
        web.run_app(app, port=self.port, handle_signals=False)

    @asyncio.coroutine
    def video_handler(self, request):
        headers = {'Content-Type': 'multipart/x-mixed-replace; boundary=frame'}
        resp = web.StreamResponse(status=200,
                                  reason='OK',
                                  headers=headers)
        
        # The StreamResponse is a FSM. Enter it with a call to prepare.
        yield from resp.prepare(request)
        
        while self.running:
            try:
                if self.frame is not None:
                    img = cv2.imencode('.jpg', self.frame)[1].tostring()
                else:
                    img = b""
                img_len = str.encode(str(len(img)))
                resp.write(b"--frame\r\n")
                resp.write(b"Content-Type: image/jpeg\r\n")
                resp.write(b"Content-length: " + img_len + b"\r\n\r\n")
                resp.write(img)
                
                # Yield to the scheduler so other processes do stuff.
                yield from resp.drain()
                 
                # Sleep for a bit..
                yield from asyncio.sleep(0.07)
            except Exception as e:
                # So you can observe on disconnects and such.
                print(repr(e))
                raise
        return resp
    
    @asyncio.coroutine
    def index_handler(self, request):
        return web.FileResponse('./web/index.html')

    @asyncio.coroutine
    def change_handler(self, request):
        self.using_pipes.clear()
        self.using_pipes.append([x for x in self.pipes 
                                if x.__class__.__name__ ==
                                request.query["filter"]][0])
        return web.Response()

    @asyncio.coroutine
    def filters_handler(self, request):
        return web.json_response([x.__class__.__name__ for x in self.pipes])
