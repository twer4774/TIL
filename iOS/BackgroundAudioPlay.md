# Background Sound Play

- 인터넷에서 플레이되는 sound인 경우 info.plist에서 App Transport Security Settings - Allow Arbitrary Loads - YES 설정해야함
- Capabilities에서 Background Modes - On - Modes - Audio, BackgroundFetch 체크 필요
- http://www.largesound.com/ashborytour/sound/brobob.mp3

```swift
import AVFoundation
//내장되어 있는 오디오 재생 
func innerSoundPlay(){
        let sound = Bundle.main.path(forResource: "audio1", ofType: "mp3")
        
        do{
            audioPlayer = try AVAudioPlayer(contentsOf: URL(fileURLWithPath: sound!))
            audioPlayer.prepareToPlay()
            audioPlayer.play()
            try AVAudioSession.sharedInstance().setCategory(AVAudioSession.Category.playback, mode: AVAudioSession.Mode.default, options: [])
        } catch {
            print(error)
        }
    }

//URL오디오 파일 재생
@IBAction func btnPlay(_ sender: UIButton){
         let sound = URL(string: "http://www.largesound.com/ashborytour/sound/brobob.mp3")
        downloadFileFromURL(url: sound!)
    }

 func downloadFileFromURL(url: URL){
        var downloadTask: URLSessionDownloadTask
        downloadTask = URLSession.shared.downloadTask(with: url, completionHandler: { (URL, response, error) -> Void in
            self.play(url: URL!)
        })
        downloadTask.resume()
    }

  func play(url: URL){
        do {
            self.audioPlayer = try AVAudioPlayer(contentsOf: url)
            audioPlayer.stop()
            audioPlayer.prepareToPlay()
            audioPlayer.volume = 1.0
            audioPlayer.play()
            
            try AVAudioSession.sharedInstance().setCategory(AVAudioSession.Category.playback, mode: AVAudioSession.Mode.default, options: [])
            
        } catch let error as NSError {
            
            print(error.localizedDescription)
        } catch {
            print("AVAudioPlayer init failed")
        }
    }
```

- 커맨드 센터 제어

```swift
import MediaPlayer //커맨드센터 컨트롤을 위함
override func viewDidLoad(){
       UIApplication.shared.beginReceivingRemoteControlEvents()
        let commandCenter = MPRemoteCommandCenter.shared()
        commandCenter.playCommand.isEnabled = true
        commandCenter.pauseCommand.isEnabled = true

        
        commandCenter.pauseCommand.addTarget { (event) -> MPRemoteCommandHandlerStatus in
            self.audioPlayer.pause()
            return .success
        }
        
        commandCenter.playCommand.addTarget { (event) -> MPRemoteCommandHandlerStatus in
            self.audioPlayer.play()
            return .success
        }
}
```



## Streaming Play

- 스트리밍 서비스를 위해서는 AVPlayer 사용

```swift
 var player: AVPlayer! //주의 사항 - viewDidLoad()의 위쪽에 선언할 것 -> 함수 내부에 선언 시에 실행안됨

func streamingPlay(url: URL){
        do{
        player = AVPlayer.init(url: url)
        player.volume = 1.0
        player.play()
        
        try AVAudioSession.sharedInstance().setCategory(AVAudioSession.Category.playback, mode: AVAudioSession.Mode.default, options: [])
        } catch {
            print(error)
        }
        
    }
```



## AVAudioPlayer VS AVPlayer

- AVPlayer: 로컬 저장된 파일뿐만 아니라 스트리밍을 재생을 위해서도 사용
- AVAudioPlayer: 로컬에 저장된 오디오 파일의 재생 기능만 제공