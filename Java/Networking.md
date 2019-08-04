# Networking

- 두대 이상의 컴퓨터를 케이블로 연결하여 네크워클 구성하는 것

### 클라이언트/서버

- 서버 : 서비스를 제공하는 컴퓨터
  - 파일서버, 메일서버, 어플리케이션 서버 등이 있다.
  - 서버기반모델(server-based model)
    - 안정적인 서비스의 제공 가능
    - 공유 데이터의 관리와 보안이 용이
    - 서버구축비용과 관리비용 필요
  - P2P모델(peer-to-peer model)
    - 서버구축 및 운용비용 절감
    - 자원의 활용 극대화
    - 자원 관리가 어려움
    - 보안 취약
- 클라이언트 : 서비스를 사용하는 컴퓨터

### IP주소(IP address)

- host를 구별하는데 사용되는 고유한 값으로 인터넷에 여결된 모든 컴퓨터는 IP주소를 갖는다.
- IP주소는 4byte(32bit)로 나누어져 있다.

```java
package Networking;

import java.net.*;
import java.util.*;

public class NetworkEx1 {
    public static void main(String[] args) {
        InetAddress ip = null;
        InetAddress[] ipArr = null;

        try{
            ip = InetAddress.getByName("www.naver.com");
            System.out.println("getHostName() :"+ip.getHostName());
            System.out.println("getHostAddress() :"+ip.getHostAddress());
            System.out.println("toString() :"+ip.toString());

            byte[] ipAddr = ip.getAddress();
            System.out.println("getAddress() :"+Arrays.toString(ipAddr));

            String result =  "";
            for (int i = 0; i < ipAddr.length; i++) {
                result += (ipAddr[i] < 0) ? ipAddr[i] + 256 : ipAddr[i];
                result += ".";
            }//for
            System.out.println("getAddress() + 256 :"+result);
            System.out.println();
        } catch (UnknownHostException e){
            e.printStackTrace();
        } //catch

        try {
            ip = InetAddress.getLocalHost();
            System.out.println("getHostName() :"+ip.getHostName());
            System.out.println("getHostAddress() :"+ip.getHostAddress());
            System.out.println();
        } catch (UnknownHostException e){
            e.printStackTrace();
        }//catch

        try {
            ipArr = InetAddress.getAllByName("www.naver.com");

            for (int i = 0; i < ipArr.length; i++) {
                System.out.println("ipArr["+i+"] :" + ipArr[i]);
            }//for
        } catch (UnknownHostException e) {
            e.printStackTrace();
        }
    }//main
}

```

### URL(Uniform Resource Locator)

- 인터넷에 존재하는 여러 서버들이 제공하는 자원에 접근할 수 있는 주소를 표현
- 프로토콜://호스트명:포트번호/경로명/파일명?쿼리스트링#참조 형태
  - 프로토콜: 자원에 접근하기 위해 서버와 통신하는데 사용하는 통신규약
  - 호스트명: 자원을 제공하는 서버의 이름
  - 포트번호: 통신에 사용되는 포트번호
  - 경로명: 접근하려는 자원이 저장된 서버상의 위치
  - 파일명: 접근하려는 자원의 이름
  - 쿼리: URL에서 '?'이후의 부분
  - 참조: URL에서 '#'이후의 부분
- java에서 URLConnection을 이용해 어플리케이션과 URL간의 통신 연결을 할 수 있다.

```java
package Networking;

import java.net.*;

public class NetworkEx3 {
    public static void main(String[] args) {
        URL url = null;
        String address = "http://www.codechobo.com/sample/hello.html";

        try{
            url = new URL(address);
            URLConnection conn = url.openConnection();

            System.out.println("conn.toString():"+conn);
            System.out.println("getAllowUserInteraction():"+conn.getAllowUserInteraction());
            System.out.println("getConnectTimeout():"+conn.getConnectTimeout());
            System.out.println("getContent():"+conn.getContent());
            System.out.println("getHeaderFields():"+conn.getHeaderFields());
            System.out.println("getURL():"+conn.getURL());
        } catch (Exception e) {
            e.printStackTrace();
        }
    }//main
}
```

