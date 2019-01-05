# Alamofire 이미지 업로드

```swift
func imgUpload(a: Int, b: String){
    let parameters = [
    	"A": a,
        "B": b
    ]
    
    let headers = ["Content-type": "multipart/form-data"]
    
    //이미지 압축
    let imgData = self.img.image!.jpegData(compressionQuality: 2.0)!
    Alamofire.upload(multipartFormData: {
        (multipartFormData) in
        //withName은 파라미터로 들어갈 이름
        multipartFormData.append(imgData, withName: "C", fileName: "image.jpg", mimeType: "image/jpg")
        
          for (key, value) in parameters {
    
                multipartFormData.append("\(value)".data(using: String.Encoding(rawValue: String.Encoding.utf8.rawValue))!, withName: key)
                    
                }
    
            },
                 usingThreshold: UInt64.init(),
                 to: apiUrl,
                 method: .post,
                 headers: headers) { (result) in
        switch result {
            case .success(let upload, _, _):

            upload.uploadProgress(closure: { (progress) in
                   print("Upload Progress: \(progress.fractionCompleted)")
		})
            upload.responseJSON(completionHandler: { response in
                print(response.request)  // original URL request

                print(response.response) // URL response

                print(response.data)     // server data                           
					if let JSON = response.result.value {
                            log.info("JSON : \(JSON)")
                           }
                 })
            	break
           case .failure(let error):
            	break
        	}            
		}
    }
}
```

