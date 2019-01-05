# 비동기 방식으로 웹에서 이미지 불러오기

```swift
func getData(from url: URL, completion: @escaping(Data?, URLResponse?, Error?) -> ()){
        URLSession.shared.dataTask(with: url, completionHandler: completion).resume()
    }

func downloadImage(from url: URL){
        getData(from: url) { (data, response, error) in
            guard let data = data, error == nil else { return }
            DispatchQueue.main.async() {
                self.imgProfile.image = UIImage(data: data)
            }
        }
}

override func viewDidLoad(){
    let imgString = "url 주소"
    downloadImage(from: URL(string: imgUrl)!)
}
```

