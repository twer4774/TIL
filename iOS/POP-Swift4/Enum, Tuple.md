# 열거형, 튜플

## 열거형

```swift
//일반적인 열거형
enum Devices{
    case IPod
    case IPhone
    case IPad
}

//스위프트 열거형 - 원시값으로 불리는 값을 할당할 수 있음
enum Devices:String{
    case IPod = "iPod"
    case IPhone = "iPhone"
    case IPad = "iPad"
}
//사용 - rawValue
Devices.IPod.rawValue

//연관값으로 재정의
enum Devices{
    case IPod(model: Int, year: Int, memory: Int)
    case IPhone(model: String, memory: Int)
    case IPad(model: String, memory: Int)
}
//사용
var myPhone = Devices.Iphone(model: "6", memory: 64)
var myTablet = Devices.IPad(model: "Pro", memory: 128)
//연관값 가져오기
switch myPhone{
    case .IPod(let model, let year, let memory):
	    print("iPod: \(model) \(memory)")
    case .IPhone(let model, let memory):
    	print("iPhone: \(model) \(memory)")
    case .IPad(let model, let memory):
    	print("iPad: \(model) \(memory)")
}

```

- 열거형에서 메소드와 연산 프로퍼티를 사용할 수 있는 방법

```swift
enum Reindeer: String{
    case Dasher, Dancer, Prancer, Vixen, Comet, Cupid, Donner, Blitzen, Rudolph 
    static var allCases: [Reindeer]{
        return [Dasher, Dancer, Prancer, Vixen, Comet, Cupid, Donner, Blitzen, Rudolph]
    }
    
    static func randomCase() -> Reindeer{
        let randomValue = Int(
            arc4random_uniform(
            UInt32(allCases.count)
            )
        )
        return allCase[randomValue]
    }
}
```

- 기능들과 함께 사용하는 열거형

```swift
enum BookFormat{
    case PaperBack (pageCount: Int, price: Double)
    case HardCover (pageCount: Int, price: Double)
    case PDF (pageCount: Int, price: Double)
    case EPub (pageCount: Int, price: Double)
    case Kindle (pageCount: Int, price: Double)
    
    //연산프로퍼티 사용
    var pageCount: Int{
        switch self{
            case .PaperBack(let pageCount, _):
            	return pageCount
           	case .HardCover(let pageCount, _):
            	return pageCount
            case .PDF(let pageCount, _):
            	return pageCount
            case .EPub(let pageCount, _):
            	return pageCount
            case .Kindle(let pageCount, _):
            	return pageCount
        }
    }
    
    var price: Double{
        switch self{
            case .PaperBack(_, let price):
            	return price
           	case .HardCover(_, let price):
            	return price
            case .PDF(_, let price):
            	return price
            case .EPub(_, let price):
            	return price
            case .Kindle(_, let price):
            	return price
        }
    }
    
    //여러권을 살 경우 20%할인
    func purchaseTogether(otherFormat: BookFormat) -> Double{
        return (self.price + otherFormat.price) * 0.80
    }
}
//사용
var paperBack = BookFormat.PaperBack(pageCount: 220, price: 39.99)
print("\(paperBack.pageCount) - \(paperBack.price)")

var pdf = BookFormat.PDF(pageCount: 180, price: 14.99)
var total = paperBack.purchaseTogether(otherFormat: pdf)
//total = 43.98400000000001
```



## 튜플

```swift
let mathGrade1 = ("Jon", 100)
let (name, score) = mathGrade1
print("\(name) - \(score)") //Jon - 100

let mathGrade2 = (name: "Jon", grade: 100)
print("\(mathGrade2.name) - \(mathGrade2.grade)")

func calculateTip(billAmount: Double, tipPercent: Double) -> (tipAmount: Double, totalAmout: Double){
    let tip = billAmount * (tipPercent/100)
    let total = billAmount + tipPercent
    return (tipAmount: tip, totalAmout: total)
}

//사용
var tip = calculateTip(billAmount:31.98, tipPercent: 20)
print("\(tip.tipAmount) - \(tip.totalAmout)")
//6.396000000000001 - 51.980000000000004
```

