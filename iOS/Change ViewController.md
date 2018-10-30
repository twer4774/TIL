# 화면전환방법

1. 뷰 컨트롤러 위에 다른 뷰 가져와 바꿔치기하기 => 컨테이너 뷰 컨트롤러
2. 뷰 컨트롤러에서 다른 뷰 컨틀로러 호출하여 화면 전환하기
3. 네비게이션 컨트롤러를 사용하여 화면 전환하기
4. 화면 전환용 객체 세그웨이(Segueway) 사용하여 화면 전환하기



## 뷰 컨트롤러 직접 호출에 의한 화면 전환

프레젠테이션 방식

```swift
//새로운 뷰 컨트롤러 불러오기
present(<새로운 뷰컨트롤러 인스턴스>, animated:(true or false), completion:(클로저등을 이용해 비동기함수실행))
//사용 예
let vc = self.storyboard!.instantiateViewController(withIdentifier: "SecondVC")
vc.modalTransitionStyle = UIModalTransitionStyle.coverVertical
self.present(vc, animated:true)

//기존 화면으로 돌아가기
dismiss(animated:completion:)
//사용예
self.presentingViewController?.dismiss(animated: true)
```

- 화면을 덮는 방식
- 뷰컨트롤러 A를 그대로 둔 뒤, 뷰 컨트롤러 B로 화면을 덮는 방식



## 네비게이션 컨트롤러를 이용한 화면전환

```swift
//화면 전환
navigationcontroller.pushViewController(_:animated:)

//돌아가기
navigationcontorller.popViewController(animated:)
```



## 세그웨이를 이용한 화면 전환

- 메뉴얼 세그웨이(Manual Segue)
  - 출발점이 뷰 컨트롤러 자체인 경우
  - performSegue(withIdentifier:sender:) 이용
  - 조건에 따라 이동하는 페이지를 바꿀 때 이용
- 액션 세그웨이(Action Segue), 트리거 세그웨이(Trigger Segue)
  - 출발점이 버튼인 경우
  - 자동으로 화면 전환이 이루어짐
  - 조건 여부와 관계없이 클릭 시 무조건 특정 페이지로 이동

## Unwind - 화면 복귀

세그웨이를 이용한 화면 복귀는 사용하면 안됨 => 계속해서 뷰를 쌓는 것이됨

- dismiss, popViewController를 이용하여 화면 복귀 
- 도크 바의 Exit를 이용해 이전 화면으로 복귀
  - 뷰 컨트롤러 A에 UIStoryboardSegue타입의 인자를 받는 @IBAction액션 메소드 정의
    이때, 버튼과 연결할 필요는 없음
  - 뷰 컨트롤러 B에 버튼을 만들고 Exit아이콘에 드래그 => 트리거 생성
  - 드래그 된 Exit아이콘은 뷰 컨트롤러 A에서 생성된 메소드를 인식하고 Unwind Segue로 자동 생성



## 전처리 메소드 이용 => prepare()

- 코드를 통한 전환 방식
- 프로그래머가 선호하는 방식
- 난이도는 높지만 코드와 상황을 임의로 제어해 자유도가 높음

- 전처리 메소드는 화면이 전환되기 직전에 먼저 실행됨

```swift
override func tableView(_ tableView: UITableView, didSelectRowAt indexPath: IndexPath){
//prepare 동작 시키는 코드
    self.performSegue(withIdentifier: "segue_detail", sender: self)
}
extension ListViewController{
    override func prepare(for segue: UIStoryboardSege, sender: Any?){
        //실행된 세그웨이의 식별자가 "segue_detail"이라면
        if segue.identifier == "segue_detail"{
            //sender 인자를 캐시통하여 테이블 셀 객체로 변환
            let cell = sender as! MovieCell
            
            //사용자가 클릭한 행을 찾아낸다.
            let path = self.tableView.indexPath(for: cell)
            
            //API영화 데이터 배열 중에서 선택된 행에 대한 데이터를 추출한다.
            let movieInfo = self.list[path!.row]
            
            //행 정보를 통해 선택된 영화 데이터를 찾은 다음, 목적지 뷰 컨트롤러의 mvo변수에 대입한다.
            let detailVC = segue.destination as? DetailViewController
            detailVC?.mvo = movieInfo
        }
    }
}
```

