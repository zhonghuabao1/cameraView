import cv2

class Camera(object):
    def __init__(self, id_):
        try:
            self.cam = cv2.VideoCapture(int(id_))
            print(self.cam)
            frame = self.read()
            assert frame is not None
        except Exception as e:
            print("{}\nFail to open camera {}".format(e, id_))
            self.cam = None

        self.map = {
                'contrast': cv2.CAP_PROP_CONTRAST,
                '对比度': cv2.CAP_PROP_CONTRAST,
                'brightness': cv2.CAP_PROP_BRIGHTNESS,
                '亮度': cv2.CAP_PROP_BRIGHTNESS,
                'exposure': cv2.CAP_PROP_EXPOSURE,
                '曝光时间': cv2.CAP_PROP_EXPOSURE,
                # 'auto_exposure': cv2.CAP_PROP_AUTO_EXPOSURE,
                # '自动曝光': cv2.CAP_PROP_AUTO_EXPOSURE,
        }

    def read(self):
        if self.cam: return self.cam.read()[1]

    def set(self, key, value):
        if self.cam and key in self.map:
            self.cam.set(self.map[key], value)
            print('set %s(%s) -> %s' %(key, self.map[key], value))

    def get(self, key):
        if self.cam and key in self.map:
            return self.cam.get(self.map[key])

    def set_resolution(self, value):
        """ value: string, like 1024x768 """
        if self.cam and 'x' in value:
            w, h = value.split("x")
            self.cam.set(cv2.CAP_PROP_FRAME_WIDTH, int(w))
            self.cam.set(cv2.CAP_PROP_FRAME_HEIGHT, int(h))

    def set_auto_exposure(self, is_auto):
        self.cam.set(cv2.CAP_PROP_AUTO_EXPOSURE, 0.75 if is_auto else 0.25)

def read(f):
    return cv2.imread(f)

def save(f, img):
    cv2.imwrite(f, img)

def resize(img, size=None, r=1.):
    if size:
        return cv2.resize(img, size)
    else:
        return cv2.resize(img, None, None, r)
