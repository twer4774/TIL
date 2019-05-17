# Print VS NSLog

print() 함수와 NSLog() 함수는 모두 콘솔에 출력하는 기능을 갖는다.

<https://riptutorial.com/swift/example/30983/print-vs-nslog>

## 차이점

1. TimeStamp

   - NSLog()는 타임스탬프가 같이 콘솔창에 출력된다.

   - print()는 타임스탬프가 출력되지 않는다.

     ```swift
     //print()
     [1, 2, 3, 4, 5]
     
     //NSLog()
     2017-05-31 13:14:38.582 ProjetName[2286:7473287] [1, 2, 3, 4, 5]
     ```

     

2. Only String

   - NSLog()는 String타입 객체만 넣을 수 있다.
   - print()는 상관없이 넣을 수 있다.

   ```swift
   let array = [1, 2, 3, 4, 5]
   print(array) // [1, 2, 3, 4, 5]
   NSLog(array) // error: Cannot convert value of type [Int] to expected argument type 'String'
   ```

3. Performance

   - NSLog()는 print()에 비해 매우 느리다

4. Synchroization

   - NSLog()는 Multi-threading 환경에서 사용가능하다.
   - NSLog()는 Multi-threading에서 중복되는 값 없이 출력한다.
   - print()는 중복되는 값을 출력하므로, 혼란을 줄 수 있다.

5. Device Console 

   - NSLog()는 디바이스 콘솔도 출력 가능하다. => 기기를 연결한뒤 동작하면 콘솔이 뜬다.
   - print()는 디바이스 콘솔을 볼 수 없다.