- URL에 연결하여 내용을 읽어오는 예제. 만일 URL이 유효하지 않으면 Malformed-URLException이 발생한다.

```java
package Networking;

import java.net.*;
import java.io.*;

public class NetworkEx4 {
    public static void main(String[] args) {
        URL url = null;
        BufferedReader input = null;
        String address = "https://github.com/twer4774/TIL/blob/master/Java/Lambda.md";
        String line = "";

        try{
            url = new URL(address);
            input = new BufferedReader(new InputStreamReader(url.openStream()));

            while ((line = input.readLine()) != null) {
                System.out.println(line);
            }//while
        } catch(Exception e){
            e.printStackTrace();
        }
    }//main
}
```



## 소켓 프로그래밍

### TCP와 UDP

- TCP
  - 연결기반 1:1 통신
  - 데이터의 경계를 구분안함
  - 신뢰성 있는 데이터 전송
    - 데이터의 전송순서가 보장됨
    - 데이터의 수신여부를 확인함
    - 데이터손실시 재전송
    - 패킷을 관리할 필요가 없음
  - UDP보다 느림
  - 관련 클래스
    - Socket
    - ServerSocket
- UDP
  - 비연결기반 1:1, 1:n, n:n 통신
  - 데이터의 경계 구분(datagram)
  - 신뢰성없는 데이터전송
    - 데이터의 전송순서가 바뀔 수 있음
    - 데이터의 수신여부 확인 안함
    - 패킷관리 필요
  - TCP보다 빠름
  - 관련 클래스
    - DatagramSocket
    - DatagramPacket
    - MulticastSocket

### TCP소켓 프로그래밍

- 통신과정

  1. 서버는 특정 포트에서 클라이언트의 연결요청을 처리할 준비를 한다.
  2. 클라이언트는 접속할 서버의 IP주소와 포트 정보를 가지고 소켓을 생성해서 서버에 연결을 요청한다.
  3. 서버소켓은 클라이언트의 요청을 받으면 서버에 새로운 소켓을 생성해서 클라이언트의 소켓과 연결되도록 한다.
  4. 서버와 클라이언트 간의 1:1 통신을 한다.

  - TCP Server

  ```java
  package Networking;
  
  import java.net.*;
  import java.io.*;
  import java.util.Date;
  import java.text.SimpleDateFormat;
  
  public class TcpIPServer {
      public static void main(String[] args) {
          ServerSocket serverSocket = null;
  
          try{
              //서버 소켓을 생성하여 7777번 포트와 bind(결합)한다.
              serverSocket = new ServerSocket(7777);
              System.out.println(getTime()+"서버가 준비되었습니다.");
          } catch (IOException e) {
              e.printStackTrace();
          }
  
          while(true){
              try{
                  System.out.println(getTime()+"연결요청을 기다립니다.");
                  //서버소켓은 클라이언트의 연결요청이 올대까지 실행을 멈추고 계속 기다린다.
                  //클라이언트의 연결요청이 오면 클라이언트 소켓과 통신할 새로운 소켓을 생성한다.
                  Socket socket= serverSocket.accept();
                  System.out.println(getTime()+socket.getInetAddress()+"로부터 연결요청이 들어왔습니다.");
  
                  //소켓의 출력스트림을 얻는다.
                  OutputStream out = socket. getOutputStream();
                  DataOutputStream dos = new DataOutputStream(out);
  
                  //원격소켓(remote socket)에 데이터를 보낸다.
                  dos.writeUTF("[Notice] Test Message1 form Server.");
                  System.out.println(getTime() + "데이터를 전송했습니다.");
  
                  //스트림과 소켓을 닫아준다.
                  dos.close();
                  socket.close();
              } catch(IOException e){
                  e.printStackTrace();
              }
  
          }//while
      }//main
  
      //현재시간을 문자열로 반환하는 함수
      static String getTime(){
          SimpleDateFormat f = new SimpleDateFormat("[hh:mm:ss]");
          return f.format(new Date());
      }
  }
  
  //결과
  [09:39:31]서버가 준비되었습니다.
  [09:39:31]연결요청을 기다립니다.
  [09:39:36]/127.0.0.1로부터 연결요청이 들어왔습니다.
  [09:39:36]데이터를 전송했습니다.
  [09:39:36]연결요청을 기다립니다.
  ```

  - TCP Client

  ```java
  package Networking;
  
  import java.net.*;
  import java.io.*;
  
  public class TcpIpClient {
      public static void main(String[] args) {
          try {
              String serverIp = "127.0.0.1";
  
              System.out.println("서버에 연결중입니다. 서버 IP :" + serverIp);
              //소켓을 생성하여 연결을 요청한다.
              Socket socket = new Socket(serverIp, 7777);
  
              //소켓의 입력 스트림을 얻는다.
              InputStream in = socket.getInputStream();
              DataInputStream dis = new DataInputStream(in);
  
              //소켓으로 받은 데이터를 출력한다.
              System.out.println("서버로부터 받은 메시지 :" + dis.readUTF());
              System.out.println("연결을 종료합니다.");
  
              //스트림과 소켓을 닫는다.
              dis.close();
              socket.close();
              System.out.println("연결이 종료되었습니다.");
  
          } catch (ConnectException ce) {
              ce.printStackTrace();
          } catch (IOException ie) {
              ie.printStackTrace();
          } catch (Exception e){
              e.printStackTrace();
          }
      }//main
  }
  
  //결과
  서버에 연결중입니다. 서버 IP :127.0.0.1
  서버로부터 받은 메시지 :[Notice] Test Message1 form Server.
  연결을 종료합니다.
  연결이 종료되었습니다.
  ```

  

