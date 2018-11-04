# Media Picker

## Media Player

- 게임 등 앱을 사용하고 있을 때 itunes로 음악을 실행할 수 있는 기능 추가시 이용됨
- info.plist에서 Privacy - Media Library Usage Description 설정필요

```swift
// Instantiate a new music player
let myMediaPlayer = MPMusicPlayerApplicationController.applicationQueuePlayer()
// Add a playback queue containing all songs on the device
myMediaPlayer.setQueue(with: MPMediaQuery.songs())
// Start playing from the beginning of the queue
myMediaPlayer.play()

//다른 방법
let mediaItems = MPMediaQuery.songs().items
let mediaCollection = MPMediaItemCollection(items: mediaItems!)
let player = MPMusicPlayerController.systemMusicPlayer
player.setQueue(with: mediaCollection)
player.play()
```



## Media Picker 이용

- 사용자 미디어 라이브러리에서 노래를 선택하는 방법
- mediaQuery를 구분하기 위해서는 MPMediaPropertyPerdicate를 이용하는데 MPMediaItem, MPMediaItemCollection 이용

```swift
class ViewController: UIViewController, MPMediaPickerControllerDelegate {

    //Creates a global instance of the system music player
    var myMediaPlayer = MPMusicPlayerController.systemMusicPlayer
}

@IBAction func chooseSongsButtonPressed(_ sender: UIButton) {
    let myMediaPickerVC = MPMediaPickerController(mediaTypes: MPMediaType.music)
    myMediaPickerVC.allowsPickingMultipleItems = true
    myMediaPickerVC.popoverPresentationController?.sourceView = sender
    myMediaPickerVC.delegate = self
    self.present(myMediaPickerVC, animated: true, completion: nil)
}

func mediaPicker(_ mediaPicker: MPMediaPickerController, didPickMediaItems mediaItemCollection: MPMediaItemCollection) {
    myMediaPlayer.setQueue(with: mediaItemCollection)
    mediaPicker.dismiss(animated: true, completion: nil)
    myMediaPlayer.play()
    
 //모든 음악 가져오기
/*
let mediaSongs = MPMediaQuery.songs().items
let mediaCollection = MPMediaItemCollection(items: mediaSong)
let player = MPMusicPlayerController.systemMusicPlayer
player.setQueue(with: mediaCollection)
player.play()

//노래 하나만 가져오기
let mediaSong = mediaItemCollection.items
let mediaCollection = MPMediaItemCollection(items: mediaSong)
let player = MPMusicPlayerController.systemMusicPlayer
player.setQueue(with: mediaCollection)
player.play()
*/
}

func mediaPickerDidCancel(_ mediaPicker: MPMediaPickerController) {
    mediaPicker.dismiss(animated: true, completion: nil)
}
```



## AVAudioPlayer

- 파일 또는 메모리에서 오디오 데이터를 재생하는 오디오 플레이어
- Media
- 기능
  - init, 재생, 일시정지, 정지 기능을 구현해주어야 함 

```swift
class ViewController: UIViewController{ 
	@IBAction func btnPlay(_ sender: Any) {
        audioPlayer.play()
        setPlayButtons(false, pause: true, stop: true)
        progressTimer = Timer.scheduledTimer(timeInterval: 0.1, target: self, selector: timePlayerSelector, userInfo: nil, repeats: true)
    }
    @IBAction func btnPause(_ sender: Any) {
        audioPlayer.pause()
        setPlayButtons(true, pause: false, stop: true)
    }
    @IBAction func btnStop(_ sender: Any) {
        audioPlayer.stop()
        setPlayButtons(true, pause: true, stop: false)
        audioPlayer.currentTime = 0
        lbCurrent.text = convertNSTimeInterval2String(0)
        progressTimer.invalidate() //타이머 무효화
    }
}
extension ViewController: AVAudioPlayerDelegate{
    //오디오 재생이 끝나면 맨 처음 상태로 돌아가는 함수 추가
    func audioPlayerDidFinishPlaying(_ player: AVAudioPlayer, successfully flag: Bool) {
        progressTimer.invalidate()
        setPlayButtons(true, pause: false, stop: false)
    }
}
```



- Media Picker에서 가져온 내 디바이스의 음악을 재생하기 위해서는 MPMediaItemPropertyAssetURL을 가져와야 함

```swift
class ViewController: UIViewController{
//MPMedia
    @IBAction func btnMediaLibrary(_ sender: Any) {
        mediaPicekr.delegate = self
        mediaPicekr.allowsPickingMultipleItems = false
        mediaPicekr.prompt = "노래선택"
        present(mediaPicekr, animated: true)
    }
}
extension ViewController: MPMediaPickerControllerDelegate{
    func mediaPicker(_ mediaPicker: MPMediaPickerController, didPickMediaItems mediaItemCollection: MPMediaItemCollection) {

        mediaURL = mediaItemCollection.items[0].value(forProperty: MPMediaItemPropertyAssetURL) as! URL

        lbMusicTitle.text = mediaItemCollection.items[0].value(forProperty: MPMediaItemPropertyTitle) as! String
        

        dismiss(animated: true, completion: nil)
    }
    
    func mediaPickerDidCancel(_ mediaPicker: MPMediaPickerController) {
        self.dismiss(animated: true, completion: nil)
    }
}
```



