# 다른 뷰 컨트롤러와 데이터 주고 받기

## 뷰 컨트롤러를 전환하면서 값 전달

```swift
//인스턴스 생성
guard let vc = self.stroyboard?.instantiateViewController(withIdentifier:"vc2") as? ResultViewCotnroller else{
    return
}

//값 전달
vc.email = self.email.text!
vc.interval = self.interval.value

//화면이동
self.present(vc, animated:true)

//ReusltViewController
//화면 복귀
self.presentingViewController?.dismiss(animated: true)
```



## 네비게이션 컨트롤러를 통해 화면 전환하면서 값 전달하기

프리젠테이션 방법과 같음

```swift
//화면을 전환하는 방법이 다를 뿐
self.navigationController?.pushViewController(vc, animated: true)
```



## 세그웨이를 이용하여 화면 전환하면서 값 전달하기

```swift
//IBAction
@IBAction func onPerformSegue(_ sender: Any){
	self.performSegue(withidentifier: "seg_name", sender: self)    
}
//값을 전달하는 코드 => 전처리메소드에 넣어줌
override func prepare(for segue: UIStoryboardSegue, sender: Any?){
    let dest = segue.destination
    guard let vc = dest as? ResultViewController else {
        return
    }
    
    //값전달
    vc.email = self.email.text!
    vc.interval = self.interval.value
}

```



## 이전 화면으로 값 전달하기

주의할 점: VC1 -> VC2는 값을 잘 전달하지만, VC2 -> VC1은 이전화면으로 복귀하는 것이기 때문에 값이 누락된다.

이런 현상은 viewDidLoad()가 실행되지 않기 때문인데, 화면을 복귀할때는 viewWillAppear()메소드에 원하는 코드를 작성해야한다.

- VC2 -> VC1은 반영구적으로 저장해야 하는 값인 경우가 많음

  - VC2 -> VC1 -> VC2로 전환시, VC2인스턴스해제 후 VC1->VC2에서 새로운 VC2인스턴스가 생성되어 새로운 인스턴스가 생김 => 값을 전달 받은적 없는 새로운 화면


### 직접 값을 주고 받기 -> 휘발성

- viewWillAppear()메소드에 코드작성 => viewWillAppear()은 화면이 보여질때 마다 실행되는 코드

```swift
//VC
override func viewWillAppear(_ animated: Bool){
    if let emial = paramEmail{
        resultEmail.text = email
    }
}

//ResultController
@IBAction func onSubmit(_ sender: Any){
    let preVC = self.presentingViewCotnroller
    guard let vc = preVC as? ViewController else {
        return
    }
    
    //값 전달
    vc.email = self.email.text
    vc.interval = self.interval.value
    
    //화면 복귀
    self.presentingViewController?.dismiss(animated: true)
}
```



### 저장소를 사용하여 값을 주고 받기 => AppDelegate이용

- 비동기 방식

- 주의: 앱이 종료되면 AppDelegate에 저장된 값이 사라짐 => UserDefaults 객체, 코어데이터 객체 이용(반영구적 저장)

```swift
//AppDelegate
//값을 저장할 변수 정의
var email: String?
var interval: Double?

//ResultController
let ad = UIApplication.shared.delegate as? AppDelegate
ad?.email = self.email.text
ad.interval = self.interval.value
self.presentingViewController?.dismiss(animated: true)

//VC
override func viewWillAppear(_ animated: Bool){
	let ad = UIApplication.shared.delegate as? AppDelegate
	if let email = ad?.email{
    	resultEmail.text = email
	}
}
```



### UserDefaults 객체를 사용하여 값을 주고 받기

- 앱을 삭제하기 전까지 저장되는 반영구적인 방법 => 로그인 여부나 간단한 설정 정보 저장

```swift
//ResultController
let ud = UserDefaults.standard
ud.set(self.email.text, forKey:"email")

//VC
let ud = UserDefaults.standard
if let email = ud.string(forKey: "email"){
    resultEmail.text = email
}
```

