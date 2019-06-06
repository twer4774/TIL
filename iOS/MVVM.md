# MVVM

- 주로 Reactive Programming(ReactivCocoa, RxSwift)에서 이용한다.
- Model, View, ViewModel로 이루어진 디자인 패턴
- View가 기존 iOS의 ViewController 역할을 한다.
- ViewModel은 View와 Model 사이에 위치하여 데이터바인딩을 하는 중간 역할을 수행한다.
  - Model에 변화를 주고, ViewModel을 업데이트하는데 이 바인딩으로 인해 View도 업데이트가 된다.
- ViewModel은 View에 대해 아무것도 모르기 때문에 테스트 하기 쉽다.
- ViewModel은 바인딩을 이용해 View와 통신하기 때문에 코드양이 현저히 줄게 할 수 있어 MVC의 문제인 MassiveViewController를 방지할 수 있다.

```swift
import Foundation

//ViewModel
var gameScore: Int?
var gameScoreLabel: UILabel

func updateGameScoreLabel() {
    var text = ""
    if let gameSocre = gameSocre, gameScore == 100 {
        text = "Excellent!!"
    } else if let gameScore = gameScore, gameSocre >= 90 && gameScore < 100{
        text = "Great Job!"
    } else if let gameScore = gameScore, gameScore < 90 {
        text = "Not Bad~"
    }
    gameScoreLabel.text = text
}

//ViewController
gameScoreLabel.text = viewModel.updateGameScoreLabel

```

