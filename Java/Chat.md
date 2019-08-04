# Chat

## 1. 단일 챗 

### Server

```java
package Networking;

import java.net.*;
import java.io.*;
import java.util.Scanner;

public class TcpIpServer5SenderReceiver {

    public static void main(String[] args) {
        ServerSocket serverSocket = null;
        Socket socket = null;

        try {
            //소켓을 생성하여 7777번 포트와 바인딩한다.
            serverSocket = new ServerSocket(7777);
            System.out.println("서버가 준비되었습니다.");

             socket = serverSocket.accept();

            Sender sender = new Sender(socket);
            Receiver receiver = new Receiver(socket);

            sender.start();
            receiver.start();

        } catch (IOException e) {
            e.printStackTrace();
        }
    }//main

}

class Sender extends Thread{
  Socket socket;
  DataOutputStream out;
  String name;

  Sender(Socket socket){
      this.socket = socket;
      try{
          out = new DataOutputStream(socket.getOutputStream());
          name = "["+socket.getInetAddress()+":"+socket.getPort()+"]";
      } catch (Exception e){

      }//catch
  }//Sender

    public void run() {
      Scanner scanner = new Scanner(System.in);
      while(out!=null){
          try{
              out.writeUTF(name+scanner.nextLine());
          } catch(IOException e){

          } //catch
      }
    }
} //class Sender

class Receiver extends Thread {
    Socket socket;
    DataInputStream in;

    Receiver(Socket socket) {
        this.socket = socket;
        try{
            in = new DataInputStream(socket.getInputStream());
        } catch (IOException e) {

        }//catch
    }

    public void run() {
        while(in!=null){
            try{
                System.out.println(in.readUTF());
            } catch(IOException e){

            }//catch
        }//while
    }
}//class Receiver

//결과
서버가 준비되었습니다.
hello
[/127.0.0.1:7777]hihi
```

### Client

```java
package Networking;

import java.net.*;
import java.io.*;

public class TcpIpClient5 {
    public static void main(String[] args) {
        try {
            String serverIp = "127.0.0.1";
            //소켓을 생성하여 연결을 요청한다.
            Socket socket = new Socket(serverIp, 7777);

            System.out.println("서버에 연결되었습니다.");
            Sender sender = new Sender(socket);
            Receiver receiver = new Receiver(socket);

            sender.start();
            receiver.start();
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
서버에 연결되었습니다.
[/127.0.0.1:53127]hello
hihi
```

## 2. 멀티 챗

### Server

```java
package Networking;

import java.net.*;
import java.io.*;
import java.util.*;

public class TcpIpMultiChatServer {
    HashMap clients;

    TcpIpMultiChatServer(){
        clients = new HashMap();
        Collections.synchronizedMap(clients);
    }//TcpIpMultiChatServer

    public void start(){
        ServerSocket serverSocket = null;
        Socket socket = null;

        try{
            serverSocket = new ServerSocket(7777);
            System.out.println("서버가 시작되었습니다.");

            while(true){
                socket = serverSocket.accept();
                System.out.println("["+socket.getInetAddress()+":"+socket.getPort()+"]"+"에서 접속하였습니다.");
                ServerReceiver thread = new ServerReceiver(socket);
                thread.start();
            } //while
        } catch (Exception e){
            e.printStackTrace();
        }//catch
    } //start

    void sendToAll(String msg){
        Iterator it = clients.keySet().iterator();

        while (it.hasNext()) {
            try{
                DataOutputStream out = (DataOutputStream) clients.get(it.next());
                out.writeUTF(msg);
            } catch (IOException e){

            }
        }//while
    }//sendToAll

    public static void main(String[] args) {
        new TcpIpMultiChatServer().start();
    }//main

    //Inner class
    class ServerReceiver extends Thread {
        Socket socket;
        DataInputStream in;
        DataOutputStream out;

        ServerReceiver(Socket socket){
            this.socket = socket;
            try{
                in = new DataInputStream(socket.getInputStream());
                out = new DataOutputStream(socket.getOutputStream());
            } catch(IOException e){

            }//catch
        }//ServerReceiver

        public void run(){
            String name = "";

            try{
                name = in.readUTF();
                sendToAll("#" + name + "님이 들어오셨습니다.");

                clients.put(name, out);
                System.out.println("현재 서버 접속자수는 " + clients.size() + "입니다.");

                while(in!=null){
                    sendToAll(in.readUTF());
                }
            } catch (IOException e){
                //ignore
            } finally {
                sendToAll("#" + name + "님이 나가셨습니다.");
                clients.remove(name);
                System.out.println("["+socket.getInetAddress()+":"+socket.getPort()+"]"+"에서 접속을 종료하였습니다.");
                System.out.println("현재 서버접속자 수는 " + clients.size() +"입니다.");
            }
        }//run
    }//class ServerReceiver extends Thread

}
```

### Client

```java
package Networking;

import java.net.*;
import java.io.*;
import java.util.Scanner;

public class TcpIpMultiChatClient {
    public static void main(String[] args) {
        if (args.length != 1) {
            System.out.println("USAGE: java TcpIpMultiChatClient 대화명");
            System.exit(0);
        }

        try {
            String serverIp = "127.0.0.1";

            //소켓을 생성하여 연결을 요청한다.
            Socket socket = new Socket(serverIp, 7777);
            System.out.println("서버에 연결되었습니다.");
            Thread sender = new Thread(new ClientSender(socket, args[0]));
            Thread receiver = new Thread(new ClientReceiver(socket));

            sender.start();
            receiver.start();
        } catch (ConnectException ce){
            ce.printStackTrace();
        } catch (Exception e){
            e.printStackTrace();
        }
    }//main

    static class ClientSender extends Thread {
        Socket socket;
        DataOutputStream out;
        String name;

        ClientSender(Socket socket, String name) {
            this.socket = socket;

            try{
                out = new DataOutputStream(socket.getOutputStream());
                this.name = name;
            } catch (Exception e) {

            } //catch
        }// CleintSender

        public void run(){
            Scanner scanner = new Scanner(System.in);
            try{
                if (out != null) {
                    out.writeUTF(name);
                }

                while(out!=null){
                    out.writeUTF("["+name+"]"+scanner.nextLine());
                } //while
            } catch (IOException e){

            }//catch
        }//run
    }//class ClientSender extends Thread

    static class ClientReceiver extends Thread{
        Socket socket;
        DataInputStream in;

        ClientReceiver(Socket socket){
            this.socket = socket;
            try{
                in = new DataInputStream(socket.getInputStream());
            } catch (IOException e) {
            }
        }//ClientReceiver

        public void run(){
            while (in != null) {
                try{
                    System.out.println(in.readUTF());
                } catch(IOException e){

                }
            }//while
        }//run
    }//class ClientReceiver extends Thread

}
```

### 결과

```java
//서버
➜  src java Networking.TcpIpMultiChatServer
서버가 시작되었습니다.
[/127.0.0.1:53372]에서 접속하였습니다.
현재 서버 접속자수는 1입니다.
[/127.0.0.1:53377]에서 접속하였습니다.
현재 서버 접속자수는 2입니다.
  
//Client1
➜  src java Networking.TcpIpMultiChatClient aaa
서버에 연결되었습니다.
#bbb님이 들어오셨습니다.
hihi
[aaa]hihi
[bbb]반가워요

//Client2
 ➜  src java Networking.TcpIpMultiChatClient bbb
서버에 연결되었습니다.
[aaa]hihi
 반가워요
[bbb]반가워요
```

