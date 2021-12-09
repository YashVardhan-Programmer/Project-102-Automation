import cv2
import dropbox
import time
import random

start_time = time.time()

def take_snapshot():
    number = random.randint(0, 100)

    videoCaptureObject = cv2.VideoCapture(0,cv2.CAP_DSHOW)
    result = True

    while (result):
        ret, frame = videoCaptureObject.read()
        img_name = 'img'+str(number)+'.png'
        cv2.imwrite(img_name, frame)
        start_time = time.time
        result = False
    
    return img_name
    print("Snapshot Taken")
    videoCaptureObject.release()
    cv2.destroyAllWindows()

def upload_file(img_name):
    access_token = "0iCq0KczEssAAAAAAAAAAUXkwDW8M7ItNZtEnIvMmAjjiB9Q3pbtPyBPjFFewsBl"

    file = img_name
    fileFrom = file
    fileTo = '/MySecuritySystem/'+(img_name)
    dbx = dropbox.Dropbox(access_token)

    with open(fileFrom, 'rb') as f:
        dbx.files_upload(f.read(), fileTo, mode=dropbox.files.WriteMode.overwrite)
        print("File Uploaded")

def main():
    while (True):
        if ((time.time()-start_time)>=10):
            name = take_snapshot()
            upload_file(name)

main()