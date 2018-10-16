# UserDefaults에 Model 저장하기

UserDefaults에 [model] 리스트를 저장하려고 할 때 에러가 생김

> **attempt to insert non-property list object**

커스텀 클래스에 따른 에러 발생

https://developer.apple.com/documentation/foundation/userdefaults

UserDefaults Class Reference 발췌

> A default object must be a property list—that is, an instance of (or for collections, a combination of instances of) [`NSData`](https://developer.apple.com/documentation/foundation/nsdata), [`NSString`](https://developer.apple.com/documentation/foundation/nsstring), [`NSNumber`](https://developer.apple.com/documentation/foundation/nsnumber), [`NSDate`](https://developer.apple.com/documentation/foundation/nsdate), [`NSArray`](https://developer.apple.com/documentation/foundation/nsarray), or [`NSDictionary`](https://developer.apple.com/documentation/foundation/nsdictionary). If you want to store any other type of object, you should typically archive it to create an instance of NSData.

배열 등의 값을 저장하려고 할 때, NSData로 전환이 필요함

1. Model을 NSCoding으로 데이터들이 저장될 수 있도록 코딩, 인코딩 코드를 만든다.
2. 데이터를 Archiver를 이용해 변형 시킨다.
3. 변형시킨 데이터(encodedData)를 UserDefaults에 저장한다.
4. 필요한 곳에서 UserDefaults에 저장된 데이터를 불러오고, UnArchiver로 데이터를 모델로 타입 캐스팅 하여 이용한다.

```swift
//1. Model => NSCoding이 필요함
class AlarmSetModel: NSObject, NSCoding{
   
    
    var title: String?
    var setIdx: Int?
    var swIs: Bool?
    
    init(title: String, setIdx: Int, swIs:Bool){
        self.title = title
        self.setIdx = setIdx
        self.swIs = swIs
    }
    
    //MARK: NSCoding
    required init(coder aDecoder: NSCoder) {
        title = aDecoder.decodeObject(forKey: "title") as? String
        setIdx = aDecoder.decodeObject(forKey: "setIdx") as? Int
        swIs = aDecoder.decodeObject(forKey: "swIs") as? Bool
    }
    
    func encode(with aCoder: NSCoder) {
        aCoder.encode(self.title, forKey: "title")
        aCoder.encode(self.setIdx, forKey: "setIdx")
        aCoder.encode(self.swIs, forKey: "swIs")
    }
    
}


//저장 동작
//2, 3 객체 저장 => NSKeyedArchiver 이용
 @IBAction func addAction(_ sender: UIButton) {
      let data = AlarmSetModel(title: self.addTextField.text!, setIdx: 1, swIs: true)
        let encodedData = NSKeyedArchiver.archivedData(withRootObject: data)
        ud.set(encodedData, forKey: "setalarmlist")
}


//4. 필요한 곳에서 데이터를 모델로 타입 캐스팅한 뒤 사용
override func viewWillAppear(_ animated: Bool) {
        if let data = ud.data(forKey: "setalarmlist"){
            let list = NSKeyedUnarchiver.unarchiveObject(with: data) as? AlarmSetModel
            print("ddddd \(list?.title)")
        }
```

