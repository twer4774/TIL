# 스토리보드 전환방법

## 같은 스토리보드 뷰로 전환되는 경우

```swift
let storyboard: UIStroyborad = self.storyboard!
let nextView = storyboard.instantiateViewController(withIdentifier: "nextView")
self.present(nextView, animated: true, completion: nil)
```



## 다른 스토리보드 뷰로 전환되는 경우

- Storyboard Reference를 이용해 여러개의 스토리보드로 나눌 때 쓰임

```swift
let storyboard: UIStoryboard = UIStoryboard(name: "Main", bundle: nil)
let nextView = storyboard.instantiateInitialViewController()
self.present(nextView!, animated: true, completion: nil)
```

