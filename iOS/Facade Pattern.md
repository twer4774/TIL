# 파사드패턴(facade pattern)

- 어떤 서브 시스템들의 일련된 인터페이스를 통합해 하나의 인터페이스로 제공
- 고수준 인터페이스를 정의하기 때문에 서브 시스템을 더 쉽게 사용할 수 있다.
- 외부에 서브시스템들의 인터페이스를 숨길 수 있다.
- 연관된 API를 한번에 처리할 경우 유용하게 쓰일 수 있다.

## 샘플 코드

- 자동차 엔진, 몸체, 악세사리 만들기

```swift
import Foundation

//각각의 기능들을 가진 클래스 정의
class Engine{
    func produceEngine(){
        print("produce engine")
    }
}

class Body{
    func produceBody(){
        print("produce body")
    }
}

class Accessories{
    func produceAccessories(){
        print("produce accessories")
    }
}


//파사드를 이용해 각 인터페이스를 통합시킨 심플한 인터페이스를 만든다.
class FactoryFacade{
    let engine = Engine()
    let body = Body()
    let accessories = Accessories()
    
    func produceCar(){
        engine.produceEngine()
        body.produceBody()
        accessories.produceAccessories()
    }
}

//파사드를 인터페이스의 인스턴스를 만들어서 사용한다.
let factoryFacade = FactoryFacade()
factoryFacade.produceCar()

//결과
produce engine
produce body
produce accessories
```



- 이미지를 저장하는 파사드 패턴 - 실행되지는 않지만,  파사드 패턴을 설명하는 또 다른 예로 참고할 것

```
enum ImageSaverError: Error{
    case couldNotCreateDestinationPath
    case couldNotCreateJPEGDataFromImage
    case couldNotcreatePNGDataFromImage
    case couldNotSaveImageInDestinationPath
}

enum ImageType{
    case png
    case jpeg(compressionQuality: CGFloat)
}

//이미지데이터를 제공하는 클래스
class ImageDataProvider {
    func data(from image: UIImage, type: ImageType) throws -> Data {
        switch type {
        case .jpeg(let compressionQuality):
            return try jpegData(from: image, compressionQuality: compressionQuality)
        case .png:
            return try pngData(from: image)
        }
    }

    private func pngData(from image: UIImage) throws -> Data {
        guard let imageData = UIImagePNGRepresentation(image) else { throw ImageSaverError.couldNotCreateJPEGDataFromImage }
        return imageData
    }

    private func jpegData(from image: UIImage, compressionQuality: CGFloat) throws -> Data {
        guard let imageData = UIImageJPEGRepresentation(image, compressionQuality) else { throw ImageSaverError.couldNotCreatePNGDataFromImage }
        return imageData
    }
}

//이미지 파일 저장을 위한 클래스
class PathProvider{
    func createDestinationPath(fileName: String) throws -> URL{
        guard let path = FileManager.default.urls(for: .documentDirectory, in: .userDomainMask).first else {
            throw ImageSaverError.couldNotCreateDestinationPath
        }
        let destinationPath = path.appendingPathComponent("\(fileName)")
        return destinationPath
    }
}


//파사드 패턴 이용 - 위의 두 인터페이스를 하나의 간단한 인터페이스로 통합
class ImageSaverFacade{
    private let pathProvider = PathProvider()
    private let dataProvider = ImageDataProvider()
    
    func save(image: UIImage, type: ImageType, fileName: String, overwrite: Bool) throws{
        let destinationURL = try pathProvider.createDestinationPath(fileName: fileName)
        let imageData = try dataProvider.data(from: image,type: type)
        let writingOptions: Data.writingOptions = overwrite ? (.atomic) : (.withoutOverwriting)
        try imageData.write(to: destinationURL, options: writingOptions)
    }
}

//파사드 패턴을 이용해 인스턴스를 생성하고 이미지 저장
let imageSaver = ImageSaverFacade()
let image = UIImage(named: "my_image")!

do {
    try imageSaver.save(image: image, type: .png, fileName: "my_file_name", overwrite: true)
} catch {
    //handle Error
}

do {
    try imageSaver.save(image: image, type: .jpeg(compressionQuality: 1.0), fileName: "my_file_name", overwrite: false)
} catch {
    //handle Error
}
```