## UDP

- DatagramSocket과 DatagramPacket 사용
- 헤더와 데이터로 구성되어 있으며, 헤더에는 호스트의 정보(주소, 포트)가 저장되어있다.

### Server

```java
package Networking;

import java.net.*;
import java.io.*;
import java.util.Date;
import java.text.SimpleDateFormat;

public class UdpServer {
    public void start() throws IOException{
        DatagramSocket socket = new DatagramSocket(7777);
        DatagramPacket inPacket, outPacket;

        byte[] inMsg = new byte[10];
        byte[] outMsg;

        while(true){
            //데이터를 수신하기 위한 패킷 생성
            inPacket = new DatagramPacket(inMsg, inMsg.length);

            //패킷을 통해 데이터를 수신(receive)
            socket.receive(inPacket);

            //수신한 패킷으로부터 client의 IP주소와 Port를 얻는다.
            InetAddress address = inPacket.getAddress();
            int port = inPacket.getPort();

            //서버의 현재시간을 시분초 형태로 변환한다.
            SimpleDateFormat sdf = new SimpleDateFormat("[hh:mm:ss]");
            String time = sdf.format(new Date());
            outMsg = time.getBytes(); //time을 byte배열로 변환

            //패킷을 생성해서 cleint에게 전송
            outPacket = new DatagramPacket(outMsg, outMsg.length, address, port);
            socket.send(outPacket);
        }//while
    }//start

    public static void main(String[] args) {
        try{
            //UDP서버를 실행시킨다.
            new UdpServer().start();
        } catch(IOException e){
            e.printStackTrace();
        }
    }//main
}

```



### Client

```java
package Networking;

import java.net.*;
import java.io.*;

public class UdpClient {

    public void start() throws IOException, UnknownHostException {
        DatagramSocket datagramSocket = new DatagramSocket();
        InetAddress serverAddress = InetAddress.getByName("127.0.0.1");

        //데이터가 저장될 공간으로 byte배열 생성
        byte[] msg = new byte[100];

        DatagramPacket outPacket = new DatagramPacket((msg), 1, serverAddress, 7777);
        DatagramPacket inPacket = new DatagramPacket(msg, msg.length);

        datagramSocket.send(outPacket); //송신
        datagramSocket.receive(inPacket); //수신

        System.out.println("current serve time: " + new String(inPacket.getData()));

        datagramSocket.close();
    }

    public static void main(String[] args) {
        try {
            new UdpClient().start();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }//main
}

//결과
➜  src java Networking.UdpClient
current serve time: [11:52:28]
```

