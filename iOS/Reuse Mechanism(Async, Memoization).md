# 재사용 메커니즘(Reuse Mechanism)

테이블 뷰에서 셀의 수가 많아도 부드러운 스크롤 UI를 구현할 수있음

동작원리

1. 테이블 뷰가 화면에 나타낼 셀 객체를 자신의 데이터 소스에게 요청
2. 데이터 소스는 재사용큐에서 사용 가능한 셀이 있는지 확인
3. 사용 가능한 셀이 있다면 그중 하나를 꺼내 전달, 없으면 새로운 셀 생성
4. tableView(_:cellForRowAt:) 메소드가 셀의 콘텐츠 구성 후 반환(return cell) 하면 테이블 뷰는 셀을 받아 화면에 표시함
5. 테이블 뷰를 스크롤함에 따라 화면을 벗어난 셀은 테이블 뷰에서 제거(완전삭제 아님) => 재사용 큐에 추가됨
6. 사용자의 스크롤에 따라 1~5 과정 반복



#### 네트워크 통신으로 썸네일을 받아올때 

- 문제점: 네트워크로 이미지를 불러오고 -> 셀 콘텐츠를 구성 후 표현하기 => 시간이 오래걸림
- 다음의 프로그래밍 원칙으로 보완
  - 반복적으로 호출되는 메소드의 내부에는 네트워크 통신 등 처리 시간이 긴 로직을 포함하지 않아야 함
  - 네트워크 통신을 통해 읽어온 데이터는 재사용할 수 있도록 캐싱 처리하여 될 수 있으면 네트워크 통신 횟수를 줄이는 것이 좋음(메모이제이션 기법)
  - 네트워크 통신이나 시간이 오래걸리는 코드를 사용할때는 비동기로 처리

```swift
/*
네트워크에서 내려받은 이미지를 MovieVO객체에 담아 self.list 배열에 저장
저장된 이미지는 필요시점에 꺼내 쓰기만 하면 됨
이 방식의 문제점: 초기 로딩시 화면이 지연됨 => 비동기로 해결
*/
//MovieVO.swift
import Foundation
import UIKit //UIImage를 위함

class MovieVO{
    var thumbnail: String? //썸네일 주소
    var title: String?
    var description: String?
    var rating: Double?
    
    //영화 썸네일 이미즈를 담을 UIImage 객체 추가
    var thumbnailImage: UIImage?
}

//ListViewController.swift
//영화 차트 API호출
func callMovieAPI(){
    do{
        for row in movie{
            //웹 상의 이미지를 읽어와 UIImage 객체로 생성
            let url: URL! = URL(string: mvo.thumbnail!)
            let imageData = try! Data(contentsOf: url)
            mvo.thumbnailImage = UIImage(data:imageData)
            
            self.list.append(mvo)
        } 
    }catch{ NSLog("Parse Error") }
}

override func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell{
    cell.thumbnail.image = row.thumbnailImage
    
    return cell
}
```



#### 이미지 비동기 처리하기

- 동기 방식: 차례대로 업무를 처리하며, 이전 업무가 처리되지 않으면 다음으로 넘어가지 않음
- 비동기 방식: 시간이 걸리는 업무는 진행해 둔 채로 기다리는 동안 다른 업무 처리
- 스위프트에서 제공하는 비동기 구현방식
  - 델리게이트 패턴 이용
    - 네트워크 통신 자체에만 국한된 비동기 처리로 NSURLConectionDelegate객체 이용
    - 델리게이트 객체에 이미지 내려받기에 대한 처리를 위임 -> 내려받기가 완료되면 델리게이트 객체가 특정 메소드를 호출하게 하여 메소드 처리
  - 범용 비동기 함수 이용
    - DispatchQueue.main.async()제공
    - 내부적으로 프로세스나 스레드에 직접 접근하지 않고도 비동기 방식으로 처리할 수 있도록 지원
    - Block, GCD(Global Centeral Dispatch, 애플에서 개발한 병렬처리, 스레드 풀에 기반한 비동기 처리기술)를 이용

```swift
//ListViewController.swift
func getThumbnailImage(_ index: Int) -> UIImage{
    //인자값으로 받은 인덱스를 기반으로 해당하는 배열 데이터를 읽어옴
    let mvo = self.list[index]
    
    //메모이제이션: 저장된 이미지가 있으면 그것을 반환하고, 없을 경우 내려받아 저장한 후 반환
    if let savedImage = mvo.thumbnailImage{
        return saveImage
    } else {
        let url: URL! = URL(stirng: mvo.thumbnail!)
        let imageData = try! Data(contentsOf: url)
        mvo.thumbnailImage = UIImage(data:imageData) //UIImage를 MovieVO 객체에 우선 저장
        
        return mvo.thumbnailImage! //저장된 이미지 반환
    }
}

//비동기 처리방식 이용
override func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell{
    let row = self.list[indexPath.row]
    NSLog("호출된 행 번호: \(indexPath.row), 제목:\(row.title!)")
    
    let cell = tableView.dequeueReusableCell(withIdentifier: "ListCell") as! MovieCell
    
    cell.title?.text = row.title
    cell.desc?.text = row.description
    cell.rating?.text = "\(row.rating!)"
    
    //비동기 방식으로 섬네일 이미지를 읽어옴
    /*클로저는 내부 함수에서 사용되는 외부 환경을 계속 유지해 주는 특성을 가지고 있기 때문에 cell객체가 제거되지 않고 계속 유지될 수 있어 비동기함수에서 이용됨(execute)*/
    DispatchQueue.main.async(execute: {
        cell.thumbnail.image = self.getThumbnailImage(indexPath.row)
    })
    
    return cell
}
```

