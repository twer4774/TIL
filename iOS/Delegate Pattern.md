# 델리게이트 패턴

디자인패턴: 특정한 상황에서 구조적인 문제를 해결하는 방식

- 팩토리, 옵저버, 데코레이터, 싱글톤, 어댑터, 이터레이터, 델리게이트 패턴 등이 있음

## 델리게이트 패턴

처리해야 할 일 중 일부를 다른 객체에 넘기는 것

효율성 관점에서 중요함 => 큰 규모의 프로젝트를 빠르게 작성 가능해짐

## 텍스트 필드

델리게이트 패턴을 사용하는 대표적인 객체

1. 텍스트 필드에 대한 델리게이트 프로토콜 구현 => UITextFieldDelegate
2. 텍스트 필드의 델리게이트 속성을 뷰 컨트롤러에 연결 => self.tf.delegate = self

```swift
class ViewController: UIViewController, UITextFieldDelegate{
    let tf = TextField()
    
    override func viewDidLoad(){
        self.tf.delegate = self //텍스트필드를 위임함
    }
    
    //UITextFieldDelegate 함수들 - 7가지가 정의되어있음
    //텍스트 필드의 편집이 시작된 후 호출
    func textFieldDidBeginEditing(_ textField: UITextField){
        print("텍스트 필드의 편집이 시작되었습니다.")
    }
    //텍스트 필드의 내용이 삭제될 때 호출
    func textFieldShouldClear(_ textField: UITextField) -> Bool{
        print("텍스트 필드의 내용이 삭제됩니다.")
        return true
    }

}
```

## 이미지 피커 컨트롤러

- UIImagePickerController 클래스

  - Photo Library로 전환할때 이용됨
  - UIViewController를 상속받아 실행시 화면을 전환 함
  - 스토리보드로 구성할 수 없으며, 오직 소스코드를 이용해 직접 인스턴스를 생성하고 화면을 호출해야 함
  - 호출 시 present(_:animated:) 이용

  ```swift
  //이미지 피커 컨트롤러 인스턴스 생성
  let picker = UIImagePickerController()
  
  picker.sourceType = .photoLibrary //이미지 소스 선택
  /*
  3가지 옵션
  .photoLibrary 이미지 라이브러리에서 이미지를 선택하는 옵션
  .savedPhotosAlbum 저장된 사진 앨범에서 이미지를 선택하는 옵션
  .camera 		 카메라를 실행하여 즉석에서 사진을 촬영하고, 이를통해 이미지를 생성하는 옵션
  */
  picker.allowsEditing = true //이미지 편집 가능 여부 설정
  picker.delegate = self //델리게이트 지정
  /*
  이미지를 반환받을 대상을 지정. self로 지정하면 자기 자신의 뷰 컨트롤러로 받겠다는 의미
  delegate프로토콜을 준수하기때문에 해당 함수들을 구현해 주어야 함
  */
  
  //이미지 피커 컨트롤러 실행
  self.present(picker, anitmated: false)
  
  //이미지 피커 컨트롤러 종료
  picker.dismiss(animated: false)
  ```

  - 이미지 피커 컨트롤러의 델레이ㅔ이트 메소드
    - imagePickerController(_:didFinishPickingMediaWithInfo:) : 이미지 피커 컨트롤러에서 이미지를 선택하거나 카메라 촬영을 완료했을 때 호출되는 메소드. 
      - 첫번째 인자: 이 메소드를 호출하는 이미지 피커 컨트롤러 객체
      - 두번째 인자: 우리가 원하는 이미지에 대한 데이터
        - UIImagePickerControllerMediaType:  kUTTypeImage, kUTTypeMovie등 미디어 타입 정보
        - UIImagePicekrcontrollerOriginalImage: 원본 이미지 데이터, 이미지가 수정되었더라도 이 키를 이용하면 원본 데이터를 받을 수  있음
        - UIImagePicekrControllerEditedImage: 이미지가 수정된 경우 수정된 이미지 전달
        - UIImagePickerControllerCroprect: 이미지가 크롭(사각형으로 잘라내는 것)된 경우 크롭된 이미지 전달
    - imagePickerControllerDidCancel(_:): 이미지 선택없이 그냥 취소했을 때 호출

## 익스텐션을 이용한 델리게이트 패턴 코딩

```swift
class ViewController: UIViewController{
    
}

//MARK:- 이미지 피커 컨트롤러 델리게이트 메소드
extension ViewController: UIImagePickerControllerDelegate{
    
}

//MARK:- 네비게이션 컨트롤러 델리게이트 메소드
extension ViewController: UINavigationControllerDelegate{
    
}
```

