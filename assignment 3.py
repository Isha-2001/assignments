import logging
ch=0
while(ch!=2):
    mess=input("enter the message : ")
    typ=input("enter the type :w-warning e-erorr c-critical i-info d-debugging : ") 
    logging.basicConfig(filename='app.txt', filemode='a',format='%(asctime)s - %(message)s', level=logging.DEBUG)
    if typ=='w':
        logging.warning(mess)
    elif typ=='d':
        logging.debug(mess)
    elif typ=='i':
        logging.info(mess)
    elif typ=='c':
        logging.critical(mess)
    elif typ=='e':
        logging.error(mess)
    ch=int(input("enter 1 - continue 2- end " ))
