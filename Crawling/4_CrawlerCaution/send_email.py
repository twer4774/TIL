import smtplib
from email.mime.text import MIMEText
from email.header import Header

#MIMEText 객체로 메일을 생성함
msg = MIMEText('메일 본문')


#제목에 한글이 포함될 경우 Header객체 사용
msg['Subject'] = Header('메일 제목', 'utf-8')
msg['From'] = 'twer4774@gmail.com'
msg['To'] = 'twer4774@gmail.com'

#Gmail말고 다른 메일일때 사용
#SMTP() 첫번재 매개변수에 SMTP 서버의 호스트 이름을 지정
# with smtplib.SMTP('localhost') as smtp:
#     #메일 전송
#     smtp.send_message(msg)

#Gmail일 경우 사용
#TLS/SLL클래스 이용
with smtplib.SMTP_SSL('smtp.gmail.com') as smtp:
    #구글 계정의 사용자 이름과 비밀번호르 지정해서 로그인
    #2단계 인증을 설정한 경우 애플리케이션 비밀번호 사용
    smtp.login('twer4774@gmail.com', 'knwmuxdvtqcaesnn')

    #send_message()메서드로 메일 전송
    smtp.send_message(msg)