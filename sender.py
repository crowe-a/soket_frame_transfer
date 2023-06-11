import socket
import cv2 as cv
import cv2
cap = cv2.VideoCapture(0)
#fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
#out = cv2.VideoWriter('output.mp4', fourcc, 25, (640, 480), isColor=True)
while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, (640, 480))


    retval, buf = cv.imencode(".JPEG", frame)
    # get number of bytes
    number_of_bytes = len(buf)
    # create a null terminated string
    header = "" + str(number_of_bytes) + "\0"
    # encode it to utf-8 byte format
    raw_header = bytes(header, "utf-8")

    
    # create server socket
    sock = socket.socket()
    sock.bind(('localhost', 1234))
    sock.listen()
    conn, addr = sock.accept()
    # send header first, reciever will use it to recieve image
    conn.send(raw_header)
    # send the rest of image
    conn.send(buf)










cap.release()
#out.release()
cv2.destroyAllWindows()

# # read a test image
# #img = cv.imread('C:/Users/darkr/Desktop/yarışmaya gidiyoruz/soket frame trasnfer/hasarlı.jpg')
# # encode it to jpg format, you can do this without redundant file openings
# retval, buf = cv.imencode(".JPEG", frame)
# # get number of bytes
# number_of_bytes = len(buf)
# # create a null terminated string
# header = "" + str(number_of_bytes) + "\0"
# # encode it to utf-8 byte format
# raw_header = bytes(header, "utf-8")
# # create server socket
# sock = socket.socket()
# sock.bind(('localhost', 1234))
# sock.listen()
# conn, addr = sock.accept()
# # send header first, reciever will use it to recieve image
# conn.send(raw_header)
# # send the rest of image
# conn.send(buf)