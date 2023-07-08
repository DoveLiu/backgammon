import smtplib
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from resource.config import Config


class EmailSender:
    def __init__(self, attach_file_name):
        self.attach_file_name = attach_file_name
        self.recipients = [
            "doveliugit@gmail.com",
            "lp77734@gmail.com",
        ]

    def send_game_file_by_email(self):
        msg = self.__create_message_container()
        smtp = self.__create_smtp_server()
        self.__send_msg_via_smtp_server(msg, smtp)
        smtp.quit()

    def __create_message_container(self) -> MIMEMultipart:
        msg = MIMEMultipart("alternative")
        msg.attach(self.__attach_file(f"./{self.attach_file_name}"))
        msg["Subject"] = "backgammon build "
        msg["From"] = Config.ROBOT_MAIL_ACCOUNT
        msg["To"] = ",".join(self.recipients)
        return msg

    def __attach_file(self, file_path: str) -> MIMEApplication:
        att = MIMEApplication(open(file_path, "rb").read())
        att.add_header("Content-Disposition", "attachment", filename=self.attach_file_name)
        return att

    def __create_smtp_server(self) -> smtplib:
        smtp = smtplib.SMTP("smtp.gmail.com", 587)
        smtp.ehlo()
        smtp.starttls()
        smtp.login(Config.ROBOT_MAIL_ACCOUNT, Config.ROBOT_MAIL_PASSWORD)
        return smtp

    def __send_msg_via_smtp_server(self, msg: MIMEMultipart, smtp: smtplib.SMTP) -> None:
        status = smtp.sendmail(
            from_addr=Config.ROBOT_MAIL_ACCOUNT,
            to_addrs=self.recipients,
            msg=msg.as_string(),
        )
        if status == {}:
            print("Send email successfully!")
        else:
            print("Send email failed!")


if __name__ == "__main__":
    email_sender = EmailSender("Makefile")
    email_sender.send_game_file_by_email()
