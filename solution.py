from socket import *


def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\n My message"
    endmsg = "\r\n.\r\n"

    # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope

    # Fill in start             *** START ***
    # mailserver = 'smtp.gmail.com'
    serverName = 127.0.0.1
    serverPort = 1025
    # Fill in end               *** END ***

    # Create socket called clientSocket and establish a TCP connection with mailserver and port

    # Fill in start             *** START ***
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect(mailserver)
    # Fill in end               *** END ***

    recv = clientSocket.recv(1024).decode()
    #print(recv) #You can use these print statement to validate return codes from the server.
    #if recv[:3] != '220':
    #    print('220 reply not received from server.')

    # Send HELO command and print server response.
    heloCommand = 'HELO Alice\r\n'
    clientSocket.send(heloCommand.encode())
    recv1 = clientSocket.recv(1024).decode()
    #print(recv1) 
    #if recv1[:3] != '250':
    #    print('250 reply not received from server.')

    # Send MAIL FROM command and handle server response.

    # Fill in start                         ***** START ******
    mail_from = "Mail From:<cc2033@nyu.edu>\r\n"
    clientSocket.send(mail_from)
    recv_from = clientSocket.recv(1024)
    print("MAIL FROM status: "+recv_from.decode())
    # Fill in end                           ***** END ******

    # Send RCPT TO command and handle server response.
    # Fill in start                         ***** START ******
    rcpt_to = "RCPT TO:<cc@gmail.com>\r\n"
    clientSocket.send(rcpt_to)
    recv_to = clientSocket.recv(1024)
    print("RCPT TO command status: "+recv_to.decode())
    # Fill in end                           ***** END ******

    # Send DATA command and handle server response.
    # Fill in start                         ***** START ******
    data = "DATA\r\n"
    clientSocket.send(data)
    recv_data = clientSocket.recv(1024)
    print("SEND DATA command status: "+recv_data.decode())
    # Fill in end                           ***** END ******

    # Send message data.
    # Fill in start                         ***** START ******
    clientSocket.send(msg)

    # Fill in end                           ***** END ******

    # Message ends with a single period, send message end and handle server response.
    # Fill in start                         ***** START ******
    clientSocket.send(endmsg)
    # Fill in end                           ***** END ******

    # Send QUIT command and handle server response.
    # Fill in start                         ***** START ******
    quit = "QUIT\r\n"
    clientSocket.send(quit)
    recv_quit = clientSocket.recv(1024)
    print(recv_quit.decode())
    clientSocket.close()
    exit(0)
    # Fill in end                           ***** END ******


if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')
